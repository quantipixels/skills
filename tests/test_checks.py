"""Exercise the opt-in hook against real staged packages in a disposable repo."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CheckEntryPointTests(unittest.TestCase):
    def test_missing_uv_has_an_actionable_message(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {**os.environ, "PATH": directory}
            result = subprocess.run(["/bin/sh", str(ROOT / "scripts/check.sh")],
                                    env=env, capture_output=True, text=True, timeout=10)
            self.assertEqual(127, result.returncode)
            self.assertIn("uv is required", result.stderr)
            self.assertIn("rerun npm run check", result.stderr)


class StagedHookTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="qp-hooks-")
        self.addCleanup(self.temporary.cleanup)
        base = Path(self.temporary.name)
        self.repo = base / "repo"
        self.repo.mkdir()
        self.env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        self.env.update(HOME=str(base / "home"), GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_CONFIG_NOSYSTEM="1")
        self.git("init", "-q")
        for relative in ("scripts/check.sh", "scripts/check.py", "scripts/install-hooks.sh",
                         "scripts/hooks/pre-commit", "scripts/skills/check_package.py",
                         "requirements-dev.txt"):
            destination = self.repo / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)
        self.skill = self.repo / "skills/example/SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.valid = "---\nname: example\ndescription: A usable skill\n---\nDo the work.\n"
        self.invalid = self.valid.replace("name: example", "name: wrong")
        self.skill.write_text(self.valid)
        for folder, manifest in ((".codex-plugin", '{"name":"qp-skills","skills":"./skills/"}'),
                                 (".claude-plugin", '{"name":"qp-skills"}')):
            (self.repo / folder).mkdir()
            (self.repo / folder / "plugin.json").write_text(manifest)
        self.git("add", ".")
        # Keep dependency setup out of the fixture's HOME. Run the real validator
        # with this suite's uv Python, which already has requirements-dev.txt.
        binary = base / "bin"
        binary.mkdir()
        uv = binary / "uv"
        uv.write_text(f"#!{sys.executable}\nimport os, sys\nposition = sys.argv.index('python')\nos.execv(sys.executable, [sys.executable, *sys.argv[position + 1:]])\n")
        uv.chmod(0o755)
        self.env["PATH"] = str(binary) + os.pathsep + self.env["PATH"]

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              check=True, capture_output=True, text=True, timeout=10)

    def hook(self):
        return subprocess.run(["sh", "scripts/hooks/pre-commit"], cwd=self.repo,
                              env=self.env, capture_output=True, text=True, timeout=20)

    def test_hook_validates_the_index_and_preserves_unstaged_edits(self):
        self.skill.write_text(self.invalid)
        result = self.hook()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(self.invalid, self.skill.read_text())
        self.git("add", "skills")
        self.skill.write_text(self.valid)
        result = self.hook()
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn("name does not match directory", result.stderr)
        self.assertEqual(self.valid, self.skill.read_text())
        self.assertEqual(self.invalid, self.git("show", ":skills/example/SKILL.md").stdout)

    def test_non_skill_changes_skip_validation(self):
        self.git("rm", "--cached", "skills/example/SKILL.md")
        self.skill.write_text(self.invalid)
        result = self.hook()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("", result.stdout)

    def test_install_is_explicit_and_preserves_custom_hook_configuration(self):
        before = subprocess.run(["git", "config", "--get", "core.hooksPath"],
                                cwd=self.repo, env=self.env, capture_output=True, text=True)
        self.assertEqual(1, before.returncode)
        result = subprocess.run(["sh", "scripts/install-hooks.sh"], cwd=self.repo,
                                env=self.env, capture_output=True, text=True, timeout=10)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("scripts/hooks", self.git("config", "--get", "core.hooksPath").stdout.strip())
        self.git("config", "core.hooksPath", "custom-hooks")
        result = subprocess.run(["sh", "scripts/install-hooks.sh"], cwd=self.repo,
                                env=self.env, capture_output=True, text=True, timeout=10)
        self.assertEqual(1, result.returncode)
        self.assertIn("leaving it unchanged", result.stderr)
        self.assertEqual("custom-hooks", self.git("config", "--get", "core.hooksPath").stdout.strip())


if __name__ == "__main__":
    unittest.main()

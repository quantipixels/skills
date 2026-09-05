import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "uninstall.sh"


class UninstallSmokeTest(unittest.TestCase):

    def run_uninstall(self, lock, malformed=False, action="remove"):

        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        home = Path(tmp.name) / "home"
        agents = home / ".agents"
        agents.mkdir(parents=True)
        lock_path = agents / ".skill-lock.json"
        if malformed:
            lock_path.write_text("{not json")
        else:
            lock_path.write_text(json.dumps(lock))

        bin_dir = Path(tmp.name) / "bin"
        bin_dir.mkdir()
        log = Path(tmp.name) / "npx.log"
        stub = bin_dir / "npx"
        stub.write_text(
            """#!/usr/bin/env bash
set -euo pipefail
printf '%s\\n' \"$*\" >> \"$NPX_LOG\"

if [[ \"${REMOVAL_ACTION:-remove}\" == fail ]]; then exit 17; fi
if [[ \"${REMOVAL_ACTION:-remove}\" == noop ]]; then exit 0; fi

python3 - \"$HOME/.agents/.skill-lock.json\" \"$@\" <<'PY'
import json
from pathlib import Path
import sys
lock_path = Path(sys.argv[1])
args = sys.argv[2:]
lock = json.loads(lock_path.read_text())
try:
    start = args.index('--yes') + 1
except ValueError:
    raise SystemExit('missing --yes')
for name in args[start:]:
    lock.get('skills', {}).pop(name, None)
lock_path.write_text(json.dumps(lock))
PY
"""
        )
        stub.chmod(0o755)
        env = os.environ.copy()
        env["HOME"] = str(home)
        env["NPX_LOG"] = str(log)

        env["REMOVAL_ACTION"] = action

        env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
        result = subprocess.run(
            ["bash", str(SCRIPT)],
            cwd=REPO_ROOT,
            env=env,
            text=True,
            capture_output=True,

            timeout=10,

        )
        return result, lock_path, log

    def test_removes_only_qp_owned_global_skills(self):
        lock = {
            "skills": {
                "qp-one": {"source": "quantipixels/skills"},
                "qp-two": {"source": "https://github.com/quantipixels/skills.git"},
                "qp-three": {"source": "git@github.com:quantipixels/skills.git"},
                "other": {"source": "someone/else"},
            }
        }
        result, lock_path, log = self.run_uninstall(lock)
        self.assertEqual(result.returncode, 0, result.stderr)
        remaining = json.loads(lock_path.read_text())["skills"]
        self.assertEqual(set(remaining), {"other"})
        invocation = log.read_text()
        self.assertIn("skills remove --global --yes", invocation)
        self.assertIn("qp-one", invocation)
        self.assertIn("qp-two", invocation)
        self.assertIn("qp-three", invocation)
        self.assertNotIn("other", invocation)

    def test_no_qp_skills_is_a_noop(self):
        result, _, log = self.run_uninstall({"skills": {"other": {"source": "someone/else"}}})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No globally installed QP skills found.", result.stdout)
        self.assertFalse(log.exists())

    def test_malformed_lock_fails_closed_without_removal(self):
        result, _, log = self.run_uninstall({}, malformed=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Could not read the global skills lock", result.stderr)
        self.assertFalse(log.exists())



    def test_malformed_schema_fails_without_calling_native_removal(self):
        for lock in ([], None, {"skills": []}, {"skills": None},
                     {"skills": {"alaga": None}}, {"skills": {"alaga": {"source": 3}}}):
            with self.subTest(lock=lock):
                result, _, log = self.run_uninstall(lock)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(log.exists())

    def test_unsafe_names_never_cross_native_removal_boundary(self):
        for name in ("*", "--all", "alaga\nother", "a b", "../other", "Alaga", "a" * 65):
            with self.subTest(name=name):
                lock = {"skills": {name: {"source": "quantipixels/skills"},
                                   "other": {"source": "someone/else"}}}
                result, target, log = self.run_uninstall(lock)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(log.exists())
                self.assertEqual(json.loads(target.read_text()), lock)

    def test_native_failure_is_not_reported_as_removal(self):
        result, target, _ = self.run_uninstall(
            {"skills": {"alaga": {"source": "quantipixels/skills"}}}, action="fail")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("alaga", json.loads(target.read_text())["skills"])
        self.assertNotIn("All globally installed", result.stdout)

    def test_native_success_without_removal_fails_readback(self):
        result, target, _ = self.run_uninstall(
            {"skills": {"alaga": {"source": "quantipixels/skills"}}}, action="noop")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Removal incomplete", result.stderr)
        self.assertIn("alaga", json.loads(target.read_text())["skills"])


if __name__ == "__main__":
    unittest.main()

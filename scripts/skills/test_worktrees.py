"""Run the bundled tool against real Git repositories and disposable worktrees."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[2] / "skills/system-cleanup/scripts/worktrees.py"


class WorktreeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="qp-worktrees-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.root = self.base / "checkouts"
        self.repo = self.root / "main checkout"
        self.repo.mkdir(parents=True)
        self.env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        self.env.update(HOME=str(self.base / "home"), GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
        self.git("init", "-q", "-b", "ori")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "tracked.txt").write_text("base\n")
        self.git("add", ".")
        self.git("commit", "-qm", "base")
        remote = self.base / "remote.git"
        subprocess.run(["git", "init", "--bare", "-q", "-b", "ori", str(remote)], env=self.env, check=True)
        self.git("remote", "add", "origin", remote)
        self.git("push", "-q", "-u", "origin", "ori")
        self.git("remote", "set-head", "origin", "ori")
        self.binary = self.base / "bin"
        self.binary.mkdir()
        # Fault injection for lsof only: all checkout discovery and Git operations are real.
        lsof = self.binary / "lsof"
        lsof.write_text(f'''#!{sys.executable}
import os, pathlib, sys
counter = pathlib.Path(os.environ["FIXTURE_LSOF_COUNT"])
count = int(counter.read_text()) + 1 if counter.exists() else 1
counter.write_text(str(count))
mode = os.environ.get("FIXTURE_LSOF_MODE", "clear")
if mode == "dirty-on-recheck" and count == 2:
    (pathlib.Path(sys.argv[sys.argv.index("+D") + 1]) / "new untracked.txt").write_text("keep me")
if mode == "open" or (mode == "open-on-recheck" and count == 2):
    print("p123")
    sys.exit(0)
if mode == "unknown":
    print("cannot inspect directory", file=sys.stderr)
sys.exit(1)
''')
        lsof.chmod(0o755)
        self.env.update(PATH=str(self.binary) + os.pathsep + self.env["PATH"],
                        FIXTURE_LSOF_COUNT=str(self.base / "lsof-count"))

    def git(self, *args, checkout=None):
        return subprocess.run(["git", "-C", str(checkout or self.repo), *map(str, args)],
                              env=self.env, check=True, capture_output=True, text=True, timeout=10)

    def worktree(self, name):
        path = self.root / name
        self.git("worktree", "add", "-q", "-b", name.replace(" ", "-"), path)
        return path

    def run_tool(self, *options, roots=None):
        result = subprocess.run([sys.executable, str(TOOL), *map(str, roots or [self.root]), *options],
                                cwd=self.base, env=self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        return json.loads(result.stdout) if "--json" in options else result.stdout

    def test_head_only_counts_and_shared_stashes_with_nested_repositories(self):
        safe = self.worktree("safe tree")
        unique = self.worktree("unique tree")
        (unique / "tracked.txt").write_text("local commit\n")
        self.git("commit", "-qam", "local", checkout=unique)
        (self.repo / "tracked.txt").write_text("stash\n")
        self.git("stash", "push", "-qm", "saved")
        nested = self.repo / "nested"
        nested.mkdir()
        self.git("init", "-q", checkout=nested)
        before = self.git("worktree", "list", "--porcelain").stdout
        report = self.run_tool("--json", roots=[self.root, self.repo])
        rows = {row["path"]: row for row in report["checkouts"]}
        self.assertEqual(4, len(rows))
        self.assertEqual("safe", rows[str(safe)]["classification"])
        self.assertEqual(0, rows[str(safe)]["commits_off_remotes"])
        self.assertTrue(rows[str(safe)]["merged_into_remote_default"])
        self.assertEqual("unique", rows[str(unique)]["classification"])
        self.assertEqual(1, rows[str(unique)]["commits_off_remotes"])
        self.assertFalse(rows[str(unique)]["merged_into_remote_default"])
        self.assertEqual("keep", rows[str(self.repo)]["classification"])
        self.assertEqual(1, sum(repo["stashes"] or 0 for repo in report["repositories"]))
        self.assertGreater(rows[str(safe)]["size_bytes"], 0)
        self.assertEqual(before, self.git("worktree", "list", "--porcelain").stdout)
        self.assertTrue(safe.exists())
        table = self.run_tool()
        self.assertIn("| Path | Kind | Class |", table)
        self.assertIn("| Repository | Shared stashes |", table)

    def test_remove_safe_preserves_branches_main_and_unique_files(self):
        safe = self.worktree("safe")
        dirty = self.worktree("dirty")
        untracked = self.worktree("untracked")
        ignored = self.worktree("ignored")
        (dirty / "tracked.txt").write_text("local edit\n")
        (untracked / "keep.txt").write_text("local file\n")
        (self.repo / ".git/info/exclude").write_text(".env\n")
        (ignored / ".env").write_text("private local data\n")
        report = self.run_tool("--json", "--remove-safe")
        self.assertEqual([str(safe)], report["removal"]["removed"])
        self.assertFalse(safe.exists())
        self.assertTrue(self.repo.exists())
        self.assertEqual("local edit\n", (dirty / "tracked.txt").read_text())
        self.assertEqual("local file\n", (untracked / "keep.txt").read_text())
        self.assertEqual("private local data\n", (ignored / ".env").read_text())
        self.git("show-ref", "--verify", "refs/heads/safe")

    def test_open_or_inconclusive_lsof_keeps_worktrees(self):
        tree = self.worktree("busy")
        for mode in ("open", "unknown"):
            with self.subTest(mode=mode):
                self.env["FIXTURE_LSOF_MODE"] = mode
                report = self.run_tool("--json", "--remove-safe")
                self.assertEqual([], report["removal"]["removed"])
                self.assertTrue(tree.exists())
                row = next(row for row in report["checkouts"] if row["path"] == str(tree))
                self.assertEqual("keep", row["classification"])

    def test_recheck_catches_new_open_files_and_git_rejects_new_dirt(self):
        for mode in ("open-on-recheck", "dirty-on-recheck"):
            with self.subTest(mode=mode):
                tree = self.worktree(mode)
                self.env["FIXTURE_LSOF_MODE"] = mode
                (self.base / "lsof-count").unlink(missing_ok=True)
                # Search exactly this worktree to make the recheck the second lsof call.
                report = self.run_tool("--json", "--remove-safe", roots=[tree])
                self.assertEqual("safe", report["checkouts"][0]["classification"])
                self.assertEqual([], report["removal"]["removed"])
                self.assertEqual(1, len(report["removal"]["skipped"]))
                self.assertTrue(tree.exists())

    def test_pushed_feature_can_be_safe_without_being_merged_and_locked_tree_is_kept(self):
        tree = self.worktree("feature")
        (tree / "tracked.txt").write_text("pushed\n")
        self.git("commit", "-qam", "feature", checkout=tree)
        self.git("push", "-q", "origin", "feature", checkout=tree)
        report = self.run_tool("--json", roots=[tree])
        self.assertEqual("safe", report["checkouts"][0]["classification"])
        self.assertFalse(report["checkouts"][0]["merged_into_remote_default"])
        self.git("worktree", "lock", tree)
        report = self.run_tool("--json", "--remove-safe", roots=[tree])
        self.assertEqual([], report["removal"]["removed"])
        self.assertTrue(tree.exists())

    @unittest.skipUnless(shutil.which("lsof"), "lsof is not installed")
    def test_real_lsof_detects_an_open_file(self):
        tree = self.worktree("real-open")
        self.env["PATH"] = os.environ["PATH"]
        with (tree / "tracked.txt").open() as handle:
            report = self.run_tool("--json", "--remove-safe", roots=[tree])
            self.assertEqual([], report["removal"]["removed"])
            self.assertTrue(report["checkouts"][0]["open_files"])
            self.assertEqual("base\n", handle.read())


if __name__ == "__main__":
    unittest.main()

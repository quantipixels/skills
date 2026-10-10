"""Prove shared working records survive removal of a real disposable worktree."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HELPER = Path(__file__).resolve().parents[1] / "skills/alarina/scripts/qp_records.py"


class QpRecordsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="qp-records-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.repo = self.base / "main checkout"
        self.repo.mkdir()
        self.home = self.base / "temporary home"
        self.home.mkdir()
        self.env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        self.env.update(HOME=str(self.home), GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_CONFIG_NOSYSTEM="1")
        self.git("init", "-q")
        self.git("config", "user.name", "Records fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "tracked.txt").write_text("fixture\n")
        self.git("add", "tracked.txt")
        self.git("commit", "-qm", "Fixture baseline")
        self.git("remote", "add", "origin", "git@example.invalid:sample-owner/sample-repo.git")
        self.exclude = self.repo / ".git/info/exclude"
        self.exclude.write_text("# Preserve existing rules\nscratch")
        self.expected = self.home / ".qp/sample-owner/sample-repo"

    def git(self, *args, checkout=None):
        return subprocess.run(["git", "-C", str(checkout or self.repo), *map(str, args)],
                              env=self.env, check=True, capture_output=True,
                              text=True, timeout=10)

    def ensure(self, checkout=None, status=0):
        result = subprocess.run([sys.executable, str(HELPER), str(checkout or self.repo)],
                                env=self.env, capture_output=True, text=True, timeout=10)
        self.assertEqual(status, result.returncode, result.stdout + result.stderr)
        return Path(result.stdout.strip()) if status == 0 else result.stderr

    def worktree(self, name):
        path = self.base / name
        self.git("worktree", "add", "-q", "--detach", path)
        return path

    def test_records_survive_worktree_removal_and_reach_a_new_worktree(self):
        other = self.worktree("first worktree")
        self.assertEqual(self.expected, self.ensure())
        self.assertEqual(self.expected, self.ensure(other))
        for checkout in (self.repo, other):
            self.assertTrue((checkout / ".qp").is_symlink())
            self.assertEqual(self.expected, (checkout / ".qp").resolve())
            exclude = self.git("rev-parse", "--path-format=absolute", "--git-path",
                               "info/exclude", checkout=checkout).stdout.strip()
            self.assertEqual(self.exclude, Path(exclude))
        record = other / ".qp/plans/feature.md"
        record.parent.mkdir()
        record.write_text("Keep this plan after the checkout is gone.\n")
        saved = self.expected / "plans/feature.md"
        self.assertEqual(saved.read_text(), (self.repo / ".qp/plans/feature.md").read_text())
        for checkout in (self.repo, other):
            self.assertEqual("", self.git("status", "--porcelain", "--untracked-files=all",
                                         checkout=checkout).stdout)
        self.git("worktree", "remove", other)
        self.assertFalse(other.exists())
        self.assertEqual("Keep this plan after the checkout is gone.\n", saved.read_text())
        replacement = self.worktree("replacement worktree")
        self.assertEqual(self.expected, self.ensure(replacement))
        self.assertEqual(saved.read_text(), (replacement / ".qp/plans/feature.md").read_text())
        for checkout in (self.repo, replacement):
            self.assertEqual("", self.git("status", "--porcelain", "--untracked-files=all",
                                         checkout=checkout).stdout)
            self.assertFalse((checkout / ".gitignore").exists())
        self.assertEqual("# Preserve existing rules\nscratch\n.qp\n", self.exclude.read_text())

    def test_remote_formats_and_nested_namespaces(self):
        cases = (
            ("https://example.invalid/sample-owner/sample-repo.git", self.expected),
            ("ssh://git@example.invalid:2222/sample-owner/sample-repo.git", self.expected),
            ("git@example.invalid:sample-owner/sample-repo.git", self.expected),
            ("https://example.invalid/group/subgroup/repo.git",
             self.home / ".qp/group/subgroup/repo"),
        )
        for remote, expected in cases:
            with self.subTest(remote=remote):
                self.git("remote", "set-url", "origin", remote)
                self.assertEqual(expected, self.ensure())
                self.assertEqual(expected, (self.repo / ".qp").resolve())

    def test_no_remote_uses_the_main_checkout_identity_in_every_worktree(self):
        self.git("remote", "remove", "origin")
        other = self.worktree("different folder")
        home = self.ensure(other)
        self.assertEqual(home, self.ensure())
        self.assertEqual(self.home / ".qp/local", home.parent)
        self.assertRegex(home.name, r"^main-checkout-[0-9a-f]{8}$")

    def test_non_origin_remote_and_local_remote(self):
        self.git("remote", "rename", "origin", "upstream")
        self.assertEqual(self.expected, self.ensure())
        local = self.base / "local-owner/local-repo.git"
        self.git("remote", "set-url", "upstream", str(local))
        self.assertEqual(self.home / ".qp/local-owner/local-repo", self.ensure())

    def test_repeated_calls_and_broken_links_preserve_records_and_excludes(self):
        self.ensure()
        saved = self.expected / "report.txt"
        saved.write_text("saved\n")
        self.ensure()
        (self.repo / ".qp").unlink()
        (self.repo / ".qp").symlink_to(self.base / "missing home")
        self.assertEqual(self.expected, self.ensure())
        self.assertEqual("saved\n", (self.repo / ".qp/report.txt").read_text())
        self.assertEqual(1, self.exclude.read_text().splitlines().count(".qp"))

    def test_existing_dot_qp_data_is_never_replaced(self):
        link = self.repo / ".qp"
        link.mkdir()
        record = link / "keep.txt"
        record.write_text("existing data\n")
        error = self.ensure(status=1)
        self.assertIn("refusing to replace existing data", error)
        self.assertFalse(link.is_symlink())
        self.assertEqual("existing data\n", record.read_text())
        self.assertFalse(self.expected.exists())
        self.assertEqual("# Preserve existing rules\nscratch", self.exclude.read_text())

    def test_remote_path_cannot_escape_records_home(self):
        self.git("remote", "set-url", "origin", "https://example.invalid/owner/../escape.git")
        self.assertIn("safe owner/repo path", self.ensure(status=1))
        self.assertFalse((self.home / ".qp").exists())
        self.assertFalse((self.repo / ".qp").is_symlink())

    def test_records_home_inside_a_checkout_is_rejected(self):
        self.env["HOME"] = str(self.repo)
        self.assertIn("outside every checkout", self.ensure(status=1))
        self.assertFalse((self.repo / ".qp").exists())


if __name__ == "__main__":
    unittest.main()

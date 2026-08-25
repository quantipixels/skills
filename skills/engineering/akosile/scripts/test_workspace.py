import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).with_name("workspace.py")
spec = importlib.util.spec_from_file_location("akosile_workspace", MODULE_PATH)
workspace = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(workspace)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        workspace.init_workspace(self.repo)

    def tearDown(self):
        self.tmp.cleanup()

    def record_text(self, revision=1, status="Draft", candidate="repo@abc", updated_at="2026-08-25T10:00:00+01:00"):
        return (
            "---\n"
            "owner: atona\n"
            "record_type: initiative-plan\n"
            "title: Demo\n"
            f"updated_at: {updated_at}\n"
            f"revision: {revision}\n"
            f"candidate: {candidate}\n"
            f"status: {status}\n"
            "---\n\n# Demo\n"
        )

    def write_current(self, record_id="20260825-demo", revision=1, updated_at="2026-08-25T10:00:00+01:00"):
        path = self.repo / ".qp/records/atona" / record_id / "record.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.record_text(revision=revision, updated_at=updated_at), encoding="utf-8")
        return path

    def test_init_is_idempotent_and_preserves_settings(self):
        settings = self.repo / ".qp/settings.json"
        settings.write_text('{"se-triage": {"labels": {"confirmed": "Confirmed defect"}}}\n', encoding="utf-8")
        before = settings.read_text()
        result = workspace.init_workspace(self.repo)
        self.assertEqual(settings.read_text(), before)
        self.assertTrue((self.repo / ".qp/INDEX.md").exists())
        self.assertEqual(result["workspace"], str((self.repo / ".qp").resolve()))
        self.assertEqual(result["workspace_path"], ".qp")

    def test_workspace_root_resolves_git_toplevel_from_subdirectory(self):
        nested = self.repo / "a" / "b"
        nested.mkdir(parents=True)
        completed = subprocess.CompletedProcess(["git"], 0, f"{self.repo}\n", "")
        with patch.object(workspace.subprocess, "run", return_value=completed):
            self.assertEqual(workspace.workspace_root(nested), self.repo / ".qp")
            self.assertEqual(workspace.workspace_path(nested, self.repo / ".qp"), ".qp")

    def test_resolve_reuses_candidate_and_returns_direct_access_paths(self):
        path = self.write_current()
        result = workspace.resolve_record(self.repo, "atona", "other-title", candidate="repo@abc")
        self.assertEqual(result["bundle"], str(path.parent))
        self.assertEqual(result["absolute_path"], str(path.parent.resolve()))
        self.assertTrue(result["workspace_path"].startswith(".qp/records/atona/"))

        created = workspace.resolve_record(self.repo, "solution-architect", "new-design", create=True)
        self.assertIn(".qp/records/solution-architect/", created["workspace_path"])

        artifact = workspace.resolve_artifact(self.repo, "comparison", create=True)
        self.assertTrue(artifact["absolute_path"].endswith("/index.html"))
        self.assertTrue(artifact["workspace_path"].startswith(".qp/artifacts/"))
        self.assertTrue(artifact["workspace_path"].endswith("/index.html"))

    def test_write_record_rejects_invalid_and_stale_candidates(self):
        current = self.write_current()
        original = current.read_text()
        invalid = self.repo / "invalid.md"
        invalid.write_text(original.replace("revision: 1", "revision: 2").replace("status: Draft\n", ""), encoding="utf-8")
        with self.assertRaises(ValueError):
            workspace.write_record(self.repo, current, invalid, workspace.digest(current))
        self.assertEqual(current.read_text(), original)

        valid = self.repo / "valid.md"
        valid.write_text(original.replace("revision: 1", "revision: 2"), encoding="utf-8")
        with self.assertRaises(ValueError):
            workspace.write_record(self.repo, current, valid, "wrong")
        result = workspace.write_record(self.repo, current, valid, workspace.digest(current))
        self.assertEqual(result["revision"], 2)
        self.assertEqual(result["absolute_path"], str(current.resolve()))
        self.assertEqual(result["workspace_path"], ".qp/records/atona/20260825-demo/record.md")
        self.assertIn("Demo", (self.repo / ".qp/INDEX.md").read_text())

    def test_settings_write_preserves_user_shape_and_requires_current_digest(self):
        settings = self.repo / ".qp/settings.json"
        candidate = self.repo / "settings-candidate.json"
        candidate.write_text(json.dumps({"se-triage": {"labels": {"confirmed": "Confirmed defect"}}}), encoding="utf-8")
        with self.assertRaises(ValueError):
            workspace.write_settings(self.repo, candidate, "wrong")
        result = workspace.write_settings(self.repo, candidate, workspace.digest(settings))
        self.assertEqual(json.loads(settings.read_text())["se-triage"]["labels"]["confirmed"], "Confirmed defect")
        self.assertEqual(result["workspace_path"], ".qp/settings.json")

    def test_settings_write_rechecks_digest_immediately_before_write(self):
        settings = self.repo / ".qp/settings.json"
        candidate = self.repo / "settings-candidate.json"
        candidate.write_text('{"x": 1}', encoding="utf-8")
        expected = workspace.digest(settings)
        real_digest = workspace.digest
        calls = 0

        def changed_digest(path):
            nonlocal calls
            calls += 1
            if path == settings and calls >= 2:
                return "concurrent-change"
            return real_digest(path)

        with patch.object(workspace, "digest", side_effect=changed_digest):
            with self.assertRaisesRegex(ValueError, "settings changed concurrently"):
                workspace.write_settings(self.repo, candidate, expected)

    def test_index_surfaces_invalid_records(self):
        self.write_current()
        invalid = self.repo / ".qp/records/atona/20260825-bad/record.md"
        invalid.parent.mkdir(parents=True)
        invalid.write_text("# missing frontmatter\n", encoding="utf-8")
        result = workspace.rebuild_index(self.repo)
        self.assertEqual(result["records"], 1)
        self.assertEqual(len(result["invalid"]), 1)
        self.assertEqual(result["workspace_path"], ".qp/INDEX.md")
        self.assertIn("Invalid records", (self.repo / ".qp/INDEX.md").read_text())

    def test_updated_at_must_be_offset_aware_and_index_sorts_by_instant(self):
        first = self.write_current("20260825-first", updated_at="2026-08-25T10:00:00+02:00")
        second = self.write_current("20260825-second", updated_at="2026-08-25T09:30:00+00:00")
        self.assertTrue(workspace.validate_record(self.repo, first)["valid"])
        self.assertTrue(workspace.validate_record(self.repo, second)["valid"])
        workspace.rebuild_index(self.repo)
        text = (self.repo / ".qp/INDEX.md").read_text()
        self.assertLess(text.index("20260825-second"), text.index("20260825-first"))

        malformed = self.repo / ".qp/records/atona/20260825-malformed/record.md"
        malformed.parent.mkdir(parents=True)
        malformed.write_text(self.record_text(updated_at="2026-08-25T10:00:00"), encoding="utf-8")
        result = workspace.validate_record(self.repo, malformed)
        self.assertFalse(result["valid"])
        self.assertIn("offset-aware ISO-8601", " ".join(result["errors"]))

    def test_path_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            workspace.ensure_inside(self.repo / ".qp", self.repo / "outside")


if __name__ == "__main__":
    unittest.main()

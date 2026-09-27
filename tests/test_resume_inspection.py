"""Resume inspection must preserve historical claims and reject stale proof."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))
from local_checks import candidate_snapshot
from project_context import ContextError, load_context
from resume_inspection import inspect_resume


class ResumeInspectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.project = self.root / "project"
        self.project.mkdir()
        for argv in (("init", "-q"), ("config", "user.email", "test@example.invalid"),
                     ("config", "user.name", "Test")):
            self.git(*argv)
        (self.project / "file").write_text("original")
        self.git("add", ".")
        self.git("commit", "-qm", "initial")
        self.record = self.root / "plan.md"
        self.record.write_text("Goal: finish the migration plan\nScope: planning only\nNext action: ask about retention\nWorker state: running\ncodex://threads/old-task\n")

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.project), *args], text=True).strip()

    def receipt(self, gate="passed"):
        context = load_context(self.project)
        snapshot = candidate_snapshot(self.project)
        path = self.root / "receipt.json"
        path.write_text(json.dumps({"schema_version": 1, "gate_status": gate,
                                   "config_digest": context["config_digest"], "base": None,
                                   "snapshot_before": snapshot, "snapshot_after": snapshot,
                                   "selection": {"not_selected": []}}))
        return path

    def test_scoped_records_do_not_select_newest_or_turn_worker_claim_into_state(self):
        (self.root / "newest.md").write_text("Scope: implement unrelated work")
        result = inspect_resume(self.project, records=[self.record], receipts=[])
        self.assertEqual(len(result["records"]), 1)
        self.assertEqual(result["worker_state"], "not_observed")
        self.assertFalse(result["history_searched"])
        self.assertIn("planning only", [x["text"] for x in result["records"][0]["claims"]])
        self.assertEqual(result["records"][0]["linked_sessions"], ["old-task"])

    def test_modified_candidate_invalidates_receipt_and_failed_gate_stays_failed(self):
        path = self.receipt("failed")
        result = inspect_resume(self.project, records=[], receipts=[path])
        self.assertTrue(result["receipts"][0]["fresh"])
        self.assertEqual(result["status"], "attention")
        path = self.receipt()
        (self.project / "file").write_text("changed")
        result = inspect_resume(self.project, records=[], receipts=[path])
        self.assertFalse(result["receipts"][0]["fresh"])
        self.assertIn("candidate changed", result["receipts"][0]["reasons"])

    def test_missing_plan_preserves_alternative_record_and_does_not_write(self):
        before = set(self.root.rglob("*"))
        result = inspect_resume(self.project, records=[self.root / "missing.md", self.record], receipts=[])
        self.assertEqual(result["status"], "attention")
        self.assertEqual(result["records"][1]["status"], "observed")
        self.assertEqual(before, set(self.root.rglob("*")))

    def test_symlink_and_unscoped_discovery_rejected(self):
        link = self.root / "link"
        link.symlink_to(self.record)
        with self.assertRaises(ContextError):
            inspect_resume(self.project, records=[link], receipts=[])
        with self.assertRaises(ContextError):
            inspect_resume(self.project, records=[], receipts=[])


if __name__ == "__main__":
    unittest.main()

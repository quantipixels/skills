"""CI source matches never substitute for execution or effective provider policy."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))
from ci_drift import inspect_ci, invocation_hints, provider_policy
from project_context import ContextError


class CIDriftTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / ".github/workflows").mkdir(parents=True)
        (self.root / ".alarina.json").write_text(json.dumps({"version": 1, "checks": [
            {"id": "unit", "argv": ["python3", "-m", "unittest"], "proof": {"type": "unittest"}},
            {"id": "lint", "argv": ["lint"], "proof": {"type": "exit"}}]}))
        self.workflow = self.root / ".github/workflows/checks.yml"
        self.workflow.write_text("jobs:\n  package:\n    if: false\n    runs-on: ubuntu-latest\n    steps:\n      - run: python3 tools/alarina.py verify --project . --check unit\n")

    def test_partial_conditional_gate_keeps_missing_check_and_no_execution_claim(self):
        result = inspect_ci(self.root)
        self.assertIn({"kind": "local_check_without_literal_ci_match", "check": "lint", "recommendation": "Trace wrappers/reusable workflows before adding or removing a job."}, result["gaps"])
        job = result["inventory"]["workflows"][0]["jobs"][0]
        self.assertIs(job["condition"], False)
        self.assertEqual(job["steps"][0]["check_ids"], ["unit"])
        self.assertEqual(result["inventory"]["provider"]["state"], "not_observed")

    def test_changed_workflow_and_inventory_are_detected_without_writes(self):
        baseline = inspect_ci(self.root)
        self.workflow.write_text(self.workflow.read_text().replace("--check unit", ""))
        result = inspect_ci(self.root, baseline=baseline)
        self.assertEqual(result["changes_since_baseline"], ["workflows"])
        self.assertFalse(result["writes"])
        self.assertFalse(any(gap["kind"] == "local_check_without_literal_ci_match" for gap in result["gaps"]))

    def test_unresolved_shell_and_reusable_workflow_remain_gaps(self):
        self.workflow.write_text("jobs:\n  reused:\n    uses: owner/repo/.github/workflows/build.yml@v1\n  local:\n    steps:\n      - run: echo ok && python3 tools/alarina.py verify --project .\n")
        result = inspect_ci(self.root)
        self.assertTrue(any(x["kind"] == "reusable_workflow_requires_tracing" for x in result["gaps"]))
        self.assertEqual(sum(x["kind"] == "local_check_without_literal_ci_match" for x in result["gaps"]), 2)

    def test_duplicate_yaml_keys_fail_instead_of_hiding_a_job(self):
        self.workflow.write_text("jobs:\n  x: {}\n  x: {}\n")
        with self.assertRaises(ContextError):
            inspect_ci(self.root)

    def test_provider_absence_and_unavailable_access_are_distinct(self):
        def unprotected(endpoint):
            if endpoint.endswith("/protection"):
                return None, "not_found"
            if "/rules/" in endpoint:
                return [], None
            return {"name": "ori"}, None
        self.assertEqual(provider_policy("owner/repo", "ori", unprotected)["state"], "no_required_checks_observed")
        self.assertEqual(provider_policy("owner/repo", "ori", lambda _: (None, "not_found"))["state"], "unknown")

    def test_rules_and_legacy_required_contexts_are_combined(self):
        def transport(endpoint):
            if "/rules/" in endpoint:
                return [{"type": "required_status_checks", "parameters": {"required_status_checks": [{"context": "linux"}]}}], None
            if endpoint.endswith("/protection"):
                return {"required_status_checks": {"contexts": ["macos"], "checks": [{"context": "windows"}]}}, None
            return {"name": "ori"}, None
        result = provider_policy("owner/repo", "ori", transport)
        self.assertEqual(result["required_checks"], ["linux", "macos", "windows"])
        self.assertEqual(result["state"], "required_checks_observed")

    def test_malformed_required_rule_remains_unknown(self):
        def transport(endpoint):
            if "/rules/" in endpoint:
                return [{"type": "required_status_checks", "parameters": {}}], None
            if endpoint.endswith("/protection"):
                return None, "not_found"
            return {"name": "ori"}, None
        self.assertEqual(provider_policy("owner/repo", "ori", transport)["state"], "unknown")

    def test_repeated_project_override_cannot_match_current_inventory(self):
        checks = [{"id": "unit", "argv": ["python3", "-m", "unittest"]}]
        for command in ("python3 tools/alarina.py verify --project . --project ../other",
                        "python3 tools/alarina.py verify --project . --project=../other"):
            self.assertEqual(invocation_hints(command, checks)["check_ids"], [])

    def test_malformed_legacy_entries_remain_unknown(self):
        def transport(endpoint):
            if "/rules/" in endpoint:
                return [], None
            if endpoint.endswith("/protection"):
                return {"required_status_checks": {"contexts": [42], "checks": []}}, None
            return {"name": "ori"}, None
        self.assertEqual(provider_policy("owner/repo", "ori", transport)["state"], "unknown")


if __name__ == "__main__":
    unittest.main()

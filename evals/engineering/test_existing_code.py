"""Behavioral gates for the opt-in repair/additive-feature comparison."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("existing_code_evaluate", Path(__file__).with_name("evaluate.py"))
evaluate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluate)

API = '''from states import AccountState, LABELS

def dispatch(service, action, key):
    if action == "pause":
        return service.hold(key)
    if action == "resume":
        return service.release(key)
    if action == "show":
        row = service.store.get(key)
        return {"id": key, "status": LABELS[AccountState(row["state"])], "cents": row["cents"]}
    raise ValueError("unknown action")
'''
TEST = '''import unittest
from store import Store
from collections_service import Collections
from api import dispatch

class FeatureTest(unittest.TestCase):
    def test_pause_resume(self):
        store = Store(":memory:")
        try:
            store.add("a", 1234)
            service = Collections(store)
            dispatch(service, "pause", "a")
            self.assertEqual([], store.eligible())
            dispatch(service, "resume", "a")
            self.assertEqual(["a"], [row["id"] for row in store.eligible()])
        finally:
            store.close()
'''


class ExistingCodeEvaluationTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.study = self.root / "study"

    def tearDown(self):
        self.temporary.cleanup()

    def prepare(self, cases=None):
        evaluate.prepare(argparse.Namespace(
            output=self.study, host="test", model="test", reasoning="medium",
            max_seconds=20, max_tool_calls=8, profile="existing-code", case=cases,
        ))
        self.manifest = evaluate.read_json(self.study / "manifest.json")

    def candidate(self):
        run = self.study / "runs" / "reuse-control-r1"
        workspace = run / "actor" / "workspace"
        (workspace / "api.py").write_text(API)
        (workspace / "test_feature.py").write_text(TEST)
        (workspace / "RESULT.md").write_text("Mechanical fixture; no model-performance evidence.\n")
        record = evaluate.read_json(run / "record.template.json")
        record["record_kind"] = "mechanical-validation"
        (run / "record.json").write_text(json.dumps(record))
        return workspace

    def check(self):
        spec = next(item for item in self.manifest["runs"] if item["id"] == "reuse-control-r1")
        return evaluate.check_cell(self.study, self.manifest, spec, timeout=2)

    def test_profile_contains_both_pairs_and_can_select_reuse(self):
        self.prepare()
        self.assertEqual(4, len(self.manifest["runs"]))
        self.assertEqual({"settlement", "reuse"}, set(self.manifest["selected_cases"]))
        for case in ("settlement", "reuse"):
            self.assertEqual({"control", "alaga"}, {r["arm"] for r in self.manifest["runs"] if r["case"] == case})
        cells, selected = evaluate.profile_cells("existing-code", ["reuse"])
        self.assertEqual(2, len(cells))
        self.assertEqual(["reuse"], selected)
        with self.assertRaises(ValueError):
            evaluate.profile_cells("historical", ["reuse"])
        self.assertEqual(8, len(evaluate.profile_cells("historical")[0]))
        self.assertEqual(6, len(evaluate.profile_cells("playbooks")[0]))
        guidance = self.study / "runs" / "reuse-alaga-r1" / "actor" / "guidance" / "alaga" / "SKILL.md"
        self.assertTrue(guidance.is_file())
        spec = next(r for r in self.manifest["runs"] if r["id"] == "reuse-control-r1")
        self.assertIn("workspace/test_accounts.py", spec["protected_hashes"])
        self.assertIn("workspace/legacy.sql", spec["protected_hashes"])

    def test_frozen_guidance_changes_only_treatment_and_is_protected(self):
        self.prepare(["reuse"])
        frozen = self.root / "frozen"
        shutil.copytree(evaluate.SKILLS / "alaga", frozen / "alaga")
        (frozen / "alaga" / "SKILL.md").write_text("Frozen comparison guidance\n")
        other = self.root / "other"
        evaluate.prepare(argparse.Namespace(
            output=other, host="test", model="test", reasoning="medium",
            max_seconds=20, max_tool_calls=8, profile="existing-code", case=["reuse"],
            guidance_root=frozen,
        ))
        manifest = evaluate.read_json(other / "manifest.json")
        for before, after in zip(self.manifest["runs"], manifest["runs"]):
            self.assertEqual(before["private_hashes"], after["private_hashes"])
            self.assertEqual(
                {k: v for k, v in before["protected_hashes"].items() if not k.startswith("guidance/")},
                {k: v for k, v in after["protected_hashes"].items() if not k.startswith("guidance/")},
            )
        spec = next(r for r in manifest["runs"] if r["arm"] == "alaga")
        guidance = other / spec["path"] / "actor/guidance/alaga/SKILL.md"
        self.assertEqual("Frozen comparison guidance\n", guidance.read_text())
        self.assertEqual(evaluate.digest(guidance), spec["protected_hashes"]["guidance/alaga/SKILL.md"])
        guidance.write_text("Tampered guidance\n")
        result = evaluate.check_cell(other, manifest, spec, timeout=2)
        self.assertEqual("invalid", result["status"], result)

    def test_missing_frozen_skill_rejected_before_creating_study(self):
        with self.assertRaisesRegex(ValueError, "missing guidance skill: alaga"):
            evaluate.prepare(argparse.Namespace(
                output=self.study, host="test", model="test", reasoning="medium",
                max_seconds=20, max_tool_calls=8, profile="existing-code", case=["reuse"],
                guidance_root=self.root / "missing",
            ))
        self.assertFalse(self.study.exists())

    def test_valid_feature_passes_with_original_runtime_errors_preserved(self):
        self.prepare(["reuse"])
        self.candidate()
        result = self.check()
        self.assertEqual("passed", result["status"], result)
        for name in ("returned_tests", "acceptance", "baseline_tests", "feature_acceptance"):
            self.assertEqual("passed", result[name]["status"])
        self.assertEqual("error", result["tests_against_original"]["status"])
        self.assertIn("ValueError: unknown action", result["tests_against_original"]["stderr"])
        self.assertEqual("error", result["acceptance_against_original"]["status"])
        self.assertEqual("failed", result["feature_acceptance_against_original"]["status"])
        self.assertTrue(evaluate.proves_missing_actions(result["feature_acceptance_against_original"]))

    def test_missing_feature_cannot_pass_baseline_tests_alone(self):
        self.prepare(["reuse"])
        workspace = self.candidate()
        shutil.copy2(evaluate.FIXTURES / "reuse" / "api.py", workspace / "api.py")
        (workspace / "test_feature.py").unlink()
        result = self.check()
        self.assertEqual("error", result["status"])
        self.assertEqual("passed", result["returned_tests"]["status"])
        self.assertEqual("error", result["acceptance"]["status"])

    def test_import_error_in_candidate_tests_is_not_feature_success(self):
        self.prepare(["reuse"])
        workspace = self.candidate()
        (workspace / "test_feature.py").write_text("import missing_test_dependency\n")
        result = self.check()
        self.assertEqual("error", result["status"])
        self.assertEqual("passed", result["acceptance"]["status"])
        self.assertEqual("error", result["returned_tests"]["status"])

    def test_original_import_and_unrelated_assertion_are_not_missing_behavior_proof(self):
        for code, expected in (("import missing_original_dependency\n", "error"),
                               ("def dispatch(*args): raise AssertionError('unrelated failure')\n", "failed")):
            with self.subTest(expected=expected):
                fixture_root = self.root / expected
                shutil.copytree(evaluate.FIXTURES / "reuse", fixture_root / "reuse")
                (fixture_root / "reuse" / "api.py").write_text(code)
                self.study = self.root / f"study-{expected}"
                with patch.object(evaluate, "FIXTURES", fixture_root):
                    self.prepare(["reuse"])
                self.candidate()
                result = self.check()
                self.assertEqual(expected, result["status"], result)
                self.assertEqual("passed", result["acceptance"]["status"])
                self.assertFalse(evaluate.proves_missing_actions(result["feature_acceptance_against_original"]))

    def test_zero_candidate_tests_and_broken_baseline_cannot_pass(self):
        self.prepare(["reuse"])
        workspace = self.candidate()
        original_run = evaluate.subprocess_result
        def no_tests(command, cwd, timeout):
            if "unittest" in command and cwd.name == "candidate":
                return {"status": "completed", "exit_code": 0, "stdout": "", "stderr": "Ran 0 tests in 0.0s\nOK\n"}
            return original_run(command, cwd, timeout)
        with patch.object(evaluate, "subprocess_result", side_effect=no_tests):
            result = self.check()
        self.assertEqual("failed", result["status"])
        self.assertEqual("no-tests", result["returned_tests"]["status"])
        (workspace / "admin.py").write_text("def set_collection_hold(*args): pass\n")
        result = self.check()
        self.assertEqual("failed", result["status"])
        self.assertEqual("failed", result["baseline_tests"]["status"])

    def test_existing_tests_must_be_preserved(self):
        self.prepare(["reuse"])
        workspace = self.candidate()
        (workspace / "test_accounts.py").write_text("")
        result = self.check()
        self.assertEqual("invalid", result["status"])
        self.assertIn("workspace/test_accounts.py", result["tampered"])

    def test_malformed_oracle_output_is_error_not_negative_proof(self):
        for payload in ([], {}, [None], [{}], [{"status": "unknown"}], [{"status": "pass"}]):
            with self.subTest(payload=payload):
                result = {"status": "completed", "exit_code": 1, "stdout": json.dumps(payload), "stderr": ""}
                self.assertEqual("error", evaluate.classify_oracle(result))


if __name__ == "__main__":
    unittest.main()

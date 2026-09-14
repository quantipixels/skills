import argparse
import importlib.util
import json
import math
from pathlib import Path
import shutil
import tempfile
import unittest


MODULE = Path(__file__).with_name("evaluate.py")
SPEC = importlib.util.spec_from_file_location("engineering_evaluate", MODULE)
evaluate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluate)


class EngineeringEvaluationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.base = Path(cls.temporary.name) / "prepared"
        evaluate.prepare(argparse.Namespace(
            output=cls.base, host="test-host", model="test-model", reasoning="medium",
            max_seconds=10, max_tool_calls=4,
        ))

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def setUp(self):
        self.case_temp = tempfile.TemporaryDirectory()
        self.study = Path(self.case_temp.name) / "study"
        shutil.copytree(self.base, self.study)

    def tearDown(self):
        self.case_temp.cleanup()

    def run_path(self, cell="batching-control-r1"):
        return self.study / "runs" / cell

    def complete(self, cell="batching-control-r1"):
        run = self.run_path(cell)
        (run / "actor" / "workspace" / "RESULT.md").write_text("mechanical fixture\n")
        record = json.loads((run / "record.template.json").read_text())
        record.update({"record_kind": "mechanical-validation", "note": "harness test"})
        (run / "record.json").write_text(json.dumps(record))
        return run

    def check(self, timeout=2):
        output = Path(self.case_temp.name) / "checks.json"
        return evaluate.check(argparse.Namespace(study=self.study, output=output, timeout=timeout))

    def result(self, report, cell="batching-control-r1"):
        return next(item for item in report["results"] if item["id"] == cell)

    def test_prepare_has_fixed_eight_cells_and_unrun_is_preserved(self):
        report = self.check()
        self.assertEqual(8, len(report["results"]))
        self.assertEqual({"unrun"}, {item["status"] for item in report["results"]})

    def test_partial_completion_preserves_record_and_missing_provenance(self):
        run = self.run_path()
        record = json.loads((run / "record.template.json").read_text())
        record.update({
            "record_kind": "mechanical-validation",
            "elapsed_seconds": 3.5,
            "tool_calls": 2,
            "note": "interrupted before RESULT.md",
        })
        (run / "record.json").write_text(json.dumps(record))
        result = self.result(self.check())
        self.assertEqual("incomplete", result["status"])
        self.assertEqual("mechanical-validation", result["record_kind"])
        self.assertEqual(3.5, result["record"]["elapsed_seconds"])
        self.assertEqual(["workspace/RESULT.md"], result["missing"])

        self.tearDown()
        self.setUp()
        run = self.run_path()
        (run / "actor" / "workspace" / "RESULT.md").write_text("output without provenance\n")
        result = self.result(self.check())
        self.assertEqual("incomplete", result["status"])
        self.assertIsNone(result["record_kind"])
        self.assertEqual(["record.json"], result["missing"])

        self.tearDown()
        self.setUp()
        run = self.run_path()
        with (run / "actor" / "workspace" / "batching.py").open("a") as stream:
            stream.write("\n# interrupted edit\n")
        result = self.result(self.check())
        self.assertEqual("incomplete", result["status"])
        self.assertIsNone(result["record_kind"])
        self.assertEqual(["record.json", "workspace/RESULT.md"], result["missing"])

    def test_valid_batching_repair_passes_and_detects_original(self):
        run = self.complete()
        workspace = run / "actor" / "workspace"
        (workspace / "batching.py").write_text(
            "def chunks(items, size):\n"
            "    if size <= 0:\n        raise ValueError('size must be positive')\n"
            "    return [items[i:i + size] for i in range(0, len(items), size)]\n"
        )
        with (workspace / "test_batching.py").open("a") as stream:
            stream.write("\nfrom pathlib import Path\nPath('test-side-effect').write_text('temporary')\nclass Regression(unittest.TestCase):\n    def test_partial(self):\n        self.assertEqual([[1, 2], [3]], chunks([1, 2, 3], 2))\n")
        cache = workspace / "__pycache__"
        cache.mkdir()
        (cache / "batching.cpython-312.pyc").write_bytes(b"host-created cache")
        result = self.result(self.check())
        self.assertEqual("passed", result["status"])
        self.assertEqual("failed", result["tests_against_original"]["status"])
        self.assertFalse((workspace / "test-side-effect").exists())

    def test_valid_settlement_repair_preserves_existing_data_contract(self):
        cell = "settlement-control-r1"
        run = self.complete(cell)
        workspace = run / "actor" / "workspace"
        (workspace / "settlement.py").write_text(
            "import sqlite3\n"
            "class Settlement:\n"
            "    def __init__(self, path, provider):\n"
            "        self.db = sqlite3.connect(path)\n"
            "        self.db.execute(\"CREATE TABLE IF NOT EXISTS completed (settlement_id TEXT PRIMARY KEY, cents INTEGER NOT NULL, transfer_id INTEGER NOT NULL)\")\n"
            "        self.provider = provider\n"
            "    def settle(self, settlement_id, cents):\n"
            "        prior = self.db.execute(\"SELECT cents, transfer_id FROM completed WHERE settlement_id = ?\", (settlement_id,)).fetchone()\n"
            "        if prior:\n"
            "            if prior[0] != cents: raise ValueError('settlement ID reused with different amount')\n"
            "            return prior[1]\n"
            "        transfer_id = self.provider.transfer(settlement_id, cents)\n"
            "        self.db.execute(\"INSERT INTO completed VALUES (?, ?, ?)\", (settlement_id, cents, transfer_id))\n"
            "        self.db.commit()\n"
            "        return transfer_id\n"
            "    def close(self): self.db.close()\n"
        )
        with (workspace / "test_settlement.py").open("a") as stream:
            stream.write(
                "\nclass RetryRegression(unittest.TestCase):\n"
                "    def test_lost_reply_reopen(self):\n"
                "        with tempfile.TemporaryDirectory() as temp:\n"
                "            root = Path(temp); provider = Provider(root/'provider.db'); service = Settlement(root/'service.db', provider)\n"
                "            provider.drop_next_reply = True\n"
                "            with self.assertRaises(Exception): service.settle('S7', 4913)\n"
                "            service.close(); provider.close(); provider = Provider(root/'provider.db'); service = Settlement(root/'service.db', provider)\n"
                "            service.settle('S7', 4913)\n"
                "            self.assertEqual(1, provider.db.execute('SELECT COUNT(*) FROM transfers').fetchone()[0])\n"
                "            service.close(); provider.close()\n"
            )
        result = self.result(self.check(), cell)
        self.assertEqual("passed", result["status"])
        self.assertEqual("passed", result["acceptance"]["status"])

    def test_zero_tests_and_baseline_only_tests_cannot_pass(self):
        run = self.complete()
        (run / "actor" / "workspace" / "test_batching.py").unlink()
        result = self.result(self.check())
        self.assertEqual("failed", result["status"])
        self.assertEqual("no-tests", result["returned_tests"]["status"])

        self.tearDown()
        self.setUp()
        run = self.complete()
        (run / "actor" / "workspace" / "batching.py").write_text(
            "def chunks(items, size):\n    if size <= 0: raise ValueError\n    return [items[i:i+size] for i in range(0, len(items), size)]\n"
        )
        result = self.result(self.check())
        self.assertEqual("failed", result["status"])
        self.assertEqual("passed", result["tests_against_original"]["status"])

    def test_timeout_and_execution_error_remain_distinct(self):
        run = self.complete()
        (run / "actor" / "workspace" / "test_hang.py").write_text(
            "import time, unittest\nclass Hang(unittest.TestCase):\n    def test_hang(self): time.sleep(2)\n"
        )
        self.assertEqual("timeout", self.result(self.check(timeout=.05))["status"])

        self.tearDown()
        self.setUp()
        run = self.complete()
        (run / "actor" / "workspace" / "test_error.py").write_text("import missing_evaluation_module\n")
        result = self.result(self.check())
        self.assertEqual("error", result["status"])
        self.assertEqual("error", result["returned_tests"]["status"])

    def test_nonassertion_exit_and_all_skipped_tests_are_not_regressions(self):
        completed = {"status": "completed", "exit_code": 1, "stdout": "", "stderr": "Ran 1 test in 0.01s\n"}
        self.assertEqual("error", evaluate.classify_tests(completed))
        skipped = {"status": "completed", "exit_code": 0, "stdout": "Ran 1 test in 0.01s\n\nOK (skipped=1)\n", "stderr": ""}
        self.assertEqual("no-tests", evaluate.classify_tests(skipped))

    def test_protected_tampering_and_missing_run_are_explicit(self):
        run = self.complete()
        (run / "actor" / "PROMPT.md").write_text("changed\n")
        self.assertEqual("invalid", self.result(self.check())["status"])

        self.tearDown()
        self.setUp()
        shutil.rmtree(self.run_path())
        self.assertEqual("missing", self.result(self.check())["status"])

    def test_summary_keeps_all_cells_and_provenance(self):
        self.complete()
        checks_path = Path(self.case_temp.name) / "checks.json"
        evaluate.check(argparse.Namespace(study=self.study, output=checks_path, timeout=2))
        output = Path(self.case_temp.name) / "summary.json"
        report = evaluate.summary(argparse.Namespace(study=self.study, checks=checks_path, output=output))
        self.assertEqual(8, len(report["cells"]))
        self.assertEqual(["mechanical-validation"], report["record_kinds_present"])
        self.assertIn("No winner", report["comparison"])

    def test_summary_rejects_stale_or_duplicate_check_results(self):
        run = self.complete()
        checks_path = Path(self.case_temp.name) / "checks.json"
        evaluate.check(argparse.Namespace(study=self.study, output=checks_path, timeout=2))
        (run / "actor" / "workspace" / "RESULT.md").write_text("changed after check\n")
        with self.assertRaisesRegex(ValueError, "stale"):
            evaluate.summary(argparse.Namespace(study=self.study, checks=checks_path, output=Path(self.case_temp.name) / "stale.json"))

        self.tearDown()
        self.setUp()
        checks_path = Path(self.case_temp.name) / "checks.json"
        report = evaluate.check(argparse.Namespace(study=self.study, output=checks_path, timeout=2))
        report["results"][1] = report["results"][0]
        duplicate = Path(self.case_temp.name) / "duplicate.json"
        duplicate.write_text(json.dumps(report))
        with self.assertRaisesRegex(ValueError, "exactly once"):
            evaluate.summary(argparse.Namespace(study=self.study, checks=duplicate, output=Path(self.case_temp.name) / "duplicate-summary.json"))

    def test_nonfinite_budget_and_record_metrics_are_rejected(self):
        with self.assertRaises(ValueError):
            evaluate.require_positive("budget", math.inf)
        manifest = json.loads((self.study / "manifest.json").read_text())
        record = json.loads((self.run_path() / "record.template.json").read_text())
        record.update({"record_kind": "mechanical-validation", "elapsed_seconds": math.nan})
        with self.assertRaisesRegex(ValueError, "invalid measurement"):
            evaluate.validate_record(record, manifest)

    def test_model_run_requires_and_reports_isolation_disclosure(self):
        run = self.run_path()
        record = json.loads((run / "record.template.json").read_text())
        record.update({
            "record_kind": "model-run",
            "isolated_host_sandbox": False,
            "trace": "trace/model-run.jsonl",
            "elapsed_seconds": 2,
        })
        (run / "record.json").write_text(json.dumps(record))
        checks_path = Path(self.case_temp.name) / "checks.json"
        result = evaluate.check(argparse.Namespace(study=self.study, output=checks_path, timeout=2))
        cell = self.result(result)
        self.assertEqual("incomplete", cell["status"])
        self.assertFalse(cell["record"]["isolated_host_sandbox"])
        summary_path = Path(self.case_temp.name) / "summary.json"
        summary = evaluate.summary(argparse.Namespace(study=self.study, checks=checks_path, output=summary_path))
        self.assertEqual(["batching-control-r1"], summary["isolation_limitations"]["unisolated_model_runs"])
        self.assertIn("causal", summary["isolation_limitations"]["claim"])

        record.pop("isolated_host_sandbox")
        manifest = json.loads((self.study / "manifest.json").read_text())
        with self.assertRaisesRegex(ValueError, "boolean"):
            evaluate.validate_record(record, manifest)


if __name__ == "__main__":
    unittest.main()

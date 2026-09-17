import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import tempfile
import time
import unittest
from unittest.mock import patch


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

    def test_guidance_root_is_validated_before_study_output_and_frozen_in_pairs(self):
        missing = Path(self.case_temp.name) / "missing-guidance"
        output = Path(self.case_temp.name) / "rejected-study"
        with self.assertRaisesRegex(ValueError, "guidance root"):
            evaluate.prepare(argparse.Namespace(
                output=output, guidance_root=missing, host="test-host", model="test-model",
                reasoning="medium", max_seconds=10, max_tool_calls=4,
            ))
        self.assertFalse(output.exists())

        frozen = Path(self.case_temp.name) / "frozen-skills"
        shutil.copytree(evaluate.SKILLS, frozen)
        prepared = Path(self.case_temp.name) / "frozen-study"
        evaluate.prepare(argparse.Namespace(
            output=prepared, guidance_root=frozen, host="test-host", model="test-model",
            reasoning="medium", max_seconds=10, max_tool_calls=4,
        ))
        manifest = json.loads((prepared / "manifest.json").read_text())
        self.assertEqual(str(frozen.resolve()), manifest["guidance_source"])
        self.assertIn("alaga", manifest["guidance_hashes"])
        guidance = prepared / "runs" / "settlement-alaga-r1" / "actor" / "guidance" / "alaga" / "SKILL.md"
        self.assertEqual(manifest["guidance_hashes"]["alaga"], hashlib.sha256(
            json.dumps(evaluate.file_hashes(frozen / "alaga"), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest())
        spec = next(item for item in manifest["runs"] if item["id"] == "settlement-alaga-r1")
        self.assertEqual(spec["protected_hashes"]["guidance/alaga/SKILL.md"], evaluate.digest(guidance))

        altered = Path(self.case_temp.name) / "altered-skills"
        shutil.copytree(evaluate.SKILLS, altered)
        (altered / "alaga" / "SKILL.md").write_text((altered / "alaga" / "SKILL.md").read_text() + "\n# paired treatment alteration\n")
        altered_study = Path(self.case_temp.name) / "altered-study"
        evaluate.prepare(argparse.Namespace(
            output=altered_study, guidance_root=altered, host="test-host", model="test-model",
            reasoning="medium", max_seconds=10, max_tool_calls=4,
        ))
        altered_manifest = json.loads((altered_study / "manifest.json").read_text())
        original_control = next(item for item in manifest["runs"] if item["id"] == "settlement-control-r1")
        altered_control = next(item for item in altered_manifest["runs"] if item["id"] == "settlement-control-r1")
        original_treatment = next(item for item in manifest["runs"] if item["id"] == "settlement-alaga-r1")
        altered_treatment = next(item for item in altered_manifest["runs"] if item["id"] == "settlement-alaga-r1")
        self.assertEqual(original_control["protected_hashes"]["TASK.md"], altered_control["protected_hashes"]["TASK.md"])
        self.assertEqual(original_control["private_hashes"], altered_control["private_hashes"])
        self.assertNotEqual(original_treatment["protected_hashes"]["guidance/alaga/SKILL.md"], altered_treatment["protected_hashes"]["guidance/alaga/SKILL.md"])

        incomplete = Path(self.case_temp.name) / "incomplete-skills"
        shutil.copytree(evaluate.SKILLS, incomplete)
        (incomplete / "alaga" / "SKILL.md").unlink()
        rejected = Path(self.case_temp.name) / "missing-skill-study"
        with self.assertRaisesRegex(ValueError, "missing guidance skill: alaga"):
            evaluate.prepare(argparse.Namespace(
                output=rejected, guidance_root=incomplete, host="test-host", model="test-model",
                reasoning="medium", max_seconds=10, max_tool_calls=4,
            ))
        self.assertFalse(rejected.exists())

    def test_cleanup_failures_are_reported_and_owned_pipes_close(self):
        with patch.object(evaluate, "stop_process_group", side_effect=evaluate.ProcessCleanupError("test cleanup failure")):
            result = evaluate.subprocess_result(
                [evaluate.sys.executable, "-c", "print('ok')"], Path(self.case_temp.name), timeout=2
            )
        self.assertEqual("cleanup-error", result["status"])
        self.assertIn("test cleanup failure", result["stderr"])

    @unittest.skipUnless(os.name == "posix", "native process-group assertion")
    def test_process_membership_rejects_empty_or_malformed_observation(self):
        for output in ("", "not process records\n", "17\n", "17 42 extra\n"):
            result = evaluate.subprocess.CompletedProcess([], 0, output, "")
            with self.subTest(output=output), patch.object(evaluate.subprocess, "run", return_value=result):
                with self.assertRaises(evaluate.ProcessCleanupError):
                    evaluate._process_group_members(42)
        result = evaluate.subprocess.CompletedProcess([], 0, "17 42\n18 43\n", "")
        with patch.object(evaluate.subprocess, "run", return_value=result):
            self.assertEqual({17}, evaluate._process_group_members(42))
            self.assertEqual(set(), evaluate._process_group_members(99))

    def test_permission_probe_needs_positive_group_membership_evidence(self):
        class ExitedProcess:
            pid = 417

            @staticmethod
            def poll():
                return 0

        with patch.object(evaluate.os, "killpg", side_effect=PermissionError("probe")), \
                patch.object(evaluate, "_process_group_members", return_value={902}):
            self.assertTrue(evaluate._group_exists(ExitedProcess()))
        with patch.object(evaluate.os, "killpg", side_effect=PermissionError("probe")), \
                patch.object(evaluate, "_process_group_members", return_value=set()):
            self.assertFalse(evaluate._group_exists(ExitedProcess()))
        with patch.object(evaluate.os, "killpg", side_effect=PermissionError("probe")), \
                patch.object(evaluate, "_process_group_members", side_effect=evaluate.ProcessCleanupError("unreadable")):
            with self.assertRaises(evaluate.ProcessCleanupError):
                evaluate._group_exists(ExitedProcess())

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
        self.assertEqual("passed", result["status"], result)
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

    @unittest.skipUnless(os.name == "posix", "native process-group assertion")
    def test_timeout_cleans_descendant_process_group(self):
        run = self.complete()
        pid_path = Path(self.case_temp.name) / "child.pid"
        (run / "actor" / "workspace" / "test_spawn.py").write_text(
            "import subprocess, sys, time, unittest\n"
            "from pathlib import Path\n"
            "class Spawn(unittest.TestCase):\n"
            "    def test_spawn(self):\n"
            "        child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'])\n"
            f"        Path({str(pid_path)!r}).write_text(str(child.pid))\n"
            "        time.sleep(30)\n"
        )
        self.assertEqual("timeout", self.result(self.check(timeout=0.2))["status"])
        pid = int(pid_path.read_text())
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            try:
                os.kill(pid, 0)
            except ProcessLookupError:
                return
            time.sleep(0.02)
        self.fail(f"descendant process {pid} survived checker timeout")

    @unittest.skipUnless(os.name == "posix", "native process-group assertion")
    def test_normal_completion_cleans_remaining_descendants(self):
        script = Path(self.case_temp.name) / "spawn_and_return.py"
        pid_path = Path(self.case_temp.name) / "returned-child.pid"
        script.write_text(
            "import subprocess, sys\n"
            "from pathlib import Path\n"
            "child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)\n"
            f"Path({str(pid_path)!r}).write_text(str(child.pid))\n"
        )
        result = evaluate.subprocess_result(
            [evaluate.sys.executable, str(script)],
            Path(self.case_temp.name),
            timeout=2,
        )
        self.assertEqual("completed", result["status"])
        self.assertEqual(0, result["exit_code"])
        pid = int(pid_path.read_text())
        with self.assertRaises(ProcessLookupError):
            os.kill(pid, 0)

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


class PlaybookEvaluationTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def prepare(self, *cases):
        study = self.root / f"study-{len(list(self.root.glob('study-*')))}"
        evaluate.prepare(argparse.Namespace(
            output=study,
            host="test-host",
            model="test-model",
            reasoning="medium",
            max_seconds=20,
            max_tool_calls=8,
            profile="playbooks",
            case=list(cases) or None,
        ))
        return study

    def complete(self, study, cell):
        run = study / "runs" / cell
        (run / "actor" / "workspace" / "RESULT.md").write_text("mechanical fixture\n")
        record = json.loads((run / "record.template.json").read_text())
        record.update({"record_kind": "mechanical-validation", "note": "harness test"})
        (run / "record.json").write_text(json.dumps(record))
        return run

    def check(self, study, name="checks.json", timeout=8):
        return evaluate.check(argparse.Namespace(
            study=study,
            output=self.root / name,
            timeout=timeout,
        ))

    def result(self, report, cell):
        return next(item for item in report["results"] if item["id"] == cell)

    def test_playbooks_profile_is_opt_in_selectable_and_freezes_relevant_guidance(self):
        study = self.prepare()
        manifest = json.loads((study / "manifest.json").read_text())
        self.assertEqual("playbooks", manifest["profile"])
        self.assertEqual(6, len(manifest["runs"]))
        self.assertEqual(
            {"verification", "migration", "profile"},
            set(manifest["selected_cases"]),
        )
        self.assertTrue((study / "runs" / "verification-alaga-r1" / "actor" / "guidance" / "oro" / "SKILL.md").is_file())
        self.assertTrue((study / "runs" / "profile-alaga-r1" / "actor" / "guidance" / "irinse" / "SKILL.md").is_file())
        profile_spec = next(item for item in manifest["runs"] if item["id"] == "profile-alaga-r1")
        self.assertIn("workspace/capture.json", profile_spec["protected_hashes"])
        self.assertIn("guidance/irinse/SKILL.md", profile_spec["protected_hashes"])

        selected = self.prepare("profile")
        selected_manifest = json.loads((selected / "manifest.json").read_text())
        self.assertEqual(["profile"], selected_manifest["selected_cases"])
        self.assertEqual(
            ["profile-control-r1", "profile-alaga-r1"],
            [item["id"] for item in selected_manifest["runs"]],
        )
        self.assertEqual(2, selected_manifest["budget"]["runs"])

    def test_profile_oracle_derives_capture_facts_and_requires_causal_abstention(self):
        study = self.prepare("profile")
        run = self.complete(study, "profile-control-r1")
        failed = self.result(self.check(study), "profile-control-r1")
        self.assertEqual("failed", failed["status"])
        self.assertEqual("failed", failed["acceptance"]["status"])
        self.assertEqual("not-applicable", failed["returned_tests"]["status"])

        diagnosis = run / "actor" / "workspace" / "diagnosis.json"
        value = json.loads(diagnosis.read_text())
        value["causal_assessment"] = {
            "status": "DIAGNOSED_BUT_UNPROVED",
            "confirmed_root_cause": None,
            "live_hypotheses": ["single_large_snapshot", "repeated_snapshot_parse"],
        }
        value["next_probe"] = {
            "scope": "one GET /reports/monthly request",
            "metrics": ["parse_calls", "snapshot_bytes"],
            "distinguishes": ["single_large_snapshot", "repeated_snapshot_parse"],
        }
        diagnosis.write_text(json.dumps(value, indent=2) + "\n")
        passed = self.result(self.check(study, "corrected-profile.json"), "profile-control-r1")
        self.assertEqual("passed", passed["status"])
        self.assertEqual("passed", passed["acceptance"]["status"])
        self.assertEqual("failed", passed["acceptance_against_original"]["status"])

        value["capture_conditions"]["artifact_kind"] = "controlled_synthetic_sampled_stack_fixture"
        value["source_attribution"] = {
            "application_entry": value["source_attribution"],
            "observation": "An inclusive hotspot does not establish parse frequency.",
        }
        diagnosis.write_text(json.dumps(value, indent=2) + "\n")
        enriched = self.result(self.check(study, "enriched-profile.json"), "profile-control-r1")
        self.assertEqual("passed", enriched["status"])

        frame = value["source_attribution"]["application_entry"]
        correct_line = frame["line"]
        frame["line"] = correct_line + 1
        diagnosis.write_text(json.dumps(value, indent=2) + "\n")
        wrong_source = self.result(self.check(study, "wrong-source.json"), "profile-control-r1")
        self.assertEqual("failed", wrong_source["status"])
        frame["line"] = correct_line

        value["source_attribution"]["line"] = correct_line + 1
        diagnosis.write_text(json.dumps(value, indent=2) + "\n")
        conflicting = self.result(self.check(study, "conflicting-source.json"), "profile-control-r1")
        self.assertEqual("failed", conflicting["status"])
        del value["source_attribution"]["line"]

        correct_duration = value["capture_conditions"]["duration_ms"]
        value["capture_conditions"]["duration_ms"] = correct_duration + 1
        diagnosis.write_text(json.dumps(value, indent=2) + "\n")
        wrong_conditions = self.result(self.check(study, "wrong-conditions.json"), "profile-control-r1")
        self.assertEqual("failed", wrong_conditions["status"])
        value["capture_conditions"]["duration_ms"] = correct_duration

        value["sample_count"] = 99
        diagnosis.write_text(json.dumps(value, indent=2) + "\n")
        wrong_count = self.result(self.check(study, "wrong-count.json"), "profile-control-r1")
        self.assertEqual("failed", wrong_count["status"])

        capture = run / "actor" / "workspace" / "capture.json"
        capture.write_text(capture.read_text() + "\n")
        tampered = self.result(self.check(study, "tampered-capture.json"), "profile-control-r1")
        self.assertEqual("invalid", tampered["status"])
        self.assertEqual(["workspace/capture.json"], tampered["tampered"])

    def test_populated_migration_passes_and_wrong_row_order_fails(self):
        study = self.prepare("migration")
        run = self.complete(study, "migration-control-r1")
        workspace = run / "actor" / "workspace"
        (workspace / "migration.py").write_text(
            "import sqlite3\n"
            "def migrate(path):\n"
            "    db = sqlite3.connect(path)\n"
            "    try:\n"
            "        version = db.execute('PRAGMA user_version').fetchone()[0]\n"
            "        if version == 2: return\n"
            "        if version != 1: raise ValueError(f'unsupported schema version: {version}')\n"
            "        db.execute('BEGIN IMMEDIATE')\n"
            "        db.execute('ALTER TABLE project_members RENAME TO project_members_legacy')\n"
            "        db.execute('CREATE TABLE project_members (project_id INTEGER NOT NULL REFERENCES projects(id), account_login TEXT NOT NULL REFERENCES accounts(login), role TEXT NOT NULL, PRIMARY KEY(project_id, account_login))')\n"
            "        db.execute('INSERT INTO project_members(project_id, account_login, role) SELECT m.project_id, a.login, m.role FROM project_members_legacy m JOIN accounts a ON a.id = m.account_id')\n"
            "        db.execute('DROP TABLE project_members_legacy')\n"
            "        db.execute('PRAGMA user_version = 2')\n"
            "        db.commit()\n"
            "    except BaseException:\n"
            "        db.rollback(); raise\n"
            "    finally:\n"
            "        db.close()\n"
        )
        with (workspace / "test_migration.py").open("a") as stream:
            stream.write(
                "\nclass PopulatedRegression(unittest.TestCase):\n"
                "    def test_sparse_ids_keep_members(self):\n"
                "        with tempfile.TemporaryDirectory() as temporary:\n"
                "            root = Path(temporary); path = root/'legacy.db'\n"
                "            with sqlite3.connect(path) as db: db.executescript(Path('legacy.sql').read_text())\n"
                "            migrate(path)\n"
                "            with sqlite3.connect(path) as db:\n"
                "                self.assertEqual([(4, 'li', 'owner'), (20, 'amy', 'reviewer'), (20, 'zoe', 'owner')], db.execute('SELECT project_id, account_login, role FROM project_members ORDER BY project_id, account_login').fetchall())\n"
            )
        result = self.result(self.check(study), "migration-control-r1")
        self.assertEqual("passed", result["status"])
        self.assertEqual("passed", result["acceptance"]["status"])
        self.assertEqual("failed", result["tests_against_original"]["status"])

    def test_verification_driver_crosses_process_boundary_and_cleans_up(self):
        study = self.prepare("verification")
        run = self.complete(study, "verification-control-r1")
        workspace = run / "actor" / "workspace"
        (workspace / "verify_project.py").write_text(
            "import argparse, json, shutil, subprocess, sys\n"
            "from pathlib import Path\n"
            "APP = Path(__file__).with_name('project_app.py')\n"
            "def build_parser():\n"
            "    parser = argparse.ArgumentParser(); parser.add_argument('--workdir', type=Path, required=True); parser.add_argument('--url', required=True); parser.add_argument('operation', choices=('put', 'get')); return parser\n"
            "def main():\n"
            "    args = build_parser().parse_args(); args.workdir.mkdir(parents=True, exist_ok=True)\n"
            "    try:\n"
            "        command = [sys.executable, str(APP), args.operation, '--url', args.url, '--id', 'alpha']\n"
            "        if args.operation == 'put': command += ['--text', 'persistent']\n"
            "        result = subprocess.run(command, text=True, capture_output=True)\n"
            "        if result.returncode != 0:\n"
            "            sys.stderr.write(result.stderr); raise SystemExit(result.returncode)\n"
            "        print(json.dumps({'status': 'passed', 'operation': args.operation, 'value': json.loads(result.stdout)}, sort_keys=True))\n"
            "    finally:\n"
            "        for path in list(args.workdir.iterdir()):\n"
            "            shutil.rmtree(path) if path.is_dir() else path.unlink()\n"
            "if __name__ == '__main__': main()\n"
        )
        with (workspace / "test_verify_project.py").open("a") as stream:
            stream.write(
                "\nimport sqlite3, subprocess, sys, tempfile, time\n"
                "from pathlib import Path\n"
                "class BoundaryRegression(unittest.TestCase):\n"
                "    def test_public_put_and_cleanup(self):\n"
                "        with tempfile.TemporaryDirectory() as temporary:\n"
                "            root = Path(temporary); owned = root/'owned'; owned.mkdir(); port = root/'port'; db = root/'state.db'\n"
                "            server = subprocess.Popen([sys.executable, 'project_app.py', 'serve', '--db', str(db), '--port-file', str(port), '--max-requests', '1'])\n"
                "            try:\n"
                "                deadline = time.monotonic() + 3\n"
                "                while not port.is_file() and time.monotonic() < deadline: time.sleep(.01)\n"
                "                result = subprocess.run([sys.executable, 'verify_project.py', '--workdir', str(owned), '--url', 'http://127.0.0.1:' + port.read_text(), 'put'], text=True, capture_output=True)\n"
                "                self.assertEqual(0, result.returncode, result.stderr)\n"
                "                deadline = time.monotonic() + 1\n"
                "                while server.poll() is None and time.monotonic() < deadline: time.sleep(.01)\n"
                "                self.assertIsNotNone(server.poll(), 'protected service received no public request')\n"
                "                with sqlite3.connect(db) as database: self.assertEqual([('put', 'alpha')], database.execute('SELECT event, item_id FROM request_log').fetchall())\n"
                "                self.assertEqual([], list(owned.iterdir()))\n"
                "            finally:\n"
                "                if server.poll() is None: server.terminate(); server.wait(timeout=1)\n"
            )
        result = self.result(self.check(study, timeout=15), "verification-control-r1")
        self.assertEqual("passed", result["status"], result)
        self.assertEqual("passed", result["acceptance"]["status"])
        self.assertEqual("failed", result["tests_against_original"]["status"])

    def test_fabricated_verification_receipts_do_not_count_as_boundary_evidence(self):
        study = self.prepare("verification")
        self.complete(study, "verification-control-r1")
        result = self.result(self.check(study, timeout=8), "verification-control-r1")
        self.assertEqual("failed", result["status"])
        self.assertEqual("failed", result["acceptance"]["status"])
        self.assertIn("received no public request", result["acceptance"]["stdout"])


if __name__ == "__main__":
    unittest.main()

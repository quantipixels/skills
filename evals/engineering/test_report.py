"""Report semantics and integration with the existing freshness checks; no model calls."""
import argparse
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


report = load("qp_report_test", "report.py")


class ReportRenderingTests(unittest.TestCase):
    def summary(self):
        return {
            "question": "Does guidance help?",
            "configuration": {"host": "test", "model": "test", "reasoning": "low"},
            "cells": [
                {"id": "control", "status": "unrun", "record_kind": "unrun"},
                {"id": "candidate", "status": "passed", "record_kind": "replay",
                 "record": {"elapsed_seconds": 0, "tool_calls": None}},
            ],
            "isolation_limitations": {"unisolated_model_runs": [], "unknown_or_non_model_cells": ["control", "candidate"]},
            "comparison": "No winner is inferred from pass counts.",
            "evidence_limit": "Replay is not model-performance evidence.",
        }

    def test_keeps_unrun_and_replay_separate(self):
        output = report.render(self.summary())
        self.assertIn("1 passed, 1 unrun", output)
        self.assertIn("| control | unrun | unrun | unknown | unknown |", output)
        self.assertIn("| candidate | passed | replay | 0 | unknown |", output)
        self.assertIn("No winner is inferred", output)

    def test_preserves_zero_test_and_original_rejection_details(self):
        summary = self.summary()
        summary["cells"][1].update(status="failed", returned_tests={"status": "no-tests"},
                                    tests_against_original={"status": "failed"})
        output = report.render(summary)
        self.assertIn("returned_tests=no-tests", output)
        self.assertIn("tests_against_original=failed", output)
        self.assertIn("original rejection can be expected", output)

    def test_control_characters_cannot_add_rows(self):
        summary = self.summary()
        summary["cells"][1]["id"] = "candidate|injected\nrow\x1b[31m"
        output = report.render(summary)
        self.assertIn("candidate\\|injected row [31m", output)
        self.assertNotIn("\x1b", output)


class ReportIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.study = self.root / "study"
        self.checks = self.root / "checks.json"
        self.evaluator = load("qp_report_evaluator_test", "evaluate.py")
        self.evaluator.prepare(argparse.Namespace(
            output=self.study, host="test", model="test", reasoning="low",
            max_seconds=10, max_tool_calls=4, profile="existing-code", case=["reuse"],
        ))
        self.evaluator.check(argparse.Namespace(study=self.study, output=self.checks, timeout=2))

    def invoke(self):
        output, error = io.StringIO(), io.StringIO()
        with redirect_stdout(output), redirect_stderr(error):
            code = report.main(["--study", str(self.study), "--checks", str(self.checks)])
        return code, output.getvalue(), error.getvalue()

    def test_unrun_report_preserves_study_and_both_arms(self):
        before = self.evaluator.tree_hash(self.study)
        code, output, error = self.invoke()
        self.assertEqual(0, code, error)
        self.assertIn("reuse-control-r1", output)
        self.assertIn("reuse-alaga-r1", output)
        self.assertIn("not an acceptance or improvement verdict", output)
        self.assertEqual(before, self.evaluator.tree_hash(self.study))

    def test_changed_candidate_refuses_stale_results(self):
        path = self.study / "runs/reuse-control-r1/actor/workspace/RESULT.md"
        path.write_text("Changed after check.\n", encoding="utf-8")
        code, output, error = self.invoke()
        self.assertEqual(2, code)
        self.assertEqual("", output)
        self.assertIn("stale check result", error)

    def test_missing_cell_is_not_a_complete_report(self):
        checked = json.loads(self.checks.read_text())
        checked["results"].pop()
        self.checks.write_text(json.dumps(checked))
        code, output, error = self.invoke()
        self.assertEqual(2, code)
        self.assertEqual("", output)
        self.assertIn("each expected cell", error)

    def test_changed_frozen_manifest_is_rejected(self):
        path = self.study / "manifest.json"
        manifest = json.loads(path.read_text())
        manifest["question"] = "Changed after check"
        path.write_text(json.dumps(manifest))
        code, output, error = self.invoke()
        self.assertEqual(2, code)
        self.assertEqual("", output)
        self.assertIn("different or changed study", error)


if __name__ == "__main__":
    unittest.main()

"""Keep decision-changing rejection evidence visible in the report projection."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("report_diagnostics", Path(__file__).with_name("report.py"))
report = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(report)


def packet(cell):
    return {
        "question": "Does this candidate satisfy the selected boundary?",
        "configuration": {"host": "fixture", "model": "fixture", "reasoning": "fixture"},
        "cells": [cell],
        "comparison": "No winner is inferred.",
        "evidence_limit": "Fixture evidence is not a model run.",
    }


class ReportDiagnosticTests(unittest.TestCase):
    def test_original_artifact_acceptance_is_visible_even_when_it_passes(self):
        value = packet({
            "id": "profile-control-r1", "status": "failed", "record_kind": "mechanical-validation",
            "acceptance": {"status": "passed"},
            # Passing the original is precisely why the independent negative control failed.
            "acceptance_against_original": {"status": "passed"},
        })
        output = report.render(value)
        self.assertIn("acceptance_against_original=passed", output)
        self.assertIn("| profile-control-r1 | failed |", output)

    def test_integrity_and_incomplete_run_reasons_are_visible(self):
        cases = (
            ({"detail": "record exceeds frozen tool-call budget"}, "detail=record exceeds frozen tool-call budget"),
            ({"missing": ["record.json", "workspace/RESULT.md"]}, "missing=record.json, workspace/RESULT.md"),
            ({"tampered": ["TASK.md"]}, "tampered=TASK.md"),
            ({"unexpected_files": ["workspace/extra.py"]}, "unexpected_files=workspace/extra.py"),
            ({"symlinks": ["actor/workspace/link"]}, "symlinks=actor/workspace/link"),
        )
        for fields, expected in cases:
            with self.subTest(fields=fields):
                state = "incomplete" if "missing" in fields else "invalid"
                cell = {"id": "case", "status": state, "record_kind": None, **fields}
                self.assertIn(expected, report.render(packet(cell)))

    def test_rejection_diagnostics_cannot_add_rows_or_terminal_controls(self):
        value = packet({"id": "case", "status": "invalid", "record_kind": None,
                        "detail": "bad\nFORGED |\x1b[31m", "tampered": ["a\r\nb"]})
        output = report.render(value)
        self.assertIn("detail=bad FORGED \\| [31m", output)
        self.assertNotIn("\nFORGED", output)
        self.assertNotIn("\x1b", output)

    def test_projection_preserves_input_and_does_not_dump_raw_logs(self):
        value = packet({"id": "case", "status": "failed", "record_kind": "replay",
                        "record": {"elapsed_seconds": 0, "tool_calls": None},
                        "acceptance": {"status": "failed", "stdout": "PRIVATE_RAW_LOG", "stderr": "PRIVATE_ERROR"}})
        original = deepcopy(value)
        output = report.render(value)
        self.assertEqual(original, value)
        self.assertIn("| case | failed | replay | 0 | unknown |", output)
        self.assertNotIn("PRIVATE_RAW_LOG", output)
        self.assertNotIn("PRIVATE_ERROR", output)


if __name__ == "__main__":
    unittest.main()

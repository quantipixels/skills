#!/usr/bin/env python3
"""Display current engineering evidence without running models or changing a study."""
from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
from pathlib import Path
import sys
import tempfile
from typing import Any


def current_summary(study: Path, checks: Path) -> dict[str, Any]:
    """Reuse the existing identity, completeness and freshness validation."""
    source = Path(__file__).with_name("evaluate.py")
    spec = importlib.util.spec_from_file_location("qp_engineering_evaluate", source)
    if spec is None or spec.loader is None:
        raise ValueError("engineering checker is unavailable")
    evaluator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(evaluator)
    with tempfile.TemporaryDirectory(prefix="qp-evidence-view-") as temporary:
        return evaluator.summary(argparse.Namespace(
            study=study, checks=checks, output=Path(temporary) / "summary.json",
        ))


def text(value: Any) -> str:
    """Keep recorded text from adding rows or terminal control sequences."""
    if value is None:
        return "unknown"
    return "".join(char if char.isprintable() else " " for char in str(value)).replace("|", "\\|")


def render(summary: dict[str, Any]) -> str:
    cells = summary["cells"]
    counts = Counter(cell.get("status", "unknown") for cell in cells)
    config = summary["configuration"]
    lines = [
        "CURRENT EVIDENCE REPORT - not an acceptance or improvement verdict",
        text(summary["question"]),
        "Frozen configuration: " + " / ".join(text(config.get(key)) for key in ("host", "model", "reasoning")),
        "Results: " + ", ".join(f"{count} {text(status)}" for status, count in sorted(counts.items())),
        "",
        "| Cell | Result | Evidence kind | Seconds | Tool calls |",
        "| --- | --- | --- | --- | --- |",
    ]
    for cell in cells:
        record = cell.get("record") or {}
        values = (cell["id"], cell.get("status"), cell.get("record_kind"),
                  record.get("elapsed_seconds"), record.get("tool_calls"))
        lines.append("| " + " | ".join(text(value) for value in values) + " |")
    details = []
    for cell in cells:
        checks = []
        for key in ("returned_tests", "acceptance", "acceptance_against_original",
                    "baseline_tests", "tests_against_original",
                    "feature_acceptance", "feature_acceptance_against_original"):
            result = cell.get(key)
            if isinstance(result, dict) and result.get("status") is not None:
                checks.append(f"{key}={text(result['status'])}")
        # Integrity failures can occur before any executable check is run.
        if cell.get("detail"):
            checks.append(f"detail={text(cell['detail'])}")
        for key in ("missing", "tampered", "unexpected_files", "symlinks"):
            if cell.get(key):
                checks.append(f"{key}=" + ", ".join(text(value) for value in cell[key]))
        if checks:
            details.append(f"{text(cell['id'])}: " + "; ".join(checks))
    if details:
        lines.extend(["", "Check details (original rejection can be expected):", *details])
    isolation = summary.get("isolation_limitations", {})
    lines.extend([
        "",
        "Unisolated model runs: " + ", ".join(map(text, isolation.get("unisolated_model_runs", [])))
        if isolation.get("unisolated_model_runs") else "Unisolated model runs: none recorded",
        "Unknown or non-model isolation: " + ", ".join(map(text, isolation.get("unknown_or_non_model_cells", [])))
        if isolation.get("unknown_or_non_model_cells") else "Unknown or non-model isolation: none recorded",
        "",
        text(summary.get("comparison")),
        text(summary.get("evidence_limit")),
        "Unknown measurements are not zero. Frozen settings are not independent runtime telemetry.",
        "Raw checks and traces remain at their existing locations; this view does not recompute acceptance.",
    ])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    parser.add_argument("--checks", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        output = render(current_summary(args.study.resolve(), args.checks.resolve()))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Cannot display current evidence: {text(error)}", file=sys.stderr)
        return 2
    print(output, end="")
    # Zero means a validated report was displayed, not that any actor passed.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

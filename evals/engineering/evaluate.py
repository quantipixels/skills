#!/usr/bin/env python3
"""Prepare, check, and summarize the bounded Alága engineering comparison."""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIXTURES = HERE / "fixtures"
ORACLE = HERE / "oracle.py"
SKILL = ROOT / "skills" / "alaga"
CELLS = (
    ("settlement-control-r1", "settlement", "control", 1),
    ("settlement-alaga-r1", "settlement", "alaga", 1),
    ("batching-alaga-r1", "batching", "alaga", 1),
    ("batching-control-r1", "batching", "control", 1),
    ("settlement-alaga-r2", "settlement", "alaga", 2),
    ("settlement-control-r2", "settlement", "control", 2),
    ("batching-control-r2", "batching", "control", 2),
    ("batching-alaga-r2", "batching", "alaga", 2),
)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write("\n")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_hashes(root):
    hashes = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink is not allowed: {path}")
        if path.is_file():
            hashes[path.relative_to(root).as_posix()] = digest(path)
    return hashes


def git_source():
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True
    )
    return result.stdout.strip() if result.returncode == 0 else None


def require_positive(name, value):
    if type(value) not in (int, float) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive")


def is_cache_file(relative):
    path = Path(relative)
    return path.suffix == ".pyc" and "__pycache__" in path.parts


def tree_hash(root):
    files = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            files[relative] = {"kind": "symlink", "target": os.readlink(path)}
        elif path.is_file() and not is_cache_file(relative):
            files[relative] = {"kind": "file", "sha256": digest(path)}
    return hashlib.sha256(
        json.dumps(files, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def validate_manifest(manifest):
    runs = manifest.get("runs")
    if not isinstance(runs, list) or len(runs) != len(CELLS):
        raise ValueError("manifest must contain the fixed eight cells")
    expected = [(cell, case, arm, repetition) for cell, case, arm, repetition in CELLS]
    actual = [(item.get("id"), item.get("case"), item.get("arm"), item.get("repetition")) for item in runs]
    if actual != expected or len({item[0] for item in actual}) != len(CELLS):
        raise ValueError("manifest cells differ from the fixed comparison")
    budget = manifest.get("budget", {})
    require_positive("budget max_seconds_per_run", budget.get("max_seconds_per_run"))
    require_positive("budget max_tool_calls_per_run", budget.get("max_tool_calls_per_run"))
    if budget.get("runs") != 8 or budget.get("automatic_retries") != 0:
        raise ValueError("manifest budget must retain eight runs and zero automatic retries")


def prepare(args):
    require_positive("max-seconds", args.max_seconds)
    require_positive("max-tool-calls", args.max_tool_calls)
    for field in ("host", "model", "reasoning"):
        if not isinstance(getattr(args, field), str) or not getattr(args, field).strip():
            raise ValueError(f"{field} must be explicit and nonempty")
    output = args.output.absolute()
    if output.exists() or output.is_symlink():
        raise ValueError("study directory already exists; previous studies are never overwritten")
    output.mkdir(parents=True)
    runs = []
    for cell_id, case, arm, repetition in CELLS:
        run = output / "runs" / cell_id
        actor = run / "actor"
        workspace = actor / "workspace"
        private = run / "private"
        shutil.copytree(FIXTURES / case, workspace)
        (workspace / "TASK.md").replace(actor / "TASK.md")
        private.mkdir(parents=True)
        shutil.copytree(workspace, private / "original")
        shutil.copy2(actor / "TASK.md", private / "TASK.md")
        shutil.copy2(ORACLE, private / "oracle.py")
        treatment = ""
        if arm == "alaga":
            shutil.copytree(SKILL, actor / "guidance" / "alaga")
            treatment = "Read guidance/alaga/SKILL.md and any directly relevant bundled references before working.\n"
        prompt = (
            "You are a software engineer responsible for this bounded repair.\n"
            "Work only in workspace/. You may change the task's production source, test_*.py files, "
            "and RESULT.md. Do not use network, Git, workers, or files outside actor/. Do not install dependencies.\n"
            + treatment
            + "Read TASK.md, implement the repair, run its tests, and write RESULT.md.\n"
        )
        (actor / "PROMPT.md").write_text(prompt, encoding="utf-8")
        protected = {
            "TASK.md": digest(actor / "TASK.md"),
            "PROMPT.md": digest(actor / "PROMPT.md"),
        }
        if case == "settlement":
            protected["workspace/provider.py"] = digest(workspace / "provider.py")
        for name, value in file_hashes(actor / "guidance").items() if (actor / "guidance").exists() else ():
            protected[f"guidance/{name}"] = value
        private_hashes = file_hashes(private)
        write_new(run / "record.template.json", {
            "record_kind": "unrun",
            "host": args.host,
            "model": args.model,
            "reasoning": args.reasoning,
            "isolated_host_sandbox": None,
            "trace": None,
            "elapsed_seconds": None,
            "tool_calls": None,
            "input_tokens": None,
            "output_tokens": None,
            "cost_usd": None,
            "note": "Copy to record.json after execution; choose model-run, replay, or mechanical-validation.",
        })
        runs.append({
            "id": cell_id, "case": case, "arm": arm, "repetition": repetition,
            "path": f"runs/{cell_id}", "protected_hashes": protected,
            "private_hashes": private_hashes,
        })
    manifest = {
        "version": 1,
        "question": "Does explicitly supplied current Alaga improve these repairs over the same host without optional QP guidance?",
        "source_revision": git_source(),
        "checker_sha256": digest(Path(__file__)),
        "host": args.host,
        "model": args.model,
        "reasoning": args.reasoning,
        "budget": {"max_seconds_per_run": args.max_seconds, "max_tool_calls_per_run": args.max_tool_calls, "runs": 8, "automatic_retries": 0},
        "execution": "external native model host; this CLI makes no model calls",
        "sandbox": "Prefer a host-enforced isolated actor sandbox; disclose assignment-only execution as isolated_host_sandbox=false.",
        "runs": runs,
    }
    write_new(output / "manifest.json", manifest)
    return {"study": str(output), "runs": [item["id"] for item in runs], "status": "prepared-not-run"}


def subprocess_result(command, cwd, timeout):
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=timeout, env=env)
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else error.stderr or ""
        return {"status": "timeout", "exit_code": None, "stdout": stdout, "stderr": stderr}
    except OSError as error:
        return {"status": "error", "exit_code": None, "stdout": "", "stderr": f"{type(error).__name__}: {error}"}
    return {"status": "completed", "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}


def classify_tests(result):
    if result["status"] != "completed":
        return result["status"]
    output = result["stdout"] + result["stderr"]
    match = re.search(r"Ran (\d+) tests?", output)
    if not match:
        return "error"
    if int(match.group(1)) == 0:
        return "no-tests"
    skipped = re.search(r"skipped=(\d+)", output)
    if skipped and int(skipped.group(1)) >= int(match.group(1)):
        return "no-tests"
    if result["exit_code"] == 0 and re.search(r"^OK(?: |$)", output, re.MULTILINE):
        return "passed"
    errors = re.search(r"errors=(\d+)", output)
    failures = re.search(r"failures=(\d+)", output)
    if "ERROR:" in output or (errors and int(errors.group(1)) > 0) or "ImportError" in output:
        return "error"
    if result["exit_code"] != 0 and failures and int(failures.group(1)) > 0 and "FAILED" in output:
        return "failed"
    return "error"


def classify_oracle(result):
    if result["status"] != "completed":
        return result["status"]
    try:
        items = json.loads(result["stdout"])
    except (json.JSONDecodeError, TypeError):
        return "error"
    states = {item.get("status") for item in items}
    if "error" in states:
        return "error"
    if result["exit_code"] == 0 and states == {"pass"}:
        return "passed"
    return "failed"


def validate_record(record, manifest):
    kind = record.get("record_kind")
    if kind not in ("model-run", "replay", "mechanical-validation"):
        raise ValueError("record_kind must be model-run, replay, or mechanical-validation")
    for field in ("host", "model", "reasoning"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError(f"record requires {field}")
        if record[field] != manifest[field]:
            raise ValueError(f"record {field} differs from the frozen study")
    if kind == "model-run":
        if type(record.get("isolated_host_sandbox")) is not bool:
            raise ValueError("model-run requires a boolean isolated_host_sandbox disclosure")
        if not isinstance(record.get("trace"), str) or not record["trace"].strip():
            raise ValueError("model-run requires a trace locator")
    for field in ("elapsed_seconds", "tool_calls", "input_tokens", "output_tokens", "cost_usd"):
        value = record.get(field)
        if value is not None and (type(value) not in (int, float) or not math.isfinite(value) or value < 0):
            raise ValueError(f"invalid measurement: {field}")
    if record.get("elapsed_seconds") is not None and record["elapsed_seconds"] > manifest["budget"]["max_seconds_per_run"]:
        raise ValueError("record exceeds frozen elapsed-time budget")
    if record.get("tool_calls") is not None and record["tool_calls"] > manifest["budget"]["max_tool_calls_per_run"]:
        raise ValueError("record exceeds frozen tool-call budget")
    return kind


def copy_without_cache(source, destination):
    shutil.copytree(
        source, destination, dirs_exist_ok=True,
        ignore=lambda _directory, names: {name for name in names if name == "__pycache__"},
    )


def check_cell(study, manifest, spec, timeout):
    run = study / spec["path"]
    actor = run / "actor"
    workspace = actor / "workspace"
    base = {"id": spec["id"], "case": spec["case"], "arm": spec["arm"], "repetition": spec["repetition"]}
    if not run.is_dir():
        return {**base, "status": "missing", "record_kind": None}
    if not actor.is_dir() or not workspace.is_dir():
        return {**base, "status": "missing", "record_kind": None, "checked_sha256": tree_hash(run)}
    changed = []
    symlinks = [path.relative_to(run).as_posix() for path in run.rglob("*") if path.is_symlink()]
    for relative, expected in spec["protected_hashes"].items():
        path = actor / relative
        if not path.is_file() or path.is_symlink() or digest(path) != expected:
            changed.append(relative)
    for relative, expected in spec["private_hashes"].items():
        path = run / "private" / relative
        if not path.is_file() or path.is_symlink() or digest(path) != expected:
            changed.append(f"private/{relative}")
    allowed = {"RESULT.md"}
    allowed.add("settlement.py" if spec["case"] == "settlement" else "batching.py")
    unexpected = []
    expected_guidance = {name for name in spec["protected_hashes"] if name.startswith("guidance/")}
    for path in actor.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(actor).as_posix()
        if relative in ("TASK.md", "PROMPT.md") or relative.startswith("workspace/") or relative in expected_guidance:
            continue
        unexpected.append(relative)
    for path in workspace.rglob("*"):
        if path.is_file() or path.is_symlink():
            relative = path.relative_to(workspace).as_posix()
            if not path.is_symlink() and is_cache_file(relative):
                continue
            provider_allowed = spec["case"] == "settlement" and relative == "provider.py"
            if relative not in allowed and not (path.parent == workspace and path.name.startswith("test_") and path.suffix == ".py") and not provider_allowed:
                unexpected.append(relative)
    if changed or unexpected or symlinks:
        return {**base, "status": "invalid", "record_kind": None, "checked_sha256": tree_hash(run), "tampered": changed, "unexpected_files": sorted(set(unexpected)), "symlinks": symlinks}
    submitted_sha256 = tree_hash(actor)
    checked_sha256 = tree_hash(run)
    record_path = run / "record.json"
    result_path = workspace / "RESULT.md"
    has_record = record_path.is_file()
    has_result = result_path.is_file()
    if not has_record and not has_result:
        untouched = tree_hash(workspace) == tree_hash(run / "private" / "original")
        return {
            **base,
            "status": "unrun" if untouched else "incomplete",
            "record_kind": None,
            "submitted_sha256": submitted_sha256,
            "checked_sha256": checked_sha256,
            **({} if untouched else {"record": None, "missing": ["record.json", "workspace/RESULT.md"]}),
        }
    record = None
    kind = None
    if has_record:
        try:
            record = read_json(record_path)
            kind = validate_record(record, manifest)
        except (ValueError, OSError, json.JSONDecodeError) as error:
            return {**base, "status": "invalid", "record_kind": None, "submitted_sha256": submitted_sha256, "checked_sha256": checked_sha256, "detail": str(error)}
    if not has_record or not has_result:
        missing = []
        if not has_record:
            missing.append("record.json")
        if not has_result:
            missing.append("workspace/RESULT.md")
        return {**base, "status": "incomplete", "record_kind": kind, "submitted_sha256": submitted_sha256, "checked_sha256": checked_sha256, "record": record, "missing": missing}
    with tempfile.TemporaryDirectory() as temporary:
        candidate = Path(temporary) / "candidate"
        copy_without_cache(workspace, candidate)
        tests = subprocess_result([sys.executable, "-m", "unittest", "discover", "-v"], candidate, timeout)
        tests["status"] = classify_tests(tests)
    with tempfile.TemporaryDirectory() as temporary:
        candidate = Path(temporary) / "candidate"
        copy_without_cache(workspace, candidate)
        oracle = subprocess_result([sys.executable, str(run / "private" / "oracle.py"), str(candidate), spec["case"]], candidate, timeout)
        oracle["status"] = classify_oracle(oracle)
    with tempfile.TemporaryDirectory() as temporary:
        original = Path(temporary)
        copy_without_cache(run / "private" / "original", original)
        for old_test in original.glob("test_*.py"):
            old_test.unlink()
        for test in workspace.glob("test_*.py"):
            shutil.copy2(test, original / test.name)
        regression = subprocess_result([sys.executable, "-m", "unittest", "discover", "-v"], original, timeout)
        regression["status"] = classify_tests(regression)
    with tempfile.TemporaryDirectory() as temporary:
        baseline = Path(temporary)
        copy_without_cache(run / "private" / "original", baseline)
        production = "settlement.py" if spec["case"] == "settlement" else "batching.py"
        candidate_source = workspace / production
        if candidate_source.is_file():
            shutil.copy2(candidate_source, baseline / production)
        baseline_tests = subprocess_result([sys.executable, "-m", "unittest", "discover", "-v"], baseline, timeout)
        baseline_tests["status"] = classify_tests(baseline_tests)
    statuses = (tests["status"], oracle["status"], regression["status"], baseline_tests["status"])
    if "timeout" in statuses:
        status = "timeout"
    elif "error" in statuses:
        status = "error"
    elif tests["status"] == "passed" and oracle["status"] == "passed" and regression["status"] == "failed" and baseline_tests["status"] == "passed":
        status = "passed"
    else:
        status = "failed"
    return {**base, "status": status, "record_kind": kind, "submitted_sha256": submitted_sha256, "checked_sha256": checked_sha256, "record": record, "returned_tests": tests, "acceptance": oracle, "tests_against_original": regression, "baseline_tests": baseline_tests}


def check(args):
    study = args.study.resolve()
    manifest = read_json(study / "manifest.json")
    validate_manifest(manifest)
    if manifest.get("checker_sha256") != digest(Path(__file__)):
        raise ValueError("checker implementation differs from the version frozen at prepare")
    require_positive("timeout", args.timeout)
    results = [check_cell(study, manifest, spec, args.timeout) for spec in manifest["runs"]]
    report = {"version": 1, "study": str(study), "manifest_sha256": digest(study / "manifest.json"), "trusted_execution_only": "Runs returned Python in disposable copies with timeouts; this is not security isolation.", "results": results}
    write_new(args.output.absolute(), report)
    return report


def summary(args):
    study = args.study.resolve()
    manifest = read_json(study / "manifest.json")
    validate_manifest(manifest)
    if manifest.get("checker_sha256") != digest(Path(__file__)):
        raise ValueError("checker implementation differs from the version frozen at prepare")
    checked = read_json(args.checks.resolve())
    if Path(checked.get("study", "")).resolve() != study or checked.get("manifest_sha256") != digest(study / "manifest.json"):
        raise ValueError("check report belongs to a different or changed study")
    results = checked.get("results", [])
    ids = [item.get("id") for item in results]
    expected_ids = [item["id"] for item in manifest["runs"]]
    if len(ids) != len(set(ids)) or set(ids) != set(expected_ids):
        raise ValueError("check report must contain each expected cell exactly once")
    by_id = {item["id"]: item for item in results}
    for spec in manifest["runs"]:
        item = by_id[spec["id"]]
        if item.get("checked_sha256") is not None:
            run = study / spec["path"]
            if not run.is_dir() or tree_hash(run) != item["checked_sha256"]:
                raise ValueError(f"stale check result for {spec['id']}")
        elif (study / spec["path"]).exists():
            raise ValueError(f"stale check result for {spec['id']}")
    cells = []
    for spec in manifest["runs"]:
        result = by_id.get(spec["id"])
        cells.append(result if result is not None else {
            "id": spec["id"], "case": spec["case"], "arm": spec["arm"],
            "repetition": spec["repetition"], "status": "missing", "record_kind": None,
        })
    kinds = sorted({item.get("record_kind") for item in cells if item.get("record_kind")})
    unisolated = [
        item["id"] for item in cells
        if item.get("record_kind") == "model-run"
        and item.get("record", {}).get("isolated_host_sandbox") is False
    ]
    isolation_unknown = [
        item["id"] for item in cells
        if item.get("record_kind") != "model-run"
        or type(item.get("record", {}).get("isolated_host_sandbox")) is not bool
    ]
    report = {
        "version": 1, "question": manifest["question"], "configuration": {key: manifest[key] for key in ("host", "model", "reasoning", "budget")},
        "cells": cells, "record_kinds_present": kinds,
        "isolation_limitations": {
            "unisolated_model_runs": unisolated,
            "unknown_or_non_model_cells": isolation_unknown,
            "claim": "Assignment-only or unknown isolation does not support a clean-room or causal claim.",
        },
        "comparison": "No winner is inferred from pass counts. Review scope, extra state, architecture, explanations, and intervention cost independently before any keep/revert judgment.",
        "evidence_limit": "Replay and mechanical-validation records are never model-performance evidence; missing and unrun cells remain explicit.",
    }
    write_new(args.output.absolute(), report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare", help="freeze all eight comparison cells")
    prep.add_argument("--output", type=Path, required=True)
    prep.add_argument("--host", required=True)
    prep.add_argument("--model", required=True)
    prep.add_argument("--reasoning", required=True)
    prep.add_argument("--max-seconds", type=float, required=True)
    prep.add_argument("--max-tool-calls", type=int, required=True)
    verify = commands.add_parser("check", help="run mechanical checks on every expected cell")
    verify.add_argument("--study", type=Path, required=True)
    verify.add_argument("--output", type=Path, required=True)
    verify.add_argument("--timeout", type=float, default=30)
    report = commands.add_parser("summary", help="emit a complete, provenance-separated table")
    report.add_argument("--study", type=Path, required=True)
    report.add_argument("--checks", type=Path, required=True)
    report.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        value = prepare(args) if args.command == "prepare" else check(args) if args.command == "check" else summary(args)
        print(json.dumps(value, indent=2, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        parser.exit(1, f"Evaluation rejected: {error}\n")


if __name__ == "__main__":
    main()

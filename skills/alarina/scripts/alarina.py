#!/usr/bin/env python3
"""Bounded Alárinà mechanics. Only verification operations execute configured checks."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import importlib
import sys
import uuid

from project_context import (
    ContextError, contained_path, doctor, load_context, read_json, resolve_destination,
)

INSPECTION_COMMANDS = {
    "resume-inspect": ("resume_inspection", "Inspect selected continuity records and current receipt freshness"),
    "ci-drift": ("ci_drift", "Inspect workflow/local-check drift and optional provider requirements"),
    "installation-inspect": ("installation_diagnostics", "Compare source, installed files and supplied discovery evidence"),
    "verify-container": ("container_verification", "Run the existing full verifier in a suitable running dev container"),
}


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="operation", required=True)
    for name in ("config", "paths", "doctor", "verify", "freshness", "workflows"):
        command = sub.add_parser(name)
        command.add_argument("--project", type=Path, default=Path.cwd())
        command.add_argument("--task", help="Stable task identity reused across resumption; not a new timestamp")
        if name == "paths":
            command.add_argument("--kind", choices=("artifact", "record", "workflow", "portable-workflow"), default="artifact")
            command.add_argument("--name", help="Relative name below the chosen root")
            command.add_argument("--destination", help="Exact explicit user destination; overrides fallback roots")
            command.add_argument("--established-root", help="Existing destination established by project/user instructions")
        if name == "verify":
            command.add_argument("--check", action="append", help="Run only these registered IDs; default runs all")
            command.add_argument("--output", type=Path, help="New private run directory; default is isolated task records")
            command.add_argument("--base", help="Integration base ref/commit to bind to the evidence")
        if name == "freshness":
            command.add_argument("receipt", type=Path)
            command.add_argument("--base", help="Current integration base; defaults to the receipt's base")
        if name == "workflows":
            command.add_argument("--path", type=Path, help="Validate one existing Markdown recipe")
            command.add_argument("--root", action="append", type=Path, help="Explicit roots instead of the current project's library")
    contribution = sub.add_parser("contribution-check", help="Inspect one curated proposal locally; never submit it")
    contribution.add_argument("path", type=Path)
    for name, (_, description) in INSPECTION_COMMANDS.items():
        sub.add_parser(name, help=description, description=f"Use {name} --help for this operation's arguments.")
    return root


def execute(args) -> tuple[dict, int]:
    if args.operation == "contribution-check":
        from workflow_tools import inspect_contribution
        result = inspect_contribution(args.path)
        return result, 0 if result["status"] == "no-patterns-found" else 1
    context = load_context(args.project, args.task)
    if args.operation == "config":
        return context, 0
    if args.operation == "paths":
        return resolve_destination(context, kind=args.kind, name=args.name,
                                   destination=args.destination, established_root=args.established_root), 0
    if args.operation == "doctor":
        result = doctor(context)
        return result, 0 if result["status"] == "configured" else 1
    if args.operation == "workflows":
        from workflow_tools import inventory_workflows, validate_workflow
        if args.path:
            result = validate_workflow(args.path)
            return result, 1 if result["classification"] == "invalid" else 0
        roots = args.root
        root_scopes = {}
        absent = []
        if roots is None:
            roots = [Path(context["locations"][key]) for key in ("project_workflows", "portable_workflows")]
            roots += [contained_path(Path(context["project"]["root"]), value, "workflow_roots")
                      for value in context["config"]["workflow_roots"]]
            root_scopes = {str(path): "project" for path in roots}
            root_scopes[context["locations"]["portable_workflows"]] = "portable"
            absent = [str(path) for path in roots if not path.exists() and not path.is_symlink()]
            roots = [path for path in roots if path.exists() or path.is_symlink()]
        result = inventory_workflows(roots, root_scopes=root_scopes)
        result["absent_optional_roots"] = absent
        result["project_id"] = context["project"]["id"]
        invalid = result["errors"] or any(item["classification"] == "invalid" for item in result["workflows"])
        return result, 1 if invalid else 0
    from local_checks import check_freshness, run_checks
    project = Path(context["project"]["root"])
    if args.operation == "freshness":
        result = check_freshness(project, read_json(args.receipt), config_digest=context["config_digest"], base=args.base)
        return result, 0 if result.get("fresh") is True else 1
    checks = context["config"]["checks"]
    requested = set(args.check or [])
    known = {check["id"] for check in checks}
    if requested - known:
        raise ContextError("unknown check IDs: " + ", ".join(sorted(requested - known)))
    selected = [check for check in checks if not requested or check["id"] in requested]
    output = args.output
    if output is None:
        if not context["locations"]["task_root"]:
            raise ContextError("verify requires --task for private records, or an explicit --output directory")
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        output = Path(context["locations"]["task_root"]) / "checks" / f"{stamp}-{uuid.uuid4().hex[:8]}"
        if output.parent.resolve() != output.parent:
            raise ContextError("default check output has a symlink parent")
    output = (project / output.expanduser()).resolve()
    result = run_checks(project, selected, output, base=args.base, config_digest=context["config_digest"])
    result["selection"] = {"executed_ids": [check["id"] for check in selected],
                           "not_selected": sorted(known - {check["id"] for check in selected})}
    if result["gate_status"] == "passed" and result["selection"]["not_selected"]:
        result["selected_status"] = "passed"
        result["gate_status"] = "partial"
    result["remote_checks"] = context["config"]["remote_checks"]
    result["receipt_path"] = str(output / "receipt.json")
    try:
        after_context = load_context(args.project, args.task)
        if after_context["config_digest"] != context["config_digest"]:
            result["gate_status"] = "stale"
            result["config_error"] = "configuration changed during checks"
    except ContextError:
        result["gate_status"] = "stale"
        result["config_error"] = "configuration became invalid during checks"
    (output / "receipt.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result, 0 if result.get("gate_status") in {"passed", "partial"} else 1


def main(argv=None) -> int:
    supplied = list(sys.argv[1:] if argv is None else argv)
    if supplied and supplied[0] in INSPECTION_COMMANDS:
        module, _ = INSPECTION_COMMANDS[supplied[0]]
        return importlib.import_module(module).main(supplied[1:])
    args = parser().parse_args(supplied)
    try:
        result, code = execute(args)
    except (ContextError, ValueError, OSError, RuntimeError) as error:
        print(json.dumps({"error": str(error), "status": "invalid-or-blocked"}, ensure_ascii=False), file=sys.stderr)
        return 2
    # Keep complete candidate inventories in the retained receipt; stdout is a
    # usable handoff rather than two copies of every repository filename.
    for field in ("snapshot_before", "snapshot_after", "current_snapshot"):
        if isinstance(result.get(field), dict):
            snapshot = result[field]
            result[field] = {key: snapshot[key] for key in (
                "candidate_digest", "kind", "head", "base", "base_oid", "complete", "limitations"
            ) if key in snapshot}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())

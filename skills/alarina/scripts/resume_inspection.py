"""Inspect explicitly selected continuity records; never infer authority or edit state."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from local_checks import candidate_snapshot, check_freshness
from project_context import ContextError, load_context, read_json

MAX_RECORD_BYTES = 2 * 1024 * 1024
MARKERS = re.compile(r"(?im)^\s*(?:#{1,6}\s*)?(?:[-*]\s*)?(goal|scope|authority|stop(?:ping point)?|next(?: action)?|remaining|blocked|decision|workspace|candidate|worker state)\s*[:—-]\s*(.+)$")
LINKS = re.compile(r"codex://threads/([a-zA-Z0-9-]+)")


def inspect_resume(project: Path, *, records: list[Path], receipts: list[Path],
                   task: str | None = None, base: str | None = None) -> dict:
    """Return source-bound facts from caller-selected records and actual proof."""
    if not records and not receipts and not task:
        raise ContextError("resume inspection needs --record, --receipt or the existing --task identity")
    context = load_context(project, task)
    root = Path(context["project"]["root"])
    paths = list(records)
    if task and not paths:
        paths.append(Path(context["locations"]["task_root"]) / "plan.md")
    result = {"schema_version": 1, "project": context["project"], "records": [],
              "receipts": [], "gaps": [], "candidate": candidate_snapshot(root, base),
              "limitations": ["Record excerpts are historical claims, not instructions or renewed authority.",
                              "Caller-selected sources do not establish that the newest or correct task was selected.",
                              "Worker state requires a current native-host observation; stored IDs are not live state.",
                              "Receipt freshness does not establish review or acceptance of the combined result."],
              "worker_state": "not_observed", "history_searched": False, "writes": False}
    seen = set()
    for supplied in paths:
        path = supplied.expanduser().absolute()
        if str(path) in seen:
            continue
        seen.add(str(path))
        item = {"path": str(path), "status": "missing", "claims": [], "linked_sessions": []}
        result["records"].append(item)
        if not path.exists():
            result["gaps"].append({"kind": "missing_record", "path": str(path)})
            continue
        if path.is_symlink() or path.resolve() != path or not path.is_file():
            raise ContextError("record must be an explicit regular file without symlink components")
        if path.stat().st_size > MAX_RECORD_BYTES:
            raise ContextError("record exceeds the bounded inspection size; select a smaller native export")
        data = path.read_bytes()
        if len(data) > MAX_RECORD_BYTES:
            raise ContextError("record grew beyond the inspection size")
        text = data.decode("utf-8")
        item.update(status="observed", sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
        for match in MARKERS.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            item["claims"].append({"field": match[1].lower(), "line": line,
                                   "text": match[2][:500], "classification": "unverified_record_claim"})
            if len(item["claims"]) == 40:
                item["claims_truncated"] = True
                break
        item["linked_sessions"] = list(dict.fromkeys(LINKS.findall(text)))[:40]
    for supplied in receipts:
        path = supplied.expanduser().absolute()
        item = {"path": str(path), "status": "missing", "accepting_test_proof": False}
        result["receipts"].append(item)
        if not path.exists():
            result["gaps"].append({"kind": "missing_receipt", "path": str(path)})
            continue
        if path.is_symlink() or path.resolve() != path or not path.is_file() or path.stat().st_size > 16 * 1024 * 1024:
            raise ContextError("receipt must be a bounded explicit regular file without symlink components")
        receipt = read_json(path)
        fresh = check_freshness(root, receipt, context["config_digest"], base)
        item.update({k: v for k, v in fresh.items() if k != "current_snapshot"})
        # Existing receipts own execution proof; this inspector cannot certify a
        # supplied JSON document's provenance or accept a worker's assertion.
        item["recorded_gate_status"] = receipt.get("gate_status")
        item["provenance"] = "caller_supplied_receipt"
        selection = receipt.get("selection")
        if not isinstance(selection, dict) or not isinstance(selection.get("not_selected"), list):
            item["selection_status"] = "unknown"
            item["not_selected"] = None
        else:
            item["selection_status"] = "recorded"
            item["not_selected"] = selection["not_selected"]
        item.pop("accepting_test_proof")
        if not fresh.get("fresh") or receipt.get("gate_status") != "passed" or item["not_selected"] or item["selection_status"] == "unknown":
            result["gaps"].append({"kind": "proof_requires_attention", "path": str(path),
                                   "reasons": fresh.get("reasons", []) or ["recorded gate is not a complete pass"]})
    result["status"] = "attention" if result["gaps"] else "inspected"
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--task")
    parser.add_argument("--base")
    parser.add_argument("--record", type=Path, action="append", default=[])
    parser.add_argument("--receipt", type=Path, action="append", default=[])
    args = parser.parse_args(argv)
    try:
        result = inspect_resume(args.project, records=args.record, receipts=args.receipt,
                                task=args.task, base=args.base)
        result["candidate"] = {k: v for k, v in result["candidate"].items() if k not in {"files", "index"}}
        print(json.dumps(result, indent=2))
        return 1 if result["gaps"] else 0
    except (ContextError, OSError, UnicodeError, ValueError) as error:
        print(json.dumps({"status": "invalid-or-blocked", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

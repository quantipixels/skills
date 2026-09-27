"""Read-only discovery and privacy preflight for Alárinà workflow artifacts.

Structured recipes opt in by starting with this exact fenced JSON block::

    ```alarina-workflow+json
    {"version": 1, "id": "short-id", "title": "Useful title",
     "scope": "project", "status": "verified",
     "assumptions": ["Applies to a project with a working CLI"],
     "steps": [{"method": "alaga-verify-project", "produces": ["journey proof"]}],
     "evidence": [{"result": "passed", "locator": "local evidence pointer",
                   "candidate": "revision or exact candidate"}],
     "retirement": "Recheck when the CLI contract changes"}
    ```

Only fenced recipes in explicitly supplied workflow roots are indexed. Plain
project documentation is outside this API; a Markdown file inside a supplied
workflow root without the fence is reported as unstructured. The parser checks
shape and declared evidence, never the truth of a result.
It does not execute a recipe, search unspecified roots, or publish anything.

Contribution proposals use a separate ``alarina-contribution+json`` fence
containing only version, purpose, generic_change, synthetic_example,
challenges, benefits, evidence_limits, and sanitized_test_result. The privacy
preflight returns categories and line numbers, never proposal text or matches.
"""

from __future__ import annotations

import json
import ipaddress
import os
import re
from pathlib import Path
from typing import Any


WORKFLOW_FENCE = "```alarina-workflow+json"
CONTRIBUTION_FENCE = "```alarina-contribution+json"
MAX_BYTES = 1_000_000
WORKFLOW_KEYS = {
    "version", "id", "title", "scope", "status", "assumptions", "steps",
    "evidence", "retirement",
}
CONTRIBUTION_KEYS = {
    "version", "purpose", "generic_change", "synthetic_example",
    "challenges", "benefits", "evidence_limits", "sanitized_test_result",
}
ID_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def _error(code: str, detail: str) -> dict[str, str]:
    return {"code": code, "detail": detail}


def _read_text(path: Path) -> tuple[str | None, list[dict[str, str]]]:
    if path.is_symlink():
        return None, [_error("symlink", "Use a regular Markdown file, not a symlink.")]
    if not path.is_file():
        return None, [_error("not-file", "The supplied path is not a regular file.")]
    if path.suffix.lower() != ".md":
        return None, [_error("not-markdown", "Use a .md file.")]
    try:
        if path.stat().st_size > MAX_BYTES:
            return None, [_error("too-large", "File exceeds the 1 MB inspection limit.")]
        return path.read_text(encoding="utf-8"), []
    except (OSError, UnicodeError) as exc:
        return None, [_error("unreadable", f"Cannot read UTF-8 Markdown ({type(exc).__name__}).")]


def _parse_fence(text: str, marker: str) -> tuple[dict[str, Any] | None, list[dict[str, str]], str]:
    lines = text.splitlines()
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first is None or lines[first] != marker:
        return None, [], "unstructured"
    close = next((i for i in range(first + 1, len(lines)) if lines[i] == "```"), None)
    if close is None:
        return None, [_error("unclosed-metadata", f"Close the {marker} block with ```.")], "structured"
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise ValueError("duplicate JSON key")
            value[key] = item
        return value

    try:
        value = json.loads("\n".join(lines[first + 1:close]), object_pairs_hook=unique_object)
    except json.JSONDecodeError as exc:
        return None, [_error("malformed-json", f"Metadata JSON is invalid at line {first + exc.lineno + 1}.")], "structured"
    except ValueError as exc:
        if str(exc) == "duplicate JSON key":
            return None, [_error("duplicate-key", "Metadata contains a duplicate JSON key; each key must occur once.")], "structured"
        raise
    if not isinstance(value, dict):
        return None, [_error("metadata-object", "Metadata must be a JSON object.")], "structured"
    return value, [], "structured"


def _strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and bool(item.strip()) for item in value)


def validate_workflow(path: Path) -> dict[str, Any]:
    """Validate one structured recipe without running it or claiming proof."""
    path = Path(path)
    text, errors = _read_text(path)
    result: dict[str, Any] = {
        "path": str(path), "classification": "invalid",
        "usable_as_guidance": False, "metadata": None, "errors": errors,
        "semantic_verification": "not-assessed",
    }
    if text is None:
        return result
    data, parse_errors, kind = _parse_fence(text, WORKFLOW_FENCE)
    if kind == "unstructured":
        errors.append(_error("unstructured", "Workflow recipes need a first alarina-workflow+json fenced block."))
        return result
    result["classification"] = "structured"
    errors.extend(parse_errors)
    if data is None:
        result["classification"] = "invalid"
        result["usable_as_guidance"] = False
        return result

    extra = sorted(set(data) - WORKFLOW_KEYS)
    missing = sorted(WORKFLOW_KEYS - set(data))
    if extra:
        errors.append(_error("unknown-fields", f"Remove unsupported metadata fields: {', '.join(extra)}."))
    if missing:
        errors.append(_error("missing-fields", f"Add required metadata fields: {', '.join(missing)}."))
    if data.get("version") != 1 or isinstance(data.get("version"), bool):
        errors.append(_error("version", "version must be the integer 1."))
    workflow_id = data.get("id")
    if not isinstance(workflow_id, str) or not ID_PATTERN.fullmatch(workflow_id):
        errors.append(_error("id", "id must be lowercase kebab-case, beginning with a letter."))
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        errors.append(_error("title", "title must be non-empty text."))
    if data.get("scope") not in ("project", "portable"):
        errors.append(_error("scope", "scope must be project or portable."))
    if data.get("status") not in ("draft", "verified", "retired"):
        errors.append(_error("status", "status must be draft, verified or retired."))
    if not _strings(data.get("assumptions")) or not data["assumptions"]:
        errors.append(_error("assumptions", "assumptions must be a non-empty list of non-empty strings."))
    if not isinstance(data.get("steps"), list) or not data["steps"]:
        errors.append(_error("steps", "steps must be a non-empty list."))
    else:
        for number, step in enumerate(data["steps"], 1):
            if not isinstance(step, dict) or not isinstance(step.get("method"), str) or not step["method"].strip():
                errors.append(_error("step", f"Step {number} needs a non-empty method pointer."))
                continue
            if set(step) - {"method", "requires", "produces"}:
                errors.append(_error("step-fields", f"Step {number} has unsupported fields."))
            for field in ("requires", "produces"):
                if field in step and not _strings(step[field]):
                    errors.append(_error("step-list", f"Step {number} {field} must be a list of non-empty strings."))
    evidence = data.get("evidence")
    if not isinstance(evidence, list):
        errors.append(_error("evidence", "evidence must be a list."))
    else:
        for number, item in enumerate(evidence, 1):
            if not isinstance(item, dict) or set(item) != {"result", "locator", "candidate"}:
                errors.append(_error("evidence-item", f"Evidence {number} needs result, locator and candidate only."))
                continue
            if item["result"] not in ("passed", "failed", "blocked") or any(
                not isinstance(item[key], str) or not item[key].strip() for key in ("locator", "candidate")
            ):
                errors.append(_error("evidence-item", f"Evidence {number} has an invalid value."))
        if data.get("status") == "verified" and not any(
            isinstance(item, dict) and item.get("result") == "passed"
            and isinstance(item.get("locator"), str) and item["locator"].strip()
            and isinstance(item.get("candidate"), str) and item["candidate"].strip()
            for item in evidence
        ):
            errors.append(_error("verified-proof", "A verified recipe needs a passing executed-evidence pointer and candidate."))
    if not isinstance(data.get("retirement"), str):
        errors.append(_error("retirement", "retirement must be text (empty when not applicable)."))
    if data.get("status") == "retired" and not str(data.get("retirement", "")).strip():
        errors.append(_error("retired-reason", "A retired recipe needs a retirement reason."))

    if errors:
        result["classification"] = "invalid"
        result["usable_as_guidance"] = False
        return result
    result["metadata"] = {
        "version": 1, "id": workflow_id, "title": data["title"],
        "scope": data["scope"], "status": data["status"],
        "assumptions": data["assumptions"],
        "steps": data["steps"], "evidence": data["evidence"],
        "retirement": data["retirement"],
    }
    result["usable_as_guidance"] = data["status"] != "retired"
    return result


def inventory_workflows(roots: list[Path], *, root_scopes: dict[str, str] | None = None) -> dict[str, Any]:
    """Inspect supplied roots, enforcing known library scope without executing recipes."""
    entries: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    seen_roots: set[str] = set()
    for root in sorted((Path(root) for root in roots), key=lambda p: str(p)):
        root_name = str(root)
        if root_name in seen_roots:
            errors.append(_error("duplicate-root", f"Root supplied more than once: {root_name}."))
            continue
        seen_roots.add(root_name)
        if root.is_symlink():
            errors.append(_error("root-symlink", f"Root is a symlink and was not traversed: {root_name}."))
            continue
        if not root.is_dir():
            errors.append(_error("root-unavailable", f"Root is not a readable directory: {root_name}."))
            continue
        try:
            def on_walk_error(exc: OSError) -> None:
                errors.append(_error("walk-error", f"Could not inspect a directory under {root_name} ({type(exc).__name__})."))

            for directory, dirs, files in os.walk(root, followlinks=False, onerror=on_walk_error):
                current = Path(directory)
                for name in sorted(dirs):
                    if (current / name).is_symlink():
                        errors.append(_error("directory-symlink", f"Directory symlink not traversed: {current / name}."))
                dirs[:] = sorted(name for name in dirs if not (current / name).is_symlink())
                for name in sorted(files):
                    path = current / name
                    if path.suffix.lower() == ".md":
                        entry = validate_workflow(path)
                        entry["root"] = root_name
                        expected_scope = (root_scopes or {}).get(root_name)
                        if entry["metadata"] and expected_scope and entry["metadata"]["scope"] != expected_scope:
                            entry["errors"].append(_error(
                                "library-scope", f"This library requires scope {expected_scope}; move the recipe to its owner or qualify its scope."
                            ))
                            entry["classification"] = "invalid"
                            entry["usable_as_guidance"] = False
                            entry["metadata"] = None
                        entries.append(entry)
        except OSError as exc:
            errors.append(_error("walk-error", f"Could not inspect {root_name} ({type(exc).__name__})."))
    entries.sort(key=lambda item: item["path"])
    by_id: dict[str, list[str]] = {}
    for entry in entries:
        metadata = entry["metadata"]
        if metadata is not None:
            by_id.setdefault(metadata["id"], []).append(entry["path"])
    duplicates = {key: paths for key, paths in sorted(by_id.items()) if len(paths) > 1}
    for workflow_id, paths in duplicates.items():
        errors.append(_error("duplicate-id", f"Workflow id {workflow_id} occurs in: {', '.join(paths)}."))
    return {"workflows": entries, "duplicates": duplicates, "errors": errors}


_PATTERNS = {
    "home-path": re.compile(r"(?:/Users/[^\s/]+|/home/[^\s/]+|~/[^\s/]+|[A-Za-z]:\\Users\\[^\s\\]+)"),
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "secret-value": re.compile(r"(?i)(?:\b[\"']?(?:api[_-]?key|access[_-]?token|auth[_-]?token|authorization|password|secret|private[_-]?key|token)[\"']?\s*[:=]\s*[\"']?\S+|\bBearer\s+\S+|\b(?:gh[pousr]_[A-Za-z0-9]{8,}|sk-[A-Za-z0-9_-]{8,}|AKIA[A-Z0-9]{12,})\b)"),
    "private-key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "private-url": re.compile(r"(?i)https?://(?:[^\s/@]+:[^\s/@]+@|[^\s/]*\b(?:localhost|intranet|corp|internal|private)(?:\.[^\s/]*)?(?:/|\b)|(?:10|127|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.[0-9.]+)"),
    "transcript-dump": re.compile(r"(?i)(?:agent-transcripts|rollout-[\w-]+\.jsonl|\"(?:turn_id|thread_id|message_id)\"\s*:|\"role\"\s*:\s*\"(?:user|assistant|tool)\")"),
}

_IPV4 = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")
_IPV6 = re.compile(r"(?<![\w:])(?:[0-9a-fA-F]{0,4}:){2,}[0-9a-fA-F:.%]*(?![\w:])")


def _private_address_in(value: str) -> bool:
    for pattern in (_IPV4, _IPV6):
        for match in pattern.finditer(value):
            try:
                address = ipaddress.ip_address(match.group(0).split("%", 1)[0])
            except ValueError:
                continue
            if address.is_private or address.is_loopback or address.is_link_local:
                return True
    return False


def _decoded_strings(value: Any, field: str) -> list[tuple[str, str]]:
    if isinstance(value, str):
        return [(field, value)]
    if isinstance(value, list):
        return [item for nested in value for item in _decoded_strings(nested, field)]
    if isinstance(value, dict):
        return [item for key, nested in value.items() for item in _decoded_strings(nested, field if field else key)]
    return []


def inspect_contribution(path: Path) -> dict[str, Any]:
    """Heuristically preflight one explicit curated proposal; never approve publication."""
    path = Path(path)
    text, errors = _read_text(path)
    result: dict[str, Any] = {
        "status": "needs-human-review", "fields": [],
        "findings": [], "errors": errors,
        "notice": "Local heuristic only. Human review is required; no guarantee of full anonymization or approval to publish.",
    }
    if text is None:
        return result
    data, parse_errors, kind = _parse_fence(text, CONTRIBUTION_FENCE)
    errors.extend(parse_errors)
    if kind == "unstructured":
        errors.append(_error("format", "Use the alarina-contribution+json fence with allowlisted fields only."))
    elif data is not None:
        result["fields"] = sorted(set(data) & CONTRIBUTION_KEYS)
        extra = sorted(set(data) - CONTRIBUTION_KEYS)
        missing = sorted(CONTRIBUTION_KEYS - set(data))
        if extra:
            errors.append(_error("unknown-fields", f"Remove {len(extra)} unsupported contribution field(s)."))
        if missing:
            errors.append(_error("missing-fields", f"Add required contribution fields: {', '.join(missing)}."))
        if data.get("version") != 1 or isinstance(data.get("version"), bool):
            errors.append(_error("version", "version must be the integer 1."))
        for key in CONTRIBUTION_KEYS - {"version", "challenges", "benefits"}:
            if not isinstance(data.get(key), str) or not data[key].strip():
                errors.append(_error("field-text", f"{key} must be non-empty text."))
        for key in ("challenges", "benefits"):
            if not _strings(data.get(key)) or not data[key]:
                errors.append(_error("field-list", f"{key} must be a non-empty list of non-empty strings."))
        lines = text.splitlines()
        close = next((i for i in range(1, len(lines)) if lines[i] == "```"), None)
        if close is not None and any(line.strip() for line in lines[close + 1:]):
            errors.append(_error("outside-content", "Remove content outside the allowlisted JSON block."))
    findings = []
    for number, line in enumerate(text.splitlines(), 1):
        for category, pattern in _PATTERNS.items():
            if pattern.search(line):
                findings.append({"line": number, "category": category, "source": "raw-line"})
        if _private_address_in(line):
            findings.append({"line": number, "category": "private-address", "source": "raw-line"})
    if isinstance(data, dict):
        lines = text.splitlines()
        for field, decoded in _decoded_strings(data, ""):
            # Use the allowlisted top-level field's source line; list elements
            # may occupy later lines, so this locator is intentionally coarse.
            source_line = next(
                (number for number, line in enumerate(lines, 1) if json.dumps(field) in line),
                1,
            )
            safe_field = field if field in CONTRIBUTION_KEYS else "unknown-field"
            for category, pattern in _PATTERNS.items():
                if pattern.search(decoded):
                    findings.append({"line": source_line, "category": category, "source": "decoded-field", "field": safe_field})
            if _private_address_in(decoded):
                findings.append({"line": source_line, "category": "private-address", "source": "decoded-field", "field": safe_field})
    result["findings"] = findings
    if not errors and not findings:
        result["status"] = "no-patterns-found"
    return result

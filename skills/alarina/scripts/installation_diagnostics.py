#!/usr/bin/env python3
"""Read-only comparison of explicit source, installation and discovery evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

MAX_FILE = 8 * 1024 * 1024
MAX_JSON = 128 * 1024
MAX_FILES = 2048
DECLARATIONS = (
    ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
    "agents/alarina.md", "agents/alarina.codex.toml", "agents/alarina.claude.md",
    ".opencode/agents/alarina.md", "opencode.json", "package.json", "LICENSE",
)


class DiagnosticError(ValueError):
    pass


def _json_file(path: Path) -> object:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_JSON:
        raise DiagnosticError("JSON evidence is missing, linked, or oversized")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeError, json.JSONDecodeError) as error:
        raise DiagnosticError("JSON evidence is malformed") from error


def _inventory(root: Path) -> dict[str, str]:
    if root.is_symlink() or not root.is_dir():
        raise DiagnosticError("package root is missing or linked")
    paths = [root / name for name in DECLARATIONS]
    skill = root / "skills" / "alarina"
    if not skill.is_dir() or skill.is_symlink():
        raise DiagnosticError("Alárinà skill directory is missing or linked")
    paths.extend(skill.rglob("*"))
    paths.extend(root.glob("skills/**/SKILL.md"))
    for directory in ("agents", ".opencode/agents"):
        base = root / directory
        if base.exists():
            paths.extend(path for path in base.rglob("*") if path.suffix in {".md", ".toml"})
    if len(paths) > MAX_FILES:
        raise DiagnosticError("package inventory is oversized")
    result = {}
    for path in paths:
        relative = path.relative_to(root)
        if any(part in {"__pycache__", ".pytest_cache"} for part in relative.parts) or path.name == ".DS_Store" or path.suffix in {".pyc", ".pyo"}:
            continue
        if path.is_symlink() or any((root / Path(*relative.parts[:i])).is_symlink()
                                     for i in range(1, len(relative.parts))):
            raise DiagnosticError("package contains a symlink")
        if path.is_file():
            if path.stat().st_size > MAX_FILE:
                raise DiagnosticError("package contains an oversized file")
            result[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if "skills/alarina/SKILL.md" not in result:
        raise DiagnosticError("package lacks Alárinà entry")
    return result


def _manager_evidence(data: object, installed_root: Path) -> dict:
    # The caller supplies a captured native list result. It remains supplied evidence.
    if not isinstance(data, dict) or data.get("host") not in {"codex", "claude", "opencode", "pi"}:
        raise DiagnosticError("manager evidence requires a recognized host")
    entries = data.get("plugins")
    if not isinstance(entries, list) or len(entries) > 256:
        raise DiagnosticError("manager evidence requires a bounded plugins list")
    matches = [entry for entry in entries if isinstance(entry, dict) and
               (entry.get("id") in {"qp-skills", "qp-skills@qp-skills"} or
                entry.get("pluginId") in {"qp-skills", "qp-skills@qp-skills"})]
    provenance = {key: data[key] for key in ("origin", "captured_at") if isinstance(data.get(key), str) and len(data[key]) <= 256}
    if len(matches) != 1:
        return {"status": "unknown", "reason": "no unique qp-skills registration", **provenance}
    entry = matches[0]
    value = entry.get("installedPath") or entry.get("installPath")
    if not isinstance(value, str) or not Path(value).is_absolute():
        return {"status": "unknown", "reason": "registration lacks an absolute installed path", **provenance}
    if Path(value).resolve() != installed_root.resolve():
        return {"status": "different-path", "reason": "registration points elsewhere", **provenance}
    return {"status": "reported-enabled" if entry.get("enabled") is True else "reported-disabled-or-unknown",
            "host": data["host"], "installed_path": str(installed_root), **provenance}


def _session_evidence(data: object, installed_root: Path, installed: dict[str, str]) -> dict:
    if not isinstance(data, dict) or not isinstance(data.get("reads"), list) or len(data["reads"]) > 128:
        raise DiagnosticError("session evidence requires a bounded reads list")
    reads = data["reads"]
    provenance = {key: data[key] for key in ("origin", "captured_at", "session_id") if isinstance(data.get(key), str) and len(data[key]) <= 256}
    package_path = installed_root / "package.json"
    package = _json_file(package_path) if package_path.is_file() else None
    version = package.get("version") if isinstance(package, dict) else None
    successful = []
    stale = []
    for record in reads:
        if not isinstance(record, dict) or record.get("success") is not True:
            continue
        path = record.get("path")
        digest = record.get("sha256")
        if not isinstance(path, str) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise DiagnosticError("successful read record needs path and SHA-256")
        if version is not None and record.get("version") != version:
            stale.append("version-mismatch")
            continue
        candidate = Path(path)
        if not candidate.is_absolute():
            raise DiagnosticError("successful read path must be absolute")
        try:
            relative = candidate.resolve().relative_to(installed_root).as_posix()
        except ValueError:
            stale.append(path)
            continue
        if (".." in candidate.parts or candidate.resolve() != (installed_root / relative).resolve() or
                relative not in installed or installed[relative] != digest):
            stale.append(relative)
        else:
            successful.append(relative)
    if stale:
        return {"status": "stale", "stale_reads": sorted(stale), **provenance}
    if not successful:
        return {"status": "unknown", "reason": "no successful installed-file read records", **provenance}
    return {"status": "supplied-current-read-records", "read_paths": sorted(set(successful)),
            "limitation": "supplied records do not independently prove active-session execution", **provenance}


def diagnose(source_root: Path, installed_root: Path, *, manager: object | None = None,
             session: object | None = None) -> dict:
    source_root, installed_root = Path(source_root).absolute(), Path(installed_root).absolute()
    if source_root.is_symlink() or installed_root.is_symlink():
        raise DiagnosticError("package roots may not be symlinks")
    source_root, installed_root = source_root.resolve(), installed_root.resolve()
    if source_root.resolve() == installed_root.resolve():
        raise DiagnosticError("source and installed roots must be distinct")
    source, installed = _inventory(source_root), _inventory(installed_root)
    for root in (source_root, installed_root):
        package = _json_file(root / "package.json")
        if not isinstance(package, dict) or package.get("name") != "qp-skills" or not isinstance(package.get("version"), str):
            raise DiagnosticError("package identity is missing or foreign")
    changed = sorted(name for name in source.keys() & installed.keys() if source[name] != installed[name])
    missing = sorted(source.keys() - installed.keys())
    added = sorted(installed.keys() - source.keys())
    result = {"source_root": str(source_root), "installed_root": str(installed_root),
              "files": {"status": "match" if not (changed or missing or added) else "different",
                        "compared": len(source), "changed": changed, "missing": missing, "added": added},
              "manager": {"status": "unknown"}, "session": {"status": "unknown"},
              "activation": "unknown"}
    if manager is not None:
        result["manager"] = _manager_evidence(manager, installed_root)
    if session is not None:
        result["session"] = _session_evidence(session, installed_root, installed)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--installed-root", type=Path, required=True)
    parser.add_argument("--manager-json", type=Path)
    parser.add_argument("--session-json", type=Path)
    args = parser.parse_args(argv)
    try:
        result = diagnose(args.source_root, args.installed_root,
                          manager=_json_file(args.manager_json) if args.manager_json else None,
                          session=_json_file(args.session_json) if args.session_json else None)
    except (DiagnosticError, OSError) as error:
        print(json.dumps({"status": "invalid", "error": str(error)}))
        return 2
    print(json.dumps(result, indent=2))
    attention = (result["files"]["status"] != "match" or
                 result["manager"]["status"] in {"different-path", "reported-disabled-or-unknown"} or
                 result["session"]["status"] == "stale")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())

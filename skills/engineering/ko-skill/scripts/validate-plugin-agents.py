#!/usr/bin/env python3
"""Validate deterministic Claude plugin-agent structure and local skill preloads."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

GROUPS = ("engineering", "design", "productivity", "experimental")
PLUGIN_IGNORED_FIELDS = ("hooks", "mcpServers", "permissionMode")
AGENT_NAME = re.compile(r"[a-z][a-z0-9-]*\Z")

@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    return parser.parse_args()

def read_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as error:
        raise ValueError("missing closing YAML frontmatter delimiter") from error
    value = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(value, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return value

def skill_metadata(repo: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    for group in GROUPS:
        group_dir = repo / "skills" / group
        if not group_dir.is_dir():
            continue
        for skill_dir in sorted(path for path in group_dir.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.is_file():
                continue
            metadata = read_frontmatter(skill_file)
            name = metadata.get("name")
            if isinstance(name, str):
                result[name] = (skill_dir, metadata)
    return result

def agent_entries(repo: Path, manifest: dict[str, Any]) -> list[str]:
    entries = manifest.get("agents")
    if entries is None:
        return ["./agents"] if (repo / "agents").is_dir() else []
    if isinstance(entries, str):
        return [entries]
    if isinstance(entries, list) and all(isinstance(item, str) for item in entries):
        return entries
    raise ValueError("plugin agents must be a string or string array")

def agent_files(repo: Path, entry: str) -> Iterable[Path]:
    if not entry.startswith("./"):
        raise ValueError(f"agent path must start with './': {entry}")
    target = (repo / entry.removeprefix("./")).resolve(strict=False)
    try:
        target.relative_to(repo.resolve())
    except ValueError as error:
        raise ValueError(f"agent path escapes repository: {entry}") from error
    if target.is_file():
        yield target
        return
    if target.is_dir():
        yield from sorted(target.rglob("*.md"))
        return
    raise ValueError(f"agent path does not resolve: {entry}")

def validate(repo: Path) -> list[Finding]:
    manifest_path = repo / ".claude-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [Finding("agent.manifest", str(manifest_path.relative_to(repo)), str(error))]
    plugin_name = manifest.get("name")
    if not isinstance(plugin_name, str) or not plugin_name:
        return [Finding("agent.manifest_name", str(manifest_path.relative_to(repo)), "plugin name must be non-empty")]
    try:
        entries = agent_entries(repo, manifest)
        skills = skill_metadata(repo)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        return [Finding("agent.inventory", str(manifest_path.relative_to(repo)), str(error))]
    findings: list[Finding] = []
    seen_names: dict[str, Path] = {}
    for entry in entries:
        try:
            files = list(agent_files(repo, entry))
        except ValueError as error:
            findings.append(Finding("agent.path", str(manifest_path.relative_to(repo)), str(error)))
            continue
        if not files:
            findings.append(Finding("agent.empty", entry, "agent path contains no Markdown files"))
            continue
        for path in files:
            relative = str(path.relative_to(repo))
            try:
                metadata = read_frontmatter(path)
            except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
                findings.append(Finding("agent.frontmatter", relative, str(error)))
                continue
            name = metadata.get("name")
            if not isinstance(name, str) or AGENT_NAME.fullmatch(name) is None:
                findings.append(Finding("agent.name", relative, "name must use lowercase letters, digits, and hyphens and start with a letter"))
            elif name in seen_names:
                findings.append(Finding("agent.duplicate", relative, f"duplicate name {name!r}; first seen at {seen_names[name]}"))
            else:
                seen_names[name] = path.relative_to(repo)
            description = metadata.get("description")
            if not isinstance(description, str) or not description.strip():
                findings.append(Finding("agent.description", relative, "description must be non-empty"))
            for field in PLUGIN_IGNORED_FIELDS:
                if field in metadata:
                    findings.append(Finding("agent.ignored_field", relative, f"plugin agents ignore frontmatter field {field!r}"))
            preloads = metadata.get("skills", [])
            if not isinstance(preloads, list) or any(not isinstance(item, str) for item in preloads):
                findings.append(Finding("agent.skills", relative, "skills must be a string array"))
                continue
            prefix = plugin_name + ":"
            for preload in preloads:
                if not preload.startswith(prefix):
                    continue
                skill_name = preload.removeprefix(prefix)
                selected = skills.get(skill_name)
                if selected is None:
                    findings.append(Finding("agent.skill_missing", relative, f"missing preloaded plugin skill {preload!r}"))
                    continue
                _, skill_meta = selected
                if skill_meta.get("disable-model-invocation") is True:
                    findings.append(Finding("agent.skill_user_only", relative, f"cannot preload model-invocation-disabled skill {preload!r}"))
    return findings

def main() -> int:
    args = parse_args()
    repo = args.repo.expanduser().resolve()
    findings = validate(repo)
    if findings:
        print(f"QP plugin agents: {len(findings)} finding(s)")
        for finding in findings:
            print(f"- [{finding.code}] {finding.path}: {finding.message}")
        return 1
    print("QP plugin agents: valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())

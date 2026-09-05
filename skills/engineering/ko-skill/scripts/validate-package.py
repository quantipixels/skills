#!/usr/bin/env python3
"""Validate deterministic QP skill-package structure and local resource integrity."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from package_metadata import UniqueKeyLoader, read_frontmatter

GROUPS = ("engineering", "design", "productivity", "experimental")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
DIRECT_REFERENCE = re.compile(r"(?<![\w])@((?:\./|\.\./)[^\s`'\"<>]+)")
SKILL_ROOT_RESOURCE = re.compile(r"<[A-Za-z0-9-]*skill-root>/((?:references|scripts|templates|assets|data)/[A-Za-z0-9._/@+-]+(?:/[A-Za-z0-9._@+-]+)*)")
REMOTE_SCHEMES = ("http://", "https://", "mailto:", "sandbox:", "data:")


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--skill", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args()


def local_targets(markdown: Path) -> Iterable[str]:
    text = markdown.read_text(encoding="utf-8")
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        target = target[1:-1] if target.startswith("<") and target.endswith(">") else target.split(maxsplit=1)[0]
        yield target
    for match in DIRECT_REFERENCE.finditer(text):
        yield match.group(1).rstrip(".,;:")
    for match in SKILL_ROOT_RESOURCE.finditer(text):
        yield "@skill/" + match.group(1).rstrip(".,;:")


def resolve_target(skill_dir: Path, markdown: Path, raw_target: str) -> Path | None:
    if not raw_target or raw_target.startswith(("#", "/", *REMOTE_SCHEMES)):
        return None
    target = raw_target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    if target.startswith("@skill/"):
        return (skill_dir / target.removeprefix("@skill/")).resolve(strict=False)
    return (markdown.parent / target).resolve(strict=False)


def contains_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(contains_key(child, key) for child in value.values())
    if isinstance(value, list):
        return any(contains_key(child, key) for child in value)
    return False


def validate_skill(repo: Path, skill_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        relative_dir = skill_dir.resolve().relative_to(repo.resolve())
    except ValueError:
        return [Finding("skill.outside_repo", str(skill_dir), "skill path is outside repository")]
    if len(relative_dir.parts) != 3 or relative_dir.parts[:1] != ("skills",) or relative_dir.parts[1] not in GROUPS:
        findings.append(Finding("skill.group", str(relative_dir), "skill must be directly under one canonical group"))
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return findings + [Finding("skill.missing", str(relative_dir / "SKILL.md"), "missing SKILL.md")]
    try:
        metadata = read_frontmatter(skill_file)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        return findings + [Finding("frontmatter.invalid", str(relative_dir / "SKILL.md"), str(error))]
    name = metadata.get("name")
    if not isinstance(name, str) or len(name) > 64 or re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is None:
        findings.append(Finding("frontmatter.identifier", str(relative_dir / "SKILL.md"), "name must be a canonical lowercase ASCII identifier of at most 64 characters"))
    if metadata.get("name") != skill_dir.name:
        findings.append(Finding("frontmatter.name", str(relative_dir / "SKILL.md"), f"frontmatter name must be {skill_dir.name!r}, got {metadata.get('name')!r}"))
    if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
        findings.append(Finding("frontmatter.description", str(relative_dir / "SKILL.md"), "description must be non-empty"))

    seen: set[tuple[Path, str]] = set()
    for markdown in sorted(skill_dir.rglob("*.md")):
        if any(part in {"node_modules", "__pycache__", ".git", ".venv"} for part in markdown.relative_to(skill_dir).parts):
            continue
        for raw in local_targets(markdown):
            key = (markdown, raw)
            if key in seen:
                continue
            seen.add(key)
            resolved = resolve_target(skill_dir, markdown, raw)
            if resolved is None:
                continue
            try:
                resolved.relative_to(skill_dir.resolve())
            except ValueError:
                findings.append(Finding("reference.escape", str(markdown.relative_to(repo)), f"reference escapes skill: {raw}"))
                continue
            if not resolved.exists():
                findings.append(Finding("reference.missing", str(markdown.relative_to(repo)), f"missing local resource: {raw}"))

    agent = skill_dir / "agents" / "openai.yaml"
    if agent.exists():
        try:
            value = yaml.load(agent.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
        except (OSError, UnicodeError, yaml.YAMLError) as error:
            findings.append(Finding("agent.invalid", str(agent.relative_to(repo)), str(error)))
        else:
            if contains_key(value, "default_prompt"):
                findings.append(Finding("agent.default_prompt", str(agent.relative_to(repo)), "default_prompt is prohibited"))
    return findings


def inventory(repo: Path) -> list[Path]:
    result: list[Path] = []
    for group in GROUPS:
        group_dir = repo / "skills" / group
        if group_dir.exists():
            result.extend(path for path in sorted(group_dir.iterdir()) if path.is_dir() and (path / "SKILL.md").exists())
    return result


def validate_inventory(repo: Path, skills: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    root = repo / "skills"
    names: dict[str, Path] = {}
    for skill in skills:
        if skill.name in names:
            findings.append(Finding("skill.duplicate", str(skill.relative_to(repo)), f"public name already used at {names[skill.name]}"))
        names[skill.name] = skill.relative_to(repo)
    if not root.is_dir():
        return findings
    expected = {path / "SKILL.md" for path in skills}
    for path in root.rglob("SKILL.md"):
        if "node_modules" in path.parts or "__pycache__" in path.parts:
            continue
        if path not in expected:
            findings.append(Finding("skill.group", str(path.relative_to(repo)), "entrypoint is not directly under one canonical group"))
    for group in GROUPS:
        directory = root / group
        if directory.is_dir():
            for path in directory.iterdir():
                if path.is_dir() and path.name != "__pycache__" and not (path / "SKILL.md").is_file():
                    findings.append(Finding("skill.missing", str(path.relative_to(repo)), "skill directory has no SKILL.md"))
    return findings


def validate_manifest(repo: Path, skills: list[Path]) -> list[Finding]:
    path = repo / ".claude-plugin" / "plugin.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [Finding("manifest.invalid", str(path.relative_to(repo)), str(error))]
    if not isinstance(manifest, dict):
        return [Finding("manifest.invalid", str(path.relative_to(repo)), "manifest must be an object")]
    entries = manifest.get("skills")
    if not isinstance(entries, list) or any(not isinstance(item, str) for item in entries):
        return [Finding("manifest.skills", str(path.relative_to(repo)), "skills must be a string array")]
    expected = {"./" + str(skill.relative_to(repo)).replace("\\", "/") for skill in skills}
    observed = set(entries)
    findings: list[Finding] = []
    for item in sorted(observed):
        if entries.count(item) > 1:
            findings.append(Finding("manifest.duplicate", str(path.relative_to(repo)), item))
    for item in sorted(expected - observed):
        findings.append(Finding("manifest.missing", str(path.relative_to(repo)), item))
    for item in sorted(observed - expected):
        findings.append(Finding("manifest.stale", str(path.relative_to(repo)), item))
    for entry in sorted(observed):
        if not ((repo / entry.removeprefix("./")) / "SKILL.md").is_file():
            findings.append(Finding("manifest.unresolved", str(path.relative_to(repo)), entry))
    return findings


def main() -> int:
    args = parse_args()
    repo = args.repo.expanduser().resolve()
    if args.skill:
        supplied = args.skill.expanduser()
        skill = (supplied if supplied.is_absolute() else repo / supplied).resolve()
        skills = [skill]
        findings = validate_skill(repo, skill)
    else:
        skills = inventory(repo)
        findings = [] if skills else [Finding("portfolio.empty", "skills", "no skills found")]
        findings.extend(validate_inventory(repo, skills))
        for skill in skills:
            findings.extend(validate_skill(repo, skill))
        findings.extend(validate_manifest(repo, skills))
    payload = {"valid": not findings, "skills_checked": len(skills), "findings": [asdict(item) for item in findings]}
    if args.format == "json":
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif findings:
        print(f"QP skill package: {len(findings)} finding(s)")
        for item in findings:
            print(f"- [{item.code}] {item.path}: {item.message}")
    else:
        print(f"QP skill package: valid ({len(skills)} skills)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

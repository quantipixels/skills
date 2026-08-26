#!/usr/bin/env python3
"""Validate deterministic QP skill-package structure."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as error:  # pragma: no cover - dependency gate
    raise SystemExit(
        "PyYAML is required. Install skills/engineering/ko-skill/scripts/requirements.txt"
    ) from error

GROUPS = ("engineering", "design", "productivity", "experimental")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
DIRECT_REFERENCE = re.compile(r"(?<![\w])@((?:\./|\.\./)[^\s`'\"<>]+)")
REMOTE_SCHEMES = ("http://", "https://", "mailto:", "sandbox:", "data:")


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--skill", type=Path, help="Validate one skill directory only")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args()


def read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
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


def local_targets(skill_file: Path) -> Iterable[str]:
    text = skill_file.read_text(encoding="utf-8")
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        else:
            target = target.split(maxsplit=1)[0]
        yield target
    for match in DIRECT_REFERENCE.finditer(text):
        yield match.group(1).rstrip(".,;:")


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
        findings.append(
            Finding("skill.group", str(relative_dir), "skill must be directly under one canonical group")
        )

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return findings + [Finding("skill.missing", str(relative_dir / "SKILL.md"), "missing SKILL.md")]

    try:
        metadata = read_frontmatter(skill_file)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        return findings + [Finding("frontmatter.invalid", str(relative_dir / "SKILL.md"), str(error))]

    name = metadata.get("name")
    description = metadata.get("description")
    if name != skill_dir.name:
        findings.append(
            Finding(
                "frontmatter.name",
                str(relative_dir / "SKILL.md"),
                f"frontmatter name must be {skill_dir.name!r}, got {name!r}",
            )
        )
    if not isinstance(description, str) or not description.strip():
        findings.append(
            Finding("frontmatter.description", str(relative_dir / "SKILL.md"), "description must be non-empty")
        )

    for raw_target in local_targets(skill_file):
        if not raw_target or raw_target.startswith(("#", "/", *REMOTE_SCHEMES)):
            continue
        target = raw_target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        resolved = (skill_file.parent / target).resolve(strict=False)
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            findings.append(
                Finding("reference.escape", str(relative_dir / "SKILL.md"), f"reference escapes skill: {raw_target}")
            )
            continue
        if not resolved.exists():
            findings.append(
                Finding("reference.missing", str(relative_dir / "SKILL.md"), f"missing local reference: {raw_target}")
            )

    agent_file = skill_dir / "agents" / "openai.yaml"
    if agent_file.exists():
        try:
            agent = yaml.safe_load(agent_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, yaml.YAMLError) as error:
            findings.append(Finding("agent.invalid", str(agent_file.relative_to(repo)), str(error)))
        else:
            if contains_key(agent, "default_prompt"):
                findings.append(
                    Finding("agent.default_prompt", str(agent_file.relative_to(repo)), "default_prompt is prohibited")
                )
    return findings


def inventory(repo: Path) -> list[Path]:
    result: list[Path] = []
    for group in GROUPS:
        group_dir = repo / "skills" / group
        if not group_dir.exists():
            continue
        result.extend(sorted(path for path in group_dir.iterdir() if path.is_dir() and (path / "SKILL.md").exists()))
    return result


def validate_manifest(repo: Path, skills: list[Path]) -> list[Finding]:
    path = repo / ".claude-plugin" / "plugin.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [Finding("manifest.invalid", str(path.relative_to(repo)), str(error))]

    entries = manifest.get("skills")
    if not isinstance(entries, list) or any(not isinstance(item, str) for item in entries):
        return [Finding("manifest.skills", str(path.relative_to(repo)), "skills must be a string array")]

    expected = {"./" + str(skill.relative_to(repo)).replace("\\", "/") for skill in skills}
    observed = set(entries)
    findings: list[Finding] = []
    for duplicate in sorted(item for item in observed if entries.count(item) > 1):
        findings.append(Finding("manifest.duplicate", str(path.relative_to(repo)), duplicate))
    for missing in sorted(expected - observed):
        findings.append(Finding("manifest.missing", str(path.relative_to(repo)), missing))
    for stale in sorted(observed - expected):
        findings.append(Finding("manifest.stale", str(path.relative_to(repo)), stale))
    for entry in sorted(observed):
        target = (repo / entry.removeprefix("./")).resolve(strict=False)
        if not (target / "SKILL.md").is_file():
            findings.append(Finding("manifest.unresolved", str(path.relative_to(repo)), entry))
    return findings


def main() -> int:
    args = parse_args()
    repo = args.repo.expanduser().resolve()
    if args.skill:
        supplied = args.skill.expanduser()
        skill = supplied if supplied.is_absolute() else repo / supplied
        skills = [skill.resolve()]
        findings = validate_skill(repo, skills[0])
    else:
        skills = inventory(repo)
        findings = []
        if not skills:
            findings.append(Finding("portfolio.empty", "skills", "no skills found"))
        for skill in skills:
            findings.extend(validate_skill(repo, skill))
        findings.extend(validate_manifest(repo, skills))

    payload = {
        "valid": not findings,
        "skills_checked": len(skills),
        "findings": [asdict(item) for item in findings],
    }
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

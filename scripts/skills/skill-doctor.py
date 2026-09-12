#!/usr/bin/env python3
"""Inventory skill context/resource and portfolio routing footprint without judging quality."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from typing import Iterable

from package_metadata import read_frontmatter, skill_directories

SCHEMA = "qp.skill-doctor/v1"
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
WORD = re.compile(r"\b[\w'-]+\b", re.UNICODE)
REMOTE_SCHEMES = ("http://", "https://", "mailto:", "sandbox:", "data:")
RESOURCE_DIRS = ("references", "scripts", "templates", "assets", "data", "agents", "workflows")
ROUTING_STOPWORDS = {
    "a", "an", "and", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it", "of", "on", "or",
    "the", "to", "use", "when", "with", "without", "one", "its", "their", "this", "that", "also", "only",
}


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, default=Path.cwd())
    p.add_argument("--skill", action="append", default=[], help="skill name or skills/<name> path; repeatable")
    p.add_argument("--format", choices=("text", "json"), default="text")
    return p.parse_args(argv)


def stats(text: str) -> dict[str, int]:
    return {
        "bytes": len(text.encode("utf-8")),
        "characters": len(text),
        "words": len(WORD.findall(text)),
        "lines": len(text.splitlines()),
    }


def body_without_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            return "\n".join(lines[i + 1 :]).lstrip("\n")
    return text


def markdown_targets(markdown: Path) -> Iterable[str]:
    text = markdown.read_text(encoding="utf-8")
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        yield target.split(maxsplit=1)[0]


def resolve_local(skill_dir: Path, markdown: Path, raw: str) -> Path | None:
    if not raw or raw.startswith(("#", "/", *REMOTE_SCHEMES)):
        return None
    target = raw.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    resolved = (markdown.parent / target).resolve(strict=False)
    try:
        resolved.relative_to(skill_dir.resolve())
    except ValueError:
        return None
    return resolved


def resource_kind(path: Path, skill_dir: Path) -> str:
    relative = path.relative_to(skill_dir)
    first = relative.parts[0] if len(relative.parts) > 1 else "root"
    return first if first in RESOURCE_DIRS else "other"


def related_skill_mentions(text: str, own: str, names: set[str]) -> list[str]:
    found = []
    for name in sorted(names - {own}):
        pattern = re.compile(rf"(?:`{re.escape(name)}`|(?<![\w-])/{re.escape(name)}(?![\w-])|(?<![\w-])\${re.escape(name)}(?![\w-]))")
        if pattern.search(text):
            found.append(name)
    return found


def routing_terms(description: str) -> set[str]:
    return {
        word.lower()
        for word in WORD.findall(description)
        if len(word) > 2 and word.lower() not in ROUTING_STOPWORDS
    }


def inspect_skill(repo: Path, skill_dir: Path, names: set[str]) -> dict:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"missing SKILL.md: {skill_dir}")
    metadata = read_frontmatter(skill_file)
    text = skill_file.read_text(encoding="utf-8")
    description = metadata.get("description")
    if not isinstance(description, str):
        description = ""

    all_files = [p for p in sorted(skill_dir.rglob("*")) if p.is_file() and "__pycache__" not in p.parts]
    markdown = [p for p in all_files if p.suffix.lower() == ".md"]
    referenced: set[Path] = set()
    entrypoint_refs: set[Path] = set()
    for source in markdown:
        for raw in markdown_targets(source):
            target = resolve_local(skill_dir, source, raw)
            if target is None:
                continue
            referenced.add(target)
            if source == skill_file:
                entrypoint_refs.add(target)

    support_markdown = [p for p in markdown if p != skill_file]
    resolved_refs = {x.resolve(strict=False) for x in referenced}
    unreferenced = [p for p in support_markdown if p.resolve(strict=False) not in resolved_refs]
    counts = Counter(resource_kind(p, skill_dir) for p in all_files if p != skill_file)
    scripts = [p.relative_to(skill_dir).as_posix() for p in all_files if p.parent.name == "scripts" and not p.name.startswith("test_")]
    tests = [p.relative_to(skill_dir).as_posix() for p in all_files if p.parent.name == "scripts" and p.name.startswith("test_")]

    return {
        "name": metadata.get("name") or skill_dir.name,
        "path": skill_dir.relative_to(repo).as_posix(),
        "maturity": (metadata.get("metadata") or {}).get("maturity") if isinstance(metadata.get("metadata"), dict) else None,
        "routing_pointer": stats(description),
        "routing_terms": sorted(routing_terms(description)),
        "entrypoint": stats(body_without_frontmatter(text)),
        "supporting_markdown": {
            "files": len(support_markdown),
            "bytes": sum(p.stat().st_size for p in support_markdown),
            "entrypoint_links": sorted(p.relative_to(skill_dir).as_posix() for p in entrypoint_refs if p.exists()),
            "unreferenced_candidates": sorted(p.relative_to(skill_dir).as_posix() for p in unreferenced),
        },
        "resources": dict(sorted(counts.items())),
        "scripts": {"non_test_files": scripts, "tests": tests},
        "related_skill_mentions": related_skill_mentions(text, skill_dir.name, names),
    }


def selected_skill_dirs(repo: Path, supplied: list[str]) -> list[Path]:
    if not supplied:
        return [p for p in skill_directories(repo) if (p / "SKILL.md").is_file()]
    out = []
    for value in supplied:
        candidate = Path(value)
        if candidate.is_absolute():
            path = candidate
        elif len(candidate.parts) > 1:
            path = repo / candidate
        else:
            path = repo / "skills" / value
        out.append(path.resolve())
    return out


def portfolio_summary(skills: list[dict]) -> dict:
    totals = {
        key: sum(skill["routing_pointer"][key] for skill in skills)
        for key in ("bytes", "characters", "words", "lines")
    }
    overlap = []
    for index, left in enumerate(skills):
        left_terms = set(left["routing_terms"])
        for right in skills[index + 1 :]:
            shared = sorted(left_terms & set(right["routing_terms"]))
            if len(shared) < 2:
                continue
            overlap.append({
                "skills": [left["name"], right["name"]],
                "shared_terms": shared,
                "shared_term_count": len(shared),
            })
    overlap.sort(key=lambda item: (-item["shared_term_count"], item["skills"]))
    return {
        "routing_pointer_total": totals,
        "description_overlap_leads": overlap[:20],
        "interpretation": "routing footprint and lexical overlap are structural leads only; they do not prove selection cost, collision, redundancy, or quality",
    }


def build(a) -> dict:
    repo = a.repo.expanduser().resolve()
    names = {p.name for p in skill_directories(repo) if (p / "SKILL.md").is_file()}
    skills = [inspect_skill(repo, p, names) for p in selected_skill_dirs(repo, a.skill)]
    return {
        "schema": SCHEMA,
        "repo": str(repo),
        "interpretation": "structural evidence only; counts and references are not quality, focus, cost, routing, redundancy, or behavior verdicts",
        "portfolio": portfolio_summary(skills),
        "skills": skills,
    }


def print_text(report: dict) -> None:
    portfolio = report["portfolio"]
    total = portfolio["routing_pointer_total"]
    print(f"portfolio routing pointers: {total['words']} words / {total['characters']} chars across {len(report['skills'])} skills")
    leads = portfolio["description_overlap_leads"]
    if leads:
        print("description overlap leads:")
        for lead in leads:
            print(f"  {lead['skills'][0]} <> {lead['skills'][1]}: {', '.join(lead['shared_terms'])}")
    else:
        print("description overlap leads: -")

    for skill in report["skills"]:
        print()
        print(skill["name"])
        print(f"  routing pointer: {skill['routing_pointer']['words']} words / {skill['routing_pointer']['characters']} chars")
        print(f"  entrypoint: {skill['entrypoint']['lines']} lines / {skill['entrypoint']['words']} words")
        support = skill["supporting_markdown"]
        print(f"  supporting markdown: {support['files']} files / {support['bytes']} bytes")
        print(f"  entrypoint links: {', '.join(support['entrypoint_links']) or '-'}")
        print(f"  unreferenced markdown candidates: {', '.join(support['unreferenced_candidates']) or '-'}")
        print(f"  related skill mentions: {', '.join(skill['related_skill_mentions']) or '-'}")
        print(f"  resources: {json.dumps(skill['resources'], sort_keys=True)}")
        print(f"  scripts/tests: {len(skill['scripts']['non_test_files'])}/{len(skill['scripts']['tests'])}")


def main(argv=None) -> int:
    try:
        a = parse_args(argv)
        report = build(a)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"skill-doctor: {error}", file=sys.stderr)
        return 2
    if a.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print_text(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

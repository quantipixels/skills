#!/usr/bin/env python3
"""Check QP package contracts. No model calls, network access or prose grading."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml
from markdown_it import MarkdownIt


class UniqueLoader(yaml.SafeLoader):
    """Reject ambiguous duplicate mapping keys instead of keeping the last value."""


def unique_mapping(loader: UniqueLoader, node: yaml.MappingNode, deep: bool = False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as error:
            raise ValueError("non-scalar mapping key") from error
        if duplicate:
            raise ValueError(f"duplicate mapping key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
MARKDOWN = MarkdownIt("commonmark")
HISTORICAL_DIRECTORIES = (
    Path("evals/coordination/observations"),
    Path("evals/engineering/observations"),
)


def mapping(text: str) -> dict:
    value = yaml.load(text, Loader=UniqueLoader)
    if not isinstance(value, dict):
        raise ValueError("expected a YAML mapping")
    return value


def frontmatter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("unclosed YAML frontmatter") from error
    return mapping("\n".join(lines[1:end]))


def destinations(text: str):
    for token in MARKDOWN.parse(text):
        for child in token.children or ():
            if child.type in ("link_open", "image"):
                yield child.attrGet("href" if child.type == "link_open" else "src")


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def complain(path: Path, message: str) -> None:
        errors.append(f"{path.relative_to(root)}: {message}")

    skills = root / "skills"
    entries = sorted(skills.glob("*/SKILL.md"))
    if not entries:
        errors.append("skills/: no skill entrypoints found")
    for directory in sorted(skills.iterdir()) if skills.is_dir() else ():
        if directory.is_dir() and not directory.name.startswith(".") and not (directory / "SKILL.md").is_file():
            complain(directory, "missing SKILL.md")
    for path in entries:
        try:
            if not path.resolve().is_relative_to(root):
                raise ValueError("entrypoint escapes package")
            data = frontmatter(path)
            name = data.get("name")
            if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                raise ValueError("invalid skill name")
            if name != path.parent.name:
                raise ValueError("name does not match directory")
            if not isinstance(data.get("description"), str) or not data["description"].strip():
                raise ValueError("description must be a nonempty string")
            disabled = data.get("disable-model-invocation", False)
            if type(disabled) is not bool:
                raise ValueError("disable-model-invocation must be boolean")
            meta_path = path.parent / "agents/openai.yaml"
            meta = {}
            if meta_path.exists() or meta_path.is_symlink():
                if not meta_path.resolve().is_relative_to(root):
                    raise ValueError("host metadata escapes package")
                if not meta_path.is_file():
                    raise ValueError("host metadata is not a readable file")
                meta = mapping(meta_path.read_text(encoding="utf-8"))
            policy = meta.get("policy", {})
            if not isinstance(policy, dict):
                raise ValueError("policy must be a mapping")
            implicit = policy.get("allow_implicit_invocation", True)
            if type(implicit) is not bool:
                raise ValueError("allow_implicit_invocation must be boolean")
            if disabled != (not implicit):
                raise ValueError("Claude and Codex invocation policies disagree")
        except (OSError, ValueError, yaml.YAMLError) as error:
            complain(path, str(error))

    documents = [root / "README.md", root / "AGENTS.md"]
    for folder in ("skills", "agents", "docs", "evals"):
        # Historical records cite their original source cuts; they are not live routes.
        documents.extend(path for path in sorted((root / folder).rglob("*.md"))
                         if not any(path.relative_to(root).is_relative_to(archive)
                                    for archive in HISTORICAL_DIRECTORIES))
    for path in documents:
        if not path.is_file():
            continue
        try:
            if not path.resolve().is_relative_to(root):
                raise ValueError("document escapes package")
            for destination in destinations(path.read_text(encoding="utf-8")):
                target = urlsplit(destination)
                if target.scheme or target.netloc or not target.path:
                    continue
                local = (path.parent / unquote(target.path)).resolve()
                if not local.is_relative_to(root):
                    complain(path, f"link escapes package: {destination}")
                elif not local.exists():
                    complain(path, f"missing link target: {destination}")
        except (OSError, ValueError) as error:
            complain(path, str(error))

    for relative in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        path = root / relative
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("name") != "qp-skills":
                raise ValueError("expected qp-skills plugin identity")
            if relative.startswith(".codex"):
                location = data.get("skills")
                if not isinstance(location, str) or (root / location).resolve() != skills:
                    raise ValueError("Codex skills path must resolve to packaged skills/")
        except (OSError, ValueError) as error:
            complain(path, str(error))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    errors = check(args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: skill identities, active local link paths, plugin paths and invocation policy consistency")
    print("Not checked: historical links, host invocation, external links/anchors, model behavior or human comprehension")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

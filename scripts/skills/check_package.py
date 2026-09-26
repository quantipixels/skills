#!/usr/bin/env python3
"""Check QP package contracts. No model calls, network access or prose grading."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
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
    Path("evals/alarina/results"),
    Path("evals/alarina/migration"),
)
ALARINA_FAMILIES = {"route", "investigate", "plan", "build", "review", "document", "ship", "utility"}
AUTHORITY_KEYS = {"edit", "publish", "merge", "deploy", "destructive"}
AUTHORITY_VALUES = {"never", "when_requested", "explicit_only", "within_existing_authority"}


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


def check_alarina_routes(root: Path, complain) -> None:
    path = root / "skills/alarina/routes.yaml"
    if not path.exists():
        return
    try:
        data = mapping(path.read_text(encoding="utf-8"))
        if data.get("version") != 2:
            raise ValueError("version must be 2")

        entry = data.get("entry")
        if not isinstance(entry, dict) or entry.get("name") != "alarina":
            raise ValueError("entry.name must be alarina")
        if entry.get("default_family") != "route":
            raise ValueError("entry.default_family must be route")

        if "bundle" in data:
            raise ValueError("obsolete bundle declaration")
        commands = data.get("commands")
        if not isinstance(commands, list) or not commands:
            raise ValueError("commands must be a nonempty list")
        command_ids = set()
        former_skills = set()
        for command in commands:
            if not isinstance(command, dict):
                raise ValueError("command must be a mapping")
            command_id = command.get("id")
            if not isinstance(command_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", command_id) or command_id in command_ids:
                raise ValueError(f"invalid or duplicate command id: {command_id}")
            command_ids.add(command_id)
            if command.get("family") not in ALARINA_FAMILIES - {"route"}:
                raise ValueError(f"invalid command family: {command_id}")
            if not isinstance(command.get("description"), str) or not command["description"].strip():
                raise ValueError(f"command needs description: {command_id}")
            reference = command.get("reference")
            if reference != f"commands/{command_id}.md" or not (path.parent / reference).is_file():
                raise ValueError(f"missing command reference: {command_id}")
            if (path.parent / reference).read_text(encoding="utf-8").startswith("---\n"):
                raise ValueError(f"command reference has skill frontmatter: {command_id}")
            if type(command.get("implicit")) is not bool:
                raise ValueError(f"invalid command invocation policy: {command_id}")
            former = command.get("former_skill")
            former_mode = command.get("former_mode")
            if (former is None) != (former_mode is None):
                raise ValueError(f"incomplete command provenance: {command_id}")
            if former is not None:
                if not isinstance(former, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", former) or not isinstance(former_mode, str) or not former_mode.strip():
                    raise ValueError(f"invalid command provenance: {command_id}")
                former_skills.add(former)
                if former in {"pese", "qp-update"} and command["implicit"]:
                    raise ValueError(f"explicit-only command allows implicit invocation: {command_id}")
        expected_former = {"adanwo", "akowe", "alaga", "amose", "architect", "arojinle", "atona", "atunwo", "ayewo-igba-ise", "fihanmi", "html-artifact", "iwadi", "oro", "pese", "qp-update", "seda-pr", "system-cleanup", "yoruba-glossary"}
        if former_skills != expected_former:
            raise ValueError("former skill coverage differs")
        actual_references = {item.stem for item in (path.parent / "commands").glob("*.md")}
        if actual_references != command_ids:
            raise ValueError("command reference inventory differs")
        if sorted((root / "skills").rglob("SKILL.md")) != [path.parent / "SKILL.md"]:
            raise ValueError("source must expose exactly one SKILL.md")
        if any(item != path.parent / "SKILL.md" for item in path.parent.rglob("SKILL.md")) or any(item != path.parent / "agents/openai.yaml" for item in path.parent.rglob("agents/openai.yaml")):
            raise ValueError("nested discovery metadata remains")

        families = data.get("families")
        if not isinstance(families, dict) or set(families) != ALARINA_FAMILIES:
            raise ValueError(f"families must be exactly: {sorted(ALARINA_FAMILIES)}")
        aliases = set()
        for family, value in families.items():
            if not isinstance(value, dict):
                raise ValueError(f"family {family} must be a mapping")
            alias = value.get("alias")
            if not isinstance(alias, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", alias):
                raise ValueError(f"family {family} has an invalid alias")
            if alias in aliases:
                raise ValueError(f"duplicate family alias: {alias}")
            aliases.add(alias)
            if not isinstance(value.get("description"), str) or not value["description"].strip():
                raise ValueError(f"family {family} needs a description")
            examples = value.get("examples")
            if not isinstance(examples, list) or not examples or any(
                not isinstance(example, str) or not example.strip() for example in examples
            ):
                raise ValueError(f"family {family} needs nonempty examples")

        routes = data.get("routes")
        if not isinstance(routes, list) or not routes:
            raise ValueError("routes must be a nonempty list")
        route_ids = set()
        referenced_commands = set()
        route_neighbours = {}
        routed_families = set()
        for route in routes:
            if not isinstance(route, dict):
                raise ValueError("every route must be a mapping")
            route_id = route.get("id")
            if not isinstance(route_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", route_id):
                raise ValueError(f"invalid route id: {route_id!r}")
            if route_id in route_ids:
                raise ValueError(f"duplicate route id: {route_id}")
            route_ids.add(route_id)
            route_families = route.get("families")
            if (
                not isinstance(route_families, list)
                or not route_families
                or len(route_families) != len(set(route_families))
                or any(family not in ALARINA_FAMILIES - {"route", "utility"} for family in route_families)
            ):
                raise ValueError(f"route {route_id} has invalid families: {route_families}")
            routed_families.update(route_families)
            for field in ("select_when",):
                if not isinstance(route.get(field), str) or not route[field].strip():
                    raise ValueError(f"route {route_id} needs {field}")
            for field in ("outcomes", "stopping_points"):
                values = route.get(field)
                if not isinstance(values, list) or not values or any(
                    not isinstance(value, str) or not value.strip() for value in values
                ):
                    raise ValueError(f"route {route_id} needs nonempty {field}")
            playbook = route.get("playbook")
            if not isinstance(playbook, str):
                raise ValueError(f"route {route_id} needs a playbook path")
            playbook_path = (path.parent / playbook).resolve()
            if not playbook_path.is_relative_to(path.parent.resolve()) or not playbook_path.is_file():
                raise ValueError(f"route {route_id} has a missing or escaping playbook: {playbook}")
            owners = route.get("owners")
            if not isinstance(owners, list) or not owners:
                raise ValueError(f"route {route_id} needs owners")
            seen_owners = set()
            for owner in owners:
                if not isinstance(owner, dict) or not isinstance(owner.get("command"), str):
                    raise ValueError(f"route {route_id} has an invalid owner")
                skill = owner["command"]
                if skill in seen_owners:
                    raise ValueError(f"route {route_id} repeats owner {skill}")
                if skill not in command_ids:
                    raise ValueError(f"route {route_id} has unknown command: {skill}")
                if type(owner.get("required")) is not bool:
                    raise ValueError(f"route {route_id} owner {skill} must declare required")
                seen_owners.add(skill)
                referenced_commands.add(skill)
            support = route.get("support")
            if not isinstance(support, list) or any(not isinstance(skill, str) for skill in support):
                raise ValueError(f"route {route_id} support must be a list")
            if len(support) != len(set(support)):
                raise ValueError(f"route {route_id} repeats a support owner")
            invalid_support = set(support) - command_ids
            if invalid_support:
                raise ValueError(f"route {route_id} has unbundled support: {sorted(invalid_support)}")
            referenced_commands.update(support)
            if type(route.get("implicit")) is not bool:
                raise ValueError(f"route {route_id} must declare implicit")
            authority = route.get("authority")
            if not isinstance(authority, dict) or set(authority) != AUTHORITY_KEYS:
                raise ValueError(f"route {route_id} must declare all authority keys")
            invalid_authority = set(authority.values()) - AUTHORITY_VALUES
            if invalid_authority:
                raise ValueError(f"route {route_id} has invalid authority values: {sorted(invalid_authority)}")
            neighbours = route.get("neighbours")
            if not isinstance(neighbours, list) or any(not isinstance(item, str) for item in neighbours):
                raise ValueError(f"route {route_id} neighbours must be a list")
            if route_id in neighbours or len(neighbours) != len(set(neighbours)):
                raise ValueError(f"route {route_id} has invalid neighbours")
            route_neighbours[route_id] = neighbours

        missing_families = (ALARINA_FAMILIES - {"route", "utility"}) - routed_families
        if missing_families:
            raise ValueError(f"families have no routes: {sorted(missing_families)}")
        explicit = {command["id"] for command in commands if command.get("former_skill") in {"pese", "qp-update"}}
        if referenced_commands & explicit:
            raise ValueError(f"route depends on explicit-only commands: {sorted(referenced_commands & explicit)}")
        for route_id, neighbours in route_neighbours.items():
            missing = set(neighbours) - route_ids
            if missing:
                raise ValueError(f"route {route_id} has missing neighbours: {sorted(missing)}")
    except (OSError, ValueError, yaml.YAMLError) as error:
        complain(path, str(error))


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

    check_alarina_routes(root, complain)

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

    real_package = root == Path(__file__).resolve().parents[2]
    for provider, marketplace_path in (
        ("codex", root / ".agents/plugins/marketplace.json"),
        ("claude", root / ".claude-plugin/marketplace.json"),
    ):
        try:
            if real_package:
                marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
                matches = [item for item in marketplace["plugins"] if item.get("name") == "qp-skills"]
                if len(matches) != 1:
                    raise ValueError("marketplace must contain exactly one qp-skills entry")
                expected = {"source": "local", "path": "./"} if provider == "codex" else "./"
                if matches[0].get("source") != expected:
                    raise ValueError("marketplace must source the repository root")
            manifest = json.loads((root / f".{provider}-plugin/plugin.json").read_text(encoding="utf-8"))
            version = json.loads((root / "package.json").read_text(encoding="utf-8"))["version"] if real_package else manifest.get("version")
            if manifest.get("name") != "qp-skills" or manifest.get("version") != version:
                raise ValueError("native plugin identity/version differs from package.json")
            if manifest.get("skills") != "./skills/":
                raise ValueError("native skills path must resolve to canonical skills/")
        except (OSError, KeyError, TypeError, ValueError) as error:
            complain(marketplace_path, str(error))
    for obsolete in (root / "plugins/codex/qp-skills", root / "plugins/claude/qp-skills"):
        if obsolete.exists():
            complain(obsolete, "obsolete copied skill tree remains")
    if real_package:
        compiler = root / "scripts/plugins/build_alarina_bundle.py"
        result = subprocess.run([sys.executable, str(compiler), "--check"], cwd=root, text=True, capture_output=True, check=False)
        if result.returncode:
            complain(compiler, result.stderr.strip() or result.stdout.strip())
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

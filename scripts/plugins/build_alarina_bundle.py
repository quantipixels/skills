#!/usr/bin/env python3
"""Build the small native declarations around the shared Alárinà skill tree."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


REPOSITORY = Path(__file__).resolve().parents[2]
COMMANDS_START = "<!-- commands:start -->"
COMMANDS_END = "<!-- commands:end -->"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\{\{[^}]*\}\}|\{%[^%]*%\}|<\s*(?:INVOCATION|PROVIDER|OWNER)[^>]*>", re.I)
FAMILIES = ("route", "investigate", "plan", "build", "review", "document", "ship", "utility")


class BuildError(ValueError):
    """The canonical package or generated declaration is invalid."""


def read_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BuildError(f"expected a mapping in {path}")
    return value


def frontmatter(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        raise BuildError(f"missing frontmatter: {path}")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise BuildError(f"invalid frontmatter: {path}")
    return metadata, content[match.end():]


def render_command_table(commands: list[dict]) -> str:
    rows: list[str] = []
    for family in FAMILIES:
        members = [command for command in commands if command["family"] == family]
        if not members:
            continue
        if rows:
            rows.append("")
        rows.extend([f"### {family.capitalize()}", "", "| Command | Purpose |", "| --- | --- |"])
        for command in members:
            purpose = command["description"] + (" (explicit invocation only)" if not command["implicit"] else "")
            rows.append(f"| [`{command['id']}`]({command['reference']}) | {purpose} |")
    return "\n".join(rows)


def validate_source(root: Path) -> tuple[dict, dict, str]:
    skill = root / "skills/alarina"
    entry = skill / "SKILL.md"
    metadata, body = frontmatter(entry)
    if metadata.get("name") != "alarina" or not metadata.get("description"):
        raise BuildError("canonical skill identity or description is invalid")
    if len(metadata["description"]) > 1024:
        raise BuildError("canonical skill description exceeds 1024 characters")
    routes = read_yaml(skill / "routes.yaml")
    commands = routes.get("commands")
    if not isinstance(commands, list) or not commands:
        raise BuildError("routes.yaml has no commands")
    if body.count(COMMANDS_START) != 1 or body.count(COMMANDS_END) != 1:
        raise BuildError("source SKILL.md needs one commands table marker pair")
    actual = body.split(COMMANDS_START, 1)[1].split(COMMANDS_END, 1)[0].strip()
    if actual != render_command_table(commands):
        raise BuildError("source commands table differs from routes.yaml")
    if sorted((root / "skills").rglob("SKILL.md")) != [entry]:
        raise BuildError("source must expose exactly one SKILL.md")
    if any(item != skill / "agents/openai.yaml" for item in skill.rglob("agents/openai.yaml")):
        raise BuildError("nested discovery metadata remains")
    for command in commands:
        command_id = command.get("id")
        reference = command.get("reference")
        if reference != f"commands/{command_id}.md" or not (skill / reference).is_file():
            raise BuildError(f"missing command reference: {command_id}")
        if command_id in {"pese", "qp-update"} and command.get("implicit") is not False:
            raise BuildError(f"explicit-only command allows implicit invocation: {command_id}")
    for route in routes.get("routes", []):
        used = [item.get("command") for item in route.get("owners", [])] + route.get("support", [])
        if {"pese", "qp-update"} & set(used):
            raise BuildError("route depends on explicit-only commands")
        playbook = route.get("playbook")
        if not isinstance(playbook, str) or not playbook.startswith("playbooks/") or ".." in Path(playbook).parts or not (skill / playbook).is_file():
            raise BuildError(f"missing or escaping playbook: {playbook}")
    for document in skill.rglob("*.md"):
        for destination in LINK.findall(document.read_text(encoding="utf-8")):
            parsed = urlsplit(destination.strip().strip("<>").split()[0])
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(skill.resolve()):
                raise BuildError(f"link escapes skill: {document.relative_to(skill)} -> {destination}")
            if not target.exists():
                raise BuildError(f"missing local link: {document.relative_to(skill)} -> {destination}")
    for path in skill.rglob("*"):
        if path.is_symlink():
            raise BuildError(f"symlink in skill: {path.relative_to(skill)}")
        if path.is_file() and path.suffix in {".md", ".yaml", ".json", ".toml"}:
            if PLACEHOLDER.search(path.read_text(encoding="utf-8")):
                raise BuildError(f"unresolved placeholder: {path.relative_to(skill)}")
    return metadata, routes, body


def render(root: Path) -> dict[str, str]:
    metadata, _routes, _body = validate_source(root)
    try:
        package = json.loads((root / "package.json").read_text(encoding="utf-8"))
        opencode = json.loads((root / "opencode.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise BuildError(f"cannot read native package configuration: {error}") from error
    if not isinstance(opencode, dict) or opencode.get("skills") != {"paths": ["./skills"]}:
        raise BuildError("OpenCode skills.paths must load ./skills")
    if not isinstance(package, dict) or package.get("pi") != {"skills": ["./skills"]}:
        raise BuildError("Pi pi.skills must load ./skills")
    registry = read_yaml(root / "scripts/plugins/providers.yaml")
    if registry.get("version") != 2 or set(registry.get("providers", {})) != {"codex", "claude", "opencode", "pi"}:
        raise BuildError("provider registry must contain exactly four supported hosts")
    expected_registry = {
        "codex": (".codex-plugin/plugin.json", "agents/alarina.codex.toml", "project_or_user"),
        "claude": (".claude-plugin/plugin.json", "agents/alarina.claude.md", "plugin"),
        "opencode": ("opencode.json", ".opencode/agents/alarina.md", "project"),
        "pi": ("package.json", None, "system_prompt_option"),
    }
    for host, (skill_path, agent_path, registration) in expected_registry.items():
        item = registry["providers"][host]
        if (item.get("skill"), item.get("agent"), item.get("agent_registration")) != (skill_path, agent_path, registration):
            raise BuildError(f"provider registry differs from native {host} declaration")
    version = package["version"]
    agent_meta, agent_body = frontmatter(root / "agents/alarina.md")
    if agent_meta.get("name") != "alarina" or agent_body.count("`alarina`") != 1:
        raise BuildError("canonical agent must name its single skill dependency")
    description = "QP software-project work through Alárinà"
    common = {"name": "qp-skills", "version": version, "description": description, "author": {"name": "Oluwaseyi Sobande"}, "license": "MIT"}
    codex = {**common, "skills": "./skills/"}
    claude = {**common, "skills": "./skills/", "agents": ["./agents/alarina.claude.md"]}
    codex_body = agent_body.replace("`alarina`", "`$qp-skills:alarina`", 1).replace("from this package", "from the installed qp-skills plugin")
    codex_agent = {**agent_meta, "developer_instructions": codex_body.strip()}
    codex_text = "\n".join(f"{key} = {json.dumps(value, ensure_ascii=False)}" for key, value in codex_agent.items()) + "\n"
    claude_body = agent_body.replace("`alarina`", "`/qp-skills:alarina`", 1).replace("its `SKILL.md` from this package", "`${CLAUDE_PLUGIN_ROOT}/skills/alarina/SKILL.md`")
    claude_agent = {**agent_meta, "skills": ["qp-skills:alarina"]}
    claude_text = "---\n" + yaml.safe_dump(claude_agent, allow_unicode=True, sort_keys=False) + "---\n\n" + claude_body
    return {
        ".codex-plugin/plugin.json": json.dumps(codex, ensure_ascii=False, indent=2) + "\n",
        ".claude-plugin/plugin.json": json.dumps(claude, ensure_ascii=False, indent=2) + "\n",
        "agents/alarina.codex.toml": codex_text,
        "agents/alarina.claude.md": claude_text,
        ".opencode/agents/alarina.md": (root / "agents/alarina.md").read_text(encoding="utf-8"),
    }


def run(root: Path, check: bool) -> None:
    expected = render(root)
    for relative, content in expected.items():
        path = root / relative
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                raise BuildError(f"generated declaration is missing or stale: {relative}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    for stale in (root / "plugins/codex/qp-skills", root / "plugins/claude/qp-skills"):
        if stale.exists():
            raise BuildError(f"obsolete copied skill tree remains: {stale.relative_to(root)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        run(args.root.resolve(), args.check)
    except (BuildError, OSError, KeyError, TypeError, yaml.YAMLError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print("PASS: canonical Alárinà source and native declarations" if args.check else "Built native declarations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Render provider-native agent profiles from one role catalogue."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
DEFAULT_ROLES = HERE.parent / "assets" / "agent-experience" / "roles.json"
VALID_SANDBOXES = {"read-only", "workspace-write"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", choices=("codex", "claude"), required=True)
    parser.add_argument("--settings", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--roles", type=Path, default=DEFAULT_ROLES)
    return parser.parse_args(argv)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_roles(path: Path) -> list[dict[str, Any]]:
    payload = load_json(path)
    if payload.get("schema") != 1 or not isinstance(payload.get("roles"), list):
        raise ValueError("unsupported role catalogue")
    seen: set[str] = set()
    roles: list[dict[str, Any]] = []
    for role in payload["roles"]:
        name = role.get("name")
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError(f"invalid or duplicate role name: {name!r}")
        if role.get("sandbox") not in VALID_SANDBOXES:
            raise ValueError(f"invalid sandbox for {name}")
        for key in ("description", "instructions"):
            if not isinstance(role.get(key), str) or not role[key].strip():
                raise ValueError(f"missing {key} for {name}")
        seen.add(name)
        roles.append(role)
    return roles


def load_settings(path: Path, roles: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    payload = load_json(path)
    settings = payload.get("roles", payload)
    if not isinstance(settings, dict):
        raise ValueError("settings must contain a role mapping")
    names = {role["name"] for role in roles}
    unknown = sorted(set(settings) - names)
    if unknown:
        raise ValueError(f"unknown roles in settings: {', '.join(unknown)}")
    normalized: dict[str, dict[str, str]] = {}
    for name, raw in settings.items():
        if not isinstance(raw, dict):
            raise ValueError(f"settings for {name} must be an object")
        values: dict[str, str] = {}
        for key in ("model", "effort"):
            value = raw.get(key)
            if value is None:
                continue
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{key} for {name} must be a non-empty string")
            values[key] = value.strip()
        normalized[name] = values
    return normalized


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_codex(role: dict[str, Any], settings: dict[str, str]) -> str:
    lines = [
        f'name = {toml_string(role["name"])}',
        f'description = {toml_string(role["description"])}',
    ]
    if model := settings.get("model"):
        lines.append(f'model = {toml_string(model)}')
    if effort := settings.get("effort"):
        lines.append(f'model_reasoning_effort = {toml_string(effort)}')
    lines.extend(
        [
            f'sandbox_mode = {toml_string(role["sandbox"])}',
            "",
            f'developer_instructions = {toml_string(role["instructions"])}',
            "",
        ]
    )
    return "\n".join(lines)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_claude(role: dict[str, Any], settings: dict[str, str]) -> str:
    lines = [
        "---",
        f'name: {yaml_string(role["name"])}',
        f'description: {yaml_string(role["description"])}',
    ]
    if model := settings.get("model"):
        lines.append(f'model: {yaml_string(model)}')
    if effort := settings.get("effort"):
        lines.append(f'effort: {yaml_string(effort)}')
    if role["sandbox"] == "read-only":
        lines.extend(
            [
                "disallowedTools:",
                "  - Write",
                "  - Edit",
                "  - NotebookEdit",
            ]
        )
    lines.extend(["---", "", role["instructions"].rstrip(), ""])
    return "\n".join(lines)


def render(
    host: str,
    roles: list[dict[str, Any]],
    settings: dict[str, dict[str, str]],
    output: Path,
) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for role in roles:
        role_settings = settings.get(role["name"], {})
        if host == "codex":
            path = output / f'{role["name"]}.toml'
            content = render_codex(role, role_settings)
        else:
            path = output / f'{role["name"]}.md'
            content = render_claude(role, role_settings)
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    roles = load_roles(args.roles)
    settings = load_settings(args.settings, roles)
    for path in render(args.host, roles, settings, args.output):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Render selected provider-native agent definitions from one work-posture catalogue."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
DEFAULT_POSTURES = HERE.parent / "assets" / "agent-experience" / "postures.json"
VALID_BOUNDARIES = {"read-only", "write-capable"}
OWNER_MARKER = "qp-skills-agent-definition: v1"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", choices=("codex", "claude"), required=True)
    parser.add_argument("--settings", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--postures", type=Path, default=DEFAULT_POSTURES)
    return parser.parse_args(argv)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_postures(path: Path) -> list[dict[str, Any]]:
    payload = load_json(path)
    if payload.get("schema") != 1 or not isinstance(payload.get("postures"), list):
        raise ValueError("unsupported work-posture catalogue")
    seen: set[str] = set()
    postures: list[dict[str, Any]] = []
    for posture in payload["postures"]:
        identifier = posture.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise ValueError(f"invalid or duplicate posture id: {identifier!r}")
        if posture.get("execution_boundary") not in VALID_BOUNDARIES:
            raise ValueError(f"invalid execution boundary for {identifier}")
        for key in ("display_name", "posture", "description", "instructions"):
            if not isinstance(posture.get(key), str) or not posture[key].strip():
                raise ValueError(f"missing {key} for {identifier}")
        seen.add(identifier)
        postures.append(posture)
    return postures


def load_settings(path: Path, postures: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    payload = load_json(path)
    definitions = payload.get("definitions", payload)
    if not isinstance(definitions, dict):
        raise ValueError("settings must contain a definition mapping")
    known = {item["id"] for item in postures}
    unknown = sorted(set(definitions) - known)
    if unknown:
        raise ValueError(f"unknown definitions in settings: {', '.join(unknown)}")
    normalized: dict[str, dict[str, str]] = {}
    for identifier, raw in definitions.items():
        if not isinstance(raw, dict):
            raise ValueError(f"settings for {identifier} must be an object")
        values: dict[str, str] = {}
        for key in ("model", "effort"):
            value = raw.get(key)
            if value is None:
                continue
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{key} for {identifier} must be a non-empty string")
            values[key] = value.strip()
        normalized[identifier] = values
    return normalized


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_codex(posture: dict[str, Any], settings: dict[str, str]) -> str:
    lines = [
        f"# {OWNER_MARKER}",
        f'name = {toml_string(posture["id"])}',
        f'description = {toml_string(posture["display_name"] + " — " + posture["description"])}',
    ]
    if model := settings.get("model"):
        lines.append(f'model = {toml_string(model)}')
    if effort := settings.get("effort"):
        lines.append(f'model_reasoning_effort = {toml_string(effort)}')
    sandbox = "read-only" if posture["execution_boundary"] == "read-only" else "workspace-write"
    lines.extend(
        [
            f'sandbox_mode = {toml_string(sandbox)}',
            "",
            f'developer_instructions = {toml_string(posture["instructions"])}',
            "",
        ]
    )
    return "\n".join(lines)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_claude(posture: dict[str, Any], settings: dict[str, str]) -> str:
    lines = [
        "---",
        f"# {OWNER_MARKER}",
        f'name: {yaml_string(posture["id"])}',
        f'description: {yaml_string(posture["display_name"] + " — " + posture["description"])}',
    ]
    if model := settings.get("model"):
        lines.append(f'model: {yaml_string(model)}')
    if effort := settings.get("effort"):
        lines.append(f'effort: {yaml_string(effort)}')
    if posture["execution_boundary"] == "read-only":
        lines.extend(["disallowedTools:", "  - Write", "  - Edit", "  - NotebookEdit"])
    lines.extend(["---", "", posture["instructions"].rstrip(), ""])
    return "\n".join(lines)


def render(
    host: str,
    postures: list[dict[str, Any]],
    definitions: dict[str, dict[str, str]],
    output: Path,
) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    selected = set(definitions)
    for posture in postures:
        identifier = posture["id"]
        if identifier not in selected:
            continue
        if host == "codex":
            path = output / f"{identifier}.toml"
            content = render_codex(posture, definitions[identifier])
        else:
            path = output / f"{identifier}.md"
            content = render_claude(posture, definitions[identifier])
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    postures = load_postures(args.postures)
    definitions = load_settings(args.settings, postures)
    for path in render(args.host, postures, definitions, args.output):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

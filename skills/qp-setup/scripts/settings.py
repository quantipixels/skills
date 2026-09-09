"""Resolve QP preferences as data; never choose models or change host permissions."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import tomllib

ASSETS = Path(__file__).resolve().parents[1] / "assets"
HOSTS = ("claude", "codex")
MODES = ("adaptive", "inherit")
EFFORTS = {
    "claude": ("low", "medium", "high", "xhigh", "max"),
    "codex": ("low", "medium", "high", "xhigh", "max", "ultra"),
}
MODEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/@+-]{0,199}\Z")
COMMUNICATION = {
    "default": "",
    "adaptive": "Match the user's current language, register, and level of detail. Preserve exact code, identifiers, commands, paths, quotations, and machine-readable output. Explicit task language and output requirements take precedence.",
    "yoruba": "Use Yoruba for user-facing prose, with appropriate diacritics. Preserve exact code, identifiers, commands, paths, quotations, and machine-readable output. Explicit task language and output requirements take precedence.",
}


class ConfigError(ValueError):
    """A configuration or installation cannot be applied safely."""


def roles() -> dict:
    return tomllib.loads((ASSETS / "agents.toml").read_text(encoding="utf-8"))


def workers() -> tuple[str, ...]:
    return tuple(name for name in roles() if name != "pepeye")


def unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ConfigError(f"duplicate key {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeError, ValueError) as error:
        raise ConfigError(f"{path}: {error}") from error
    if not isinstance(value, dict):
        raise ConfigError(f"{path}: expected a JSON object")
    return value


def keys(value: object, allowed: set, location: str) -> None:
    if not isinstance(value, dict):
        raise ConfigError(f"{location}: expected an object")
    unknown = set(value) - allowed
    if unknown:
        raise ConfigError(f"{location}: unknown keys: {', '.join(sorted(unknown))}")


def policy(value: dict, host: str, location: str) -> None:
    for key in ("model", "reasoning"):
        if key not in value:
            continue
        item = value[key]
        if not isinstance(item, str):
            raise ConfigError(f"{location}.{key}: expected a string")
        if key == "model" and not MODEL.fullmatch(item):
            raise ConfigError(f"{location}.model: expected a model identifier, adaptive, or inherit")
        if key == "reasoning" and item not in (*MODES, *EFFORTS[host]):
            raise ConfigError(f"{location}.reasoning: unsupported {host} effort {item!r}")


def validate(value: dict, location: str) -> None:
    keys(value, {"$schema", "version", "communication", *HOSTS}, location)
    if "version" in value and (type(value["version"]) is not int or value["version"] != 1):
        raise ConfigError(f"{location}.version: expected 1")
    if "$schema" in value and not isinstance(value["$schema"], str):
        raise ConfigError(f"{location}.$schema: expected a string")
    if "communication" in value and (not isinstance(value["communication"], str)
                                      or value["communication"] not in COMMUNICATION):
        raise ConfigError(f"{location}.communication: expected default, adaptive, or yoruba")
    for host in HOSTS:
        if host not in value:
            continue
        section = value[host]
        keys(section, {"model", "reasoning", "agents"}, f"{location}.{host}")
        policy(section, host, f"{location}.{host}")
        if "agents" in section:
            keys(section["agents"], set(workers()), f"{location}.{host}.agents")
            for name, config in section["agents"].items():
                at = f"{location}.{host}.agents.{name}"
                keys(config, {"model", "reasoning"}, at)
                policy(config, host, at)


def repo_root(cwd: Path) -> Path | None:
    """Use Git's checkout root, including linked worktrees; never walk .qp parents."""
    try:
        result = subprocess.run(["git", "-C", str(cwd), "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, timeout=10, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return Path(result.stdout.strip()).resolve() if result.returncode == 0 else None


def resolve(home: Path | None = None, repo: Path | None = None) -> dict:
    home = (home or Path.home()).expanduser().resolve()
    paths = [home / ".qp/setting.json"]
    if repo is not None:
        local = repo.expanduser().resolve() / ".qp/setting.json"
        if local != paths[0]:
            paths.append(local)
    result = {
        "communication": "default", "communication_instruction": "",
        "sources": [], "origins": {"communication": "builtin"},
        "hosts": {host: {name: {"model": "adaptive", "reasoning": "adaptive"}
                          for name in workers()} for host in HOSTS},
    }
    for path in paths:
        if not os.path.lexists(path):
            continue
        value = load_json(path)
        validate(value, str(path))
        result["sources"].append(str(path))
        if "communication" in value:
            result["communication"] = value["communication"]
            result["origins"]["communication"] = str(path)
        for host in HOSTS:
            section = value.get(host, {})
            # Scope wins over specificity: a repo default can reset a global role pin.
            for name, effective in result["hosts"][host].items():
                for layer in (section, section.get("agents", {}).get(name, {})):
                    for key in ("model", "reasoning"):
                        if key in layer:
                            effective[key] = layer[key]
                            result["origins"][f"{host}.{name}.{key}"] = str(path)
    result["communication_instruction"] = COMMUNICATION[result["communication"]]
    return result


def schema() -> dict:
    """Editor schema from the same finite choices used by the resolver."""
    result = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "QP preferences (.qp/setting.json)", "type": "object",
        "additionalProperties": False, "$defs": {},
        "properties": {
            "$schema": {"type": "string"}, "version": {"type": "integer", "const": 1},
            "communication": {"enum": list(COMMUNICATION), "default": "default"},
        },
    }
    for host in HOSTS:
        fields = {
            "model": {"type": "string", "pattern": r"^[A-Za-z0-9][A-Za-z0-9._:/@+-]{0,199}(?![\s\S])", "default": "adaptive"},
            "reasoning": {"enum": [*MODES, *EFFORTS[host]], "default": "adaptive"},
        }
        result["$defs"][host + "Policy"] = {"type": "object", "additionalProperties": False, "properties": fields}
        role = {"$ref": "#/$defs/" + host + "Policy"}
        result["properties"][host] = {
            "type": "object", "additionalProperties": False,
            "properties": {**fields, "agents": {"type": "object", "additionalProperties": False,
                                                "properties": {name: role for name in workers()}}},
        }
    return result

#!/usr/bin/env python3
"""Compile one canonical Alárinà skill into a single-entry native plugin."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

import yaml


HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[1]
PROVIDERS = HERE / "providers.yaml"
COMPILER_VERSION = 1
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\{\{[^}]*\}\}|\{%[^%]*%\}|<\s*(?:INVOCATION|PROVIDER|OWNER)[^>]*>", re.I)
FAMILIES = ("route", "investigate", "plan", "build", "review", "document", "ship", "utility")
FORMER_SKILLS = {"adanwo", "akowe", "alaga", "amose", "architect", "arojinle", "atona", "atunwo", "ayewo-igba-ise", "fihanmi", "html-artifact", "iwadi", "oro", "pese", "qp-update", "seda-pr", "system-cleanup", "yoruba-glossary"}
EXPLICIT_ONLY = {"pese", "qp-update"}
COMMANDS_START = "<!-- commands:start -->"
COMMANDS_END = "<!-- commands:end -->"


class BuildError(ValueError):
    """The candidate cannot preserve the declared bundle contract."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_yaml(path: Path) -> dict:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise BuildError(f"cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BuildError(f"expected a mapping in {path}")
    return value


def safe_relative(value: str, label: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise BuildError(f"invalid {label}: {value!r}")
    path = Path(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in value.split("/")):
        raise BuildError(f"escaping {label}: {value}")
    return path


def frontmatter(source: Path) -> tuple[dict, str]:
    content = source.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        raise BuildError(f"missing frontmatter: {source}")
    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise BuildError(f"invalid frontmatter: {source}: {exc}") from exc
    if not isinstance(metadata, dict) or not isinstance(metadata.get("description"), str):
        raise BuildError(f"missing description: {source}")
    return metadata, content[match.end():]


def render_command_table(commands: list[dict]) -> str:
    rows = ["| Command | Family | Purpose |", "| --- | --- | --- |"]
    for command in commands:
        purpose = command["description"] + (" (explicit invocation only)" if not command["implicit"] else "")
        rows.append(f"| [`{command['id']}`]({command['reference']}) | {command['family']} | {purpose} |")
    return "\n".join(rows)


def validate_command_table(body: str, commands: list[dict]) -> None:
    if body.count(COMMANDS_START) != 1 or body.count(COMMANDS_END) != 1:
        raise BuildError("source SKILL.md needs one commands table marker pair")
    actual = body.split(COMMANDS_START, 1)[1].split(COMMANDS_END, 1)[0].strip()
    if actual != render_command_table(commands):
        raise BuildError("source commands table differs from routes.yaml")


def validate_routes(data: dict, repository: Path, entry_name: str) -> tuple[list[dict], dict]:
    if data.get("version") != 2:
        raise BuildError("unsupported routes version")
    entry = data.get("entry")
    if not isinstance(entry, dict) or entry.get("name") != entry_name or entry.get("default_family") != "route":
        raise BuildError("route entry does not match canonical Alárinà")
    if "bundle" in data:
        raise BuildError("obsolete bundle declaration")
    families = data.get("families")
    if not isinstance(families, dict) or set(families) != set(FAMILIES):
        raise BuildError("invalid public families")
    aliases = []
    for name in FAMILIES:
        item = families[name]
        if not isinstance(item, dict) or not isinstance(item.get("description"), str) or not item["description"].strip():
            raise BuildError(f"invalid family {name}")
        alias = item.get("alias")
        if not isinstance(alias, str) or not NAME.fullmatch(alias):
            raise BuildError(f"invalid alias for {name}")
        examples = item.get("examples")
        if not isinstance(examples, list) or not examples or any(not isinstance(x, str) or not x.strip() for x in examples):
            raise BuildError(f"invalid examples for {name}")
        aliases.append(alias)
    if len(set(aliases)) != len(aliases):
        raise BuildError("duplicate public alias")
    commands = data.get("commands")
    if not isinstance(commands, list) or not commands:
        raise BuildError("missing commands")
    command_ids: set[str] = set()
    former_skills: set[str] = set()
    for command in commands:
        if not isinstance(command, dict):
            raise BuildError("command must be a mapping")
        command_id = command.get("id")
        if not isinstance(command_id, str) or not NAME.fullmatch(command_id) or command_id in command_ids:
            raise BuildError(f"invalid or duplicate command ID: {command_id!r}")
        command_ids.add(command_id)
        if command.get("family") not in set(FAMILIES) - {"route"}:
            raise BuildError(f"invalid command family: {command_id}")
        if not isinstance(command.get("description"), str) or not command["description"].strip():
            raise BuildError(f"missing command description: {command_id}")
        reference = safe_relative(command.get("reference"), f"reference for {command_id}")
        if reference != Path("commands") / f"{command_id}.md" or not (repository / "skills" / entry_name / reference).is_file():
            raise BuildError(f"missing command reference: {command_id}")
        if (repository / "skills" / entry_name / reference).read_text(encoding="utf-8").startswith("---\n"):
            raise BuildError(f"command reference has skill frontmatter: {command_id}")
        if type(command.get("implicit")) is not bool:
            raise BuildError(f"invalid command invocation policy: {command_id}")
        former = command.get("former_skill")
        former_mode = command.get("former_mode")
        if (former is None) != (former_mode is None):
            raise BuildError(f"incomplete command provenance: {command_id}")
        if former is not None:
            if not isinstance(former, str) or not NAME.fullmatch(former) or not isinstance(former_mode, str) or not former_mode.strip():
                raise BuildError(f"invalid command provenance: {command_id}")
            if former in EXPLICIT_ONLY and command["implicit"]:
                raise BuildError(f"explicit-only command allows implicit invocation: {command_id}")
            former_skills.add(former)
    if former_skills != FORMER_SKILLS:
        raise BuildError(f"former skill coverage differs: missing={sorted(FORMER_SKILLS - former_skills)}, extra={sorted(former_skills - FORMER_SKILLS)}")
    reference_dir = repository / "skills" / entry_name / "commands"
    actual_references = {path.stem for path in reference_dir.glob("*.md")}
    if actual_references != command_ids:
        raise BuildError(f"command reference inventory differs: missing={sorted(command_ids - actual_references)}, extra={sorted(actual_references - command_ids)}")
    routes = data.get("routes")
    if not isinstance(routes, list) or not routes:
        raise BuildError("missing routes")
    ids: set[str] = set()
    dependencies: set[str] = set()
    for route in routes:
        if not isinstance(route, dict):
            raise BuildError("route must be a mapping")
        route_id = route.get("id")
        if not isinstance(route_id, str) or not NAME.fullmatch(route_id) or route_id in ids:
            raise BuildError(f"invalid or duplicate route ID: {route_id!r}")
        ids.add(route_id)
        route_families = route.get("families")
        if (
            not isinstance(route_families, list)
            or not route_families
            or len(route_families) != len(set(route_families))
            or any(family not in set(families) - {"route"} for family in route_families)
            or not isinstance(route.get("implicit"), bool)
        ):
            raise BuildError(f"invalid families or implicit policy: {route_id}")
        for key in ("select_when",):
            if not isinstance(route.get(key), str) or not route[key].strip():
                raise BuildError(f"missing {key}: {route_id}")
        for key in ("outcomes", "stopping_points"):
            if not isinstance(route.get(key), list) or not route[key] or any(not isinstance(v, str) or not v for v in route[key]):
                raise BuildError(f"invalid {key}: {route_id}")
        playbook = safe_relative(route.get("playbook"), f"playbook for {route_id}")
        if not str(playbook).startswith("playbooks/") or not (repository / "skills" / entry_name / playbook).is_file():
            raise BuildError(f"missing playbook: {route_id}")
        owners = route.get("owners")
        support = route.get("support")
        if not isinstance(owners, list) or not owners or not isinstance(support, list):
            raise BuildError(f"invalid owners/support: {route_id}")
        for owner in owners:
            if not isinstance(owner, dict) or type(owner.get("required")) is not bool:
                raise BuildError(f"invalid owner: {route_id}")
            command_id = owner.get("command")
            if not isinstance(command_id, str):
                raise BuildError(f"invalid owner command: {route_id}")
            dependencies.add(command_id)
        if any(not isinstance(command_id, str) for command_id in support):
            raise BuildError(f"invalid support command: {route_id}")
        dependencies.update(support)
        if not isinstance(route.get("authority"), dict) or not route["authority"]:
            raise BuildError(f"missing authority: {route_id}")
        if not isinstance(route.get("neighbours"), list):
            raise BuildError(f"missing neighbours: {route_id}")
    for route in routes:
        if any(neighbour not in ids for neighbour in route["neighbours"]):
            raise BuildError(f"unknown neighbour: {route['id']}")
    if dependencies - command_ids:
        raise BuildError(f"route depends on unknown commands: {sorted(dependencies - command_ids)}")
    explicit_ids = {command["id"] for command in commands if command["former_skill"] in EXPLICIT_ONLY}
    if dependencies & explicit_ids:
        raise BuildError(f"route depends on explicit-only commands: {sorted(dependencies & explicit_ids)}")
    if sorted((repository / "skills").rglob("SKILL.md")) != [repository / "skills" / entry_name / "SKILL.md"]:
        raise BuildError("source must expose exactly one SKILL.md")
    source_root = repository / "skills" / entry_name
    if any(path != source_root / "SKILL.md" for path in source_root.rglob("SKILL.md")) or any(path != source_root / "agents/openai.yaml" for path in source_root.rglob("agents/openai.yaml")):
        raise BuildError("nested discovery metadata remains")
    return commands, families


def validate_provider(registry: dict, provider_id: str) -> dict:
    if registry.get("version") != 1 or not isinstance(registry.get("providers"), dict):
        raise BuildError("invalid provider registry")
    candidates = registry.get("candidate_providers")
    if not isinstance(candidates, list):
        raise BuildError("invalid candidate provider registry")
    candidate_ids = set()
    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise BuildError("candidate provider must be a mapping")
        candidate_id = candidate.get("id")
        if not isinstance(candidate_id, str) or not NAME.fullmatch(candidate_id) or candidate_id in candidate_ids:
            raise BuildError(f"invalid or duplicate candidate provider: {candidate_id!r}")
        if candidate.get("support_state") != "experimental" or candidate.get("release_inclusion") is not False:
            raise BuildError(f"candidate provider cannot be released: {candidate_id}")
        safe_relative(candidate.get("skill_path"), f"candidate skill path for {candidate_id}")
        invocation = candidate.get("invocation")
        if not isinstance(invocation, str) or not invocation.startswith(("$", "/")):
            raise BuildError(f"invalid candidate invocation: {candidate_id}")
        candidate_ids.add(candidate_id)
    provider = registry["providers"].get(provider_id)
    if provider_id not in ("codex", "claude") or not isinstance(provider, dict):
        raise BuildError(f"unsupported provider: {provider_id}")
    fields = provider.get("frontmatter")
    allowed = {"name", "description"} if provider_id == "codex" else {"name", "description", "when_to_use", "argument-hint", "user-invocable", "disable-model-invocation"}
    if not isinstance(fields, list) or set(fields) != allowed or len(fields) != len(allowed):
        raise BuildError("invalid provider frontmatter fields")
    invocation = provider.get("qualified_invocation")
    expected = "$qp-skills:alarina" if provider_id == "codex" else "/qp-skills:alarina"
    if invocation != expected:
        raise BuildError("invalid qualified invocation")
    if provider.get("support_state") not in ("verified", "experimental", "unsupported") or provider.get("support_state") == "unsupported":
        raise BuildError("provider not buildable")
    for key in ("skill_path", "plugin_manifest"):
        safe_relative(provider.get(key), key)
    if provider["skill_path"] != "skills/alarina" or provider["plugin_manifest"] != (".codex-plugin/plugin.json" if provider_id == "codex" else ".claude-plugin/plugin.json"):
        raise BuildError("invalid provider layout")
    native_agent = provider.get("native_agent_path")
    if provider_id == "codex" and native_agent is not None:
        raise BuildError("Codex native plugin agents are not established")
    if provider_id == "claude" and safe_relative(native_agent, "native_agent_path") != Path("agents/alarina.md"):
        raise BuildError("invalid Claude agent path")
    if not isinstance(provider.get("description_limit"), int) or provider["description_limit"] < 100:
        raise BuildError("invalid provider description limit")
    if provider_id == "claude" and (not isinstance(provider.get("when_to_use"), str) or not provider["when_to_use"].strip()):
        raise BuildError("missing Claude when_to_use guidance")
    return provider


def copy_file(source: Path, target: Path, provenance: dict, repository: Path) -> None:
    if source.is_symlink() or not source.is_file() or not source.resolve().is_relative_to(repository):
        raise BuildError(f"unsafe source file: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    provenance[target] = {"source": source.relative_to(repository).as_posix(), "source_sha256": digest(source.read_bytes())}


def copy_package(source: Path, target: Path, provenance: dict, repository: Path) -> None:
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise BuildError(f"symlink in package: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        if "__pycache__" in relative.parts or ".pytest_cache" in relative.parts or relative.suffix == ".pyc" or relative.name == ".DS_Store":
            continue
        copy_file(path, target / relative, provenance, repository)


def check_links(root: Path) -> None:
    for document in sorted(root.rglob("*.md")):
        for destination in LINK.findall(document.read_text(encoding="utf-8")):
            parsed = urlsplit(destination.strip().strip("<>").split()[0])
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root.resolve()):
                raise BuildError(f"link escapes bundle: {document.relative_to(root)} -> {destination}")
            if not target.exists():
                raise BuildError(f"missing local link: {document.relative_to(root)} -> {destination}")


def check_tokens(root: Path) -> None:
    for path in root.rglob("*"):
        if path.suffix in (".md", ".yaml", ".json", ".toml") and path.is_file():
            if PLACEHOLDER.search(path.read_text(encoding="utf-8")):
                raise BuildError(f"unresolved placeholder: {path.relative_to(root)}")


def source_identity(provenance: dict[Path, dict], provider_bytes: bytes) -> dict:
    """Return an identity that remains true after the generated bundle is committed."""
    inputs = sorted(
        (record["source"], record["source_sha256"])
        for record in provenance.values()
        if record["source"] is not None
    )
    inputs.append(("scripts/plugins/providers.yaml", digest(provider_bytes)))
    encoded = json.dumps(inputs, ensure_ascii=False, separators=(",", ":")).encode()
    return {"inputs": len(inputs), "sha256": digest(encoded)}


def build(
    output: Path,
    provider_id: str,
    repository: Path = REPOSITORY,
    providers_path: Path = PROVIDERS,
    replace: bool = False,
) -> dict:
    repository = repository.resolve()
    output = output.absolute()
    source_root = repository / "skills" / "alarina"
    resolved_output = output.resolve()
    if repository.is_relative_to(resolved_output) or (resolved_output.is_relative_to(repository) and not resolved_output.is_relative_to(repository / "plugins")):
        raise BuildError(f"output overlaps canonical source: {output}")
    if output.is_symlink() or (output.exists() and not output.is_dir()):
        raise BuildError(f"output is not a replaceable directory: {output}")
    if output.exists() and not replace:
        raise BuildError(f"output already exists: {output}")
    source_skill = source_root / "SKILL.md"
    metadata, body = frontmatter(source_skill)
    if metadata.get("name") != "alarina":
        raise BuildError("canonical skill name must be alarina")
    routes_path = source_root / "routes.yaml"
    routes = read_yaml(routes_path)
    commands, families = validate_routes(routes, repository, "alarina")
    validate_command_table(body, commands)
    provider_bytes = providers_path.read_bytes()
    provider = validate_provider(read_yaml(providers_path), provider_id)
    description = metadata["description"]
    trigger_length = len(description) + len(provider.get("when_to_use", ""))
    if trigger_length > provider["description_limit"]:
        raise BuildError("combined provider trigger metadata exceeds provider limit")
    version = json.loads((repository / "package.json").read_text(encoding="utf-8"))["version"]
    if not isinstance(version, str) or not version:
        raise BuildError("missing plugin version")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{output.name}.stage-", dir=output.parent) as temporary:
        staged = Path(temporary) / "bundle"
        skill_root = staged / provider["skill_path"]
        skill_root.mkdir(parents=True)
        provenance: dict[Path, dict] = {}
        for child in sorted(source_root.iterdir()):
            if child.name in ("SKILL.md", "agents"):
                continue
            if child.is_dir():
                copy_package(child, skill_root / child.name, provenance, repository)
            elif child.is_file():
                copy_file(child, skill_root / child.name, provenance, repository)
        appendix = f"Explicit plugin invocation: `{provider['qualified_invocation']} <request>`. Commands in the table above use this single Alárinà entrypoint; invoke a command by placing its ID first in `<request>`."
        values = {"name": "alarina", "description": description}
        if provider_id == "claude":
            values.update({"when_to_use": provider["when_to_use"], "argument-hint": "[request]", "user-invocable": True, "disable-model-invocation": False})
        rendered = "---\n" + yaml.safe_dump({key: values[key] for key in provider["frontmatter"]}, allow_unicode=True, sort_keys=False).rstrip() + "\n---\n\n" + body.rstrip() + "\n\n" + appendix + "\n"
        entry = skill_root / "SKILL.md"
        entry.write_text(rendered, encoding="utf-8")
        provenance[entry] = {"source": source_skill.relative_to(repository).as_posix(), "source_sha256": digest(source_skill.read_bytes())}
        if provider_id == "codex":
            original_metadata = source_root / "agents" / "openai.yaml"
            native = read_yaml(original_metadata)
            native.setdefault("policy", {})["allow_implicit_invocation"] = True
            target = skill_root / "agents" / "openai.yaml"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(yaml.safe_dump(native, allow_unicode=True, sort_keys=False), encoding="utf-8")
            provenance[target] = {"source": original_metadata.relative_to(repository).as_posix(), "source_sha256": digest(original_metadata.read_bytes())}
        else:
            agent_source = repository / "agents" / "alarina.md"
            agent_target = staged / "agents" / "alarina.md"
            agent_text = agent_source.read_text(encoding="utf-8")
            if agent_text.count("skills:\n  - alarina") != 1 or agent_text.count("`skills/alarina/SKILL.md`") != 1:
                raise BuildError("canonical agent preload or skill path differs from expected")
            agent_text = agent_text.replace("skills:\n  - alarina", "skills:\n  - qp-skills:alarina", 1)
            agent_text = agent_text.replace("`skills/alarina/SKILL.md`", "`${CLAUDE_PLUGIN_ROOT}/skills/alarina/SKILL.md`", 1)
            agent_target.parent.mkdir(parents=True, exist_ok=True)
            agent_target.write_text(agent_text, encoding="utf-8")
            provenance[agent_target] = {"source": agent_source.relative_to(repository).as_posix(), "source_sha256": digest(agent_source.read_bytes())}
        manifest_path = staged / provider["plugin_manifest"]
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        plugin = {"name": "qp-skills", "version": version, "description": "QP software-project work through Alárinà", "author": {"name": "Oluwaseyi Sobande"}, "license": "MIT"}
        if provider_id == "codex":
            plugin["skills"] = "./skills/"
        manifest_path.write_text(json.dumps(plugin, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        copy_file(repository / "LICENSE", staged / "LICENSE", provenance, repository)
        if len(list(staged.rglob("SKILL.md"))) != 1:
            raise BuildError("bundle must have exactly one discoverable SKILL.md")
        check_links(skill_root)
        check_tokens(staged)
        files = []
        for path in sorted(p for p in staged.rglob("*") if p.is_file()):
            record = {"path": path.relative_to(staged).as_posix(), "sha256": digest(path.read_bytes()), "mode": oct(path.stat().st_mode & 0o777)}
            record.update(provenance.get(path, {"source": None, "source_sha256": None}))
            files.append(record)
        result = {"compiler_version": COMPILER_VERSION, "plugin_version": version, "provider": provider_id, "support_state": provider["support_state"], "source": source_identity(provenance, provider_bytes), "route_digest": digest(routes_path.read_bytes()), "qualified_invocation": provider["qualified_invocation"], "aliases": [families[name]["alias"] for name in FAMILIES], "commands": [command["id"] for command in commands], "untested_native_claims": ["implicit selection", "runtime route loading"], "files": files}
        (staged / "bundle-manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        previous = None
        if output.exists() or output.is_symlink():
            previous = output.with_name(f".{output.name}.previous")
            if previous.exists() or previous.is_symlink():
                raise BuildError(f"replacement backup already exists: {previous}")
            output.rename(previous)
        try:
            staged.rename(output)
        except Exception:
            if previous is not None:
                previous.rename(output)
            raise
        if previous is not None:
            shutil.rmtree(previous)
    return result


def tree_snapshot(root: Path) -> dict[str, tuple[str, int]]:
    if not root.is_dir() or root.is_symlink():
        raise BuildError(f"bundle output is missing or unsafe: {root}")
    return {
        path.relative_to(root).as_posix(): (digest(path.read_bytes()), path.stat().st_mode & 0o777)
        for path in sorted(root.rglob("*"))
        if path.is_file() and not path.is_symlink()
    }


def verify_output(
    output: Path,
    provider_id: str,
    repository: Path = REPOSITORY,
    providers_path: Path = PROVIDERS,
) -> dict:
    """Rebuild in isolation and reject a missing, stale, or locally changed artifact."""
    actual = tree_snapshot(output)
    with tempfile.TemporaryDirectory(prefix="qp-alarina-check-") as temporary:
        candidate = Path(temporary) / "bundle"
        result = build(candidate, provider_id, repository, providers_path)
        expected = tree_snapshot(candidate)
    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        changed = sorted(path for path in set(actual) & set(expected) if actual[path] != expected[path])
        raise BuildError(f"stale bundle: missing={missing}, extra={extra}, changed={changed}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("codex", "claude"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replace", action="store_true", help="Replace a previous generated bundle after the candidate validates")
    parser.add_argument("--check", action="store_true", help="Rebuild in isolation and compare with the existing output")
    args = parser.parse_args()
    if args.check and args.replace:
        parser.error("--check and --replace cannot be combined")
    try:
        result = verify_output(args.output, args.provider) if args.check else build(args.output, args.provider, replace=args.replace)
    except (BuildError, OSError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps({"output": str(args.output), "provider": result["provider"], "files": len(result["files"]), "checked": args.check}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

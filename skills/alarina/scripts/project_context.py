"""Resolve Alárinà configuration and record locations without writing or executing checks."""
from __future__ import annotations

import hashlib
from copy import deepcopy
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


class ContextError(ValueError):
    """The requested context is ambiguous, invalid or unavailable."""


PERSONAL_KEYS = {"version", "state_root", "contribution_suggestions"}
PROJECT_KEYS = {
    "version", "doc_root", "checks", "required_tools", "remote_checks",
    "policy_sources", "workflow_roots",
}
DEFAULTS = {
    "version": 1, "state_root": "~/.qp/alarina", "doc_root": None,
    "checks": [], "required_tools": [], "remote_checks": [],
    "policy_sources": [], "workflow_roots": [], "contribution_suggestions": False,
}


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContextError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ContextError(f"cannot read valid JSON from {path}: {type(error).__name__}") from error
    if not isinstance(value, dict):
        raise ContextError(f"expected a JSON object: {path}")
    return value


def _text(value, name: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
        raise ContextError(f"{name} must be a nonempty string without control characters")
    return value


def _strings(value, name: str) -> list[str]:
    if not isinstance(value, list):
        raise ContextError(f"{name} must be an array")
    for item in value:
        _text(item, name)
    if len(value) != len(set(value)):
        raise ContextError(f"{name} contains duplicates")
    return value


def contained_path(root: Path, value: str, name: str, *, allow_root=False) -> Path:
    """Validate configured project-relative paths, including existing symlink parents."""
    _text(value, name)
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts or value.startswith("~"):
        raise ContextError(f"{name} must be a project-relative path without '..'")
    if ".git" in candidate.parts:
        raise ContextError(f"{name} cannot use Git metadata")
    root = root.resolve()
    try:
        resolved = (root / candidate).resolve()
    except (OSError, RuntimeError) as error:
        raise ContextError(f"{name} cannot be resolved") from error
    if not resolved.is_relative_to(root) or (resolved == root and not allow_root):
        raise ContextError(f"{name} must remain inside the project, below its root")
    if ".git" in resolved.relative_to(root).parts:
        raise ContextError(f"{name} resolves into Git metadata")
    return resolved


def _git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args], capture_output=True, text=True,
            timeout=10, check=False,
        )
    except FileNotFoundError:
        return None
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ContextError("cannot inspect project Git identity") from error
    return result.stdout.strip() if result.returncode == 0 else None


def _key(label: str, identity: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")[:40] or "project"
    return f"{slug}-{hashlib.sha256(os.fsencode(identity)).hexdigest()[:16]}"


def project_identity(project: Path) -> dict:
    root = project.expanduser().resolve()
    if not root.is_dir():
        raise ContextError(f"project directory does not exist: {root}")
    top = _git(root, "rev-parse", "--show-toplevel")
    common = None
    if top:
        root = Path(top).resolve()
        raw_common = _git(root, "rev-parse", "--git-common-dir")
        if not raw_common:
            raise ContextError("Git project has no discoverable common directory")
        common = (root / raw_common).resolve()
    elif (root / ".git").exists():
        raise ContextError("Git metadata exists but its identity could not be resolved")
    identity = str(common or root)
    label = common.parent.name if common and common.name == ".git" else root.name
    return {
        "root": str(root), "common_dir": str(common) if common else None,
        "id": _key(label, identity), "worktree_id": _key(root.name, str(root)),
    }


def _validate_check(check, root: Path) -> None:
    if not isinstance(check, dict):
        raise ContextError("each check must be an object")
    extra = set(check) - {"id", "argv", "cwd", "timeout_seconds", "proof"}
    if extra:
        raise ContextError(f"unsupported check fields: {', '.join(sorted(extra))}")
    identity = _text(check.get("id"), "check.id")
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}", identity):
        raise ContextError("check.id must be a simple name of at most 80 characters")
    argv = check.get("argv")
    if not isinstance(argv, list) or not argv:
        raise ContextError(f"{identity}.argv must be a nonempty argument array")
    for arg in argv:
        _text(arg, f"{identity}.argv")
    contained_path(root, check.get("cwd", "."), "check.cwd", allow_root=True)
    timeout = check.get("timeout_seconds", 300)
    if type(timeout) is not int or not 1 <= timeout <= 3600:
        raise ContextError("timeout_seconds must be an integer from 1 to 3600")
    proof = check.get("proof")
    if not isinstance(proof, dict) or set(proof) - {"type", "path"}:
        raise ContextError("check.proof must explicitly declare its type")
    if proof.get("type") not in {"exit", "unittest", "pytest", "tap", "junit"}:
        raise ContextError("unsupported check.proof.type")
    if proof["type"] == "junit":
        contained_path(root, proof.get("path"), "proof.path")
    elif "path" in proof:
        raise ContextError("proof.path is only supported for junit")


def _validate_layer(value: dict, root: Path, personal: bool) -> None:
    keys = PERSONAL_KEYS if personal else PROJECT_KEYS
    extra = set(value) - keys
    if extra:
        raise ContextError(f"unsupported configuration fields: {', '.join(sorted(extra))}")
    if type(value.get("version")) is not int or value["version"] != 1:
        raise ContextError("configuration version must be 1")
    if "state_root" in value:
        _text(value["state_root"], "state_root")
        if not (Path(value["state_root"]).is_absolute() or value["state_root"].startswith("~/")):
            raise ContextError("state_root must be absolute or start with '~/'; project namespaces are appended")
    if "contribution_suggestions" in value and type(value["contribution_suggestions"]) is not bool:
        raise ContextError("contribution_suggestions must be a boolean")
    if value.get("doc_root") is not None:
        contained_path(root, value["doc_root"], "doc_root")
    for key in ("required_tools", "remote_checks", "policy_sources", "workflow_roots"):
        if key in value:
            _strings(value[key], key)
    for key in ("policy_sources", "workflow_roots"):
        for item in value.get(key, []):
            contained_path(root, item, key)
    checks = value.get("checks", [])
    if not isinstance(checks, list):
        raise ContextError("checks must be an array")
    for check in checks:
        _validate_check(check, root)
    ids = [check["id"] for check in checks]
    if len(ids) != len(set(ids)):
        raise ContextError("duplicate check IDs")


def _home_path(value: str, home: Path) -> Path:
    path = home / value[2:] if value.startswith("~/") else Path(value)
    return path.resolve()


def load_context(project: Path, task: str | None = None, *, home: Path | None = None) -> dict:
    """Load optional personal, project and project-local layers; return provenance."""
    home = (home or Path.home()).resolve()
    identity = project_identity(project)
    root = Path(identity["root"])
    effective = deepcopy(DEFAULTS)
    sources = {key: "records.md default" if key in {"doc_root", "state_root"} else "default" for key in DEFAULTS}
    layers = []
    for path, personal in (
        (home / ".qp/alarina/config.json", True),
        (root / ".alarina.json", False),
        (root / ".alarina.local.json", True),
    ):
        if not path.exists() and not path.is_symlink():
            continue
        if path.parent == root and path.is_symlink():
            raise ContextError(f"project configuration cannot be a symlink: {path}")
        value = read_json(path)
        _validate_layer(value, root, personal)
        effective.update(value)
        sources.update({key: str(path) for key in value})
        layers.append(str(path))
    state_root = _home_path(effective["state_root"], home)
    if state_root == Path(state_root.anchor) or state_root == root or ".git" in state_root.parts:
        raise ContextError("state_root must be a dedicated directory outside Git metadata")
    project_state = state_root / "projects" / identity["id"]
    worktree_state = project_state / "worktrees" / identity["worktree_id"]
    locations = {
        "state_root": str(state_root), "project_state": str(project_state),
        "worktree_state": str(worktree_state), "project_workflows": str(project_state / "workflows"),
        "portable_workflows": str(state_root / "workflows/portable"),
        "task_root": None, "doc_root": None,
    }
    if task is not None:
        _text(task, "task")
        task_root = worktree_state / "tasks" / _key(task, task)
        locations["task_root"] = str(task_root)
        locations["doc_root"] = str(task_root / "artifacts")
    if effective["doc_root"] is not None:
        locations["doc_root"] = str(contained_path(root, effective["doc_root"], "doc_root"))
    # Detect private namespace symlinks too: a valid base must not hide cross-project mixing.
    for key in ("project_state", "worktree_state", "project_workflows", "portable_workflows", "task_root"):
        if locations[key] and Path(locations[key]).resolve() != Path(locations[key]):
            raise ContextError(f"{key} contains a symlink; use an explicit existing record instead")
    if effective["doc_root"] is None and locations["doc_root"] and Path(locations["doc_root"]).resolve() != Path(locations["doc_root"]):
        raise ContextError("default doc_root contains a symlink; use an explicit existing destination instead")
    digest = hashlib.sha256(json.dumps(effective, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "schema_version": 1, "project": identity, "task": task, "config": effective,
        "config_sources": sources, "loaded_files": layers, "config_digest": digest,
        "locations": locations,
    }


def resolve_destination(context: dict, *, kind: str, name: str | None = None,
                        destination: str | None = None, established_root: str | None = None) -> dict:
    """Explicit exact destination > existing owner > configured fallback > records.md."""
    root = Path(context["project"]["root"])
    if kind not in {"artifact", "record", "workflow", "portable-workflow"}:
        raise ContextError("unknown record kind")
    if name is not None:
        _text(name, "name")
    if established_root is not None:
        _text(established_root, "established_root")
    if destination is not None:
        _text(destination, "destination")
        chosen = Path(destination).expanduser()
        path = (root / chosen).resolve()
        source = "explicit destination"
    else:
        field = {"artifact": "doc_root", "record": "task_root", "workflow": "project_workflows",
                 "portable-workflow": "portable_workflows"}[kind]
        base = established_root if established_root is not None else context["locations"][field]
        if not base:
            raise ContextError("a stable --task identifier or an established destination is required")
        path = (root / Path(base).expanduser()).resolve()
        source = "established owner" if established_root else "records.md default"
        if not established_root and kind == "artifact" and context["config"]["doc_root"] is not None:
            source = context["config_sources"]["doc_root"]
        if name:
            path = contained_path(path, name, "name")
    if path == root or ".git" in path.parts:
        raise ContextError("destination cannot replace a project root or use Git metadata")
    return {"path": str(path), "source": source, "kind": kind, "created": False,
            "project_id": context["project"]["id"], "worktree_id": context["project"]["worktree_id"]}


def _executable(argv0: str, cwd: Path) -> str | None:
    if os.sep in argv0 or (os.altsep and os.altsep in argv0):
        path = (cwd / argv0).resolve()
        return str(path) if path.is_file() and os.access(path, os.X_OK) else None
    return shutil.which(argv0)


def doctor(context: dict) -> dict:
    """Report configuration/capability gaps; never run project commands or promise readiness."""
    root = Path(context["project"]["root"])
    config = context["config"]
    gaps = []
    check_results = []
    if not config["checks"]:
        gaps.append({"kind": "local_verification", "message": "No local gates are registered. Discover existing project checks and explicitly advise the user of missing verification before relying on CI."})
    for check in config["checks"]:
        cwd = contained_path(root, check.get("cwd", "."), "check.cwd", allow_root=True)
        executable = _executable(check["argv"][0], cwd)
        available = cwd.is_dir() and executable is not None
        check_results.append({"id": check["id"], "argv": check["argv"], "cwd": str(cwd),
                              "executable": executable, "available": available, "executed": False})
        if not available:
            gaps.append({"kind": "check_prerequisite", "check": check["id"], "message": "Check working directory or executable is unavailable."})
    tools = [{"name": name, "path": _executable(name, root)} for name in config["required_tools"]]
    for item in tools:
        if not item["path"]:
            gaps.append({"kind": "required_tool", "name": item["name"], "message": "Required executable is unavailable."})
    policy_sources = []
    for value in config["policy_sources"]:
        path = contained_path(root, value, "policy_sources")
        policy_sources.append({"path": str(path), "exists": path.is_file()})
        if not path.is_file():
            gaps.append({"kind": "policy_source", "message": f"Declared policy source is missing: {value}"})
    suggestions = []
    package = root / "package.json"
    if package.is_symlink():
        gaps.append({"kind": "discovery", "message": "package.json is a symlink; discover project checks manually."})
    elif package.is_file():
        try:
            data = read_json(package)
            scripts = data.get("scripts", {})
            if not isinstance(scripts, dict) or any(not isinstance(value, str) for value in scripts.values()):
                raise ContextError("package.json scripts must be an object of strings")
            for name in sorted(scripts):
                if re.search(r"(^|:)(test|check|lint|typecheck|verify|build)(:|$)", name):
                    suggestions.append({"source": "package.json", "argv": ["npm", "run", name], "verified": False})
        except ContextError:
            gaps.append({"kind": "discovery", "message": "package.json could not be inspected; discover project checks manually."})
    return {
        "schema_version": 1, "status": "gaps" if gaps else "configured",
        "project": context["project"], "config_sources": context["config_sources"],
        "locations": context["locations"], "checks": check_results, "required_tools": tools,
        "policy_sources": policy_sources, "remote_checks": config["remote_checks"],
        "unverified_suggestions": suggestions, "gaps": gaps, "executed": False,
        "limits": ["Configured commands are not executed proof.",
                   "Read applicable scoped project instructions; this does not interpret policy precedence.",
                   "Model, subagent and permission settings belong to the user and host."],
    }

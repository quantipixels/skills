#!/usr/bin/env python3
"""Verify faithful installation through the native Codex and Claude managers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
PACKAGE_NAME = "qp-skills"
MARKETPLACE_NAME = "qp-skills"
PACKAGE_SELECTOR = f"{PACKAGE_NAME}@{MARKETPLACE_NAME}"
DEFAULT_TIMEOUT = 30.0
PACKAGE_INPUTS = (
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    "skills",
    "agents",
)


class NativeVerificationError(RuntimeError):
    """A bounded native installation check could not establish its contract."""


def _group_exists(process):
    try:
        os.killpg(process.pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError as error:
        members = _process_group_members(process.pid)
        if members is None:
            raise NativeVerificationError(f"cannot inspect command process group: {error}") from error
        return bool(members)
    return True


def _process_group_members(pgid):
    try:
        result = subprocess.run(
            ["ps", "-axo", "pid=,pgid="],
            text=True,
            capture_output=True,
            check=False,
            timeout=0.25,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise NativeVerificationError(f"cannot enumerate command process group {pgid}: {error}") from error
    if result.returncode != 0:
        raise NativeVerificationError(f"cannot enumerate command process group {pgid}: ps exited {result.returncode}")
    members = set()
    lines = result.stdout.splitlines()
    if not lines:
        raise NativeVerificationError("process-group enumeration returned no process records")
    for line in lines:
        fields = line.split()
        if len(fields) != 2 or not all(field.isdigit() for field in fields):
            raise NativeVerificationError("process-group enumeration returned a malformed process record")
        if int(fields[1]) == pgid:
            members.add(int(fields[0]))
    return members


def _stop_process_group(process, grace=0.5):
    if os.name != "posix":
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=grace)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=grace)
        return
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    except PermissionError as error:
        raise NativeVerificationError(f"cannot terminate command process group: {error}") from error
    deadline = time.monotonic() + grace
    while _group_exists(process) and time.monotonic() < deadline:
        process.poll()
        time.sleep(0.01)
    if _group_exists(process):
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        except PermissionError as error:
            raise NativeVerificationError(f"cannot kill command process group: {error}") from error
        deadline = time.monotonic() + grace
        while _group_exists(process) and time.monotonic() < deadline:
            process.poll()
            time.sleep(0.01)
        if _group_exists(process):
            raise NativeVerificationError(f"command process group {process.pid} remained after SIGKILL")
    try:
        process.wait(timeout=grace)
    except subprocess.TimeoutExpired as error:
        raise NativeVerificationError(f"command leader {process.pid} was not reaped") from error


def run(command, env, timeout=DEFAULT_TIMEOUT):
    """Run one native manager command with bounded execution and owned cleanup."""
    try:
        process = subprocess.Popen(
            command,
            cwd=ROOT,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=os.name == "posix",
        )
    except OSError as error:
        raise NativeVerificationError(f"command could not start ({' '.join(command)}): {error}") from error
    timed_out = False
    cleanup_error = None
    stdout = stderr = ""
    try:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired as error:
            timed_out = True
            stdout = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else error.stdout or ""
            stderr = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else error.stderr or ""
        try:
            _stop_process_group(process)
        except NativeVerificationError as error:
            cleanup_error = str(error)
            try:
                process.kill()
                process.wait(timeout=1)
            except (OSError, subprocess.TimeoutExpired) as fallback:
                cleanup_error = f"{cleanup_error}; fallback reap failed: {fallback}"
        if timed_out:
            try:
                tail_out, tail_err = process.communicate(timeout=1)
                stdout = tail_out or stdout
                stderr = tail_err or stderr
            except subprocess.TimeoutExpired as error:
                cleanup_error = cleanup_error or f"pipes remained open after timeout: {error}"
    finally:
        if process.stdout is not None:
            process.stdout.close()
        if process.stderr is not None:
            process.stderr.close()
    if cleanup_error:
        raise NativeVerificationError(
            f"command cleanup failed ({' '.join(command)}): {cleanup_error}\n{stderr}".strip()
        )
    if timed_out:
        raise NativeVerificationError(f"command timed out after {timeout:g}s ({' '.join(command)})\n{stderr}".strip())
    if process.returncode:
        raise NativeVerificationError(
            f"command failed ({process.returncode}): {' '.join(command)}\n{stdout}{stderr}".strip()
        )
    return stdout


def load_json(output, command):
    try:
        value = json.loads(output)
    except (json.JSONDecodeError, TypeError) as error:
        raise NativeVerificationError(f"{command} did not return JSON: {error}") from error
    return value


def require_mapping(value, label):
    if not isinstance(value, dict):
        raise NativeVerificationError(f"{label} returned {type(value).__name__}; expected an object")
    return value


def require_list(value, label):
    if not isinstance(value, list):
        raise NativeVerificationError(f"{label} returned {type(value).__name__}; expected a list")
    return value


def _path_value(value, label):
    if not isinstance(value, str) or not value.strip():
        raise NativeVerificationError(f"{label} did not include an installation path")
    path = Path(value).expanduser()
    if not path.is_dir():
        raise NativeVerificationError(f"{label} installation path is missing: {path}")
    return path.resolve()


def _plugin_id(item):
    if not isinstance(item, dict):
        return None
    for key in ("pluginId", "id", "name"):
        if isinstance(item.get(key), str):
            return item[key]
    return None


def require_enabled_plugin(items, label):
    if any(not isinstance(item, dict) for item in items):
        raise NativeVerificationError(f"{label} returned a malformed plugin entry")
    matches = [item for item in items if _plugin_id(item) in {PACKAGE_NAME, PACKAGE_SELECTOR}]
    if len(matches) != 1:
        raise NativeVerificationError(f"{label} did not report exactly one {PACKAGE_NAME} plugin")
    if matches[0].get("enabled") is not True:
        raise NativeVerificationError(f"{label} reported {PACKAGE_NAME} as disabled")
    return matches[0]


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _source_identity():
    try:
        revision = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=False, timeout=5
        )
    except (OSError, subprocess.TimeoutExpired):
        revision = None
    try:
        status = subprocess.run(
            ["git", "status", "--short"], cwd=ROOT, text=True, capture_output=True, check=False, timeout=5
        )
    except (OSError, subprocess.TimeoutExpired):
        status = None
    return {
        "root": str(ROOT),
        "revision": revision.stdout.strip() if revision and revision.returncode == 0 else None,
        "working_tree_clean": status is not None and status.returncode == 0 and not status.stdout.strip(),
        "package_inputs": list(PACKAGE_INPUTS),
        "package_tree_sha256": _tree_digest(ROOT),
    }


def _tree_digest(root):
    entries = []
    paths = []
    for relative in PACKAGE_INPUTS:
        path = root / relative
        if path.is_file():
            paths.append(path)
        elif path.is_dir():
            paths.extend(candidate for candidate in path.rglob("*") if candidate.is_file())
    for path in sorted(paths):
        if path.is_symlink() or "__pycache__" in path.parts or ".pytest_cache" in path.parts:
            continue
        entries.append((path.relative_to(root).as_posix(), _sha256(path)))
    return hashlib.sha256(json.dumps(entries, separators=(",", ":")).encode()).hexdigest()


def _inventory_scope(root):
    skills_root = root / "skills"
    agents_root = root / "agents"
    skill_names = sorted(path.name for path in skills_root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()) if skills_root.is_dir() else []
    agent_names = sorted(path.name for path in agents_root.glob("*.md") if path.is_file()) if agents_root.is_dir() else []
    return {"skills": len(skill_names), "agents": len(agent_names), "skill_names": skill_names, "agent_names": agent_names}


def validate_installed_inventory(installed_root, host):
    source = _inventory_scope(ROOT)
    if not source["skill_names"]:
        raise NativeVerificationError("source inventory is empty or unavailable")
    installed = _inventory_scope(installed_root)
    if installed["skill_names"] != source["skill_names"]:
        raise NativeVerificationError(f"{host} installed skill inventory differs from source")
    if host == "claude" and installed["agent_names"] != source["agent_names"]:
        raise NativeVerificationError(f"{host} installed agent inventory differs from source")
    return source, installed


def sample_files(installed_root, manifest_path):
    """Compare a small explicit source sample and return its observed hashes."""
    relative_paths = [manifest_path, "skills/alarina/SKILL.md"]
    # A fresh SKILL.md with stale/missing references is still a stale updater.
    updater = Path("skills/qp-update")
    if not (ROOT / updater / "SKILL.md").is_file():
        raise NativeVerificationError("source inventory is missing qp-update/SKILL.md")
    source_files = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / updater).rglob("*") if path.is_file())
    installed_files = sorted(path.relative_to(installed_root).as_posix() for path in (installed_root / updater).rglob("*") if path.is_file())
    if source_files != installed_files:
        raise NativeVerificationError("installed updater file inventory differs from source")
    relative_paths.extend(source_files)
    if (ROOT / "agents/alarina.md").is_file() and (installed_root / "agents/alarina.md").is_file():
        relative_paths.append("agents/alarina.md")
    samples = []
    for relative in relative_paths:
        source = ROOT / relative
        installed = installed_root / relative
        if not source.is_file() or not installed.is_file():
            raise NativeVerificationError(f"installed plugin is missing sampled file: {relative}")
        source_hash = _sha256(source)
        installed_hash = _sha256(installed)
        if source_hash != installed_hash:
            raise NativeVerificationError(f"installed sampled file differs from source: {relative}")
        samples.append({"path": relative, "source_sha256": source_hash, "installed_sha256": installed_hash})
    return samples


def validate_claude_validation(value):
    value = require_mapping(value, "claude plugin validate")
    manifest = value.get("manifest")
    if not isinstance(manifest, dict):
        raise NativeVerificationError("Claude validation returned no manifest object")
    if value.get("success") is not True or manifest.get("errors"):
        raise NativeVerificationError("Claude rejected the plugin manifest")
    return value


def _result(host, version, installed_root, manifest_path, extra=None):
    source_scope, installed_scope = validate_installed_inventory(installed_root, host)
    result = {
        "host": host,
        "version": version.strip(),
        "package": PACKAGE_NAME,
        "selector": PACKAGE_SELECTOR,
        "source": _source_identity(),
        "source_scope": source_scope,
        "installed_scope": installed_scope,
        "sampled_files": sample_files(installed_root, manifest_path),
    }
    if extra:
        result.update(extra)
    return result


def verify_upgrade_snapshot(before_root, installed_root, host):
    """Read-only A/B evidence; caller supplies a saved pre-update plugin copy.

    This comparison cannot establish that a manager performed the transition,
    that its registration/scope was preserved, or that a session reloaded.
    """
    if host not in {"codex", "claude"}:
        raise NativeVerificationError("snapshot comparison requires one native host")
    before_root = _path_value(str(before_root), "before snapshot")
    installed_root = _path_value(str(installed_root), "installed snapshot")
    if before_root in {installed_root, ROOT.resolve()}:
        raise NativeVerificationError("before snapshot must be separate from source and installed roots")
    manifest_path = f".{host}-plugin/plugin.json"
    for root, label in ((ROOT, "source"), (before_root, "before snapshot"), (installed_root, "installed snapshot")):
        manifest = require_mapping(load_json((root / manifest_path).read_text(), label), label)
        if manifest.get("name") != PACKAGE_NAME:
            raise NativeVerificationError(f"{label} has a different plugin identity")
    before = _inventory_scope(before_root)
    if not before["skill_names"]:
        raise NativeVerificationError("before snapshot inventory is empty or unavailable")
    result = _result(host, "", installed_root, manifest_path)
    installed_digest = _tree_digest(installed_root)
    if installed_digest != result["source"]["package_tree_sha256"]:
        raise NativeVerificationError("installed package content differs from source")
    current_names = set(result["installed_scope"]["skill_names"])
    previous_names = set(before["skill_names"])
    result.update({
        "version": None,
        "evidence": "snapshot-comparison",
        "before_root": str(before_root),
        "before_scope": before,
        "before_tree_sha256": _tree_digest(before_root),
        "installed_path": str(installed_root),
        "installed_tree_sha256": installed_digest,
        "added_skills": sorted(current_names - previous_names),
        "retired_skills": sorted(previous_names - current_names),
        "manager_transition": "not_observed",
        "session_activation": "not_observed",
    })
    return result


def verify_codex():
    if not shutil.which("codex"):
        raise NativeVerificationError("codex executable is unavailable")
    with tempfile.TemporaryDirectory(prefix="qp-codex-home-") as home:
        env = os.environ.copy()
        env["CODEX_HOME"] = home
        marketplace = require_mapping(
            load_json(run(["codex", "plugin", "marketplace", "add", str(ROOT), "--json"], env), "codex marketplace add"),
            "codex marketplace add",
        )
        if marketplace.get("marketplaceName") != MARKETPLACE_NAME:
            raise NativeVerificationError("Codex registered an unexpected marketplace identity")
        install = require_mapping(
            load_json(run(["codex", "plugin", "add", PACKAGE_NAME, "--marketplace", MARKETPLACE_NAME, "--json"], env), "codex plugin add"),
            "codex plugin add",
        )
        installed_root = _path_value(install.get("installedPath") or install.get("installPath"), "Codex install result")
        listing = require_mapping(
            load_json(run(["codex", "plugin", "list", "--json"], env), "codex plugin list"),
            "codex plugin list",
        )
        installed = require_list(listing.get("installed"), "Codex plugin list")
        require_enabled_plugin(installed, "Codex plugin list")
        return _result("codex", run(["codex", "--version"], env), installed_root, ".codex-plugin/plugin.json", {"installed_path": str(installed_root)})


def verify_claude():
    if not shutil.which("claude"):
        raise NativeVerificationError("claude executable is unavailable")
    with tempfile.TemporaryDirectory(prefix="qp-claude-home-") as home:
        env = os.environ.copy()
        env["CLAUDE_CONFIG_DIR"] = home
        validation = validate_claude_validation(
            load_json(run(["claude", "plugin", "validate", str(ROOT), "--json"], env), "claude plugin validate"),
        )
        run(["claude", "plugin", "marketplace", "add", str(ROOT), "--scope", "user"], env)
        run(["claude", "plugin", "install", PACKAGE_SELECTOR, "--scope", "user", "--yes"], env)
        listing = require_list(
            load_json(run(["claude", "plugin", "list", "--json"], env), "claude plugin list"),
            "claude plugin list",
        )
        installed = require_enabled_plugin(listing, "Claude plugin list")
        installed_root = _path_value(installed.get("installPath") or installed.get("installedPath"), "Claude install result")
        inventory = run(["claude", "plugin", "details", PACKAGE_SELECTOR], env)
        scope = _inventory_scope(ROOT)
        for expected in (f"Skills ({scope['skills']})", f"Agents ({scope['agents']})", "alarina"):
            if expected not in inventory:
                raise NativeVerificationError(f"Claude inventory is missing {expected!r}")
        return _result(
            "claude",
            run(["claude", "--version"], env),
            installed_root,
            ".claude-plugin/plugin.json",
            {"installed_path": str(installed_root), "inventory": inventory},
        )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("all", "codex", "claude"), default="all")
    parser.add_argument("--before-root", help="Saved pre-update native plugin copy; comparison only")
    parser.add_argument("--installed-root", help="Post-update native plugin root; comparison only")
    args = parser.parse_args(argv)
    comparing = args.before_root is not None or args.installed_root is not None
    if comparing and (not args.before_root or not args.installed_root or args.host == "all"):
        parser.error("snapshot comparison requires --before-root, --installed-root and one --host")
    try:
        results = []
        if comparing:
            results.append(verify_upgrade_snapshot(args.before_root, args.installed_root, args.host))
        elif args.host in ("all", "codex"):
            results.append(verify_codex())
        if not comparing and args.host in ("all", "claude"):
            results.append(verify_claude())
    except (NativeVerificationError, OSError, ValueError) as error:
        print(json.dumps({"success": False, "error": str(error)}, indent=2))
        return 1
    print(json.dumps({"success": True, "results": results}, indent=2))
    print("Fresh-session skill invocation remains a separate runtime check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

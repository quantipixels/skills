#!/usr/bin/env python3
"""Verify a native install or compare saved before/after package snapshots."""
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
PACKAGE = "qp-skills"
SELECTOR = "qp-skills@qp-skills"
DECLARATIONS = (
    ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
    "agents/alarina.md", "agents/alarina.codex.toml", "agents/alarina.claude.md",
    ".opencode/agents/alarina.md", "opencode.json", "package.json",
    "LICENSE",
)


class NativeVerificationError(ValueError):
    pass


def _process_group_members(pgid: int) -> set[int]:
    try:
        result = subprocess.run(["ps", "-axo", "pid=,pgid="], text=True, capture_output=True, timeout=0.25)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise NativeVerificationError(f"cannot enumerate command process group {pgid}: {error}") from error
    if result.returncode:
        raise NativeVerificationError(f"cannot enumerate command process group {pgid}: ps exited {result.returncode}")
    lines = result.stdout.splitlines()
    if not lines:
        raise NativeVerificationError("process-group enumeration returned no process records")
    members = set()
    for line in lines:
        fields = line.split()
        if len(fields) != 2 or not all(field.isdigit() for field in fields):
            raise NativeVerificationError("process-group enumeration returned a malformed process record")
        if int(fields[1]) == pgid:
            members.add(int(fields[0]))
    return members


def _group_exists(process) -> bool:
    try:
        os.killpg(process.pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError as error:
        return bool(_process_group_members(process.pid))
    return True


def _stop_process_group(process, grace: float = 0.5) -> None:
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
    deadline = time.monotonic() + grace
    while _group_exists(process) and time.monotonic() < deadline:
        process.poll()
        time.sleep(0.01)
    if _group_exists(process):
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        deadline = time.monotonic() + grace
        while _group_exists(process) and time.monotonic() < deadline:
            process.poll()
            time.sleep(0.01)
        if _group_exists(process):
            raise NativeVerificationError(f"command process group {process.pid} remained after SIGKILL")
    process.wait(timeout=grace)


def run(command: list[str], env: dict[str, str], timeout: float = 90) -> str:
    try:
        process = subprocess.Popen(command, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, start_new_session=os.name == "posix")
    except OSError as error:
        raise NativeVerificationError(f"command could not start: {error}") from error
    timed_out = False
    stdout = stderr = ""
    try:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired as error:
            timed_out = True
            stdout = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else error.stdout or ""
            stderr = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else error.stderr or ""
        _stop_process_group(process)
        if timed_out:
            try:
                tail_out, tail_err = process.communicate(timeout=1)
                stdout = tail_out or stdout
                stderr = tail_err or stderr
            except subprocess.TimeoutExpired as error:
                raise NativeVerificationError(f"pipes remained open after timeout: {error}") from error
    finally:
        if process.stdout is not None:
            process.stdout.close()
        if process.stderr is not None:
            process.stderr.close()
    if timed_out:
        raise NativeVerificationError(f"command timed out after {timeout:g}s: {' '.join(command)}")
    if process.returncode:
        raise NativeVerificationError(f"command failed ({process.returncode}): {' '.join(command)}\n{stdout}{stderr}")
    return stdout


def load_json(value: str, label: str):
    try:
        return json.loads(value)
    except json.JSONDecodeError as error:
        raise NativeVerificationError(f"{label} did not return JSON") from error


def _manifest(root: Path, host: str) -> dict:
    path = root / f".{host}-plugin/plugin.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise NativeVerificationError(f"missing or invalid {host} manifest: {path}") from error
    if value.get("name") != PACKAGE or not isinstance(value.get("version"), str):
        raise NativeVerificationError(f"foreign {host} package identity: {path}")
    return value


def _files(root: Path) -> dict[str, str]:
    if not root.is_dir():
        raise NativeVerificationError(f"package root is missing: {root}")
    paths = [root / relative for relative in DECLARATIONS]
    paths.extend((root / "skills/alarina").rglob("*"))
    result = {}
    for path in paths:
        if path.is_symlink():
            raise NativeVerificationError(f"package contains a symlink: {path}")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def _inventory(root: Path) -> list[str]:
    return sorted(path.relative_to(root).as_posix() for path in root.glob("skills/**/SKILL.md"))


def compare_installed_files(installed_root: Path, source_root: Path) -> int:
    expected = _files(source_root)
    observed = _files(installed_root)
    if observed != expected:
        changed = sorted(path for path in expected.keys() & observed.keys() if expected[path] != observed[path])
        added = sorted(observed.keys() - expected.keys())
        missing = sorted(expected.keys() - observed.keys())
        raise NativeVerificationError(f"installed package content differs: changed={changed}, added={added}, missing={missing}")
    if _inventory(installed_root) != ["skills/alarina/SKILL.md"]:
        raise NativeVerificationError("installed skill inventory differs from one Alárinà entry")
    return len(expected)


def stage_package(destination: Path) -> None:
    """Export the declared runtime surface, excluding checkout and ignored state."""
    paths = {Path(item) for item in DECLARATIONS}
    paths.add(Path("LICENSE"))
    paths.update(path.relative_to(ROOT) for path in (ROOT / "skills/alarina").rglob("*") if path.is_file())
    for relative in sorted(paths):
        source = ROOT / relative
        if not source.is_file():
            raise NativeVerificationError(f"runtime package file is missing: {relative}")
        if source.is_symlink():
            raise NativeVerificationError(f"tracked package contains a symlink: {relative}")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def verify_upgrade_snapshot(before_root: Path, installed_root: Path, host: str, source_root: Path = ROOT) -> dict:
    if host not in {"codex", "claude"}:
        raise NativeVerificationError("snapshot comparison requires Codex or Claude")
    before_root, installed_root, source_root = (Path(path).resolve() for path in (before_root, installed_root, source_root))
    if before_root in {installed_root, source_root}:
        raise NativeVerificationError("before snapshot must be separate from source and installed roots")
    versions = {label: _manifest(root, host)["version"] for label, root in
                (("source", source_root), ("before", before_root), ("installed", installed_root))}
    count = compare_installed_files(installed_root, source_root)
    before = {path.relative_to(before_root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in before_root.rglob("*") if path.is_file()}
    after = _files(source_root)
    return {
        "host": host, "evidence": "snapshot-comparison", "versions": versions,
        "before_root": str(before_root), "installed_path": str(installed_root),
        "verified_file_count": count,
        "changed_paths": sorted(path for path in before.keys() & after.keys() if before[path] != after[path]),
        "added_paths": sorted(after.keys() - before.keys()),
        "removed_paths": sorted(before.keys() - after.keys()),
        "manager_transition": "not_observed", "session_activation": "not_observed",
    }


def _installed_path(value, label: str) -> Path:
    if not isinstance(value, str) or not Path(value).is_dir():
        raise NativeVerificationError(f"{label} returned no installed path")
    return Path(value).resolve()


def verify_native(host: str) -> dict:
    executable = "codex" if host == "codex" else "claude"
    if not shutil.which(executable):
        raise NativeVerificationError(f"{executable} executable is unavailable")
    with tempfile.TemporaryDirectory(prefix="qp-native-package-") as temporary:
        base = Path(temporary)
        package = base / "package"
        package.mkdir()
        stage_package(package)
        env = os.environ.copy()
        if host == "codex":
            env["CODEX_HOME"] = str(base / "codex-home")
            Path(env["CODEX_HOME"]).mkdir()
            added = load_json(run(["codex", "plugin", "marketplace", "add", str(package), "--json"], env), "Codex marketplace add")
            if added.get("marketplaceName") != PACKAGE:
                raise NativeVerificationError("Codex registered an unexpected marketplace")
            installed = load_json(run(["codex", "plugin", "add", PACKAGE, "--marketplace", PACKAGE, "--json"], env), "Codex plugin add")
            path = _installed_path(installed.get("installedPath") or installed.get("installPath"), "Codex install")
        else:
            env["CLAUDE_CONFIG_DIR"] = str(base / "claude-home")
            Path(env["CLAUDE_CONFIG_DIR"]).mkdir()
            validation = load_json(run(["claude", "plugin", "validate", str(package / ".claude-plugin/plugin.json"), "--json"], env), "Claude validate")
            if validation.get("success") is not True:
                raise NativeVerificationError("Claude rejected plugin manifest")
            run(["claude", "plugin", "marketplace", "add", str(package), "--scope", "user"], env)
            run(["claude", "plugin", "install", SELECTOR, "--scope", "user", "--yes"], env)
            listing = load_json(run(["claude", "plugin", "list", "--json"], env), "Claude plugin list")
            matches = [item for item in listing if item.get("pluginId") in {PACKAGE, SELECTOR} or item.get("id") in {PACKAGE, SELECTOR}]
            if len(matches) != 1 or matches[0].get("enabled") is not True:
                raise NativeVerificationError(f"Claude plugin list did not report one enabled qp-skills: {listing}")
            path = _installed_path(matches[0].get("installPath") or matches[0].get("installedPath"), "Claude install")
        count = compare_installed_files(path, package)
        return {"host": host, "evidence": "native-manager-install", "installed_path": str(path),
                "plugin_version": _manifest(path, host)["version"], "verified_file_count": count,
                "session_activation": "not_observed"}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("all", "codex", "claude"), default="all")
    parser.add_argument("--before-root", type=Path)
    parser.add_argument("--installed-root", type=Path)
    parser.add_argument("--export", type=Path, help="Write a clean runtime package to a new directory")
    args = parser.parse_args(argv)
    comparing = args.before_root is not None or args.installed_root is not None
    if args.export is not None:
        if comparing:
            parser.error("--export cannot be combined with snapshot comparison")
        destination = args.export.resolve()
        if destination.exists() or destination.is_relative_to(ROOT):
            parser.error("export destination must be a new directory outside the repository")
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix=".qp-package-stage-", dir=destination.parent) as temporary:
                staging = Path(temporary) / "package"
                staging.mkdir()
                stage_package(staging)
                staging.rename(destination)
        except (OSError, NativeVerificationError) as error:
            print(json.dumps({"success": False, "error": str(error)}))
            return 1
        print(json.dumps({"success": True, "exported_path": str(destination), "files": len(_files(destination))}))
        return 0
    if comparing and (not args.before_root or not args.installed_root or args.host == "all"):
        parser.error("snapshot comparison requires both roots and one host")
    try:
        results = ([verify_upgrade_snapshot(args.before_root, args.installed_root, args.host)] if comparing else
                   [verify_native(host) for host in (("codex", "claude") if args.host == "all" else (args.host,))])
    except (NativeVerificationError, OSError, ValueError) as error:
        print(json.dumps({"success": False, "error": str(error)}, indent=2))
        return 1
    print(json.dumps({"success": True, "results": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

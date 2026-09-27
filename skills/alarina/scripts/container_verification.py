#!/usr/bin/env python3
"""Use an existing running dev container to run the project's existing verifier."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import selectors
import subprocess
import sys
import time
import uuid

MAX_JSON = 256 * 1024
MAX_RECEIPT = 16 * 1024 * 1024


class ContainerVerificationError(ValueError):
    pass


def _host_snapshot(project: Path) -> dict:
    from local_checks import candidate_snapshot
    return candidate_snapshot(project)


def _config(project: Path) -> dict:
    choices = [project / ".devcontainer/devcontainer.json", project / ".devcontainer.json"]
    found = [path for path in choices if path.exists() or path.is_symlink()]
    if len(found) != 1 or found[0].is_symlink() or not found[0].is_file():
        raise ContainerVerificationError("one regular project devcontainer config is required")
    path = found[0]
    if path.stat().st_size > MAX_JSON or path.parent.is_symlink():
        raise ContainerVerificationError("devcontainer config is linked or oversized")
    return {"path": path.relative_to(project).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def _candidate_files(snapshot: dict) -> list[tuple]:
    if not isinstance(snapshot, dict) or snapshot.get("kind") != "git" or snapshot.get("complete") is not True:
        raise ContainerVerificationError("complete Git candidate inventory is required")
    files = snapshot.get("files")
    if not isinstance(files, list) or not files:
        raise ContainerVerificationError("candidate file inventory is missing")
    normalized = []
    for item in files:
        if not isinstance(item, dict) or item.get("kind") not in {"file", "deleted", "symlink"}:
            raise ContainerVerificationError("candidate file inventory is unsupported")
        mode = item.get("mode")
        if not isinstance(mode, int):
            raise ContainerVerificationError("candidate file mode is missing")
        normalized.append((item.get("path"), item.get("kind"), item.get("sha256"),
                           item.get("size"), item.get("target"), mode & 0o111))
    return sorted(normalized)


def _same_candidate(host: dict, container: dict) -> bool:
    return (host.get("head") == container.get("head") and
            host.get("base_oid") == container.get("base_oid") and
            host.get("index") == container.get("index") and
            _candidate_files(host) == _candidate_files(container))


def _run(argv: list[str], timeout: int) -> tuple[int, str]:
    try:
        process = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL)
    except OSError as error:
        raise ContainerVerificationError("Docker command could not start") from error
    chunks = []
    size = 0
    deadline = time.monotonic() + timeout
    try:
        with selectors.DefaultSelector() as selector:
            selector.register(process.stdout, selectors.EVENT_READ)
            while selector.get_map():
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ContainerVerificationError(
                        "Docker client timed out; container-side check state is unknown. Inspect the receipt and container before retrying")
                for key, _ in selector.select(remaining):
                    block = key.fileobj.read1(65536)
                    if not block:
                        selector.unregister(key.fileobj)
                        continue
                    size += len(block)
                    if size > MAX_JSON:
                        raise ContainerVerificationError("Docker output exceeded limit; container-side check state is unknown")
                    chunks.append(block)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise ContainerVerificationError("Docker client timed out; container-side check state is unknown")
        return process.wait(timeout=remaining), b"".join(chunks).decode("utf-8", errors="replace")
    except subprocess.TimeoutExpired as error:
        raise ContainerVerificationError("Docker client timed out; container-side check state is unknown") from error
    finally:
        if process.poll() is None:
            process.kill()  # Only the local Docker client; remote checks may continue.
        process.wait()
        if process.stdout is not None:
            process.stdout.close()


def _json(text: str, label: str, *, limit: int = MAX_JSON) -> object:
    if len(text.encode("utf-8")) > limit:
        raise ContainerVerificationError(f"{label} exceeded limit")
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise ContainerVerificationError(f"{label} returned malformed JSON") from error


def _container_path(value: str, label: str) -> PurePosixPath:
    if not isinstance(value, str) or not value.startswith("/") or "\x00" in value:
        raise ContainerVerificationError(f"{label} must be an absolute container path")
    path = PurePosixPath(value)
    if ".." in path.parts or str(path) != value.rstrip("/"):
        raise ContainerVerificationError(f"{label} must be normalized")
    return path


def _read_receipt(path: Path) -> dict:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_RECEIPT:
        raise ContainerVerificationError("verification receipt is missing, linked, or oversized")
    data = _json(path.read_text(encoding="utf-8"), "verification receipt", limit=MAX_RECEIPT)
    if not isinstance(data, dict):
        raise ContainerVerificationError("verification receipt must be an object")
    return data


def verify_existing(container_id: str, project: Path, workspace: str, runner: str, *,
                    run=_run, snapshot=_host_snapshot, expected_runner_sha: str | None = None,
                    output_relative: str | None = None, timeout: int = 900) -> dict:
    if os.name != "posix":
        raise ContainerVerificationError("container verification requires a POSIX host and container")
    if not re.fullmatch(r"[0-9a-fA-F]{12,64}", container_id):
        raise ContainerVerificationError("container must be a 12..64 character hex ID")
    project = Path(project).resolve(strict=True)
    if not project.is_dir():
        raise ContainerVerificationError("project is not a directory")
    workspace_path = _container_path(workspace, "workspace")
    runner_path = _container_path(runner, "runner")
    configuration = _config(project)
    host_before = snapshot(project)
    _candidate_files(host_before)
    if timeout < 1 or timeout > 7200:
        raise ContainerVerificationError("timeout must be 1..7200 seconds")
    if output_relative is None:
        output_relative = f".qp/container-verification/{uuid.uuid4().hex}"
    relative = PurePosixPath(output_relative)
    if (relative.is_absolute() or ".." in relative.parts or
            not relative.parts or relative.parts[0] != ".qp"):
        raise ContainerVerificationError("output must be a fresh relative path below .qp")
    host_output = project.joinpath(*relative.parts)
    if any(project.joinpath(*relative.parts[:i]).is_symlink() for i in range(1, len(relative.parts) + 1)):
        raise ContainerVerificationError("output path contains a symlink")
    if host_output.exists() or host_output.is_symlink():
        raise ContainerVerificationError("output already exists")
    container_output = str(workspace_path / relative)
    code, raw = run(["docker", "inspect", "--type=container", container_id], min(timeout, 20))
    if code:
        raise ContainerVerificationError("Docker inspect failed")
    inspected = _json(raw, "Docker inspect")
    if not isinstance(inspected, list) or len(inspected) != 1 or not isinstance(inspected[0], dict):
        raise ContainerVerificationError("Docker inspect did not identify one container")
    info = inspected[0]
    if info.get("State", {}).get("Running") is not True:
        raise ContainerVerificationError("container is not running")
    mounts = info.get("Mounts")
    if not isinstance(mounts, list):
        raise ContainerVerificationError("Docker inspect has no mount inventory")
    matches = [m for m in mounts if isinstance(m, dict) and m.get("Type") == "bind" and
               m.get("Destination") == str(workspace_path) and isinstance(m.get("Source"), str)
               and Path(m["Source"]).resolve() == project and m.get("RW") is True]
    if len(matches) != 1:
        raise ContainerVerificationError("workspace is not a writable bind mount of this real checkout")
    relevant_mounts = [mount for mount in mounts if isinstance(mount, dict) and
                       isinstance(mount.get("Destination"), str) and
                       (mount["Destination"] == str(workspace_path) or
                        mount["Destination"].startswith(str(workspace_path) + "/") or
                        str(workspace_path).startswith(mount["Destination"].rstrip("/") + "/"))]
    identity = {"container_id": info.get("Id"), "image": info.get("Image"),
                "workspace": str(workspace_path), "host_project": str(project),
                "runner": str(runner_path), "mounts": relevant_mounts, "devcontainer_config": configuration}
    if not isinstance(identity["container_id"], str) or not identity["container_id"].startswith(container_id):
        raise ContainerVerificationError("Docker inspect returned a different container")
    probe_code_text = ("import hashlib,json,sys\n"
                       "h=hashlib.sha256()\n"
                       "with open(sys.argv[1], 'rb') as stream:\n"
                       "    for block in iter(lambda: stream.read(65536), b''):\n"
                       "        h.update(block)\n"
                       "print(json.dumps({'python':sys.version.split()[0], 'runner_sha256':h.hexdigest()}))")
    probe = ["docker", "exec", "--workdir", str(workspace_path), container_id,
             "python3", "-c", probe_code_text,
             str(runner_path)]
    probe_code, probe_raw = run(probe, min(timeout, 20))
    probe_result = _json(probe_raw, "container runtime probe") if probe_code == 0 else None
    if not isinstance(probe_result, dict) or not re.fullmatch(r"[0-9a-f]{64}", str(probe_result.get("runner_sha256"))):
        raise ContainerVerificationError("runner identity probe failed")
    version = str(probe_result.get("python", ""))
    match = re.fullmatch(r"(\d+)\.(\d+)\.\d+", version)
    if not match or (int(match[1]), int(match[2])) < (3, 10):
        raise ContainerVerificationError("container Python runtime is unsupported")
    try:
        runner_relative = runner_path.relative_to(workspace_path)
    except ValueError:
        runner_relative = None
    if runner_relative is not None:
        host_runner = project.joinpath(*runner_relative.parts)
        if not host_runner.is_file() or host_runner.is_symlink():
            raise ContainerVerificationError("mapped runner is missing or linked")
        expected_runner_sha = hashlib.sha256(host_runner.read_bytes()).hexdigest()
    if expected_runner_sha is None or probe_result["runner_sha256"] != expected_runner_sha:
        raise ContainerVerificationError("container runner does not match host source or expected digest")
    identity["runtime"] = probe_result
    # The existing verifier owns its configured check process groups and receipt.
    command = ["docker", "exec", "--workdir", str(workspace_path), container_id,
               "python3", str(runner_path), "verify", "--project", str(workspace_path),
               "--output", container_output]
    try:
        code, _ = run(command, timeout)
    except ContainerVerificationError as error:
        raise ContainerVerificationError(
            f"{error}; container={container_id}; output={host_output}; container-side state unknown") from error
    if any(project.joinpath(*relative.parts[:i]).is_symlink() for i in range(1, len(relative.parts) + 1)):
        raise ContainerVerificationError("output path became linked")
    receipt = _read_receipt(host_output / "receipt.json")
    before, after = receipt.get("snapshot_before"), receipt.get("snapshot_after")
    host_after = snapshot(project)
    if (code != 0 or receipt.get("gate_status") != "passed" or
            receipt.get("schema_version") != 1 or
            receipt.get("project") != str(workspace_path) or
            not isinstance(before, dict) or not isinstance(after, dict) or
            not before.get("complete") or not after.get("complete") or
            before.get("candidate_digest") != after.get("candidate_digest") or
            not isinstance(receipt.get("selection"), dict) or
            receipt["selection"].get("not_selected") != [] or
            not isinstance(receipt.get("checks"), list) or not receipt["checks"] or
            any(not isinstance(check, dict) or check.get("result") != "passed" for check in receipt["checks"])):
        raise ContainerVerificationError("container verification gate failed, was partial, or changed candidate")
    if not (_same_candidate(host_before, before) and _same_candidate(host_after, after) and
            _same_candidate(host_before, host_after)):
        raise ContainerVerificationError("host and container candidate inventories differ or changed")
    # Reuse the verifier's candidate/config freshness contract after reading the receipt.
    fresh_command = ["docker", "exec", "--workdir", str(workspace_path), container_id,
                     "python3", str(runner_path), "freshness", "--project", str(workspace_path),
                     container_output + "/receipt.json"]
    try:
        fresh_code, fresh_raw = run(fresh_command, min(timeout, 120))
    except ContainerVerificationError as error:
        raise ContainerVerificationError(
            f"{error}; container={container_id}; output={host_output}; freshness state unknown") from error
    freshness = _json(fresh_raw, "container freshness")
    if fresh_code or not isinstance(freshness, dict) or freshness.get("fresh") is not True:
        raise ContainerVerificationError("container receipt is stale or freshness could not be established")
    if not _same_candidate(snapshot(project), after) or _config(project) != configuration:
        raise ContainerVerificationError("host candidate or devcontainer configuration changed after freshness")
    return {"status": "passed", "environment": identity, "receipt_path": str(host_output / "receipt.json"),
            "candidate_digest": after["candidate_digest"], "check_count": len(receipt["checks"]),
            "limitation": "container proof does not establish native host activation or platform-specific behavior"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--container", required=True)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--runner", required=True, help="Existing container-side path to alarina.py")
    parser.add_argument("--expected-runner-sha", help="Required SHA-256 when runner is outside the workspace mount")
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args(argv)
    try:
        result = verify_existing(args.container, args.project, args.workspace, args.runner,
                                 expected_runner_sha=args.expected_runner_sha, timeout=args.timeout)
    except (ContainerVerificationError, OSError, UnicodeError) as error:
        print(json.dumps({"status": "blocked", "reason": str(error)}))
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

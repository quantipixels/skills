#!/usr/bin/env python3
"""Create a read-only, exact snapshot of an uncommitted Git candidate."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
from typing import Any


class SnapshotError(RuntimeError):
    pass


class SnapshotDrift(SnapshotError):
    pass


def run(command: list[str], *, cwd: Path | None = None) -> bytes:
    environment = dict(os.environ)
    for name in (
        "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
        "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE",
        "GIT_PREFIX",
    ):
        environment.pop(name, None)
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    environment["LC_ALL"] = "C"
    result = subprocess.run(
        command, cwd=cwd, check=False, capture_output=True, env=environment
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", "replace").strip()
        raise SnapshotError(message or f"command failed ({result.returncode}): {' '.join(command)}")
    return result.stdout


def git(repo: Path, *args: str) -> bytes:
    return run([
        "git", "--no-optional-locks", "-c", "core.fsmonitor=false",
        "-C", str(repo), *args,
    ])


def decode(value: bytes) -> str:
    return value.decode("utf-8", "surrogateescape")


def resolve_repository(raw_repo: str) -> Path:
    supplied = Path(raw_repo).expanduser().resolve()
    root = Path(decode(run([
        "git", "--no-optional-locks", "-c", "core.fsmonitor=false",
        "-C", str(supplied), "rev-parse", "--show-toplevel",
    ])).strip())
    if decode(git(root, "rev-parse", "--is-inside-work-tree")).strip() != "true":
        raise SnapshotError(f"not a Git worktree: {root}")
    return root


def resolve_commit(repo: Path, revision: str) -> str:
    return decode(git(repo, "rev-parse", "--verify", f"{revision}^{{commit}}")).strip()


def status_bytes(repo: Path) -> bytes:
    return git(repo, "status", "--porcelain=v2", "-z", "--untracked-files=all")


def parse_status(raw: bytes) -> list[dict[str, Any]]:
    fields = raw.split(b"\0")
    records: list[dict[str, Any]] = []
    index = 0
    while index < len(fields):
        record = fields[index]
        index += 1
        if not record:
            continue
        kind = record[:1]
        if kind == b"1":
            parts = record.split(b" ", 8)
            if len(parts) != 9:
                raise SnapshotError("could not parse ordinary Git status record")
            xy = decode(parts[1])
            records.append({
                "path": decode(parts[8]),
                "original_path": None,
                "status": {
                    "record": "ordinary", "index": xy[0], "worktree": xy[1],
                    "submodule": decode(parts[2]), "head_mode": decode(parts[3]),
                    "index_mode": decode(parts[4]), "worktree_mode": decode(parts[5]),
                    "head_oid": decode(parts[6]), "index_oid": decode(parts[7]),
                },
            })
        elif kind == b"2":
            parts = record.split(b" ", 9)
            if len(parts) != 10 or index >= len(fields):
                raise SnapshotError("could not parse renamed or copied Git status record")
            original_path = decode(fields[index])
            index += 1
            xy = decode(parts[1])
            records.append({
                "path": decode(parts[9]),
                "original_path": original_path,
                "status": {
                    "record": "renamed_or_copied", "index": xy[0], "worktree": xy[1],
                    "submodule": decode(parts[2]), "head_mode": decode(parts[3]),
                    "index_mode": decode(parts[4]), "worktree_mode": decode(parts[5]),
                    "head_oid": decode(parts[6]), "index_oid": decode(parts[7]),
                    "score": decode(parts[8]),
                },
            })
        elif kind == b"u":
            parts = record.split(b" ", 10)
            if len(parts) != 11:
                raise SnapshotError("could not parse unmerged Git status record")
            xy = decode(parts[1])
            records.append({
                "path": decode(parts[10]),
                "original_path": None,
                "status": {
                    "record": "unmerged", "index": xy[0], "worktree": xy[1],
                    "submodule": decode(parts[2]), "stage1_mode": decode(parts[3]),
                    "stage2_mode": decode(parts[4]), "stage3_mode": decode(parts[5]),
                    "worktree_mode": decode(parts[6]), "stage1_oid": decode(parts[7]),
                    "stage2_oid": decode(parts[8]), "stage3_oid": decode(parts[9]),
                },
            })
        elif kind == b"?":
            records.append({
                "path": decode(record[2:]), "original_path": None,
                "status": {"record": "untracked", "index": "?", "worktree": "?"},
            })
        elif kind == b"!":
            continue
        else:
            raise SnapshotError(f"unsupported Git status record: {decode(record[:40])}")

    for record in records:
        status = record["status"]
        status["staged"] = status["index"] not in {".", "?"}
        status["unstaged"] = status["worktree"] not in {".", "?"}
        status["untracked"] = status["record"] == "untracked"
        status["conflicted"] = status["record"] == "unmerged" or "U" in (
            status["index"] + status["worktree"]
        )
    return sorted(records, key=lambda item: item["path"])


def normalize_selection(repo: Path, raw_path: str) -> str:
    if not raw_path.strip():
        raise SnapshotError("selected path cannot be empty")
    supplied = Path(raw_path).expanduser()
    if supplied.is_absolute():
        try:
            supplied = supplied.relative_to(repo)
        except ValueError as error:
            raise SnapshotError(f"selected path is outside the repository: {raw_path}") from error
    normalized = os.path.normpath(str(supplied)).replace(os.sep, "/")
    if normalized == ".":
        raise SnapshotError("use --all-changes instead of selecting the repository root")
    if normalized == ".." or normalized.startswith("../"):
        raise SnapshotError(f"selected path escapes the repository: {raw_path}")
    return normalized.removeprefix("./")


def path_matches(path: str | None, selection: str) -> bool:
    if path is None:
        return False
    return selection == "." or path == selection or path.startswith(selection.rstrip("/") + "/")


def index_entries(repo: Path, path: str) -> list[dict[str, Any]]:
    raw = git(repo, "ls-files", "--stage", "-z", "--", path)
    entries: list[dict[str, Any]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, separator, entry_path = record.partition(b"\t")
        parts = metadata.split(b" ")
        if not separator or len(parts) != 3:
            raise SnapshotError(f"could not parse index entry for {path}")
        entries.append({
            "mode": decode(parts[0]), "oid": decode(parts[1]),
            "stage": int(parts[2]), "path": decode(entry_path),
        })
    return entries


def stat_fingerprint(info: os.stat_result) -> tuple[int, int, int, int, int]:
    return (info.st_dev, info.st_ino, info.st_mode, info.st_size, info.st_mtime_ns)


def hash_regular_file(path: Path, before: os.stat_result) -> str:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        if stat_fingerprint(opened) != stat_fingerprint(before):
            raise SnapshotDrift(f"file changed while snapshot started: {path}")
        digest = hashlib.sha256()
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
        after = os.fstat(descriptor)
        if stat_fingerprint(after) != stat_fingerprint(opened):
            raise SnapshotDrift(f"file changed while hashing: {path}")
        return digest.hexdigest()
    finally:
        os.close(descriptor)


def describe_present_path(
    repo: Path, relative_path: str
) -> tuple[dict[str, Any], list[str], dict[str, Any]]:
    path = repo / relative_path
    before = path.lstat()
    limitations: list[str] = []
    description: dict[str, Any] = {
        "mode": format(stat.S_IMODE(before.st_mode), "04o"),
        "size": before.st_size,
    }
    guard: dict[str, Any] = {
        "path": relative_path, "present": True,
        "fingerprint": stat_fingerprint(before), "symlink_target": None,
    }
    if stat.S_ISREG(before.st_mode):
        description.update({"type": "file", "sha256": hash_regular_file(path, before)})
    elif stat.S_ISLNK(before.st_mode):
        target = os.readlink(path)
        after = path.lstat()
        if stat_fingerprint(after) != stat_fingerprint(before) or os.readlink(path) != target:
            raise SnapshotDrift(f"symbolic link changed while hashing: {relative_path}")
        description.update({
            "type": "symlink", "target": target,
            "sha256": hashlib.sha256(os.fsencode(target)).hexdigest(),
        })
        guard["symlink_target"] = target
    elif stat.S_ISDIR(before.st_mode):
        description.update({"type": "directory", "sha256": None})
        try:
            description["git_head"] = decode(run([
                "git", "--no-optional-locks", "-c", "core.fsmonitor=false",
                "-C", str(path), "rev-parse", "HEAD",
            ])).strip()
        except SnapshotError:
            description["git_head"] = None
        limitations.append(f"directory content was not hashed: {relative_path}")
    else:
        description.update({"type": "special", "sha256": None})
        limitations.append(f"special-file content was not hashed: {relative_path}")
    return description, limitations, guard


def enrich_record(repo: Path, record: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    enriched = dict(record)
    path = record["path"]
    present = os.path.lexists(repo / path)
    enriched["present"] = present
    enriched["deleted"] = not present
    enriched["index_entries"] = index_entries(repo, path)
    limitations: list[str] = []
    if present:
        enriched["content"], limitations, enriched["_guard"] = describe_present_path(repo, path)
    else:
        enriched["content"] = None
        enriched["_guard"] = {"path": path, "present": False}
    original_path = record.get("original_path")
    if original_path is not None:
        enriched["original_path_deleted"] = not os.path.lexists(repo / original_path)
    return enriched, limitations


def verify_and_remove_guard(repo: Path, record: dict[str, Any]) -> None:
    guard = record.pop("_guard")
    path = repo / guard["path"]
    if not guard["present"]:
        if os.path.lexists(path):
            raise SnapshotDrift(f"deleted path reappeared during snapshot: {guard['path']}")
        return
    try:
        current = path.lstat()
    except FileNotFoundError as error:
        raise SnapshotDrift(f"path disappeared during snapshot: {guard['path']}") from error
    if stat_fingerprint(current) != guard["fingerprint"]:
        raise SnapshotDrift(f"path changed after hashing: {guard['path']}")
    if guard["symlink_target"] is not None and os.readlink(path) != guard["symlink_target"]:
        raise SnapshotDrift(f"symbolic link changed after hashing: {guard['path']}")


def candidate_digest(base_oid: str, head_oid: str, records: list[dict[str, Any]]) -> str:
    material = {"base_oid": base_oid, "head_oid": head_oid, "paths": records}
    encoded = json.dumps(
        material, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8", "surrogatepass")
    return hashlib.sha256(encoded).hexdigest()


def build_snapshot(args: argparse.Namespace) -> dict[str, Any]:
    repo = resolve_repository(args.repo)
    base_oid = resolve_commit(repo, args.base)
    head_before = resolve_commit(repo, "HEAD")
    status_before = status_bytes(repo)
    records = parse_status(status_before)
    if not records:
        raise SnapshotError("worktree has no changed paths")

    requested = [] if args.all_changes else list(dict.fromkeys(
        normalize_selection(repo, item) for item in args.path
    ))
    selected: list[dict[str, Any]] = []
    ambient: list[dict[str, Any]] = []
    matched = {item: False for item in requested}
    for record in records:
        is_selected = args.all_changes
        for selection in requested:
            if path_matches(record["path"], selection) or path_matches(record.get("original_path"), selection):
                matched[selection] = True
                is_selected = True
        (selected if is_selected else ambient).append(record)
    unmatched = [path for path, did_match in matched.items() if not did_match]
    if unmatched:
        raise SnapshotError("selected path has no current change: " + ", ".join(unmatched))
    if not selected:
        raise SnapshotError("selection produced no candidate paths")

    limitations: list[str] = []
    enriched_selected: list[dict[str, Any]] = []
    enriched_ambient: list[dict[str, Any]] = []
    for partition, destination in ((selected, enriched_selected), (ambient, enriched_ambient)):
        for record in partition:
            enriched, record_limitations = enrich_record(repo, record)
            destination.append(enriched)
            limitations.extend(record_limitations)

    status_after = status_bytes(repo)
    head_after = resolve_commit(repo, "HEAD")
    if status_after != status_before or head_after != head_before:
        raise SnapshotDrift("repository changed while the candidate snapshot was created")
    for record in (*enriched_selected, *enriched_ambient):
        verify_and_remove_guard(repo, record)

    digest = candidate_digest(base_oid, head_before, enriched_selected)
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository_root": str(repo),
        "base": {"revision": args.base, "oid": base_oid},
        "head_oid": head_before,
        "selection": {
            "mode": "all_changes" if args.all_changes else "explicit_paths",
            "requested_paths": requested,
        },
        "candidate_digest_sha256": digest,
        "selected_paths": enriched_selected,
        "ambient_paths": enriched_ambient,
        "complete": not limitations,
        "limitations": sorted(set(limitations)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Path inside the target Git worktree")
    parser.add_argument("--base", default="HEAD", help="Base commit or revision; default: HEAD")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--path", action="append", help="Intended file or directory; repeat as needed")
    selection.add_argument("--all-changes", action="store_true", help="Treat every changed path as intended")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        snapshot = build_snapshot(args)
    except SnapshotError as error:
        print(json.dumps({"complete": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(snapshot, ensure_ascii=False, indent=2))
    return 0 if snapshot["complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

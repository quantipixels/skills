#!/usr/bin/env python3
"""Fingerprint one exact selected uncommitted Git candidate."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any


class SnapshotError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--path", action="append", default=[], dest="paths")
    parser.add_argument("--all-changes", action="store_true")
    args = parser.parse_args()
    if args.all_changes == bool(args.paths):
        parser.error("choose --all-changes or one or more --path values")
    return args


def run(repo: Path, *args: str) -> bytes:
    environment = dict(os.environ)
    for name in (
        "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
        "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE", "GIT_PREFIX",
    ):
        environment.pop(name, None)
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    environment["LC_ALL"] = "C"
    result = subprocess.run(
        ["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        env=environment,
    )
    if result.returncode != 0:
        raise SnapshotError(result.stderr.decode("utf-8", "replace").strip() or "git command failed")
    return result.stdout


def repository_root(raw: Path) -> Path:
    supplied = raw.expanduser().resolve()
    return Path(run(supplied, "rev-parse", "--show-toplevel").decode().strip()).resolve()


def nul_paths(raw: bytes) -> list[str]:
    return sorted(value.decode("utf-8", "surrogateescape") for value in raw.split(b"\0") if value)


def normalize_selection(repo: Path, raw: str) -> str:
    supplied = Path(raw).expanduser()
    if supplied.is_absolute():
        try:
            supplied = supplied.resolve().relative_to(repo)
        except ValueError as error:
            raise SnapshotError(f"selected path is outside repository: {raw}") from error
    normalized = os.path.normpath(str(supplied)).replace(os.sep, "/")
    if normalized in {"", "."} or normalized == ".." or normalized.startswith("../"):
        raise SnapshotError(f"invalid selected path: {raw}")
    return normalized.removeprefix("./")


def matches(path: str, selection: str) -> bool:
    return path == selection or path.startswith(selection.rstrip("/") + "/")


def changed_paths(repo: Path) -> tuple[list[str], list[str], list[str]]:
    tracked = nul_paths(run(repo, "diff", "--name-only", "-z", "HEAD", "--"))
    untracked = nul_paths(run(repo, "ls-files", "--others", "--exclude-standard", "-z"))
    conflicts = nul_paths(run(repo, "diff", "--name-only", "--diff-filter=U", "-z", "--"))
    return tracked, untracked, conflicts


def file_digest(path: Path) -> tuple[str, str, int]:
    before = path.lstat()
    if stat.S_ISLNK(before.st_mode):
        target = os.readlink(path)
        after = path.lstat()
        if before.st_mtime_ns != after.st_mtime_ns or os.readlink(path) != target:
            raise SnapshotError(f"symlink changed during snapshot: {path}")
        return "symlink", hashlib.sha256(os.fsencode(target)).hexdigest(), len(os.fsencode(target))
    if not stat.S_ISREG(before.st_mode):
        raise SnapshotError(f"selected untracked path is not a regular file or symlink: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    after = path.lstat()
    if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
        raise SnapshotError(f"file changed during snapshot: {path}")
    return "file", digest.hexdigest(), after.st_size


def status_fingerprint(repo: Path) -> bytes:
    return run(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all")


def snapshot(repo: Path, selections: list[str] | None) -> dict[str, Any]:
    before_status = status_fingerprint(repo)
    head = run(repo, "rev-parse", "HEAD").decode().strip()
    tracked, untracked, conflicts = changed_paths(repo)
    all_paths = sorted(set(tracked + untracked))

    if selections is None:
        selected = all_paths
    else:
        selected = sorted(path for path in all_paths if any(matches(path, item) for item in selections))
        missing = [item for item in selections if not any(matches(path, item) for path in all_paths)]
        if missing:
            raise SnapshotError(f"selected path has no uncommitted change: {', '.join(missing)}")
    ambient = sorted(set(all_paths) - set(selected))
    selected_tracked = [path for path in tracked if path in selected]
    selected_untracked = [path for path in untracked if path in selected]

    diff = run(repo, "diff", "--binary", "HEAD", "--", *selected_tracked) if selected_tracked else b""
    untracked_rows = []
    for relative in selected_untracked:
        kind, sha256, size = file_digest(repo / relative)
        untracked_rows.append({"path": relative, "type": kind, "sha256": sha256, "size": size})

    material = {
        "head": head,
        "selected_paths": selected,
        "tracked_diff_sha256": hashlib.sha256(diff).hexdigest(),
        "untracked_files": untracked_rows,
    }
    candidate_digest = hashlib.sha256(
        json.dumps(material, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    after_status = status_fingerprint(repo)
    if before_status != after_status:
        raise SnapshotError("worktree changed during snapshot")

    return {
        "repository": str(repo),
        "head": head,
        "selected_paths": selected,
        "ambient_paths": ambient,
        "tracked_diff_sha256": material["tracked_diff_sha256"],
        "untracked_files": untracked_rows,
        "candidate_digest": candidate_digest,
        "conflicts": sorted(path for path in conflicts if path in selected),
        "limitations": [],
    }


def main() -> int:
    args = parse_args()
    try:
        repo = repository_root(args.repo)
        selections = None if args.all_changes else [normalize_selection(repo, value) for value in args.paths]
        result = snapshot(repo, selections)
    except (OSError, SnapshotError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

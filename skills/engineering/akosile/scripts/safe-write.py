#!/usr/bin/env python3
"""Snapshot exact target bytes or publish exact validated candidate bytes with CAS."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import tempfile
from pathlib import Path
from typing import Any

from filelock import FileLock, Timeout

ABSENT = "absent"
DIGEST = re.compile(r"^[0-9a-f]{64}$")


class Failure(Exception):
    def __init__(self, code: str, message: str, **details: Any) -> None:
        super().__init__(message)
        self.code, self.message, self.details = code, message, details

    def payload(self) -> dict[str, Any]:
        value: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.details:
            value["details"] = self.details
        return value


def absolute(path: Path) -> Path:
    return Path(os.path.abspath(path.expanduser()))


def root_dir(path: Path) -> Path:
    raw = absolute(path)
    if raw.is_symlink() or not raw.is_dir():
        raise Failure("INVALID_ROOT", "Root must be an existing real directory", path=str(raw))
    return raw.resolve()


def contained_target(root: Path, supplied: Path) -> tuple[Path, Path]:
    root = root_dir(root)
    target = absolute(supplied if supplied.is_absolute() else root / supplied)
    try:
        relative = target.relative_to(root)
    except ValueError as error:
        raise Failure("TARGET_OUTSIDE_ROOT", "Target is outside the supplied root") from error
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise Failure("SYMLINK_PATH", "Target path cannot traverse symbolic links", path=str(current))
    if not target.parent.is_dir():
        raise Failure("INVALID_TARGET_PARENT", "Target parent must already exist", path=str(target.parent))
    return root, target


def outside_path(root: Path, supplied: Path, label: str, *, must_exist: bool) -> Path:
    raw = absolute(supplied)
    if raw.is_symlink():
        raise Failure(f"INVALID_{label}", f"{label.title()} cannot be a symbolic link")
    parent = raw.parent
    if parent.is_symlink() or not parent.is_dir():
        raise Failure(f"INVALID_{label}_PARENT", f"{label.title()} parent must be an existing real directory")
    resolved = parent.resolve() / raw.name
    try:
        resolved.relative_to(root)
    except ValueError:
        pass
    else:
        raise Failure(f"{label}_INSIDE_ROOT", f"{label.title()} must be outside the root")
    if must_exist and not resolved.is_file():
        raise Failure(f"INVALID_{label}", f"{label.title()} must be a regular file")
    return resolved


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def atomic_replace(path: Path, content: bytes, mode: int = 0o600) -> None:
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        if hasattr(os, "fchmod"):
            os.fchmod(descriptor, mode & 0o777)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def snapshot(root: Path, target: Path, output: Path) -> dict[str, Any]:
    root, target = contained_target(root, target)
    output = outside_path(root, output, "SNAPSHOT", must_exist=False)
    if not target.exists():
        output.unlink(missing_ok=True)
        return {"target": str(target), "snapshot": None, "digest": ABSENT, "bytes": 0}
    if target.is_symlink() or not target.is_file():
        raise Failure("NOT_A_FILE", "Target must be a regular non-symlink file")
    content = target.read_bytes()
    digest = sha256(content)
    atomic_replace(output, content)
    if sha256(output.read_bytes()) != digest:
        raise Failure("SNAPSHOT_MISMATCH", "Snapshot does not match target bytes")
    return {"target": str(target), "snapshot": str(output), "digest": digest, "bytes": len(content)}


def read_candidate(root: Path, candidate: Path, expected: str) -> tuple[bytes, int, str]:
    if not DIGEST.fullmatch(expected):
        raise Failure("INVALID_CANDIDATE_DIGEST", "Expected candidate digest must be SHA-256")
    candidate = outside_path(root, candidate, "CANDIDATE", must_exist=True)
    before = candidate.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise Failure("INVALID_CANDIDATE", "Candidate must be a regular file")
    with candidate.open("rb") as handle:
        content = handle.read()
        opened = os.fstat(handle.fileno())
    after = candidate.lstat()
    before_id = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
    after_id = (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
    open_id = (opened.st_dev, opened.st_ino, opened.st_size, opened.st_mtime_ns)
    if before_id != after_id or before_id != open_id:
        raise Failure("CANDIDATE_CHANGED", "Candidate changed while being read")
    actual = sha256(content)
    if actual != expected:
        raise Failure("CANDIDATE_CHANGED", "Candidate no longer matches validated bytes", expected=expected, actual=actual)
    return content, before.st_mode, actual


def publish(root: Path, target: Path, candidate: Path, expected_target: str, expected_candidate: str, timeout: float) -> dict[str, Any]:
    if expected_target != ABSENT and not DIGEST.fullmatch(expected_target):
        raise Failure("INVALID_TARGET_DIGEST", "Expected target digest must be 'absent' or SHA-256")
    root, target = contained_target(root, target)
    content, candidate_mode, candidate_digest = read_candidate(root, candidate, expected_candidate)
    lock = target.parent / f".{target.name}.lock"
    if lock.is_symlink():
        raise Failure("SYMLINK_LOCK", "Target lock cannot be a symbolic link")
    try:
        with FileLock(str(lock), timeout=timeout):
            _, target = contained_target(root, target)
            if target.exists() and (target.is_symlink() or not target.is_file()):
                raise Failure("NOT_A_FILE", "Target must be a regular non-symlink file")
            current = target.read_bytes() if target.exists() else None
            actual_target = sha256(current) if current is not None else ABSENT
            if actual_target != expected_target:
                raise Failure("STALE_TARGET", "Target changed since snapshot", expected=expected_target, actual=actual_target)
            mode = target.stat().st_mode if target.exists() else candidate_mode
            atomic_replace(target, content, mode)
            readback = target.read_bytes()
            if sha256(readback) != candidate_digest or readback != content:
                raise Failure("READBACK_MISMATCH", "Written target does not match validated candidate bytes")
    except Timeout as error:
        raise Failure("LOCK_TIMEOUT", "Timed out waiting for target lock") from error
    return {"target": str(target), "previous_digest": actual_target, "digest": candidate_digest, "bytes": len(content)}


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    snap = commands.add_parser("snapshot")
    snap.add_argument("--root", type=Path, required=True)
    snap.add_argument("--target", type=Path, required=True)
    snap.add_argument("--output", type=Path, required=True)
    write = commands.add_parser("write")
    write.add_argument("--root", type=Path, required=True)
    write.add_argument("--target", type=Path, required=True)
    write.add_argument("--candidate", type=Path, required=True)
    write.add_argument("--expected-target", required=True)
    write.add_argument("--expected-candidate", required=True)
    write.add_argument("--timeout", type=float, default=30.0)
    return parser


def main() -> None:
    args = make_parser().parse_args()
    try:
        result = snapshot(args.root, args.target, args.output) if args.command == "snapshot" else publish(
            args.root, args.target, args.candidate, args.expected_target, args.expected_candidate, args.timeout
        )
    except (Failure, OSError) as error:
        payload = error.payload() if isinstance(error, Failure) else {"code": "IO_ERROR", "message": str(error)}
        print(json.dumps({"ok": False, "error": payload}, ensure_ascii=False))
        raise SystemExit(2) from error
    print(json.dumps({"ok": True, "result": result}, ensure_ascii=False))


if __name__ == "__main__":
    main()

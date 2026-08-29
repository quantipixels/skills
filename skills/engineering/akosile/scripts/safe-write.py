#!/usr/bin/env python3
"""Publish exact validated candidate bytes with target compare-and-swap semantics."""
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


def real_root(path: Path) -> Path:
    raw = absolute(path)
    if raw.is_symlink() or not raw.is_dir():
        raise Failure("INVALID_ROOT", "Root must be an existing real directory", path=str(raw))
    return raw.resolve()


def target_path(root: Path, supplied: Path) -> tuple[Path, Path]:
    root = real_root(root)
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


def candidate_path(root: Path, supplied: Path) -> Path:
    raw = absolute(supplied)
    if raw.is_symlink():
        raise Failure("INVALID_CANDIDATE", "Candidate cannot be a symbolic link")
    if raw.parent.is_symlink() or not raw.parent.is_dir():
        raise Failure("INVALID_CANDIDATE_PARENT", "Candidate parent must be an existing real directory")
    resolved = raw.parent.resolve() / raw.name
    try:
        resolved.relative_to(root)
    except ValueError:
        pass
    else:
        raise Failure("CANDIDATE_INSIDE_ROOT", "Candidate must be outside the root")
    if not resolved.is_file():
        raise Failure("INVALID_CANDIDATE", "Candidate must be a regular file")
    return resolved


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def validated_candidate(root: Path, candidate: Path, expected: str) -> tuple[bytes, int, str]:
    if not DIGEST.fullmatch(expected):
        raise Failure("INVALID_CANDIDATE_DIGEST", "Expected candidate digest must be SHA-256")

    candidate = candidate_path(root, candidate)
    before = candidate.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise Failure("INVALID_CANDIDATE", "Candidate must be a regular file")

    with candidate.open("rb") as handle:
        content = handle.read()
        opened = os.fstat(handle.fileno())
    after = candidate.lstat()

    before_id = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
    open_id = (opened.st_dev, opened.st_ino, opened.st_size, opened.st_mtime_ns)
    after_id = (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
    if before_id != open_id or before_id != after_id:
        raise Failure("CANDIDATE_CHANGED", "Candidate changed while being read")

    actual = sha256(content)
    if actual != expected:
        raise Failure(
            "CANDIDATE_CHANGED",
            "Candidate no longer matches validated bytes",
            expected=expected,
            actual=actual,
        )
    return content, before.st_mode, actual


def atomic_replace(path: Path, content: bytes, mode: int) -> None:
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        if hasattr(os, "fchmod"):
            os.fchmod(descriptor, mode & 0o777)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def publish(
    root: Path,
    target: Path,
    candidate: Path,
    expected_target: str,
    expected_candidate: str,
    timeout: float,
) -> dict[str, Any]:
    if expected_target != ABSENT and not DIGEST.fullmatch(expected_target):
        raise Failure("INVALID_TARGET_DIGEST", "Expected target digest must be 'absent' or SHA-256")

    root, target = target_path(root, target)
    content, candidate_mode, candidate_digest = validated_candidate(root, candidate, expected_candidate)
    lock = target.parent / f".{target.name}.lock"
    if lock.is_symlink():
        raise Failure("SYMLINK_LOCK", "Target lock cannot be a symbolic link")

    try:
        with FileLock(str(lock), timeout=timeout):
            _, target = target_path(root, target)
            if target.exists() and (target.is_symlink() or not target.is_file()):
                raise Failure("NOT_A_FILE", "Target must be a regular non-symlink file")

            current = target.read_bytes() if target.exists() else None
            actual_target = sha256(current) if current is not None else ABSENT
            if actual_target != expected_target:
                raise Failure(
                    "STALE_TARGET",
                    "Target changed since its expected digest was captured",
                    expected=expected_target,
                    actual=actual_target,
                )

            mode = target.stat().st_mode if target.exists() else candidate_mode
            atomic_replace(target, content, mode)
            readback = target.read_bytes()
            if readback != content or sha256(readback) != candidate_digest:
                raise Failure("READBACK_MISMATCH", "Written target does not match validated candidate bytes")
    except Timeout as error:
        raise Failure("LOCK_TIMEOUT", "Timed out waiting for target lock") from error

    return {
        "target": str(target),
        "previous_digest": actual_target,
        "digest": candidate_digest,
        "bytes": len(content),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--expected-target", required=True)
    parser.add_argument("--expected-candidate", required=True)
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()

    try:
        result = publish(
            args.root,
            args.target,
            args.candidate,
            args.expected_target,
            args.expected_candidate,
            args.timeout,
        )
    except (Failure, OSError) as error:
        payload = error.payload() if isinstance(error, Failure) else {"code": "IO_ERROR", "message": str(error)}
        print(json.dumps({"ok": False, "error": payload}, ensure_ascii=False))
        raise SystemExit(2) from error

    print(json.dumps({"ok": True, "result": result}, ensure_ascii=False))


if __name__ == "__main__":
    main()

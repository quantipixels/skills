#!/usr/bin/env python3
"""Snapshot one exact file with its digest, or atomically replace it when that digest matches."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
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

    def as_dict(self) -> dict[str, Any]:
        value: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.details:
            value["details"] = self.details
        return value


def absolute(path: Path) -> Path:
    return Path(os.path.abspath(path.expanduser()))


def real_directory(path: Path, code: str, *, reject_symlink: bool = False) -> Path:
    raw = absolute(path)
    if not raw.is_dir() or (reject_symlink and raw.is_symlink()):
        raise Failure(code, "Path must be an existing directory", path=str(raw))
    return raw.resolve()


def target_path(root: Path, supplied: Path) -> tuple[Path, Path]:
    root = real_directory(root, "INVALID_ROOT", reject_symlink=True)
    target = absolute(supplied if supplied.is_absolute() else root / supplied)
    try:
        relative = target.relative_to(root)
    except ValueError as error:
        raise Failure("TARGET_OUTSIDE_ROOT", "Target is outside the supplied root") from error

    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise Failure(
                "SYMLINK_PATH",
                "Target path cannot traverse symbolic links",
                path=str(current),
            )
    if not target.parent.is_dir():
        raise Failure(
            "INVALID_TARGET_PARENT",
            "Target parent must be an existing directory",
            path=str(target.parent),
        )
    return root, target


def external_file(path: Path, label: str) -> Path:
    raw = absolute(path)
    parent = real_directory(raw.parent, f"INVALID_{label.upper()}_PARENT")
    if raw.is_symlink() or not raw.is_file():
        raise Failure(
            f"INVALID_{label.upper()}",
            f"{label.title()} must be a regular non-symlink file",
        )
    return parent / raw.name


def external_output(path: Path, root: Path) -> Path:
    raw = absolute(path)
    parent = real_directory(raw.parent, "INVALID_SNAPSHOT_PARENT")
    if raw.is_symlink():
        raise Failure("INVALID_SNAPSHOT", "Snapshot output cannot be a symbolic link")
    output = parent / raw.name
    try:
        output.relative_to(root)
    except ValueError:
        return output
    raise Failure("SNAPSHOT_INSIDE_ROOT", "Snapshot output must be outside the root")


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
    root, target = target_path(root, target)
    output = external_output(output, root)
    if not target.exists():
        output.unlink(missing_ok=True)
        return {"target": str(target), "snapshot": None, "digest": ABSENT, "bytes": 0}
    if not target.is_file():
        raise Failure("NOT_A_FILE", "Target must be a regular file")
    content = target.read_bytes()
    digest = sha256(content)
    atomic_replace(output, content)
    if sha256(output.read_bytes()) != digest:
        raise Failure("SNAPSHOT_MISMATCH", "Snapshot does not match the target bytes")
    return {"target": str(target), "snapshot": str(output), "digest": digest, "bytes": len(content)}


def compare_and_swap(
    root: Path, target: Path, candidate: Path, expected: str, timeout: float
) -> dict[str, Any]:
    if expected != ABSENT and not DIGEST.fullmatch(expected):
        raise Failure("INVALID_EXPECTED_DIGEST", "Expected digest must be 'absent' or SHA-256")
    root, target = target_path(root, target)
    candidate = external_file(candidate, "candidate")
    if candidate == target:
        raise Failure("CANDIDATE_IS_TARGET", "Candidate must be separate from the target")
    lock = target.parent / f".{target.name}.lock"
    if lock.is_symlink():
        raise Failure("SYMLINK_LOCK", "Target lock cannot be a symbolic link")
    try:
        with FileLock(str(lock), timeout=timeout):
            _, target = target_path(root, target)
            if target.exists() and not target.is_file():
                raise Failure("NOT_A_FILE", "Target must be a regular file")
            current = target.read_bytes() if target.exists() else None
            actual = sha256(current) if current is not None else ABSENT
            if actual != expected:
                raise Failure(
                    "STALE_TARGET",
                    "Target changed since the caller's exact snapshot",
                    expected=expected,
                    actual=actual,
                )
            content = candidate.read_bytes()
            candidate_digest = sha256(content)
            mode = target.stat().st_mode if target.exists() else candidate.stat().st_mode
            atomic_replace(target, content, mode)
            written = sha256(target.read_bytes())
            if written != candidate_digest:
                raise Failure("READBACK_MISMATCH", "Written target does not match candidate")
    except Timeout as error:
        raise Failure("LOCK_TIMEOUT", "Timed out waiting for target lock") from error
    return {
        "target": str(target),
        "previous_digest": actual,
        "digest": written,
        "bytes": len(content),
    }


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    read = commands.add_parser("snapshot")
    read.add_argument("--root", type=Path, required=True)
    read.add_argument("--target", type=Path, required=True)
    read.add_argument("--output", type=Path, required=True)
    write = commands.add_parser("write")
    write.add_argument("--root", type=Path, required=True)
    write.add_argument("--target", type=Path, required=True)
    write.add_argument("--candidate", type=Path, required=True)
    write.add_argument("--expected", required=True)
    write.add_argument("--timeout", type=float, default=30.0)
    return root


def main() -> None:
    args = parser().parse_args()
    try:
        result = (
            snapshot(args.root, args.target, args.output)
            if args.command == "snapshot"
            else compare_and_swap(args.root, args.target, args.candidate, args.expected, args.timeout)
        )
    except (Failure, OSError) as error:
        payload = error.as_dict() if isinstance(error, Failure) else {"code": "IO_ERROR", "message": str(error)}
        print(json.dumps({"ok": False, "error": payload}, indent=2, ensure_ascii=False))
        raise SystemExit(2) from error
    print(json.dumps({"ok": True, "result": result}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

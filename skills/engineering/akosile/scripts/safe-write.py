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
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")


class SafeWriteError(Exception):
    def __init__(self, code: str, message: str, **details: Any) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details

    def payload(self) -> dict[str, Any]:
        result: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.details:
            result["details"] = self.details
        return result


def hash_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def resolve_root(root: Path) -> Path:
    supplied = Path(os.path.abspath(root.expanduser()))
    if supplied.is_symlink():
        raise SafeWriteError("SYMLINK_ROOT", "Root cannot be a symbolic link", root=str(supplied))
    if not supplied.exists() or not supplied.is_dir():
        raise SafeWriteError("INVALID_ROOT", "Root must be an existing directory", root=str(supplied))
    return supplied.resolve()


def resolve_target(root: Path, target: Path) -> tuple[Path, Path]:
    resolved_root = resolve_root(root)
    supplied = target.expanduser()
    lexical = Path(os.path.abspath(supplied if supplied.is_absolute() else resolved_root / supplied))
    try:
        relative = lexical.relative_to(resolved_root)
    except ValueError as error:
        raise SafeWriteError(
            "TARGET_OUTSIDE_ROOT",
            "Target is outside the supplied root",
            root=str(resolved_root),
            target=str(lexical),
        ) from error

    current = resolved_root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise SafeWriteError(
                "SYMLINK_PATH", "Target path cannot traverse symbolic links", path=str(current)
            )
    if not lexical.parent.exists() or not lexical.parent.is_dir():
        raise SafeWriteError(
            "PARENT_MISSING",
            "Target parent must already exist; create workspace paths with native filesystem tools",
            parent=str(lexical.parent),
        )
    return resolved_root, lexical


def resolve_input(path: Path, *, label: str) -> Path:
    lexical = Path(os.path.abspath(path.expanduser()))
    if lexical.is_symlink() or not lexical.is_file():
        raise SafeWriteError(
            f"INVALID_{label.upper()}", f"{label.title()} must be a regular non-symlink file"
        )
    return lexical.resolve()


def resolve_output(path: Path) -> Path:
    lexical = Path(os.path.abspath(path.expanduser()))
    if lexical.is_symlink():
        raise SafeWriteError("INVALID_SNAPSHOT", "Snapshot output cannot be a symbolic link")
    if not lexical.parent.exists() or not lexical.parent.is_dir():
        raise SafeWriteError("SNAPSHOT_PARENT_MISSING", "Snapshot output parent must already exist")
    return lexical


def validate_expected(value: str) -> str:
    if value == ABSENT or DIGEST_RE.fullmatch(value):
        return value
    raise SafeWriteError(
        "INVALID_EXPECTED_DIGEST",
        "Expected digest must be 'absent' or a lowercase SHA-256 digest",
    )


def fsync_directory(directory: Path) -> None:
    if os.name == "nt":
        return
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def atomic_replace(target: Path, content: bytes, mode: int) -> None:
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
    temporary = Path(temporary_name)
    try:
        if hasattr(os, "fchmod"):
            os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
        fsync_directory(target.parent)
    finally:
        temporary.unlink(missing_ok=True)


def target_lock(target: Path, timeout: float) -> FileLock:
    lock_path = target.parent / f".{target.name}.lock"
    if lock_path.is_symlink():
        raise SafeWriteError("SYMLINK_LOCK", "Target lock cannot be a symbolic link")
    return FileLock(str(lock_path), timeout=timeout)


def snapshot(*, root: Path, target: Path, output: Path, timeout: float = 30.0) -> dict[str, Any]:
    root, target = resolve_target(root, target)
    output = resolve_output(output)
    try:
        output.relative_to(root)
    except ValueError:
        pass
    else:
        raise SafeWriteError(
            "SNAPSHOT_INSIDE_ROOT",
            "Snapshot output must be outside the authoritative root",
        )
    if output == target:
        raise SafeWriteError("SNAPSHOT_IS_TARGET", "Snapshot output must be separate from the target")
    try:
        with target_lock(target, timeout):
            _, target = resolve_target(root, target)
            if target.is_symlink():
                raise SafeWriteError("SYMLINK_TARGET", "Target cannot be a symbolic link")
            if not target.exists():
                output.unlink(missing_ok=True)
                return {"target": str(target), "snapshot": None, "digest": ABSENT, "bytes": 0}
            if not target.is_file():
                raise SafeWriteError("NOT_A_FILE", "Target must be a regular file")
            content = target.read_bytes()
            digest = hash_bytes(content)
            atomic_replace(output, content, target.stat().st_mode & 0o777)
            if hash_bytes(output.read_bytes()) != digest:
                raise SafeWriteError("SNAPSHOT_MISMATCH", "Snapshot does not match the target bytes")
    except Timeout as error:
        raise SafeWriteError("LOCK_TIMEOUT", "Timed out waiting for the target lock") from error
    except OSError as error:
        raise SafeWriteError("IO_ERROR", "File operation failed", error=str(error)) from error
    return {"target": str(target), "snapshot": str(output), "digest": digest, "bytes": len(content)}


def compare_and_swap(
    *, root: Path, target: Path, candidate: Path, expected: str, timeout: float = 30.0
) -> dict[str, Any]:
    expected = validate_expected(expected)
    root, target = resolve_target(root, target)
    candidate = resolve_input(candidate, label="candidate")
    if candidate == target:
        raise SafeWriteError("CANDIDATE_IS_TARGET", "Candidate must be separate from the target")

    try:
        with target_lock(target, timeout):
            _, target = resolve_target(root, target)
            if target.is_symlink():
                raise SafeWriteError("SYMLINK_TARGET", "Target cannot be a symbolic link")
            if target.exists() and not target.is_file():
                raise SafeWriteError("NOT_A_FILE", "Target must be a regular file")
            current = target.read_bytes() if target.exists() else None
            actual = hash_bytes(current) if current is not None else ABSENT
            if actual != expected:
                raise SafeWriteError(
                    "STALE_TARGET",
                    "Target changed since the caller's exact snapshot",
                    expected=expected,
                    actual=actual,
                )
            content = candidate.read_bytes()
            candidate_digest = hash_bytes(content)
            mode = (target.stat().st_mode if target.exists() else candidate.stat().st_mode) & 0o777
            atomic_replace(target, content, mode)
            written_digest = hash_bytes(target.read_bytes())
            if written_digest != candidate_digest:
                raise SafeWriteError(
                    "READBACK_MISMATCH",
                    "Written target does not match the candidate",
                    candidate_digest=candidate_digest,
                    written_digest=written_digest,
                )
    except Timeout as error:
        raise SafeWriteError("LOCK_TIMEOUT", "Timed out waiting for the target lock") from error
    except OSError as error:
        raise SafeWriteError("IO_ERROR", "File operation failed", error=str(error)) from error

    return {
        "target": str(target),
        "previous_digest": actual,
        "digest": written_digest,
        "bytes": len(content),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    read = commands.add_parser("snapshot", help="Copy one locked target snapshot and return its digest")
    read.add_argument("--root", type=Path, required=True)
    read.add_argument("--target", type=Path, required=True)
    read.add_argument("--output", type=Path, required=True)
    read.add_argument("--timeout", type=float, default=30.0)

    write = commands.add_parser(
        "write", help="Atomically replace a target when its snapshot digest still matches"
    )
    write.add_argument("--root", type=Path, required=True)
    write.add_argument("--target", type=Path, required=True)
    write.add_argument("--candidate", type=Path, required=True)
    write.add_argument("--expected", required=True)
    write.add_argument("--timeout", type=float, default=30.0)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        if args.command == "snapshot":
            result = snapshot(
                root=args.root,
                target=args.target,
                output=args.output,
                timeout=args.timeout,
            )
        else:
            result = compare_and_swap(
                root=args.root,
                target=args.target,
                candidate=args.candidate,
                expected=args.expected,
                timeout=args.timeout,
            )
    except (SafeWriteError, OSError) as error:
        payload = (
            error.payload()
            if isinstance(error, SafeWriteError)
            else {"code": "IO_ERROR", "message": str(error)}
        )
        print(json.dumps({"ok": False, "error": payload}, ensure_ascii=False, indent=2))
        raise SystemExit(2) from error
    print(json.dumps({"ok": True, "result": result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

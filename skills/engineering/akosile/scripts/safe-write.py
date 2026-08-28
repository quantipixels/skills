#!/usr/bin/env python3
"""Fingerprint or atomically compare-and-swap one exact file under a supplied root."""
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


def fingerprint(path: Path) -> str:
    path = path.expanduser()
    if path.is_symlink():
        raise SafeWriteError("SYMLINK_TARGET", "Target cannot be a symbolic link", target=str(path))
    if not path.exists():
        return ABSENT
    if not path.is_file():
        raise SafeWriteError("NOT_A_FILE", "Target must be a regular file", target=str(path))
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_expected(value: str) -> str:
    if value == ABSENT or DIGEST_RE.fullmatch(value):
        return value
    raise SafeWriteError(
        "INVALID_EXPECTED_DIGEST",
        "Expected digest must be 'absent' or a lowercase SHA-256 digest",
    )


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
                "SYMLINK_PATH",
                "Target path cannot traverse symbolic links",
                path=str(current),
            )
    if not lexical.parent.exists() or not lexical.parent.is_dir():
        raise SafeWriteError(
            "PARENT_MISSING",
            "Target parent must already exist; create workspace paths with native filesystem tools",
            parent=str(lexical.parent),
        )
    return resolved_root, lexical


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


def compare_and_swap(
    *, root: Path, target: Path, candidate: Path, expected: str, timeout: float = 30.0
) -> dict[str, Any]:
    expected = validate_expected(expected)
    root, target = resolve_target(root, target)

    candidate_lexical = Path(os.path.abspath(candidate.expanduser()))
    if candidate_lexical.is_symlink():
        raise SafeWriteError(
            "INVALID_CANDIDATE",
            "Candidate must be a regular non-symlink file",
            candidate=str(candidate_lexical),
        )
    candidate = candidate_lexical.resolve()
    if not candidate.is_file():
        raise SafeWriteError(
            "INVALID_CANDIDATE",
            "Candidate must be a regular non-symlink file",
            candidate=str(candidate),
        )
    if candidate == target:
        raise SafeWriteError("CANDIDATE_IS_TARGET", "Candidate must be separate from the target")

    lock_path = target.parent / f".{target.name}.lock"
    if lock_path.is_symlink():
        raise SafeWriteError("SYMLINK_LOCK", "Target lock cannot be a symbolic link")
    try:
        with FileLock(str(lock_path), timeout=timeout):
            _, target = resolve_target(root, target)
            actual = fingerprint(target)
            if actual != expected:
                raise SafeWriteError(
                    "STALE_TARGET",
                    "Target changed since the caller's exact read",
                    expected=expected,
                    actual=actual,
                )
            content = candidate.read_bytes()
            candidate_digest = hashlib.sha256(content).hexdigest()
            mode = (target.stat().st_mode if target.exists() else candidate.stat().st_mode) & 0o777
            atomic_replace(target, content, mode)
            written_digest = fingerprint(target)
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

    digest = commands.add_parser("digest", help="Print the current SHA-256 digest or 'absent'")
    digest.add_argument("--target", type=Path, required=True)

    write = commands.add_parser(
        "write", help="Atomically replace a target when its digest still matches"
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
        if args.command == "digest":
            result: Any = {
                "target": str(args.target.expanduser().resolve(strict=False)),
                "digest": fingerprint(args.target),
            }
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

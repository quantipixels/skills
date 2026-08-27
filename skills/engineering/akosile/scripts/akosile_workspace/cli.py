from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from filelock import Timeout

from .artifacts import resolve_artifact
from .errors import WorkspaceError
from .records import read_record, resolve_record, write_record
from .workspace_state import (
    doctor,
    initialize,
    read_settings,
    rebuild_index,
    repair,
    write_settings,
)


def _json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise WorkspaceError(
            "INVALID_JSON_INPUT", "Input file must contain a UTF-8 JSON object", error=str(error)
        ) from error
    if not isinstance(value, dict):
        raise WorkspaceError("INVALID_JSON_INPUT", "Input file must contain a JSON object")
    return value


def _repo(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo", type=Path, default=Path.cwd())


def build_parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Deterministic repository-local QP workspace operations")
    commands = root.add_subparsers(dest="command", required=True)
    for name in ("init", "read-settings", "index", "doctor", "repair"):
        _repo(commands.add_parser(name))

    resolve = commands.add_parser("resolve-record")
    _repo(resolve)
    resolve.add_argument("--record-ref")
    resolve.add_argument("--owner")
    resolve.add_argument("--subject")
    resolve.add_argument("--slug")
    resolve.add_argument("--create", action="store_true")

    read = commands.add_parser("read-record")
    _repo(read)
    read.add_argument("--record-ref", required=True)

    write = commands.add_parser("write-record")
    _repo(write)
    write.add_argument("--record-ref", required=True)
    write.add_argument("--frontmatter-file", type=Path, required=True)
    write.add_argument("--body-file", type=Path, required=True)
    write.add_argument("--expected-digest", required=True)

    artifact = commands.add_parser("resolve-artifact")
    _repo(artifact)
    artifact.add_argument("--artifact-id")
    artifact.add_argument("--slug")
    artifact.add_argument("--create", action="store_true")

    settings = commands.add_parser("write-settings")
    _repo(settings)
    settings.add_argument("--candidate-file", type=Path, required=True)
    settings.add_argument("--expected-digest", required=True)
    return root


def dispatch(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "init":
        return initialize(args.repo)
    if args.command == "resolve-record":
        return resolve_record(
            args.repo,
            record_ref=args.record_ref,
            owner=args.owner,
            subject=args.subject,
            slug=args.slug,
            create=args.create,
        )
    if args.command == "read-record":
        return read_record(args.repo, args.record_ref)
    if args.command == "write-record":
        return write_record(
            args.repo,
            args.record_ref,
            _json_object(args.frontmatter_file),
            args.body_file.read_text(encoding="utf-8"),
            args.expected_digest,
        )
    if args.command == "resolve-artifact":
        return resolve_artifact(
            args.repo,
            artifact_id=args.artifact_id,
            slug=args.slug,
            create=args.create,
        )
    if args.command == "read-settings":
        return read_settings(args.repo)
    if args.command == "write-settings":
        return write_settings(
            args.repo,
            args.candidate_file.read_text(encoding="utf-8"),
            args.expected_digest,
        )
    if args.command == "index":
        return rebuild_index(args.repo)
    if args.command == "doctor":
        return doctor(args.repo)
    if args.command == "repair":
        return repair(args.repo)
    raise AssertionError(args.command)


def main() -> None:
    args = build_parser().parse_args()
    try:
        result = dispatch(args)
    except (WorkspaceError, Timeout) as error:
        payload = (
            error.payload()
            if isinstance(error, WorkspaceError)
            else {"code": "LOCK_TIMEOUT", "message": str(error)}
        )
        print(json.dumps({"ok": False, "error": payload}, ensure_ascii=False, indent=2))
        raise SystemExit(2) from error
    print(json.dumps({"ok": True, "result": result}, ensure_ascii=False, indent=2, default=str))

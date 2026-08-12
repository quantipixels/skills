#!/usr/bin/env python3
"""Read provider state and emit deterministic wo-pr JSON or JSONL actions."""

from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from github_provider import GitHubProvider
from gitlab_provider import GitLabProvider
from watch_core import (
    LeaseConflict,
    acquire_file_lease,
    acquire_lease,
    canonical_state_key,
    clear_read_errors,
    default_user_state_directory,
    evaluate_snapshot,
    load_state,
    mark_action,
    new_state,
    record_read_error,
    record_retry,
    release_file_lease,
    release_lease,
    save_state_atomic,
    validate_state_target,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Watch one GitHub PR or GitLab MR without provider writes")
    parser.add_argument("--provider", choices=("auto", "github", "gitlab"), default="auto")
    parser.add_argument("--pr", default="auto", help="PR/MR number, URL, or auto")
    parser.add_argument("--repo", help="owner/repository or group/project")
    parser.add_argument("--host", help="provider host")
    parser.add_argument("--objective", choices=("until-ready", "until-merged", "until-stopped"), default="until-ready")
    parser.add_argument("--authority", action="append", default=[], help="Granted action capability; repeat as needed")
    parser.add_argument("--state-file", type=Path)
    parser.add_argument("--once", action="store_true", help="Emit one snapshot")
    parser.add_argument("--watch", action="store_true", help="Emit JSONL until a terminal state")
    parser.add_argument("--takeover", action="store_true", help="Explicitly take over an existing watcher lease")
    parser.add_argument("--no-pipeline-expected", action="store_true")
    parser.add_argument("--max-snapshots", type=int, help="Bound a watch for diagnostics or host limits")
    parser.add_argument("--mark-action", action="append", default=[], metavar="ID=PHASE")
    parser.add_argument("--record-retry", metavar="HEAD_SHA")
    args = parser.parse_args(argv)
    state_only = bool(args.mark_action or args.record_retry)
    if state_only:
        if args.once or args.watch:
            parser.error("state updates cannot be combined with --once or --watch")
        if not args.state_file:
            parser.error("state updates require --state-file")
    elif args.once == args.watch:
        parser.error("choose exactly one of --once or --watch")
    if args.max_snapshots is not None and args.max_snapshots <= 0:
        parser.error("--max-snapshots must be positive")
    return args


def target_identity(target: str, *, provider: str) -> dict[str, str | None]:
    identity: dict[str, str | None] = {"provider": None, "host": None, "repository": None}
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        path = parsed.path.strip("/")
        if "/pull/" in f"/{path}/":
            repository = path.split("/pull/", 1)[0]
            identity.update({"provider": "github", "host": parsed.hostname, "repository": repository})
        elif "/-/merge_requests/" in f"/{path}/":
            repository = path.split("/-/merge_requests/", 1)[0]
            identity.update({"provider": "gitlab", "host": parsed.hostname, "repository": repository})
    if provider != "auto":
        if identity["provider"] and identity["provider"] != provider:
            raise ValueError(f"target URL is for {identity['provider']}, not {provider}")
        identity["provider"] = provider
    if identity["provider"]:
        return identity
    remote = subprocess.run(
        ["git", "remote", "get-url", "origin"], check=False, capture_output=True, text=True
    )
    url = remote.stdout.lower()
    if "github" in url:
        identity["provider"] = "github"
    elif "gitlab" in url:
        identity["provider"] = "gitlab"
    if identity["provider"]:
        return identity
    raise ValueError("cannot infer provider; pass --provider github or --provider gitlab")


def make_provider(args: argparse.Namespace):
    identity = target_identity(args.pr, provider=args.provider)
    provider = identity["provider"]
    host = args.host or identity["host"]
    repository = args.repo or identity["repository"]
    if provider == "github":
        return GitHubProvider(host=host or "github.com", repository=repository)
    return GitLabProvider(host=host or "gitlab.com", repository=repository)


def apply_state_updates(
    path: str | Path,
    *,
    marks: list[str],
    retry_sha: str | None,
    now: float | None = None,
) -> dict[str, Any]:
    state_path = Path(path)
    state = load_state(state_path)
    if state is None:
        raise ValueError(f"state file does not exist: {state_path}")
    timestamp = now if now is not None else time.time()
    applied = []
    for value in marks:
        try:
            action_id, phase = value.rsplit("=", 1)
        except ValueError as error:
            raise ValueError(f"invalid --mark-action {value!r}; expected ID=PHASE") from error
        if not action_id:
            raise ValueError("action ID cannot be empty")
        mark_action(state, action_id, phase, now=timestamp)
        applied.append({"id": action_id, "phase": phase})
    retry_count = record_retry(state, retry_sha) if retry_sha else None
    save_state_atomic(state_path, state)
    return {
        "schema_version": state["schema_version"],
        "state_file": str(state_path.resolve()),
        "marked_actions": applied,
        "retry_sha": retry_sha,
        "retry_count": retry_count,
    }


def _project_state_directory(cwd: Path) -> Path | None:
    top = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], cwd=cwd, check=False, capture_output=True, text=True
    )
    if top.returncode != 0:
        return None
    root = Path(top.stdout.strip())
    ignored = subprocess.run(
        ["git", "check-ignore", "-q", ".qp"], cwd=root, check=False, capture_output=True
    )
    if ignored.returncode != 0:
        return None
    qp = root / ".qp"
    probe_parent = qp if qp.exists() else root
    if not os.access(probe_parent, os.W_OK):
        return None
    return qp / "state" / "wo-pr"


def resolve_state_path(args: argparse.Namespace, snapshot: dict[str, Any]) -> Path:
    if args.state_file:
        return args.state_file.resolve()
    directory = _project_state_directory(Path.cwd()) or default_user_state_directory()
    return directory / canonical_state_key(snapshot)


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")), flush=True)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.mark_action or args.record_retry:
        try:
            emit(
                apply_state_updates(
                    args.state_file,
                    marks=args.mark_action,
                    retry_sha=args.record_retry,
                )
            )
            return 0
        except (ValueError, OSError) as error:
            emit({"terminal": True, "reason": "state_update_failed", "error": str(error)})
            return 2
    provider = make_provider(args)
    owner = f"{socket.gethostname()}:{os.getpid()}:{uuid.uuid4().hex[:8]}"
    state_path: Path | None = None
    state: dict[str, Any] | None = None
    lease_path: Path | None = None
    snapshots = 0
    try:
        while True:
            now = time.time()
            try:
                snapshot = provider.fetch(args.pr)
                clear_read_errors(state) if state else None
            except Exception as error:  # provider errors are emitted as state, not pipeline truth
                if state is None:
                    emit({"terminal": True, "reason": "initial_provider_read_failed", "error": str(error)})
                    return 2
                read_result = record_read_error(state, str(error), now=now)
                save_state_atomic(state_path, state)
                emit({"schema_version": state["schema_version"], "actions": ["provider_read_failed"], **read_result})
                if args.once or read_result["terminal"]:
                    return 2 if read_result["terminal"] else 0
                time.sleep(read_result["next_poll_seconds"])
                continue

            if state is None:
                state_path = resolve_state_path(args, snapshot)
                lease_path = state_path.with_name(f"{state_path.name}.lease")
                file_lease_state = acquire_file_lease(
                    lease_path, owner=owner, now=now, takeover=args.takeover
                )
                state = load_state(state_path) or new_state(objective=args.objective)
                validate_state_target(state, snapshot)
                if state["objective"] != args.objective:
                    raise ValueError(
                        f"state objective is {state['objective']!r}; use a new state file or the same objective"
                    )
                lease_state = acquire_lease(state, owner=owner, now=now, takeover=args.takeover)
                state["authority_observed"] = sorted(set(args.authority))
                state["lease_state"] = file_lease_state
            else:
                acquire_lease(state, owner=owner, now=now)

            result = evaluate_snapshot(
                snapshot,
                state,
                now=now,
                authority=set(args.authority),
                no_pipeline_expected=args.no_pipeline_expected,
            )
            result["state_file"] = str(state_path)
            result["lease_state"] = state.get("lease_state")
            save_state_atomic(state_path, state)
            emit(result)
            snapshots += 1
            if args.once or result["terminal"]:
                return 0
            if args.max_snapshots is not None and snapshots >= args.max_snapshots:
                return 0
            time.sleep(result["next_poll_seconds"])
    except LeaseConflict as error:
        emit({"terminal": True, "reason": "lease_conflict", "error": str(error), "state_file": str(state_path) if state_path else None})
        return 3
    except (ValueError, OSError) as error:
        emit({"terminal": True, "reason": "configuration_error", "error": str(error), "state_file": str(state_path) if state_path else None})
        return 2
    except KeyboardInterrupt:
        emit({"terminal": True, "reason": "user_interrupted", "state_file": str(state_path) if state_path else None})
        return 130
    finally:
        if state is not None and state_path is not None:
            release_lease(state, owner=owner)
            try:
                save_state_atomic(state_path, state)
            except OSError:
                pass
        if lease_path is not None:
            try:
                release_file_lease(lease_path, owner=owner)
            except (OSError, ValueError):
                pass


if __name__ == "__main__":
    raise SystemExit(main())

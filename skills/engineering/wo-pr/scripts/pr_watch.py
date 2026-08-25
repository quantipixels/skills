#!/usr/bin/env python3
"""Observe one PR or MR and keep a small recoverable checkpoint."""

from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import urlparse

from github_provider import GitHubProvider
from gitlab_provider import GitLabProvider

SCHEMA_VERSION = 2
SUCCESS = {"success", "neutral", "skipped"}
ACTIVE = {"created", "waiting", "pending", "queued", "running", "scheduled"}


class WatchConflict(RuntimeError):
    pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Observe one GitHub PR or GitLab MR without provider writes")
    parser.add_argument("--provider", choices=("auto", "github", "gitlab"), default="auto")
    parser.add_argument("--pr", default="auto", help="PR/MR number, URL, or auto")
    parser.add_argument("--repo", help="owner/repository or group/project")
    parser.add_argument("--host", help="provider host")
    parser.add_argument("--trusted-github-host", action="append", default=[])
    parser.add_argument("--trusted-gitlab-host", action="append", default=[])
    parser.add_argument("--state-file", type=Path)
    parser.add_argument("--once", action="store_true", help="Emit one complete snapshot assessment")
    parser.add_argument("--watch", action="store_true", help="Emit JSONL until closed or interrupted")
    parser.add_argument("--max-snapshots", type=int)
    parser.add_argument("--no-pipeline-expected", action="store_true")
    parser.add_argument("--record-receipt", action="append", nargs=4, default=[], metavar=("HEAD", "EVENT_ID", "FINGERPRINT", "RECEIPT"))
    parser.add_argument("--record-retry", action="append", nargs=2, default=[], metavar=("HEAD", "JOB_ID"))
    args = parser.parse_args(argv)
    state_only = bool(args.record_receipt or args.record_retry)
    if state_only:
        if args.once or args.watch:
            parser.error("checkpoint updates cannot be combined with --once or --watch")
        if not args.state_file:
            parser.error("checkpoint updates require --state-file")
    elif args.once == args.watch:
        parser.error("choose exactly one of --once or --watch")
    if args.max_snapshots is not None and args.max_snapshots <= 0:
        parser.error("--max-snapshots must be positive")
    return args


def _normalized_host(host: str) -> str:
    return host.lower().rstrip(".")


def target_identity(target: str, provider: str) -> dict[str, str | None]:
    identity: dict[str, str | None] = {"provider": None, "host": None, "repository": None}
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        path = parsed.path.strip("/")
        host = parsed.hostname
        if host and ":" in host and not host.startswith("["):
            host = f"[{host}]"
        if host and parsed.port is not None:
            host = f"{host}:{parsed.port}"
        if "/pull/" in f"/{path}/":
            identity.update(provider="github", host=host, repository=path.split("/pull/", 1)[0])
        elif "/-/merge_requests/" in f"/{path}/":
            identity.update(provider="gitlab", host=host, repository=path.split("/-/merge_requests/", 1)[0])
    if provider != "auto":
        if identity["provider"] and identity["provider"] != provider:
            raise ValueError(f"target URL is for {identity['provider']}, not {provider}")
        identity["provider"] = provider
    if identity["provider"]:
        return identity
    remote = subprocess.run(["git", "remote", "get-url", "origin"], check=False, capture_output=True, text=True)
    remote_url = remote.stdout.strip()
    parsed_remote = urlparse(remote_url if "://" in remote_url else f"ssh://{remote_url.replace(':', '/', 1)}")
    remote_host = (parsed_remote.hostname or "").lower().rstrip(".")
    if remote_host == "github.com" or remote_host.startswith("github."):
        identity["provider"] = "github"
    elif remote_host == "gitlab.com" or remote_host.startswith("gitlab."):
        identity["provider"] = "gitlab"
    if not identity["provider"]:
        raise ValueError("cannot infer provider; pass --provider github or --provider gitlab")
    return identity


def make_provider(args: argparse.Namespace):
    identity = target_identity(args.pr, args.provider)
    if identity["host"] and args.host and _normalized_host(args.host) != _normalized_host(str(identity["host"])):
        raise ValueError("--host conflicts with target URL host")
    if identity["repository"] and args.repo and args.repo.strip("/") != str(identity["repository"]).strip("/"):
        raise ValueError("--repo conflicts with target URL repository")
    host = args.host or identity["host"]
    repository = args.repo or identity["repository"]
    if identity["provider"] == "github":
        return GitHubProvider(host=host or "github.com", repository=repository, trusted_hosts=set(args.trusted_github_host))
    return GitLabProvider(host=host or "gitlab.com", repository=repository, trusted_hosts=set(args.trusted_gitlab_host))


def _state_directory(_cwd: Path) -> Path:
    base = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state"))
    return base / "qp" / "wo-pr"


def _state_key(snapshot: dict[str, Any]) -> str:
    target = snapshot_target(snapshot)
    raw = "|".join(str(target.get(key) or "") for key in ("provider", "host", "repository", "number"))
    return hashlib.sha256(raw.encode()).hexdigest()[:20] + ".json"


def snapshot_target(snapshot: dict[str, Any]) -> dict[str, Any]:
    return {
        "provider": snapshot.get("provider"),
        "host": snapshot.get("host"),
        "repository": snapshot.get("repository"),
        "number": snapshot.get("number"),
        "base_branch": (snapshot.get("base") or {}).get("branch"),
        "head_branch": (snapshot.get("head") or {}).get("branch"),
    }


@contextlib.contextmanager
def file_lock(path: Path, *, lifetime: bool = False) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("a+")
    try:
        flags = fcntl.LOCK_EX | (fcntl.LOCK_NB if lifetime else 0)
        try:
            fcntl.flock(handle.fileno(), flags)
        except BlockingIOError as error:
            raise WatchConflict(f"another watcher owns {path}") from error
        yield
    finally:
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def load_checkpoint(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    value = json.loads(path.read_text())
    if value.get("schema_version") == SCHEMA_VERSION:
        return value
    if value.get("schema_version") == 1:
        archive = path.with_name(f"{path.name}.v1-{int(time.time())}.bak")
        os.replace(path, archive)
        return None
    raise ValueError(f"unsupported checkpoint schema: {value.get('schema_version')!r}")


def save_checkpoint(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w") as handle:
            json.dump(value, handle, sort_keys=True, separators=(",", ":"))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def snapshot_fingerprint(snapshot: dict[str, Any]) -> str:
    material = {
        "state": snapshot.get("state"),
        "draft": snapshot.get("draft"),
        "mergeability": snapshot.get("mergeability"),
        "head": snapshot.get("head"),
        "review_decision": snapshot.get("review_decision"),
        "review_items": snapshot.get("review_items"),
        "pipeline": snapshot.get("pipeline"),
        "capabilities": snapshot.get("capabilities"),
        "errors": snapshot.get("errors"),
    }
    return hashlib.sha256(json.dumps(material, sort_keys=True, default=str).encode()).hexdigest()


def event_rows(snapshot: dict[str, Any], checkpoint: dict[str, Any]) -> list[dict[str, str]]:
    head = str((snapshot.get("head") or {}).get("sha") or "")
    rows = []
    for item in snapshot.get("review_items") or []:
        fingerprint = hashlib.sha256(json.dumps(item, sort_keys=True, default=str).encode()).hexdigest()
        row = {"head_sha": head, "id": str(item.get("id")), "fingerprint": fingerprint, "kind": "feedback"}
        receipt_key = f"{head}:{row['id']}:{fingerprint}"
        if receipt_key not in checkpoint.get("handled_events", {}):
            rows.append(row)
    return rows


def failed_job_ids(snapshot: dict[str, Any]) -> list[str]:
    return sorted(
        str(job.get("id"))
        for job in (snapshot.get("pipeline") or {}).get("jobs") or []
        if job.get("required", True) and str(job.get("status") or "unknown").lower() not in SUCCESS | ACTIVE
    )


def assess(snapshot: dict[str, Any], checkpoint: dict[str, Any], no_pipeline_expected: bool) -> dict[str, Any]:
    state = str(snapshot.get("state") or "").lower()
    closed = state in {"merged", "closed"} or bool(snapshot.get("merged"))
    blockers: list[str] = []
    target = snapshot_target(snapshot)
    if any(not target.get(key) for key in ("provider", "host", "repository", "number", "base_branch", "head_branch")):
        blockers.append("incomplete_target_identity")
    if not (snapshot.get("head") or {}).get("sha"):
        blockers.append("incomplete_head_identity")
    if snapshot.get("draft"):
        blockers.append("draft")
    if str(snapshot.get("mergeability") or "").lower() not in {"mergeable", "can_be_merged"}:
        blockers.append("mergeability")
    capabilities = snapshot.get("capabilities") or {}
    if not capabilities or any(value is not True for value in capabilities.values()) or snapshot.get("errors"):
        blockers.append("incomplete_provider_evidence")
    events = event_rows(snapshot, checkpoint)
    if events:
        blockers.append("published_feedback")
    pipeline = snapshot.get("pipeline") or {}
    jobs = pipeline.get("jobs") or []
    if not pipeline.get("evidence_complete", False):
        blockers.append("incomplete_pipeline_evidence")
    elif not jobs and not no_pipeline_expected:
        blockers.append("no_pipeline_evidence")
    else:
        for job in jobs:
            if not job.get("required", True):
                continue
            status = str(job.get("status") or "unknown").lower()
            if status not in SUCCESS:
                blockers.append("pipeline_active" if status in ACTIVE else "pipeline_failed")
                break
    if str(snapshot.get("review_decision") or "").upper() in {"CHANGES_REQUESTED", "REVIEW_REQUIRED"}:
        blockers.append("review_decision")
    fingerprint = snapshot_fingerprint(snapshot)
    ready = not closed and not blockers
    milestone = ready and checkpoint.get("handoff_ready_fingerprint") != fingerprint
    return {
        "terminal": closed,
        "reason": "item_closed" if closed else ("handoff_ready" if ready else "watching"),
        "handoff_ready": ready,
        "new_handoff_milestone": milestone,
        "blockers": sorted(set(blockers)),
        "events": events,
        "snapshot_fingerprint": fingerprint,
        "next_poll_seconds": 120 if ready else 30,
    }


def update_checkpoint(path: Path, receipts: list[list[str]], retries: list[list[str]]) -> dict[str, Any]:
    with file_lock(path.with_suffix(path.suffix + ".state.lock")):
        checkpoint = load_checkpoint(path)
        if checkpoint is None:
            raise ValueError("checkpoint does not exist; run one complete snapshot first")
        current_head = str(checkpoint.get("head_sha") or "")
        last_snapshot = checkpoint.get("last_snapshot") or {}
        surfaced_events = {
            (str(event.get("id")), str(event.get("fingerprint")))
            for event in last_snapshot.get("events") or []
        }
        surfaced_failed_jobs = {str(job_id) for job_id in last_snapshot.get("failed_job_ids") or []}
        for head, event_id, fingerprint, receipt in receipts:
            if head != current_head:
                raise ValueError(f"stale receipt head {head!r}; current head is {current_head!r}")
            if (event_id, fingerprint) not in surfaced_events:
                raise ValueError(f"event {event_id!r} with this fingerprint was not in the last complete snapshot")
            key = f"{head}:{event_id}:{fingerprint}"
            checkpoint.setdefault("handled_events", {})[key] = {"receipt": receipt, "recorded_at": time.time()}
        for head, job_id in retries:
            if head != current_head:
                raise ValueError(f"stale retry head {head!r}; current head is {current_head!r}")
            if job_id not in surfaced_failed_jobs:
                raise ValueError(f"failed job {job_id!r} was not in the last complete snapshot")
            key = f"{head}:{job_id}"
            count = int(checkpoint.setdefault("retries", {}).get(key, 0))
            if count >= 3:
                raise ValueError(f"retry budget exhausted for {job_id!r} on {head!r}")
            checkpoint["retries"][key] = count + 1
        save_checkpoint(path, checkpoint)
        return checkpoint


def emit(value: dict[str, Any]) -> None:
    print(json.dumps(value, sort_keys=True, separators=(",", ":")), flush=True)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.record_receipt or args.record_retry:
            checkpoint = update_checkpoint(args.state_file.resolve(), args.record_receipt, args.record_retry)
            emit({"schema_version": SCHEMA_VERSION, "state_file": str(args.state_file.resolve()), "checkpoint": checkpoint})
            return 0
        provider = make_provider(args)
        read_failures = 0
        while True:
            try:
                first = provider.fetch(args.pr)
                break
            except Exception as error:
                read_failures += 1
                emit({"terminal": False, "reason": "provider_read_failed", "error": str(error), "consecutive_failures": read_failures})
                if args.once:
                    return 2
                time.sleep(30 * (2 ** min(read_failures - 1, 2)))
        state_path = args.state_file.resolve() if args.state_file else (_state_directory(Path.cwd()) / _state_key(first))
        with file_lock(state_path.with_suffix(state_path.suffix + ".watch.lock"), lifetime=True):
            snapshots = 0
            pending = first
            while True:
                try:
                    snapshot = pending if snapshots == 0 else provider.fetch(args.pr)
                    read_failures = 0
                except Exception as error:
                    read_failures += 1
                    emit({"terminal": False, "reason": "provider_read_failed", "error": str(error), "consecutive_failures": read_failures, "state_file": str(state_path)})
                    time.sleep(30 * (2 ** min(read_failures - 1, 2)))
                    continue
                pending = None
                with file_lock(state_path.with_suffix(state_path.suffix + ".state.lock")):
                    checkpoint = load_checkpoint(state_path) or {
                        "schema_version": SCHEMA_VERSION,
                        "target": snapshot_target(snapshot),
                        "head_sha": None,
                        "handled_events": {},
                        "retries": {},
                        "last_snapshot": None,
                        "handoff_ready_fingerprint": None,
                    }
                    if checkpoint["target"] != snapshot_target(snapshot):
                        raise ValueError("checkpoint target does not match provider target")
                    head = str((snapshot.get("head") or {}).get("sha") or "")
                    if checkpoint.get("head_sha") != head:
                        checkpoint["head_sha"] = head
                        checkpoint["handled_events"] = {
                            key: value
                            for key, value in checkpoint.get("handled_events", {}).items()
                            if key.startswith(f"{head}:")
                        }
                        checkpoint["retries"] = {
                            key: value
                            for key, value in checkpoint.get("retries", {}).items()
                            if key.startswith(f"{head}:")
                        }
                        checkpoint["handoff_ready_fingerprint"] = None
                    result = assess(snapshot, checkpoint, args.no_pipeline_expected)
                    checkpoint["last_snapshot"] = {
                        "fingerprint": result["snapshot_fingerprint"],
                        "observed_at": time.time(),
                        "events": event_rows(snapshot, {"handled_events": {}}),
                        "failed_job_ids": failed_job_ids(snapshot),
                    }
                    if result["new_handoff_milestone"]:
                        checkpoint["handoff_ready_fingerprint"] = result["snapshot_fingerprint"]
                    save_checkpoint(state_path, checkpoint)
                result.update(schema_version=SCHEMA_VERSION, state_file=str(state_path), target=snapshot_target(snapshot), head_sha=checkpoint["head_sha"])
                emit(result)
                snapshots += 1
                if args.once or result["terminal"] or (args.max_snapshots and snapshots >= args.max_snapshots):
                    return 0
                time.sleep(result["next_poll_seconds"])
    except WatchConflict as error:
        emit({"terminal": True, "reason": "watch_conflict", "error": str(error)})
        return 3
    except KeyboardInterrupt:
        emit({"terminal": True, "reason": "user_interrupted"})
        return 130
    except Exception as error:
        emit({"terminal": False, "reason": "blocked", "error": str(error)})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

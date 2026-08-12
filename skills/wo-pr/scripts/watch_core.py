"""Deterministic state policy for wo-pr.

This module does not call provider APIs or perform provider writes.
"""

from __future__ import annotations

import hashlib
import json
import os
import socket
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Iterable

try:
    import fcntl
except ImportError:  # pragma: no cover - exercised on Windows only
    fcntl = None


SCHEMA_VERSION = 1
SETTLE_SECONDS = 300
MAX_RETRIES_PER_SHA = 3
LEASE_STALE_SECONDS = 300
ACTION_PHASES = {"surfaced": 1, "claimed": 2, "handled": 3}


class LeaseConflict(RuntimeError):
    """Raised when another watcher owns the canonical target."""


def new_state(*, objective: str) -> dict[str, Any]:
    if objective not in {"until-ready", "until-merged", "until-stopped"}:
        raise ValueError(f"unknown objective: {objective}")
    return {
        "schema_version": SCHEMA_VERSION,
        "objective": objective,
        "target": {},
        "current_head": None,
        "settle": {"fingerprint": None, "green_since": None, "snapshots": 0},
        "retry_counts": {},
        "actions": {},
        "lease": None,
        "read_errors": {"consecutive": 0, "last": None},
        "last_change_key": None,
        "last_heartbeat": None,
    }


def load_state(path: str | Path) -> dict[str, Any] | None:
    state_path = Path(path)
    if not state_path.exists():
        return None
    with state_path.open("r", encoding="utf-8") as handle:
        state = json.load(handle)
    if state.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"unsupported wo-pr state schema {state.get('schema_version')!r}; "
            f"expected {SCHEMA_VERSION}"
        )
    return state


def save_state_atomic(path: str | Path, state: dict[str, Any]) -> None:
    state_path = Path(path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{state_path.name}.", dir=state_path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(state, handle, sort_keys=True, separators=(",", ":"))
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, state_path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


@contextmanager
def state_file_lock(path: str | Path):
    """Serialize state reads and writes without claiming the watcher lease."""
    state_path = Path(path)
    lock_path = state_path.with_name(f".{state_path.name}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as handle:
        if fcntl is None:  # pragma: no cover - supported watcher hosts are POSIX
            raise OSError("state update locking is unavailable on this platform")
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def pipeline_summary(
    jobs: Iterable[dict[str, Any]],
    *,
    evidence_complete: bool,
    no_pipeline_expected: bool = False,
) -> dict[str, Any]:
    rows = list(jobs)
    counts: dict[str, int] = {}
    for job in rows:
        status = str(job.get("status") or "unknown").lower()
        counts[status] = counts.get(status, 0) + 1

    if not evidence_complete:
        return {"state": "incomplete", "counts": counts, "total": len(rows)}
    if not rows:
        state = "green" if no_pipeline_expected else "no_pipeline_evidence"
        return {"state": state, "counts": counts, "total": 0}

    failed = False
    incomplete = False
    pending = False
    for job in rows:
        status = str(job.get("status") or "unknown").lower()
        required = job.get("required")
        allow_failure = bool(job.get("allow_failure"))
        if required is False:
            continue
        if status in {"queued", "created", "pending", "running", "waiting", "scheduled"}:
            pending = True
        elif status == "manual":
            if required is True:
                pending = True
            elif required is None:
                incomplete = True
        elif status == "success":
            continue
        elif status in {"neutral", "skipped"}:
            if required is True:
                failed = True
            elif required is None:
                incomplete = True
        elif status in {"failure", "failed", "cancelled", "canceled", "timed_out", "action_required"}:
            if not allow_failure:
                failed = True
        else:
            incomplete = True

    if failed:
        state = "failed"
    elif incomplete:
        state = "incomplete"
    elif pending:
        state = "pending"
    else:
        state = "green"
    return {"state": state, "counts": counts, "total": len(rows)}


def _pipeline_fingerprint(snapshot: dict[str, Any]) -> str:
    jobs = []
    for job in snapshot.get("pipeline", {}).get("jobs", []):
        jobs.append(
            {
                "id": job.get("id"),
                "name": job.get("name"),
                "status": job.get("status"),
                "required": job.get("required"),
                "allow_failure": bool(job.get("allow_failure")),
            }
        )
    payload = {
        "head": snapshot.get("head", {}).get("sha"),
        "complete": bool(snapshot.get("pipeline", {}).get("evidence_complete")),
        "jobs": sorted(jobs, key=lambda row: (str(row["name"]), str(row["id"]), str(row["status"]))),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def mark_action(state: dict[str, Any], action_id: str, phase: str, *, now: float | None = None) -> None:
    if phase not in ACTION_PHASES:
        raise ValueError(f"unknown action phase: {phase}")
    previous = state.setdefault("actions", {}).get(action_id, {}).get("phase")
    if previous and ACTION_PHASES[phase] < ACTION_PHASES[previous]:
        raise ValueError(f"cannot move action {action_id!r} from {previous} to {phase}")
    previous_action = state["actions"].get(action_id, {})
    state["actions"][action_id] = {
        **previous_action,
        "phase": phase,
        "updated_at": now if now is not None else time.time(),
    }


def record_retry(state: dict[str, Any], head_sha: str) -> int:
    retries = state.setdefault("retry_counts", {})
    retries[head_sha] = int(retries.get(head_sha, 0)) + 1
    return retries[head_sha]


def _review_action(snapshot: dict[str, Any], state: dict[str, Any], *, now: float) -> tuple[list[str], list[str]]:
    pending_ids = []
    for item in snapshot.get("review_items", []):
        item_id = str(item.get("id") or "")
        if not item_id:
            continue
        fingerprint = _review_fingerprint(item)
        action = state.setdefault("actions", {}).get(item_id, {})
        phase = action.get("phase")
        if phase == "handled" and action.get("fingerprint") is None:
            action["fingerprint"] = fingerprint
        elif phase == "handled" and action.get("fingerprint") != fingerprint:
            phase = None
        if phase != "handled":
            pending_ids.append(item_id)
            if phase is None:
                state["actions"][item_id] = {
                    "phase": "surfaced", "updated_at": now, "fingerprint": fingerprint
                }
            elif action.get("fingerprint") is None:
                action["fingerprint"] = fingerprint
    return (["process_review_comment"] if pending_ids else []), pending_ids


def _review_fingerprint(item: dict[str, Any]) -> str:
    payload = {
        "body": item.get("body"),
        "state": item.get("state"),
        "path": item.get("path"),
        "line": item.get("line"),
        "resolved": item.get("resolved"),
        "updated_at": item.get("updated_at"),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def evaluate_snapshot(
    snapshot: dict[str, Any],
    state: dict[str, Any],
    *,
    now: float,
    authority: set[str],
    no_pipeline_expected: bool = False,
) -> dict[str, Any]:
    objective = state["objective"]
    head_sha = snapshot.get("head", {}).get("sha")
    state["target"] = {
        key: snapshot.get(key)
        for key in ("provider", "host", "repository", "number", "url")
    }
    state["current_head"] = head_sha

    if snapshot.get("merged") or snapshot.get("closed") or str(snapshot.get("state", "")).upper() in {"MERGED", "CLOSED"}:
        return _result(state, snapshot, now, ["stop_pr_closed"], terminal=True, reason="provider_closed", next_poll=0)

    review_actions, review_ids = _review_action(snapshot, state, now=now)
    pipeline = snapshot.get("pipeline", {})
    summary = pipeline_summary(
        pipeline.get("jobs", []),
        evidence_complete=bool(pipeline.get("evidence_complete")),
        no_pipeline_expected=no_pipeline_expected,
    )
    snapshot["pipeline_summary"] = summary

    if review_actions:
        result = _result(state, snapshot, now, review_actions, terminal=False, reason="review_activity", next_poll=30)
        result["review_item_ids"] = review_ids
        return result

    capabilities = snapshot.get("capabilities") or {}
    if capabilities.get("review_thread_resolution") is False:
        return _result(
            state,
            snapshot,
            now,
            ["user_help_required"],
            terminal=True,
            reason="incomplete_review_evidence",
            next_poll=0,
        )

    pipeline_state = summary["state"]
    if pipeline_state == "failed":
        _reset_settle(state)
        failed_jobs = [
            job for job in pipeline.get("jobs", [])
            if str(job.get("status", "")).lower() in {"failure", "failed", "cancelled", "canceled", "timed_out", "action_required"}
            and not job.get("allow_failure")
        ]
        failure_kinds = {job.get("failure_kind") for job in failed_jobs if job.get("failure_kind")}
        if "infrastructure" in failure_kinds:
            return _result(state, snapshot, now, ["user_help_required"], terminal=True, reason="infrastructure_failure", next_poll=0)
        if failure_kinds and failure_kinds <= {"flaky"}:
            used = int(state.setdefault("retry_counts", {}).get(head_sha, 0))
            if used >= MAX_RETRIES_PER_SHA:
                return _result(state, snapshot, now, ["stop_exhausted_retries"], terminal=True, reason="retry_budget_exhausted", next_poll=0)
            if "retry-ci" not in authority:
                return _result(state, snapshot, now, ["user_help_required"], terminal=True, reason="retry_authority_required", next_poll=0)
            return _result(state, snapshot, now, ["retry_failed_checks"], terminal=False, reason="flaky_failure", next_poll=30)
        return _result(state, snapshot, now, ["diagnose_ci_failure"], terminal=False, reason="pipeline_failed", next_poll=30)

    if pipeline_state == "no_pipeline_evidence":
        _reset_settle(state)
        terminal = objective == "until-ready"
        return _result(
            state,
            snapshot,
            now,
            ["no_pipeline_evidence"],
            terminal=terminal,
            reason="no_pipeline_evidence",
            next_poll=0 if terminal else 30,
        )

    if pipeline_state == "incomplete":
        _reset_settle(state)
        return _result(state, snapshot, now, ["provider_evidence_incomplete"], terminal=False, reason="incomplete_pipeline_evidence", next_poll=30)

    if pipeline_state == "pending":
        _reset_settle(state)
        return _result(state, snapshot, now, ["idle"], terminal=False, reason="pipeline_pending", next_poll=30)

    fingerprint = _pipeline_fingerprint(snapshot)
    settle = state.setdefault("settle", {})
    if settle.get("fingerprint") != fingerprint:
        settle.update({"fingerprint": fingerprint, "green_since": now, "snapshots": 1})
    else:
        settle["snapshots"] = int(settle.get("snapshots", 0)) + 1

    if objective == "until-ready":
        elapsed = now - float(settle["green_since"])
        if elapsed >= SETTLE_SECONDS and int(settle["snapshots"]) >= 2:
            return _result(state, snapshot, now, ["stop_ready"], terminal=True, reason="pipeline_ready", next_poll=0)
        return _result(state, snapshot, now, ["ready_settling"], terminal=False, reason="pipeline_green_settling", next_poll=60)

    return _result(state, snapshot, now, ["ready_to_merge"], terminal=False, reason="pipeline_green", next_poll=120)


def _reset_settle(state: dict[str, Any]) -> None:
    state["settle"] = {"fingerprint": None, "green_since": None, "snapshots": 0}


def _result(
    state: dict[str, Any],
    snapshot: dict[str, Any],
    now: float,
    actions: list[str],
    *,
    terminal: bool,
    reason: str,
    next_poll: int,
) -> dict[str, Any]:
    change_payload = {
        "head": snapshot.get("head", {}).get("sha"),
        "state": snapshot.get("state"),
        "pipeline": snapshot.get("pipeline_summary"),
        "review": snapshot.get("review_decision"),
        "mergeability": snapshot.get("mergeability"),
        "actions": actions,
        "reason": reason,
    }
    change_key = hashlib.sha256(json.dumps(change_payload, sort_keys=True).encode("utf-8")).hexdigest()
    changed = change_key != state.get("last_change_key")
    heartbeat_due = state.get("last_heartbeat") is None or now - float(state["last_heartbeat"]) >= SETTLE_SECONDS
    if changed:
        state["last_change_key"] = change_key
    if heartbeat_due:
        state["last_heartbeat"] = now
    return {
        "schema_version": SCHEMA_VERSION,
        "snapshot": snapshot,
        "actions": actions,
        "terminal": terminal,
        "reason": reason,
        "next_poll_seconds": next_poll,
        "changed": changed,
        "heartbeat_due": heartbeat_due,
    }


def acquire_lease(
    state: dict[str, Any],
    *,
    owner: str,
    host: str | None = None,
    pid: int | None = None,
    now: float | None = None,
    takeover: bool = False,
    process_alive: Callable[[int], bool] | None = None,
) -> str:
    host = host or socket.gethostname()
    pid = pid or os.getpid()
    now = now if now is not None else time.time()
    existing = state.get("lease")
    new_lease = {"owner": owner, "host": host, "pid": pid, "heartbeat": now}
    if not existing:
        state["lease"] = new_lease
        return "acquired"
    if existing.get("owner") == owner:
        state["lease"] = new_lease
        return "renewed"
    if takeover:
        state["lease"] = new_lease
        return "taken_over"
    if existing.get("host") == host:
        checker = process_alive or _process_alive
        if not checker(int(existing.get("pid") or 0)):
            state["lease"] = new_lease
            return "recovered"
    age = now - float(existing.get("heartbeat") or 0)
    raise LeaseConflict(
        f"target lease is owned by {existing.get('owner')} on {existing.get('host')} "
        f"(pid {existing.get('pid')}, heartbeat age {age:.0f}s); explicit takeover required"
    )


def release_lease(state: dict[str, Any], *, owner: str) -> None:
    if state.get("lease", {}).get("owner") == owner:
        state["lease"] = None


def acquire_file_lease(
    path: str | Path,
    *,
    owner: str,
    host: str | None = None,
    pid: int | None = None,
    now: float | None = None,
    takeover: bool = False,
    process_alive: Callable[[int], bool] | None = None,
) -> str:
    """Claim one watcher with an atomic create-if-absent lease file."""
    lease_path = Path(path)
    lease_path.parent.mkdir(parents=True, exist_ok=True)
    host = host or socket.gethostname()
    pid = pid or os.getpid()
    now = now if now is not None else time.time()
    lease = {"owner": owner, "host": host, "pid": pid, "heartbeat": now}
    recovered = False
    while True:
        try:
            descriptor = os.open(lease_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            try:
                with lease_path.open("r", encoding="utf-8") as handle:
                    existing = json.load(handle)
            except (OSError, ValueError) as error:
                raise LeaseConflict(f"cannot verify existing lease {lease_path}: {error}") from error
            if existing.get("owner") == owner:
                save_state_atomic(lease_path, lease)
                return "renewed"
            checker = process_alive or _process_alive
            dead_same_host = (
                existing.get("host") == host
                and not checker(int(existing.get("pid") or 0))
            )
            if not takeover and not dead_same_host:
                age = now - float(existing.get("heartbeat") or 0)
                raise LeaseConflict(
                    f"target lease is owned by {existing.get('owner')} on {existing.get('host')} "
                    f"(pid {existing.get('pid')}, heartbeat age {age:.0f}s); explicit takeover required"
                )
            try:
                os.unlink(lease_path)
            except FileNotFoundError:
                pass
            recovered = dead_same_host and not takeover
            continue
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(lease, handle, sort_keys=True, separators=(",", ":"))
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        if takeover:
            return "taken_over"
        return "recovered" if recovered else "acquired"


def release_file_lease(path: str | Path, *, owner: str) -> None:
    lease_path = Path(path)
    try:
        with lease_path.open("r", encoding="utf-8") as handle:
            existing = json.load(handle)
    except FileNotFoundError:
        return
    if existing.get("owner") == owner:
        try:
            os.unlink(lease_path)
        except FileNotFoundError:
            pass


def _process_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def record_read_error(state: dict[str, Any], message: str, *, now: float) -> dict[str, Any]:
    errors = state.setdefault("read_errors", {"consecutive": 0, "last": None})
    errors["consecutive"] = int(errors.get("consecutive", 0)) + 1
    errors["last"] = {"message": message, "at": now}
    count = errors["consecutive"]
    return {
        "consecutive": count,
        "next_poll_seconds": min(30 * (2 ** (count - 1)), 300),
        "terminal": count >= 3,
        "reason": "provider_read_blocker" if count >= 3 else "transient_provider_read_error",
    }


def clear_read_errors(state: dict[str, Any]) -> None:
    state["read_errors"] = {"consecutive": 0, "last": None}


def canonical_state_key(snapshot: dict[str, Any]) -> str:
    identity = "|".join(
        str(snapshot.get(key) or "") for key in ("provider", "host", "repository", "number")
    )
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    provider = str(snapshot.get("provider") or "provider")
    number = str(snapshot.get("number") or "item")
    return f"{provider}-{number}-{digest}.json"


def validate_state_target(state: dict[str, Any], snapshot: dict[str, Any]) -> None:
    stored = state.get("target") or {}
    if not stored:
        return
    keys = ("provider", "host", "repository", "number")
    mismatches = [key for key in keys if str(stored.get(key) or "") != str(snapshot.get(key) or "")]
    if mismatches:
        details = ", ".join(
            f"{key}={stored.get(key)!r} (fetched {snapshot.get(key)!r})" for key in mismatches
        )
        raise ValueError(f"state file belongs to a different canonical target: {details}")


def default_user_state_directory() -> Path:
    if os.name == "nt" and os.environ.get("LOCALAPPDATA"):
        return Path(os.environ["LOCALAPPDATA"]) / "qp" / "state" / "wo-pr"
    if os.sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "qp" / "state" / "wo-pr"
    base = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state"))
    return base / "qp" / "wo-pr"

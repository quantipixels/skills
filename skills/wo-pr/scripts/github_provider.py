"""Read-only GitHub adapter for wo-pr."""

from __future__ import annotations

import json
import os
import subprocess
from typing import Any, Callable


class CommandError(RuntimeError):
    pass


def _run_json(
    command: list[str], *, allowed_codes: set[int] | None = None, env: dict[str, str] | None = None
) -> Any:
    result = subprocess.run(command, check=False, capture_output=True, text=True, env=env)
    allowed = allowed_codes or {0}
    if result.returncode not in allowed:
        raise CommandError(f"command failed ({result.returncode}): {result.stderr.strip()}")
    text = result.stdout.strip()
    return json.loads(text) if text else []


def normalize_pr(raw: dict[str, Any], *, host: str, repository: str) -> dict[str, Any]:
    state = str(raw.get("state") or "UNKNOWN").upper()
    merged = bool(raw.get("mergedAt")) or state == "MERGED"
    closed = bool(raw.get("closedAt")) or state == "CLOSED"
    return {
        "provider": "github",
        "host": host,
        "repository": repository,
        "number": raw.get("number"),
        "url": raw.get("url"),
        "state": "MERGED" if merged else "CLOSED" if closed else state,
        "merged": merged,
        "closed": closed,
        "base": {"branch": raw.get("baseRefName"), "sha": raw.get("baseRefOid")},
        "head": {"branch": raw.get("headRefName"), "sha": raw.get("headRefOid")},
        "mergeability": raw.get("mergeable") or "UNKNOWN",
        "review_decision": raw.get("reviewDecision") or "",
        "draft": bool(raw.get("isDraft")),
    }


def normalize_checks(checks: list[dict[str, Any]], *, required_names: set[str] | None) -> list[dict[str, Any]]:
    mapping = {
        "SUCCESS": "success",
        "NEUTRAL": "neutral",
        "SKIPPED": "skipped",
        "CANCELLED": "cancelled",
        "CANCELED": "cancelled",
        "TIMED_OUT": "timed_out",
        "FAILURE": "failure",
        "ERROR": "failure",
        "ACTION_REQUIRED": "action_required",
        "PENDING": "pending",
        "QUEUED": "queued",
        "IN_PROGRESS": "running",
        "EXPECTED": "pending",
    }
    jobs = []
    for check in checks:
        raw_state = str(check.get("state") or "").upper()
        jobs.append(
            {
                "id": check.get("id") or check.get("link") or check.get("detailsUrl") or check.get("name"),
                "name": check.get("name"),
                "status": mapping.get(raw_state, "unknown"),
                "required": None if required_names is None else check.get("name") in required_names,
                "allow_failure": False,
                "workflow": check.get("workflow"),
                "url": check.get("link") or check.get("detailsUrl"),
                "raw_state": raw_state,
            }
        )
    return jobs


def normalize_review_items(
    issue_comments: list[dict[str, Any]],
    inline_comments: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
    *,
    resolution_by_comment: dict[int, bool] | None = None,
) -> list[dict[str, Any]]:
    pending_review_ids = {review.get("id") for review in reviews if str(review.get("state", "")).upper() == "PENDING"}
    items = []
    for comment in issue_comments:
        items.append(_review_item("issue", comment))
    for comment in inline_comments:
        if comment.get("pull_request_review_id") in pending_review_ids:
            continue
        resolved = (resolution_by_comment or {}).get(comment.get("id"))
        if resolved is not False:
            continue
        item = _review_item("comment", comment)
        item["resolved"] = resolved
        items.append(item)
    for review in reviews:
        if str(review.get("state", "")).upper() == "PENDING":
            continue
        if not str(review.get("body") or "").strip():
            continue
        items.append(_review_item("review", review))
    return sorted(items, key=lambda item: (str(item.get("created_at") or ""), item["id"]))


def _review_item(kind: str, raw: dict[str, Any]) -> dict[str, Any]:
    user = raw.get("user") or {}
    return {
        "id": f"{kind}:{raw.get('id')}",
        "kind": kind,
        "body": raw.get("body") or "",
        "author": user.get("login"),
        "author_association": raw.get("author_association"),
        "state": raw.get("state"),
        "path": raw.get("path"),
        "line": raw.get("line") or raw.get("original_line"),
        "url": raw.get("html_url"),
        "created_at": raw.get("created_at") or raw.get("submitted_at"),
        "updated_at": raw.get("updated_at") or raw.get("submitted_at"),
        "resolved": raw.get("resolved"),
    }


class GitHubProvider:
    def __init__(
        self,
        *,
        host: str = "github.com",
        repository: str | None = None,
        runner: Callable[[list[str]], Any] | None = None,
        trusted_hosts: set[str] | None = None,
    ) -> None:
        self.host = host
        self.repository = repository
        self.runner = runner
        self.trusted_hosts = {"github.com", *(trusted_hosts or set())}

    def _call(self, command: list[str], *, allowed_codes: set[int] | None = None) -> Any:
        if self.runner:
            return self.runner(command)
        return _run_json(command, allowed_codes=allowed_codes, env=self._command_environment())

    def _command_environment(self) -> dict[str, str]:
        environment = os.environ.copy()
        host = self.host.lower().rstrip(".")
        environment["GH_HOST"] = host
        environment.pop("GH_REPO", None)
        trusted_hosts = {value.lower().rstrip(".") for value in self.trusted_hosts}
        if host not in trusted_hosts:
            for name in ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN", "GITHUB_ENTERPRISE_TOKEN"):
                environment.pop(name, None)
        return environment

    def _repo(self) -> str:
        if self.repository:
            return self.repository
        raw = self._call(["gh", "repo", "view", "--json", "nameWithOwner"])
        self.repository = raw["nameWithOwner"]
        return self.repository

    def _repo_spec(self) -> str:
        repository = self._repo()
        return repository if self.host == "github.com" else f"{self.host}/{repository}"

    def _current_branch(self) -> str:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            check=False,
            capture_output=True,
            text=True,
        )
        branch = result.stdout.strip()
        if result.returncode != 0 or not branch:
            raise ValueError("cannot resolve the current branch for --pr auto")
        return branch

    def _thread_resolutions(self, number: int) -> tuple[dict[int, bool], bool]:
        repository = self._repo()
        parts = repository.split("/", 1)
        if len(parts) != 2:
            return {}, False
        query = """query($owner:String!,$name:String!,$number:Int!,$endCursor:String){repository(owner:$owner,name:$name){pullRequest(number:$number){reviewThreads(first:100,after:$endCursor){nodes{isResolved comments(first:100){nodes{databaseId}}}pageInfo{hasNextPage endCursor}}}}}"""
        raw = self._call([
            "gh", "api", "graphql", "--hostname", self.host, "--paginate", "--slurp",
            "-F", f"owner={parts[0]}", "-F", f"name={parts[1]}", "-F", f"number={number}",
            "-f", f"query={query}",
        ])
        pages = raw if isinstance(raw, list) else [raw]
        resolutions: dict[int, bool] = {}
        for page in pages:
            threads = (((page.get("data") or {}).get("repository") or {}).get("pullRequest") or {}).get("reviewThreads") or {}
            for thread in threads.get("nodes") or []:
                for comment in ((thread.get("comments") or {}).get("nodes") or []):
                    if comment.get("databaseId") is not None:
                        resolutions[int(comment["databaseId"])] = bool(thread.get("isResolved"))
        return resolutions, True

    def _paginate(self, endpoint: str) -> list[dict[str, Any]]:
        raw = self._call(["gh", "api", "--hostname", self.host, "--paginate", "--slurp", endpoint])
        if raw and isinstance(raw[0], list):
            return [item for page in raw for item in page]
        return raw or []

    def fetch(self, target: str = "auto") -> dict[str, Any]:
        repository = self._repo()
        repo_spec = self._repo_spec()
        selector = [self._current_branch() if target == "auto" else target]
        pr = self._call(
            [
                "gh", "--repo", repo_spec, "pr", "view", *selector, "--json",
                "number,url,state,mergedAt,closedAt,baseRefName,baseRefOid,headRefName,headRefOid,mergeable,reviewDecision,isDraft",
            ]
        )
        snapshot = normalize_pr(pr, host=self.host, repository=repository)
        number = snapshot["number"]
        checks = self._call(
            ["gh", "--repo", repo_spec, "pr", "checks", str(number), "--json", "name,state,bucket,link,workflow"],
            allowed_codes={0, 1, 8},
        )
        required_names: set[str] | None
        try:
            required = self._call(
                ["gh", "--repo", repo_spec, "pr", "checks", str(number), "--required", "--json", "name,state,bucket,link,workflow"],
                allowed_codes={0, 1, 8},
            )
            required_names = {row.get("name") for row in required}
        except CommandError:
            required_names = None
        issue_comments = self._paginate(f"repos/{repository}/issues/{number}/comments?per_page=100")
        inline_comments = self._paginate(f"repos/{repository}/pulls/{number}/comments?per_page=100")
        reviews = self._paginate(f"repos/{repository}/pulls/{number}/reviews?per_page=100")
        resolutions, resolution_complete = self._thread_resolutions(int(number))
        inline_ids = {int(row["id"]) for row in inline_comments if row.get("id") is not None}
        resolution_complete = resolution_complete and inline_ids <= set(resolutions)
        snapshot.update(
            {
                "pipeline": {
                    "evidence_complete": required_names is not None,
                    "jobs": normalize_checks(checks, required_names=required_names),
                },
                "review_items": normalize_review_items(
                    issue_comments, inline_comments, reviews, resolution_by_comment=resolutions
                ),
                "capabilities": {
                    "required_check_identity": required_names is not None,
                    "review_thread_resolution": resolution_complete,
                },
                "errors": (
                    ([] if required_names is not None else ["required check identity unavailable"])
                    + ([] if resolution_complete else ["review thread resolution unavailable or incomplete"])
                ),
            }
        )
        return snapshot

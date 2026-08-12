"""Read-only GitLab adapter for wo-pr."""

from __future__ import annotations

import json
import os
import re
import subprocess
from typing import Any, Callable
from urllib.parse import quote, urlparse


class CommandError(RuntimeError):
    pass


def _run_json(command: list[str], *, env: dict[str, str] | None = None) -> Any:
    result = subprocess.run(command, check=False, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise CommandError(f"command failed ({result.returncode}): {result.stderr.strip()}")
    text = result.stdout.strip()
    return json.loads(text) if text else []


def normalize_mr(raw: dict[str, Any], *, host: str, repository: str) -> dict[str, Any]:
    state = str(raw.get("state") or "unknown").upper()
    merged = bool(raw.get("merged_at")) or state == "MERGED"
    closed = bool(raw.get("closed_at")) or state == "CLOSED"
    diff_refs = raw.get("diff_refs") or {}
    return {
        "provider": "gitlab",
        "host": host,
        "repository": repository,
        "number": raw.get("iid"),
        "url": raw.get("web_url"),
        "state": "MERGED" if merged else "CLOSED" if closed else state,
        "merged": merged,
        "closed": closed,
        "base": {"branch": raw.get("target_branch"), "sha": diff_refs.get("base_sha")},
        "head": {"branch": raw.get("source_branch"), "sha": raw.get("sha") or diff_refs.get("head_sha")},
        "diff_refs": {
            "base_sha": diff_refs.get("base_sha"),
            "head_sha": diff_refs.get("head_sha"),
            "start_sha": diff_refs.get("start_sha"),
        },
        "mergeability": raw.get("detailed_merge_status") or raw.get("merge_status") or "unknown",
        "review_decision": raw.get("approval_state") or "",
        "draft": bool(raw.get("draft") or raw.get("work_in_progress")),
    }


def normalize_jobs(raw_jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    mapping = {
        "created": "created",
        "waiting_for_resource": "waiting",
        "preparing": "pending",
        "pending": "pending",
        "running": "running",
        "success": "success",
        "failed": "failure",
        "canceled": "cancelled",
        "cancelled": "cancelled",
        "skipped": "skipped",
        "manual": "manual",
        "scheduled": "scheduled",
    }
    jobs = []
    for job in raw_jobs:
        raw_status = str(job.get("status") or "").lower()
        allow_failure = bool(job.get("allow_failure"))
        jobs.append(
            {
                "id": job.get("id"),
                "name": job.get("name"),
                "status": mapping.get(raw_status, "unknown"),
                "required": not allow_failure and raw_status != "skipped",
                "allow_failure": allow_failure,
                "stage": job.get("stage"),
                "url": job.get("web_url"),
                "raw_state": raw_status,
            }
        )
    return jobs


def normalize_trigger_jobs(raw_jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    jobs = []
    for raw_job in raw_jobs:
        downstream = raw_job.get("downstream_pipeline") or {}
        trigger_status = str(raw_job.get("status") or "").lower()
        downstream_status = str(downstream.get("status") or "").lower()
        effective = dict(raw_job)
        if downstream_status and trigger_status in {
            "created", "waiting_for_resource", "preparing", "pending", "running", "success"
        }:
            effective["status"] = downstream_status
        if downstream.get("web_url"):
            effective["web_url"] = downstream["web_url"]
        job = normalize_jobs([effective])[0]
        job["id"] = f"trigger:{raw_job.get('id')}"
        job["downstream_pipeline_id"] = downstream.get("id")
        jobs.append(job)
    return jobs


def current_job_attempts(raw_jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    for job in raw_jobs:
        key = (str(job.get("name") or ""), str(job.get("stage") or ""))
        if key not in latest or int(job.get("id") or 0) > int(latest[key].get("id") or 0):
            latest[key] = job
    return list(latest.values())


def normalize_discussions(discussions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    items = []
    for discussion in discussions:
        discussion_id = discussion.get("id")
        for note in discussion.get("notes") or []:
            if note.get("system"):
                continue
            if bool(note.get("resolved", discussion.get("resolved", False))):
                continue
            author = note.get("author") or {}
            items.append(
                {
                    "id": f"discussion:{discussion_id}:note:{note.get('id')}",
                    "kind": "discussion",
                    "discussion_id": discussion_id,
                    "note_id": note.get("id"),
                    "body": note.get("body") or "",
                    "author": author.get("username") or author.get("name"),
                    "resolved": bool(note.get("resolved", discussion.get("resolved", False))),
                    "created_at": note.get("created_at"),
                    "url": note.get("web_url"),
                }
            )
    return sorted(items, key=lambda item: (str(item.get("created_at") or ""), item["id"]))


class GitLabProvider:
    def __init__(
        self,
        *,
        host: str = "gitlab.com",
        repository: str | None = None,
        runner: Callable[[list[str]], Any] | None = None,
        trusted_hosts: set[str] | None = None,
    ) -> None:
        self.host = host
        self.repository = repository
        self.runner = runner
        self.trusted_hosts = {"gitlab.com", *(trusted_hosts or set())}

    def _call(self, command: list[str]) -> Any:
        return self.runner(command) if self.runner else _run_json(command, env=self._command_environment())

    def _command_environment(self) -> dict[str, str]:
        environment = os.environ.copy()
        environment.pop("GITLAB_HOST", None)
        host = self.host.lower().rstrip(".")
        trusted_hosts = {value.lower().rstrip(".") for value in self.trusted_hosts}
        if host not in trusted_hosts:
            for name in ("GITLAB_TOKEN", "GITLAB_ACCESS_TOKEN", "OAUTH_TOKEN", "CI_JOB_TOKEN"):
                environment.pop(name, None)
            environment["GLAB_ENABLE_CI_AUTOLOGIN"] = "false"
        return environment

    def _repo(self) -> str:
        if self.repository:
            return self.repository
        raw = self._call([
            "glab", "api", "--hostname", self.host, "projects/:fullpath"
        ])
        repository = raw.get("path_with_namespace") or raw.get("fullPath") or raw.get("nameWithNamespace")
        if not repository:
            raise CommandError("cannot resolve GitLab project; pass --repo owner/project")
        self.repository = repository
        return repository

    def _api(self, endpoint: str) -> Any:
        return self._call(["glab", "api", "--hostname", self.host, endpoint])

    def _paginate(self, endpoint: str) -> list[dict[str, Any]]:
        rows = []
        page = 1
        separator = "&" if "?" in endpoint else "?"
        while True:
            batch = self._api(f"{endpoint}{separator}per_page=100&page={page}") or []
            rows.extend(batch)
            if len(batch) < 100:
                return rows
            page += 1

    def _iid(self, target: str, project: str) -> int:
        parsed = urlparse(target)
        target_path = parsed.path if parsed.scheme and parsed.netloc else target
        match = re.search(r"/merge_requests/(\d+)(?:/|$)", target_path)
        if match:
            return int(match.group(1))
        if target != "auto":
            return int(target)
        branch_result = subprocess.run(["git", "branch", "--show-current"], check=False, capture_output=True, text=True)
        branch = branch_result.stdout.strip()
        if branch_result.returncode != 0 or not branch:
            raise CommandError("cannot infer current branch for GitLab MR auto selection")
        encoded = quote(project, safe="")
        rows = self._api(f"projects/{encoded}/merge_requests?state=opened&source_branch={quote(branch, safe='')}")
        if len(rows) != 1:
            raise CommandError(f"expected one open GitLab MR for branch {branch!r}, found {len(rows)}")
        return int(rows[0]["iid"])

    def fetch(self, target: str = "auto") -> dict[str, Any]:
        project = self._repo()
        encoded = quote(project, safe="")
        iid = self._iid(target, project)
        raw = self._api(f"projects/{encoded}/merge_requests/{iid}")
        snapshot = normalize_mr(raw, host=self.host, repository=project)
        pipelines = self._paginate(f"projects/{encoded}/merge_requests/{iid}/pipelines")
        jobs: list[dict[str, Any]] = []
        errors: list[str] = []
        head_pipeline = raw.get("head_pipeline") or {}
        pipeline_id = head_pipeline.get("id")
        selected_pipeline = head_pipeline
        if pipeline_id is None:
            head_sha = snapshot.get("head", {}).get("sha")
            current = [pipeline for pipeline in pipelines if pipeline.get("sha") == head_sha]
            if current:
                selected_pipeline = max(current, key=lambda row: int(row.get("id") or 0))
                pipeline_id = selected_pipeline.get("id")
        elif not selected_pipeline.get("status"):
            selected_pipeline = next(
                (pipeline for pipeline in pipelines if pipeline.get("id") == pipeline_id),
                selected_pipeline,
            )
        if pipeline_id is not None:
            raw_jobs = self._paginate(f"projects/{encoded}/pipelines/{pipeline_id}/jobs?include_retried=true")
            jobs = normalize_jobs(current_job_attempts(raw_jobs))
            trigger_evidence_complete = True
            try:
                raw_trigger_jobs = self._paginate(
                    f"projects/{encoded}/pipelines/{pipeline_id}/trigger_jobs"
                )
            except CommandError:
                try:
                    raw_trigger_jobs = self._paginate(
                        f"projects/{encoded}/pipelines/{pipeline_id}/bridges"
                    )
                except CommandError:
                    raw_trigger_jobs = []
                    trigger_evidence_complete = False
                    errors.append("trigger job evidence unavailable")
            jobs.extend(normalize_trigger_jobs(current_job_attempts(raw_trigger_jobs)))
            if not jobs and selected_pipeline.get("status"):
                pipeline_job = dict(selected_pipeline)
                pipeline_job.update({
                    "id": f"pipeline:{pipeline_id}",
                    "name": "pipeline",
                    "allow_failure": False,
                    "web_url": selected_pipeline.get("web_url"),
                })
                jobs = normalize_jobs([pipeline_job])
        else:
            trigger_evidence_complete = True
        discussions = self._paginate(f"projects/{encoded}/merge_requests/{iid}/discussions")
        approvals = self._api(f"projects/{encoded}/merge_requests/{iid}/approvals")
        snapshot["review_decision"] = "APPROVED" if approvals.get("approved") else "REVIEW_REQUIRED"
        snapshot.update(
            {
                "pipeline": {
                    "evidence_complete": trigger_evidence_complete,
                    "pipeline_id": pipeline_id,
                    "jobs": jobs,
                },
                "review_items": normalize_discussions(discussions),
                "capabilities": {
                    "required_check_identity": True,
                    "discussion_resolution": True,
                    "approval_state": True,
                },
                "errors": errors,
            }
        )
        return snapshot

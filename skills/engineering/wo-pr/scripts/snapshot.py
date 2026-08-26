#!/usr/bin/env python3
"""Return a read-only normalized snapshot of one GitHub PR or GitLab MR."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

PUBLIC_HOST = {"github": "github.com", "gitlab": "gitlab.com"}
GITHUB_TOKENS = ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN", "GITHUB_ENTERPRISE_TOKEN")
GITLAB_TOKENS = ("GITLAB_TOKEN", "GITLAB_ACCESS_TOKEN", "OAUTH_TOKEN", "CI_JOB_TOKEN")


class SnapshotError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("auto", "github", "gitlab"), default="auto")
    parser.add_argument("--pr", default="auto", help="number, URL, or auto")
    parser.add_argument("--repo", help="owner/repository or group/project")
    parser.add_argument("--host", help="provider host")
    parser.add_argument("--trusted-host", action="append", default=[])
    parser.add_argument("--fixture", type=Path, help="normalize captured provider JSON instead of contacting a provider")
    parser.add_argument("--timeout", type=int, default=90)
    return parser.parse_args()


def run(command: list[str], *, environment: dict[str, str], timeout: int) -> str:
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
        timeout=timeout,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise SnapshotError(message or f"command failed ({result.returncode}): {' '.join(command)}")
    return result.stdout


def command_environment(provider: str, host: str, trusted_hosts: set[str]) -> dict[str, str]:
    host = host.lower().rstrip(".")
    allowed = {PUBLIC_HOST[provider], *(value.lower().rstrip(".") for value in trusted_hosts)}
    if host not in allowed:
        raise SnapshotError(f"trust for custom provider host {host!r} was not confirmed")
    result = dict(os.environ)
    if provider == "github":
        result["GH_HOST"] = host
        result.pop("GH_REPO", None)
        if host == "github.com":
            result.pop("GH_ENTERPRISE_TOKEN", None)
            result.pop("GITHUB_ENTERPRISE_TOKEN", None)
        else:
            for name in GITHUB_TOKENS:
                result.pop(name, None)
    else:
        result.pop("GITLAB_HOST", None)
        result["GLAB_ENABLE_CI_AUTOLOGIN"] = "false"
        result.pop("CI_JOB_TOKEN", None)
        if host != "gitlab.com":
            for name in GITLAB_TOKENS:
                result.pop(name, None)
    return result


def remote_identity() -> tuple[str | None, str | None, str | None]:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        check=False,
        capture_output=True,
        text=True,
    )
    remote = result.stdout.strip()
    if not remote:
        return None, None, None
    if "://" not in remote and ":" in remote:
        user_host, path = remote.split(":", 1)
        remote = f"ssh://{user_host}/{path}"
    parsed = urlparse(remote)
    host = (parsed.hostname or "").lower().rstrip(".") or None
    repo = parsed.path.strip("/")
    if repo.endswith(".git"):
        repo = repo[:-4]
    provider = None
    if host and (host == "github.com" or host.startswith("github.")):
        provider = "github"
    elif host and (host == "gitlab.com" or host.startswith("gitlab.")):
        provider = "gitlab"
    return provider, host, repo or None


def target_from_url(value: str) -> tuple[str | None, str | None, str | None, int | None]:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None, None, None, None
    host = (parsed.hostname or "").lower().rstrip(".")
    path = parsed.path.strip("/")
    if "/pull/" in f"/{path}/":
        repo, raw_number = path.split("/pull/", 1)
        return "github", host, repo, int(raw_number.split("/", 1)[0])
    marker = "/-/merge_requests/"
    if marker in f"/{path}/":
        repo, raw_number = path.split(marker, 1)
        return "gitlab", host, repo, int(raw_number.split("/", 1)[0])
    return None, host or None, None, None


def resolve_target(args: argparse.Namespace) -> tuple[str, str, str | None, int | None]:
    url_provider, url_host, url_repo, url_number = target_from_url(args.pr)
    remote_provider, remote_host, remote_repo = remote_identity()
    provider = args.provider if args.provider != "auto" else url_provider or remote_provider
    if provider not in {"github", "gitlab"}:
        raise SnapshotError("cannot infer provider; pass --provider github or --provider gitlab")
    if url_provider and url_provider != provider:
        raise SnapshotError(f"target URL is for {url_provider}, not {provider}")
    host = (args.host or url_host or remote_host or PUBLIC_HOST[provider]).lower().rstrip(".")
    if args.host and url_host and args.host.lower().rstrip(".") != url_host:
        raise SnapshotError("--host conflicts with target URL")
    repo = args.repo or url_repo or remote_repo
    if args.repo and url_repo and args.repo.strip("/") != url_repo.strip("/"):
        raise SnapshotError("--repo conflicts with target URL")
    number = url_number
    if number is None and args.pr != "auto":
        try:
            number = int(args.pr)
        except ValueError as error:
            raise SnapshotError("--pr must be a number, supported URL, or auto") from error
    return provider, host, repo, number


def json_command(command: list[str], *, environment: dict[str, str], timeout: int) -> Any:
    output = run(command, environment=environment, timeout=timeout)
    try:
        return json.loads(output)
    except json.JSONDecodeError as error:
        raise SnapshotError(f"provider returned invalid JSON: {error}") from error


def normalize_check(item: dict[str, Any]) -> dict[str, Any]:
    name = item.get("name") or item.get("context") or item.get("stage") or "unknown"
    status = item.get("state") or item.get("status") or item.get("bucket") or "unknown"
    conclusion = item.get("conclusion")
    return {
        "id": str(item.get("id") or item.get("databaseId") or name),
        "name": str(name),
        "status": str(status).lower(),
        "conclusion": str(conclusion).lower() if conclusion is not None else None,
        "required": item.get("required"),
        "url": item.get("link") or item.get("detailsUrl") or item.get("targetUrl") or item.get("web_url"),
    }


def normalize_github(raw: dict[str, Any]) -> dict[str, Any]:
    core = raw.get("core") or raw
    checks_raw = raw.get("checks")
    if checks_raw is None:
        checks_raw = core.get("statusCheckRollup") or []
    threads = raw.get("threads") or {}
    nodes = threads.get("nodes") or []
    feedback = []
    for thread in nodes:
        if thread.get("isResolved"):
            continue
        comments = (thread.get("comments") or {}).get("nodes") or []
        feedback.append(
            {
                "id": str(thread.get("id")),
                "path": thread.get("path"),
                "line": thread.get("line"),
                "outdated": bool(thread.get("isOutdated")),
                "comments": [
                    {
                        "id": str(comment.get("id")),
                        "author": ((comment.get("author") or {}).get("login")),
                        "body": comment.get("body"),
                        "url": comment.get("url"),
                        "created_at": comment.get("createdAt"),
                    }
                    for comment in comments
                ],
            }
        )
    capabilities = {
        "target_complete": all(core.get(key) is not None for key in ("number", "url", "state")),
        "head_complete": bool(core.get("headRefName") and core.get("headRefOid")),
        "checks_complete": bool(raw.get("checks_complete", checks_raw is not None)),
        "feedback_complete": not bool((threads.get("pageInfo") or {}).get("hasNextPage")),
    }
    return {
        "provider": "github",
        "host": raw.get("host") or "github.com",
        "repository": raw.get("repository"),
        "number": core.get("number"),
        "url": core.get("url"),
        "state": str(core.get("state") or "unknown").lower(),
        "merged": str(core.get("state") or "").upper() == "MERGED",
        "draft": bool(core.get("isDraft")),
        "base": {"branch": core.get("baseRefName"), "sha": raw.get("base_sha")},
        "head": {"branch": core.get("headRefName"), "sha": core.get("headRefOid")},
        "mergeability": str(core.get("mergeable") or "unknown").lower(),
        "review_decision": core.get("reviewDecision"),
        "checks": [normalize_check(item) for item in checks_raw],
        "feedback": feedback,
        "capabilities": capabilities,
        "errors": list(raw.get("errors") or []),
    }


def normalize_gitlab(raw: dict[str, Any]) -> dict[str, Any]:
    core = raw.get("core") or raw
    pipeline = raw.get("pipeline") or {}
    jobs = raw.get("jobs") or pipeline.get("jobs") or []
    discussions = raw.get("discussions") or []
    feedback = []
    for discussion in discussions:
        notes = discussion.get("notes") or []
        unresolved = [note for note in notes if note.get("resolvable") and not note.get("resolved")]
        if not unresolved:
            continue
        feedback.append(
            {
                "id": str(discussion.get("id")),
                "path": ((unresolved[-1].get("position") or {}).get("new_path")),
                "line": ((unresolved[-1].get("position") or {}).get("new_line")),
                "outdated": False,
                "comments": [
                    {
                        "id": str(note.get("id")),
                        "author": ((note.get("author") or {}).get("username")),
                        "body": note.get("body"),
                        "url": note.get("web_url"),
                        "created_at": note.get("created_at"),
                    }
                    for note in notes
                ],
            }
        )
    approvals = raw.get("approvals") or {}
    capabilities = {
        "target_complete": all(core.get(key) is not None for key in ("iid", "web_url", "state")),
        "head_complete": bool(core.get("source_branch") and core.get("sha")),
        "checks_complete": bool(raw.get("checks_complete", True)),
        "feedback_complete": bool(raw.get("feedback_complete", len(discussions) < 100)),
    }
    return {
        "provider": "gitlab",
        "host": raw.get("host") or "gitlab.com",
        "repository": raw.get("repository"),
        "number": core.get("iid"),
        "url": core.get("web_url"),
        "state": str(core.get("state") or "unknown").lower(),
        "merged": str(core.get("state") or "").lower() == "merged",
        "draft": bool(core.get("draft") or core.get("work_in_progress")),
        "base": {"branch": core.get("target_branch"), "sha": raw.get("base_sha")},
        "head": {"branch": core.get("source_branch"), "sha": core.get("sha")},
        "mergeability": str(core.get("detailed_merge_status") or core.get("merge_status") or "unknown").lower(),
        "review_decision": {
            "approved": bool(approvals.get("approved")),
            "approvals_left": approvals.get("approvals_left"),
        },
        "checks": [normalize_check(item) for item in jobs],
        "feedback": feedback,
        "capabilities": capabilities,
        "errors": list(raw.get("errors") or []),
    }


def github_live(host: str, repo: str | None, number: int | None, args: argparse.Namespace) -> dict[str, Any]:
    environment = command_environment("github", host, set(args.trusted_host))
    repo_args = ["--repo", repo] if repo else []
    if number is None:
        identity = json_command(
            ["gh", "pr", "view", *repo_args, "--json", "number"],
            environment=environment,
            timeout=args.timeout,
        )
        number = int(identity["number"])
    core = json_command(
        [
            "gh", "pr", "view", str(number), *repo_args,
            "--json",
            "number,url,state,isDraft,baseRefName,headRefName,headRefOid,mergeable,reviewDecision,statusCheckRollup",
        ],
        environment=environment,
        timeout=args.timeout,
    )
    if repo is None:
        view = json_command(
            ["gh", "repo", "view", "--json", "nameWithOwner"],
            environment=environment,
            timeout=args.timeout,
        )
        repo = view["nameWithOwner"]
    owner, name = repo.split("/", 1)
    try:
        required_checks = json_command(
            ["gh", "pr", "checks", str(number), "--repo", repo, "--required", "--json", "name,state,bucket,link,workflow"],
            environment=environment,
            timeout=args.timeout,
        )
        for item in required_checks:
            item["required"] = True
        checks_complete = True
    except SnapshotError:
        required_checks = list(core.get("statusCheckRollup") or [])
        checks_complete = False
    query = """
query($owner:String!,$name:String!,$number:Int!){
  repository(owner:$owner,name:$name){
    pullRequest(number:$number){
      reviewThreads(first:100){
        nodes{id isResolved isOutdated path line comments(first:20){nodes{id url body createdAt author{login}} totalCount}}
        pageInfo{hasNextPage}
      }
    }
  }
}
"""
    thread_response = json_command(
        [
            "gh", "api", "graphql", "--hostname", host,
            "-f", f"query={query}", "-f", f"owner={owner}", "-f", f"name={name}", "-F", f"number={number}",
        ],
        environment=environment,
        timeout=args.timeout,
    )
    threads = (((thread_response.get("data") or {}).get("repository") or {}).get("pullRequest") or {}).get("reviewThreads") or {}
    return {
        "provider": "github",
        "host": host,
        "repository": repo,
        "core": core,
        "checks": required_checks,
        "checks_complete": checks_complete,
        "threads": threads,
    }


def gitlab_api(path: str, *, host: str, environment: dict[str, str], timeout: int) -> Any:
    return json_command(
        ["glab", "api", "--hostname", host, path],
        environment=environment,
        timeout=timeout,
    )


def gitlab_live(host: str, repo: str | None, number: int | None, args: argparse.Namespace) -> dict[str, Any]:
    environment = command_environment("gitlab", host, set(args.trusted_host))
    if repo is None:
        _, _, repo = remote_identity()
    if not repo:
        raise SnapshotError("GitLab snapshot requires --repo or an origin remote")
    project = quote(repo, safe="")
    if number is None:
        branch = run(["git", "branch", "--show-current"], environment=dict(os.environ), timeout=args.timeout).strip()
        candidates = gitlab_api(
            f"projects/{project}/merge_requests?state=opened&source_branch={quote(branch, safe='')}&per_page=100",
            host=host,
            environment=environment,
            timeout=args.timeout,
        )
        if len(candidates) != 1:
            raise SnapshotError(f"expected one open MR for branch {branch!r}, found {len(candidates)}")
        number = int(candidates[0]["iid"])
    core = gitlab_api(
        f"projects/{project}/merge_requests/{number}", host=host, environment=environment, timeout=args.timeout
    )
    pipelines = gitlab_api(
        f"projects/{project}/merge_requests/{number}/pipelines?per_page=100",
        host=host,
        environment=environment,
        timeout=args.timeout,
    )
    pipeline = next((item for item in pipelines if item.get("sha") == core.get("sha")), pipelines[0] if pipelines else {})
    jobs: list[dict[str, Any]] = []
    checks_complete = True
    if pipeline.get("id"):
        jobs = gitlab_api(
            f"projects/{project}/pipelines/{pipeline['id']}/jobs?per_page=100",
            host=host,
            environment=environment,
            timeout=args.timeout,
        )
        checks_complete = len(jobs) < 100
    discussions = gitlab_api(
        f"projects/{project}/merge_requests/{number}/discussions?per_page=100",
        host=host,
        environment=environment,
        timeout=args.timeout,
    )
    try:
        approvals = gitlab_api(
            f"projects/{project}/merge_requests/{number}/approvals",
            host=host,
            environment=environment,
            timeout=args.timeout,
        )
    except SnapshotError:
        approvals = {}
    return {
        "provider": "gitlab",
        "host": host,
        "repository": repo,
        "core": core,
        "pipeline": pipeline,
        "jobs": jobs,
        "checks_complete": checks_complete,
        "discussions": discussions,
        "feedback_complete": len(discussions) < 100,
        "approvals": approvals,
    }


def main() -> int:
    args = parse_args()
    try:
        if args.fixture:
            raw = json.loads(args.fixture.read_text(encoding="utf-8"))
            provider = raw.get("provider")
        else:
            provider, host, repo, number = resolve_target(args)
            raw = github_live(host, repo, number, args) if provider == "github" else gitlab_live(host, repo, number, args)
        if provider == "github":
            result = normalize_github(raw)
        elif provider == "gitlab":
            result = normalize_gitlab(raw)
        else:
            raise SnapshotError("fixture must declare provider github or gitlab")
    except (OSError, ValueError, json.JSONDecodeError, subprocess.TimeoutExpired, SnapshotError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

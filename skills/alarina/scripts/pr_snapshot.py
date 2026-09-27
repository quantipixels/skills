"""Read-only, bounded GitHub PR facts.

The caller owns review judgment, authorization and any later provider write.
This module only asks the installed gh CLI for GraphQL facts. Bodies, tokens and
raw command stderr are never included in the result.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from typing import Any, Callable

SCHEMA_VERSION = 1
PAGE_SIZE = 100
MAX_PAGES = 1000
MAX_OUTPUT_BYTES = 8 * 1024 * 1024

META_QUERY = """
query($owner:String!,$name:String!,$number:Int!) {
  repository(owner:$owner,name:$name) {
    pullRequest(number:$number) {
      id number url state isDraft headRefOid baseRefOid
      headRefName baseRefName
    }
  }
}
"""

THREADS_QUERY = """
query($owner:String!,$name:String!,$number:Int!,$cursor:String) {
  repository(owner:$owner,name:$name) {
    pullRequest(number:$number) {
      reviewThreads(first:100,after:$cursor) {
        nodes {
          id isResolved isOutdated
          comments(first:100) {
            nodes { id url createdAt author { login ... on Node { id } } }
            pageInfo { hasNextPage endCursor }
          }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}
"""

THREAD_COMMENTS_QUERY = """
query($threadId:ID!,$cursor:String) {
  node(id:$threadId) {
    ... on PullRequestReviewThread {
      id
      comments(first:100,after:$cursor) {
        nodes { id url createdAt author { login ... on Node { id } } }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}
"""

REVIEWS_QUERY = """
query($owner:String!,$name:String!,$number:Int!,$cursor:String) {
  repository(owner:$owner,name:$name) {
    pullRequest(number:$number) {
      reviews(first:100,after:$cursor) {
        nodes {
          id url state createdAt submittedAt
          author { login ... on Node { id } }
          commit { oid }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}
"""

ISSUE_COMMENTS_QUERY = """
query($owner:String!,$name:String!,$number:Int!,$cursor:String) {
  repository(owner:$owner,name:$name) {
    pullRequest(number:$number) {
      comments(first:100,after:$cursor) {
        nodes { id url createdAt author { login ... on Node { id } } }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}
"""

CHECKS_QUERY = """
query($owner:String!,$name:String!,$oid:GitObjectID!,$cursor:String) {
  repository(owner:$owner,name:$name) {
    object(oid:$oid) {
      ... on Commit {
        oid
        statusCheckRollup {
          contexts(first:100,after:$cursor) {
            nodes {
              __typename
              ... on CheckRun {
                id name status conclusion detailsUrl
              }
              ... on StatusContext {
                id context state targetUrl
              }
            }
            pageInfo { hasNextPage endCursor }
          }
        }
      }
    }
  }
}
"""


class SnapshotError(Exception):
    """Incomplete provider evidence, without private command output."""

    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def _validate(repo: str, number: int, host: str) -> tuple[str, str]:
    if not isinstance(repo, str) or not re.fullmatch(
        r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo
    ):
        raise ValueError("repo must be explicit OWNER/NAME")
    owner, name = repo.split("/")
    if owner in {".", ".."} or name in {".", ".."}:
        raise ValueError("invalid repository name")
    if type(number) is not int or number <= 0:
        raise ValueError("PR number must be a positive integer")
    if not isinstance(host, str) or not re.fullmatch(
        r"[A-Za-z0-9](?:[A-Za-z0-9.-]{0,251}[A-Za-z0-9])?", host
    ) or ".." in host:
        raise ValueError("host must be a DNS hostname")
    return owner, name


def _gh_transport(argv: list[str]) -> dict:
    try:
        proc = subprocess.run(argv, stdin=subprocess.DEVNULL,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=False, timeout=30)
    except FileNotFoundError as error:
        raise SnapshotError("gh_missing") from error
    except subprocess.TimeoutExpired as error:
        raise SnapshotError("api_timeout") from error
    if proc.returncode != 0:
        raise SnapshotError("api_failed")
    if len(proc.stdout) > MAX_OUTPUT_BYTES:
        raise SnapshotError("api_response_too_large")
    try:
        result = json.loads(proc.stdout)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SnapshotError("api_invalid_json") from error
    if not isinstance(result, dict):
        raise SnapshotError("api_invalid_shape")
    return result


def _api(transport: Callable[[list[str]], Any], host: str, query: str,
         *, owner: str | None = None, name: str | None = None,
         number: int | None = None, cursor: str | None = None,
         oid: str | None = None, thread_id: str | None = None) -> dict:
    argv = ["gh", "api", "--hostname", host, "graphql", "-f", "query=" + query]
    for key, value in (("owner", owner), ("name", name), ("cursor", cursor),
                       ("oid", oid), ("threadId", thread_id)):
        if value is not None:
            argv.extend(["-f", key + "=" + value])
    if number is not None:
        argv.extend(["-F", "number=" + str(number)])
    try:
        value = transport(argv)
    except SnapshotError:
        raise
    except (OSError, subprocess.SubprocessError) as error:
        raise SnapshotError("api_failed") from error
    if not isinstance(value, dict) or value.get("errors"):
        raise SnapshotError("api_partial_or_error")
    data = value.get("data")
    if not isinstance(data, dict):
        raise SnapshotError("api_missing_data")
    return data


def _pr(data: dict) -> dict:
    repo = data.get("repository")
    if not isinstance(repo, dict) or not isinstance(repo.get("pullRequest"), dict):
        raise SnapshotError("pr_missing")
    return repo["pullRequest"]


def _required(obj: dict, key: str, kind: type) -> Any:
    value = obj.get(key)
    if type(value) is not kind or (kind is str and not value):
        raise SnapshotError("missing_" + key)
    return value


def _metadata(transport: Callable[[list[str]], Any], host: str,
              owner: str, name: str, number: int) -> dict:
    pr = _pr(_api(transport, host, META_QUERY, owner=owner, name=name, number=number))
    result = {
        "id": _required(pr, "id", str),
        "number": _required(pr, "number", int),
        "url": _required(pr, "url", str),
        "state": _required(pr, "state", str),
        "is_draft": _required(pr, "isDraft", bool),
        "head_oid": _required(pr, "headRefOid", str),
        "base_oid": _required(pr, "baseRefOid", str),
        "head_ref": _required(pr, "headRefName", str),
        "base_ref": _required(pr, "baseRefName", str),
    }
    if result["number"] != number or not re.fullmatch(r"[0-9a-fA-F]{40}", result["head_oid"]):
        raise SnapshotError("pr_identity_invalid")
    if not re.fullmatch(r"[0-9a-fA-F]{40}", result["base_oid"]):
        raise SnapshotError("pr_base_invalid")
    return result


def _connection(obj: dict, key: str) -> tuple[list[dict], dict]:
    conn = obj.get(key)
    if not isinstance(conn, dict) or not isinstance(conn.get("nodes"), list):
        raise SnapshotError("missing_" + key + "_connection")
    info = conn.get("pageInfo")
    if not isinstance(info, dict) or type(info.get("hasNextPage")) is not bool:
        raise SnapshotError("missing_" + key + "_page_info")
    if any(not isinstance(node, dict) for node in conn["nodes"]):
        raise SnapshotError("invalid_" + key + "_node")
    return conn["nodes"], info


def _next_cursor(info: dict, seen: set[str], pages: int) -> str | None:
    if not info["hasNextPage"]:
        return None
    if pages >= MAX_PAGES:
        raise SnapshotError("pagination_limit")
    cursor = info.get("endCursor")
    if not isinstance(cursor, str) or not cursor or cursor in seen:
        raise SnapshotError("pagination_no_progress")
    seen.add(cursor)
    return cursor


def _author(node: dict) -> tuple[str | None, str | None]:
    author = node.get("author")
    if author is not None and not isinstance(author, dict):
        raise SnapshotError("invalid_comment_author")
    if author is None:
        return None, None
    login = _required(author, "login", str)
    actor_id = author.get("id")
    if actor_id is not None and (not isinstance(actor_id, str) or not actor_id):
        raise SnapshotError("invalid_author_id")
    return actor_id, login


def _comment(node: dict) -> dict:
    author_id, author_login = _author(node)
    # Deleted accounts can have a null author. Preserve that uncertainty.
    return {
        "id": _required(node, "id", str),
        "url": _required(node, "url", str),
        "created_at": _required(node, "createdAt", str),
        "author_id": author_id,
        "author_login": author_login,
    }


def _all_thread_comments(transport: Callable[[list[str]], Any], host: str,
                         thread_id: str, initial: dict) -> list[dict]:
    nodes, info = _connection({"comments": initial}, "comments")
    comments = [_comment(item) for item in nodes]
    seen_ids = {item["id"] for item in comments}
    if len(seen_ids) != len(comments):
        raise SnapshotError("comments_pagination_duplicate")
    cursors: set[str] = set()
    pages = 1
    while cursor := _next_cursor(info, cursors, pages):
        data = _api(transport, host, THREAD_COMMENTS_QUERY,
                    thread_id=thread_id, cursor=cursor)
        node = data.get("node")
        if not isinstance(node, dict) or node.get("id") != thread_id:
            raise SnapshotError("thread_changed_during_pagination")
        nodes, info = _connection(node, "comments")
        if not nodes:
            raise SnapshotError("comments_pagination_empty")
        for raw in nodes:
            item = _comment(raw)
            if item["id"] in seen_ids:
                raise SnapshotError("comments_pagination_duplicate")
            seen_ids.add(item["id"])
            comments.append(item)
        pages += 1
    return comments


def _issue_comments(transport: Callable[[list[str]], Any], host: str,
                    owner: str, name: str, number: int) -> list[dict]:
    result = []
    seen_ids: set[str] = set()
    cursors: set[str] = set()
    cursor = None
    pages = 0
    while True:
        data = _pr(_api(transport, host, ISSUE_COMMENTS_QUERY, owner=owner,
                        name=name, number=number, cursor=cursor))
        nodes, info = _connection(data, "comments")
        if pages and not nodes:
            raise SnapshotError("issue_comments_pagination_empty")
        for raw in nodes:
            item = _comment(raw)
            if item["id"] in seen_ids:
                raise SnapshotError("issue_comments_pagination_duplicate")
            seen_ids.add(item["id"])
            result.append(item)
        pages += 1
        cursor = _next_cursor(info, cursors, pages)
        if cursor is None:
            return result


def _threads(transport: Callable[[list[str]], Any], host: str,
             owner: str, name: str, number: int) -> list[dict]:
    result = []
    seen_ids: set[str] = set()
    cursors: set[str] = set()
    cursor = None
    pages = 0
    while True:
        data = _pr(_api(transport, host, THREADS_QUERY, owner=owner, name=name,
                        number=number, cursor=cursor))
        nodes, info = _connection(data, "reviewThreads")
        if pages and not nodes:
            raise SnapshotError("threads_pagination_empty")
        for raw in nodes:
            thread_id = _required(raw, "id", str)
            if thread_id in seen_ids:
                raise SnapshotError("threads_pagination_duplicate")
            seen_ids.add(thread_id)
            comments = raw.get("comments")
            if not isinstance(comments, dict):
                raise SnapshotError("missing_comments_connection")
            result.append({
                "id": thread_id,
                "is_resolved": _required(raw, "isResolved", bool),
                "is_outdated": _required(raw, "isOutdated", bool),
                "comments": _all_thread_comments(transport, host, thread_id, comments),
            })
        pages += 1
        cursor = _next_cursor(info, cursors, pages)
        if cursor is None:
            return result


def _reviews(transport: Callable[[list[str]], Any], host: str,
             owner: str, name: str, number: int) -> tuple[list[dict], list[dict], list[dict]]:
    all_reviews = []
    seen_ids: set[str] = set()
    cursors: set[str] = set()
    cursor = None
    pages = 0
    while True:
        data = _pr(_api(transport, host, REVIEWS_QUERY, owner=owner, name=name,
                        number=number, cursor=cursor))
        nodes, info = _connection(data, "reviews")
        if pages and not nodes:
            raise SnapshotError("reviews_pagination_empty")
        for raw in nodes:
            author_id, author_login = _author(raw)
            commit = raw.get("commit")
            item = {
                "id": _required(raw, "id", str),
                "url": _required(raw, "url", str),
                "state": _required(raw, "state", str),
                "created_at": _required(raw, "createdAt", str),
                "submitted_at": raw.get("submittedAt"),
                "author_id": author_id,
                "author_login": author_login,
                "commit_oid": _required(commit, "oid", str) if isinstance(commit, dict) else None,
            }
            if item["submitted_at"] is not None and not isinstance(item["submitted_at"], str):
                raise SnapshotError("review_time_invalid")
            if item["id"] in seen_ids:
                raise SnapshotError("reviews_pagination_duplicate")
            seen_ids.add(item["id"])
            all_reviews.append(item)
        pages += 1
        cursor = _next_cursor(info, cursors, pages)
        if cursor is None:
            break
    latest: dict[str, dict] = {}
    decisive: dict[str, dict] = {}
    for item in all_reviews:
        # An unknown deleted author cannot safely be grouped with another actor.
        if item["author_login"] is None:
            continue
        key = item["author_id"] or "login:" + item["author_login"].lower()
        marker = (item["submitted_at"] or item["created_at"], item["id"])
        previous = latest.get(key)
        if previous is None or marker > (previous["submitted_at"] or previous["created_at"], previous["id"]):
            latest[key] = item
        if item["state"] in {"APPROVED", "CHANGES_REQUESTED", "DISMISSED"}:
            previous = decisive.get(key)
            if previous is None or marker > (previous["submitted_at"] or previous["created_at"], previous["id"]):
                decisive[key] = item
    order = lambda item: item["author_login"].lower()
    return all_reviews, sorted(latest.values(), key=order), sorted(decisive.values(), key=order)


def _checks(transport: Callable[[list[str]], Any], host: str,
            owner: str, name: str, oid: str) -> tuple[list[dict], str]:
    result = []
    seen_ids: set[str] = set()
    cursors: set[str] = set()
    cursor = None
    pages = 0
    while True:
        data = _api(transport, host, CHECKS_QUERY, owner=owner, name=name,
                    oid=oid, cursor=cursor)
        repo = data.get("repository")
        obj = repo.get("object") if isinstance(repo, dict) else None
        if not isinstance(obj, dict) or obj.get("oid") != oid:
            raise SnapshotError("head_commit_missing_or_changed")
        rollup = obj.get("statusCheckRollup")
        if rollup is None:
            if pages:
                raise SnapshotError("checks_disappeared_during_pagination")
            return [], "none_observed"
        nodes, info = _connection(rollup, "contexts")
        if pages and not nodes:
            raise SnapshotError("checks_pagination_empty")
        for raw in nodes:
            kind = _required(raw, "__typename", str)
            item_id = _required(raw, "id", str)
            if item_id in seen_ids:
                raise SnapshotError("checks_pagination_duplicate")
            seen_ids.add(item_id)
            if kind == "CheckRun":
                item = {"kind": "check_run", "id": item_id,
                        "name": _required(raw, "name", str),
                        "status": _required(raw, "status", str),
                        "conclusion": raw.get("conclusion"),
                        "url": raw.get("detailsUrl")}
                if item["conclusion"] is not None and not isinstance(item["conclusion"], str):
                    raise SnapshotError("check_conclusion_invalid")
                if item["status"] == "COMPLETED" and not item["conclusion"]:
                    raise SnapshotError("completed_check_missing_conclusion")
            elif kind == "StatusContext":
                item = {"kind": "status_context", "id": item_id,
                        "name": _required(raw, "context", str),
                        "state": _required(raw, "state", str),
                        "url": raw.get("targetUrl")}
            else:
                raise SnapshotError("unknown_check_context_kind")
            if item["url"] is not None and not isinstance(item["url"], str):
                raise SnapshotError("check_url_invalid")
            result.append(item)
        pages += 1
        cursor = _next_cursor(info, cursors, pages)
        if cursor is None:
            return result, ("observed" if result else "none_observed")


def collect_snapshot(repo: str, number: int, host: str = "github.com",
                     transport: Callable[[list[str]], Any] | None = None) -> dict:
    """Collect provider facts; any uncertainty is explicit and never a ready verdict."""
    owner, name = _validate(repo, number, host)
    call = transport or _gh_transport
    result = {
        "schema_version": SCHEMA_VERSION,
        "provider": "github",
        "repo": repo,
        "number": number,
        "host": host,
        "complete": False,
        "stale": False,
        "pr_before": None,
        "pr_after": None,
        "threads": None,
        "issue_comments": None,
        "reviews": None,
        "latest_review_activity_by_author": None,
        "latest_decisive_review_by_author": None,
        "checks": None,
        "checks_observation": "unknown",
        "limits": ["required checks/branch protection and mergeability are not assessed",
                   "comment and review bodies are omitted; open their URLs to read feedback",
                   "deleted review authors remain ungrouped in raw reviews",
                   "check/review facts alone do not confer approval or merge authority"],
        "errors": [],
    }
    try:
        before = _metadata(call, host, owner, name, number)
        result["pr_before"] = before
        result["threads"] = _threads(call, host, owner, name, number)
        result["issue_comments"] = _issue_comments(call, host, owner, name, number)
        reviews, latest_activity, latest_decisive = _reviews(call, host, owner, name, number)
        result["reviews"] = reviews
        result["latest_review_activity_by_author"] = latest_activity
        result["latest_decisive_review_by_author"] = latest_decisive
        checks, observation = _checks(call, host, owner, name, before["head_oid"])
        result["checks"] = checks
        result["checks_observation"] = observation
        after = _metadata(call, host, owner, name, number)
        result["pr_after"] = after
        if before != after:
            result["stale"] = True
            result["errors"].append("pr_changed_during_capture")
        else:
            result["complete"] = True
    except SnapshotError as error:
        result["errors"].append(error.code)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--number", required=True, type=int)
    parser.add_argument("--host", default="github.com")
    args = parser.parse_args(argv)
    try:
        result = collect_snapshot(args.repo, args.number, args.host)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, sort_keys=True))
    return 0 if result["complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

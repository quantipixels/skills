"""Fixture transport tests; no live GitHub calls."""

from __future__ import annotations

import json
import subprocess
import unittest
from unittest import mock

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))
import pr_snapshot

SHA_A = "a" * 40
SHA_B = "b" * 40
SHA_C = "c" * 40


def connection(nodes: list[dict], *, more: bool = False, cursor: str | None = None) -> dict:
    return {"nodes": nodes, "pageInfo": {"hasNextPage": more, "endCursor": cursor}}


def comment(number: int) -> dict:
    return {"id": f"C{number}", "url": f"https://github.com/o/r/pull/7#comment-{number}",
            "createdAt": f"2026-01-01T00:{number % 60:02d}:00Z",
            "author": {"id": "U1", "login": "reviewer"}}


def thread(number: int, *, many_comments: bool = False) -> dict:
    comments = ([comment(index) for index in range(100)] if many_comments
                else [comment(number + 1000)])
    return {"id": f"T{number}", "isResolved": number % 2 == 0,
            "isOutdated": False,
            "comments": connection(comments, more=many_comments,
                                   cursor="comment-page" if many_comments else None)}


def review(number: int, *, author: str = "U1", state: str = "COMMENTED") -> dict:
    day, hour = divmod(number, 24)
    return {"id": f"R{number}", "url": f"https://github.com/o/r/pull/7#pullrequestreview-{number}",
            "state": state,
            "createdAt": f"2026-01-{day + 1:02d}T{hour:02d}:00:00Z",
            "submittedAt": f"2026-01-{day + 1:02d}T{hour:02d}:01:00Z",
            "author": {"id": author, "login": author.lower()},
            "commit": {"oid": SHA_A}}


def check(number: int) -> dict:
    return {"__typename": "CheckRun", "id": f"K{number}", "name": f"test-{number}",
            "status": "COMPLETED", "conclusion": "SUCCESS",
            "detailsUrl": f"https://github.com/o/r/actions/runs/{number}"}


def meta(head: str = SHA_A, base: str = SHA_B) -> dict:
    return {"data": {"repository": {"pullRequest": {
        "id": "PR7", "number": 7, "url": "https://github.com/o/r/pull/7",
        "state": "OPEN", "isDraft": False, "headRefOid": head,
        "baseRefOid": base, "headRefName": "feature", "baseRefName": "main",
    }}}}


def variables(argv: list[str]) -> dict[str, str]:
    return {arg.split("=", 1)[0]: arg.split("=", 1)[1]
            for arg in argv if "=" in arg and arg.split("=", 1)[0] in
            {"owner", "name", "number", "oid", "threadId", "cursor"}}


class FixtureTransport:
    def __init__(self, *, extensive: bool = False, change_head: bool = False,
                 empty: bool = False, error: bool = False, repeat_cursor: bool = False,
                 later_comment: bool = False, deleted_reviewer: bool = False,
                 duplicate_first_comments: bool = False, change_identity: bool = False):
        self.extensive = extensive
        self.change_head = change_head
        self.empty = empty
        self.error = error
        self.repeat_cursor = repeat_cursor
        self.later_comment = later_comment
        self.deleted_reviewer = deleted_reviewer
        self.duplicate_first_comments = duplicate_first_comments
        self.change_identity = change_identity
        self.calls: list[list[str]] = []
        self.meta_calls = 0

    def __call__(self, argv: list[str]) -> dict:
        self.calls.append(argv)
        if self.error:
            return {"errors": [{"message": "secret provider detail"}], "data": {}}
        self._assert_read_only(argv)
        query = argv[argv.index("-f") + 1].split("=", 1)[1]
        values = variables(argv)
        cursor = values.get("cursor")
        if "headRefOid baseRefOid" in query:
            self.meta_calls += 1
            head = SHA_C if self.change_head and self.meta_calls == 2 else SHA_A
            result = meta(head)
            if self.change_identity and self.meta_calls == 2:
                result["data"]["repository"]["pullRequest"]["id"] = "REPLACED"
            return result
        if "reviewThreads(" in query:
            if self.empty:
                nodes = []
                more = False
            elif cursor:
                nodes = [thread(100)]
                more = self.repeat_cursor
            else:
                nodes = [thread(index, many_comments=index == 0)
                         for index in range(100 if self.extensive else 1)]
                if self.duplicate_first_comments:
                    nodes[0]["comments"]["nodes"].append(nodes[0]["comments"]["nodes"][0])
                more = self.extensive
            return {"data": {"repository": {"pullRequest": {
                "reviewThreads": connection(nodes, more=more,
                                            cursor="thread-page" if more else None)}}}}
        if "node(id:$threadId)" in query:
            return {"data": {"node": {"id": values["threadId"],
                                      "comments": connection([comment(100)])}}}
        if "pullRequest(number:$number) {\n      comments(" in query:
            if self.empty:
                nodes = []
                more = False
            elif cursor:
                nodes = [comment(200)]
                more = False
            else:
                nodes = [comment(index + 300) for index in range(100 if self.extensive else 1)]
                more = self.extensive
            return {"data": {"repository": {"pullRequest": {
                "comments": connection(nodes, more=more,
                                       cursor="issue-page" if more else None)}}}}
        if "reviews(" in query:
            if self.empty:
                nodes = []
                more = False
            elif cursor:
                nodes = [review(100, state="CHANGES_REQUESTED")]
                more = False
            else:
                nodes = [review(index) for index in range(100 if self.extensive else 1)]
                if self.later_comment:
                    nodes[0] = review(0, state="APPROVED")
                    nodes.append(review(101, state="COMMENTED"))
                if self.deleted_reviewer:
                    nodes.append({**review(102), "author": None})
                more = self.extensive
            return {"data": {"repository": {"pullRequest": {
                "reviews": connection(nodes, more=more,
                                      cursor="review-page" if more else None)}}}}
        if "object(oid:$oid)" in query:
            if self.empty:
                rollup = None
            else:
                if cursor:
                    nodes = [{"__typename": "StatusContext", "id": "S1",
                              "context": "deploy", "state": "PENDING",
                              "targetUrl": "https://github.com/o/r/status/1"}]
                    more = False
                else:
                    nodes = [check(index) for index in range(100 if self.extensive else 1)]
                    more = self.extensive
                rollup = {"contexts": connection(nodes, more=more,
                                                 cursor="checks-page" if more else None)}
            return {"data": {"repository": {"object": {
                "oid": values["oid"], "statusCheckRollup": rollup}}}}
        raise AssertionError("unexpected query")

    @staticmethod
    def _assert_read_only(argv: list[str]) -> None:
        assert argv[:5] == ["gh", "api", "--hostname", "github.com", "graphql"]
        assert all(token not in argv for token in
                   ["mutation", "PATCH", "POST", "PUT", "DELETE", "merge", "reply"])


class SnapshotTests(unittest.TestCase):
    def test_all_pagination_including_nested_comments_and_exact_head_checks(self) -> None:
        fixture = FixtureTransport(extensive=True)
        result = pr_snapshot.collect_snapshot("o/r", 7, transport=fixture)
        self.assertTrue(result["complete"])
        self.assertFalse(result["stale"])
        self.assertEqual(101, len(result["threads"]))
        self.assertEqual(101, len(result["threads"][0]["comments"]))
        self.assertEqual(101, len(result["issue_comments"]))
        self.assertEqual(101, len(result["reviews"]))
        self.assertEqual("CHANGES_REQUESTED",
                         result["latest_decisive_review_by_author"][0]["state"])
        self.assertEqual("https://github.com/o/r/pull/7#pullrequestreview-100",
                         result["reviews"][-1]["url"])
        self.assertEqual(101, len(result["checks"]))
        self.assertEqual("status_context", result["checks"][-1]["kind"])
        check_calls = [variables(call) for call in fixture.calls
                       if "object(oid:$oid)" in next((part for part in call
                                                     if part.startswith("query=")), "")]
        self.assertTrue(check_calls)
        self.assertEqual({SHA_A}, {call["oid"] for call in check_calls})
        self.assertEqual(2, fixture.meta_calls)
        self.assertNotIn("body", json.dumps(result).lower())

    def test_head_change_mid_capture_is_stale(self) -> None:
        result = pr_snapshot.collect_snapshot("o/r", 7,
                                              transport=FixtureTransport(change_head=True))
        self.assertFalse(result["complete"])
        self.assertTrue(result["stale"])
        self.assertIn("pr_changed_during_capture", result["errors"])

    def test_empty_provider_results_are_not_green_or_ready(self) -> None:
        result = pr_snapshot.collect_snapshot("o/r", 7, transport=FixtureTransport(empty=True))
        self.assertTrue(result["complete"])
        self.assertEqual([], result["checks"])
        self.assertEqual("none_observed", result["checks_observation"])
        self.assertEqual([], result["reviews"])
        self.assertEqual([], result["threads"])
        self.assertEqual([], result["issue_comments"])
        self.assertNotIn("ready", json.dumps(result).lower())

    def test_partial_api_and_no_progress_fail_closed(self) -> None:
        errored = pr_snapshot.collect_snapshot("o/r", 7,
                                               transport=FixtureTransport(error=True))
        self.assertFalse(errored["complete"])
        self.assertEqual(["api_partial_or_error"], errored["errors"])
        self.assertNotIn("secret provider detail", json.dumps(errored))
        repeated = pr_snapshot.collect_snapshot(
            "o/r", 7, transport=FixtureTransport(extensive=True, repeat_cursor=True))
        self.assertFalse(repeated["complete"])
        self.assertIn("pagination_no_progress", repeated["errors"])

    def test_missing_gh_and_failed_cli_do_not_expose_stderr(self) -> None:
        with mock.patch.object(pr_snapshot.subprocess, "run",
                               side_effect=FileNotFoundError()):
            missing = pr_snapshot.collect_snapshot("o/r", 7)
        self.assertFalse(missing["complete"])
        self.assertEqual(["gh_missing"], missing["errors"])
        failed = subprocess.CompletedProcess(["gh"], 1, b"", b"token=super-secret")
        with mock.patch.object(pr_snapshot.subprocess, "run", return_value=failed):
            result = pr_snapshot.collect_snapshot("o/r", 7)
        self.assertEqual(["api_failed"], result["errors"])
        self.assertNotIn("super-secret", json.dumps(result))

    def test_missing_authoritative_fields_and_invalid_input(self) -> None:
        class MissingMeta:
            def __call__(self, argv):
                result = meta()
                del result["data"]["repository"]["pullRequest"]["baseRefOid"]
                return result
        result = pr_snapshot.collect_snapshot("o/r", 7, transport=MissingMeta())
        self.assertFalse(result["complete"])
        self.assertEqual(["missing_baseRefOid"], result["errors"])
        for repo, number, host in [("bad", 7, "github.com"),
                                   ("o/r", 0, "github.com"),
                                   ("o/r", 7, "bad..host")]:
            with self.assertRaises(ValueError):
                pr_snapshot.collect_snapshot(repo, number, host)

    def test_review_activity_does_not_erase_decisive_opinion_and_deleted_author(self) -> None:
        result = pr_snapshot.collect_snapshot(
            "o/r", 7, transport=FixtureTransport(later_comment=True,
                                                   deleted_reviewer=True))
        self.assertTrue(result["complete"])
        self.assertEqual("COMMENTED", result["latest_review_activity_by_author"][0]["state"])
        self.assertEqual("APPROVED", result["latest_decisive_review_by_author"][0]["state"])
        self.assertIsNone(result["reviews"][-1]["author_id"])

    def test_first_page_duplicate_and_identity_change_fail_closed(self) -> None:
        duplicate = pr_snapshot.collect_snapshot(
            "o/r", 7, transport=FixtureTransport(duplicate_first_comments=True))
        self.assertFalse(duplicate["complete"])
        self.assertIn("comments_pagination_duplicate", duplicate["errors"])
        identity = pr_snapshot.collect_snapshot(
            "o/r", 7, transport=FixtureTransport(change_identity=True))
        self.assertTrue(identity["stale"])
        self.assertFalse(identity["complete"])

    def test_exact_page_bound_is_allowed(self) -> None:
        self.assertIsNone(pr_snapshot._next_cursor(
            {"hasNextPage": False, "endCursor": None}, set(), pr_snapshot.MAX_PAGES))

    def test_queries_use_actor_node_fragment_and_documented_fields(self) -> None:
        # Actor exposes login, while id belongs to Node; fixture shape follows
        # the official GitHub GraphQL reference rather than the old invalid query.
        for query in (pr_snapshot.THREADS_QUERY, pr_snapshot.THREAD_COMMENTS_QUERY,
                      pr_snapshot.REVIEWS_QUERY, pr_snapshot.ISSUE_COMMENTS_QUERY):
            self.assertIn("author { login ... on Node { id } }", query)
            self.assertNotIn("author { id login }", query)
        self.assertIn("id url state", pr_snapshot.REVIEWS_QUERY)


if __name__ == "__main__":
    unittest.main()

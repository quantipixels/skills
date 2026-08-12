import unittest

from github_provider import GitHubProvider, normalize_checks, normalize_pr, normalize_review_items
from gitlab_provider import GitLabProvider, normalize_discussions, normalize_jobs, normalize_mr


class GitHubNormalizationTests(unittest.TestCase):
    def test_pr_identity_is_lossless(self):
        raw = {
            "number": 42,
            "url": "https://github.com/acme/widgets/pull/42",
            "state": "OPEN",
            "mergedAt": None,
            "closedAt": None,
            "baseRefName": "main",
            "baseRefOid": "base",
            "headRefName": "feature",
            "headRefOid": "head",
            "mergeable": "MERGEABLE",
            "reviewDecision": "REVIEW_REQUIRED",
        }
        result = normalize_pr(raw, host="github.com", repository="acme/widgets")
        self.assertEqual("head", result["head"]["sha"])
        self.assertEqual("REVIEW_REQUIRED", result["review_decision"])

    def test_checks_preserve_requiredness_and_unknown_states(self):
        checks = [
            {"name": "test", "state": "SUCCESS", "bucket": "pass", "workflow": "CI"},
            {"name": "optional", "state": "NEUTRAL", "bucket": "pass", "workflow": "CI"},
            {"name": "new", "state": "MYSTERY", "bucket": "pending", "workflow": "CI"},
        ]
        jobs = normalize_checks(checks, required_names={"test"})
        self.assertTrue(jobs[0]["required"])
        self.assertFalse(jobs[1]["required"])
        self.assertEqual("unknown", jobs[2]["status"])

    def test_pending_reviews_are_not_published_items(self):
        reviews = [
            {"id": 1, "state": "PENDING", "body": "draft", "user": {"login": "a"}},
            {"id": 2, "state": "COMMENTED", "body": "published", "user": {"login": "b"}},
        ]
        items = normalize_review_items([], [], reviews)
        self.assertEqual(["review:2"], [item["id"] for item in items])

    def test_resolved_inline_comments_are_not_actionable(self):
        comments = [{"id": 8, "body": "done", "user": {"login": "a"}}]
        items = normalize_review_items([], comments, [], resolution_by_comment={8: True})
        self.assertEqual([], items)

    def test_inline_comments_with_unknown_resolution_are_not_assumed_unresolved(self):
        comments = [{"id": 8, "body": "unknown", "user": {"login": "a"}}]
        self.assertEqual([], normalize_review_items([], comments, []))

    def test_enterprise_commands_use_a_host_qualified_repository(self):
        commands = []

        def runner(command):
            commands.append(command)
            if command[:3] == ["gh", "pr", "view"]:
                return {
                    "number": 42, "url": "https://github.acme.test/acme/widgets/pull/42",
                    "state": "OPEN", "headRefOid": "head",
                }
            if "graphql" in command:
                return {"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": [], "pageInfo": {"hasNextPage": False}}}}}}
            return []

        GitHubProvider(host="github.acme.test", repository="acme/widgets", runner=runner).fetch("42")
        pr_commands = [command for command in commands if command[:3] in (["gh", "pr", "view"], ["gh", "pr", "checks"])]
        self.assertTrue(pr_commands)
        for command in pr_commands:
            self.assertEqual("github.acme.test/acme/widgets", command[command.index("--repo") + 1])


class GitLabNormalizationTests(unittest.TestCase):
    def test_mr_identity_preserves_diff_refs(self):
        raw = {
            "iid": 9,
            "web_url": "https://gitlab.com/acme/widgets/-/merge_requests/9",
            "state": "opened",
            "merged_at": None,
            "closed_at": None,
            "source_branch": "feature",
            "target_branch": "main",
            "sha": "head",
            "diff_refs": {"base_sha": "base", "head_sha": "head", "start_sha": "start"},
            "detailed_merge_status": "mergeable",
            "draft": False,
        }
        result = normalize_mr(raw, host="gitlab.com", repository="acme/widgets")
        self.assertEqual("base", result["base"]["sha"])
        self.assertEqual("head", result["head"]["sha"])
        self.assertEqual("start", result["diff_refs"]["start_sha"])

    def test_allowed_failure_and_manual_are_preserved(self):
        jobs = normalize_jobs([
            {"id": 1, "name": "test", "status": "success", "allow_failure": False},
            {"id": 2, "name": "lint", "status": "failed", "allow_failure": True},
            {"id": 3, "name": "deploy", "status": "manual", "allow_failure": False},
        ])
        self.assertTrue(jobs[1]["allow_failure"])
        self.assertEqual("manual", jobs[2]["status"])

    def test_discussions_keep_resolution_and_note_identity(self):
        discussions = [{
            "id": "d1",
            "resolved": False,
            "notes": [{"id": 5, "body": "Please fix", "system": False, "author": {"username": "reviewer"}}],
        }]
        items = normalize_discussions(discussions)
        self.assertEqual("discussion:d1:note:5", items[0]["id"])
        self.assertFalse(items[0]["resolved"])

    def test_resolved_discussions_are_not_actionable_items(self):
        discussions = [{
            "id": "d1",
            "resolved": True,
            "notes": [{"id": 5, "body": "Done", "system": False, "author": {"username": "reviewer"}}],
        }]
        self.assertEqual([], normalize_discussions(discussions))

    def test_fetch_uses_head_pipeline_instead_of_newest_unrelated_pipeline(self):
        responses = {
            "projects/acme%2Fwidgets/merge_requests/9": {
                "iid": 9,
                "web_url": "https://gitlab.com/acme/widgets/-/merge_requests/9",
                "state": "opened",
                "source_branch": "feature",
                "target_branch": "main",
                "sha": "head",
                "diff_refs": {"base_sha": "base", "head_sha": "head", "start_sha": "start"},
                "head_pipeline": {"id": 10, "sha": "head"},
            },
            "projects/acme%2Fwidgets/merge_requests/9/pipelines?per_page=100&page=1": [
                {"id": 11, "sha": "other"}, {"id": 10, "sha": "head"}
            ],
            "projects/acme%2Fwidgets/pipelines/10/jobs?include_retried=true&per_page=100&page=1": [
                {"id": 1, "name": "test", "status": "success", "allow_failure": False}
            ],
            "projects/acme%2Fwidgets/merge_requests/9/discussions?per_page=100&page=1": [],
            "projects/acme%2Fwidgets/merge_requests/9/approvals": {"approved": False},
        }

        def runner(command):
            return responses[command[-1]]

        snapshot = GitLabProvider(repository="acme/widgets", runner=runner).fetch("9")
        self.assertEqual(10, snapshot["pipeline"]["pipeline_id"])
        self.assertEqual("test", snapshot["pipeline"]["jobs"][0]["name"])

    def test_fetch_keeps_latest_retried_job_attempt(self):
        responses = self._fetch_responses()
        responses["projects/acme%2Fwidgets/pipelines/10/jobs?include_retried=true&per_page=100&page=1"] = [
            {"id": 1, "name": "test", "stage": "verify", "status": "failed", "allow_failure": False},
            {"id": 2, "name": "test", "stage": "verify", "status": "success", "allow_failure": False},
        ]
        snapshot = GitLabProvider(repository="acme/widgets", runner=lambda command: responses[command[-1]]).fetch("9")
        self.assertEqual([2], [job["id"] for job in snapshot["pipeline"]["jobs"]])

    def test_approval_read_failure_does_not_corrupt_pipeline_evidence(self):
        from gitlab_provider import CommandError

        responses = self._fetch_responses()

        def runner(command):
            if command[-1].endswith("/approvals"):
                raise CommandError("approval endpoint unavailable")
            return responses[command[-1]]

        snapshot = GitLabProvider(repository="acme/widgets", runner=runner).fetch("9")
        self.assertTrue(snapshot["pipeline"]["evidence_complete"])
        self.assertFalse(snapshot["capabilities"]["approval_state"])

    @staticmethod
    def _fetch_responses():
        return {
            "projects/acme%2Fwidgets/merge_requests/9": {
                "iid": 9, "web_url": "https://gitlab.com/acme/widgets/-/merge_requests/9",
                "state": "opened", "source_branch": "feature", "target_branch": "main",
                "sha": "head", "diff_refs": {"base_sha": "base", "head_sha": "head"},
                "head_pipeline": {"id": 10, "sha": "head"},
            },
            "projects/acme%2Fwidgets/merge_requests/9/pipelines?per_page=100&page=1": [{"id": 10, "sha": "head"}],
            "projects/acme%2Fwidgets/pipelines/10/jobs?include_retried=true&per_page=100&page=1": [
                {"id": 1, "name": "test", "stage": "verify", "status": "success", "allow_failure": False}
            ],
            "projects/acme%2Fwidgets/merge_requests/9/discussions?per_page=100&page=1": [],
            "projects/acme%2Fwidgets/merge_requests/9/approvals": {"approved": False},
        }


if __name__ == "__main__":
    unittest.main()

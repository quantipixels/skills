import json
import os
import subprocess
import unittest
from unittest.mock import patch

from github_provider import (
    CommandError as GitHubCommandError,
    GitHubProvider,
    normalize_checks,
    normalize_pr,
    normalize_review_items,
)
from gitlab_provider import (
    CommandError,
    GitLabProvider,
    normalize_discussions,
    normalize_jobs,
    normalize_mr,
    normalize_trigger_jobs,
)


def is_github_pr_command(command, action):
    return "pr" in command and command[command.index("pr"):command.index("pr") + 2] == [
        "pr", action,
    ]


class GitHubNormalizationTests(unittest.TestCase):
    def test_auto_target_resolves_current_branch_before_pinned_repo_read(self):
        commands = []

        def runner(command):
            commands.append(command)
            if is_github_pr_command(command, "view"):
                return {
                    "number": 42,
                    "url": "https://github.com/acme/widgets/pull/42",
                    "state": "OPEN",
                    "headRefOid": "head",
                }
            if "graphql" in command:
                return {
                    "data": {"repository": {"pullRequest": {"reviewThreads": {
                        "nodes": [], "pageInfo": {"hasNextPage": False},
                    }}}}
                }
            return []

        completed = subprocess.CompletedProcess(
            ["git", "branch", "--show-current"], 0, "feature/watch\n", ""
        )
        with patch("github_provider.subprocess.run", return_value=completed):
            GitHubProvider(repository="acme/widgets", runner=runner).fetch("auto")

        view = next(command for command in commands if is_github_pr_command(command, "view"))
        self.assertEqual(["gh", "--repo", "acme/widgets", "pr", "view", "feature/watch"], view[:6])

    def test_transient_thread_read_failure_propagates_to_watch_backoff(self):
        def runner(command):
            if is_github_pr_command(command, "view"):
                return {
                    "number": 42,
                    "url": "https://github.com/acme/widgets/pull/42",
                    "state": "OPEN",
                    "headRefOid": "head",
                }
            if "graphql" in command:
                raise GitHubCommandError("temporary GraphQL failure")
            return []

        with self.assertRaisesRegex(GitHubCommandError, "temporary GraphQL failure"):
            GitHubProvider(repository="acme/widgets", runner=runner).fetch("42")

    def test_fetch_accepts_valid_check_json_when_gh_returns_one(self):
        """`gh pr checks` uses exit 1 to report non-success check buckets."""
        checks = [{"name": "test", "state": "SUCCESS", "bucket": "pass", "workflow": "CI"}]

        def run(command, **_kwargs):
            if is_github_pr_command(command, "view"):
                payload = {"number": 42, "url": "https://github.com/acme/widgets/pull/42", "state": "OPEN"}
            elif is_github_pr_command(command, "checks"):
                payload = checks
            elif "graphql" in command:
                payload = {"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": [], "pageInfo": {}}}}}}
            else:
                payload = []
            return subprocess.CompletedProcess(command, 1 if is_github_pr_command(command, "checks") else 0, json.dumps(payload), "")

        with patch("github_provider.subprocess.run", side_effect=run):
            result = GitHubProvider(repository="acme/widgets").fetch("42")

        self.assertTrue(result["pipeline"]["evidence_complete"])
        self.assertTrue(result["pipeline"]["jobs"][0]["required"])

    def test_empty_exit_one_required_check_read_is_not_accepted(self):
        def run(command, **_kwargs):
            if is_github_pr_command(command, "view"):
                payload = {"number": 42, "url": "https://github.com/acme/widgets/pull/42", "state": "OPEN"}
                return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")
            if is_github_pr_command(command, "checks") and "--required" in command:
                return subprocess.CompletedProcess(command, 1, "", "API failure")
            if is_github_pr_command(command, "checks"):
                payload = [{"name": "test", "state": "FAILURE", "link": "https://example.test/check/1"}]
                return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")
            return subprocess.CompletedProcess(command, 0, "[]", "")

        with patch("github_provider.subprocess.run", side_effect=run):
            with self.assertRaises(GitHubCommandError):
                GitHubProvider(repository="acme/widgets").fetch("42")

    def test_known_no_required_checks_exit_one_is_valid_empty_evidence(self):
        def run(command, **_kwargs):
            if is_github_pr_command(command, "view"):
                payload = {"number": 42, "url": "https://github.com/acme/widgets/pull/42", "state": "OPEN"}
                return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")
            if is_github_pr_command(command, "checks") and "--required" in command:
                return subprocess.CompletedProcess(
                    command, 1, "", "no required checks reported on the 'feature/watch' branch"
                )
            if is_github_pr_command(command, "checks"):
                payload = [{"name": "preview", "state": "FAILURE", "link": "https://example.test/check/1"}]
                return subprocess.CompletedProcess(command, 1, json.dumps(payload), "")
            if "graphql" in command:
                payload = {"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": []}}}}}
                return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")
            return subprocess.CompletedProcess(command, 0, "[]", "")

        with patch("github_provider.subprocess.run", side_effect=run):
            result = GitHubProvider(repository="acme/widgets").fetch("42")

        self.assertTrue(result["pipeline"]["evidence_complete"])
        self.assertFalse(result["pipeline"]["jobs"][0]["required"])

    def test_known_no_checks_exit_one_is_valid_empty_evidence(self):
        def run(command, **_kwargs):
            if is_github_pr_command(command, "view"):
                payload = {"number": 42, "url": "https://github.com/acme/widgets/pull/42", "state": "OPEN"}
                return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")
            if is_github_pr_command(command, "checks"):
                message = (
                    "no required checks reported on the 'feature/watch' branch"
                    if "--required" in command
                    else "no checks reported on the 'feature/watch' branch"
                )
                return subprocess.CompletedProcess(command, 1, "", message)
            if "graphql" in command:
                payload = {"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": []}}}}}
                return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")
            return subprocess.CompletedProcess(command, 0, "[]", "")

        with patch("github_provider.subprocess.run", side_effect=run):
            result = GitHubProvider(repository="acme/widgets").fetch("42")

        self.assertTrue(result["pipeline"]["evidence_complete"])
        self.assertEqual([], result["pipeline"]["jobs"])

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
        jobs = normalize_checks(checks, required_identities={("name-workflow", "test", "CI")})
        self.assertTrue(jobs[0]["required"])
        self.assertFalse(jobs[1]["required"])
        self.assertEqual("unknown", jobs[2]["status"])

    def test_checks_use_job_link_as_identity_when_no_provider_id_exists(self):
        jobs = normalize_checks(
            [{"name": "test", "state": "SUCCESS", "link": "https://github.com/acme/widgets/runs/123"}],
            required_identities={("link", "https://github.com/acme/widgets/runs/123")},
        )
        self.assertEqual("https://github.com/acme/widgets/runs/123", jobs[0]["id"])

    def test_same_named_checks_match_requiredness_by_row_identity(self):
        checks = [
            {"name": "test", "state": "SUCCESS", "link": "https://example.test/check/required"},
            {"name": "test", "state": "FAILURE", "link": "https://example.test/check/optional"},
        ]
        jobs = normalize_checks(
            checks,
            required_identities={("link", "https://example.test/check/required")},
        )
        self.assertTrue(jobs[0]["required"])
        self.assertFalse(jobs[1]["required"])

    def test_pending_reviews_are_not_published_items(self):
        reviews = [
            {"id": 1, "state": "PENDING", "body": "draft", "user": {"login": "a"}},
            {"id": 2, "state": "COMMENTED", "body": "published", "user": {"login": "b"}},
        ]
        items = normalize_review_items([], [], reviews)
        self.assertEqual(["review:2"], [item["id"] for item in items])

    def test_empty_review_summaries_are_not_actionable_items(self):
        inline_comments = [{
            "id": 8,
            "body": "Please fix the boundary",
            "user": {"login": "reviewer"},
        }]
        reviews = [
            {"id": 1, "state": "COMMENTED", "body": "", "user": {"login": "a"}},
            {"id": 2, "state": "APPROVED", "body": "   ", "user": {"login": "b"}},
            {"id": 3, "state": "COMMENTED", "body": "Please fix this", "user": {"login": "c"}},
        ]

        items = normalize_review_items(
            [], inline_comments, reviews, resolution_by_comment={8: False}
        )

        self.assertEqual(["comment:8", "review:3"], [item["id"] for item in items])

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
            if is_github_pr_command(command, "view"):
                return {
                    "number": 42, "url": "https://github.acme.test/acme/widgets/pull/42",
                    "state": "OPEN", "headRefOid": "head",
                }
            if "graphql" in command:
                return {"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": [], "pageInfo": {"hasNextPage": False}}}}}}
            return []

        GitHubProvider(
            host="github.acme.test",
            repository="acme/widgets",
            runner=runner,
            trusted_hosts={"github.acme.test"},
        ).fetch("42")
        pr_commands = [
            command for command in commands
            if is_github_pr_command(command, "view") or is_github_pr_command(command, "checks")
        ]
        self.assertTrue(pr_commands)
        for command in pr_commands:
            self.assertEqual("github.acme.test/acme/widgets", command[command.index("--repo") + 1])

    def test_untrusted_github_host_is_rejected_before_provider_contact(self):
        with patch("github_provider.subprocess.run") as run, self.assertRaisesRegex(
            ValueError, "separate trust is required"
        ):
            GitHubProvider(host="untrusted.test", repository="acme/widgets", trusted_hosts=set())

        run.assert_not_called()

    def test_explicitly_trusted_github_host_keeps_enterprise_token(self):
        environments = []

        def run(command, **kwargs):
            environments.append(kwargs["env"])
            if is_github_pr_command(command, "view"):
                payload = {"number": 42, "url": "https://github.acme.test/acme/widgets/pull/42", "state": "OPEN"}
            elif "graphql" in command:
                payload = {"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": [], "pageInfo": {}}}}}}
            else:
                payload = []
            return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")

        with patch.dict(os.environ, {"GH_ENTERPRISE_TOKEN": "enterprise-token"}, clear=True), patch(
            "github_provider.subprocess.run", side_effect=run
        ):
            GitHubProvider(
                host="github.acme.test", repository="acme/widgets", trusted_hosts={"github.acme.test"}
            ).fetch("42")

        self.assertTrue(all(environment["GH_ENTERPRISE_TOKEN"] == "enterprise-token" for environment in environments))

    def test_github_commands_pin_declared_host_and_remove_ambient_repo(self):
        environments = []

        def run(command, **kwargs):
            environments.append(kwargs["env"])
            if is_github_pr_command(command, "view"):
                payload = {
                    "number": 42,
                    "url": "https://github.com/acme/widgets/pull/42",
                    "state": "OPEN",
                }
            elif "graphql" in command:
                payload = {
                    "data": {"repository": {"pullRequest": {"reviewThreads": {
                        "nodes": [], "pageInfo": {"hasNextPage": False}
                    }}}}
                }
            else:
                payload = []
            return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")

        with patch.dict(
            os.environ,
            {"GH_HOST": "attacker.test", "GH_REPO": "attacker.test/acme/api", "GH_TOKEN": "token"},
            clear=True,
        ), patch("github_provider.subprocess.run", side_effect=run):
            GitHubProvider(repository="acme/widgets").fetch("42")

        self.assertTrue(environments)
        for environment in environments:
            self.assertEqual("github.com", environment["GH_HOST"])
            self.assertNotIn("GH_REPO", environment)


class GitLabNormalizationTests(unittest.TestCase):
    def test_repository_discovery_pins_gitlab_host_and_removes_ambient_override(self):
        environments = []

        def run(command, **kwargs):
            environments.append((command, kwargs["env"]))
            if command[:2] == ["glab", "api"] and command[-1] == "projects/:fullpath":
                payload = {"path_with_namespace": "acme/widgets"}
            else:
                payload = self._fetch_responses()[command[-1]]
            return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")

        with patch.dict(
            os.environ,
            {"GITLAB_HOST": "attacker.test", "GITLAB_TOKEN": "token"},
            clear=True,
        ), patch("gitlab_provider.subprocess.run", side_effect=run):
            GitLabProvider().fetch("9")

        repo_command, repo_environment = environments[0]
        self.assertEqual(["glab", "api"], repo_command[:2])
        self.assertEqual("gitlab.com", repo_command[repo_command.index("--hostname") + 1])
        self.assertEqual("projects/:fullpath", repo_command[-1])
        self.assertNotIn("GITLAB_HOST", repo_environment)

    def test_mr_url_with_query_or_fragment_resolves_iid(self):
        provider = GitLabProvider(repository="acme/widgets", runner=lambda _command: [])

        self.assertEqual(9, provider._iid(
            "https://gitlab.com/acme/widgets/-/merge_requests/9?diff_id=2", "acme/widgets"
        ))
        self.assertEqual(9, provider._iid(
            "https://gitlab.com/acme/widgets/-/merge_requests/9#note_1", "acme/widgets"
        ))

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

    def test_skipped_gitlab_job_is_non_blocking(self):
        jobs = normalize_jobs([
            {"id": 1, "name": "failure-report", "status": "skipped", "allow_failure": False},
        ])

        self.assertFalse(jobs[0]["required"])
        self.assertEqual("skipped", jobs[0]["status"])

    def test_trigger_job_tracks_the_downstream_pipeline_status(self):
        jobs = normalize_trigger_jobs([{
            "id": 7,
            "name": "downstream",
            "stage": "deploy",
            "status": "success",
            "allow_failure": False,
            "downstream_pipeline": {
                "id": 70,
                "status": "running",
                "web_url": "https://gitlab.com/acme/downstream/-/pipelines/70",
            },
        }])

        self.assertEqual("running", jobs[0]["status"])
        self.assertTrue(jobs[0]["required"])
        self.assertEqual("trigger:7", jobs[0]["id"])

    def test_failed_trigger_job_is_not_masked_by_a_downstream_pipeline(self):
        jobs = normalize_trigger_jobs([{
            "id": 8,
            "name": "downstream",
            "status": "failed",
            "allow_failure": False,
            "downstream_pipeline": {"id": 80, "status": "success"},
        }])

        self.assertEqual("failure", jobs[0]["status"])

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
            "projects/acme%2Fwidgets/pipelines/10/trigger_jobs?per_page=100&page=1": [{
                "id": 7,
                "name": "downstream",
                "status": "success",
                "allow_failure": False,
                "downstream_pipeline": {"id": 70, "status": "running"},
            }],
            "projects/acme%2Fwidgets/merge_requests/9/discussions?per_page=100&page=1": [],
            "projects/acme%2Fwidgets/merge_requests/9/approvals": {"approved": False},
        }

        def runner(command):
            return responses[command[-1]]

        snapshot = GitLabProvider(repository="acme/widgets", runner=runner).fetch("9")
        self.assertEqual(10, snapshot["pipeline"]["pipeline_id"])
        self.assertEqual("test", snapshot["pipeline"]["jobs"][0]["name"])
        self.assertEqual("running", snapshot["pipeline"]["jobs"][1]["status"])

    def test_fetch_keeps_latest_retried_job_attempt(self):
        responses = self._fetch_responses()
        responses["projects/acme%2Fwidgets/pipelines/10/jobs?include_retried=true&per_page=100&page=1"] = [
            {"id": 1, "name": "test", "stage": "verify", "status": "failed", "allow_failure": False},
            {"id": 2, "name": "test", "stage": "verify", "status": "success", "allow_failure": False},
        ]
        snapshot = GitLabProvider(repository="acme/widgets", runner=lambda command: responses[command[-1]]).fetch("9")
        self.assertEqual([2], [job["id"] for job in snapshot["pipeline"]["jobs"]])

    def test_fetch_falls_back_to_legacy_bridge_endpoint(self):
        responses = self._fetch_responses()
        responses["projects/acme%2Fwidgets/pipelines/10/bridges?per_page=100&page=1"] = [{
            "id": 7,
            "name": "downstream",
            "status": "success",
            "allow_failure": False,
            "downstream_pipeline": {"id": 70, "status": "failed"},
        }]

        def runner(command):
            if "/trigger_jobs?" in command[-1]:
                raise CommandError("endpoint unavailable")
            return responses[command[-1]]

        snapshot = GitLabProvider(repository="acme/widgets", runner=runner).fetch("9")

        self.assertEqual("failure", snapshot["pipeline"]["jobs"][1]["status"])
        self.assertTrue(snapshot["pipeline"]["evidence_complete"])

    def test_empty_running_head_pipeline_is_reported_as_pending_work(self):
        responses = self._fetch_responses()
        responses["projects/acme%2Fwidgets/merge_requests/9"]["head_pipeline"]["status"] = "running"
        responses[
            "projects/acme%2Fwidgets/pipelines/10/jobs?include_retried=true&per_page=100&page=1"
        ] = []

        snapshot = GitLabProvider(
            repository="acme/widgets", runner=lambda command: responses[command[-1]]
        ).fetch("9")

        self.assertEqual("running", snapshot["pipeline"]["jobs"][0]["status"])
        self.assertEqual("pipeline:10", snapshot["pipeline"]["jobs"][0]["id"])
        self.assertTrue(snapshot["pipeline"]["evidence_complete"])

    def test_transient_approval_read_failure_propagates_to_watch_backoff(self):
        responses = self._fetch_responses()

        def runner(command):
            if command[-1].endswith("/approvals"):
                raise CommandError("temporary approval read failure")
            return responses[command[-1]]

        with self.assertRaisesRegex(CommandError, "temporary approval read failure"):
            GitLabProvider(repository="acme/widgets", runner=runner).fetch("9")

    def test_fetch_marks_pipeline_incomplete_when_trigger_evidence_is_unavailable(self):
        responses = self._fetch_responses()

        def runner(command):
            if "/trigger_jobs?" in command[-1] or "/bridges?" in command[-1]:
                raise CommandError("endpoint unavailable")
            return responses[command[-1]]

        snapshot = GitLabProvider(repository="acme/widgets", runner=runner).fetch("9")

        self.assertFalse(snapshot["pipeline"]["evidence_complete"])
        self.assertIn("trigger job evidence unavailable", snapshot["errors"])

    def test_untrusted_gitlab_host_is_rejected_before_provider_contact(self):
        with patch("gitlab_provider.subprocess.run") as run, self.assertRaisesRegex(
            ValueError, "separate trust is required"
        ):
            GitLabProvider(
                host="untrusted.test", repository="acme/widgets", trusted_hosts=set()
            )

        run.assert_not_called()

    def test_explicitly_trusted_gitlab_host_keeps_access_token(self):
        environments = []
        responses = self._fetch_responses(host="gitlab.acme.test")

        def run(command, **kwargs):
            environments.append(kwargs["env"])
            payload = responses[command[-1]]
            return subprocess.CompletedProcess(command, 0, json.dumps(payload), "")

        with patch.dict(os.environ, {"GITLAB_ACCESS_TOKEN": "access-token"}, clear=True), patch(
            "gitlab_provider.subprocess.run", side_effect=run
        ):
            GitLabProvider(
                host="gitlab.acme.test",
                repository="acme/widgets",
                trusted_hosts={"gitlab.acme.test"},
            ).fetch("9")

        self.assertTrue(
            all(environment["GITLAB_ACCESS_TOKEN"] == "access-token" for environment in environments)
        )

    @staticmethod
    def _fetch_responses(host="gitlab.com"):
        return {
            "projects/acme%2Fwidgets/merge_requests/9": {
                "iid": 9, "web_url": f"https://{host}/acme/widgets/-/merge_requests/9",
                "state": "opened", "source_branch": "feature", "target_branch": "main",
                "sha": "head", "diff_refs": {"base_sha": "base", "head_sha": "head"},
                "head_pipeline": {"id": 10, "sha": "head"},
            },
            "projects/acme%2Fwidgets/merge_requests/9/pipelines?per_page=100&page=1": [{"id": 10, "sha": "head"}],
            "projects/acme%2Fwidgets/pipelines/10/jobs?include_retried=true&per_page=100&page=1": [
                {"id": 1, "name": "test", "stage": "verify", "status": "success", "allow_failure": False}
            ],
            "projects/acme%2Fwidgets/pipelines/10/trigger_jobs?per_page=100&page=1": [],
            "projects/acme%2Fwidgets/merge_requests/9/discussions?per_page=100&page=1": [],
            "projects/acme%2Fwidgets/merge_requests/9/approvals": {"approved": False},
        }


if __name__ == "__main__":
    unittest.main()

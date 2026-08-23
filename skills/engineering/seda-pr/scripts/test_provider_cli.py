import subprocess
import unittest
from io import StringIO
from unittest.mock import patch

from provider_cli import (
    command_environment,
    main,
    validate_command_host,
    validate_publication_state,
)


class ProviderCliTests(unittest.TestCase):
    def test_untrusted_github_host_is_rejected_before_environment_creation(self):
        with self.assertRaisesRegex(ValueError, "separate trust is required"):
            command_environment(
                "github", "attacker.test", trusted_hosts=set(), environment={"PATH": "/bin"}
            )

    def test_untrusted_gitlab_host_is_rejected_before_environment_creation(self):
        with self.assertRaisesRegex(ValueError, "separate trust is required"):
            command_environment(
                "gitlab", "attacker.test", trusted_hosts=set(), environment={"PATH": "/bin"}
            )

    def test_trusted_custom_github_host_strips_ambient_tokens(self):
        environment = command_environment(
            "github",
            "github.acme.test.",
            trusted_hosts={"GITHUB.ACME.TEST"},
            environment={
                "GH_TOKEN": "public-token",
                "GITHUB_TOKEN": "public-token-2",
                "GH_ENTERPRISE_TOKEN": "enterprise-token",
                "GITHUB_ENTERPRISE_TOKEN": "enterprise-token-2",
            },
        )

        for name in (
            "GH_TOKEN",
            "GITHUB_TOKEN",
            "GH_ENTERPRISE_TOKEN",
            "GITHUB_ENTERPRISE_TOKEN",
        ):
            self.assertNotIn(name, environment)

    def test_trusted_custom_gitlab_host_strips_ambient_tokens_and_ci_autologin(self):
        environment = command_environment(
            "gitlab",
            "gitlab.acme.test",
            trusted_hosts={"gitlab.acme.test"},
            environment={
                "GITLAB_TOKEN": "token",
                "GITLAB_ACCESS_TOKEN": "access-token",
                "OAUTH_TOKEN": "oauth-token",
                "CI_JOB_TOKEN": "job-token",
                "GLAB_ENABLE_CI_AUTOLOGIN": "true",
            },
        )

        for name in ("GITLAB_TOKEN", "GITLAB_ACCESS_TOKEN", "OAUTH_TOKEN", "CI_JOB_TOKEN"):
            self.assertNotIn(name, environment)
        self.assertEqual("false", environment["GLAB_ENABLE_CI_AUTOLOGIN"])

    def test_github_environment_pins_declared_host_and_removes_repo_override(self):
        environment = command_environment(
            "github",
            "github.com",
            trusted_hosts=set(),
            environment={
                "GH_HOST": "attacker.test",
                "GH_REPO": "attacker.test/acme/api",
                "GH_TOKEN": "token",
                "GH_ENTERPRISE_TOKEN": "enterprise-token",
            },
        )

        self.assertEqual("github.com", environment["GH_HOST"])
        self.assertNotIn("GH_REPO", environment)
        self.assertEqual("token", environment["GH_TOKEN"])
        self.assertNotIn("GH_ENTERPRISE_TOKEN", environment)

    def test_gitlab_environment_disables_ci_autologin_and_drops_ci_job_token(self):
        environment = command_environment(
            "gitlab",
            "gitlab.com",
            trusted_hosts=set(),
            environment={
                "GITLAB_TOKEN": "token",
                "CI_JOB_TOKEN": "job-token",
                "GLAB_ENABLE_CI_AUTOLOGIN": "true",
            },
        )

        self.assertEqual("token", environment["GITLAB_TOKEN"])
        self.assertNotIn("CI_JOB_TOKEN", environment)
        self.assertEqual("false", environment["GLAB_ENABLE_CI_AUTOLOGIN"])

    def test_github_command_must_select_a_repository_or_hostname(self):
        with self.assertRaisesRegex(ValueError, "must select the declared host"):
            validate_command_host("github", "github.com", ["gh", "pr", "view", "7"])

        validate_command_host(
            "github", "github.com", ["gh", "pr", "view", "7", "-R", "owner/repo"]
        )

    def test_gitlab_command_requires_an_explicit_host_selector(self):
        with self.assertRaisesRegex(ValueError, "must select the declared host"):
            validate_command_host(
                "gitlab", "gitlab.com", ["glab", "mr", "view", "7", "-R", "group/repo"]
            )

    def test_content_url_cannot_supply_host_evidence(self):
        commands = [
            ("github", "github.com", ["gh", "pr", "edit", "7", "--body", "https://github.com"]),
            (
                "gitlab", "gitlab.com",
                ["glab", "mr", "update", "7", "--description", "https://gitlab.com"],
            ),
        ]
        for provider, host, command in commands:
            with self.subTest(command=command), self.assertRaisesRegex(
                ValueError, "must select the declared host"
            ):
                validate_command_host(provider, host, command)

    def test_attached_repo_selector_cannot_hide_a_host_mismatch(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            validate_command_host(
                "github",
                "github.com",
                ["gh", "pr", "edit", "7", "-Rattacker.test/acme/api", "--body", "text"],
            )

    def test_main_rejects_untrusted_host_before_provider_cli(self):
        with patch("provider_cli.subprocess.run") as run, self.assertRaisesRegex(
            ValueError, "separate trust is required"
        ):
            main([
                "--provider", "github",
                "--host", "attacker.test",
                "--", "gh", "api", "--hostname", "attacker.test", "user",
            ])

        run.assert_not_called()

    def test_declared_host_must_match_command_host_selectors(self):
        commands = [
            ["gh", "api", "--hostname", "attacker.test", "user"],
            ["gh", "pr", "edit", "--repo", "attacker.test/acme/api", "7"],
            ["gh", "api", "https://attacker.test/api/v3/user"],
        ]
        for command in commands:
            with self.subTest(command=command), self.assertRaises(ValueError):
                validate_command_host("github", "github.com", command)

    def test_github_creation_and_transition_require_state_match(self):
        commands = [
            (["gh", "pr", "create", "--repo", "owner/repo", "--draft"], "ready", "draft"),
            (["gh", "--repo", "owner/repo", "pr", "create"], "draft", "draft"),
            (["gh", "pr", "ready", "7", "--repo", "owner/repo", "--undo"], "ready", "draft"),
            (["gh", "pr", "ready", "7", "--repo", "owner/repo"], "draft", "draft"),
            (["gh", "pr", "ready", "--repo", "owner/repo", "--undo"], "draft", "canonical"),
            (["gh", "pr", "edit", "7", "--repo", "owner/repo", "--draft"], "draft", "approved"),
        ]
        for command, publication_state, error in commands:
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, error):
                validate_publication_state("github", command, publication_state)

    def test_gitlab_creation_and_transition_require_state_match(self):
        commands = [
            (["glab", "mr", "create", "--hostname", "gitlab.com", "--wip"], "ready", "draft"),
            ([
                "glab", "api", "--hostname", "gitlab.com", "--method", "POST",
                "/projects/acme%2Fapi/merge_requests", "-f", "draft=true",
            ], "ready", "native"),
            (["glab", "mr", "create", "--hostname", "gitlab.com"], "draft", "draft"),
            (
                ["glab", "mr", "update", "7", "--hostname", "gitlab.com", "--draft"],
                "ready", "draft",
            ),
            (
                ["glab", "mr", "update", "7", "--hostname", "gitlab.com", "--ready"],
                "draft", "draft",
            ),
            (["glab", "mr", "update", "--hostname", "gitlab.com", "--draft"], "draft", "canonical"),
            ([
                "glab", "api", "--hostname", "gitlab.com", "--method", "PUT",
                "/projects/acme%2Fapi/merge_requests/7", "-f", "draft=true",
            ], "draft", "publication-state"),
            ([
                "glab", "api", "--hostname", "gitlab.com", "--method", "PUT",
                "/projects/acme%2Fapi/merge_requests/current", "-f", "title=Change",
            ], "draft", "canonical"),
            ([
                "glab", "mr", "create", "--hostname", "gitlab.com",
                "-t", "Draft: add lifecycle skills",
            ], "draft", "draft"),
            ([
                "glab", "mr", "create", "--hostname", "gitlab.com",
                "--title", "[Draft] add lifecycle skills",
            ], "draft", "draft"),
            ([
                "glab", "mr", "create", "--hostname", "gitlab.com",
                "--title", "[ Draft ] add lifecycle skills",
            ], "draft", "draft"),
            ([
                "glab", "mr", "create", "--hostname", "gitlab.com",
                "--title", "WIP — add lifecycle skills",
            ], "draft", "draft"),
        ]
        for command, publication_state, error in commands:
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, error):
                validate_publication_state("gitlab", command, publication_state)

    def test_requested_creation_and_transition_state_is_allowed(self):
        commands = [
            ("github", "ready", ["gh", "pr", "create", "--repo", "owner/repo"]),
            (
                "github", "draft",
                ["gh", "pr", "create", "--repo", "owner/repo", "--draft"],
            ),
            ("github", "ready", ["gh", "pr", "ready", "7", "--repo", "owner/repo"]),
            (
                "github", "draft",
                ["gh", "pr", "ready", "7", "--repo", "owner/repo", "--undo"],
            ),
            (
                "github", "draft",
                ["gh", "pr", "edit", "7", "--repo", "owner/repo", "--body", "Updated"],
            ),
            (
                "gitlab", "ready",
                [
                    "glab", "mr", "create", "--hostname", "gitlab.com",
                    "-d", "Ordinary merge request description",
                ],
            ),
            (
                "gitlab", "draft",
                ["glab", "mr", "create", "--hostname", "gitlab.com", "--draft"],
            ),
            (
                "github", "ready",
                [
                    "gh", "api", "--hostname", "github.com", "--method", "PATCH",
                    "repos/owner/repo/pulls/7", "-f", "title=Updated",
                ],
            ),
            (
                "gitlab", "draft",
                [
                    "glab", "api", "--hostname", "gitlab.com", "--method", "PUT",
                    "/projects/acme%2Fapi/merge_requests/7", "-f", "title=Updated",
                ],
            ),
            (
                "gitlab", "ready",
                ["glab", "mr", "update", "7", "--hostname", "gitlab.com", "--ready"],
            ),
            (
                "gitlab", "draft",
                ["glab", "mr", "update", "7", "--hostname", "gitlab.com", "--draft"],
            ),
            (
                "gitlab", "draft",
                [
                    "glab", "mr", "update", "7", "--hostname", "gitlab.com",
                    "--description", "Updated",
                ],
            ),
        ]
        for provider, publication_state, command in commands:
            with self.subTest(command=command):
                validate_publication_state(provider, command, publication_state)

    def test_unverified_or_graphql_creation_payload_is_rejected(self):
        commands = [
            (
                "github",
                ["gh", "api", "graphql", "--hostname", "github.com", "--input", "payload.json"],
            ),
            (
                "github",
                ["gh", "api", "graphql", "--hostname", "github.com", "-F", "query=@mutation.graphql"],
            ),
            (
                "github",
                [
                    "gh", "api", "graphql", "--hostname", "github.com", "-f",
                    "query=mutation { convertPullRequestToDraft(input: $input) "
                    "{ clientMutationId } }",
                ],
            ),
            (
                "github",
                [
                    "gh", "api", "--hostname", "github.com",
                    "https://github.com/graphql", "-f",
                    "query=mutation { convertPullRequestToDraft(input: $input) "
                    "{ clientMutationId } }",
                ],
            ),
            (
                "github",
                [
                    "gh", "api", "--hostname", "github.com", "--method", "PATCH",
                    "repos/owner/repo/pulls/7", "--input", "payload.json",
                ],
            ),
            (
                "github",
                [
                    "gh", "--repo", "owner/repo", "api",
                    "repos/owner/repo/pulls", "--input", "payload.json",
                ],
            ),
            (
                "github",
                [
                    "gh", "--repo", "owner/repo", "api", "--method", "POST",
                    "repos/owner/repo/pulls", "--input", "payload.json",
                ],
            ),
            (
                "github",
                [
                    "gh", "api", "graphql", "--hostname", "github.com", "-f",
                    "query=mutation { createPullRequest(input: $input) { pullRequest { id } } }",
                ],
            ),
        ]
        for provider, command in commands:
            with self.subTest(command=command), self.assertRaisesRegex(
                ValueError, "payload|GraphQL|native"
            ):
                validate_publication_state(provider, command, "ready")

    def test_field_arguments_make_creation_api_post_implicit(self):
        commands = [
            [
                "gh", "api", "--hostname", "github.com", "repos/owner/repo/pulls",
                "-f", "title=Change", "-F", "draft=true",
            ],
            [
                "glab", "api", "--hostname", "gitlab.com",
                "/projects/acme%2Fapi/merge_requests", "--form", "draft=true",
            ],
        ]
        for provider, command in zip(("github", "gitlab"), commands):
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, "native"):
                validate_publication_state(provider, command, "ready")

    def test_file_backed_draft_value_is_rejected(self):
        commands = [
            ["gh", "api", "repos/owner/repo/pulls/7", "-F", "draft=@draft.txt"],
            ["gh", "api", "repos/owner/repo/pulls/7", "--field=draft=@-"],
        ]
        for command in commands:
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, "draft"):
                validate_publication_state("github", command, "draft")

    def test_main_requires_explicit_draft_state_before_provider_contact(self):
        with patch("provider_cli.subprocess.run") as run:
            with self.assertRaisesRegex(ValueError, "draft"):
                main([
                    "--provider", "github", "--host", "github.com", "--",
                    "gh", "pr", "create", "--repo", "owner/repo", "--draft",
                ])

        run.assert_not_called()

        completed = subprocess.CompletedProcess(args=[], returncode=0)
        with patch("provider_cli.subprocess.run", return_value=completed) as run:
            result = main([
                "--provider", "github", "--host", "github.com",
                "--publication-state", "draft", "--",
                "gh", "pr", "create", "--repo", "owner/repo", "--draft",
            ])

        self.assertEqual(0, result)
        run.assert_called_once()

    def test_main_times_out_provider_command_without_retrying(self):
        command = ["gh", "pr", "edit", "7", "--repo", "owner/repo"]
        with patch(
            "provider_cli.subprocess.run",
            side_effect=subprocess.TimeoutExpired(command, 120),
        ) as run, patch("sys.stderr", new_callable=StringIO) as stderr:
            result = main([
                "--provider", "github", "--host", "github.com", "--", *command,
            ])

        self.assertEqual(124, result)
        self.assertIn("outcome is unknown", stderr.getvalue())
        self.assertIn("read back the exact target before retry", stderr.getvalue())
        run.assert_called_once()
        self.assertEqual(120, run.call_args.kwargs["timeout"])


if __name__ == "__main__":
    unittest.main()

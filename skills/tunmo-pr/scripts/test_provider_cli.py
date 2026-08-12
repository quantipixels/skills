import os
import subprocess
import unittest
from unittest.mock import patch

from provider_cli import command_environment, main, validate_command_host


class ProviderCliTests(unittest.TestCase):
    def test_untrusted_github_host_loses_generic_tokens(self):
        environment = command_environment(
            "github",
            "attacker.test",
            trusted_hosts=set(),
            environment={
                "GH_TOKEN": "one",
                "GITHUB_TOKEN": "two",
                "GH_ENTERPRISE_TOKEN": "three",
                "GITHUB_ENTERPRISE_TOKEN": "four",
                "PATH": "/bin",
            },
        )

        self.assertEqual({"PATH": "/bin"}, environment)

    def test_untrusted_gitlab_host_loses_generic_and_ci_tokens(self):
        environment = command_environment(
            "gitlab",
            "attacker.test",
            trusted_hosts=set(),
            environment={
                "GITLAB_TOKEN": "one",
                "GITLAB_ACCESS_TOKEN": "two",
                "OAUTH_TOKEN": "three",
                "CI_JOB_TOKEN": "four",
                "GLAB_ENABLE_CI_AUTOLOGIN": "true",
            },
        )

        self.assertEqual({"GLAB_ENABLE_CI_AUTOLOGIN": "false"}, environment)

    def test_explicitly_trusted_host_keeps_tokens(self):
        environment = command_environment(
            "github",
            "github.acme.test.",
            trusted_hosts={"GITHUB.ACME.TEST"},
            environment={"GH_ENTERPRISE_TOKEN": "token"},
        )

        self.assertEqual("token", environment["GH_ENTERPRISE_TOKEN"])

    def test_main_passes_sanitized_environment_to_the_provider_cli(self):
        completed = subprocess.CompletedProcess(["gh"], 0)
        with patch.dict(os.environ, {"GH_ENTERPRISE_TOKEN": "token"}, clear=True), patch(
            "provider_cli.subprocess.run", return_value=completed
        ) as run:
            result = main([
                "--provider", "github",
                "--host", "attacker.test",
                "--", "gh", "api", "--hostname", "attacker.test", "user",
            ])

        self.assertEqual(0, result)
        self.assertNotIn("GH_ENTERPRISE_TOKEN", run.call_args.kwargs["env"])

    def test_declared_host_must_match_command_host_selectors(self):
        commands = [
            ["gh", "api", "--hostname", "attacker.test", "user"],
            ["gh", "pr", "view", "--repo", "attacker.test/acme/api", "7"],
            ["gh", "api", "https://attacker.test/api/v3/user"],
        ]
        for command in commands:
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, "does not match"):
                validate_command_host("github.com", command)


if __name__ == "__main__":
    unittest.main()

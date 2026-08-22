#!/usr/bin/env python3
"""Run one provider CLI command only after its exact host is trusted."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from urllib.parse import urlparse


DEFAULT_TRUSTED_HOST = {"github": "github.com", "gitlab": "gitlab.com"}
EXECUTABLE = {"github": "gh", "gitlab": "glab"}
PROVIDER_TIMEOUT_SECONDS = 120
GITHUB_TOKEN_VARIABLES = (
    "GH_TOKEN",
    "GITHUB_TOKEN",
    "GH_ENTERPRISE_TOKEN",
    "GITHUB_ENTERPRISE_TOKEN",
)
GITLAB_TOKEN_VARIABLES = (
    "GITLAB_TOKEN",
    "GITLAB_ACCESS_TOKEN",
    "OAUTH_TOKEN",
    "CI_JOB_TOKEN",
)


def command_environment(
    provider: str,
    host: str,
    *,
    trusted_hosts: set[str],
    environment: dict[str, str] | None = None,
) -> dict[str, str]:
    result = dict(environment if environment is not None else os.environ)
    normalized_host = host.lower().rstrip(".")
    allowed = {
        DEFAULT_TRUSTED_HOST[provider],
        *(value.lower().rstrip(".") for value in trusted_hosts),
    }
    if normalized_host not in allowed:
        raise ValueError(
            f"separate trust is required before contacting custom provider host {host!r}"
        )

    if provider == "github":
        result["GH_HOST"] = normalized_host
        result.pop("GH_REPO", None)
        if normalized_host == "github.com":
            result.pop("GH_ENTERPRISE_TOKEN", None)
            result.pop("GITHUB_ENTERPRISE_TOKEN", None)
        else:
            for name in GITHUB_TOKEN_VARIABLES:
                result.pop(name, None)
    else:
        result.pop("GITLAB_HOST", None)
        result["GLAB_ENABLE_CI_AUTOLOGIN"] = "false"
        if normalized_host == "gitlab.com":
            result.pop("CI_JOB_TOKEN", None)
        else:
            for name in GITLAB_TOKEN_VARIABLES:
                result.pop(name, None)
    return result


def validate_command_host(provider: str, host: str, command: list[str]) -> None:
    declared = host.lower().rstrip(".")
    selected_hosts = set()
    repository_selected = False
    for index, value in enumerate(command):
        if value == "--hostname" and index + 1 < len(command):
            selected_hosts.add(command[index + 1])
        elif value.startswith("--hostname="):
            selected_hosts.add(value.split("=", 1)[1])
        elif value in {"--repo", "-R"} and index + 1 < len(command):
            repository_selected = True
            _add_repository_host(selected_hosts, command[index + 1])
        elif value.startswith("--repo="):
            repository_selected = True
            _add_repository_host(selected_hosts, value.split("=", 1)[1])
        elif value.startswith("-R") and len(value) > 2:
            repository_selected = True
            _add_repository_host(selected_hosts, value[2:].removeprefix("="))
    mismatches = sorted(
        value for value in selected_hosts if value.lower().rstrip(".") != declared
    )
    if mismatches:
        raise ValueError(
            f"declared provider host {host!r} does not match command host(s): {', '.join(mismatches)}"
        )
    if not selected_hosts and not (provider == "github" and repository_selected):
        raise ValueError(
            f"provider command must select the declared host {host!r} through --hostname "
            "or an explicit repository selector"
        )


def validate_ready_for_review_creation(provider: str, command: list[str]) -> None:
    """Reject a PR or MR creation command that can create a draft item."""
    if provider == "github" and _has_opaque_graphql_payload(command):
        raise ValueError(
            "seda-pr rejects opaque GraphQL payloads because PR creation draft state cannot be verified"
        )
    if not _is_item_creation(provider, command):
        return

    if any(value == "--input" or value.startswith("--input=") for value in command):
        raise ValueError(
            "seda-pr rejects unverified creation payload files; use explicit ready-for-review fields"
        )
    if provider == "github" and any("createPullRequest" in value for value in command):
        raise ValueError(
            "seda-pr rejects GraphQL PR creation because draft state is not safely verified"
        )

    fields: list[str] = []
    titles: list[str] = []
    for index, value in enumerate(command):
        lowered = value.lower()
        draft_flags = {"--draft"}
        if provider == "github":
            draft_flags.add("-d")
        elif provider == "gitlab":
            draft_flags.add("--wip")
        if lowered in draft_flags:
            raise ValueError("seda-pr never creates a draft PR or MR")
        if lowered.startswith("--draft=") and _truthy(value.split("=", 1)[1]):
            raise ValueError("seda-pr never creates a draft PR or MR")
        if value in {"-f", "-F", "--field", "--raw-field", "--form"} and index + 1 < len(command):
            fields.append(command[index + 1])
        elif value.startswith(("--field=", "--raw-field=", "--form=")):
            fields.append(value.split("=", 1)[1])
        elif value.startswith(("-f", "-F")) and len(value) > 2:
            fields.append(value[2:].removeprefix("="))
        if value == "--title" and index + 1 < len(command):
            titles.append(command[index + 1])
        elif value.startswith("--title="):
            titles.append(value.split("=", 1)[1])

    for field in fields:
        name, separator, raw_value = field.partition("=")
        if not separator:
            continue
        if name.lower() == "draft" and _truthy(raw_value):
            raise ValueError("seda-pr never creates a draft PR or MR")
        if name.lower() == "draft" and raw_value.startswith("@"):
            raise ValueError("seda-pr rejects file-backed draft state")
        if name.lower() == "title":
            titles.append(raw_value)
    if any(re.match(r"^\s*(?:draft|wip)\s*:", title, re.IGNORECASE) for title in titles):
        raise ValueError("seda-pr never creates a draft PR or MR by title convention")


def _is_item_creation(provider: str, command: list[str]) -> bool:
    if provider == "github" and any(
        _contains_subcommand(command, "pr", action) for action in ("create", "new")
    ):
        return True
    if provider == "gitlab" and _contains_subcommand(command, "mr", "create"):
        return True
    if not command or command[0] != EXECUTABLE[provider] or "api" not in command[1:]:
        return False
    if provider == "github" and any("createPullRequest" in value for value in command):
        return True
    method: str | None = None
    for index, value in enumerate(command):
        if value in {"--method", "-X"} and index + 1 < len(command):
            method = command[index + 1].upper()
        elif value.startswith("--method="):
            method = value.split("=", 1)[1].upper()
        elif value.startswith("-X") and len(value) > 2:
            method = value[2:].removeprefix("=").upper()
    if method is None:
        method = "POST" if _has_api_fields(command) else "GET"
    if method != "POST":
        return False
    return any(
        re.search(r"/(?:pulls|merge_requests)/?$", value.split("?", 1)[0])
        for value in command
    )


def _contains_subcommand(command: list[str], group: str, action: str) -> bool:
    return any(
        command[index:index + 2] == [group, action]
        for index in range(1, len(command) - 1)
    )


def _has_api_fields(command: list[str]) -> bool:
    field_flags = {"-f", "-F", "--field", "--raw-field", "--form"}
    return any(
        value in field_flags
        or value == "--input"
        or value.startswith("--input=")
        or value.startswith(("--field=", "--raw-field=", "--form="))
        or (value.startswith(("-f", "-F")) and len(value) > 2)
        for value in command
    )


def _has_opaque_graphql_payload(command: list[str]) -> bool:
    if "api" not in command[1:] or "graphql" not in command[1:]:
        return False
    if any(value == "--input" or value.startswith("--input=") for value in command):
        return True
    field_flags = {"-f", "-F", "--field", "--raw-field", "--form"}
    fields: list[str] = []
    for index, value in enumerate(command):
        if value in field_flags and index + 1 < len(command):
            fields.append(command[index + 1])
        elif value.startswith(("--field=", "--raw-field=", "--form=")):
            fields.append(value.split("=", 1)[1])
        elif value.startswith(("-f", "-F")) and len(value) > 2:
            fields.append(value[2:].removeprefix("="))
    return any(field.lower().startswith("query=@") for field in fields)


def _truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _add_repository_host(selected_hosts: set[str], repository: str) -> None:
    if repository.startswith(("http://", "https://")):
        parsed = urlparse(repository)
        if parsed.hostname:
            selected_hosts.add(parsed.hostname)
        return
    parts = repository.split("/", 2)
    if len(parts) == 3 and "." in parts[0]:
        selected_hosts.add(parts[0])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=("github", "gitlab"), required=True)
    parser.add_argument("--host", required=True)
    parser.add_argument("--trusted-host", action="append", default=[])
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    if args.command[:1] == ["--"]:
        args.command = args.command[1:]
    if not args.command:
        parser.error("a provider CLI command is required after --")
    if args.command[0] != EXECUTABLE[args.provider]:
        parser.error(f"{args.provider} commands must start with {EXECUTABLE[args.provider]!r}")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    validate_command_host(args.provider, args.host, args.command)
    validate_ready_for_review_creation(args.provider, args.command)
    environment = command_environment(
        args.provider,
        args.host,
        trusted_hosts=set(args.trusted_host),
    )
    try:
        return subprocess.run(
            args.command,
            check=False,
            env=environment,
            timeout=PROVIDER_TIMEOUT_SECONDS,
        ).returncode
    except subprocess.TimeoutExpired:
        print(
            "provider command timed out; a write outcome is unknown. "
            "Stop dependent writes and read back the exact target before retry.",
            file=sys.stderr,
        )
        return 124


if __name__ == "__main__":
    raise SystemExit(main())

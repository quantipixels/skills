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


def validate_publication_state(
    provider: str,
    command: list[str],
    publication_state: str,
) -> None:
    """Reject PR or MR commands that conflict with the requested publication state."""
    if publication_state not in {"ready", "draft"}:
        raise ValueError(f"unsupported publication state {publication_state!r}")
    _validate_canonical_mutation_target(provider, command)
    if provider == "github" and _has_opaque_graphql_payload(command):
        raise ValueError(
            "seda-pr rejects opaque GraphQL payloads because publication state cannot be verified"
        )
    if provider == "github" and _has_graphql_mutation(command):
        raise ValueError(
            "seda-pr rejects GraphQL mutations because publication state cannot be verified"
        )

    is_creation = _is_item_creation(provider, command)
    is_native_creation = _is_native_item_creation(provider, command)
    if is_creation and not is_native_creation:
        raise ValueError(
            "seda-pr requires the provider's native PR or MR creation command"
        )
    _validate_api_mutation_target(provider, command)

    if is_creation and any(
        value == "--input" or value.startswith("--input=") for value in command
    ):
        raise ValueError(
            "seda-pr rejects unverified creation payload files; "
            "use explicit publication-state fields"
        )
    if is_creation and provider == "github" and any(
        "createPullRequest" in value for value in command
    ):
        raise ValueError(
            "seda-pr rejects GraphQL PR creation because draft state is not safely verified"
        )

    fields, titles = _fields_and_titles(command)
    signalled_states: set[str] = set()
    for field in fields:
        name, separator, raw_value = field.partition("=")
        if not separator:
            continue
        if name.lower() == "draft":
            parsed_state = _parse_boolean_publication_state(raw_value)
            if "api" in command[1:]:
                raise ValueError(
                    "seda-pr rejects publication-state fields in provider API writes"
                )
            signalled_states.add(parsed_state)
        if name.lower() == "title":
            titles.append(raw_value)

    draft_flags = {"--draft"}
    if provider == "github" and is_creation:
        draft_flags.add("-d")
    if provider == "gitlab":
        draft_flags.add("--wip")
    has_draft_flag = any(value.lower() in draft_flags for value in command)
    has_attached_draft_flag = any(
        value.lower().startswith(("--draft=", "--wip=")) for value in command
    )
    is_github_transition = provider == "github" and _contains_subcommand(
        command, "pr", "ready"
    )
    is_gitlab_transition = provider == "gitlab" and _contains_subcommand(
        command, "mr", "update"
    )
    if (has_draft_flag or has_attached_draft_flag) and not (
        is_native_creation or is_github_transition or is_gitlab_transition
    ):
        raise ValueError(
            "seda-pr accepts draft flags only on approved creation or state commands"
        )
    if has_draft_flag:
        signalled_states.add("draft")
    if "--ready" in command and not is_gitlab_transition:
        raise ValueError(
            "seda-pr accepts ready flags only on the approved GitLab state command"
        )
    if "--undo" in command and not is_github_transition:
        raise ValueError(
            "seda-pr accepts --undo only on the approved GitHub state command"
        )
    for value in command:
        lowered = value.lower()
        if lowered.startswith(("--draft=", "--wip=")):
            signalled_states.add(
                _parse_boolean_publication_state(value.split("=", 1)[1])
            )

    if is_github_transition:
        signalled_states.add("draft" if "--undo" in command else "ready")
    if is_gitlab_transition:
        if "--ready" in command or "-r" in command:
            signalled_states.add("ready")

    title_state_pattern = re.compile(
        r"^\s*(?:(?:draft|wip)\s*[:\-–—]|\[\s*(?:draft|wip)\s*\]|\(\s*(?:draft|wip)\s*\))",
        re.IGNORECASE,
    )
    if any(title_state_pattern.match(title) for title in titles):
        raise ValueError("seda-pr requires native draft state, not a title convention")

    if len(signalled_states) > 1:
        raise ValueError("provider command contains conflicting ready and draft signals")
    if not is_creation and not signalled_states:
        return

    command_state = next(iter(signalled_states), "ready")
    if command_state != publication_state:
        raise ValueError(
            f"provider command requests {command_state!r} publication but "
            f"seda-pr pinned {publication_state!r}"
        )


def _fields_and_titles(command: list[str]) -> tuple[list[str], list[str]]:
    fields: list[str] = []
    titles: list[str] = []
    for index, value in enumerate(command):
        if value in {"-f", "-F", "--field", "--raw-field", "--form"} and index + 1 < len(command):
            fields.append(command[index + 1])
        elif value.startswith(("--field=", "--raw-field=", "--form=")):
            fields.append(value.split("=", 1)[1])
        elif value.startswith(("-f", "-F")) and len(value) > 2:
            fields.append(value[2:].removeprefix("="))
        if value in {"--title", "-t"} and index + 1 < len(command):
            titles.append(command[index + 1])
        elif value.startswith("--title="):
            titles.append(value.split("=", 1)[1])
        elif value.startswith("-t") and len(value) > 2:
            titles.append(value[2:].removeprefix("="))
    return fields, titles


def _parse_boolean_publication_state(value: str) -> str:
    if value.startswith("@"):
        raise ValueError("seda-pr rejects file-backed draft state")
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return "draft"
    if normalized in {"0", "false", "no", "off"}:
        return "ready"
    raise ValueError(f"seda-pr requires an explicit boolean draft field, got {value!r}")


def _is_item_creation(provider: str, command: list[str]) -> bool:
    if _is_native_item_creation(provider, command):
        return True
    if not command or command[0] != EXECUTABLE[provider] or "api" not in command[1:]:
        return False
    if provider == "github" and any("createPullRequest" in value for value in command):
        return True
    if _api_method(command) != "POST":
        return False
    return any(
        re.search(r"/(?:pulls|merge_requests)/?$", value.split("?", 1)[0])
        for value in command
    )


def _is_native_item_creation(provider: str, command: list[str]) -> bool:
    if provider == "github" and any(
        _contains_subcommand(command, "pr", action) for action in ("create", "new")
    ):
        return True
    if provider == "gitlab" and _contains_subcommand(command, "mr", "create"):
        return True
    return False


def _api_method(command: list[str]) -> str:
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
    return method


def _contains_subcommand(command: list[str], group: str, action: str) -> bool:
    return any(
        command[index:index + 2] == [group, action]
        for index in range(1, len(command) - 1)
    )


def _validate_canonical_mutation_target(provider: str, command: list[str]) -> None:
    actions = {"github": {("pr", "edit"), ("pr", "ready")}, "gitlab": {("mr", "update")}}
    for group, action in actions[provider]:
        index = _subcommand_index(command, group, action)
        if index is None:
            continue
        target_index = index + 2
        if target_index >= len(command) or not command[target_index].isdigit():
            item = "PR" if provider == "github" else "MR"
            raise ValueError(
                f"existing-item mutation requires the canonical {item} number"
            )


def _validate_api_mutation_target(provider: str, command: list[str]) -> None:
    if "api" not in command[1:] or _api_method(command) in {"GET", "HEAD"}:
        return
    if any(value == "--input" or value.startswith("--input=") for value in command):
        raise ValueError(
            "seda-pr rejects opaque input payloads for provider API mutations"
        )
    endpoint_pattern = re.compile(r"/(?:pulls|merge_requests)/(\d+)/?$")
    collection_pattern = re.compile(r"/(?:pulls|merge_requests)/?$")
    endpoints = [value.split("?", 1)[0] for value in command if "/" in value]
    if any(collection_pattern.search(value) for value in endpoints):
        raise ValueError(
            "seda-pr requires the provider's native PR or MR creation command"
        )
    if any("pulls" in value or "merge_requests" in value for value in endpoints) and not any(
        endpoint_pattern.search(value) for value in endpoints
    ):
        item = "PR" if provider == "github" else "MR"
        raise ValueError(
            f"provider API mutation requires the canonical {item} number"
        )


def _subcommand_index(command: list[str], group: str, action: str) -> int | None:
    for index in range(1, len(command) - 1):
        if command[index:index + 2] == [group, action]:
            return index
    return None


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
    if not _is_graphql_command(command):
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


def _has_graphql_mutation(command: list[str]) -> bool:
    if not _is_graphql_command(command):
        return False
    return any(
        re.search(r"(?:^|[=\s])mutation(?:[\s({]|$)", value, re.IGNORECASE)
        for value in command
    )


def _is_graphql_command(command: list[str]) -> bool:
    if "api" not in command[1:]:
        return False
    return any(
        re.search(r"(?:^|/)graphql(?:\?.*)?$", value, re.IGNORECASE)
        for value in command
    )


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
    parser.add_argument(
        "--publication-state",
        choices=("ready", "draft"),
        default="ready",
    )
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
    validate_publication_state(args.provider, args.command, args.publication_state)
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

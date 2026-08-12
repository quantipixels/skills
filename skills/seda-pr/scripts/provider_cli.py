#!/usr/bin/env python3
"""Run one provider CLI command without leaking generic tokens to an untrusted host."""

from __future__ import annotations

import argparse
import os
import subprocess
from urllib.parse import urlparse


TOKEN_VARIABLES = {
    "github": ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN", "GITHUB_ENTERPRISE_TOKEN"),
    "gitlab": ("GITLAB_TOKEN", "GITLAB_ACCESS_TOKEN", "OAUTH_TOKEN", "CI_JOB_TOKEN"),
}
DEFAULT_TRUSTED_HOST = {"github": "github.com", "gitlab": "gitlab.com"}
EXECUTABLE = {"github": "gh", "gitlab": "glab"}


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
        for name in TOKEN_VARIABLES[provider]:
            result.pop(name, None)
        if provider == "gitlab":
            result["GLAB_ENABLE_CI_AUTOLOGIN"] = "false"
    return result


def validate_command_host(host: str, command: list[str]) -> None:
    declared = host.lower().rstrip(".")
    selected_hosts = set()
    for index, value in enumerate(command):
        if value == "--hostname" and index + 1 < len(command):
            selected_hosts.add(command[index + 1])
        elif value.startswith("--hostname="):
            selected_hosts.add(value.split("=", 1)[1])
        elif value in {"--repo", "-R"} and index + 1 < len(command):
            _add_repository_host(selected_hosts, command[index + 1])
        elif value.startswith("--repo="):
            _add_repository_host(selected_hosts, value.split("=", 1)[1])
        elif value.startswith(("http://", "https://")):
            parsed = urlparse(value)
            if parsed.hostname:
                selected_hosts.add(parsed.hostname)
    mismatches = sorted(
        value for value in selected_hosts if value.lower().rstrip(".") != declared
    )
    if mismatches:
        raise ValueError(
            f"declared provider host {host!r} does not match command host(s): {', '.join(mismatches)}"
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
    validate_command_host(args.host, args.command)
    environment = command_environment(
        args.provider,
        args.host,
        trusted_hosts=set(args.trusted_host),
    )
    return subprocess.run(args.command, check=False, env=environment).returncode


if __name__ == "__main__":
    raise SystemExit(main())

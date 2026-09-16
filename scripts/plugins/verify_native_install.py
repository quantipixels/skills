#!/usr/bin/env python3
"""Verify that native Codex and Claude managers install this checkout faithfully."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[2]
PLUGIN_ID = "qp-skills@qp-skills"


def run(command: list[str], env: dict[str, str]) -> str:
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(command)}\n{result.stdout}"
        )
    return result.stdout


def load_json(output: str, command: str) -> object:
    try:
        return json.loads(output)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"{command} did not return JSON:\n{output}") from error


def require_same(installed_root: Path, paths: tuple[str, ...]) -> None:
    for relative in paths:
        source = ROOT / relative
        installed = installed_root / relative
        if not installed.is_file():
            raise RuntimeError(f"installed plugin is missing {relative}")
        if source.read_bytes() != installed.read_bytes():
            raise RuntimeError(f"installed content differs from source: {relative}")


def verify_codex() -> dict[str, object]:
    if not shutil.which("codex"):
        raise RuntimeError("codex executable is unavailable")

    with tempfile.TemporaryDirectory(prefix="qp-codex-home-") as home:
        env = os.environ.copy()
        env["CODEX_HOME"] = home

        marketplace = load_json(
            run(["codex", "plugin", "marketplace", "add", str(ROOT), "--json"], env),
            "codex plugin marketplace add",
        )
        install = load_json(
            run(["codex", "plugin", "add", PLUGIN_ID, "--json"], env),
            "codex plugin add",
        )
        listing = load_json(
            run(["codex", "plugin", "list", "--json"], env),
            "codex plugin list",
        )

        if marketplace.get("marketplaceName") != "qp-skills":
            raise RuntimeError("Codex registered an unexpected marketplace identity")
        matches = [
            item
            for item in listing.get("installed", [])
            if item.get("pluginId") == PLUGIN_ID
        ]
        if len(matches) != 1 or not matches[0].get("enabled"):
            raise RuntimeError("Codex did not report one enabled QP plugin")

        installed_root = Path(install["installedPath"])
        require_same(
            installed_root,
            (".codex-plugin/plugin.json", "skills/alarina/SKILL.md"),
        )
        return {
            "host": "codex",
            "version": run(["codex", "--version"], env).strip(),
            "plugin": PLUGIN_ID,
            "installed_content_matches": True,
        }


def verify_claude() -> dict[str, object]:
    if not shutil.which("claude"):
        raise RuntimeError("claude executable is unavailable")

    with tempfile.TemporaryDirectory(prefix="qp-claude-home-") as home:
        env = os.environ.copy()
        env["CLAUDE_CONFIG_DIR"] = home

        validation = load_json(
            run(["claude", "plugin", "validate", str(ROOT), "--json"], env),
            "claude plugin validate",
        )
        if not validation.get("success") or validation.get("manifest", {}).get("errors"):
            raise RuntimeError("Claude rejected the plugin manifest")

        run(
            ["claude", "plugin", "marketplace", "add", str(ROOT), "--scope", "user"],
            env,
        )
        run(
            ["claude", "plugin", "install", PLUGIN_ID, "--scope", "user"],
            env,
        )
        listing = load_json(
            run(["claude", "plugin", "list", "--json"], env),
            "claude plugin list",
        )
        matches = [item for item in listing if item.get("id") == PLUGIN_ID]
        if len(matches) != 1 or not matches[0].get("enabled"):
            raise RuntimeError("Claude did not report one enabled QP plugin")

        inventory = run(["claude", "plugin", "details", PLUGIN_ID], env)
        skill_count = sum(
            1
            for path in (ROOT / "skills").iterdir()
            if (path / "SKILL.md").is_file()
        )
        agent_count = len(tuple((ROOT / "agents").glob("*.md")))
        for expected in (f"Skills ({skill_count})", f"Agents ({agent_count})", "alarina"):
            if expected not in inventory:
                raise RuntimeError(f"Claude inventory is missing {expected!r}")

        installed_root = Path(matches[0]["installPath"])
        require_same(
            installed_root,
            (
                ".claude-plugin/plugin.json",
                "skills/alarina/SKILL.md",
                "agents/alarina.md",
            ),
        )
        return {
            "host": "claude",
            "version": run(["claude", "--version"], env).strip(),
            "plugin": PLUGIN_ID,
            "installed_content_matches": True,
            "inventory": {"skills": skill_count, "agents": agent_count},
            "validator_warnings": validation.get("manifest", {}).get("warnings", []),
        }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Install this checkout through isolated native host managers and compare "
            "representative installed content with the source."
        )
    )
    parser.add_argument(
        "--host",
        choices=("all", "codex", "claude"),
        default="all",
        help="native host to verify (default: all)",
    )
    args = parser.parse_args()

    results = []
    if args.host in ("all", "codex"):
        results.append(verify_codex())
    if args.host in ("all", "claude"):
        results.append(verify_claude())

    print(json.dumps({"success": True, "results": results}, indent=2))
    print("Fresh-session skill invocation remains a separate runtime check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

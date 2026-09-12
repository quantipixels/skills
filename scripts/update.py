#!/usr/bin/env python3
"""Update QP Skills through the installation manager that already owns it."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request

SOURCE = "quantipixels/skills"
PLUGIN = "qp-skills@qp-skills"
CATALOGUE_URL = "https://api.github.com/repos/quantipixels/skills/contents/skills?ref=ori"


class UpdateError(Exception):
    pass


def data_root() -> Path:
    value = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local/share")
    return Path(value) / "qp-skills"


def global_skills_lock_path() -> Path:
    state = os.environ.get("XDG_STATE_HOME")
    return Path(state) / "skills/.skill-lock.json" if state else Path.home() / ".agents/.skill-lock.json"


def project_skills_lock_path(cwd: Path | None = None) -> Path:
    return (cwd or Path.cwd()) / "skills-lock.json"


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def direct_installation(root: Path | None = None) -> dict | None:
    root = root or data_root()
    owner = root / "owner.json"
    current = root / "current"
    if not owner.is_file() or not current.exists():
        return None
    try:
        ownership = read_json(owner)
        manifest = read_json(current / "installation.json")
    except (OSError, json.JSONDecodeError):
        return None
    if ownership != {"format": 1, "source": SOURCE}:
        return None
    if not isinstance(manifest, dict) or manifest.get("source") != SOURCE:
        return None
    skills = manifest.get("skills")
    if not isinstance(skills, list) or not all(isinstance(name, str) for name in skills):
        return None
    return {"manager": "direct", "skills": sorted(set(skills)), "manifest": manifest}


def skills_cli_from_lock(lock: Path, manager: str) -> dict | None:
    if not lock.is_file():
        return None
    try:
        payload = read_json(lock)
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(payload, dict) or not isinstance(payload.get("skills"), dict):
        return None
    names = []
    for name, entry in payload["skills"].items():
        if not isinstance(name, str) or not isinstance(entry, dict):
            continue
        source = str(entry.get("source") or "").removesuffix(".git")
        source_url = str(entry.get("sourceUrl") or "").removesuffix(".git").rstrip("/")
        if source == SOURCE or source_url.endswith("/" + SOURCE):
            names.append(name)
    if not names:
        return None
    return {"manager": manager, "skills": sorted(set(names)), "lock": str(lock)}


def skills_cli_global_installation(lock: Path | None = None) -> dict | None:
    return skills_cli_from_lock(lock or global_skills_lock_path(), "skills-global")


def skills_cli_project_installation(lock: Path | None = None) -> dict | None:
    return skills_cli_from_lock(lock or project_skills_lock_path(), "skills-project")


def _walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def claude_plugin_from_payload(payload: object) -> dict | None:
    for item in _walk(payload):
        strings = {str(v) for v in item.values() if isinstance(v, (str, int, float, bool))}
        if "qp-skills" in strings or PLUGIN in strings:
            scope = item.get("scope") if isinstance(item.get("scope"), str) else "user"
            return {"manager": "claude-plugin", "scope": scope}
    return None


def claude_plugin_installation(run=subprocess.run) -> dict | None:
    if shutil.which("claude") is None:
        return None
    result = run(
        ["claude", "plugin", "list", "--json"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        return None
    try:
        return claude_plugin_from_payload(json.loads(result.stdout))
    except json.JSONDecodeError:
        return None


def remote_catalogue(opener=urllib.request.urlopen) -> list[str]:
    request = urllib.request.Request(
        CATALOGUE_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "qp-skills-updater"},
    )
    with opener(request, timeout=15) as response:
        payload = json.load(response)
    if not isinstance(payload, list):
        raise UpdateError("Unexpected QP catalogue response")
    names = sorted(
        item["name"]
        for item in payload
        if isinstance(item, dict)
        and item.get("type") == "dir"
        and isinstance(item.get("name"), str)
    )
    if not names:
        raise UpdateError("QP catalogue is empty")
    return names


def catalogue_delta(installed: list[str], available: list[str]) -> tuple[list[str], list[str]]:
    current, remote = set(installed), set(available)
    return sorted(remote - current), sorted(current - remote)


def confirm(prompt: str, assume_yes: bool = False, input_fn=input) -> bool:
    if assume_yes:
        return True
    answer = input_fn(f"{prompt} [y/N] ").strip().lower()
    return answer in {"y", "yes"}


def command(args: list[str], dry_run: bool, run=subprocess.run) -> None:
    if dry_run:
        print("$ " + " ".join(args))
        return
    result = run(args, check=False)
    if result.returncode:
        raise UpdateError(f"Command failed ({result.returncode}): {' '.join(args)}")


def update_direct(
    installation: dict,
    available: list[str],
    script_root: Path,
    dry_run: bool,
    assume_yes: bool,
    run=subprocess.run,
) -> None:
    additions, deprecated = catalogue_delta(installation["skills"], available)
    if additions or deprecated:
        print("Catalogue changes detected:")
        if additions:
            print("  new: " + ", ".join(additions))
        if deprecated:
            print("  deprecated: " + ", ".join(deprecated))
        if not confirm(
            "Allow the direct installation to add/remove these catalogue entries?",
            assume_yes,
        ):
            raise UpdateError("Direct update cancelled before catalogue migration")
    install = script_root / "install.sh"
    if not install.is_file():
        raise UpdateError("Direct updater requires scripts/install.sh from a QP checkout")
    command(["bash", str(install), "--ref", "ori"], dry_run, run)


def update_skills_cli(
    installation: dict,
    available: list[str] | None,
    dry_run: bool,
    assume_yes: bool,
    sync: bool,
    run=subprocess.run,
) -> None:
    if shutil.which("npx") is None:
        raise UpdateError("npx is required for the existing Skills CLI installation")
    installed = installation["skills"]
    scope = "--global" if installation["manager"] == "skills-global" else "--project"
    command(["npx", "--yes", "skills", "update", *installed, scope, "-y"], dry_run, run)
    if available is None:
        print("Catalogue migration audit skipped: current remote catalogue could not be read.")
        return
    additions, deprecated = catalogue_delta(installed, available)
    if deprecated:
        print("Deprecated QP skills still installed: " + ", ".join(deprecated))
        if confirm("Remove deprecated QP skills?", assume_yes):
            command(
                ["npx", "--yes", "skills", "remove", scope, *deprecated, "-y"],
                dry_run,
                run,
            )
    if additions:
        print("QP skills not in this installation: " + ", ".join(additions))
        if sync and confirm(
            "Install these missing QP skills? This may include skills you intentionally omitted.",
            assume_yes,
        ):
            for name in additions:
                command(
                    [
                        "npx",
                        "--yes",
                        "skills",
                        "add",
                        SOURCE,
                        "--skill",
                        name,
                        scope,
                        "-y",
                    ],
                    dry_run,
                    run,
                )
        elif not sync:
            print("Use --sync to offer installation of missing QP skills.")


def update_claude_plugin(
    installation: dict,
    dry_run: bool,
    run=subprocess.run,
) -> None:
    if shutil.which("claude") is None:
        raise UpdateError("claude is required for the existing Claude Code plugin installation")
    command(
        ["claude", "plugin", "update", PLUGIN, "--scope", installation.get("scope", "user")],
        dry_run,
        run,
    )


def detect() -> list[dict]:
    found = []
    for candidate in (
        direct_installation(),
        skills_cli_project_installation(),
        skills_cli_global_installation(),
        claude_plugin_installation(),
    ):
        if candidate:
            found.append(candidate)
    return found


def choose(found: list[dict], requested: str | None, input_fn=input) -> dict:
    if requested:
        matches = [item for item in found if item["manager"] == requested]
        if len(matches) != 1:
            raise UpdateError(f"Requested manager not detected: {requested}")
        return matches[0]
    if not found:
        raise UpdateError("No supported QP installation manager detected")
    if len(found) == 1:
        return found[0]
    print("Multiple QP installation managers detected:")
    for index, item in enumerate(found, start=1):
        print(f"  {index}) {item['manager']}")
    answer = input_fn("Choose the installation to update: ").strip()
    try:
        selected = int(answer)
    except ValueError as error:
        raise UpdateError("Update cancelled: choose one manager") from error
    if selected < 1 or selected > len(found):
        raise UpdateError("Update cancelled: invalid manager choice")
    return found[selected - 1]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manager",
        choices=("direct", "skills-project", "skills-global", "claude-plugin"),
        help="Use one detected manager when more than one exists.",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Offer QP skills missing from a selective Skills CLI installation.",
    )
    parser.add_argument("--yes-migrations", action="store_true", help="Approve catalogue add/remove prompts.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        installation = choose(detect(), args.manager)
        try:
            available = remote_catalogue()
        except Exception as error:
            available = None
            print(f"Could not audit the current QP catalogue: {error}", file=sys.stderr)
        script_root = Path(__file__).resolve().parent
        if installation["manager"] == "direct":
            if available is None:
                raise UpdateError("Direct update needs the current catalogue to preview add/remove changes")
            update_direct(
                installation,
                available,
                script_root,
                args.dry_run,
                args.yes_migrations,
            )
        elif installation["manager"] in {"skills-project", "skills-global"}:
            update_skills_cli(
                installation,
                available,
                args.dry_run,
                args.yes_migrations,
                args.sync,
            )
        else:
            update_claude_plugin(installation, args.dry_run)
        return 0
    except UpdateError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

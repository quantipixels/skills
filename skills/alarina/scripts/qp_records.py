#!/usr/bin/env python3
"""Ensure a checkout's .qp link reaches records outside every worktree.

Usage: python3 "$SKILL_DIR/scripts/qp_records.py" [CHECKOUT]
Uses origin (or the first remote), preserving nested owner namespaces. Without
remotes, uses local/<main-checkout-name>-<short-id>. Prints the records home;
callers can then write plans/, reports/, or another record kind through .qp.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def remote_identity(remote: str, main: Path) -> list[str]:
    if "://" in remote:
        parsed = urlsplit(remote)
        path = unquote(parsed.path).strip("/")
        local = parsed.scheme == "file"
    else:
        scp = re.fullmatch(r"(?:[^/@:]+@)?[^/:]+:(.+)", remote)
        path = scp.group(1).strip("/") if scp else remote
        local = scp is None
    if local:
        location = Path(path if "://" not in remote else unquote(urlsplit(remote).path))
        location = (main / location).resolve()
        parts = [location.parent.name, location.name]
    else:
        parts = path.split("/")
    parts[-1] = parts[-1].removesuffix(".git")
    if len(parts) < 2 or any(part in ("", ".", "..") or not re.fullmatch(r"[\w.-]+", part)
                             for part in parts):
        raise ValueError("remote must identify a safe owner/repo path")
    return parts


def records_home(checkout: Path) -> Path:
    """Resolve the shared home without creating directories or changing Git."""
    common = Path(git(checkout, "rev-parse", "--path-format=absolute", "--git-common-dir"))
    worktrees = git(checkout, "worktree", "list", "--porcelain", "-z").split("\0")
    main = Path(worktrees[0].removeprefix("worktree "))
    remotes = git(checkout, "remote").splitlines()
    if remotes:
        name = "origin" if "origin" in remotes else remotes[0]
        identity = remote_identity(git(checkout, "remote", "get-url", name), main)
    else:
        short_id = hashlib.sha256(str(common).encode()).hexdigest()[:8]
        name = re.sub(r"[^\w.-]+", "-", main.name).strip(".-") or "repo"
        identity = ["local", f"{name}-{short_id}"]
    home = (Path.home() / ".qp").joinpath(*identity).resolve()
    for entry in worktrees:
        if entry.startswith("worktree ") and home.is_relative_to(Path(entry[9:]).resolve()):
            raise ValueError("records home must live outside every checkout")
    return home


def ensure_records(checkout: Path) -> Path:
    """Create or repair only the link and the shared local exclude entry."""
    checkout = Path(git(checkout, "rev-parse", "--show-toplevel"))
    home = records_home(checkout)
    link = checkout / ".qp"
    if not link.is_symlink() and link.exists():
        raise FileExistsError(f"refusing to replace existing data at {link}")
    home.mkdir(parents=True, exist_ok=True)
    if link.is_symlink() and link.resolve() != home:
        link.unlink()
    if not link.is_symlink():
        link.symlink_to(home, target_is_directory=True)
    common = Path(git(checkout, "rev-parse", "--path-format=absolute", "--git-common-dir"))
    exclude = common / "info/exclude"
    exclude.parent.mkdir(parents=True, exist_ok=True)
    content = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    if ".qp" not in content.splitlines():
        with exclude.open("a", encoding="utf-8") as stream:
            stream.write(("\n" if content and not content.endswith("\n") else "") + ".qp\n")
    return home


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        print(ensure_records(args.checkout.resolve()))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"qp-records: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

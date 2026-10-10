#!/usr/bin/env python3
"""Inventory Git checkouts using local remote refs; optionally remove safe worktrees."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

DEFAULT_ROOTS = ("~/Projects", "~/.sigidi/worktrees", "~/.sigidi/scratch")


def command(argv, timeout=30):
    try:
        return subprocess.run(argv, capture_output=True, text=True, errors="replace",
                              timeout=timeout, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"})
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ValueError(str(error)) from error


def git(path, *argv):
    result = command(["git", "-C", str(path), *argv])
    if result.returncode:
        raise ValueError(result.stderr.strip() or "Git could not inspect this checkout")
    return result.stdout.strip()


def discover(roots, errors):
    found = set()
    for root in roots:
        root = root.expanduser().resolve()
        if not root.exists():
            continue
        def failed(error):
            errors.append(str(error))
        for folder, directories, filenames in os.walk(root, onerror=failed):
            path = Path(folder)
            bare = "HEAD" in filenames and "objects" in directories and "config" in filenames
            if ".git" in directories or ".git" in filenames or bare:
                found.add(path)
            directories[:] = [d for d in directories if d != ".git"]
            if bare:
                directories.clear()
    return sorted(found)


def size(path):
    total = 0
    def failed(error):
        raise error
    for folder, directories, filenames in os.walk(path, onerror=failed):
        for name in filenames:
            total += (Path(folder) / name).lstat().st_size
        for name in directories:
            child = Path(folder) / name
            if child.is_symlink():
                total += child.lstat().st_size
    return total


def open_files(path):
    binary = shutil.which("lsof")
    if not binary:
        return None, "lsof is unavailable"
    try:
        result = command([binary, "-nP", "+D", str(path), "-F", "p"], timeout=60)
    except ValueError as error:
        return None, str(error)
    if result.stdout.strip():
        return True, "open files"
    if result.returncode == 1 and not result.stderr.strip():
        return False, None
    return None, result.stderr.strip() or "lsof could not prove there are no open files"


def inspect(path, measure=True):
    row = {"path": str(path), "kind": "repo", "classification": "keep", "reason": None,
           "remote": None, "branch": None, "commits_off_remotes": None,
           "remote_default_branch": None, "merged_into_remote_default": None,
           "uncommitted_files": None, "untracked_files": None, "last_commit_date": None,
           "size_bytes": None, "open_files": None, "repository": None}
    try:
        directory = Path(git(path, "rev-parse", "--absolute-git-dir")).resolve()
        common = Path(git(path, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
        row["repository"] = str(common)
        row["kind"] = "worktree" if directory != common else "repo"
        remotes = git(path, "remote").splitlines()
        remote = "origin" if "origin" in remotes else (remotes[0] if remotes else None)
        if remote:
            row["remote"] = git(path, "remote", "get-url", remote)
            head = command(["git", "-C", str(path), "symbolic-ref", "--quiet", f"refs/remotes/{remote}/HEAD"])
            if head.returncode == 0:
                row["remote_default_branch"] = head.stdout.strip().removeprefix("refs/remotes/")
        row["branch"] = git(path, "rev-parse", "--abbrev-ref", "HEAD")
        # Other local branches and the shared stash stack do not belong to this HEAD.
        row["commits_off_remotes"] = int(git(path, "rev-list", "--count", "HEAD", "--not", "--remotes"))
        row["last_commit_date"] = git(path, "show", "-s", "--format=%cI", "HEAD")
        default = row["remote_default_branch"]
        if default:
            merged = command(["git", "-C", str(path), "merge-base", "--is-ancestor", "HEAD", f"refs/remotes/{default}"])
            if merged.returncode in (0, 1):
                row["merged_into_remote_default"] = merged.returncode == 0
        bare = git(path, "rev-parse", "--is-bare-repository") == "true"
        # Ignored files can contain local secrets or other data Git has never saved.
        status = [] if bare else git(path, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignored=matching").split("\0")
        # Rename records carry a second path without a status prefix.
        tracked = untracked = 0
        records = iter(status)
        for record in records:
            if not record:
                continue
            if record.startswith(("??", "!!")):
                untracked += 1
            else:
                tracked += 1
                if "R" in record[:2] or "C" in record[:2]:
                    next(records, None)
        row["uncommitted_files"], row["untracked_files"] = tracked, untracked
        if row["kind"] == "repo":
            row["reason"] = "main checkout"
        elif row["commits_off_remotes"] or tracked or untracked:
            row["classification"], row["reason"] = "unique", "local commits or files"
        else:
            row["open_files"], reason = open_files(path)
            if row["open_files"] is False:
                row["classification"], row["reason"] = "safe", "clean, on a remote, no open files"
            else:
                row["reason"] = reason
        if measure:
            row["size_bytes"] = size(path)
    except (OSError, ValueError) as error:
        row["classification"], row["reason"] = "keep", str(error)
    return row


def inventory(roots):
    errors = []
    rows = [inspect(path) for path in discover(roots, errors)]
    # A stash belongs to the common repository, not each linked checkout.
    repositories = {}
    for row in rows:
        common = row["repository"]
        if not common or common in repositories:
            continue
        try:
            stashes = git(Path(row["path"]), "stash", "list", "--format=%H").splitlines()
            repositories[common] = {"path": common, "stashes": len(stashes)}
        except ValueError as error:
            repositories[common] = {"path": common, "stashes": None, "error": str(error)}
    return {"checkouts": rows, "repositories": list(repositories.values()), "scan_errors": errors}


def remove_safe(rows):
    removed, skipped = [], []
    for row in rows:
        if row["classification"] != "safe":
            skipped.append({"path": row["path"], "reason": row["reason"]})
            continue
        path = Path(row["path"])
        current = inspect(path, measure=False)
        if current["classification"] != "safe" or current["repository"] != row["repository"]:
            skipped.append({"path": str(path), "reason": current["reason"] or "repository changed"})
            continue
        try:
            # Normal Git removal checks registration, locks and cleanliness again.
            result = command(["git", "--git-dir", current["repository"], "worktree", "remove", str(path)], timeout=60)
            if result.returncode:
                raise ValueError(result.stderr.strip() or "Git refused removal")
            removed.append(str(path))
        except ValueError as error:
            skipped.append({"path": str(path), "reason": str(error)})
    return {"removed": removed, "skipped": skipped}


def cell(value):
    if value is None:
        return "unknown"
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def markdown(report):
    fields = ("path", "kind", "classification", "remote", "branch", "commits_off_remotes",
              "merged_into_remote_default", "uncommitted_files", "untracked_files", "last_commit_date", "size_bytes", "reason")
    print("Remote checks use local refs; refresh them before deciding whether remote proof is current. Sizes are logical bytes; untracked counts include ignored paths.\n")
    print("| Path | Kind | Class | Remote | Branch | HEAD off remotes | Merged into remote default | Changed | Untracked | Last commit | Bytes | Reason |")
    print("| " + " | ".join("---" for _ in fields) + " |")
    for row in report["checkouts"]:
        print("| " + " | ".join(cell(row[key]) for key in fields) + " |")
    print("\n| Repository | Shared stashes |\n| --- | --- |")
    for repo in report["repositories"]:
        print(f"| {cell(repo['path'])} | {cell(repo['stashes'])} |")
    for error in report["scan_errors"]:
        print(f"\nScan error: {error}")
    if "removal" in report:
        for path in report["removal"]["removed"]:
            print(f"\nRemoved: {path}")
        for row in report["removal"]["skipped"]:
            print(f"\nSkipped: {row['path']} ({row['reason']})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="*", type=Path, help="Folders to search recursively")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--remove-safe", action="store_true", help="Recheck and remove only safe linked worktrees")
    args = parser.parse_args()
    report = inventory(args.roots or [Path(root) for root in DEFAULT_ROOTS])
    if args.remove_safe:
        report["removal"] = remove_safe(report["checkouts"])
    if args.json:
        json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

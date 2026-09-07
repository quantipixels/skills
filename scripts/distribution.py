#!/usr/bin/env python3
"""Own one QP snapshot and its exact host links; never adopt another installer."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

SOURCE = "quantipixels/skills"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
GENERATION = re.compile(r"[a-f0-9]{32}\Z")


class InstallError(Exception):
    pass


def exists(path: Path) -> bool:
    return os.path.lexists(path)


def read_json(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():
        raise InstallError(f"Expected a regular state file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise InstallError(f"Invalid state object: {path}")
    return value


def write_json(path: Path, value: dict) -> None:
    # Both the journal and ownership record must survive a killed process.
    fd, temporary = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def files(root: Path):
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for name in [*dirs, *sorted(names)]:
            path = Path(directory) / name
            if path.is_symlink():
                raise InstallError(f"Symlinks are not package content: {path}")
            if path.is_file() and not name.endswith(".pyc"):
                yield path
            elif not path.is_dir():
                raise InstallError(f"Unsupported package file: {path}")


def digest(root: Path) -> str:
    result = hashlib.sha256()
    for path in sorted(files(root)):
        if path == root / "installation.json":
            continue
        result.update(path.relative_to(root).as_posix().encode() + b"\0")
        result.update(hashlib.sha256(path.read_bytes()).digest())
        result.update(b"x" if path.stat().st_mode & 0o111 else b"-")
    return result.hexdigest()


def location() -> Path:
    value = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local/share")
    base = Path(value)
    if not base.is_absolute():
        raise InstallError("XDG_DATA_HOME must be absolute")
    return base / "qp-skills"


def generation(root: Path, identity: str) -> Path:
    if (root / "generations").is_symlink():
        raise InstallError("Generations directory must not be a symlink")
    if not isinstance(identity, str) or not GENERATION.fullmatch(identity):
        raise InstallError("Invalid generation identity")
    path = root / "generations" / identity
    if path.is_symlink() or not path.is_dir():
        raise InstallError(f"Missing or substituted generation: {path}")
    return path


def current(root: Path) -> str | None:
    link = root / "current"
    if not exists(link):
        return None
    if not link.is_symlink():
        raise InstallError(f"Expected managed current symlink: {link}")
    target = os.readlink(link)
    parts = Path(target).parts
    if len(parts) != 2 or parts[0] != "generations" or not GENERATION.fullmatch(parts[1]):
        raise InstallError("Current pointer is outside the managed generations")
    generation(root, parts[1])
    return parts[1]


def manifest(root: Path, identity: str | None) -> dict:
    if identity is None:
        return {"skills": [], "hosts": {}}
    folder = generation(root, identity)
    data = read_json(folder / "installation.json")
    if data.get("format") != 1 or data.get("source") != SOURCE:
        raise InstallError("Unrecognized QP installation; no automatic migration")
    names, hosts = data.get("skills"), data.get("hosts")
    if (not isinstance(names, list) or not names or len(names) != len(set(names))
            or any(not isinstance(n, str) or len(n) > 64 or not NAME.fullmatch(n) for n in names)
            or not isinstance(hosts, dict) or not hosts or set(hosts) - {"codex", "claude"}):
        raise InstallError("Invalid installed skill/host inventory")
    for destination in hosts.values():
        if not isinstance(destination, str) or not Path(destination).is_absolute():
            raise InstallError("Invalid host destination")
        if Path(destination).resolve().is_relative_to(root.resolve()):
            raise InstallError("Host destination overlaps the managed store")
    if data.get("digest") != digest(folder):
        raise InstallError(f"Installed files were modified; preserve them before updating/removing: {folder}")
    return data


def links(root: Path, data: dict) -> dict[Path, Path]:
    return {Path(host) / name: root / "current/skills" / name
            for host in data["hosts"].values() for name in data["skills"]}


def matches(link: Path, target: Path) -> bool:
    return link.is_symlink() and Path(os.path.abspath(link.parent / os.readlink(link))) == target


def check_links(root: Path, data: dict) -> None:
    for link, target in links(root, data).items():
        if exists(link) and not matches(link, target):
            raise InstallError(f"Unmanaged or replaced path; refusing to change it: {link}")


def remove_links(selected: dict[Path, Path]) -> None:
    for link, target in selected.items():
        if not exists(link):
            continue
        if not matches(link, target):
            raise InstallError(f"Link changed during operation; preserved: {link}")
        link.unlink()


def recover(root: Path) -> None:
    journal = root / "transaction.json"
    if not exists(journal):
        return
    data = read_json(journal)
    if set(data) != {"old", "new"} or data["old"] == data["new"]:
        raise InstallError("Invalid installation transaction")
    old, new = data["old"], data["new"]
    old_links, new_links = links(root, manifest(root, old)), links(root, manifest(root, new))
    active = current(root)
    if active == new:
        remove_links({p: t for p, t in old_links.items() if p not in new_links})
        retired = old
    elif active == old:
        remove_links({p: t for p, t in new_links.items() if p not in old_links})
        retired = new
    else:
        raise InstallError("Current generation conflicts with pending transaction")
    # Settle visible links before collecting unreferenced snapshots.
    journal.unlink()
    if new is not None:
        pointer = root / (".current-" + new)
        if pointer.is_symlink() and os.readlink(pointer) == "generations/" + new:
            pointer.unlink()
    if retired is not None:
        shutil.rmtree(generation(root, retired))


@contextmanager
def locked(root: Path):
    if root.is_symlink():
        raise InstallError("Managed installation root must not be a symlink")
    root.mkdir(parents=True, exist_ok=True)
    owner = root / "owner.json"
    if not exists(owner):
        if any(root.iterdir()):
            raise InstallError(f"Unowned nonempty installation directory: {root}")
        write_json(owner, {"format": 1, "source": SOURCE})
    if read_json(owner) != {"format": 1, "source": SOURCE}:
        raise InstallError("Foreign installation owner")
    lock = root / ".lock"
    if exists(lock) and (lock.is_symlink() or not lock.is_file()):
        raise InstallError("Invalid installation lock")
    with lock.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise InstallError("Another QP install/remove operation is active") from error
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def source_skills(source: Path) -> list[str]:
    folder = source / "skills"
    if not folder.is_dir() or folder.is_symlink():
        raise InstallError("Source has no canonical skills directory")
    names = []
    for item in sorted(folder.iterdir()):
        if item.name == "__pycache__":
            continue
        if (not item.is_dir() or item.is_symlink() or not NAME.fullmatch(item.name)
                or len(item.name) > 64 or not (item / "SKILL.md").is_file()):
            raise InstallError(f"Source must use skills/<name>/SKILL.md: {item}")
        names.append(item.name)
    if not names:
        raise InstallError("Source contains no skills")
    list(files(folder))
    if not (source / "scripts/distribution.py").is_file():
        raise InstallError("Source lacks its uninstall implementation")
    return names


def guard_external_manager(names: list[str]) -> None:
    state = os.environ.get("XDG_STATE_HOME")
    if state and not Path(state).is_absolute():
        raise InstallError("XDG_STATE_HOME must be absolute")
    lock = Path(state) / "skills/.skill-lock.json" if state else Path.home() / ".agents/.skill-lock.json"
    if exists(lock):
        records = read_json(lock).get("skills", {})
        if not isinstance(records, dict):
            raise InstallError("External Skills CLI lock is invalid; resolve it with that manager")
        overlap = set(names) & records.keys()
        if overlap:
            raise InstallError("Skills CLI owns these names; remove/migrate through that manager first: " + ", ".join(sorted(overlap)))


def collect(root: Path) -> None:
    directory = root / "generations"
    if directory.is_symlink():
        raise InstallError("Generations directory must not be a symlink")
    if not directory.exists():
        return
    active = current(root)
    for folder in directory.iterdir():
        if folder.name != active and GENERATION.fullmatch(folder.name):
            if (folder / "installation.json").is_file():
                manifest(root, folder.name)
                shutil.rmtree(generation(root, folder.name))


def install(source: Path, selected: list[str], dry_run: bool = False) -> None:
    source = source.resolve()
    names = source_skills(source)
    root = location()
    if root.resolve().is_relative_to(source) or source.is_relative_to(root.resolve()):
        raise InstallError("Source and managed installation must not overlap")
    if dry_run and exists(root / "transaction.json"):
        raise InstallError("A pending transaction needs recovery; preview does not mutate it")
    if dry_run:
        prepare(root, source, names, selected, True)
        return
    with locked(root):
        recover(root)
        collect(root)
        prepare(root, source, names, selected, False)


def prepare(root: Path, source: Path, names: list[str], selected: list[str], dry_run: bool) -> None:
    old = current(root)
    previous = manifest(root, old)
    check_links(root, previous)
    hosts = dict(previous["hosts"])
    for host in selected or ([] if hosts else ["codex"]):
        if host == "codex":
            destination = Path.home() / ".agents/skills"
        else:
            destination = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "skills"
        if not destination.is_absolute():
            raise InstallError("Host configuration directories must be absolute")
        if destination.resolve().is_relative_to(root.resolve()):
            raise InstallError("Host destination overlaps the managed store")
        hosts[host] = str(destination)
    guard_external_manager(names)
    planned = {"skills": names, "hosts": hosts}
    prior_links = links(root, previous)
    for link, target in links(root, planned).items():
        if exists(link) and (link not in prior_links or not matches(link, target)):
            raise InstallError(f"Skill collision; existing path is not owned by this installation: {link}")
    if dry_run:
        print(f"Would install {len(names)} skills for {', '.join(hosts)}; update only owned links at {root}")
        return
    generations = root / "generations"
    if generations.is_symlink():
        raise InstallError("Generations directory must not be a symlink")
    generations.mkdir(exist_ok=True)
    identity = uuid.uuid4().hex
    stage = generations / identity
    stage.mkdir()
    try:
        expected = digest(source / "skills")
        shutil.copytree(source / "skills", stage / "skills", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        if digest(stage / "skills") != expected or digest(source / "skills") != expected:
            raise InstallError("Source changed while staging; previous installation is unchanged")
        (stage / "scripts").mkdir()
        shutil.copy2(source / "scripts/distribution.py", stage / "scripts/distribution.py")
        if (source / "agents").is_dir():
            list(files(source / "agents"))
            shutil.copytree(source / "agents", stage / "agents")
        result = subprocess.run(["git", "-C", str(source), "rev-parse", "HEAD"], capture_output=True, text=True, check=False)
        planned.update(format=1, source=SOURCE, revision=result.stdout.strip() if result.returncode == 0 else "local", digest=digest(stage))
        write_json(stage / "installation.json", planned)
        write_json(root / "transaction.json", {"old": old, "new": identity})
        for link, target in links(root, planned).items():
            if not exists(link):
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(target, target_is_directory=True)
        pointer = root / (".current-" + identity)
        pointer.symlink_to("generations/" + identity, target_is_directory=True)
        os.replace(pointer, root / "current")
        recover(root)
    except Exception:
        if exists(root / "transaction.json"):
            recover(root)
        elif stage.exists() and current(root) != identity:
            shutil.rmtree(stage)
        raise
    for link, target in links(root, planned).items():
        if not matches(link, target) or not (link / "SKILL.md").is_file():
            raise InstallError(f"Installed link is not discoverable: {link}")
    print(f"Installed {len(names)} skills for {', '.join(hosts)} at {root / 'current'}. Startup defaults unchanged.")


def uninstall(dry_run: bool = False) -> None:
    root = location()
    if not exists(root):
        print("No QP-owned installation found; other managers are unchanged.")
        return
    if dry_run:
        if exists(root / "transaction.json"):
            raise InstallError("A pending transaction needs recovery; preview does not mutate it")
        data = manifest(root, current(root))
        check_links(root, data)
        print(f"Would remove {len(links(root, data))} owned links; other managers and startup defaults are unchanged.")
        return
    with locked(root):
        recover(root)
        old = current(root)
        if old is not None:
            check_links(root, manifest(root, old))
            write_json(root / "transaction.json", {"old": old, "new": None})
            (root / "current").unlink()
            recover(root)
        collect(root)
    print("QP-owned skills and links removed. Other managers and startup defaults are unchanged.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("install", "uninstall"))
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--codex", action="store_true")
    parser.add_argument("--claude", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        if args.action == "install":
            install(args.source, [h for h in ("codex", "claude") if getattr(args, h)], args.dry_run)
        else:
            if args.codex or args.claude:
                parser.error("Uninstall removes this installation's owned links, not selected hosts")
            uninstall(args.dry_run)
        return 0
    except (InstallError, OSError, ValueError, TypeError) as error:
        print(f"QP: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

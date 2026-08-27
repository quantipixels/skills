from __future__ import annotations

import hashlib
import os
import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

from filelock import FileLock

from .errors import WorkspaceError

OWNER_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_ID_RE = re.compile(r"^\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*(?:-\d+)?$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
ABSENT = "absent"


def _absolute(path: Path) -> Path:
    return Path(os.path.abspath(path))


def _git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=check,
        capture_output=True,
        text=True,
    )


def repository_root(path: Path) -> Path:
    path = _absolute(path)
    if path.is_file():
        path = path.parent
    try:
        return Path(_git(path, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    except (OSError, subprocess.CalledProcessError):
        return path.resolve()


def assert_safe_path(root: Path, target: Path) -> Path:
    root, target = _absolute(root), _absolute(target)
    try:
        relative = target.relative_to(root)
    except ValueError as error:
        raise WorkspaceError("PATH_ESCAPE", "Target is outside the workspace", target=str(target)) from error
    current = root
    if current.exists() and current.is_symlink():
        raise WorkspaceError("SYMLINK_ESCAPE", "Workspace root cannot be a symlink", path=str(current))
    for part in relative.parts:
        current /= part
        if current.exists() and current.is_symlink():
            raise WorkspaceError(
                "SYMLINK_ESCAPE", "Workspace paths cannot traverse symlinks", path=str(current)
            )
    return target


def workspace_root(repo: Path) -> Path:
    root = repository_root(repo)
    return assert_safe_path(root, root / ".qp")


def qp_path(repo: Path, *parts: str) -> Path:
    root = workspace_root(repo)
    return assert_safe_path(root, root.joinpath(*parts))


def workspace_path(repo: Path, path: Path) -> str:
    try:
        return _absolute(path).relative_to(repository_root(repo)).as_posix()
    except ValueError as error:
        raise WorkspaceError("PATH_ESCAPE", "Resource is outside the repository", path=str(path)) from error


def resource_paths(repo: Path, path: Path) -> dict[str, str]:
    return {"absolute_path": str(path), "workspace_path": workspace_path(repo, path)}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        if os.name != "nt":
            directory = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
    finally:
        temporary.unlink(missing_ok=True)


def workspace_lock(repo: Path, identity: str) -> FileLock:
    directory = qp_path(repo, ".locks")
    directory.mkdir(parents=True, exist_ok=True)
    name = hashlib.sha256(identity.encode("utf-8")).hexdigest() + ".lock"
    return FileLock(directory / name, timeout=30)


def safe_owner(value: str) -> str:
    if not OWNER_RE.fullmatch(value):
        raise WorkspaceError("INVALID_OWNER", "Owner must be a canonical ASCII skill name", owner=value)
    return value


def safe_slug(value: str) -> str:
    if not OWNER_RE.fullmatch(value):
        raise WorkspaceError(
            "INVALID_SLUG", "Slug must be lowercase ASCII words separated by hyphens", slug=value
        )
    return value


def safe_subject(value: Any) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 512:
        raise WorkspaceError(
            "INVALID_SUBJECT", "Subject must be a non-empty stable string of at most 512 characters"
        )
    if any(ord(character) < 32 for character in value):
        raise WorkspaceError("INVALID_SUBJECT", "Subject cannot contain control characters")
    return value


def parse_record_ref(value: str) -> tuple[str, str]:
    parts = value.split("/")
    if len(parts) != 2:
        raise WorkspaceError("INVALID_RECORD_REF", "Record reference must be <owner>/<record-id>")
    owner, record_id = safe_owner(parts[0]), parts[1]
    if not RESOURCE_ID_RE.fullmatch(record_id):
        raise WorkspaceError("INVALID_RECORD_ID", "Record ID must be <YYYYMMDD>-<stable-slug>")
    return owner, record_id


def semantic_slug(resource_id: str) -> str:
    if not RESOURCE_ID_RE.fullmatch(resource_id):
        raise WorkspaceError("INVALID_RESOURCE_ID", "Resource ID is not canonical")
    return resource_id[9:]


def record_bundle(repo: Path, record_ref: str) -> Path:
    owner, record_id = parse_record_ref(record_ref)
    return qp_path(repo, "records", owner, record_id)


def record_file(repo: Path, record_ref: str) -> Path:
    return record_bundle(repo, record_ref) / "record.md"


def projection_file(repo: Path, record_ref: str) -> Path:
    bundle = record_bundle(repo, record_ref)
    return bundle / f"{semantic_slug(bundle.name)}.html"


def artifact_bundle(repo: Path, artifact_id: str) -> Path:
    if not RESOURCE_ID_RE.fullmatch(artifact_id):
        raise WorkspaceError("INVALID_ARTIFACT_ID", "Artifact ID must be <YYYYMMDD>-<stable-slug>")
    return qp_path(repo, "artifacts", artifact_id)


def artifact_file(repo: Path, artifact_id: str) -> Path:
    return artifact_bundle(repo, artifact_id) / f"{semantic_slug(artifact_id)}.html"


def initialize_dirs(repo: Path) -> Path:
    root = workspace_root(repo)
    root.mkdir(parents=True, exist_ok=True)
    for name in ("records", "artifacts", ".locks"):
        qp_path(repo, name).mkdir(parents=True, exist_ok=True)
    return root


def allocate(parent: Path, slug: str) -> Path:
    base = f"{datetime.now().astimezone():%Y%m%d}-{safe_slug(slug)}"
    suffix = 1
    while True:
        candidate = parent / (base if suffix == 1 else f"{base}-{suffix}")
        try:
            candidate.mkdir()
            return candidate
        except FileExistsError:
            suffix += 1


def validate_expected_digest(value: str) -> str:
    if value == ABSENT or DIGEST_RE.fullmatch(value):
        return value
    raise WorkspaceError(
        "INVALID_EXPECTED_DIGEST", "Expected digest must be 'absent' or a SHA-256 digest"
    )

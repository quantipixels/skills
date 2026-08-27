from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from .errors import WorkspaceError
from .frontmatter import read_record_data, render_record, required_string, split_record, validate_metadata
from .storage import (
    ABSENT,
    allocate,
    atomic_write,
    initialize_dirs,
    parse_record_ref,
    projection_file,
    qp_path,
    record_bundle,
    record_file,
    safe_owner,
    safe_slug,
    safe_subject,
    digest,
    validate_expected_digest,
    workspace_lock,
    workspace_path,
)


def record_result(repo: Path, owner: str, record_id: str, existing: bool) -> dict[str, Any]:
    ref = f"{owner}/{record_id}"
    bundle = record_bundle(repo, ref)
    record = record_file(repo, ref)
    projection = projection_file(repo, ref)
    return {
        "record_ref": ref,
        "existing": existing,
        "bundle": str(bundle),
        "record": str(record),
        "projection": str(projection),
        "projection_name": projection.name,
        "bundle_workspace_path": workspace_path(repo, bundle),
        "record_workspace_path": workspace_path(repo, record),
        "projection_workspace_path": workspace_path(repo, projection),
    }


def owner_records(repo: Path, owner: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    root = qp_path(repo, "records", safe_owner(owner))
    if not root.exists():
        return [], []
    records: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []
    for bundle in sorted(root.iterdir()):
        path = bundle / "record.md"
        if bundle.is_symlink():
            invalid.append({"path": workspace_path(repo, bundle), "code": "SYMLINK_ESCAPE"})
        elif path.exists():
            try:
                records.append({"path": path, **read_record_data(repo, path)})
            except WorkspaceError as error:
                invalid.append({"path": workspace_path(repo, path), **error.payload()})
    return records, invalid


def resolve_record(
    repo: Path,
    *,
    record_ref: str | None = None,
    owner: str | None = None,
    subject: str | None = None,
    slug: str | None = None,
    create: bool = False,
) -> dict[str, Any]:
    initialize_dirs(repo)
    if record_ref:
        owner, record_id = parse_record_ref(record_ref)
        bundle = record_bundle(repo, record_ref)
        existed = bundle.exists()
        if create and not existed:
            with workspace_lock(repo, f"record-ref:{record_ref}"):
                if bundle.exists():
                    existed = True
                else:
                    bundle.mkdir(parents=True, exist_ok=False)
        return record_result(repo, owner, record_id, existed)
    if owner is None or subject is None:
        raise WorkspaceError("MISSING_RECORD_IDENTITY", "Provide record_ref or owner plus subject")
    owner, subject = safe_owner(owner), safe_subject(subject)
    with workspace_lock(repo, f"subject:{owner}:{subject}"):
        records, invalid = owner_records(repo, owner)
        matches = [item for item in records if item["normalized"]["subject"] == subject]
        legacy = [item for item in records if item["normalized"]["subject"] is None]
        if len(matches) > 1:
            raise WorkspaceError("DUPLICATE_SUBJECT", "Multiple records share this owner and subject")
        if matches:
            return record_result(repo, owner, matches[0]["path"].parent.name, True)
        if not create:
            return {
                "record_ref": None,
                "existing": False,
                "owner": owner,
                "subject": subject,
                "invalid": invalid,
                "legacy": [workspace_path(repo, item["path"]) for item in legacy],
            }
        if legacy:
            raise WorkspaceError(
                "LEGACY_IDENTITY_REQUIRED",
                "Legacy records without subject require an exact record_ref update before subject-based allocation",
                records=[workspace_path(repo, item["path"]) for item in legacy],
            )
        if invalid:
            raise WorkspaceError(
                "INVALID_OWNER_RECORDS",
                "Cannot allocate by subject while owner records are invalid",
                invalid=invalid,
            )
        if slug is None:
            raise WorkspaceError("MISSING_SLUG", "Creating a record requires a stable slug")
        parent = qp_path(repo, "records", owner)
        parent.mkdir(parents=True, exist_ok=True)
        bundle = allocate(parent, slug)
        return record_result(repo, owner, bundle.name, False)


def read_record(repo: Path, record_ref: str) -> dict[str, Any]:
    path = record_file(repo, record_ref)
    if not path.exists():
        raise WorkspaceError("RECORD_NOT_FOUND", "Record does not exist", record_ref=record_ref)
    owner, record_id = parse_record_ref(record_ref)
    data = read_record_data(repo, path)
    return {
        **record_result(repo, owner, record_id, True),
        "metadata": data["metadata"],
        "digest": data["digest"],
    }


def write_record(
    repo: Path,
    record_ref: str,
    frontmatter: Mapping[str, Any],
    body: str,
    expected: str,
) -> dict[str, Any]:
    expected = validate_expected_digest(expected)
    owner, record_id = parse_record_ref(record_ref)
    path = record_file(repo, record_ref)
    initialize_dirs(repo)
    path.parent.mkdir(parents=True, exist_ok=True)
    with workspace_lock(repo, f"record:{record_ref}"):
        current = read_record_data(repo, path) if path.exists() else None
        if current and expected == ABSENT:
            raise WorkspaceError("RECORD_EXISTS", "Record already exists")
        if current and current["digest"] != expected:
            raise WorkspaceError(
                "STALE_WRITE", "Record changed since the caller's exact read", actual=current["digest"]
            )
        if not current and expected != ABSENT:
            raise WorkspaceError("RECORD_MISSING", "Expected record does not exist")

        if required_string(frontmatter, "owner") != owner:
            raise WorkspaceError(
                "RECORD_PATH_MISMATCH", "Frontmatter owner does not match the record reference"
            )
        safe_slug(required_string(frontmatter, "record_type"))
        subject = safe_subject(required_string(frontmatter, "subject"))
        required_string(frontmatter, "title")
        required_string(frontmatter, "status")

        revision = 1
        if current:
            for key in ("owner", "record_type"):
                if current["metadata"].get(key) != frontmatter.get(key):
                    raise WorkspaceError(
                        "IMMUTABLE_RECORD_IDENTITY", f"{key} cannot change", field=key
                    )
            old_subject = current["normalized"]["subject"]
            if old_subject is not None and old_subject != subject:
                raise WorkspaceError(
                    "IMMUTABLE_RECORD_IDENTITY", "subject cannot change", field="subject"
                )
            revision = current["normalized"]["revision"] + 1

        candidate = render_record(frontmatter, body, revision)
        metadata, _ = split_record(candidate)
        validate_metadata(repo, path, metadata)
        latest = digest(path) if path.exists() else None
        if latest != (current["digest"] if current else None):
            raise WorkspaceError("CONCURRENT_CHANGE", "Record changed during the write")
        atomic_write(path, candidate)
        written = read_record_data(repo, path)

    index: dict[str, Any]
    try:
        from .workspace_state import rebuild_index

        index = rebuild_index(repo)
    except WorkspaceError as error:
        index = {"state": "FAILED", "error": error.payload()}
    return {
        **record_result(repo, owner, record_id, True),
        "revision": revision,
        "updated_at": written["metadata"]["updated_at"],
        "digest": written["digest"],
        "index": index,
    }

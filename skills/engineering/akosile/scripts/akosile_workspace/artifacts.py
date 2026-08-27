from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .errors import WorkspaceError
from .storage import (
    allocate,
    artifact_bundle,
    artifact_file,
    initialize_dirs,
    qp_path,
    resource_paths,
    safe_slug,
    workspace_lock,
    workspace_path,
)


def _artifact_result(repo: Path, artifact_id: str, existing: bool) -> dict[str, Any]:
    bundle = artifact_bundle(repo, artifact_id)
    html = artifact_file(repo, artifact_id)
    return {
        "artifact_id": artifact_id,
        "existing": existing,
        "bundle": str(bundle),
        "html": str(html),
        "html_name": html.name,
        "bundle_workspace_path": workspace_path(repo, bundle),
        "html_workspace_path": workspace_path(repo, html),
        **resource_paths(repo, html),
    }


def _find_artifacts(repo: Path, slug: str) -> list[Path]:
    parent = qp_path(repo, "artifacts")
    if not parent.exists():
        return []
    pattern = re.compile(rf"^\d{{8}}-{re.escape(slug)}(?:-\d+)?$")
    return [
        path
        for path in sorted(parent.iterdir())
        if path.is_dir() and not path.is_symlink() and pattern.fullmatch(path.name)
    ]


def resolve_artifact(
    repo: Path,
    *,
    artifact_id: str | None = None,
    slug: str | None = None,
    create: bool = False,
) -> dict[str, Any]:
    if artifact_id:
        bundle = artifact_bundle(repo, artifact_id)
        existing = bundle.exists()
        if not create:
            return _artifact_result(repo, artifact_id, existing)
        initialize_dirs(repo)
        with workspace_lock(repo, f"artifact-id:{artifact_id}"):
            if bundle.exists():
                existing = True
            else:
                bundle.mkdir(parents=True, exist_ok=False)
        return _artifact_result(repo, artifact_id, existing)

    if slug is None:
        raise WorkspaceError("MISSING_ARTIFACT_IDENTITY", "Provide artifact_id or slug")
    slug = safe_slug(slug)
    if not create:
        matches = _find_artifacts(repo, slug)
        if len(matches) > 1:
            raise WorkspaceError(
                "AMBIGUOUS_ARTIFACT", "Multiple artifacts match; use the exact artifact ID"
            )
        if matches:
            return _artifact_result(repo, matches[0].name, True)
        parent = qp_path(repo, "artifacts")
        return {
            "artifact_id": None,
            "existing": False,
            "slug": slug,
            "expected_html_name": f"{slug}.html",
            "artifacts_workspace_path": workspace_path(repo, parent),
        }

    initialize_dirs(repo)
    with workspace_lock(repo, f"artifact-slug:{slug}"):
        matches = _find_artifacts(repo, slug)
        if len(matches) > 1:
            raise WorkspaceError(
                "AMBIGUOUS_ARTIFACT", "Multiple artifacts match; use the exact artifact ID"
            )
        if matches:
            bundle, existing = matches[0], True
        else:
            parent = qp_path(repo, "artifacts")
            parent.mkdir(parents=True, exist_ok=True)
            bundle, existing = allocate(parent, slug), False
        return _artifact_result(repo, bundle.name, existing)

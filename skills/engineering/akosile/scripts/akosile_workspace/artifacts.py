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


def resolve_artifact(
    repo: Path,
    *,
    artifact_id: str | None = None,
    slug: str | None = None,
    create: bool = False,
) -> dict[str, Any]:
    initialize_dirs(repo)
    if artifact_id:
        bundle = artifact_bundle(repo, artifact_id)
        existing = bundle.exists()
        if create and not existing:
            with workspace_lock(repo, f"artifact-id:{artifact_id}"):
                try:
                    bundle.mkdir(parents=True, exist_ok=False)
                except FileExistsError as error:
                    raise WorkspaceError(
                        "ARTIFACT_EXISTS", "Artifact bundle was allocated concurrently"
                    ) from error
    else:
        if slug is None:
            raise WorkspaceError("MISSING_ARTIFACT_IDENTITY", "Provide artifact_id or slug")
        slug = safe_slug(slug)
        with workspace_lock(repo, f"artifact-slug:{slug}"):
            parent = qp_path(repo, "artifacts")
            pattern = re.compile(rf"^\d{{8}}-{re.escape(slug)}(?:-\d+)?$")
            matches = [
                path
                for path in sorted(parent.iterdir())
                if path.is_dir() and pattern.fullmatch(path.name)
            ]
            if len(matches) > 1:
                raise WorkspaceError(
                    "AMBIGUOUS_ARTIFACT", "Multiple artifacts match; use the exact artifact ID"
                )
            if matches:
                bundle, existing = matches[0], True
            elif create:
                bundle, existing = allocate(parent, slug), False
            else:
                return {"artifact_id": None, "existing": False, "slug": slug}
            artifact_id = bundle.name
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

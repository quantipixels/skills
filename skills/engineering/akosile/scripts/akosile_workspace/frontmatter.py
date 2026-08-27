from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import yaml

from .errors import WorkspaceError
from .storage import assert_safe_path, digest, qp_path, safe_owner, safe_subject, workspace_root


class FrontmatterLoader(yaml.SafeLoader):
    """Safe YAML loader that retains timestamps as strings and rejects duplicate keys."""


FrontmatterLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in rules if tag != "tag:yaml.org,2002:timestamp"]
    for key, rules in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _unique_mapping(
    loader: FrontmatterLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise yaml.constructor.ConstructorError(
                "while constructing frontmatter",
                node.start_mark,
                "frontmatter keys must be unique strings",
                key_node.start_mark,
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


FrontmatterLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _unique_mapping)


def parse_timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise WorkspaceError("INVALID_UPDATED_AT", "updated_at must be an offset-aware ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as error:
        raise WorkspaceError(
            "INVALID_UPDATED_AT", "updated_at must be an offset-aware ISO-8601 string"
        ) from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise WorkspaceError("INVALID_UPDATED_AT", "updated_at must include a UTC offset")
    return parsed.astimezone(timezone.utc)


def split_record(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise WorkspaceError("INVALID_FRONTMATTER", "Record must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise WorkspaceError("INVALID_FRONTMATTER", "Record frontmatter is not terminated")
    try:
        metadata = yaml.load(text[4:end], Loader=FrontmatterLoader) or {}
    except yaml.YAMLError as error:
        raise WorkspaceError(
            "INVALID_FRONTMATTER", "Record frontmatter is not valid YAML", error=str(error)
        ) from error
    if not isinstance(metadata, dict) or any(not isinstance(key, str) for key in metadata):
        raise WorkspaceError("INVALID_FRONTMATTER", "Record frontmatter must be a string-key mapping")
    return metadata, text[end + 5 :]


def required_string(metadata: Mapping[str, Any], key: str) -> str:
    value = metadata.get(key)
    if not isinstance(value, str) or not value.strip():
        raise WorkspaceError("INVALID_RECORD", f"{key} must be a non-empty string", field=key)
    return value


def validate_metadata(repo: Path, path: Path, metadata: Mapping[str, Any]) -> dict[str, Any]:
    owner = safe_owner(required_string(metadata, "owner"))
    record_type = required_string(metadata, "record_type")
    subject_value = metadata.get("subject")
    subject = safe_subject(subject_value) if subject_value is not None else None
    title = required_string(metadata, "title")
    status = required_string(metadata, "status")
    instant = parse_timestamp(metadata.get("updated_at"))
    revision = metadata.get("revision")
    if isinstance(revision, bool) or not isinstance(revision, int) or revision < 1:
        raise WorkspaceError("INVALID_RECORD", "revision must be a positive integer", field="revision")
    candidate = metadata.get("candidate")
    if candidate is not None and (not isinstance(candidate, str) or not candidate.strip()):
        raise WorkspaceError("INVALID_RECORD", "candidate must be a non-empty string when present")
    expected = qp_path(repo, "records", owner, path.parent.name, "record.md")
    if path.resolve(strict=False) != expected.resolve(strict=False):
        raise WorkspaceError("RECORD_PATH_MISMATCH", "Record path does not match its owner and record ID")
    return {
        "owner": owner,
        "record_type": record_type,
        "subject": subject,
        "title": title,
        "status": status,
        "instant": instant,
        "revision": revision,
        "candidate": candidate,
    }


def read_record_data(repo: Path, path: Path) -> dict[str, Any]:
    assert_safe_path(workspace_root(repo), path)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise WorkspaceError("INVALID_RECORD_ENCODING", "Record must be UTF-8", path=str(path)) from error
    metadata, body = split_record(text)
    return {
        "metadata": metadata,
        "body": body,
        "normalized": validate_metadata(repo, path, metadata),
        "digest": digest(path),
    }


def render_record(frontmatter: Mapping[str, Any], body: str, revision: int) -> str:
    if not isinstance(frontmatter, Mapping):
        raise WorkspaceError("INVALID_FRONTMATTER_INPUT", "Frontmatter input must be a JSON object")
    if "revision" in frontmatter or "updated_at" in frontmatter:
        raise WorkspaceError("RESERVED_RECORD_FIELD", "revision and updated_at are assigned by Akọsílẹ̀")
    ordered: dict[str, Any] = {}
    for key in ("owner", "record_type", "subject", "title"):
        if key in frontmatter:
            ordered[key] = frontmatter[key]
    ordered["updated_at"] = datetime.now(timezone.utc).isoformat()
    ordered["revision"] = revision
    if frontmatter.get("candidate") is not None:
        ordered["candidate"] = frontmatter["candidate"]
    if "status" in frontmatter:
        ordered["status"] = frontmatter["status"]
    for key, value in frontmatter.items():
        if key not in ordered:
            ordered[key] = value
    header = yaml.safe_dump(ordered, allow_unicode=True, sort_keys=False, width=1000)
    normalized_body = body if body.endswith("\n") else body + "\n"
    return f"---\n{header}---\n\n{normalized_body}"

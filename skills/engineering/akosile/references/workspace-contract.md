# Workspace contract

Use this reference for the repository-local `.qp` v0 root, paths, common record fields, safe writes, direct user access, and the generated index.

## Root and layout

For `v0-experiment`, the canonical workspace root is exactly `<repository>/.qp`. Akọsílẹ̀ normally resolves and constructs this root and its record/artifact paths; semantic owners keep ownership of the resulting content.

```text
.qp/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
└── artifacts/<artifact-id>/
```

New records use owner-first paths. Do not introduce open-ended roots such as `.qp/plans`, `.qp/architecture`, `.qp/reports`, `.qp/research`, `.qp/triage`, or `.qp/findings`. Existing legacy paths remain readable, but new QP writes do not use them.

If Akọsílẹ̀ cannot be invoked, use these canonical paths directly. Do not create an alternate workspace layout or require each semantic skill to define its own fallback behavior.

Global `~/.qp` storage is deferred. Do not add project registries, checkout resolution, global/project settings precedence, or automatic local-to-global migration until observed cross-project discovery or continuity failures justify that architecture.

## Identity

- Owner is the canonical ASCII skill `name`.
- Record and artifact IDs use `<YYYYMMDD>-<stable-slug>` with a numeric suffix on collision.
- Prefer an exact record path or candidate identity before slug matching.
- Keep the directory stable across title, status, and projection changes.
- Reject absolute paths as identifiers, path separators in identifiers, `.`/`..`, symlink escape, secrets in identifiers, and targets outside the resolved repository `.qp` root.

## Common record fields

A record may add owner-specific fields, but frontmatter needs only:

```yaml
owner: <canonical-skill-name>
record_type: <owner-native type>
title: <human title>
updated_at: <offset-aware timestamp>
revision: <positive integer>
candidate: <exact subject identity, optional>
status: <owner-native state>
```

The record ID and bundle are derived from the path. The semantic owner defines valid record types, statuses, transitions, evidence, and body structure.

## Safe writes

For an existing record or settings file:

1. Read and retain its digest.
2. Build the complete candidate separately.
3. Validate the candidate before replacement.
4. Recheck the current digest immediately before writing.
5. Atomically replace the file.
6. Reread it.
7. Rebuild `INDEX.md` after a record write.

For records, revision starts at `1` and increments by exactly one. A failed index rebuild does not invalidate a successfully verified record.

## Index

`.qp/INDEX.md` is generated directly from valid `record.md` frontmatter and sorted by `updated_at` descending. It displays owner, record type, title, native status, record link, and optional HTML view. Invalid records appear in a separate diagnostic section.

The index is navigation, not semantic state. Users edit records or settings, not the index.

## Direct user access

When a resource is produced for direct user consumption, return both:

```text
Absolute path: <resolved absolute filesystem path>
Workspace path: <path relative to repository root, beginning .qp/...>
```

The absolute path is for immediate opening, attachment, or tool use. The workspace-relative path is the stable project-local reference. Do not use an absolute machine path as the canonical source identity inside portable records or HTML unless explicitly required.

## Git hygiene

`.qp` is generated local state. Prefer existing ignore rules; otherwise use repository-local Git exclude when workspace setup is allowed. Never stage or publish `.qp` through QP workflows.

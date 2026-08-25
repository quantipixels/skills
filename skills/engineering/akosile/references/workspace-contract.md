# Workspace contract

Use this reference for the repository-local `.qp` v0 root, paths, common record fields, safe writes, direct user access, and the generated index.

## Root and layout

For `v0-experiment`, resolve the Git worktree root when available; the canonical workspace is exactly `<repository>/.qp`. Akọsílẹ̀ constructs record/artifact locations from this contract while semantic owners keep ownership of the resulting content.

```text
.qp/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
└── artifacts/<artifact-id>/
```

New records use owner-first paths. Do not introduce open-ended roots such as `.qp/plans`, `.qp/architecture`, `.qp/reports`, `.qp/research`, `.qp/triage`, or `.qp/findings`. Existing legacy paths remain readable, but new QP writes do not use them.

Global `~/.qp` storage is deferred. Do not add project registries, checkout resolution, global/project settings precedence, or automatic local-to-global migration until observed cross-project discovery or continuity failures justify that architecture.

## Record-bundle slots

Within an owner-record bundle, these relative slots are canonical when needed:

```text
record.md      semantic owner record
index.html     optional human HTML projection
receipts/      optional supporting-owner or checkpoint receipts
evidence/      optional retained supporting evidence
```

Semantic skills may refer to these slots relative to the resolved owner bundle without repeating `.qp/records/<owner>/<record-id>/`. They describe bundle roles, not new workspace roots.

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

1. Read the exact current target before building the candidate.
2. Build and validate the complete replacement separately.
3. Immediately before replacement, reread the target.
4. If the target changed, stop and reconcile instead of overwriting it.
5. Replace the complete file using the host's safe filesystem capability.
6. Reread the written result.
7. Rebuild `INDEX.md` after a record write.

For records, revision starts at `1` and increments by exactly one. A failed index rebuild does not invalidate a successfully verified record.

## Index

`.qp/INDEX.md` is generated directly from valid `record.md` frontmatter and sorted by the chronological instant represented by `updated_at`, newest first. It displays owner, record type, title, native status, record link, and optional HTML view. Invalid records appear in a separate diagnostic section.

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

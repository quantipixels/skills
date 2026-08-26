# Workspace contract

Use this reference for QP workspace roots, owner-first paths, common record fields, safe writes, direct user access, indexing, and scope isolation.

## Scope and authority

Resolve exactly one scope per operation:

```text
repository -> <git-worktree>/.qp
personal   -> ${QP_HOME:-$HOME/.qp}
```

Repository scope is the default for repository-local records/artifacts.

Personal scope requires an explicit current user instruction authorizing personal/cross-project access for the operation. A semantic owner may request path resolution only after that authority is established. Existing files, prior skill selection, or a semantic owner's own instruction do not grant access.

Do not automatically copy, merge, migrate, or synchronize records between scopes.

## Layout

Both scopes use:

```text
<root>/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
└── artifacts/<artifact-id>/
```

Do not create extra semantic roots such as `plans`, `research`, `findings`, or `patterns`; semantic owners use owner-first records.

Within a record bundle:

```text
record.md      semantic owner record
index.html     optional human HTML projection
receipts/      optional supporting/checkpoint/publication receipts
evidence/      optional retained supporting evidence
```

## Identity

- Owner is the canonical ASCII skill `name`.
- Record/artifact IDs use `<YYYYMMDD>-<stable-slug>` with a numeric suffix on collision.
- Prefer an exact path or candidate identity before slug matching.
- Keep the directory stable across title/status/projection changes.
- Reject absolute paths as identifiers, separators in identifiers, `.`/`..`, symlink escape, secrets in identifiers, and targets outside the resolved root.

## Common record fields

```yaml
owner: <canonical-skill-name>
record_type: <owner-native type>
title: <human title>
updated_at: <offset-aware timestamp>
revision: <positive integer>
candidate: <exact subject identity, optional>
status: <owner-native state>
```

The semantic owner defines additional fields, record types, statuses, transitions, evidence, and body structure.

## Safe writes

For an existing record or settings file:

1. Read the exact current target.
2. Build and validate the complete replacement separately.
3. Immediately before replacement, reread the target.
4. If it changed, stop and reconcile.
5. Replace the complete file safely.
6. Reread the written result.
7. Rebuild that scope's `INDEX.md` after a record write.

Record revision starts at `1` and increments by exactly one. A failed index rebuild does not invalidate a successfully verified record.

## Index

Each scope has an independent `INDEX.md`, generated from valid `record.md` frontmatter and sorted by `updated_at`, newest first. It displays owner, record type, title, native status, record link, and optional HTML view. Invalid records appear in a diagnostic section.

The index is navigation, not semantic state.

## Direct user access

Repository scope:

```text
Absolute path: <resolved absolute path>
Workspace scope: repository
Workspace path: .qp/<relative path>
```

Personal scope:

```text
Absolute path: <resolved absolute path>
Workspace scope: personal
Workspace path: <path relative to the personal root>
```

Do not use an absolute machine path as portable canonical identity inside records or HTML unless explicitly required.

## Repository Git hygiene

Repository `.qp` is generated local state. Prefer existing ignore rules; otherwise use repository-local Git exclude when workspace setup is allowed. Never stage or publish repository `.qp` through QP workflows.

## Personal privacy

When supported, create personal directories as user-only and files as user-read/write only. Do not attach, publish, quote, or search personal records beyond the exact authorized task.

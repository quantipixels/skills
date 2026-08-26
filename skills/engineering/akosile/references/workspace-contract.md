# Workspace contract

Use this reference for QP workspace roots, owner-first paths, common record fields, safe writes, direct user access, indexing, and scope isolation.

## Scope and roots

Resolve exactly one scope for each operation:

```text
repository -> <git-worktree>/.qp
personal   -> ${QP_HOME:-$HOME/.qp}
```

Repository scope is the default for repository-local records/artifacts. Personal scope requires an explicit user request or an explicit semantic-owner request for personal/cross-project state. Existing personal files do not grant authority to read or write them.

Both scopes use:

```text
<root>/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
└── artifacts/<artifact-id>/
```

Do not create extra semantic roots such as `plans`, `research`, `findings`, or `patterns`; semantic owners use owner-first records. Do not automatically copy, merge, migrate, or synchronize records between personal and repository scopes.

## Record-bundle slots

Within an owner-record bundle:

```text
record.md      semantic owner record
index.html     optional human HTML projection
receipts/      optional supporting-owner/checkpoint/publication receipts
evidence/      optional retained supporting evidence
```

These are bundle roles, not new workspace roots.

## Identity

- Owner is the canonical ASCII skill `name`.
- Record and artifact IDs use `<YYYYMMDD>-<stable-slug>` with a numeric suffix on collision.
- Prefer an exact record path or candidate identity before slug matching.
- Keep the directory stable across title, status, and projection changes.
- Reject absolute paths as identifiers, path separators in identifiers, `.`/`..`, symlink escape, secrets in identifiers, and targets outside the resolved scope root.

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

The semantic owner defines record types, statuses, transitions, evidence, and body structure.

## Safe writes

For an existing record or settings file:

1. Read the exact current target.
2. Build and validate the complete replacement separately.
3. Immediately before replacement, reread the target.
4. If it changed, stop and reconcile.
5. Replace the complete file with the host's safe filesystem capability.
6. Reread the written result.
7. Rebuild that scope's `INDEX.md` after a record write.

Record revision starts at `1` and increments by exactly one. A failed index rebuild does not invalidate a successfully verified record.

## Index

Each scope has an independent `INDEX.md`, generated from valid `record.md` frontmatter and sorted by the instant represented by `updated_at`, newest first. It displays owner, record type, title, native status, record link, and optional HTML view. Invalid records appear in a diagnostic section.

The index is navigation, not semantic state.

## Direct user access

When a generated resource is intended for direct use, return:

```text
Absolute path: <resolved path>
Workspace scope: repository | personal
Workspace path: <path relative to that scope root>
```

Do not use an absolute machine path as the portable canonical identity inside records or HTML unless explicitly required.

## Repository Git hygiene

Repository `.qp` is generated local state. Prefer existing ignore rules; otherwise use repository-local Git exclude when workspace setup is allowed. Never stage or publish repository `.qp` through QP workflows.

## Personal privacy

Personal scope is user-owned local state. When supported, create directories as user-only and files as user-read/write only. Do not attach, publish, or quote personal evidence outside the authorized task merely because a semantic owner can derive a portable result from it.

# Workspace contract

Use this reference for the repository-local `.qp` root, shared paths, common record envelope, focused safe-write/index helpers, direct user access, and generated navigation.

## Root and layout

Resolve the Git worktree root when available; the canonical workspace is exactly `<repository>/.qp`.

```text
.qp/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
│   ├── record.md
│   ├── <record-slug>.html       # optional owner projection
│   ├── receipts/                # optional
│   └── evidence/                # optional
└── artifacts/<artifact-id>/
    └── <artifact-slug>.html
```

New records use owner-first paths. Do not introduce open-ended roots such as `.qp/plans`, `.qp/architecture`, `.qp/reports`, `.qp/research`, `.qp/triage`, `.qp/findings`, or `.qp/state`.

This version supports repository-local `.qp` only. Do not add a global registry, daemon, synchronizer, global/project precedence, or automatic local-to-global migration.

## Identity and naming

- Owner is the canonical ASCII skill `name`.
- Record and artifact IDs use `<YYYYMMDD>-<stable-slug>` with a numeric suffix on collision.
- Prefer an exact supplied path or exact candidate identity before slug matching.
- Keep the allocated directory stable across title, status, candidate, and projection changes.
- Use the actual allocated slug as the HTML filename, including a collision suffix: `<stable-slug>.html`.
- New QP writes never use `index.html` as an artifact or projection entrypoint.
- Reject absolute identifiers, separators inside owner/slug, `.`/`..`, secret-bearing identifiers, symlink traversal, and destinations outside `.qp`.

Use native filesystem creation for allocation. Directory creation is already atomic; if the desired ID exists, select the next numeric suffix.

## Common record fields

A record may add owner-specific fields, but frontmatter needs:

```yaml
owner: <canonical-skill-name>
record_type: <owner-native type>
title: <human title>
updated_at: <offset-aware timestamp>
revision: <positive integer>
candidate: <exact current candidate, optional>
status: <owner-native state>
```

The semantic owner defines valid record types, statuses, transitions, evidence, candidate meaning, revision policy, timestamp policy, and body structure. Akọsílẹ̀'s index renderer validates only this shared mechanical envelope and owner/path agreement.

## Focused safe writes

Use `scripts/safe-write.py`; do not build a workspace command layer around it.

The semantic owner:

1. selects the exact target and an external temporary snapshot path;
2. requests one locked snapshot whose bytes and digest come from the same read;
3. builds and semantically validates the complete replacement from that snapshot; and
4. supplies the `.qp` root, exact target, candidate file, and snapshot digest.

The helper:

1. verifies the target resolves within the supplied root;
2. takes a per-target file lock;
3. reads the exact target bytes once and copies those bytes to the external snapshot;
4. returns the digest of those same bytes, or `absent` for a missing target;
5. on write, rereads and fingerprints the target under the same lock;
6. rejects a stale expected digest;
7. atomically replaces the complete file; and
8. rereads and verifies the written digest.

Snapshot output must remain outside `.qp`. The helper does not allocate workspace paths, interpret frontmatter, assign revisions or timestamps, choose recovery, or retry stale writes. A stale write returns to the semantic owner for reconciliation.

Hidden sibling lock files are mechanical coordination files, not records or registry state. They may remain after successful operations.

## Generated index

Use `scripts/render-index.py` to produce a separate `INDEX.md` candidate outside `.qp`. Do not let the renderer mutate the authoritative workspace.

The renderer reads mechanically valid `record.md` frontmatter and sorts by the chronological instant represented by `updated_at`, newest first. It displays owner, record type, title, native status, record link, and the expected real slug-named HTML view when that file exists.

Malformed records and legacy `index.html` entrypoints appear diagnostically rather than disappearing. Records remain authoritative.

To publish the candidate, snapshot `.qp/INDEX.md` first, render the candidate, then replace `INDEX.md` through `safe-write.py` with the snapshot digest. A failed or stale index refresh does not invalidate a successfully verified record write.

## Direct user access

For a generated resource intended for direct use, return:

```text
Absolute path: <resolved absolute filesystem path>
Workspace path: <path relative to repository root, beginning .qp/...>
```

The workspace path is the stable project-local reference. Do not embed machine-specific absolute paths as portable source identity.

## Git hygiene

`.qp` is generated local state. Prefer existing ignore rules; otherwise use repository-local Git exclude. Never stage or publish `.qp` through QP workflows.

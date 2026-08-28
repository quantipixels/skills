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

The semantic owner defines valid record types, statuses, transitions, evidence, candidate meaning, revision policy, timestamp policy, and body structure. Akọsílẹ̀'s index helper validates only this shared mechanical envelope and owner/path agreement.

## Focused safe writes

Use `scripts/safe-write.py`; do not build a workspace command layer around it.

The semantic owner:

1. reads the exact current target;
2. records its digest, or `absent` when creating it;
3. builds and semantically validates the complete replacement separately; and
4. supplies the `.qp` root, exact target, candidate file, and expected digest.

The helper:

1. verifies the target resolves within the supplied root;
2. takes a per-target file lock;
3. rereads and fingerprints the target under the lock;
4. rejects a stale expected digest;
5. atomically replaces the complete file;
6. fsyncs where supported; and
7. rereads and verifies the written digest.

The helper does not allocate paths, interpret frontmatter, assign revisions or timestamps, choose recovery, or retry stale writes. A stale write returns to the semantic owner for reconciliation.

Hidden sibling lock files are mechanical coordination files, not records or registry state. They may remain after successful operations.

## Generated index

Use `scripts/rebuild-index.py` after record writes or when navigation is stale.

`.qp/INDEX.md` is generated from mechanically valid `record.md` frontmatter and sorted by the chronological instant represented by `updated_at`, newest first. It displays owner, record type, title, native status, record link, and the expected real slug-named HTML view when that file exists.

Malformed records and legacy `index.html` entrypoints appear diagnostically rather than disappearing. Records remain authoritative; users and semantic owners do not edit the generated index.

A failed index rebuild does not invalidate a successfully verified record write.

## Direct user access

For a generated resource intended for direct use, return:

```text
Absolute path: <resolved absolute filesystem path>
Workspace path: <path relative to repository root, beginning .qp/...>
```

The workspace path is the stable project-local reference. Do not embed machine-specific absolute paths as portable source identity.

## Git hygiene

`.qp` is generated local state. Prefer existing ignore rules; otherwise use repository-local Git exclude. Never stage or publish `.qp` through QP workflows.

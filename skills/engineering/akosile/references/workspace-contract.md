# Workspace contract

Use this reference for the repository-scoped `.qp` home, owner-first paths, common record envelope, safe writes, generated indexing, and direct-access receipts.

## Canonical home

`.qp` is repository-scoped state.

- single worktree: `<worktree>/.qp` is the real workspace;
- linked worktrees: `<main-worktree>/.qp` is the one real workspace and every linked worktree exposes a symlink to it;
- the main/canonical `.qp` must not itself be a symlink;
- pass the resolved real canonical root to Akọsílẹ̀ scripts;
- do not create alternate semantic roots or global `~/.qp` machinery.

Read [worktrees](worktrees.md) for inventory, migration, symlink, and repair behavior.

## Layout and identity

```text
.qp/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
│   ├── record.md
│   ├── index.html          # optional human projection
│   ├── receipts/           # optional
│   └── evidence/           # optional
└── artifacts/<artifact-id>/
    └── index.html
```

- Owner is the canonical ASCII skill name.
- Semantic owners provide record/artifact kind, stable subject, and semantic content; Akọsílẹ̀ resolves canonical paths and collision suffixes.
- Record/artifact IDs use `<YYYYMMDD>-<stable-slug>` and `-2`, `-3`, etc. on collision.
- Allocate directories with native atomic creation and keep the allocated bundle stable across semantic changes.
- Prefer exact record path or candidate identity before subject/title matching.
- Reject unsafe identifiers, secrets, symlink traversal inside the canonical workspace, and destinations outside `.qp`.

## Common record envelope

Owner records may add fields, but generated navigation requires:

```yaml
owner: <canonical-skill-name>
record_type: <owner-native type>
title: <human title>
updated_at: <offset-aware timestamp>
revision: <positive integer>
candidate: <exact current candidate, optional>
status: <owner-native state>
```

The semantic owner defines valid types, statuses, transitions, candidate meaning, revision/timestamp policy, evidence, and body structure. Akọsílẹ̀ validates only the shared mechanical envelope and owner/path agreement for indexing.

## Exact snapshot and compare-and-swap

Use `scripts/safe-write.py` rather than a workspace command layer.

For an existing target:

1. select an external temporary snapshot path;
2. run `snapshot`; it reads the target bytes once, copies those exact bytes outside `.qp`, and returns their digest;
3. build and semantically validate the complete candidate only from that snapshot;
4. run `write` with the returned digest.

For a missing target, `snapshot` returns `digest: absent` and removes any stale supplied snapshot output.

On write, the helper verifies containment under the real canonical root, holds a per-target lock, reads/hashes under that lock, rejects a stale expected digest, atomically replaces the complete file, and verifies the written bytes.

It does not create parent paths, allocate IDs, parse semantic data, assign revision/timestamp, select recovery, or retry. A stale result returns to the semantic owner. Hidden sibling lock files are mechanical coordination state, not records.

## Generated index

`scripts/render-index.py` reads canonical `.qp/records/*/*/record.md` and writes one candidate outside `.qp`. It:

- parses YAML with duplicate-key detection;
- validates the common envelope and owner/path agreement;
- sorts `updated_at` by chronological instant;
- links `index.html` when present; and
- reports malformed records.

It cannot mutate `.qp`. Snapshot `INDEX.md`, render the external candidate, then publish it through `safe-write.py write`. Records remain authoritative; a failed/stale index refresh does not invalidate a verified record write.

## Settings and repair

`settings.json` is a sparse JSON object. Akọsílẹ̀ preserves it as an opaque whole; each consuming skill owns its section. Never overwrite malformed settings as repair.

Use native Git/filesystem inspection for setup, allocation, worktree aliasing, diagnosis, and bounded repair. Repair only missing/derived infrastructure or a proved alias defect; do not infer semantic record changes.

## Direct access and Git hygiene

For generated resources intended for direct use, return:

```text
Absolute path: <resolved absolute filesystem path>
Workspace path: <repository-relative .qp/... path>
```

Keep `.qp` outside Git through existing rules or repository-local Git exclude. Never stage or publish it through QP workflows.
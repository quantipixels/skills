# Workspace contract

Use this reference for repository-local `.qp` paths, the common record envelope, focused safe writes, generated indexing, and direct-access receipts.

## Layout and naming

```text
.qp/
├── settings.json
├── INDEX.md
├── records/<owner>/<record-id>/
│   ├── record.md
│   ├── <record-slug>.html       # optional projection
│   ├── receipts/                # optional
│   └── evidence/                # optional
└── artifacts/<artifact-id>/
    └── <artifact-slug>.html
```

- Resolve the Git worktree root when available; the workspace is exactly `<repository>/.qp`.
- Owner is the canonical ASCII skill name.
- Record/artifact IDs use `<YYYYMMDD>-<stable-slug>` and `-2`, `-3`, etc. on collision.
- Allocate with native atomic directory creation.
- Keep allocated directories stable across semantic changes.
- Use the actual allocated slug as the HTML filename, including a collision suffix.
- New QP projections and artifacts never use `index.html`.
- Reject unsafe identifiers, secrets, symlink traversal, and destinations outside `.qp`.
- Do not add alternate semantic roots or global `~/.qp` machinery.

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

1. Select an external temporary snapshot path.
2. Run `snapshot`; it reads the target bytes once, copies those exact bytes outside `.qp`, and returns their digest.
3. Build and semantically validate the complete candidate only from that snapshot.
4. Run `write` with the returned digest.

For a missing target, `snapshot` returns `digest: absent` and removes any stale supplied snapshot output.

On write, the helper:

1. verifies the target resolves within the supplied root;
2. holds a per-target lock;
3. reads and hashes the target under that lock;
4. rejects a stale expected digest;
5. atomically replaces the complete file; and
6. verifies the written bytes.

It does not create parent paths, allocate IDs, parse semantic data, assign revision/timestamp, select recovery, or retry. A stale result returns to the semantic owner.

Hidden sibling lock files are mechanical coordination state, not records.

## Generated index

`scripts/render-index.py` reads `.qp/records/*/*/record.md` and writes one candidate outside `.qp`. It:

- parses YAML with duplicate-key detection;
- validates the common envelope and owner/path agreement;
- sorts `updated_at` by chronological instant;
- links `<record-slug>.html` when present; and
- reports malformed records and legacy `index.html` entrypoints.

It cannot mutate `.qp`. Snapshot `INDEX.md`, render the external candidate, then publish it through `safe-write.py write`. Records remain authoritative; a failed or stale index refresh does not invalidate a verified record write.

## Settings and repair

`settings.json` is a sparse JSON object. Akọsílẹ̀ preserves it as an opaque whole; each consuming skill owns its section. Never overwrite malformed settings as repair.

Use native inspection and filesystem commands for setup, diagnosis, and bounded repair. Repair only missing or derived infrastructure; do not infer semantic record changes or migrate legacy files automatically.

## Direct access and Git hygiene

For generated resources intended for direct use, return:

```text
Absolute path: <resolved absolute filesystem path>
Workspace path: <repository-relative .qp/... path>
```

Keep `.qp` outside Git through existing rules or repository-local Git exclude. Never stage or publish it through QP workflows.

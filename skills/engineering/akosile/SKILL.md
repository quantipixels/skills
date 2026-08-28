---
name: akosile
description: Initialize and maintain one repository-local QP `.qp` workspace. Use for owner-first record or artifact paths, exact snapshot-based record/settings replacement, deterministic index rendering, or bounded workspace repair. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, project knowledge, and global `~/.qp` storage.
compatibility: Requires Git. The two deterministic helpers require Python 3, PyYAML, and filelock.
---

# Akọsílẹ̀

Own the shared repository-local `.qp` convention. Semantic skills own record meaning; Akọsílẹ̀ owns common placement, safe replacement, and generated navigation.

Use normal Git, filesystem, shell, and search capabilities for repository discovery, initialization, lookup, path selection, directory allocation, diagnosis, repair, and Git exclude. Do not reproduce those capabilities in a workspace runtime.

Keep code at two deterministic seams only:

```text
safe-write.py
→ exact snapshot bytes + matching digest, or locked compare-and-swap replacement

render-index.py
→ current record frontmatter → external INDEX.md candidate
```

Read [workspace contract](references/workspace-contract.md) before record, artifact, write, or index work. Read [settings](references/settings.md) only when settings are involved.

## Establish the workspace natively

Resolve the Git worktree root when available and use exactly `<repository>/.qp`. Create only missing infrastructure:

```text
.qp/
├── settings.json
├── INDEX.md
├── records/
└── artifacts/
```

Initialize missing `settings.json` as `{}`. Create owner/artifact directories lazily. Preserve malformed or existing user files during initialization or repair. Use existing ignore rules or repository-local Git exclude; do not edit tracked `.gitignore` merely for setup.

A global `~/.qp` root is not supported.

## Resolve paths directly

Records use:

```text
.qp/records/<owner>/<YYYYMMDD-stable-slug>/record.md
.qp/records/<owner>/<YYYYMMDD-stable-slug>/<stable-slug>.html
```

Standalone artifacts use:

```text
.qp/artifacts/<YYYYMMDD-stable-slug>/<stable-slug>.html
```

Use the exact ASCII skill name as owner. Prefer an exact supplied path or candidate identity before title matching. Allocate directories with native atomic creation; on collision use `-2`, `-3`, and so on. The HTML filename uses the actual allocated slug, including its collision suffix.

Do not create new QP artifacts or projections as `index.html`. Reject unsafe identifiers, secrets, symlink escape, and destinations outside `.qp`.

## Replace exact files safely

The semantic owner supplies and validates the complete replacement, including native status, revision, timestamp, candidate identity, owner-specific fields, and body.

Take one exact snapshot whose bytes and digest cannot diverge:

```bash
python3 <skill-root>/scripts/safe-write.py snapshot \
  --root <repository>/.qp \
  --target <target> \
  --output <temporary-snapshot-outside-.qp>
```

Build an existing-file candidate only from that snapshot, then replace it through:

```bash
python3 <skill-root>/scripts/safe-write.py write \
  --root <repository>/.qp \
  --target <target> \
  --candidate <complete-candidate-file> \
  --expected <snapshot-digest-or-absent>
```

The helper owns only path containment, exact snapshotting, the per-target write lock, under-lock digest comparison, atomic replacement, and readback verification. It does not create paths, allocate IDs, parse semantic content, assign metadata, choose recovery, or retry.

On `STALE_TARGET`, take a new snapshot and reconcile.

## Refresh generated navigation

Snapshot `.qp/INDEX.md`, render a separate candidate, then publish it through the same safe-write helper:

```bash
python3 <skill-root>/scripts/render-index.py \
  --workspace <repository>/.qp \
  --output <temporary-index-candidate-outside-.qp>
```

The renderer parses the common YAML envelope, sorts offset-aware timestamps by instant, links real slug-named projections, and surfaces invalid records or legacy `index.html` entrypoints. It cannot write inside `.qp`; records remain authoritative.

## Report

Return the workspace, affected resource, changed items, index and Git-hygiene state, conflicts or limits, and—when generated for direct use—both:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

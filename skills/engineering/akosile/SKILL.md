---
name: akosile
description: Initialize and maintain one repository-scoped QP `.qp` workspace across Git worktrees. Use for owner-first record/artifact paths, worktree-safe workspace migration or repair, exact snapshot-based replacement, and deterministic index rendering. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, project knowledge, and global `~/.qp` storage.
compatibility: Requires Git. Current deterministic helpers require Python 3, PyYAML, and filelock. Linked-worktree aliases require filesystem symlink support.
---

# Akọsílẹ̀

Own the repository-local `.qp` workspace contract. Semantic skills own what records mean; Akọsílẹ̀ owns the canonical workspace home, owner-first paths and allocation, worktree aliases/migration, safe replacement protocol, and generated navigation.

Use native Git, filesystem, shell, and search capabilities to execute discovery, directory allocation, symlink creation, inspection, Git exclude, and bounded repair. Do not reproduce those capabilities in a workspace runtime.

The current design uses two bundled deterministic seams:

```text
safe-write.py
→ exact snapshot bytes + matching digest, or locked compare-and-swap replacement

render-index.py
→ current record frontmatter → external INDEX.md candidate
```

They are current justified seams, not a permanent numeric limit. Any future executable addition must pass Kọ Skill's script boundary.

Read [workspace contract](references/workspace-contract.md) before record, artifact, write, or index work. Read [worktrees](references/worktrees.md) when linked worktrees exist, `.qp` may be split across worktrees, or workspace migration/alias repair is needed. Read [settings](references/settings.md) only when settings are involved.

## Establish one repository workspace

For an ordinary single-worktree repository, the workspace is `<worktree>/.qp`.

For a repository with linked worktrees, resolve the main worktree through `git worktree list --porcelain -z`. The main worktree owns the one real `.qp` directory; every linked worktree exposes a symlink to it. Never create a second physical `.qp` merely because work is running in another worktree.

Create only missing canonical infrastructure:

```text
.qp/
├── settings.json
├── INDEX.md
├── records/
└── artifacts/
```

Initialize missing `settings.json` as `{}`. Create owner/artifact directories lazily. Preserve existing or malformed user state during initialization/repair. Prefer existing ignore rules; otherwise use repository-local Git exclude. Do not edit tracked `.gitignore` merely for setup.

A global `~/.qp` root is not supported.

## Resolve paths as the workspace owner

Akọsílẹ̀ receives the record/artifact kind and stable subject from the semantic owner, then resolves and allocates the canonical workspace path. Semantic owners do not construct `.qp` roots or choose collision suffixes themselves.

Record bundles use:

```text
.qp/records/<owner>/<YYYYMMDD-stable-slug>/
├── record.md
├── index.html       # optional human projection
├── receipts/        # optional
└── evidence/        # optional
```

Standalone artifacts use:

```text
.qp/artifacts/<YYYYMMDD-stable-slug>/index.html
```

Use the exact ASCII skill name as owner. Prefer an exact supplied record path/candidate identity before subject/title matching. Allocate directories with native atomic creation; on collision use `-2`, `-3`, and so on. Keep the allocated bundle stable across semantic changes. Reject unsafe identifiers, secrets, symlink traversal inside the canonical workspace, and destinations outside `.qp`.

## Replace exact files safely

The semantic owner supplies and validates the complete replacement, including native status, revision/timestamp, candidate identity, owner-specific fields, and body.

Invoke `safe-write.py` only with the resolved real canonical `.qp` root, never a linked-worktree symlink alias.

```bash
python3 <skill-root>/scripts/safe-write.py snapshot \
  --root <canonical-main-worktree>/.qp \
  --target <target> \
  --output <temporary-snapshot-outside-.qp>
```

Build an existing-file candidate only from that exact snapshot, then replace it through:

```bash
python3 <skill-root>/scripts/safe-write.py write \
  --root <canonical-main-worktree>/.qp \
  --target <target> \
  --candidate <complete-candidate-file> \
  --expected <snapshot-digest-or-absent>
```

The helper owns only containment, exact snapshotting, the per-target write lock, under-lock digest comparison, atomic replacement, and readback verification. It does not create paths, allocate IDs, parse semantic content, assign metadata, choose recovery, or retry. On `STALE_TARGET`, resnapshot and reconcile.

## Refresh generated navigation

Snapshot canonical `.qp/INDEX.md`, render a separate candidate, then publish it through the same safe-write seam:

```bash
python3 <skill-root>/scripts/render-index.py \
  --workspace <canonical-main-worktree>/.qp \
  --output <temporary-index-candidate-outside-.qp>
```

The renderer parses the common YAML envelope, sorts offset-aware timestamps by instant, links canonical `index.html` projections when present, and surfaces malformed records. It cannot write inside `.qp`; records remain authoritative.

## Report

Return canonical workspace identity, active worktree/alias state when relevant, affected resource, changed/migrated items, index and Git-hygiene state, conflicts or limits, and—when generated for direct use—both:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

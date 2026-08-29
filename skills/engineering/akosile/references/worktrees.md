# Worktrees

Use only when linked worktrees exist, `.qp` may already exist in more than one worktree, or an alias is wrong/broken.

## Invariant

```text
non-bare main worktree: .qp = real directory
linked worktree:        .qp = symlink → main .qp
```

Resolve the registered worktrees from Git's exact worktree metadata. If the main record is bare, return `BARE_REPOSITORY_UNSUPPORTED` without mutation; never infer a writable main `.qp` under a bare repository.

Before creating or repairing aliases, inspect `.qp` in every registered worktree and distinguish absent, canonical directory, canonical link, empty/populated physical directory, live noncanonical link, and broken link. A live noncanonical target is possible historical state and must be inventoried before replacement; record a broken link's former target before repair.

## Consolidate existing physical stores

Keep migration agent-owned; do not introduce a workspace migration runtime.

1. Preflight every physical/historical source before destructive mutation. Treat `record.md`, settings, owner evidence, and unknown non-derived files as retained unless their owner proves otherwise; indexes/projections/locks/temp files are derived or coordination state.
2. Same authoritative relative path + same bytes → deduplicate.
3. Unique authoritative/evidence path → preserve at the canonical relative path.
4. Same authoritative relative path + different bytes → stop for semantic reconciliation; never overwrite or invent a suffix.
5. Same semantic source + divergent derived projection → preserve the source and regenerate the projection.
6. Regenerate derived workspace navigation after consolidation rather than merging it.

### Freeze before cross-filesystem copy

Do not move a linked physical `.qp` directly to the main worktree: cross-filesystem rename semantics are not reliable enough for the migration contract.

For each linked physical store preserve this recovery ordering:

```text
preflight source
→ atomically freeze it as a sibling backup on its own filesystem, outside the worktree
→ create the linked-worktree alias to canonical main/.qp
→ re-inventory the frozen backup
→ copy retained files into canonical paths without overwriting conflicts
→ verify retained content identity/inventory
→ regenerate derived navigation/projections
→ remove backup only after all retained information is proved present
```

If verification fails, remove the new alias and restore the frozen source before continuing. Once the alias exists, ordinary QP writers use the canonical main `.qp`; use `safe-write.py` where exact concurrent publication requires CAS.

## Alias and ignore proof

Prefer a relative symlink when practical. Verify the root `.qp` entry is ignored after alias creation; use a repository-local untracked exclude rather than editing tracked `.gitignore` merely for QP setup. The rule must match the symlink itself, not only a directory path, so a trailing-slash directory-only pattern is insufficient.

If symlinks are unsupported, return a capability gap rather than creating a second live physical workspace.

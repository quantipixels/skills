# Worktrees

Use when multiple registered worktrees exist, a worktree `.qp` alias is absent/wrong/broken, legacy physical `.qp` stores exist, or the repository is a bare worktree hub.

## Invariant

```text
repository shared state: <git-common-dir>/qp = one real directory
registered worktree:     <worktree>/.qp     = symlink → canonical store
bare/no-worktree repo:   canonical store exists without a worktree alias
```

Resolve registered worktrees and the common directory from Git's exact metadata. Do not infer a special authoritative “main worktree.” Worktree paths may move; the alias is repairable derived state.

Before creating/repairing aliases, inspect the canonical store plus `.qp` in every registered worktree and distinguish absent, correct canonical link, live noncanonical link, broken link, empty/populated physical directory, and unresolved conflict. Record a broken/noncanonical link's target before replacement when it may identify historical state.

## Consolidate legacy physical stores

Keep migration agent-owned; do not introduce a workspace migration runtime.

1. Preflight every physical/historical source and the canonical destination before destructive mutation. Treat `record.md`, settings, owner evidence, and unknown non-derived files as retained unless their owner proves otherwise; indexes/projections/locks/temp files are derived or coordination state.
2. Same authoritative relative path + same bytes → deduplicate.
3. Unique authoritative/evidence path → preserve at the canonical relative path.
4. Same authoritative relative path + different bytes → stop for semantic reconciliation; never overwrite or invent a suffix.
5. Same semantic source + divergent derived projection → preserve source and regenerate projection.
6. Regenerate workspace navigation/projections after consolidation rather than merging derived output.

### Freeze before moving authoritative data

For each physical worktree `.qp` source that must be migrated, first establish a bounded quiescence window for readers/writers that may use that worktree-relative path. If quiescence cannot be established, block migration rather than expose an absent/partial workspace or allow another writer to recreate `.qp` during the move.

While consumers are quiesced:

```text
preflight source + canonical destination
→ freeze source through a reversible same-filesystem rename/backup
→ re-inventory frozen source
→ copy retained files into canonical paths without overwriting conflicts
→ verify retained content identity/inventory
→ create/repair worktree alias to canonical store
→ verify alias + retained content through the worktree path
→ regenerate derived navigation/projections
→ release quiescence
→ remove backup only after retained information is proved present
```

When several physical stores exist, preflight all of them before deleting any backup. If verification fails, preserve the frozen source, restore a safe readable path before releasing quiescence, and report the exact residual state; do not claim migration complete.

If an existing canonical `<git-common-dir>/qp` store already contains authoritative data, it participates in conflict comparison and is never silently replaced by a worktree source.

## Alias and ignore proof

Create/repair each worktree alias only after authoritative physical content at that path is preserved/reconciled. Prefer a relative symlink when practical and stable for the actual topology. Verify the alias resolves to the canonical Git-common store and the root `.qp` entry is ignored. Prefer shared repository-local exclude policy over tracked `.gitignore` merely for workspace setup; the pattern must match the symlink itself, not only a directory form.

If symlinks are unsupported, report `ALIAS_CAPABILITY_GAP` for worktree-relative access rather than creating another physical workspace. Canonical operations against `<git-common-dir>/qp` may continue when they do not require the alias.

## Bare worktree hubs

A bare repository is not a workspace failure. It can own `<git-common-dir>/qp` and linked worktrees can expose aliases to it. If no worktree exists, return canonical state without a worktree-relative `.qp` locator.

## Repair principle

On each operation that needs a worktree-visible path, derive the expected alias from current Git metadata. Repair safe absence/breakage instead of preserving stale alias topology as semantic state. Do not create a daemon, registry, or parallel worktree index merely to remember what Git already knows.
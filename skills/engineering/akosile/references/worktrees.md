# Worktrees

Use this reference only when linked worktrees exist, `.qp` may already exist in more than one worktree, or an alias is wrong/broken.

## Invariant

```text
non-bare main worktree: .qp = real directory
linked worktree:        .qp = symlink → main .qp
```

Resolve registered worktrees with `git worktree list --porcelain -z`. If its first record is `bare`, return `BARE_REPOSITORY_UNSUPPORTED` without mutation. Do not infer a main `.qp` under a bare repository.

Before creating or repairing aliases, inspect `.qp` in every registered worktree. Distinguish:

- absent;
- canonical real directory;
- link to canonical;
- empty physical directory;
- populated physical directory;
- link to another existing target; and
- broken link.

A live noncanonical symlink target is a possible historical workspace and must be inventoried before the link is replaced. A broken link may be replaced only after its former target is recorded in the migration report.

## Consolidate existing physical stores

Keep migration agent-owned and command-oriented; do not introduce a workspace migration runtime.

1. Preflight every physical/historical source before destructive mutation. Classify files by authority:
   - `record.md`, settings and owner evidence are semantic/authoritative;
   - `INDEX.md`, bundle `index.html`, locks and temporary files are derived/coordination state;
   - unknown non-derived files are preserved unless proved disposable.
2. Same authoritative relative path + same bytes → deduplicate.
3. Unique authoritative/evidence path → preserve at the canonical relative path.
4. Same authoritative relative path + different bytes → stop and return the conflict to the semantic owner/user. Never overwrite or create a semantic suffix.
5. Same `record.md` + different derived `index.html` → preserve the record and regenerate the projection; projection divergence does not block semantic migration.
6. Do not merge `INDEX.md`; regenerate it after consolidation.

### Freeze before cross-filesystem copy

Do not move a linked physical `.qp` to the main worktree. A rename across filesystems can fail with `EXDEV` or degrade to copy/delete semantics.

For each linked physical store:

```text
preflight source
→ atomically rename it on its own filesystem to a sibling backup outside the worktree
→ create linked/.qp symlink to canonical main/.qp
→ re-inventory the frozen backup
→ copy retained files into canonical paths without overwriting conflicts
→ verify digests/inventory
→ regenerate derived index/projections
→ remove backup only after all retained information is proved present
```

The backup belongs outside the linked worktree so it does not appear as untracked project content. If verification fails, remove the new alias and restore the frozen source directory before continuing.

Once the alias exists, ordinary QP writers resolve the canonical main `.qp`; they do not keep writing the historical frozen store. Use `safe-write.py` for exact canonical file publication where concurrent QP writers may race.

## Alias and ignore proof

Prefer a relative symlink when practical. After creating an alias:

```bash
git check-ignore -q -- .qp
```

If it is not ignored, add `/.qp` to `$(git rev-parse --git-path info/exclude)` and verify again. Do not add `/.qp/`, because the trailing slash does not match the symlink itself. Do not edit tracked `.gitignore` merely for QP setup.

If symlinks are unsupported, return a capability gap rather than creating a second live physical workspace.

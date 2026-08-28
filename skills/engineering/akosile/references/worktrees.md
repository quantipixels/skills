# Worktrees

Use this when the repository has Git linked worktrees or when existing `.qp` state may be split across worktrees.

`.qp` is repository-scoped state. The main worktree owns the one real `.qp` directory. Every linked worktree exposes only a symlink to that canonical directory so deleting a linked worktree cannot delete QP records or artifacts.

## Resolve the canonical home

From any worktree, use Git's machine-readable worktree inventory:

```bash
git worktree list --porcelain -z
```

Treat the first worktree entry as the main worktree and set:

```text
canonical workspace = <main-worktree>/.qp
```

Akọsílẹ̀ owns this resolution policy. Git supplies the repository/worktree facts.

The invariant is:

```text
main worktree:   .qp = real directory
linked worktree: .qp = symlink → main worktree .qp
```

The main `.qp` must never itself be a symlink. When invoking `safe-write.py` or `render-index.py`, pass the resolved real canonical `.qp` path, not a linked-worktree symlink alias. Internal symlink traversal remains rejected.

Prefer a relative symlink from the linked worktree when practical. If symlinks are unavailable on the host, return a capability gap rather than creating a second physical `.qp` store.

## Initialize without losing existing state

Before creating or repairing aliases, inventory `.qp` at **every registered worktree**, not only the active checkout. Classify each as:

```text
ABSENT
CANONICAL_REAL_DIRECTORY
LINK_TO_CANONICAL
EMPTY_REAL_DIRECTORY
POPULATED_REAL_DIRECTORY
WRONG_OR_BROKEN_LINK
```

Never replace a populated real directory with a symlink before migration.

When the main worktree has no `.qp` and exactly one existing populated `.qp` exists across all worktrees, that directory may become the canonical content after the full inventory proves no competing state exists. Move it to the main worktree, verify, then replace its former location with the alias.

When several physical `.qp` stores exist, consolidate into the main-worktree workspace first.

## Consolidate conservatively

Classify each resource before moving it:

- same relative path + same bytes/digest → deduplicate;
- relative path exists only in one workspace → preserve it at the same canonical relative path;
- same relative path + different bytes → stop and reconcile; never overwrite or auto-suffix a semantic resource;
- `INDEX.md` → never merge; regenerate from canonical records;
- lock/temp/coordination state → do not migrate as semantic state;
- unknown non-derived files → preserve; conflicting unknown files require explicit reconciliation.

A path collision between different record contents is an owner-level semantic conflict, not a filesystem allocation problem. Return it to the record owner rather than inventing a new record ID.

For `settings.json`:

- identical complete files may deduplicate;
- disjoint top-level consumer sections may be combined while preserving unknown sections;
- the same top-level section with different values must return to that consuming skill/user for reconciliation;
- malformed settings are preserved and reported, never overwritten as repair.

## Make the final swap recoverable

For each linked worktree with a real `.qp` after successful consolidation:

```text
linked/.qp
→ rename to linked/.qp.pre-migration
→ create linked/.qp symlink to canonical main/.qp
→ verify alias, expected resources, and canonical index regeneration
→ remove .qp.pre-migration only after proof succeeds
```

If any final verification fails, remove the new alias and restore the pre-migration directory.

After migration, repair should enforce only the invariant above. New records and artifacts are always allocated in the canonical main-worktree `.qp`; linked worktrees merely provide access aliases.

## Git hygiene

`.qp` is generated local repository state. Prefer an existing ignore rule; otherwise add a repository-local exclude matching the root entry (for example `/.qp`) so both the real directory and linked-worktree symlink remain untracked. Do not edit tracked `.gitignore` merely to initialize QP.
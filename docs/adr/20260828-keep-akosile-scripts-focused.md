# Keep Akọsílẹ̀ repository-scoped with focused deterministic seams

Status: Accepted

Refines the workspace and safe-write parts of [Use owner records as semantic sources for HTML projections](20260824-use-owner-records-for-html-projections.md).

## Context

QP records and artifacts must survive linked-worktree deletion. A physical `.qp` per worktree loses repository knowledge when a temporary worktree is removed and allows concurrent worktrees to diverge silently.

Akọsílẹ̀ also needs two mechanical guarantees ordinary agent command sequences do not provide reliably:

- a file's working bytes and expected digest must come from the same read, with cooperating writers unable to accept the same stale prior state; and
- generated navigation must parse record YAML and order timestamps consistently.

A broader workspace runtime would duplicate Git/filesystem discovery, allocation, repair, and semantic-owner capabilities.

## Decision

1. `.qp` is repository-scoped state.
2. In repositories with linked worktrees, the main worktree owns the one real `.qp` directory. Every linked worktree exposes a symlink to that canonical directory.
3. Resolve the main worktree from Git's worktree inventory. Akọsílẹ̀ owns the canonical-home and alias policy; native Git/filesystem operations execute it.
4. Before establishing aliases, inventory `.qp` across every registered worktree. Never replace a populated real `.qp` with a symlink before migration.
5. Consolidate identical or non-colliding resources mechanically; regenerate `INDEX.md`; stop on same-identity/different-content semantic conflicts and return them to the owning skill. Make the final linked-directory-to-symlink swap recoverable.
6. Semantic owners supply record/artifact kind, stable subject, and semantic content. Akọsílẹ̀ owns canonical paths, collision allocation, safe-write protocol, and indexing.
7. Retain the current justified deterministic helpers:
   - `safe-write.py` returns one exact snapshot with its matching digest, or performs locked compare-and-swap replacement;
   - `render-index.py` parses record YAML and renders an external `INDEX.md` candidate.
8. `safe-write.py` owns only containment beneath the resolved real canonical root, exact snapshotting, the per-target lock, under-lock comparison, atomic replacement, and readback.
9. `render-index.py` validates only the common record envelope and owner/path agreement, orders timestamps, links canonical `index.html` projections, and reports malformed records. It cannot write inside `.qp`.
10. Publish `INDEX.md` through the same safe-write primitive; do not add a second mutation implementation.
11. Keep canonical bundle entrypoints as `index.html` for owner projections and standalone artifacts.
12. Do not add a general workspace CLI, subject registry, doctor/repair runtime, automatic semantic migration engine, or semantic record model. Future scripts are allowed only when they independently pass Kọ Skill's capability/script boundary.

## Consequences

Deleting a linked worktree removes only its `.qp` alias; repository records remain under the main worktree. Concurrent worktrees operate on the same physical targets and the same per-target locks.

Existing worktrees with physical `.qp` directories require bounded migration before aliasing. Migration preserves unknown/user state, does not auto-rename conflicting semantic records, and remains recoverable until final verification succeeds.

The helpers require Python, PyYAML, and filelock. Filesystem symlink support is required for linked-worktree aliases; unsupported hosts return a capability gap rather than creating duplicate physical stores.

## Rejected alternatives

- Physical `.qp` per linked worktree: loses or forks repository state when worktrees are deleted.
- Store `.qp` inside Git's internal common directory: hides a human/agent workspace inside Git implementation state.
- Prose-only stale checks: cannot make cooperating compare-and-swap writers atomic.
- Separate content read and digest calculation: can describe different target states.
- Complete workspace engine: duplicates agent and native Git/filesystem capabilities.
- Semantic owners constructing `.qp` paths: leaks Akọsílẹ̀'s persistence boundary into callers.
- Slug-named HTML entry files: duplicates bundle identity without a demonstrated benefit; canonical `index.html` remains simpler and portable.

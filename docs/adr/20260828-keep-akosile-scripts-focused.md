# Keep Akọsílẹ̀ repository-scoped with minimal deterministic kernels

Status: Accepted

## Decision

QP `.qp` state is repository-scoped. In a non-bare repository, the main worktree owns the one real `.qp` directory and linked worktrees expose symlinks to it. Bare repositories have no supported canonical `.qp` home.

New owner records and standalone artifacts use the semantic owner's stable subject as path identity. Do not add date prefixes or automatic collision suffixes. Existing dated bundles remain valid legacy identities and are not renamed merely for consistency.

Akọsílẹ̀ initializes lazily: create the canonical `.qp` directory when QP state is first needed, then create settings, index, records, artifacts, receipts or evidence only when an owning operation requires them.

Worktree discovery, symlink creation, source freezing, copy/compare migration, ignore configuration and repair use native Git/filesystem operations guided by Akọsílẹ̀ invariants. Existing physical stores are preflighted conservatively. Migration freezes a linked source by local rename before any cross-filesystem copy; conflicting authoritative bytes stop for owner reconciliation. Derived `INDEX.md` and `index.html` are regenerated rather than treated as semantic conflicts.

The agent harness retains worktree and branch creation, session isolation, shell execution, and ordinary file editing. Akọsílẹ̀ neither wraps nor replaces those capabilities; it starts from existing worktrees and governs only shared repository-local QP state.

Akọsílẹ̀ retains two deterministic kernels:

1. `safe-write.py` — lock-held compare-and-swap publication from native target and candidate digests. Candidates must remain outside `.qp`.
2. `render-index.py` — canonical owner records to Markdown on stdout. It validates only the common envelope/path identity, orders offset-aware timestamps, treats metadata as literal text, links canonical `index.html` projections, and reports malformed records.

`safe-write.py` does not snapshot targets or replace ordinary writes. The agent uses native hashing and invokes it only when shared writers or an exact publication claim require CAS. `render-index.py` does not choose an output path or mutate `.qp`; the caller captures stdout and publishes through `safe-write.py` when an index is needed.

Akọsílẹ̀ does not grow a general workspace CLI, migration engine, subject registry, settings semantic model, provider abstraction, or repair runtime without new demonstrated deterministic need and Kọ Skill capability-placement proof.

## Consequences

- deleting a linked worktree cannot delete canonical QP records;
- one stable subject cannot silently become two semantic identities through `-2/-3` allocation;
- cross-filesystem migration does not rely on rename-to-main semantics;
- validated candidate bytes cannot change between validation and publication unnoticed;
- empty repositories carry no unnecessary QP files beyond the canonical workspace/alias when QP state is actually needed;
- target hashing and ordinary worktree mechanics remain inspectable native commands rather than a QP-owned orchestration engine.

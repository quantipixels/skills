# Keep Akọsílẹ̀ repository-scoped with minimal deterministic kernels

Status: Partially superseded by `20260903-worktree-independent-qp-workspace.md`

The canonical-storage topology and bare-repository limitation in this ADR are superseded. Current repository state lives under `<git-common-dir>/qp`, with worktree `.qp` entries as reconstructible aliases when useful and bare repositories supported. The stable-subject, lazy-materialization, migration-safety, and deterministic-kernel decisions below remain active.

## Decision

New owner records and standalone artifacts use the semantic owner's stable subject as path identity. Do not add date prefixes or automatic collision suffixes. Existing dated bundles remain valid legacy identities and are not renamed merely for consistency.

Akọsílẹ̀ initializes lazily: create the canonical workspace when state is first needed, then create settings, index, records, artifacts, receipts or evidence only when an owning operation requires them.

Worktree discovery, symlink creation, source freezing, copy/compare migration, ignore configuration and repair use native Git/filesystem operations guided by Akọsílẹ̀ invariants. Existing physical stores are preflighted conservatively. Migration freezes a physical source by local rename before any cross-filesystem copy; conflicting authoritative bytes stop for owner reconciliation. Derived `INDEX.md` and `index.html` are regenerated rather than treated as semantic conflicts.

The agent harness retains worktree and branch creation, session isolation, shell execution, and ordinary file editing. Akọsílẹ̀ neither wraps nor replaces those capabilities; it governs only shared repository-local workspace state.

Akọsílẹ̀ retains two deterministic kernels:

1. `safe-write.py` — lock-held compare-and-swap publication from native target and candidate digests. Candidates must remain outside the canonical workspace.
2. `render-index.py` — canonical owner records to Markdown on stdout. It validates only the common envelope/path identity, orders offset-aware timestamps, treats metadata as literal text, links canonical `index.html` projections, and reports malformed records.

`safe-write.py` does not snapshot targets or replace ordinary writes. The agent uses native hashing and invokes it only when shared writers or an exact publication claim require CAS. `render-index.py` does not choose an output path or mutate the workspace; the caller captures stdout and publishes through `safe-write.py` when an index is needed.

Akọsílẹ̀ does not grow a general workspace CLI, migration engine, subject registry, settings semantic model, provider abstraction, or repair runtime without new demonstrated deterministic need and Kọ Skill capability-placement proof.

## Consequences

- deleting any worktree cannot delete canonical records;
- one stable subject cannot silently become two semantic identities through `-2/-3` allocation;
- cross-filesystem migration does not rely on rename-to-main semantics;
- validated candidate bytes cannot change between validation and publication unnoticed;
- empty repositories carry no unnecessary workspace files before state is actually needed; and
- target hashing and ordinary worktree mechanics remain inspectable native commands rather than an owned orchestration engine.
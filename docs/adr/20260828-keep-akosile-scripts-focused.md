# Keep Akọsílẹ̀ repository-scoped with one deterministic publication kernel

Status: Accepted

## Decision

QP `.qp` state is repository-scoped. In a non-bare repository, the main worktree owns the one real `.qp` directory and linked worktrees expose symlinks to it. Bare repositories have no supported canonical `.qp` home.

New owner records and standalone artifacts use the semantic owner's stable subject as path identity. Do not add date prefixes or automatic collision suffixes. Existing dated bundles remain valid legacy identities and are not renamed merely for consistency.

Akọsílẹ̀ initializes lazily: create the canonical `.qp` directory when QP state is first needed, then create settings, index, records, artifacts, receipts or evidence only when an owning operation requires them.

Worktree discovery, symlink creation, source freezing, copy/compare migration, ignore configuration and repair use native Git/filesystem operations guided by Akọsílẹ̀ invariants. Existing physical stores are preflighted conservatively. Migration freezes a linked source by local rename before any cross-filesystem copy; conflicting authoritative bytes stop for owner reconciliation. Derived `INDEX.md` and `index.html` are regenerated rather than treated as semantic conflicts.

Akọsílẹ̀ retains one deterministic kernel:

- `safe-write.py` — exact compare-and-swap publication. The caller uses native host SHA-256 tooling to pin current target identity and validated candidate-byte identity. The helper verifies the candidate, excludes concurrent target writers, rechecks target identity, atomically installs the already-verified bytes, and verifies exact readback. Candidates remain outside `.qp`.

Akọsílẹ̀ does **not** retain a target snapshot runtime or an index renderer. Target/candidate hashing is ordinary agent/native-tool work. `INDEX.md` is derived navigation: the agent reads canonical records, composes the current view from the common storage envelope, and regenerates it whenever stale or malformed. Derived navigation does not justify a private parser/runtime because an incorrect or stale index cannot overwrite semantic truth.

Akọsílẹ̀ does not grow a general workspace CLI, migration engine, subject registry, settings semantic model, provider abstraction, snapshot runtime, index compiler, or repair runtime without new demonstrated deterministic need and Kọ Skill capability-placement proof.

## Consequences

- deleting a linked worktree cannot delete canonical QP records;
- one stable subject cannot silently become two semantic identities through `-2/-3` allocation;
- cross-filesystem migration does not rely on rename-to-main semantics;
- concurrent writers cannot both accept the same expected target identity;
- validated candidate bytes cannot change between validation and publication unnoticed;
- target/candidate snapshotting, index composition, and ordinary filesystem orchestration stay visible agent/native operations;
- PyYAML is no longer an Akọsílẹ̀ runtime dependency;
- stale or malformed `INDEX.md` is regenerated from canonical `record.md` files rather than repaired as authoritative state;
- empty repositories carry no unnecessary QP files beyond the canonical workspace/alias when QP state is actually needed.

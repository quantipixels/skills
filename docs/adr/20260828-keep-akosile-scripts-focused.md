# Keep Akọsílẹ̀ scripts focused on irreducible mechanics

Status: Accepted

Refines the safe-write and HTML-entry naming parts of [Use owner records as semantic sources for HTML projections](20260824-use-owner-records-for-html-projections.md).

## Context

Akọsílẹ̀ needs two guarantees that ordinary agent command sequences do not provide reliably:

- a file's working bytes and expected digest must come from the same read; and
- two cooperating writers must not both accept the same prior target state.

Generated navigation also needs consistent YAML parsing and timestamp ordering.

A proposed workspace engine went much further by implementing repository discovery, lookup, allocation, identity registries, settings operations, metadata assignment, diagnosis, repair, and a general command model. Those duplicate agent, Git, filesystem, and semantic-owner capabilities.

## Decision

1. Agents and native Git/filesystem tools own root discovery, initialization, lookup, path/slug selection, atomic directory allocation, Git exclude, diagnosis, and repair.
2. Keep exactly two deterministic helpers:
   - `safe-write.py` returns one exact snapshot with its matching digest, or performs locked compare-and-swap replacement.
   - `render-index.py` parses record YAML and renders an external `INDEX.md` candidate.
3. `safe-write.py` owns only containment, exact snapshotting, the per-target write lock, under-lock comparison, atomic replacement, and readback.
4. Semantic owners select paths; supply complete content; assign revision/timestamp; validate native state; and reconcile stale writes.
5. `render-index.py` validates only the common envelope and owner/path agreement, orders timestamps, and reports malformed records. It cannot write inside `.qp`.
6. Publish `INDEX.md` through the same safe-write primitive; do not add a second mutation implementation.
7. New projections and standalone artifacts use real slug filenames:

   ```text
   .qp/records/<owner>/<record-id>/<record-slug>.html
   .qp/artifacts/<artifact-id>/<artifact-slug>.html
   ```

8. Do not add a workspace CLI, subject registry, doctor/repair runtime, automatic migration, global lock registry, or semantic record model.

## Consequences

Akọsílẹ̀ retains the exact-snapshot, concurrency, and deterministic-index guarantees that require code while remaining a lightweight convention driven by natural agent capabilities.

The helpers require Python, PyYAML, and filelock. Per-target lock files are mechanical coordination state. Existing `index.html` files remain historical inputs and are reported, not migrated automatically.

## Rejected alternatives

- Prose-only stale checks: not atomic across processes.
- Separate content read and digest calculation: can describe different target states.
- Complete workspace engine: duplicates existing agent and native-tool capabilities.
- Engine-assigned identity or metadata: belongs to semantic owners.
- Direct index mutation by the renderer: duplicates the safe-write seam.
- `index.html` for every artifact: hides semantic identity.

# Keep Akọsílẹ̀ scripts focused on irreducible mechanics

Status: Accepted

Refines the safe-write and HTML-entry naming parts of [Use owner records as semantic sources for HTML projections](20260824-use-owner-records-for-html-projections.md).

## Context

Akọsílẹ̀ needs one guarantee that ordinary sequential agent commands cannot provide: two cooperating writers must not both accept the same previously read file state. The owner must also receive the file bytes and digest from one exact snapshot; reading content and hashing the target separately can pair stale content with a newer digest. Generated navigation needs deterministic YAML parsing and chronological timestamp ordering.

A proposed workspace engine went much further. It added Git-root discovery, path and identity resolution, record/artifact allocation, subject registries, revision/timestamp assignment, settings operations, diagnostics, repair, and a general command model. Those duplicate capabilities agents, Git, and normal filesystems already provide and make Akọsílẹ̀ a second workspace product rather than a small shared convention.

## Decision

1. Agents and host-native Git/filesystem tools own repository-root discovery, workspace initialization, lookup, ID/slug selection, atomic directory allocation, Git exclude, diagnosis, and repair.
2. Keep exactly two bundled deterministic helpers:
   - `safe-write.py` takes one locked target snapshot with its matching digest or atomically compare-and-swap replaces that target.
   - `render-index.py` parses record YAML and renders one `INDEX.md` candidate outside `.qp`.
3. `safe-write.py` receives the `.qp` root, exact target, an external snapshot or complete candidate path, and the expected snapshot digest. It owns path containment, locking, same-read snapshot/digest, under-lock comparison, atomic replacement, and readback only.
4. Semantic owners continue to choose paths, supply complete frontmatter/body, assign revision and timestamp, validate native state, and reconcile stale writes.
5. `render-index.py` validates only the common record envelope and owner/path agreement, sorts offset-aware timestamps by instant, and surfaces invalid records. It cannot write inside the authoritative workspace.
6. `.qp/INDEX.md` is replaced through the same safe-write primitive; the index renderer does not duplicate locking or atomic-write mechanics.
7. Owner projections and standalone artifacts use a real descriptive slug filename:

   ```text
   .qp/records/<owner>/<record-id>/<record-slug>.html
   .qp/artifacts/<artifact-id>/<artifact-slug>.html
   ```

   New QP artifacts and projections do not use `index.html`.
8. Do not add an Akọsílẹ̀ workspace CLI, subject registry, doctor/repair runtime, global lock registry, automatic migration, or semantic record model.

## Consequences

Akọsílẹ̀ retains the concurrency, exact-snapshot, and deterministic-index guarantees that need code while remaining usable through normal agent capabilities. The scripts have one-sentence contracts, safe-write is the only authoritative mutation primitive, and semantic owners remain responsible for their own data.

The focused helpers require Python, PyYAML, and filelock. Hidden per-target lock files may remain beside protected files; they are mechanical coordination state, not records.

Existing `index.html` projections remain readable historical files. The renderer reports them diagnostically, but migration or renaming requires the owning workflow's authority.

## Rejected alternatives

- Prose-only stale checks: rejected because the check and replacement are not atomic across processes.
- Separate content read and digest calculation: rejected because they can describe different file snapshots.
- A complete workspace engine: rejected because it duplicates agent, Git, and filesystem capabilities.
- Engine-assigned identity, revision, or timestamp: rejected because those belong to semantic owners and their records.
- Let the index renderer write `.qp/INDEX.md` directly: rejected because it duplicates the safe-write seam and broadens its mutation authority.
- One generic command surface for initialization, lookup, write, diagnosis, and repair: rejected because only exact snapshot/CAS and index rendering require bundled code.
- Keep `index.html`: rejected because it hides the artifact's semantic identity and gives every generated resource the same opaque filename.

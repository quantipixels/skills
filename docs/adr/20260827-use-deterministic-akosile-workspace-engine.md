# Use a deterministic Akọsílẹ̀ workspace engine

Status: Accepted

Supersedes the workspace-write and HTML-entry naming parts of [Use owner records as semantic sources for HTML projections](20260824-use-owner-records-for-html-projections.md). That decision remains authoritative for semantic-owner records, linked evidence, and HTML projection ownership.

## Context

Akọsílẹ̀ owns repository-local `.qp` placement, safe record/settings replacement, identity resolution, and derived indexing. The prose-only implementation asked each calling agent to recreate these mechanics through general filesystem and shell capabilities.

Earlier runtime experiments exposed concrete mechanical failures: execution below the Git root could create a second workspace; digest checks without a lock allowed two accepted writers to overwrite one another; settings had the same race; an ad hoc frontmatter parser did not implement YAML; and raw timestamp strings produced incorrect index order across offsets. Removing the runtime removed the implementation but not the underlying concurrency, parsing, and identity obligations.

The repository's script policy permits a bundled script when one owner needs a narrow deterministic transformation or validation that native tools do not express adequately. Here the observed cross-process write race justifies resource locking, and focused PyYAML/filelock dependencies avoid custom parsers and platform-specific lock machinery.

## Decision

1. Keep `akosile` as the semantic boundary for `.qp` mechanics and add one deterministic Python engine with a JSON CLI.
2. The engine owns Git worktree-root resolution, path/symlink containment, owner-first allocation, generic YAML parsing, resource locking, digest compare-and-swap, revision/timestamp assignment, atomic replacement, settings persistence, index rebuilding, diagnostics, and derived repair.
3. Semantic owners retain record type/status/transition validity, subject meaning, candidate meaning, evidence, body structure, completion, and provider authority.
4. New record identity is `owner + subject`. The allocated dated slug is a stable physical location; exact `record_ref` is the operational identity after allocation. Legacy records without `subject` remain readable and may be upgraded only through an exact record reference.
5. New record projections and standalone HTML artifacts use a real slug filename, not `index.html`:

   ```text
   .qp/records/<owner>/<record-id>/<record-slug>.html
   .qp/artifacts/<artifact-id>/<artifact-slug>.html
   ```

6. The engine assigns `updated_at` and `revision`. Callers supply the complete semantic candidate without those reserved fields and the exact digest returned by the corresponding read, or `absent` for a new target.
7. Record and settings writes hold a per-resource file lock across the current-state check and atomic replacement. Participating writes that are stale, ambiguous, malformed, path-escaping, or lock-blocked return typed conflicts instead of overwriting or retrying blindly.
8. `INDEX.md` remains derived navigation. A verified record write remains authoritative when a later index rebuild fails; the failure is reported separately.
9. `doctor` is read-only. `repair` may recreate missing infrastructure, initialize missing `{}`, regenerate the index, and establish repository-local Git exclude. It does not rewrite semantic records, infer subjects, delete legacy roots, or migrate legacy `index.html` files.
10. The repository validates the engine with focused tests for worktree resolution, YAML, identity, slug filenames, compare-and-swap concurrency, malformed settings, timestamp ordering, symlink containment, legacy diagnostics, and index failure after a verified write.

## Consequences

Akọsílẹ̀ becomes deep in reliability while remaining narrow in domain. Callers no longer duplicate path or stale-write mechanics, and the same operation produces the same typed result across supported hosts.

The engine introduces two small runtime dependencies and one private `.qp/.locks` directory. They carry no semantic state and remain outside Git. Hosts must make the declared requirements available before invoking the engine.

Existing `index.html` projections and records without `subject` are not silently migrated. They remain explicit diagnostics until an owning workflow performs an exact, authorized update.

## Rejected alternatives

- Keep prose-only writes: rejected because the advertised concurrency and parsing guarantees cannot be obtained reliably from independent ad hoc command sequences.
- Restore the previous broad workspace runtime unchanged: rejected because the new engine is limited to deterministic Akọsílẹ̀ mechanics and uses focused libraries for YAML and locking.
- Use candidate or title as record identity: rejected because both change during a record's lifecycle.
- Keep `index.html`: rejected because the entrypoint hides the artifact's semantic identity and causes every generated bundle to present the same opaque filename.
- Automatically migrate legacy records/artifacts: rejected because identity and semantic ownership cannot be inferred safely.
- Add a global registry or daemon: rejected because repository-local operations do not justify cross-project identity, synchronization, privacy, and lifecycle machinery.

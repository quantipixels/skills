# Workspace contract

Use this reference for the repository-local `.qp` v0 layout, common record envelope, identity, deterministic writes, generated index, and direct-access receipts.

## Root and layout

Resolve the Git worktree root; the canonical workspace is exactly `<repository>/.qp`.

```text
.qp/
├── settings.json
├── INDEX.md
├── .locks/
├── records/<owner>/<record-id>/
│   ├── record.md
│   ├── <record-slug>.html       # optional owner projection
│   ├── receipts/                # optional
│   └── evidence/                # optional
└── artifacts/<artifact-id>/
    └── <artifact-slug>.html     # owner-selected entry artifact
```

`.locks/` is private mechanical state and never a semantic registry. New records use owner-first paths. Do not introduce open-ended roots such as `.qp/plans`, `.qp/architecture`, `.qp/reports`, `.qp/research`, `.qp/triage`, `.qp/findings`, or `.qp/state`.

This version supports repository-local `.qp` only. Do not add a global registry, background synchronizer, daemon, global/project precedence, or automatic local-to-global migration.

## Identity and naming

- `owner` is the canonical ASCII skill `name`.
- `subject` is the stable semantic identity within that owner.
- `record_ref` is `<owner>/<record-id>` and is the exact operational identity after allocation.
- Record and artifact IDs use `<YYYYMMDD>-<stable-slug>` with a numeric suffix on collision.
- The physical directory remains stable across title, status, candidate, and projection changes.
- The HTML entry filename is the actual resource slug, including any collision suffix: `<stable-slug>.html`. New writes never use `index.html`.
- Reject absolute identifiers, separators inside owner/slug, `.`/`..`, control characters, secret-bearing identifiers, symlink traversal, and targets outside `.qp`.

Resolve by exact `record_ref` when known. Otherwise resolve a current record by `owner + subject`. Similar titles and candidates are not identity. Legacy records without `subject` remain readable but require an exact-ref update before subject-based allocation can proceed safely.

## Common record envelope

New records contain:

```yaml
owner: <canonical-skill-name>
record_type: <owner-native type>
subject: <stable owner-scoped identity>
title: <human title>
updated_at: <Akọsílẹ̀-assigned offset-aware timestamp>
revision: <Akọsílẹ̀-assigned positive integer>
candidate: <exact current candidate, optional>
status: <owner-native state>
```

The semantic owner supplies and validates `owner`, `record_type`, `subject`, `title`, optional `candidate`, `status`, owner-specific fields, and the complete Markdown body. Akọsílẹ̀ owns `updated_at`, `revision`, the physical ID/path, generic YAML parsing, and the common-envelope/path checks.

After creation, `owner` and `record_type` do not change. `subject` is assigned once and then does not change. The semantic owner defines record types, statuses, transitions, evidence, and body structure.

## Compare-and-swap writes

Every record or settings replacement uses the bundled engine and one expected current digest:

1. Read the exact target and retain the returned SHA-256 digest; use `absent` only for a new target.
2. Build and semantically validate the complete candidate outside the engine.
3. Acquire the per-resource file lock.
4. Reread under the lock and compare the exact digest/absence.
5. Validate the generic candidate and immutable identity.
6. Assign record revision and `updated_at` where applicable.
7. Write a temporary file, flush it, and atomically replace the target.
8. Reread and validate the written result.
9. Rebuild `INDEX.md` after a record write.

A stale digest, lock timeout, concurrent participating write, malformed current file, identity conflict, path escape, or ambiguous subject returns a typed conflict. Do not overwrite or silently retry it. Writes that bypass the engine are outside this guarantee.

Record revision starts at `1` and increments by exactly one. A failed index rebuild does not invalidate a successfully verified record; the operation reports the derived index failure separately.

## Index

`.qp/INDEX.md` is generated from mechanically valid `record.md` frontmatter and sorted by the UTC instant represented by `updated_at`, newest first. It displays owner, record type, title, native status, record link, and optional expected slug-named HTML view.

Malformed records, path mismatches, and duplicate `owner + subject` identities appear in diagnostic sections rather than disappearing. Records remain authoritative; users and semantic owners do not edit the generated index.

## Doctor and repair

`doctor` is read-only. It may report:

- missing workspace infrastructure;
- malformed settings or records;
- missing or duplicate subjects;
- path, owner, ID, or symlink violations;
- stale/missing index state;
- legacy roots or `index.html`; and
- missing repository-local Git hygiene.

`repair` may create missing directories, initialize a missing settings file as `{}`, regenerate `INDEX.md`, and add `.qp/` to repository-local Git exclude. It never rewrites semantic records, deletes legacy material, migrates identities, or renames artifact entry files.

## Direct user access

For a resource intended for direct user use, return:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative path beginning .qp/...>
```

The workspace path is the stable project-local reference. Do not embed machine-specific absolute paths as portable source identity.

## Git hygiene

`.qp` is generated local state. Prefer existing ignore rules; otherwise use repository-local Git exclude. Never stage or publish `.qp` through QP workflows.

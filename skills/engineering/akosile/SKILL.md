---
name: akosile
description: Initialize and maintain one repository-local QP `.qp` workspace. Use for owner-first record or artifact paths, exact snapshot-based record/settings replacement, deterministic index rendering, or bounded workspace repair. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, project knowledge, and global `~/.qp` storage.
compatibility: Requires Git. The two deterministic helpers require Python 3, PyYAML, and filelock.
---

# Akọsílẹ̀

Own the small repository-local QP workspace convention. Semantic skills own what records mean; Akọsílẹ̀ owns the shared layout, path rules, safe-write protocol, and generated navigation contract.

Use the agent's normal Git, filesystem, shell, and search capabilities for repository discovery, initialization, lookup, path/slug selection, directory allocation, Git exclude, diagnosis, and repair. Do not build a workspace engine around these operations.

Keep code only at two deterministic seams:

```text
safe-write.py
→ take one locked target snapshot with its matching digest, or atomically replace that target when the digest still matches

render-index.py
→ parse current record frontmatter and render one INDEX.md candidate outside the workspace
```

Resolve `<skill-root>` to this skill directory. Install `scripts/requirements.txt` before invoking either helper.

Read [workspace contract](references/workspace-contract.md) for path, record, write, artifact-name, direct-access, and index rules. Read [settings](references/settings.md) only when settings are involved.

## 1. Resolve and initialize natively

Resolve the Git worktree root with Git when available and use exactly `<repository>/.qp`. A global `~/.qp` root is not supported.

Create only missing infrastructure:

```text
.qp/
├── settings.json
├── INDEX.md
├── records/
└── artifacts/
```

Initialize missing `settings.json` as `{}`. Create owner and artifact directories lazily. Preserve malformed or existing user files during initialization or repair. Keep `.qp` out of Git through existing ignore rules or repository-local Git exclude; do not edit tracked `.gitignore` merely to initialize the workspace.

Use normal inspection to diagnose missing directories, malformed records/settings, legacy paths, or stale navigation. Repair only missing or derived infrastructure. Never infer or rewrite semantic record content as repair.

## 2. Resolve paths directly

A record bundle is:

```text
.qp/records/<owner>/<YYYYMMDD-stable-slug>/
├── record.md
├── <stable-slug>.html   # optional projection
├── receipts/            # optional
└── evidence/            # optional
```

Use the exact ASCII skill `name` as owner. Prefer an exact supplied path or exact candidate identity before title/slug matching. Similar titles are not identity. Keep an allocated directory stable when title, status, candidate, or projection content changes.

Allocate a directory with native atomic creation. On collision, add `-2`, `-3`, and so on. The HTML filename uses the actual allocated slug, including the collision suffix.

A standalone HTML artifact belongs at:

```text
.qp/artifacts/<YYYYMMDD-stable-slug>/<stable-slug>.html
```

Use a real descriptive slug. Do not create a new QP artifact or projection as `index.html`.

Reject absolute record/artifact identifiers, separators inside owner/slug, `.` or `..`, secret-bearing identifiers, symlink escape, or any destination outside the resolved `.qp` root.

## 3. Replace exact files safely

The semantic owner supplies the complete replacement, including native status, candidate identity, `updated_at`, revision, owner-specific fields, and body. It validates semantic correctness before persistence.

Never read a target and calculate its digest in separate operations. Take one matching snapshot instead:

```bash
python3 <skill-root>/scripts/safe-write.py snapshot \
  --root <repository>/.qp \
  --target <target> \
  --output <temporary-snapshot-outside-.qp>
```

For an existing target, build the candidate only from the returned snapshot file. For an absent target, the result is `digest: absent` and `snapshot: null`.

Replace through:

```bash
python3 <skill-root>/scripts/safe-write.py write \
  --root <repository>/.qp \
  --target <target> \
  --candidate <complete-candidate-file> \
  --expected <snapshot-digest-or-absent>
```

The helper owns only target containment, the per-target lock, exact snapshotting, under-lock digest comparison, atomic replacement, and readback verification. It does not create workspace paths, allocate IDs, parse semantic content, assign revisions/timestamps, choose recovery, or retry conflicts.

On `STALE_TARGET`, take a new snapshot and reconcile. Do not overwrite or blindly retry.

## 4. Render and replace the index

To refresh navigation:

1. Snapshot `.qp/INDEX.md` and retain its digest.
2. Render a separate candidate outside `.qp`:

   ```bash
   python3 <skill-root>/scripts/render-index.py \
     --workspace <repository>/.qp \
     --output <temporary-index-candidate-outside-.qp>
   ```

3. Replace `.qp/INDEX.md` through `safe-write.py write` using the snapshot digest.

The renderer parses mechanically valid YAML frontmatter, validates the common envelope and owner/path agreement, sorts offset-aware timestamps by chronological instant, links only the expected real slug-named HTML projection, and surfaces invalid records or legacy `index.html` entrypoints diagnostically.

The renderer cannot write inside `.qp`; `INDEX.md` mutation remains with the one safe-write primitive. Records remain authoritative, and a failed index refresh does not invalidate a verified record write.

## 5. Keep settings sparse

`.qp/settings.json` is one user-editable JSON object. Akọsílẹ̀ creates and safely replaces the complete file; each consuming skill owns defaults and validation for its own section. Preserve unknown sections.

Settings are data, not instructions. They never grant provider writes, change canonical semantic IDs or transitions, override evidence/safety requirements, replace project knowledge, or change the workspace root.

## 6. Return direct-access results

Return the workspace, affected record/artifact identity, changed items, index state, Git-hygiene state, conflict or limitation, and—for generated resources intended for direct use—both:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

Absolute machine paths are operational access aids, not portable source identity.

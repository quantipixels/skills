---
name: akosile
description: Initialize, diagnose, repair, and safely mutate one repository-local QP `.qp` workspace. Use for owner-first record or artifact allocation, compare-and-swap record/settings writes, subject identity, slug-named HTML paths, or index rebuilding. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, project knowledge, and global `~/.qp` storage.
compatibility: Requires Python 3, Git, PyYAML, and filelock.
---

# Akọsílẹ̀

Own the deterministic mechanics of one repository-local QP workspace. Semantic skills own record meaning and validity; Akọsílẹ̀ owns the canonical root, identity-safe placement, locked compare-and-swap writes, generated navigation, and exact path receipts.

Use the bundled engine rather than rebuilding these mechanics with ad hoc shell commands. Resolve `<skill-root>` to this skill directory and use:

```bash
python3 <skill-root>/scripts/workspace.py <operation> --repo <repository-or-path-inside-it>
```

The runtime dependencies are declared in `scripts/requirements.txt`. Keep semantic judgment outside the engine.

Read [workspace contract](references/workspace-contract.md) before record, artifact, index, doctor, or repair operations. Read [settings](references/settings.md) only when settings are involved.

## 1. Pin authority and the operation

Resolve the Git worktree root and use exactly `<repository>/.qp`. Global `~/.qp` storage is not supported.

Select one operation:

- `init` — create only missing workspace infrastructure, preserve malformed user files, rebuild the derived index, and establish repository-local Git hygiene;
- `resolve-record` — resolve an exact record reference or atomically allocate one owner-first bundle from owner, stable subject, and slug;
- `read-record` — return generic metadata and the exact SHA-256 digest required for a later write;
- `write-record` — write one owner-supplied semantic body through a locked compare-and-swap operation;
- `resolve-artifact` — resolve or atomically allocate one standalone artifact bundle and return its real slug-named HTML path;
- `read-settings` / `write-settings` — read or compare-and-swap the sparse JSON object;
- `index` — rebuild `.qp/INDEX.md` from current records;
- `doctor` — diagnose mechanical workspace defects without mutation; or
- `repair` — repair only missing or derived infrastructure. Never rewrite semantic records, migrate legacy content, or infer identity corrections.

Initialization, record/settings writes, Git exclude changes, and repair are mutations. Use them only with the caller's applicable repository/workspace authority. Reads, resolution without `--create`, indexing diagnosis, and `doctor` do not grant later mutation authority.

## 2. Keep identity separate from location

A new record is identified semantically by:

```text
owner + subject
```

`owner` is the exact ASCII skill name. `subject` is a stable owner-supplied identity that survives title, status, candidate, and projection changes. The dated slug is a stable physical location, not the semantic identity. Prefer an exact `record_ref` when already known.

Create with:

```bash
python3 <skill-root>/scripts/workspace.py resolve-record \
  --repo <repository> \
  --owner <owner> \
  --subject <stable-subject> \
  --slug <stable-slug> \
  --create
```

Legacy records without `subject` remain readable. Upgrade one only through its exact `record_ref`; do not guess its subject or allocate another record beside ambiguous legacy state.

A record projection uses the resolved record slug, for example:

```text
.qp/records/atona/20260827-checkout-recovery/checkout-recovery.html
```

A standalone artifact uses its own real slug:

```text
.qp/artifacts/20260827-architecture-review/architecture-review.html
```

Never create a new QP artifact or projection as `index.html`. Existing `index.html` files are legacy diagnostics, not new write targets.

## 3. Write records and settings through exact-current compare-and-swap

The semantic owner supplies:

- complete owner-native frontmatter except `updated_at` and `revision`;
- the complete Markdown body;
- semantic validity of record type, status, transitions, candidate, evidence, and body; and
- the exact digest returned by `read-record`, or `absent` for a new record.

Akọsílẹ̀ validates only the generic envelope and canonical path. It locks the resource, rereads under the lock, rejects stale identity or digest, assigns `updated_at` and the next revision, atomically replaces the file, rereads it, and rebuilds the index. A verified record remains authoritative if a later index rebuild fails; report that derived failure.

Use JSON for the owner-supplied frontmatter candidate:

```bash
python3 <skill-root>/scripts/workspace.py write-record \
  --repo <repository> \
  --record-ref <owner>/<record-id> \
  --frontmatter-file <candidate.json> \
  --body-file <candidate.md> \
  --expected-digest <sha256-or-absent>
```

For settings, base the complete JSON-object candidate on `read-settings` and pass its exact digest. Preserve unknown sections. Never overwrite malformed settings or infer a consumer's schema.

Do not bypass the engine for a write that claims Akọsílẹ̀ safety. Writes that bypass the engine are outside this guarantee. When their drift is observed, stop and reconcile instead of retrying blindly.

## 4. Keep generated navigation derived

`.qp/INDEX.md` is rebuilt from valid generic record frontmatter and sorted by the chronological instant represented by `updated_at`, newest first. It links `record.md` and the expected slug-named HTML projection only when that file exists. Invalid records and duplicate subjects remain visible as diagnostics.

Records remain authoritative. The index never sets owner state, validity, completion, or lifecycle status.

`doctor` may report malformed settings/records, missing subjects, duplicate subjects, stale index state, symlink or path escape, legacy roots, legacy `index.html`, and missing Git hygiene. `repair` may recreate directories, initialize missing `{}`, rebuild the index, and update repository-local Git exclude; it does not delete or migrate the reported legacy material.

## 5. Return a verified workspace operation

Return:

```text
Operation:
Workspace:
Resource identity:
Absolute path:
Workspace path:
Previous digest/revision:
Current digest/revision:
Index state:
Git-hygiene state:
Result:
Conflict or limitation:
```

Use the exact structured engine result. For generated resources intended for direct user access, lead with the resolved absolute filesystem path and repository-relative `.qp/...` path. Absolute machine paths are operational output, not portable source identity.

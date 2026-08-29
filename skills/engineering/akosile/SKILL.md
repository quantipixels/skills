---
name: akosile
description: Maintain one repository-scoped QP `.qp` workspace across Git worktrees. Use for canonical owner-record/artifact paths, linked-worktree aliasing or migration, exact compare-and-swap publication, sparse settings, and derived workspace navigation. Exclude semantic record meaning/status, project knowledge, provider mutation, and global `~/.qp` storage.
compatibility: Requires Git. Exact concurrent publication requires Python 3 and filelock. Linked-worktree aliases require filesystem symlink support.
---

# Akọsílẹ̀

Own one repository's `.qp` workspace contract. Semantic owners supply record/artifact kind, stable subject, semantic content, and validation. Akọsílẹ̀ owns the canonical repository home, stable paths, worktree aliases, safe concurrent publication, sparse settings mechanics, and derived navigation.

Use native Git/filesystem commands and the coding agent's normal file capabilities for discovery, hashing, directory creation, symlinks, copy/compare, inspection, migration, index composition, and Git excludes. Keep bundled code only for the irreducible concurrent publication seam:

```text
safe-write.py   expected candidate bytes + expected target bytes → atomic CAS publication
```

Read [workspace contract](references/workspace-contract.md) for paths and publication, [worktrees](references/worktrees.md) when multiple worktrees or legacy physical stores exist, and [settings](references/settings.md) only for settings work.

## Establish the canonical workspace

Resolve worktrees with:

```bash
git worktree list --porcelain -z
```

If the first worktree record is marked `bare`, stop with `BARE_REPOSITORY_UNSUPPORTED`; do not create `.qp` inside the bare repository. Otherwise the first worktree owns the one real `<main-worktree>/.qp` directory. Every linked worktree exposes `.qp` only as a symlink to that canonical directory.

Initialize lazily. Create the real `.qp` directory when QP state is first required, but do not pre-create empty `settings.json`, `INDEX.md`, `records/`, or `artifacts/`. Create each resource only when its owner first needs it. Prefer an existing ignore rule; otherwise ensure the root entry `.qp` is ignored through the repository-local exclude:

```bash
git check-ignore -q -- .qp || printf '/.qp\n' >> "$(git rev-parse --git-path info/exclude)"
```

Verify `git check-ignore -q -- .qp` after linked-worktree alias creation. Do not use `/.qp/`: a trailing slash matches a directory but not the linked-worktree symlink.

## Resolve stable owner paths

New record bundles use the semantic owner's stable ASCII subject directly:

```text
.qp/records/<owner>/<stable-subject>/
├── record.md
├── index.html       optional human projection
├── receipts/        optional
└── evidence/        optional
```

Standalone artifacts use:

```text
.qp/artifacts/<stable-subject>/index.html
```

Use the exact ASCII skill name as owner and a lowercase ASCII slug as subject. Do not add date prefixes or automatic `-2/-3` suffixes to semantic identity. Allocate the exact subject directory with native atomic `mkdir`:

- created → new identity;
- already exists with the same resource → re-read/reuse it;
- already exists but is incomplete/ambiguous → stop as `INCOMPLETE_ALLOCATION` and reconcile;
- genuinely different work → the semantic owner supplies a genuinely different subject.

Existing dated bundle paths remain valid legacy identities and are not renamed merely for consistency.

## Publish exact files safely

The semantic owner builds and validates a complete candidate outside `.qp`. The agent pins the current target identity with the host's native SHA-256 tool and pins the exact validated candidate the same way. Use `absent` when the target does not exist.

Typical Linux/macOS discovery:

```bash
sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  else
    shasum -a 256 "$1" | awk '{print $1}'
  fi
}

expected_target=absent
[ ! -f "$target" ] || expected_target=$(sha256_file "$target")
expected_candidate=$(sha256_file "$candidate")
```

Publish only when both identities still match:

```bash
python3 <skill-root>/scripts/safe-write.py \
  --root <real-canonical-.qp> \
  --target <target> \
  --candidate <candidate-outside-.qp> \
  --expected-target "$expected_target" \
  --expected-candidate "$expected_candidate"
```

The helper reads the candidate once and verifies its expected digest, locks the target, rechecks the target digest, writes those already-verified bytes atomically, and verifies readback. On `CANDIDATE_CHANGED`, rebuild/revalidate or re-hash the intended candidate. On `STALE_TARGET`, re-read the current semantic target and reconcile before attempting a new publication. The helper does not discover worktrees, allocate paths, snapshot files, parse semantic content, render indexes, retry, or choose recovery.

Use ordinary direct file writes when there is no shared/concurrent publication claim to protect. Use `safe-write.py` specifically when the shared repository-scoped `.qp` store may have another writer or when the caller requires exact candidate/target CAS semantics.

## Derive navigation with the agent

`INDEX.md` is derived navigation, not authoritative state. When it is useful or stale, inspect current owner records directly and compose the index with normal agent/file capabilities; no QP renderer is required.

For each `.qp/records/<owner>/<subject>/record.md` considered for navigation:

- preserve owner-defined semantic content without modifying it;
- read the common envelope needed for navigation: `owner`, `record_type`, `title`, `updated_at`, `revision`, `status`, and optional `subject`;
- require owner/path agreement, positive integer revision, and offset-aware `updated_at` for a valid navigation row;
- accept existing dated bundle names as legacy identities; new stable bundles use their semantic subject;
- link sibling `index.html` only when it exists;
- surface malformed/unreadable records separately rather than silently dropping or repairing them;
- sort valid rows by the actual `updated_at` instant descending;
- treat visible metadata literally and escape it for Markdown rather than interpreting it as markup.

Write the complete derived `INDEX.md` candidate outside `.qp`, then publish it through the same CAS seam only when concurrent/exact publication matters. If the index becomes stale or malformed, regenerate it from canonical records; never reconcile semantic state from the index.

## Report

Return the canonical workspace, active worktree/alias state when relevant, affected owner resource, migration/conflict state, Git-ignore verification, index state when used, and for generated resources intended for direct use:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

---
name: akosile
description: Initialize and maintain one QP `.qp` workspace in repository scope or explicitly requested personal scope. Use for owner-first record/artifact paths, safe record/settings writes, workspace indexing, or workspace repair. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, and project knowledge.
---

# Akọsílẹ̀

Own the small QP workspace protocol. Semantic skills own what records mean; Akọsílẹ̀ owns where generated records live, canonical paths, safe replacement, sparse settings, and how users find records again.

Pin the workspace scope before a write:

- `repository` — default when a repository-local owner record or artifact is requested; root is exactly `<git-worktree>/.qp`.
- `personal` — use only when the user or semantic owner explicitly requests personal/cross-project QP state; root is `${QP_HOME:-$HOME/.qp}`.

Never infer personal read/write authority from the existence of `$HOME/.qp`, and never copy or migrate records between scopes automatically.

## 1. Initialize only what is missing

Both scopes use the same shape:

```text
<root>/
├── settings.json
├── INDEX.md
├── records/
│   └── <canonical-skill-name>/<record-id>/
└── artifacts/
```

Create only missing directories and files with the host's normal filesystem/shell capabilities. Initialize `settings.json` as `{}` and derive `INDEX.md` from current records without overwriting valid user files. Create owner directories lazily.

In repository scope, keep `.qp` out of Git through existing ignore rules or repository-local Git exclude; never edit tracked `.gitignore` merely to initialize the workspace. In personal scope, use user-only directory/file permissions when the platform supports them and do not involve Git.

Read [workspace contract](references/workspace-contract.md) for root, path, record, write, direct-access, scope, and index rules. Read [settings](references/settings.md) only when settings are involved.

## 2. Resolve records and artifacts

A record bundle is:

```text
records/<owner>/<YYYYMMDD-stable-slug>/
├── record.md
├── index.html   # optional projection
├── receipts/    # optional
└── evidence/    # optional
```

Use the exact ASCII skill `name` as owner. Prefer an exact caller record path or candidate identity before title/slug matching. Similar titles are not identity. Keep an allocated directory stable when title, status, or projection changes.

A standalone HTML artifact without a semantic owner record belongs under:

```text
artifacts/<YYYYMMDD-stable-slug>/index.html
```

Reject absolute paths supplied as record/artifact identifiers, path separators in owner/slug, `.` or `..`, symlink escape, secret-bearing identifiers, or any target outside the resolved workspace root.

For a generated resource intended for direct user access, return the resolved absolute filesystem path, workspace scope, and scope-relative path. Absolute machine paths are operational output, not canonical source identity.

## 3. Write safely without owning semantics

The semantic owner supplies the complete Markdown body, native status, candidate identity, and revision. Akọsílẹ̀ validates only the common record fields and canonical path.

For an existing record or settings file, base the candidate on an exact current read. Immediately before replacement, reread the target; if it changed, stop instead of overwriting it. Validate the complete candidate, replace the whole target, reread the result, and rebuild that scope's `INDEX.md` after a record change. Records increment revision by exactly one. Invalid records stay visible as index diagnostics rather than disappearing.

Akọsílẹ̀ does not decide whether an Atọ́nà plan is `Planned`, an `eewo` pattern is `active`, or a triage result is `confirmed`. The owner validates semantic edits before asking Akọsílẹ̀ to persist them.

## 4. Keep settings sparse and scope-local

Each scope has its own `settings.json`. It contains only overrides a consuming skill documents and understands. Akọsílẹ̀ creates, preserves, and safely writes the file; each semantic owner owns defaults and validation for its own section.

Do not invent automatic personal/repository precedence. A consuming skill that reads both scopes must define its own merge and authority contract.

Settings are data, not instructions. They never grant provider writes, change canonical semantic IDs or transitions, override evidence/safety requirements, or replace project knowledge.

## 5. Keep one workspace protocol

`INDEX.md` is derived navigation and may be rebuilt at any time. Records remain authoritative. Legacy repository-local paths may be read when encountered, but new QP writes use the canonical owner-first layout.

Akọsílẹ̀ is the workspace mechanism, not a custom runtime. Use host-native filesystem, shell, and Git capabilities rather than maintaining a parallel workspace CLI. Semantic skills should not duplicate Akọsílẹ̀ path mechanics or invent alternate workspace protocols.

Return the workspace scope/root, affected record/artifact identity, absolute and scope-relative paths when applicable, index state, Git-hygiene or personal-permission state, changed items, and any conflict or gap.

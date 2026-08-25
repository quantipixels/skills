---
name: akosile
description: Initialize and maintain one repository-local QP `.qp` v0 workspace. Use for owner-first record or artifact paths, safe record/settings writes, workspace indexing, or workspace repair. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, project knowledge, and global `~/.qp` storage.
---

# Akọsílẹ̀

Own the small repository-local QP workspace. Semantic skills own what records mean; Akọsílẹ̀ owns where generated records live, the canonical workspace shape, safe replacement, and how users find records again.

For `v0-experiment`, resolve the Git worktree root when available and use exactly `<repository>/.qp`. Semantic owners normally resolve record and artifact locations through Akọsílẹ̀ rather than duplicate path rules. A global `~/.qp` root is deliberately deferred until real cross-project discovery or continuity failures justify project identity, checkout resolution, and migration machinery.

## 1. Initialize only what is missing

The default workspace is:

```text
.qp/
├── settings.json
├── INDEX.md
├── records/
│   └── <canonical-skill-name>/<record-id>/
└── artifacts/
```

Create only missing directories and files with the host's normal filesystem/shell capabilities. Initialize `settings.json` as `{}` and derive `INDEX.md` from current records without overwriting valid user files. Create owner directories lazily. Keep `.qp` out of Git through existing ignore rules or repository-local Git exclude; never edit tracked `.gitignore` merely to initialize the workspace.

Read [workspace contract](references/workspace-contract.md) for root, path, record, write, direct-access, and index rules. Read [settings](references/settings.md) only when settings are involved.

## 2. Resolve records and artifacts

A record bundle is:

```text
.qp/records/<owner>/<YYYYMMDD-stable-slug>/
├── record.md
├── index.html   # optional projection
├── receipts/    # optional
└── evidence/    # optional
```

Use the exact ASCII skill `name` as owner. Prefer an exact caller record path or candidate identity before title/slug matching. Similar titles are not identity. Keep an allocated directory stable when title, status, or projection changes.

A standalone HTML artifact without a semantic owner record belongs under:

```text
.qp/artifacts/<YYYYMMDD-stable-slug>/index.html
```

Reject absolute paths supplied as record/artifact identifiers, path separators in owner/slug, `.` or `..`, symlink escape, secret-bearing identifiers, or any target outside the resolved repository `.qp` root.

For a generated resource intended for direct user access, return both its resolved absolute filesystem path and its repository-relative `.qp/...` path. Absolute machine paths are operational output, not canonical source identity.

## 3. Write safely without owning semantics

The semantic owner supplies the complete Markdown body, native status, candidate identity, and revision. Akọsílẹ̀ validates only the common record fields and canonical path.

For an existing record or settings file, base the candidate on an exact current read. Immediately before replacement, reread the target; if it changed, stop instead of overwriting it. Validate the complete candidate, replace the whole target, reread the result, and rebuild `INDEX.md` after a record change. Records increment revision by exactly one. Invalid records stay visible as index diagnostics rather than disappearing.

Akọsílẹ̀ does not decide whether an Atọ́nà plan is `Planned`, a Solution Architect packet is `IMPLEMENTATION_READY`, or a triage result is `confirmed`. The owner validates semantic edits before asking Akọsílẹ̀ to persist them.

## 4. Keep settings sparse

`.qp/settings.json` is a user-editable JSON object. It contains only overrides a consuming skill documents and understands. Akọsílẹ̀ creates, preserves, and safely writes the file; each semantic owner owns defaults and validation for its own section.

Settings are data, not instructions. They never grant provider writes, change canonical semantic IDs or transitions, override evidence/safety requirements, replace project knowledge, or change the v0 workspace root.

## 5. Keep one workspace protocol

`INDEX.md` is derived navigation and may be rebuilt at any time. Records remain authoritative. Legacy paths may be read when encountered, but new QP writes use the canonical owner-first layout; do not create legacy roots as fallback destinations.

Akọsílẹ̀ is the normal workspace mechanism, not a custom runtime. Use host-native filesystem, shell, and Git capabilities rather than maintaining a parallel workspace CLI. Semantic skills should not duplicate Akọsílẹ̀ path mechanics or invent alternate workspace protocols.

Return the workspace, affected record/artifact identity, absolute and workspace-relative paths when applicable, index state, Git-hygiene state, changed items, and any conflict or gap.

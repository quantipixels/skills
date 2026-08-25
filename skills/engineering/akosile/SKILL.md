---
name: akosile
description: Initialize and maintain one repository-local QP `.qp` v0 workspace. Use for owner-first record or artifact paths, safe record/settings writes, workspace indexing, or workspace repair. Exclude semantic record meaning, owner-native status validity or transitions, provider mutation, project knowledge, and global `~/.qp` storage.
---

# Akọsílẹ̀

Own the small repository-local QP workspace. Semantic skills own what records mean; Akọsílẹ̀ owns where generated records live, how paths are resolved, how they are written safely, and how users find them again.

For `v0-experiment`, the canonical root is fixed at `<repository>/.qp`. Semantic owners must request record or artifact locations from Akọsílẹ̀ rather than construct `.qp` paths themselves. A global `~/.qp` root is deliberately deferred until real cross-project discovery or continuity failures justify project identity, checkout resolution, and migration machinery.

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

Use `scripts/workspace.py init`. It creates missing directories, an empty `{}` settings file, and the derived index without overwriting valid user files. Create owner directories lazily. Keep `.qp` out of Git through the repository's existing ignore rules or repository-local Git exclude; never edit tracked `.gitignore` merely to initialize the workspace.

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

For a generated resource intended for direct user access, return both:

- its resolved absolute filesystem path for immediate opening/use; and
- its `.qp` workspace-relative path for stable project-local reference.

Absolute machine paths are operational output, not canonical source identity, and should not be embedded into portable records or HTML unless the user explicitly needs them there.

## 3. Write safely without owning semantics

The semantic owner supplies the complete Markdown body, native status, candidate identity, and revision. Akọsílẹ̀ validates only the common record fields and canonical path, then writes atomically.

For an existing record or settings file, require the digest read by the caller. Reject stale or invalid candidates before replacement. After a record write, rebuild `.qp/INDEX.md` directly from valid record frontmatter. Invalid records remain listed as diagnostics rather than disappearing.

Akọsílẹ̀ does not decide whether an Atọ́nà plan is `Planned`, a Solution Architect packet is `IMPLEMENTATION_READY`, or a triage result is `confirmed`. The owner must validate manual/user semantic edits before asking Akọsílẹ̀ to write them.

## 4. Keep settings sparse

`.qp/settings.json` is a user-editable JSON object. It contains only overrides a consuming skill documents and understands. Akọsílẹ̀ creates, preserves, and safely writes the file; each semantic owner owns defaults and validation for its own section.

Settings are data, not instructions. They never grant provider writes, change canonical semantic IDs or transitions, override evidence/safety requirements, replace project knowledge, or change the v0 workspace root.

## 5. Repair and degrade safely

`INDEX.md` is derived navigation and may be rebuilt at any time. Records remain authoritative. Legacy paths may be discovered by their native owner, but Akọsílẹ̀ does not move or reinterpret them automatically.

If Akọsílẹ̀ is unavailable, the semantic owner may return its result inline or use an exact caller-supplied path. Report workspace integration as unavailable rather than duplicating this protocol.

Return:

```text
Akọsílẹ̀ result
Operation: init | resolve-record | resolve-artifact | write-record | write-settings | index
Workspace: <resolved absolute repository .qp path>
Record or artifact: <identity or none>
Absolute path: <resolved path for the produced resource, when applicable>
Workspace path: <.qp-relative path for the produced resource, when applicable>
Index: CURRENT | INCOMPLETE
Git hygiene: CURRENT | INCOMPLETE | NOT_APPLICABLE
Changed: <created/updated or none>
Conflicts and gaps: <items or none>
```

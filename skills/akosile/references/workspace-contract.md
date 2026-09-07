# Workspace contract

Akọsílẹ̀ owns repository-shared storage mechanics. Semantic owners retain record meaning, status, evidence, transitions, and validation.

## Canonical repository state

Resolve the exact Git common directory and keep one physical store at:

```text
<git-common-dir>/qp/
├── settings.json                         optional, created on first settings write
├── INDEX.md                              optional generated navigation
├── records/<owner>/<stable-subject>/     owner record bundle
└── artifacts/<stable-subject>/           standalone artifact bundle
```

A worktree root `.qp` is only a symlink/view onto this store. The canonical directory is independent of main/linked worktree identity. A bare repository can therefore retain state even when no working tree exists.

A new record subject is a lowercase ASCII slug supplied by its semantic owner. Stable subject is stable identity; do not derive another identity from title/date changes or filename collision suffixes. Existing dated bundle names remain accepted legacy identities.

A record bundle's semantic source is `record.md`. `index.html` is an optional derived human projection. `INDEX.md` is derived navigation. Divergent derived bytes never outrank semantic source.

## Common record envelope

Akọsílẹ̀ may validate only the cross-owner envelope needed for storage/indexing:

```yaml
owner: <canonical skill name>
record_type: <non-empty owner-defined type>
title: <human title>
updated_at: <offset-aware ISO-8601>
revision: <positive integer>
status: <non-empty owner-defined state>
subject: <stable subject, optional for legacy records>
```

Write each common-envelope value as one top-level single-line scalar: plain, JSON-compatible double-quoted, or YAML single-quoted. Do not use block scalars, collections, tags, anchors, or aliases for common-envelope fields. Owner-specific nested metadata may follow; index rendering ignores it.

The semantic owner validates owner-specific fields and transitions. When `subject` is present, it must match the bundle directory.

## Worktree-visible alias

For each registered worktree that needs repository-relative access:

```text
<worktree>/.qp → <git-common-dir>/qp
```

Treat this symlink as reconstructible derived state. Verify it resolves to the canonical store and is ignored by Git. Prefer a relative link when it remains correct/stable for the actual topology; otherwise use the narrowest reliable link form supported by the host. Do not persist alias targets as semantic workspace metadata.

If symlinks are unsupported, do not mirror/copy the store into each worktree. Report an alias capability gap only to consumers that require the worktree-visible `.qp/...` path; canonical storage operations may still use the real Git-common path.

## Allocation

Create the exact owner/subject directory with native atomic directory creation. Existing directory means re-read/reuse or reconcile incomplete allocation; never invent `-2`, `-3`, or another semantic identity to escape a collision.

Create optional `receipts/`, `evidence/`, `index.html`, settings, or index only when an owning operation actually needs them.

## Safe publication

Mutation root must be the real `<git-common-dir>/qp`, never a worktree alias. Build complete validated candidates outside that root, pin candidate and target identity with native SHA-256 tooling, and publish through `safe-write.py` only when shared writers/exact publication claims require CAS. The helper is a byte-publication kernel; it does not snapshot targets or own semantic merge policy.

For generated navigation, render to stdout, capture candidate outside the store, then publish exact bytes through the same CAS seam.

## Locators

When a worktree alias exists, return both canonical filesystem identity and worktree-relative `.qp/...` locator for human/tool convenience. In bare/no-worktree contexts return only the canonical path/semantic identity supported by the current host; do not fabricate a workspace-relative worktree path.
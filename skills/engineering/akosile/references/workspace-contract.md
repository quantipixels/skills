# Workspace contract

Akọsílẹ̀ owns repository-local storage mechanics. Semantic owners retain record meaning, status, evidence, transitions, and validation.

## Canonical resources

Create resources lazily under the one real repository `.qp`:

```text
.qp/
├── settings.json                         optional, created on first settings write
├── INDEX.md                              optional generated navigation
├── records/<owner>/<stable-subject>/     owner record bundle
└── artifacts/<stable-subject>/           standalone artifact bundle
```

A new record subject is a lowercase ASCII slug supplied by its semantic owner. Stable subject is stable identity; do not derive a new identity from title changes, date changes, or filename collision suffixes. Existing dated bundle names are accepted legacy identities.

A record bundle's semantic source is `record.md`. `index.html` is an optional derived human projection. `INDEX.md` is derived navigation. Divergent derived bytes never outrank the semantic source.

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

Write each common-envelope value as one top-level, single-line scalar: a plain value, a JSON-compatible double-quoted string, or a YAML single-quoted string. Do not use block scalars, collections, tags, anchors, or aliases for common-envelope fields. Owner-specific nested metadata may follow; the index renderer ignores it. The renderer uses only the Python standard library, rejects duplicate top-level keys and unsupported common-envelope forms, and does not execute YAML tags or constructors.

The semantic owner validates all owner-specific fields and whether its status/revision transition is valid. When `subject` is present, it must match the bundle directory.

## Allocation

Create the exact owner/subject directory with native atomic directory creation. Existing directory means re-read/reuse or reconcile an incomplete allocation; never invent `-2`, `-3`, or another semantic identity to escape a collision.

Create optional `receipts/`, `evidence/`, `index.html`, settings, or index only when an owning operation actually needs them.

## Safe publication

Mutation roots must be the real canonical `.qp`, never a linked-worktree alias. Build complete validated candidates outside `.qp`, pin both candidate and target identity, and publish through `safe-write.py`. The helper is a byte-publication kernel; it does not own semantic merge policy.

For generated navigation, render to stdout, capture the candidate outside `.qp`, then publish that exact candidate through the same CAS seam.

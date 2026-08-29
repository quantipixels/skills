# Workspace contract

Akọsílẹ̀ owns repository-local storage mechanics. Semantic owners retain record meaning, status, evidence, transitions, and validation.

## Canonical resources

Create resources lazily under the one real repository `.qp`:

```text
.qp/
├── settings.json                         optional, created on first settings write
├── INDEX.md                              optional derived navigation
├── records/<owner>/<stable-subject>/     owner record bundle
└── artifacts/<stable-subject>/           standalone artifact bundle
```

A new record subject is a lowercase ASCII slug supplied by its semantic owner. Stable subject is stable identity; do not derive a new identity from title changes, date changes, or filename collision suffixes. Existing dated bundle names are accepted legacy identities.

A record bundle's semantic source is `record.md`. `index.html` is an optional derived human projection. `INDEX.md` is derived navigation. Divergent derived bytes never outrank the semantic source.

## Common record envelope

Akọsílẹ̀ may inspect only the cross-owner envelope needed for storage/navigation:

```yaml
owner: <canonical skill name>
record_type: <non-empty owner-defined type>
title: <human title>
updated_at: <offset-aware ISO-8601>
revision: <positive integer>
status: <non-empty owner-defined state>
subject: <stable subject, optional for legacy records>
```

The semantic owner validates all owner-specific fields and whether its status/revision transition is valid. When `subject` is present, it must match the bundle directory.

## Allocation

Create the exact owner/subject directory with native atomic directory creation. Existing directory means re-read/reuse or reconcile an incomplete allocation; never invent `-2`, `-3`, or another semantic identity to escape a collision.

Create optional `receipts/`, `evidence/`, `index.html`, settings, or index only when an owning operation actually needs them.

## Exact publication

Mutation roots must be the real canonical `.qp`, never a linked-worktree alias. Build complete validated candidates outside `.qp`. Use the agent/host's native SHA-256 capability to pin the current target (`absent` when missing) and the exact validated candidate. Use `safe-write.py` only for the final compare-and-swap publication when shared/concurrent writers or an exact publication claim make that guarantee material.

`safe-write.py` owns only:

```text
expected candidate digest
+ expected target digest
+ candidate read stability
+ target writer exclusion
+ atomic replacement
+ exact readback
```

It does not snapshot targets, discover paths, interpret owner records, render derived files, retry, or choose semantic recovery.

## Derived navigation

`INDEX.md` has no private renderer. When navigation is needed, the agent reads canonical owner records, validates only the common envelope/path agreement needed for the index, sorts valid rows by the actual offset-aware `updated_at` instant descending, escapes visible metadata literally, links sibling `index.html` only when present, and reports malformed records separately.

Compose the complete index candidate outside `.qp`. Publish it with ordinary file capabilities when no concurrent/exact publication claim exists; otherwise pass the candidate and current target/candidate digests through `safe-write.py`.

A stale or broken index is regenerated from `record.md`; it never participates in semantic conflict resolution.

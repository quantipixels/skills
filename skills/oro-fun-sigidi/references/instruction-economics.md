# Instruction economics

Read when routing pointers, always-loaded instructions, disclosure, or pruning may change agent behaviour or context pressure.

The objective is not minimum words. Spend context only where it changes selection, judgment, authority, execution, or completion.

## Two loads

Agent-facing systems spend two different budgets:

- **context load** — text that is present whether or not it is useful now, such as skill descriptions and repository-level instructions;
- **human cognitive load** — things a person must remember to invoke or maintain because they are not automatically discoverable.

A model-invoked skill trades some context load for discoverability. A human-only instruction trades model context for human memory. Choose deliberately; neither load should be driven to zero by default.

## Pointers must carry trigger information

A pointer is useful only if the agent can tell when to follow it. A skill description, an instruction line naming another file, or a workflow branch all fail when the target is good but the selection condition is vague.

Write distinct trigger branches, not synonym coverage. Preserve wording that changes routing; remove wording that only restates the target.

## Use progressive disclosure by branch

Keep universal rules where every invocation sees them. Move conditional expertise behind a pointer only when the root can reliably identify the condition that loads it.

Do not equate file size with load. Inspect the real path: a tiny entrypoint that always opens five references may cost and distract more than one cohesive file.

## Apply the no-op test

A sentence is a deletion candidate when removing it is unlikely to change:

- selection or disclosure;
- a recurring non-obvious decision;
- authority or safety;
- evidence/completion semantics;
- recovery/compatibility behaviour; or
- useful domain expertise.

Generic diligence, ordinary tool mechanics, cached repository facts, repeated summaries, and rationale with no behavioural consequence are common no-ops for capable models.

Keep deliberate repetition when it protects different boundaries. A generation rule and an independent verification condition may sound similar while serving different failure modes.

## Preserve semantics before compressing

For material pruning, compare old and candidate contracts. Pay particular attention to:

- public triggers and exclusions;
- routing topology and adjacent-owner boundaries;
- authority and provider effects;
- evidence/proof admission;
- candidate/source identity;
- recovery, retry, cancellation, and liveness;
- compatibility and legacy invocation; and
- conditional references whose load path changed.

A rule is not redundant because another sentence uses similar words. Show that the replacement preserves the same behavioural boundary.

For frontier-capability claims, compare realistic tasks against the ordinary model/host without the guidance. A good no-skill baseline can justify deleting generic scaffolding; it does not prove specialised expertise or topology unnecessary.

## Stop when deletion creates guessing

Shorter text is worse when the agent must reconstruct a consequential distinction that the previous instruction made explicit. Stop pruning when the next cut would make behaviour, authority, coverage, or recovery materially ambiguous.

Record material retired/relocated semantics in the PR or review discussion; do not create a permanent dossier merely to justify a rewrite.

# Editing agent text

Use for reviewing, revising, or pruning supplied agent-facing prose.

Pin exact identifiers, schemas/fields, accepted decisions, current authority, and the behaviour graph before changing them. This pin is for deliberate evolution, not automatic preservation.

## Map the behaviour graph

Identify the current:

- trigger and exclusions;
- branches and skip conditions;
- actions/prohibitions;
- authority and side effects;
- bounds/evidence conditions;
- recovery/retry semantics; and
- pointers to deeper material.

Then decide what each material part should become: **retain**, **strengthen**, **relocate**, **replace**, or **retire**.

A wording-only edit should not silently change those semantics. A refactor may change them when the requested scope and evidence justify it.

## Remove load by effect

Prefer this order:

1. delete **no-ops** the capable model already performs without the instruction;
2. delete **caches** of cheap environment/repository facts;
3. remove **duplication** and keep one authoritative meaning;
4. remove **sediment** that no longer bears on the owned result;
5. replace superseded mechanism with the current abstraction/skill/tool;
6. move branch-specific expertise behind a reliable pointer;
7. compress repeated explanations with a strong established term;
8. remove examples that neither replace prose nor prevent a plausible wrong action;
9. replace long constructions with direct, precise language.

Keep deliberate repetition only when the repeated text protects a different trigger, authority boundary, recovery condition, or independent verification step.

## Preserve what is live, not what is old

Do not keep topology, compatibility, or safeguards merely because they existed before. Keep them when they still change useful behaviour or protect a necessary boundary.

Good:

- Retire a compatibility note after the compatibility window genuinely ends.
- Replace repeated setup prose with `qp-setup` plus the one relevant mode/constraint.
- Keep a routing boundary that prevents a real adjacent-owner collision.

Bad:

- Delete a live route because the model can probably infer it.
- Keep obsolete workflow choreography solely to avoid semantic loss.
- Treat historical wording as the acceptance target.

## Tighten bounds, not ceremony

When a step tends to stop too early, first improve its bound.

Good:

> Account for every changed public contract.

Bad:

> Be thorough before continuing.

Only add more staging, review, or isolation when the failure cannot be fixed by a clearer/demanding bound.

## Prefer positive target behaviour

Phrase the desired action directly. Keep prohibitions for hard boundaries or observed failure modes.

Good: `Name the exact skill and useful variant.`

Weak: `Do not use vague owner language.`

## Verify proportionally

Compare the candidate with the intended current behaviour, not blindly with the old wording.

Ask:

1. Can the agent still tell when the text applies?
2. Are the remaining branches and owner boundaries intentional?
3. Did any permission or side effect broaden unintentionally?
4. Are material bounds/evidence requirements clear and demanding enough?
5. Does each moved reference retain a strong pointer?
6. Were compatibility or recovery semantics deliberately retained/replaced/retired?
7. Did the change actually remove no-op/cache/sediment rather than just shorten sentences?

For meaningful behaviour changes, use realistic before/after tasks. For ordinary editorial cleanup, do not invent an evaluation harness.

Report only material semantics retired/replaced/relocated and any proof gap. Word count describes compression; it does not prove improvement.

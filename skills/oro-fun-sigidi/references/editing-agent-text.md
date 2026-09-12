# Editing agent text

Use for reviewing, revising, or pruning supplied agent-facing prose.

Preserve exact identifiers, accepted decisions, required schemas/fields, and authority boundaries. Do not turn a prose pass into an unrequested redesign.

## Preserve the behaviour graph

Before editing, identify the existing:

- trigger and exclusions;
- branches and skip conditions;
- actions/prohibitions;
- authority and side effects;
- completion/evidence conditions;
- recovery or retry semantics; and
- pointers to deeper material.

A stylistic edit should not silently add, remove, reorder, or reinterpret those. Flag a behaviour-changing correction explicitly.

## Remove load by effect

Prefer this order:

1. remove filler, assistant-performance language, repeated summaries, and duplicated rationale;
2. merge statements with genuinely identical behavioural effect;
3. move branch-specific expertise behind a reliable pointer;
4. remove examples that neither replace prose nor prevent a material error;
5. replace long constructions with direct, precise language.

Keep repetition that protects a distinct trigger, safety/authority boundary, recovery condition, or verification step.

Do not delete topology merely because a capable model can infer a plausible path. If a route, dependency, handoff, or exception is intentional behaviour, preserve it until evidence shows the replacement is equivalent.

## Verify the revision

Compare the final text against the original and ask:

1. Can the agent still tell when the text applies?
2. Are all material branches and owner boundaries intact?
3. Did any permission or side effect become broader or less explicit?
4. Are completion/evidence requirements still reachable at the right point?
5. Did a moved reference keep a reliable loading condition?
6. Did any compatibility behaviour disappear unintentionally?

For material pruning, report the meaningful behaviour that was removed, merged, or relocated and any proof gap. Do not claim equivalence from word count alone.

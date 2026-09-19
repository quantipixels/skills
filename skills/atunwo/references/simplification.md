# Simplification review

Use for unnecessary complexity in a bounded system or exact change, at the selected light or deep review depth. Keep the entrypoint's inspection-only boundary for simplification-only requests. Prefer elimination, direct state, local ownership, deep modules, native capability, and YAGNI; retaining the current form is valid.

## Choose a clearer sufficient form

Understand the actual flow, consumers, contracts, and proof before proposing reduction. Prefer the earliest sound option:

1. Eliminate behavior or mechanisms with no required contract or consumer.
2. Reuse existing implementation, then native platform/framework capability, then installed dependencies.
3. Derive duplicated state when timing, ownership, history, and cost permit it.
4. Localize policy and state with their real owner.
5. Simplify the remaining control flow and interfaces without moving complexity into callers.

Use Beck's simple-design order: preserve behavior, reveal intent, remove duplicated knowledge, then unnecessary elements. Apply KISS to reasoning burden, not line count. Preserve useful names, intermediates, comments, guards and cleanup. Generalization needs real variation or a meaningful boundary; scores justify neither extraction nor deletion.

Use complexity, churn, fan-out, invalid states and lifecycle transitions as leads. Before proposing extraction, compare policy ownership, caller knowledge, navigation and proof across the affected path. Flag relocated complexity when it worsens caller burden, ownership or proof; a named operation may still lower reasoning cost without reducing branches. Prefer representations that exclude invalid combinations while preserving timing and lifecycle contracts.

## Match the scope

For a system, sample relevant boundaries in light review or cover the agreed inventory in deep review: source, entry points, build, tests, dependencies, configuration, tooling, and generated/runtime behavior. Classify material removal candidates as `retain | delete-safe | blocked`. Search absence is not deletion proof: account for dynamic/framework/generated reachability, external consumers, configuration/data, history, migration, and proof owners. Remove an implementation only when its obligation is obsolete or another implementation fulfills it; remove proof only when its obligation is obsolete or retained evidence covers it at least as strongly.

For a change, inspect scope drift, speculative abstractions, parallel implementations, compatibility paths, unnecessary dependencies, duplicated policy/state, and production seams introduced only for shallow tests. Dead code is not automatically a blocking defect. Preserve justified deliberate limits and their observable revisit triggers.

Assess tests by the contract they can independently falsify. Mirrored production logic, mock choreography, private-structure snapshots, library-owned behavior, duplicate proof, and disproportionate scaffolding are candidates for reduction. Retain tests that uniquely protect material invariants and real regressions. Passing checks or coverage alone proves neither redundancy nor clarity.

For a proposed test merge, deletion, or move to a stronger proof owner, name the surviving guarantee and explain why distinct failure detection remains. If a simplification eliminates invalid states, reconsider proof for those states rather than preserving obsolete tests. Implementation and rerunning affected checks remain with `alaga` or the active delivery owner.

## Return actionable findings

For each material opportunity, identify its location, concrete maintenance burden, proposed improvement, retained behavior and supporting evidence. Include counterevidence, risks, dependencies and future proof ownership when they affect the recommendation. Prioritize by expected benefit and risk; state blocked deletions and justified retains. Implementation stays with its owner; use `architect` only for an unresolved structural design question.

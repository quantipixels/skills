# Simplification review

Use for unnecessary complexity in a bounded system or exact change, at the selected light or deep review depth. Keep the entrypoint's inspection-only boundary for simplification-only requests. Prefer elimination, direct state, local ownership, deep modules, native capability, and YAGNI; retaining the current form is valid.

## Choose a clearer sufficient form

Understand the actual flow, consumers, contracts, and proof before proposing reduction. Prefer the earliest sound option:

1. Eliminate behavior or mechanisms with no required contract or consumer.
2. Reuse existing implementation, then native platform/framework capability, then installed dependencies.
3. Derive duplicated state when timing, ownership, history, and cost permit it.
4. Localize policy and state with their real owner.
5. Simplify the remaining control flow and interfaces without moving complexity into callers.

Apply KISS to reasoning burden, not line count. Preserve useful names, intermediate values, comments, guard clauses and cleanup. A helper needs a coherent operation; generalization needs real variation or a meaningful boundary. File size and scores alone justify neither extraction nor deletion.

Use complexity, churn, fan-out, invalid states, and lifecycle transitions as leads, not findings. Before proposing extraction, compare policy ownership, caller knowledge, navigation, meaningful decisions, and proof burden across the whole affected path. Reject relocated complexity; a clearer named operation can still help when state or branch counts remain unchanged. Prefer representations that exclude invalid combinations when they preserve timing and lifecycle contracts.

## Match the scope

For a system, sample relevant boundaries in light review or cover the agreed inventory in deep review: source, entry points, build, tests, dependencies, configuration, tooling, and generated/runtime behavior. Classify material removal candidates as `retain | delete-safe | blocked`. Search absence is not deletion proof: account for dynamic/framework/generated reachability, external consumers, configuration/data, history, migration, and proof owners. Preserve public, security, integrity, concurrency, recovery, adapter, runtime, interaction, and accessibility contracts without a stronger complete owner.

For a change, inspect scope drift, speculative abstractions, parallel implementations, compatibility paths, unnecessary dependencies, duplicated policy/state, and production seams introduced only for shallow tests. Dead code is not automatically a blocking defect. Preserve justified deliberate limits and their observable revisit triggers.

Assess tests by the contract they can independently falsify. Mirrored production logic, mock choreography, private-structure snapshots, library-owned behavior, duplicate proof, and disproportionate scaffolding are candidates for reduction. Retain tests that uniquely protect material invariants and real regressions. Passing checks or coverage alone proves neither redundancy nor clarity.

For a proposed test merge, deletion, or move to a stronger proof owner, name the surviving guarantee and explain why distinct failure detection remains. If a simplification eliminates invalid states, reconsider proof for those states rather than preserving obsolete tests. Available mutation results can expose weak detection; investigate surviving non-equivalent mutants without imposing a universal score target. Implementation and rerunning affected checks remain with `alaga` or the active delivery owner.

## Return actionable findings

For each material opportunity, give its location, current maintenance cost, proposed sufficient form, why it lowers total burden, counterevidence, retained contracts, risk, and future verification or proof owner. Rank by impact, risk, effort, and dependencies; identify implementation slices without executing them. State blocked deletion claims and a justified retain result where appropriate. Use `architect` only for an unresolved structural design question.

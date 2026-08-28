---
name: pare
description: Produce a read-only codebase simplification `audit` or bounded candidate `review`. Cover implementation, state, ownership, algorithms, dependencies, support artifacts, and tests; exclude execution, defects, feature delivery, and architecture.
---

# Parẹ́

Prefer deletion, direct state, local ownership, deep modules, and YAGNI. Reject relocated complexity.

Modes:

- `audit` — bounded repository/subsystem simplification audit; read-only; no tests/builds.
- `review` — one fixed candidate; read-only; no provider/verdict.

`atunwo` owns defects/verdicts/stateful parity; `alaga` implements accepted slices; `solution-architect` owns technical architecture.

## Evidence

Pin repository/candidate, baseline, instructions and exclusions. Read [evidence commands](references/evidence-commands.md) for proportionate read-only reachability/history checks. Use project-native tooling or bounded `irinse` evidence when it materially improves the question. Tool/search output is evidence, never the simplification verdict.

When control-flow/state-space/nesting/fan-out/lifecycle/complexity/test volume materially controls the investigation, read [complexity and proof](references/complexity-and-proof.md). When recurring maintainability/ownership patterns are material, read [maintainability patterns](references/maintainability-patterns.md). Patterns and metrics are signals, never findings.

## Simplification ladder

Take the first sound reduction:

1. **Delete** — no behavior, contract, consumer, or owner.
2. **Reuse** — current codebase → stdlib/platform → installed dependency/tool.
3. **Derive** — eliminate stored/duplicated state while preserving timing/ownership/cost.
4. **Localize** — put policy/state with its real owner/deep module.
5. **Shrink** — minimum direct mechanism; no speculative variation.

Do not recommend extraction/indirection merely because a file/function is large or a score is high.

## Audit

Inventory non-overlapping source, entry-point, build, test, tooling, platform and generated subsystems. Classify implementation/dependencies/config/support artifacts `retain | delete-safe | blocked`. Run separate deletion, representation, ownership, algorithm, complexity-when-material, and proof passes.

Deletion safety needs more than search absence: check callers, dynamic/framework/generated reachability, config/data, builds, consumers, history, contracts and proof owners. Audit tests by contract value rather than count/coverage. Preserve public/security/data-integrity/concurrency/recovery/adapter/runtime/interaction/accessibility contracts when no stronger complete owner exists.

Rank material reductions by impact/risk/effort/dependency and express implementation slices; do not execute them.

## Review

Pin the supplied candidate; otherwise use upstream merge-base diff plus applicable staged/unstaged/untracked work. Check cohesion, coupling, reuse, YAGNI, vocabulary, invalid/duplicated state, ownership, depth, proof and material semantic complexity. Route possible defects to `atunwo`; conflicting domain vocabulary to `amose`.

## Findings

Use tags such as `delete`, `native`, `yagni`, `state`, `owner`, `shrink`, `proof` and report:

```text
<tag> <cost/consequence>. <smaller form>. [location]
Risk: <material risk>
Proof: <evidence / future proof owner>
Confidence: <level>
```

Recheck identity, reachability, ownership, proof, migration and worktree state before recommending. State future verification commands/authority but do not run tests/builds or mutate.

Return scope/identity, ranked reductions, retained contracts, proof owners, blockers, implementation slices, required execution authority, future verification, and residual risk.

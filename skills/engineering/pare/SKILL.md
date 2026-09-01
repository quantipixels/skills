---
name: pare
description: Produce a read-only codebase simplification `audit` or bounded candidate `review`. Cover implementation, state, ownership, algorithms, dependencies, support artifacts, and tests; exclude execution, defects, feature delivery, and architecture.
---

# Parẹ́

Prefer elimination, direct state, local ownership, deep modules, native capability, and YAGNI. Reject relocated complexity.

Modes:

- `audit` — bounded repository/subsystem simplification audit; read-only; no tests/builds.
- `review` — one fixed candidate; read-only; no provider/verdict.

Keep defect verdicts/stateful parity, implementation, and technical architecture outside this read-only simplification result.

## Evidence

Pin repository/candidate, baseline, instructions and exclusions. Inspect only the current consumers, history, configuration, generated/framework reachability, and project-native evidence needed to distinguish material simplification claims. Search or tool absence is never deletion proof by itself, and tool/metric output is evidence rather than the simplification verdict.

When control-flow/state-space/nesting/fan-out/lifecycle/complexity/test volume materially controls the investigation, read [complexity and proof](references/complexity-and-proof.md). When recurring maintainability/ownership patterns are material, read [maintainability patterns](references/maintainability-patterns.md). Patterns and metrics are signals, never findings.

## Simplification ladder

Take the first sound reduction after understanding the real flow/consumers/contracts:

1. **Eliminate** — the mechanism need not exist, or an existing element has no required behavior, contract, consumer, or owner.
2. **Reuse** — current codebase → stdlib/framework/platform → installed dependency/tool.
3. **Derive** — eliminate stored/duplicated state while preserving timing/ownership/cost.
4. **Localize** — put policy/state with its real owner/deep module.
5. **Shrink** — minimum direct mechanism; no speculative variation.

Do not recommend extraction/indirection merely because a file/function is large or a score is high. A new abstraction is not simplification unless it removes net semantic burden and owns a current variation or independently real boundary.

## Audit

Inventory non-overlapping source, entry-point, build, test, tooling, platform and generated subsystems. Classify implementation/dependencies/config/support artifacts `retain | delete-safe | blocked`. Run separate deletion, representation, ownership, algorithm, complexity-when-material, and proof passes.

Deletion safety needs more than search absence: check callers, dynamic/framework/generated reachability, config/data, builds, consumers, history, contracts and proof owners. Preserve public/security/data-integrity/concurrency/recovery/adapter/runtime/interaction/accessibility contracts when no stronger complete owner exists.

Audit tests by durable contract value rather than count/coverage. A test is a simplification candidate when evidence shows it cannot independently falsify a material contract, recomputes/mirrors production logic, verifies mocks/choreography rather than behavior, protects private structure, tests framework/library behavior the project does not own, duplicates stronger proof, requires disproportionate scaffolding, or survives only as construction history. Do not recommend deletion when the test uniquely protects a material stable invariant even if its implementation is small.

Rank material reductions by impact/risk/effort/dependency and express implementation slices; do not execute them.

## Review

Pin the supplied candidate; otherwise use the exact current change boundary. Check cohesion, coupling, reuse, YAGNI, vocabulary, invalid/duplicated state, ownership, depth, proof and material semantic complexity.

Also check:

- change-envelope drift: touched subsystems/files/contracts that do not have a concise requested-behavior or proof reason;
- scope expansion through new dependencies, parallel implementations, compatibility paths, speculative abstractions, or unrelated cleanup;
- production architecture introduced mainly for testability without an independently real production boundary;
- edge-case machinery that could disappear by eliminating/strengthening the causal state or owner; and
- durable tests against stable seam, independent oracle, falsifiability, stronger existing proof, and maintenance burden.

Treat passing tests, coverage, line-count reduction, or tool scores as evidence only. Demonstrably dead or redundant code may be surfaced as a cleanup recommendation when safe removal is supported by evidence; its mere presence is not a blocking finding. Route possible defects to `atunwo`; conflicting domain vocabulary to `amose`.

When a deliberate simplification has a documented ceiling/revisit trigger, preserve it if current evidence supports it. A material deliberate limitation with no observable revisit trigger is a maintainability concern, not a reason to manufacture a separate debt system.

## Findings

Use tags such as `delete`, `native`, `yagni`, `state`, `owner`, `scope`, `test`, `shrink`, `proof` and report:

```text
<tag> <cost/consequence>. <smaller form>. [location]
Risk: <material risk>
Proof: <evidence / future proof owner>
Confidence: <level>
```

Recheck identity, reachability, ownership, proof, migration and worktree state before recommending. State future verification/authority without executing tests/builds or mutating.

Return scope/identity, ranked reductions, retained contracts, proof owners, blockers, implementation slices, required execution authority, future verification, and residual risk.

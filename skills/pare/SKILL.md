---
name: pare
description: Assess simplification opportunities in a bounded software system or code change, read-only. Cover implementation, state, ownership, algorithms, dependencies, support artifacts, and tests; exclude execution, defects, feature delivery, and architecture.
---

# Parẹ́

Prefer elimination, direct state, local ownership, deep modules, native capability, and YAGNI. Reject relocated complexity. A reduction must preserve or improve readability.

Delegate substantial analysis, research, and expert work to subagents, returning concise findings and evidence links to keep the main context lean.

Set the scope to the requested system/subsystem or exact code change. Use the shared evidence and simplification criteria below; select system inventory or change inspection according to that scope. Stay read-only: do not run tests/builds, write to providers, or issue candidate acceptance verdicts.

Keep defect verdicts/stateful parity, implementation, and technical architecture outside this read-only simplification result.

## Evidence

Pin the software system/candidate, baseline, instructions and exclusions. Inspect only the current consumers, implementation/configuration, history, generated/framework reachability, and system-native evidence needed to distinguish material simplification claims. Search or tool absence is never deletion proof by itself, and tool/metric output is evidence rather than the simplification verdict.

When control-flow/state-space/nesting/fan-out/lifecycle/complexity/test volume materially controls the investigation, read [complexity and proof](references/complexity-and-proof.md). When recurring maintainability/ownership patterns are material, read [maintainability patterns](references/maintainability-patterns.md). Patterns and metrics are signals, never findings.

## Simplification ladder

Understand the real flow, consumers, and contracts. Choose a reduction only when it lowers overall maintenance and comprehension burden while preserving required behavior. Retaining the current form is a valid outcome. Consider these options:

1. **Eliminate** — the mechanism need not exist, or an existing element has no required behavior, contract, consumer, or owner.
2. **Reuse** — current implementation/system capability → stdlib/framework/platform → installed dependency/tool.
3. **Derive** — eliminate stored/duplicated state while preserving timing/ownership/cost.
4. **Localize** — put policy/state with its real owner/deep module.
5. **Simplify** — minimize total semantic and cognitive burden across implementation and callers. Preserve idiomatic, readable control flow; do not compress code merely to reduce lines or move complexity into callers.

Do not recommend extraction/indirection merely because a file/function is large or a score is high. Extract a helper when its name and boundary make a coherent operation easier to understand, considering navigation and caller burden. Reuse or independent lifecycle ownership is not required for every helper. A general-purpose abstraction still needs a current variation or independently real boundary that justifies its added machinery.

## Readability constraint

Reduce responsibilities and reasoning burden, not formatting. Removing useful whitespace or line breaks, collapsing statements, and compressing expressions are not acceptable code-reduction outcomes. Do not count formatter churn or fewer physical lines as simplification.

Preserve helpful names, intermediate values, explanatory comments, guard clauses, and explicit lifecycle steps. Additional lines can make control flow, state transitions, errors, and cleanup easier to follow. Compare the original and proposed forms on those paths; reject a reduction that makes them harder to understand, even if behavior is unchanged and tests pass. Describe what knowledge, state, policy, or indirection disappears and why the remaining code is at least as readable.

## System inventory

When the scope is an existing system or subsystem:

Inventory non-overlapping source, entry-point, build, test, tooling, platform, runtime/configuration, and generated subsystems. Classify implementation/dependencies/config/support artifacts `retain | delete-safe | blocked`. Run separate deletion, representation, ownership, algorithm, complexity-when-material, and proof passes.

Deletion safety needs more than search absence: check callers, dynamic/framework/generated reachability, config/data, builds, consumers, history, contracts and proof owners. Preserve public/security/data-integrity/concurrency/recovery/adapter/runtime/interaction/accessibility contracts when no stronger complete owner exists.

Audit tests by durable contract value rather than count/coverage. A test is a simplification candidate when evidence shows it cannot independently falsify a material contract, recomputes/mirrors production logic, verifies mocks/choreography rather than behavior, protects private structure, tests framework/library behavior the project does not own, duplicates stronger proof, requires disproportionate scaffolding, or survives only as construction history. Do not recommend deletion when the test uniquely protects a material stable invariant even if its implementation is small.

Rank material simplifications by impact/risk/effort/dependency and express implementation slices; do not execute them. Credit clearer forms even when they require more lines, and retain the current implementation when alternatives add burden. When scattered caller knowledge, forwarding layers, duplicated policy, or shallow seams indicate a deepening opportunity, identify the misplaced responsibility and caller burden. Use `architect` as needed.

## Change inspection

When the scope is a code change:

Pin the supplied candidate; otherwise use the exact current change boundary. Check cohesion, coupling, reuse, YAGNI, vocabulary, invalid/duplicated state, ownership, depth, proof and material semantic complexity.

Also check:

- change-envelope drift: touched subsystems/files/contracts that do not have a concise requested-behavior or proof reason;
- scope expansion through new dependencies, parallel implementations, compatibility paths, speculative abstractions, or unrelated cleanup;
- production architecture introduced mainly for testability without an independently real production boundary;
- edge-case machinery that could disappear by eliminating/strengthening the causal state or owner; and
- durable tests against stable seam, independent oracle, falsifiability, stronger existing proof, and maintenance burden.

Treat passing tests, coverage, line-count reduction, or tool scores as evidence only. Demonstrably dead or redundant code may be surfaced as a cleanup recommendation when safe removal is supported by evidence; its mere presence is not a blocking finding. Use `amose` and `architect` as needed.

When a deliberate simplification has a documented ceiling/revisit trigger, preserve it if current evidence supports it. A material deliberate limitation with no observable revisit trigger is a maintainability concern, not a reason to manufacture a separate debt system.

## Findings

Use tags such as `delete`, `native`, `yagni`, `state`, `owner`, `scope`, `test`, `shrink`, `proof` and report:

```text
<tag> <cost/consequence>. <proposed form and why it is simpler to maintain>. [location]
Risk: <material risk>
Proof: <evidence / future proof owner>
Confidence: <level>
```

Recheck identity, reachability, ownership, proof, migration and relevant workspace state before recommending. State future verification/authority without executing tests/builds or mutating.

Return scope/identity, ranked simplifications or a justified retain result, retained contracts, proof owners, blockers, implementation slices, required execution authority, future verification, and residual risk.

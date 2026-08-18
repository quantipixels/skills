---
name: pare
description: "Produce a read-only codebase simplification `audit` or bounded candidate `review`. Cover implementation, state, ownership, algorithms, dependencies, support artifacts, and tests; exclude execution, defects, feature delivery, and architecture."
---

# Parẹ́

Prefer deletion, direct state, local ownership, deep modules, and YAGNI. Reject relocated complexity.

## Modes

- `audit`: every subsystem; read-only; no test runs.
- `review`: one fixed candidate; read-only; no provider or verdict.

Never edit files, run tests or builds, change Git state, execute cleanup, or use provider writes. Return recommendations and implementation slices only.

`atunwo` owns defects, verdicts, and providers; `alaga` implements accepted slices; `atona` owns architecture; `audit-refactor-behavior` owns stateful parity. A `deep-clean candidate` requires explicit opt-in before `alaga` may abandon non-contract proof.

Use `rg` and `git` directly for proportionate read-only reachability and history checks. When a companion tool could materially improve the evidence, give `irinse` the bounded question and candidate, then consume its exact-current read-only result. `pare` retains simplification judgment and never treats tool output as a verdict.

## Ladder

Understand the flow; take the first sound reduction:

1. Delete: no behavior, contract, consumer, or owner.
2. Reuse: codebase → stdlib → platform → installed dependency.
3. Derive: preserve timing, consistency, lifecycle, cost, ownership.
4. Localize: owned model, state machine, deep module, or policy.
5. Shrink: minimum direct mechanism; no speculation.

- Good: remove invalid states.
- Bad: wrap the same branches.

## Tags and finding format

- `delete`: dead
- `native`: stdlib/platform
- `yagni`: unproved variation
- `state`: invalid/duplicate
- `owner`: scattered policy
- `shrink`: less mechanism
- `proof`: stronger owner

```text
<tag> <cost>. <smaller form>. [path]
```

Add risk, proof, confidence. Smells are not evidence. For each `Needs defect review` concern, report its location, scope, reason, evidence, and possible consequence.

## `audit`

Pin repository, baseline, instructions, exclusions. Inventory non-overlapping source, entry-point, build, test, tool, platform, and generated subsystems; record boundary, interfaces, callers, tests, status. Exclusions need owner/reason; `not reviewed` means `PARTIAL`.

Run separate deletion, representation, ownership, algorithm, and proof passes. Do not let easy dead code replace state-space, lifecycle, cross-language policy, or repeated scan/copy analysis.

Classify implementation, dependencies, configuration, and support artifacts as `retain | delete-safe | blocked`. Check interfaces, callers, dynamic/platform/generated reachability, builds, consumers, and owners; search alone does not prove deletion.

Audit tests with the cleanup taxonomy. Classify each coherent group as `retain | delete-safe | deep-clean candidate | blocked`; report its signal, stronger proof owner, consequence, and required authority. `delete-safe` requires complete stronger static, contract, integration, or acceptance proof. A `deep-clean candidate` may abandon non-contract proof but requires explicit opt-in before execution.

Target existence, typecheck-satisfied, implementation-detail, duplicate, provider-shape, snapshot, layout, render-presence, registration, and shallow UI proof without a selected contract. Retain public, security, integrity, recovery, adapter, runtime, interaction, and accessibility contracts. Handwritten provider fixtures do not prove live compatibility.

Find material reductions per subsystem. Verify semantics, ownership, migration, proof; deduplicate. Independently check coverage, materiality, priorities, dependencies. Complete when all subsystems are `recommend` or `skip`; report inventory, ranking, skips, slices, limits, worktree evidence.

## `review`

Pin the supplied candidate. Otherwise use the upstream merge-base diff plus applicable staged, unstaged, and untracked work; apply repository rules first. Check cohesion, coupling, reuse, YAGNI, vocabulary, waste, depth, testability, documentation, and applicable audit classifications. Send conflicting domain vocabulary to `amose`. Recommend compatibility removal only when proved unreleased with no consumers. Recheck identity; report findings, gaps, boundary, limits.

- Good: `state Stored total can diverge from owned line items. Derive it at the owner. [checkout.ts:42]`
- Bad: “This class is long; split it.”

## Verify recommendations

Recheck identity, reachability, ownership, proof, migration, risk, and worktree state with read-only evidence. State the future verification commands and authority; do not run them. Stop on ambiguity, drift, missing content, uncertain consumers, or unsupported claims.

Report scope, identities, ranked reductions, retained contracts, proof owners, `deep-clean candidate` consequences, blockers, implementation slices, required execution authority, future verification, and residual risk.

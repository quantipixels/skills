# Anti-overengineering engineering guard

QP should constrain agent over-engineering without adding a master coordinator, a parallel implementation lifecycle, or a family of overlapping audit/test-debt skills. The control model combines three distinct failure boundaries: scope drift before/during work, unnecessary mechanism selection, and review/proof loops that accrete machinery instead of converging.

## Decision

Engineering work follows three composable guards:

```text
scope control
    ↓
minimum sufficient mechanism
    ↓
convergence + proof control
```

`scope-guard` is the reusable public steering contract for users/agents that explicitly need this behavior surfaced or carried across hosts. It does not own implementation, architecture, review, proof, or lifecycle state. Existing owners carry the relevant invariants directly so Scope Guard does not become a mandatory phase.

## 1. Scope control

Before material coding, establish the exact outcome, local non-goals/task exclusions, expected change envelope, explicitly unchanged contracts, and smallest sufficient proof. Understand the affected flow and real owners before optimizing for a small diff.

Local non-goals/task exclusions are strong negative boundaries for this task, plan, specification, or implementation. They do not become the project's durable root `.nongoals`; that file remains the project-wide exclusion contract owned by `amose`.

The expected change envelope is not a frozen file list. Material growth is a diagnostic event: re-check whether initial understanding was incomplete, the causal owner is wrong, workaround layers are accumulating, or a genuine scope expansion has been discovered.

The following are scope-expansion events when they were not already accepted:

- new dependency, framework, service, runtime, or infrastructure;
- public API/schema/storage/migration/wire/compatibility changes;
- material new abstraction/configuration mechanisms;
- unrelated subsystem changes or opportunistic cleanup;
- parallel/duplicate implementations or compatibility paths;
- new test infrastructure or production architecture introduced mainly for testability; and
- destructive data/history/deployment/credential/provider effects.

An extra file is not automatically expansion. If the requested outcome still works without the material expansion, shrink back. If it does not, surface why and route the decision/authority instead of silently enlarging the task.

## 2. Minimum sufficient mechanism

After understanding the flow, prefer the first sound option:

```text
eliminate
→ reuse current project capability
→ stdlib/framework/platform/language/database native capability
→ already-selected dependency/tool
→ derive duplicated state / localize policy at its owner
→ minimum new mechanism
```

No indirection exists for hypothetical variation. A new abstraction needs either a current second consumer/variant or an independently real boundary such as external protocol, trust, persistence, volatile platform integration, lifecycle, or policy ownership.

For defects, optimize for the narrowest confirmed causal owner that covers affected paths, not the smallest textual patch. For architecture, eliminate causal state/duplicate ownership before designing reconciliation or edge-case machinery around it.

A deliberate simplification with a known limit should record its ceiling and an observable revisit trigger at the natural owner. Local mechanism → code comment; architectural decision → ADR; actual planned work → issue; durable project truth → `.learnings`. QP does not create a separate simplification-debt ledger merely for this convention.

## 3. Convergence control

Review may discover broadly; it does not silently expand the accepted implementation contract.

Before applying a review correction:

1. confirm the concern is inside the accepted contract/blocking criteria;
2. ask whether the causal state/branch/duplicate owner can be removed or strengthened so the edge case disappears;
3. prefer an existing mechanism at the real owner; and
4. identify any scope-expansion event and route it rather than auto-building it.

This prevents the failure loop where a reviewer finds a rare edge case, a fixer introduces a new subsystem, the subsystem creates new edge cases, and review continues indefinitely.

Before delivery closes, every touched file, new abstraction, dependency, compatibility path, and durable test should have a concise requested-contract or necessary-proof reason to exist. Passing tests and line-count reduction are evidence only.

## Proof and tests

QP requires proof, not a new test.

A persistent test earns admission only when it protects a material contract through a stable behavior-bearing seam, uses an oracle/expectation independent of production logic, and would fail for a plausible wrong implementation for the right reason. Stronger existing proof should be reused instead of duplicated.

Tests are rejected as durable proof when they merely:

- recompute/mirror the production algorithm;
- verify mocks return configured values or assert internal choreography;
- protect private structure rather than a contract;
- test framework/library behavior the project does not own;
- duplicate stronger existing proof; or
- require testability architecture/scaffolding disproportionate to the protected invariant.

TDD is used when the user explicitly requests test-first delivery or when a material behavior seam with an independent oracle lets a failing test genuinely control implementation. A production-behavior change alone is not enough. Glue, wiring, declarative configuration, trivial delegation, and framework-native usage may be proved by stronger/cheaper evidence without a new test.

TDD is red → green in vertical behavior slices. Structural refactoring and durable test-portfolio simplification happen in the normal review/convergence stage, where the full candidate can be judged together. Development tests/probes/harnesses do not automatically earn permanent repository residence.

## Instruction design discipline

QP optimizes for the smallest instruction surface that reliably produces the intended behavior, not the fewest instructions. A deliberately expensive instruction is valid when it overrides a likely model tendency that would otherwise damage the owner's outcome and its cost is proportionate to the improvement.

Audit each consequential instruction by:

```text
default tendency
→ owner-specific failure
→ deliberate override
→ value gained
→ cost incurred
→ trigger calibration
→ cross-owner composition
```

Do not simplify these established patterns merely because they add friction:

- `arojinle`'s relentless complete material decision frontier trades convenience for decision completeness, clarity, and explicit user authority;
- `atona` keeps semantic Markdown as the exact-current machine/agent record while HTML remains its primary approachable human operating view;
- bounded delegation in owners such as `arojinle`, `atona`, and `wo-pr` may deliberately isolate noisy/independent work so it does not pollute the primary reasoning/user context;
- local non-goals remain strong task/plan/spec/implementation direction guards while root `.nongoals` remains durable project-wide exclusion knowledge;
- Alága's delivery proof followed by Àtúnwò broad review and Parẹ́ maintainability/simplification review is deliberate defense-in-depth; constrain correction scope/convergence rather than deleting review merely because it is expensive;
- Wò PR's use of `se-triage` for reviewer claims prevents a reviewer statement from becoming mutation authority by default; and
- provider-capable owners repeat independently required trust, credential, completeness, refresh, and readback invariants so each remains safe when invoked alone.

An instruction still fails when a useful mechanism is mis-triggered. Eager TDD was such a case: tests can be valuable while `production behavior changed → TDD` was too broad.

## Owner mapping

- `scope-guard` — reusable prospective steering contract; no lifecycle.
- `alaga` — carries change-envelope, minimum-mechanism, proof-admission, correction-convergence, and final necessity gates during delivery.
- `pare` — read-only simplification judgment, including scope drift and durable test value.
- `atunwo` — defect/review verdict; tests count as proof only when they can independently discriminate wrong behavior; review findings do not grant scope-expansion authority.
- `solution-architect` — native/current capability before new mechanisms, real-boundary requirement for abstraction, and simpler causal/state models before reconciliation machinery.
- `irinse` — current/project-native evidence before adding tools; new tooling is surfaced as consuming-task scope expansion when not already accepted.
- `ko-skill` — one canonical semantic skill contract, thin host projections, behavioral instruction admission, steering-effect proof when materially needed, and no counterfactual productivity claims without a comparable observed baseline.
- `ayewo-igba-ise` — evidence-backed retrospective signals for recurring scope/test/review over-engineering; it does not turn the signals into automatic scores or new rules.

## Host portability

The semantic source remains the owning skill, not a Codex `AGENTS.md`, Claude plugin rule, Cursor rule, or other host-specific copy. Add a host adapter only when actual loader semantics require one. Keep adapters thin and mechanically verify them when drift would be consequential.

Do not add adapters merely to claim compatibility already supplied by normal skill installation. This preserves agent-agnostic behavior while allowing Codex or another host to project the same contract later.

## Behavioral evidence

QP does not add a standing prompt benchmark suite merely to defend these instructions. When a model-steering change remains materially uncertain, `ko-skill` may compare the same realistic bounded task/candidate/context under the prior/no contract and changed contract, then verify both the intended behavior shift and preserved correctness/safety.

Persist a behavioral regression suite only when recurring stable risk justifies maintaining it. Do not claim saved LOC, tokens, cost, time, latency, or quality without an observed comparable baseline. A smaller source tree or diff is simplification evidence, not a counterfactual productivity measurement.

Real agent sessions/corpora feed `ayewo-igba-ise`. Repeated evidence can justify a later smaller policy correction through `ko-skill`; one incident does not earn another rule.

Experimental skills remain opt-in and cannot silently displace stable owners. However, exact-current evidence from an explicitly selected experiment may be evaluated by `ko-skill` for later promotion, consolidation, or stable-owner correction; the stable portfolio remains authoritative until that decision is made.

## Evidence-gated open questions

Do not change these from intuition alone:

- the mandatory `technical-writing` → `yo-slop` chain for ordinary PR descriptions, commit messages, and small technical communication should be compared against direct owner output and `technical-writing` alone before being narrowed; preserve the chain until evidence shows the second pass adds no reliable value;
- lightweight steering owners such as `salaye` and `ro-wo` remain valid while their named contracts provide useful reusable behavior; base-model capability alone is not removal evidence; and
- Experimental `pepeye` remains explicit-only until repeated task evidence justifies promotion or architecture-level adoption.

## Rejected alternatives

- no QP clone of Ponytail review/audit/debt/gain/help skills;
- no `test-hygiene` or separate testing lifecycle skill;
- no mandatory `scope-guard` phase before every implementation;
- no `lite/full/ultra` hidden intensity state;
- no blanket `production behavior changed → TDD` rule;
- no fixed requirement to leave one new test behind;
- no "fewest LOC wins" acceptance target;
- no automatic reviewer-found edge case → implementation expansion;
- no handwritten behavior copies across host adapters;
- no instruction cleanup that removes deliberate friction solely because a capable model can perform the underlying act.

The stable owners remain independently useful deep modules. The engineering guard constrains how they choose scope, mechanism, proof, and instruction behavior without creating a new coordinator above them.

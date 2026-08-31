---
name: scope-guard
description: Constrain one bounded coding task against over-engineering before or during implementation. Pin the exact outcome, local non-goals/task exclusions, expected change envelope, proof, scope-expansion events, and minimum sufficient mechanism. Use when the user asks to prevent scope creep or over-engineering, keep an agent narrow, make the smallest sound change, or establish a pre-implementation guard. Exclude implementation, architecture ownership, review verdicts, and repo-wide simplification.
---

# Scope Guard

Keep one coding task from silently becoming a larger task. Scope Guard is a lightweight steering contract, not a lifecycle, implementation owner, reviewer, or persistent mode. Apply it directly while another owner works, or return the compact guard when the user wants to carry it into another agent/host.

## Pin before building

Understand the affected flow, current owners, contracts, and real callers before minimizing anything. Then pin:

- **outcome** — the exact requested behavior/result;
- **local non-goals / task exclusions** — strong negative implementation boundaries for what this task will not solve or change; keep them with this task/plan/spec and do not promote them into repository-level `.nongoals` unless `amose` separately establishes a durable project-wide exclusion;
- **expected change envelope** — likely owners, subsystems, files/surfaces, and explicitly unchanged contracts; this is an evidence-backed expectation, not a prohibition on necessary discovery; and
- **proof** — the smallest evidence that can establish completion.

A small diff in the wrong place is not simplification. Revisit the causal owner when the change envelope starts growing rather than preserving the first plan by adding workaround layers.

## Minimum sufficient mechanism

After understanding the real flow, take the first sound option:

1. **Eliminate** — the requested mechanism is unnecessary because existing behavior already satisfies the outcome, or the causal state/branch can be removed.
2. **Reuse project capability** — use an existing helper, owner, module, pattern, or proof surface.
3. **Use native capability** — standard library, framework, platform, language, database, or other native mechanism.
4. **Use an already-selected dependency/tool** — do not add a dependency for behavior current capabilities adequately provide.
5. **Derive or localize** — remove duplicated/stored state or place policy/state at its real owner.
6. **Add minimally** — introduce only the mechanism the confirmed outcome still requires.

Do not introduce indirection for hypothetical variation. A new interface, adapter, factory, configuration layer, generic mechanism, or similar abstraction needs either a current second consumer/variant or an independently real boundary such as an external protocol, trust boundary, persistence boundary, volatile platform integration, or owned lifecycle/policy boundary.

For a defect, prefer the narrowest confirmed causal owner that covers the affected paths rather than the smallest textual patch or repeated guards at symptoms.

## Scope-expansion events

Treat these as material expansion signals when they were not already part of the accepted task:

- a new dependency, framework, service, runtime, or infrastructure component;
- a public API, schema, storage, migration, wire-format, or compatibility-contract change;
- a new abstraction/configuration mechanism that materially changes the design shape;
- unrelated subsystem changes, cleanup, or opportunistic refactoring;
- parallel/duplicate implementations or compatibility paths;
- new test infrastructure or production architecture introduced mainly for testability; and
- destructive data, history, credential, deployment, or provider effects.

An extra touched file is not automatically scope expansion. When the envelope grows materially, ask whether the original outcome can still be achieved without the expansion. If yes, shrink back. If no, state why the expansion is necessary, what contract/authority it changes, and route any required decision or authority instead of silently enlarging the task.

## Proof without test inflation

Proof is required; a new test is not.

Prefer existing affected proof, type/compiler guarantees, static analysis, build/schema validation, focused runtime probes, real integration checks, bug reproduction, browser/manual verification, or another stronger current proof surface when they can falsify the changed contract.

A new durable test earns its place only when it protects a material contract through a stable behavior-bearing seam, has an expectation/oracle independent of production logic, and would fail for a plausible wrong implementation for the right reason. Do not create a production abstraction solely to make a test convenient unless that abstraction also owns a real production boundary. New test infrastructure is a scope-expansion event.

## Converge instead of accreting

Review may discover broadly; it does not silently enlarge the accepted implementation contract. Before implementing a review correction, ask:

1. Is the concern inside the accepted contract/blocking criteria?
2. Can the state, branch, duplicate owner, or causal condition producing the edge case be removed or strengthened instead?
3. Can an existing mechanism handle it at the real owner?
4. Would the correction trigger a scope-expansion event?

Prefer eliminating the cause over adding edge-case machinery. If the required correction genuinely expands scope, surface the expansion instead of building a second system around the first.

Before completion, every touched file, new abstraction, dependency, compatibility path, and durable test should have a concise contract/proof reason to exist. Passing tests or a smaller line count do not justify unnecessary structure.

When a deliberate simplification has a known ceiling, record the simplification, the ceiling, and an observable revisit trigger at its natural owner: local code comment for a local mechanism, ADR for architecture, issue for planned work, or `.learnings` for durable project knowledge. Do not create a separate debt ledger merely for the convention.

## Result

When used as a standalone guard, return only:

```text
Outcome: <exact result>
Local non-goals / exclusions: <strong negative implementation boundaries>
Change envelope: <expected owners/surfaces + unchanged contracts>
Proof: <smallest sufficient proof>
Expansion gates: <material unapproved scope-expansion events>
Ceilings: <deliberate simplification + revisit trigger, or none>
```

When used inside active work, apply the contract without creating parallel lifecycle state. The implementation, architecture, review, proof, publication, and durable-knowledge owners keep their normal authority and results.

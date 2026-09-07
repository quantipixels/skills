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

After understanding the real flow, prefer in order:

1. eliminate unnecessary mechanism or causal state;
2. reuse existing project capability;
3. use native platform/framework/language capability;
4. use an already-selected dependency/tool;
5. derive duplicated state or localize policy at its real owner; then
6. add only the mechanism the confirmed outcome still requires.

Do not introduce indirection for hypothetical variation. A new abstraction needs a current real variant/consumer or independently real production boundary; testing convenience alone is not such a boundary.

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

An extra touched file is not automatically scope expansion. When the envelope grows materially, ask whether the original outcome can still be achieved without the expansion. If yes, shrink back. If no, state why the expansion is necessary and what contract or authority changes instead of silently enlarging the task.

## Proportional proof

Proof is required; a new test is not. Prefer existing affected proof, type/compiler guarantees, static analysis, build/schema validation, focused runtime probes, real integration checks, bug reproduction, browser/manual verification, or another stronger current proof surface when it can falsify the changed contract.

Do not add durable tests, test infrastructure, or production abstractions merely to increase proof volume. When test/proof portfolio judgment itself becomes material, leave the deeper maintainability or delivery judgment to its owning result rather than reproducing it here.

## Converge instead of accreting

Review may discover broadly; it does not silently enlarge the accepted implementation contract. Before accepting a correction, ask whether it is inside the accepted contract, whether the causal state/duplicate mechanism can be removed instead, whether an existing owner/mechanism already covers it, and whether the correction triggers scope expansion.

Before completion, every touched file, new abstraction, dependency, compatibility path, and durable test should have a concise contract/proof reason to exist. Passing tests or a smaller line count do not justify unnecessary structure.

When a deliberate simplification has a known ceiling, record the simplification, ceiling, and observable revisit trigger at its natural owner rather than creating a parallel debt ledger.

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

---
name: alaga
description: Deliver one supplied build job from settled outcome through implementation, proof, review, and handoff. Use for a bounded test-first feature/fix or any build/migration requiring an exact reviewed candidate. Exclude pure explanation, bare review, monitoring, and provider publication except where they support delivery.
---

# Alága

Deliver one supplied software/build job as a coherent proved result. Use `test-first` only when the user requests it or a material behavior-bearing seam with an independent oracle makes a failing test capable of controlling implementation; otherwise use `job`.

## 1. Map the job

Pin only what can change delivery:

- outcome and current/desired behavior;
- scope and local non-goals/task exclusions;
- expected change envelope and explicitly unchanged contracts;
- acceptance and smallest sufficient proof;
- governing specification/decision identities when present;
- documentation or durable-knowledge obligations that belong in the delivered result; and
- workspace and mutation authority.

Treat local non-goals as active negative implementation boundaries. Material growth outside the expected envelope is a signal to re-check understanding, causal ownership, or scope rather than preserve the first plan with workaround layers.

Respect explicit owner/tool choices and consume another owner's result only when delivery actually depends on an independently useful decision, architecture, specification, diagnosis, or lifecycle result. Ordinary implementation discretion remains agent-owned while it stays inside accepted behavior, architecture, authority, safety, compatibility, ownership/lifecycle, and material risk/cost boundaries. Otherwise surface the decision gap instead of selecting a plausible default from model priors.

When consequential stack-native behavior, ownership/lifecycle, compatibility, proportionality, or version-specific evidence is genuinely non-obvious, read [expert implementation counsel](references/expert-implementation-counsel.md). For multi-candidate, blocked/handoff-prone, migration/security/recovery-sensitive, or externally destructive work, read [job report](references/job-report.md). Do not create parallel reporting when an active plan already owns that continuity.

Repository/Git state never grants commit, history-rewrite, publication, provider-write, or destructive authority.

## 2. Deliver and prove

Prepare the workspace without disturbing unrelated changes. Continue until the requested outcome is proved, a material decision/authority gap blocks safe progress, or no safe independent work remains.

### Minimum sufficient mechanism

Understand the affected flow and real owners, then take the first sound option:

1. eliminate unnecessary mechanism or causal state;
2. reuse an existing project capability;
3. use native language/framework/platform capability;
4. use an already-selected dependency/tool;
5. derive duplicated state or localize policy at its real owner; then
6. add the minimum new mechanism still required.

Do not add indirection for hypothetical variation. A new abstraction needs a current second consumer/variant or an independently real production boundary such as external protocol, trust, persistence, volatile platform integration, or owned lifecycle/policy. Do not create production architecture solely for test convenience.

For a defect, correct the narrowest confirmed causal owner that covers affected paths. Treat an unplanned dependency/service/infrastructure component, public API/schema/storage/wire/compatibility change, material new abstraction, unrelated subsystem cleanup, parallel implementation, new test infrastructure, or destructive effect as scope expansion. If the accepted outcome genuinely needs it, surface the reason and required authority rather than silently enlarging the job.

### Proof policy

Proof is required; a new test is not. Use the smallest evidence that can independently falsify the changed contract: existing affected tests, compiler/type guarantees, static analysis, builds/schema checks, focused runtime probes, integration checks, bug reproduction, browser/manual verification, or another stronger current proof surface.

Apply [TDD](references/tdd.md) only when its admission gate is met. Glue, wiring, declarative configuration, trivial delegation, framework-native behavior, or similarly low-information changes do not earn a new test by ceremony.

Run focused proof while changing the relevant behavior, then job-level integration/acceptance proof. Use real-browser journey evidence only when literal user journeys changed and browser-dependent acceptance remains materially unproved by cheaper evidence.

For a planned stateful refactor/rewrite that can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior, require a current independent parity/contract result before relying on the rewrite plan.

## Exact candidate boundary

Before independent review, pin the exact candidate with the strongest native content identity available: commit, tree, snapshot, digest, or equivalent. Ambient unrelated changes must not enter the candidate. If the candidate/base changes, or unresolved conflict state makes the content ambiguous, refresh the identity before relying on review evidence. Leave ordinary Git mechanics to native Git capability.

Before review, include required ordinary documentation and durable knowledge that belongs to the delivered contract.

### Pre-review convergence

Remove issues you already know an independent reviewer should not need to discover: scope drift, wrong causal owner, unnecessary files/abstractions/dependencies/state/compatibility paths, temporary scaffolding, low-value durable tests, and proof that cannot distinguish plausible wrong behavior. This is a delivery self-check, not a retrospective or substitute for independent review.

## 3. Review and converge

Review each stable, understandable candidate once at the smallest coherent boundary. Source code/tests require independent code review after implementation proof is sufficient; other candidates use their native review/proof boundary.

A review finding is a hypothesis, not automatic mutation authority. Before correcting it:

- verify the failure/contract consequence;
- confirm it is inside accepted scope and local non-goals;
- prefer removing causal state/duplication over adding special-case machinery;
- prefer an existing mechanism at the real owner; and
- surface any genuine scope expansion instead of auto-building it.

Apply corrections through the proof mechanism appropriate to the changed invariant, refresh the exact candidate, and rerun only evidence invalidated by the correction. Do not close with a blocking finding or material evidence gap.

Before closing, every touched file, new abstraction, dependency, compatibility path, and durable test should have a concise requested-contract or necessary-proof reason to exist. Passing tests and smaller line counts are evidence, not permission for unnecessary structure.

When a deliberate simplification has a known ceiling, record the ceiling and observable revisit trigger at its natural owner rather than creating a parallel debt ledger.

## 4. Report

Return the job boundary, local exclusions, final change shape, delivered result, proof/review state, exact candidate identity, material scope decisions, blockers/residual limits, and next safe action. Publication remains a separate authority/outcome.

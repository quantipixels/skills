---
name: alaga
description: Deliver one supplied build job from settled outcome through implementation, proof, review, and handoff. Use for a bounded test-first feature/fix or any build/migration requiring an exact reviewed candidate. Exclude pure explanation, bare review, monitoring, and provider publication except where they support delivery.
---

# Alága

Deliver one supplied job as a coherent proved result. Use `test-first` only when the user requests it or a material behavior-bearing seam with an independent oracle makes a failing test capable of controlling implementation; otherwise use `job`. A job is the complete requested outcome; delivery units are only useful existing slices inside it.

## 1. Map the job

Pin:

- outcome and current/desired behavior;
- scope and **local non-goals / task exclusions** that constrain implementation direction for this job without becoming repository-level `.nongoals`;
- expected change envelope: likely owners/subsystems/surfaces plus explicitly unchanged contracts;
- acceptance and the smallest sufficient proof;
- governing specification identity and material behavior references when present;
- documentation and durable-knowledge reconciliation obligations and destinations;
- workspace and authority; and
- the minimum real user/operational path that must pass.

Treat local non-goals as active negative implementation boundaries, not descriptive footnotes. A proposal that violates one is out of scope unless the owning task/plan/spec changes it. Root `.nongoals` remains the separate durable project-wide exclusion contract owned by `amose`.

The change envelope is an evidence-backed expectation, not a prohibition on necessary discovery. Material growth is a signal to re-check understanding, causal ownership, and scope rather than preserve the first plan with workaround layers.

### Ownership and supporting results

Respect explicit owner/tool choices and use the shortest combination of current specialists and direct work. Supporting owners retain their native procedures/results; Alága owns integration and job acceptance. Read relevant root `.learnings` and complete `.nongoals` when present.

Do not resolve an independent decision, architecture, specification, diagnosis, or initiative-lifecycle outcome inside delivery. Consume its established owner result only when delivery actually depends on it. Use `scope-guard` only when the user explicitly wants its portable anti-overengineering result, and `root-cause` when causal diagnosis itself remains the missing outcome rather than a settled implementation premise.

Ordinary implementation discretion remains agent-owned only while the choice stays inside accepted behavior, architecture, authority, safety, compatibility, ownership/lifecycle, and material risk/cost boundaries. When a choice can materially change one of those and current evidence/contract does not determine it, surface a decision gap instead of selecting a plausible default from model priors.

When consequential implementation choices need deeper scrutiny of stack-native behavior, ownership/lifecycle, compatibility, proportionality, or version-specific evidence, read [expert implementation counsel](references/expert-implementation-counsel.md). This is a selectively loaded Alága path, not another owner. Skip it for obvious mechanical edits whose sound shape is already determined by current project evidence.

Read [job report](references/job-report.md) when the job is multi-candidate, blocked/handoff-prone, migration/security/recovery sensitive, externally destructive, or otherwise meets that reference's report gate. Reuse an active Atọ́nà plan instead of creating a parallel job report.

### Session policy

Derive session policy only where it changes execution:

- horizon;
- authorized commit granularity;
- continuation boundary; and
- extra research/evidence needs.

Repository/Git state never grants commit, history-rewrite, publication, provider-write, or destructive authority.

## 2. Deliver and prove

Prepare the workspace without disturbing unrelated changes. Continue through the confirmed horizon until completion, a material decision/authority gap, or no safe independent work remains.

When the expert-counsel path is active, keep it candidate-pinned and use it while consequential choices are being made. Refresh only when the candidate, touched mechanism, stack/version, accepted contract, material premise, or controlling evidence changes. The counsel remains part of delivery judgment; it does not replace proof or independent final review.

### Minimum sufficient mechanism

Understand the real affected flow and callers before minimizing. Then take the first sound option:

1. eliminate an unnecessary mechanism or causal state/branch;
2. reuse an existing project owner/module/helper/pattern;
3. use stdlib/framework/platform/language/database native capability;
4. use an already-selected dependency/tool;
5. derive duplicated state or localize policy/state at its real owner; then
6. add the minimum mechanism still required.

Do not add indirection for hypothetical variation. A new interface, adapter, factory, generic/configuration layer, or similar abstraction needs either a current second consumer/variant or an independently real production boundary such as an external protocol, trust boundary, persistence boundary, volatile platform integration, or owned lifecycle/policy boundary. Do not create production architecture solely to make testing convenient.

For a defect, correct the narrowest confirmed causal owner that covers the affected paths. Do not optimize for the smallest textual patch when it leaves sibling paths broken.

Treat an unplanned new dependency/service/infrastructure component, public API/schema/storage/wire/compatibility change, material design-shape abstraction, unrelated subsystem cleanup, parallel implementation, new test infrastructure, or destructive effect as a scope-expansion event. If the accepted outcome cannot be achieved without it, surface the reason and required decision/authority instead of silently enlarging the job.

### Proof policy

Proof is required; a new test is not. Use the smallest evidence that can independently falsify the changed contract: existing affected tests, compiler/type guarantees, static analysis, builds/schema checks, focused runtime probes, real integration checks, bug reproduction, browser/manual verification, or another stronger current proof surface. When existing proof tooling already exposes coverage, mutation, or equivalent evidence, use it to identify changed behavior that is not adequately constrained rather than pursuing the metric itself.

Apply [TDD](references/tdd.md) only when test-first is requested or a material behavior-bearing seam has an independent oracle and a failing test can materially control implementation. Glue, wiring, declarative configuration, trivial delegation, framework-native behavior, or similarly low-information changes do not earn a new test merely because production behavior changed. Never manufacture an abstraction or test harness just to satisfy a test-first ceremony.

Run focused/affected proof per unit, then job-level integration/acceptance proof.

When delivery changes literal user journeys and material browser-dependent acceptance claims remain that narrower proof cannot establish, use `dogfood` for the smallest complete affected journey set. Do not use Dogfood for document-shaped HTML, routine visual smoke, or a whole-product audit.

Before a planned stateful refactor/rewrite can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior, require exact-current Àtúnwò `audit` and consume its contract/guardrails as implementation input.

If one unit blocks, record the blocker/resume trigger, continue independent in-scope work, and delegate bounded independent/noisy support only when it improves progress/evidence or protects the primary delivery context.

## Exact candidate identity

Every review candidate must identify exactly what is being reviewed without disturbing unrelated work.

- **Committed work:** pin the exact commit/tree.
- **Selected uncommitted work:** produce a Git-native content-addressed tree for only the intended paths while leaving the real index and refs untouched. Pin the base `HEAD` once and use that same SHA as the tree's base and reported identity. Reject selected paths with unresolved index stages rather than treating conflict content as an ordinary candidate.
- **Whole worktree:** use only when the whole worktree is intentionally the candidate.

Record the pinned base SHA, candidate tree SHA, exact selected paths, and ambient uncommitted paths. Ambient changes must not enter the candidate. If the pinned base or selected content changes during capture, recapture before review; when concurrent mutation is a material risk, require a stable repeated capture.

Before review, update required ordinary documentation in the candidate and use `amose` when verified delivery changes durable project knowledge. Consume applicable Atọ́nà reconciliation items without copying the lifecycle archive into delivery state.

### Pre-review convergence

Before handing the candidate to an independent reviewer, remove anything you already know the reviewer should not have to tell you about. Recheck local non-goals/change-envelope drift, the causal owner, unnecessary files/abstractions/dependencies/state/compatibility paths, temporary scaffolding, low-value durable tests, and whether proof can actually discriminate plausible wrong behavior. This is a self-check, not a postmortem or substitute for independent review.

When the expert-counsel path was active, perform its final exact-candidate comparison during this convergence. Resolve material unresolved counsel that can still change implementation/proof, or record the evidence-backed reason for a deliberate departure. Counsel status is delivery evidence, not review acceptance.

Good: remove an interface introduced only for mocking when no production boundary requires it.

Bad: run a retrospective, reconsider settled architecture, or manufacture edge cases before review.

## 3. Review and converge

1. Review each stable, understandable, verifiable, reversible candidate once. Keep dependent changes together when separation creates a broken intermediate result; split independent candidates.
2. After implementation proof is sufficient, source code/tests require broad `atunwo`. Other candidates use their native verification/review owner. Findings remain hypotheses until verified. Review may discover broadly; it does not silently enlarge the accepted delivery contract.
3. Before implementing a correction, confirm it is inside the accepted contract/blocking criteria and local non-goals. Before adding special-case machinery, ask whether removing the causal state, branch, or duplicate owner would make the edge case impossible; otherwise prefer an existing mechanism at the real owner and surface genuine scope expansion.
4. Apply behavior-changing corrections through TDD only when they meet the TDD admission gate; otherwise use the appropriate proof owner. Recapture the exact candidate and rerun only invalidated proof/review. Do not finish with a blocking finding or material evidence gap.
5. Before closing, justify every touched file, new abstraction, dependency, compatibility path, and durable test by the requested contract or necessary proof. Passing tests and smaller line counts are evidence, not permission for unnecessary structure.
6. Close a candidate only after acceptance, proof, documentation, and required review pass against the governing specification when present. Close the job only when every in-scope unit maps to the requested outcome and job-level integration/acceptance passes.

When a deliberate simplification has a known ceiling, record the simplification, ceiling, and observable revisit trigger at its natural owner: local comment for a local mechanism, ADR for architecture, issue for planned work, or `.learnings` for durable project knowledge. Do not create a parallel debt ledger merely for this convention.

## 4. Report

Return:

- job boundary, local non-goals/task exclusions, expected/final change envelope, and session policy;
- delivered units plus documentation and durable-knowledge reconciliation;
- proof/review state;
- commit state and exact candidate identities;
- scope-expansion decisions plus deliberate simplification ceilings/triggers when any;
- blockers and residual limits;
- remaining work; and
- next safe action.

Return generated artifact paths from their owning skill. Publication remains with `seda-pr`.

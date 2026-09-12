---
name: alaga
description: Deliver one accepted coding change or fix through implementation and proportionate proof. Use when the desired behavior and authority are sufficiently settled to change code; exclude planning, specification, bare review, monitoring, provider publication, and standalone scope documents from normal selection.
---

# Alága

Deliver the accepted coding outcome. Own implementation and proof.

A scope correction during authorized delivery updates the active boundary without revoking delivery authority unless the user pauses or narrows it. Do not turn ordinary local choices inside the accepted scope into approval gates.

Delegate substantial analysis, research, and expert work to subagents when it materially helps.

## 1. Bound the job

Pin only what can change delivery:

- desired/current behavior and accepted outcome;
- scope, local non-goals, and explicitly unchanged contracts;
- expected change envelope and expansion triggers;
- acceptance and smallest sufficient proof;
- governing specification/decision identities when present;
- ordinary documentation required by the delivered contract; and
- workspace and mutation authority.

Use project behavior and accepted decisions to define boundaries, not arbitrary file, line, test, or dependency quotas. Expose changes to accepted interfaces, storage, compatibility, permissions, operational burden, or material risk/cost as expansion. New dependencies/infrastructure, public schema or wire changes, broad abstractions, parallel implementations, unrelated cleanup, new test infrastructure, or destructive effects need a current reason tied to the accepted outcome and the authority their effects require.

When project knowledge could change implementation or proof, reuse applicable evidence already supplied; otherwise search existing project knowledge/research destinations by affected concepts/components, read plausible matches, and check authority/current applicability before applying a constraint or avoiding a past approach. Historical guidance is evidence, not automatic authority. Report material conflicts; an empty search does not require new documentation. Use `amose`, `architect`, `arojinle`, or `seda-spec` when their result is genuinely missing; do not replay settled work.

When consequential stack-native behavior, ownership/lifecycle, compatibility, proportionality, or version-specific behavior is non-obvious, read [expert implementation counsel](references/expert-implementation-counsel.md). For material product-interface work, read [UI delivery](references/ui-delivery.md). For multi-candidate, migration/security/recovery-sensitive, or handoff-prone delivery, read [job report](references/job-report.md).

Repository/Git state never grants commit, history-rewrite, publication, provider-write, or destructive authority.

## 2. Implement the minimum sufficient mechanism

Prepare the workspace without disturbing unrelated changes. Continue until the accepted outcome is proved, a material decision/authority gap blocks safe progress, or no safe independent work remains.

Understand the affected flow and real owners before editing. Prefer the first sound option:

1. eliminate unnecessary mechanism or causal state;
2. reuse an existing project capability;
3. use native language/framework/platform capability;
4. use an already-selected dependency/tool;
5. derive duplicated state or localize policy at its real owner; then
6. add the minimum new mechanism still required.

Minimum means the least necessary mechanism that stays idiomatic and readable, not the fewest lines/files. Do not add indirection for hypothetical variation. A new abstraction needs a current second consumer/variant or an independently real production boundary such as protocol, trust, persistence, volatile integration, or owned lifecycle/policy. Do not create production architecture solely for test convenience.

For a defect, correct the narrowest confirmed causal owner that covers the affected paths. Material growth outside the expected envelope is a reason to re-check the causal owner or scope rather than preserve the first implementation with workaround layers.

### Shared-state mutations

When a mutation is authorized by mutable shared state—existence, uniqueness, balance/capacity, ownership, quota/count, expected version, or another predicate another actor can change—identify the invariant and its authoritative enforcement before writing the change. A read → decide → write sequence must not be the sole authority when another actor can invalidate the read.

Treat concurrency correctness as an invariant question, not a traffic threshold. Existing constraints, conditional mutation, version checks, serialized ownership, locking, or isolation count only when they protect the same invariant across all relevant writers. Use expert implementation counsel when exact database/runtime semantics can change the mechanism.

## 3. Prove the changed contract

Proof is required; a new test is not. Use the smallest evidence that can independently falsify the changed behavior: existing affected tests, compiler/type guarantees, static analysis, builds/schema checks, focused runtime probes, integration checks, bug reproduction, browser/manual verification, or another stronger current proof surface.

Apply [TDD](references/tdd.md) only when its admission gate is met. Glue, wiring, declarative configuration, trivial delegation, or framework-native behavior do not earn a test by ceremony. Wiring that binds identity, authority, or resource limits needs proof through the assembled path; constructor tests alone may miss incorrect combinations.

Run focused proof while changing behavior, then job-level integration/acceptance proof. Use real-browser journey evidence only when literal user journeys changed and browser-dependent acceptance remains materially unproved by cheaper evidence. For a stateful refactor/rewrite that can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior, require a current independent parity/contract result before relying on the rewrite plan.

Before independent review, include required ordinary documentation and pin the exact candidate with the strongest native content identity available: commit, tree, snapshot, digest, or equivalent. For a PR/MR candidate, the current base is part of that identity; when the candidate is one stack layer, pin at least the head SHA plus current base-ref SHA. A stable head with a changed base-ref SHA is a changed review candidate. If an ancestor changes the effective stacked base or conflict resolution changes the candidate content, refresh identity before relying on review evidence. Preserve proof that is independently unaffected by the base change; rerun only evidence whose falsification boundary moved. Ambient unrelated changes must not enter the candidate.

Remove issues an independent reviewer should not need to discover: known scope drift, wrong causal owner, unnecessary files/abstractions/dependencies/state/compatibility paths, temporary scaffolding, low-value durable tests, and proof that cannot distinguish plausible wrong behavior.

## 4. Integrate independent review when useful

Use `atunwo` when independent code judgment is explicitly required or materially valuable for the candidate's consequence, uncertainty, or residual risk. Alága does not review its own candidate by relabelling the same reasoning as review.

Treat each review finding as a hypothesis. Before correcting it:

- verify the failure or contract consequence;
- confirm it is inside accepted scope and non-goals;
- prefer removing causal state/duplication over adding special-case machinery;
- prefer an existing mechanism at the real owner; and
- surface genuine scope expansion instead of auto-building it.

Apply justified corrections through the proof mechanism appropriate to the changed invariant, refresh candidate identity, and rerun only invalidated evidence. Do not claim a reviewed/accepted state while a blocking confirmed finding or material review evidence gap remains.

Every touched file, new abstraction, dependency, compatibility path, and durable test should have a concise accepted-contract or necessary-proof reason to exist. Passing tests and smaller line counts are evidence, not permission for unnecessary structure. When a deliberate simplification has a known ceiling, keep the ceiling and observable revisit trigger at its natural owner rather than creating a parallel debt ledger.

## Compatibility: explicit `scope-only`

For this minor release, an existing direct invocation that explicitly requests Alága `scope-only` remains supported. Return the desired result, protected behavior/areas, exclusions, sufficient evidence, and the event that requires reconsidering scope, then stop before editing, proof execution, commit, or publication.

Do not select this compatibility path for an ordinary request to plan, specify, or decide scope; route those unresolved outcomes to their natural owner. A future major version may retire the explicit compatibility mode after usage evidence supports doing so.

## 5. Return the delivery result

Return the accepted job boundary, final change shape, delivered behavior, proof and independent-review state when applicable, exact candidate identity, material scope decisions, blockers/residual limits, and next safe action.

Publication remains a separate outcome handled by `seda-pr` when requested.

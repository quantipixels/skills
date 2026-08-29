---
name: alaga
description: Deliver one supplied build job from settled outcome through implementation, proof, review, and handoff. Use for a bounded test-first feature/fix or any build/migration requiring an exact reviewed candidate. Exclude pure explanation, bare review, monitoring, and provider publication except where they support delivery.
---

# Alága

Deliver one supplied job as a coherent proved result. Use `test-first` for a bounded behavior change that warrants TDD; otherwise use `job`. A job is the complete requested outcome; delivery units are only useful existing slices inside it.

## 1. Map the job

Pin outcome, current/desired behavior, scope, exclusions, acceptance, proof, documentation destinations, workspace, and authority. Name the minimum real user/operational path that must pass.

Respect explicit owner/tool choices. Use the shortest combination of current specialists and direct work. Supporting owners retain their native procedures/results; Alága owns integration and job acceptance.

Derive session policy only where it changes execution: horizon, authorized commit granularity, continuation boundary, and extra research/evidence needs. Repository/Git state never grants commit, history-rewrite, publication, provider-write, or destructive authority.

Read relevant root `.learnings` and complete `.nongoals` when present. Use `arojinle` for unresolved material user choices, `solution-architect` for material technical architecture, `atona` when an initiative plan must remain live, and `seda-ticket` only when supplied work benefits from consumable vertical tickets.

Read [job report](references/job-report.md) when the job is multi-candidate, blocked/handoff-prone, migration/security/recovery sensitive, externally destructive, or otherwise meets that reference's report gate. Reuse an active Atọ́nà plan instead of creating a parallel job report.

## 2. Deliver and prove

Prepare the workspace without disturbing unrelated changes. Continue through the confirmed horizon until completion, a material decision/authority gap, or no safe independent work remains.

Use the proof owner for each unit. When production behavior changes or test-first work is requested, apply [TDD](references/tdd.md) in coherent green slices. Run focused/affected proof per unit, then job-level integration/acceptance proof.

Before a planned stateful refactor/rewrite can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior, require exact-current Àtúnwò `audit` and consume its contract/guardrails as implementation input.

If one unit blocks, continue independent in-scope work and record the blocker, affected dependencies, proof, and exact resume trigger. Delegate bounded independent support when it materially improves progress or evidence.

## Exact candidate identity

Every review candidate must identify exactly what is being reviewed without disturbing unrelated work.

For committed work, pin the exact commit/tree. For selected uncommitted work, produce a Git-native content-addressed tree for only the intended paths while leaving the real index and refs untouched. Pin the base `HEAD` once and use that same SHA as the tree's base and reported identity. Reject selected paths with unresolved index stages rather than treating conflict content as an ordinary candidate.

Record the pinned base SHA, candidate tree SHA, exact selected paths, and ambient uncommitted paths. Ambient changes must not enter the candidate. If the pinned base or selected content changes during capture, recapture before review; when concurrent mutation is a material risk, require a stable repeated capture. Temporary capture state must not affect subsequent repository operations.

Use the whole worktree only when the whole worktree is intentionally the candidate.

Before review, update required ordinary documentation in the candidate and use `amose` when verified delivery changes durable project knowledge.

## 3. Review and converge

Review each stable, understandable, verifiable, reversible candidate once. Keep dependent changes together when separation creates a broken intermediate result; split independent candidates.

After implementation proof is green, source code/tests require broad `atunwo`. Other candidates use their native verification/review owner. Findings remain hypotheses until verified.

Apply behavior-changing corrections through TDD/proof owner, recapture the exact candidate, rerun invalidated proof/review, and do not finish with a blocking finding or material evidence gap.

Close a candidate only after acceptance, proof, documentation, and required review pass. Close the job only when every in-scope unit maps to the requested outcome and job-level integration/acceptance passes.

## 4. Report

Return job boundary/session policy, delivered units, documentation, proof/review, commit state, exact candidate identities, blockers/residual limits, remaining work, and next safe action. Return generated artifact paths from their owning skill. Publication remains with `seda-pr`.

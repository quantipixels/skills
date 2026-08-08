---
name: alaga
description: Deliver one self-contained production-feature candidate from settled scope through test-backed implementation and broad review. Use when code must change and an exact reviewed candidate is required; exclude PR or MR creation and provider lifecycle work.
---

# Alaga

## Functional workflow

```text
Feature request + repository state
               │
               ▼
     Scope + authority ready
               │
               ▼
       TDD behavior proof
               │
               ▼
    Stable review candidate
               │
               ▼
        Simplify review
               │
               ▼
         QP code review
          ├── Findings ──> Correct through TDD ──> Repeat proof and review
          └── Exact candidate ready ──> Report
```

The workflow describes one feature-delivery sequence. It does not create a host execution framework or require provider publication.

## 1. Settle scope and authority

Establish:

- the feature boundary, acceptance behavior, exclusions, and proof expectations;
- the documentation impact and each required destination, or `not applicable` with evidence;
- whether a dedicated worktree or branch is needed;
- whether local commits are authorized.

Ask only when the request and current repository state do not settle a material choice.

When a feature contains a substantial independently verifiable task, Alaga may request its bounded result through host-provided subagent work. Give the request the current candidate identity, task scope and exclusions, relevant confirmed decisions and evidence, required result or proof, and acceptance criteria as starting context, not proof. Apply an owning specialist's rules when the task requires that specialist outcome. Accept the task result only when its identity and evidence satisfy the current stage gate. Alaga retains candidate integration, stage-gate verification, and correction convergence.

Reuse a current confirmed clarification when it covers the feature. Use `arojinle` only when material user decisions remain. Use `atona` when architecture decisions must remain active during delivery.

When a standalone feature specification or plan controls material implementation and no architecture plan owns it, verify its acceptance behavior, interactions, recovery, and proof against current evidence. Use `arojinle` for newly exposed user decisions and record required artifact corrections for its owner.

## 2. Implement and prove

Prepare the selected workspace and branch without disturbing unrelated changes.

Run `tdd` through coherent green behavior slices. Commit a slice only when local commits are authorized. Otherwise, preserve the verified changes without committing them.

Use focused and affected proof for each slice. Treat a local commit as a meaningful green history, bisect, or rollback point, not as a trigger for broad review.

Before the candidate becomes stable for review, reconcile each required documentation destination in the same candidate as its implementation change. Record the destination and one status: `updated now`, `already correct` with evidence, or `not applicable` with evidence. Keep the record compact. Do not defer required documentation as untracked follow-up work.

## 3. Review and converge

Run broad review once for each stable, self-contained candidate that can be understood, validated, accepted, and rolled back as one change. A candidate may contain one or more coherent behavior slices and local commits. Do not use every slice, commit, or delivery phase as an automatic broad-review boundary. Split a phase when it contains independent reviewable changes; keep dependent slices together when separation would hide the behavior or leave an unusable intermediate state.

Request an earlier bounded review only when a material design, security, data-integrity, migration, public-contract, or cross-system risk would be costly to correct later. Record its limited question and candidate. It does not replace broad review of the final exact candidate.

Classify each confirmed review correction as behavior-changing or behavior-preserving. Apply behavior-changing corrections through `tdd`. Apply behavior-preserving corrections while affected proof is green; do not create a failing test when required behavior does not change. After either correction, rerun affected proof and each completed review stage against the updated candidate.

Run the read-only `simplify` review after implementation proof is green. Record its exact candidate identity, findings or clean claim, and limitations. Treat each finding as a hypothesis and verify it against the current candidate.

Supply the exact-current `simplify` result and its material `Needs qp-code-review` concerns to `qp-code-review`. Treat it as the broad review's maintainability evidence; do not repeat it for the same candidate.

Run `qp-code-review` in broad scope. Treat its findings as hypotheses and verify each failure mechanism against the current candidate.

Correct each confirmed `NON_BLOCKING` maintainability finding when the correction remains within settled feature scope and its delivery risk and cost do not exceed the evidenced maintenance benefit. Otherwise, record the finding, the reason it remains, and the residual limitation.

Do not complete delivery while a confirmed blocking finding or evidence gap remains.

## 4. Report the candidate

Confirm that the selected workspace contains the reviewed candidate and that no intended change remains outside the authorized Git state.

Report the feature boundary, decisions, implementation, documentation-destination record, proof, review results, commit state, exact final candidate, and residual limitations.

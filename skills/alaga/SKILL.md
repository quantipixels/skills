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

Keep feature-local exclusions with the candidate and state the current behavior, desired behavior, independently verifiable acceptance criteria, and explicit out-of-scope work.

Read relevant parts of root `.learnings` and the complete root `.nongoals` when present. Preserve confirmed project knowledge. If the feature conflicts with `.nongoals`, require Amọ̀ṣẹ́ to record an explicit one-time exception or authorized boundary update before implementation.

When a feature contains a substantial independently verifiable task, Alaga may request its bounded result through host-provided subagent work. Give the request the current candidate identity, task scope and exclusions, relevant confirmed decisions and evidence, required result or proof, and acceptance criteria as starting context, not proof. Apply an owning specialist's rules when the task requires that specialist outcome. Accept the task result only when its identity and evidence satisfy the current stage gate. Alaga retains candidate integration, stage-gate verification, and correction convergence.

Reuse a current confirmed clarification when it covers the feature. Use `arojinle` only when material user decisions remain. Use `atona` when architecture decisions must remain active during delivery.

When a standalone feature specification or plan controls material implementation and no architecture plan owns it, verify its acceptance behavior, interactions, recovery, and proof against current evidence. Use `arojinle` for newly exposed user decisions and record required artifact corrections for its owner.

## 2. Implement and prove

Prepare the selected workspace and branch without disturbing unrelated changes.

When delivery starts from a persisted ticket, pin its identity, current state, dependencies, transition authority, and persistence owner. Start only from `Ready` after every dependency is `Done`. With authority for the exact ticket and transition, move it to `In Progress`; otherwise return the requested transition and evidence without changing ticket state.

During delivery, use the ticket lifecycle supplied by its owner. Move `In Progress → Blocked` with a reason, unblock owner or trigger, and `resume_to: In Progress`; move `In Review → Blocked` with the same fields plus the exact candidate and proof summary and `resume_to: In Review`. Resume only to the recorded state. Move a stable proved candidate `In Progress → In Review` with its exact identity and proof summary. A review correction moves `In Review → In Progress`. Move `In Review → Done` only after its acceptance and proof succeed. Cancellation requires separate explicit authority and a reason. Never reopen `Done` or `Cancelled`. On every transition, replace state evidence with only the fields required by the new state.

Immediately before an authorized ticket write, refresh its identity, current state, dependency states, evidence, and permitted transitions. Reject a stale, replayed, invalid, unauthorized, or terminal transition without mutation. If Alaga does not own persistence, return the requested transition and evidence to its owner. Ticket state does not override plan, phase, implementation, or review state.

Use an Irinṣẹ result when bounded companion-tool evidence materially improves impact orientation or directs source reading. Keep candidate integration, implementation, and proof in Alaga; do not treat the tool result as acceptance evidence by itself.

Run `tdd` through coherent green behavior slices. Commit a slice only when local commits are authorized. Otherwise, preserve the verified changes without committing them.

Use focused and affected proof for each slice. Treat a local commit as a meaningful green history, bisect, or rollback point, not as a trigger for broad review.

Before the candidate becomes stable for review, update each required ordinary-documentation destination in the same candidate as its implementation change. Keep code-local comments with the implementation owner. When verified implementation exposes a durable non-obvious rule, pattern, constraint, term, or conflict, send one exact evidence package for the candidate to Amọ̀ṣẹ́; do not repeat it unless its identity or evidence changes, and do not redefine the model locally. Reconcile any required `.learnings`, `.nongoals`, or ADR result before review. Do not defer required documentation as untracked follow-up work.

## 3. Review and converge

Run broad review once per stable candidate that is understandable, verifiable, acceptable, and reversible as one change.

- **Good:** keep dependent slices and local commits together when separation would hide behavior or create an unusable intermediate state; split independent reviewable changes.
- **Bad:** use every slice, commit, or whole delivery phase as an automatic review boundary.

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

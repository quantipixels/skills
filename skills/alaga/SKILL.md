---
name: alaga
description: Deliver one supplied build job from settled outcome through proved delivery and applicable review. Use when an artifact or working result must be created, changed, assembled, or migrated and an exact reviewed candidate is required; the job can contain one or many delivery units. Exclude pure explanation, bare review, monitoring, publication, and provider lifecycle work unless they support the build.
---

# Alaga

Deliver one supplied job as a coherent, proved, reviewed result. Own the build job and its integration without taking over the native outcomes or lifecycle of supporting specialists.

## Functional workflow

```text
Supplied job + repository state
              │
              ▼
   Scope + authority + horizon
              │
              ▼
 Job envelope + useful capabilities
              │
              ▼
   Deliver and prove each unit
              │
              ▼
 Stable candidate or candidate set
              │
              ▼
       Required candidate review
              │
      Findings ──> Correct ──┐
              │              │
              └──────────────┘
              ▼
 Job acceptance + exact handoff
```

A **job** is the complete build outcome supplied to Alaga. A **delivery unit** is an existing feature, plan, phase, ticket, task, review candidate, or other bounded result that contributes to the job. One job can contain one or many units and candidates. This workflow is not a complete engineering-lifecycle framework and does not authorize provider publication.

## 1. Accept and map the job

Establish the requested outcome, current and desired behavior, scope, exclusions, independently verifiable acceptance, proof expectations, documentation destinations, workspace, and authority. A plan can be the delivered artifact. Pure explanation, bare review, monitoring, PR or MR publication, and provider lifecycle work remain with their direct owners unless they are supporting units in the build.

`alarina` selects the first route for an unqualified prompt. Once `alaga` is explicitly selected or routed, Alaga owns the active build job. Inspect the current capability inventory and select the shortest useful combination of skills, tools, and direct work from job evidence. Examples are not an allowlist. If a required owner is unavailable, name the capability gap and pause only dependent work; do not imitate the missing specialist.

Before delivery starts, establish one session delivery policy from the user request and repository state:

- execution horizon: one unit, candidate, ticket, phase, all startable work, or the complete job;
- commit granularity when local commits are authorized;
- continuation boundary: continue automatically through the confirmed horizon, or pause after one stated existing unit; and
- any research or evidence requirement beyond the owning proof gates.

Reuse choices already settled by the request, an exact-current plan or ticket, and repository instructions. Ask one focused question only when a remaining material choice or missing authority changes the safe path. Repository history and Git state do not grant user, commit, history-rewrite, publication, or provider-write authority.

Create one job envelope that maps the job to its delivery units, owners, dependencies, exact-current native state, acceptance, proof, blockers, results, and candidate identities. Each specialist retains its own lifecycle and state. For every specialist request, pin caller, owner, scope, required result, candidate, and the active owner-and-scope ancestry. Each callee extends that ancestry for nested requests. When it needs a result owned by an ancestor for the same or overlapping scope, return that need to the active ancestor instead of invoking it. Return a named cycle gap only when control cannot safely return or the owner scopes conflict.

Read relevant root `.learnings` and the complete root `.nongoals` when present. Preserve confirmed project knowledge. If the job conflicts with `.nongoals`, require Amọ̀ṣẹ́ to record an authorized exception or boundary update before dependent implementation.

Read [living-report.md](references/living-report.md) when evaluating the independent-report threshold at job acceptance. If the job qualifies, use `html-artifact` to create the report. Re-evaluate after decomposition and every material shift; create the report at the first trigger.

Use `arojinle` when a material user decision remains. Use `atona` when architecture, migration, integration, phase, or recovery decisions must remain active during delivery. Use `seda-ticket` when the supplied work needs consumable vertical tickets. These specialists return exact-current results; Alaga does not copy their procedures or state machines.

## 2. Deliver and prove

Prepare the selected workspace and branch without disturbing unrelated changes. Work through the confirmed horizon without stopping after every unit. Stop only when the policy requires it, a material decision or authority gap appears, or no safe independent work remains.

Start a persisted ticket only when its exact-current state is `Ready` and every dependency is `Done`. Use the lifecycle supplied by its owner. Refresh identity, state, dependencies, evidence, and permitted transition immediately before a write. If Alaga does not own persistence, return the requested transition and evidence to the owner. Ticket state never sets job, plan, phase, implementation, or review state.

Use the proof owner appropriate to each unit. Run `tdd` through coherent green slices when production behavior changes. Use focused and affected proof for every unit, then run job-level integration and acceptance proof. A local commit is an optional green-history, rollback, or review boundary only when explicitly authorized; it is not an automatic unit or review trigger.

When one unit blocks, continue independent in-scope units within the confirmed horizon. Record the blocker, affected dependencies, completed units, partial proof, and exact resume trigger. Do not continue dependent or unsafe work.

When host-provided subagent work materially improves delivery, give each bounded request the current candidate identity, scope and exclusions, confirmed decisions, required result, and acceptance. Alaga retains integration, stage-gate verification, and correction convergence. Use an exact-current Irinṣẹ result only when bounded companion-tool evidence materially improves impact orientation or source selection; it is not acceptance evidence by itself.

Identify every review candidate exactly. For an uncommitted candidate, record base `HEAD` and partition the ordered path status into intended candidate paths and ambient unrelated paths. For every path, record applicable index entries, file type and mode, SHA-256 for present content, and explicit deletions. Preserve ambient user changes and stop for ownership clarification when an overlap prevents safe isolation. Do not require a clean index. A commit policy does not authorize amend, squash, rebase, force-push, or another history rewrite.

Before review, update every required ordinary-documentation destination in the same candidate. Send one exact evidence package to Amọ̀ṣẹ́ when verified delivery changes durable project knowledge. Reconcile required `.learnings`, `.nongoals`, or ADR results before review; do not leave required documentation as an untracked follow-up.

## 3. Review and converge

Review each stable candidate once when it is understandable, verifiable, acceptable, and reversible as one change. Keep dependent units together when separation creates a broken or misleading intermediate result; split independent reviewable candidates. Do not make every task, TDD slice, or commit a review boundary.

Request an early bounded review only for material design, security, data-integrity, migration, public-contract, or cross-system risk that would be costly to correct later. It does not replace the final review required for that candidate type.

Select review owners from the candidate type and job contract. For source code or tests, run `simplify` after implementation proof is green. Pin its exact candidate, findings or clean claim, and limitations. Supply that exact-current result and every material `Needs qp-code-review` concern to broad `qp-code-review`. For an agent-skill candidate, require exact-current `ko-skill` verification and any independent review that its contract selects; do not substitute code review unless its published scope includes the candidate. For a plan, report, research record, ordinary document, provider-owned result, or another non-code artifact, require the owning specialist's verification and every review named by its contract; do not send it to code review only because Alaga owns the job. Treat findings as hypotheses until verified.

Apply behavior-changing code corrections through `tdd`. Apply other corrections through their owning proof workflow. After any correction, pin the new candidate and rerun affected proof and each stale review stage. Resolve each confirmed non-blocking maintainability finding when the correction stays in scope and its delivery risk does not exceed the evidenced benefit. Do not complete the job while a blocking finding or evidence gap remains.

Close a candidate only after its acceptance, proof, documentation, and required review pass. Close the job only after all in-scope units and candidates map to the requested outcome and job-level integration and acceptance proof pass.

## 4. Report the result

Keep a qualifying living report current under [living-report.md](references/living-report.md). At handoff, confirm that the selected workspace contains the exact reviewed candidate and no intended change remains outside the authorized Git state.

Report the job boundary, session policy, completed horizon, decisions, delivered units, documentation disposition, proof, review results, ticket transitions, commit state, exact candidate or candidate set, remaining units, blockers, and residual limitations. Return the full absolute path for every plan, report, or other local artifact used with the user.

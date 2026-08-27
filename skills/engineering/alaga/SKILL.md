---
name: alaga
description: Deliver one supplied build job from settled outcome through implementation, proof, review, and handoff. Use for a bounded test-first feature or fix, or any artifact, change, or migration that needs an exact reviewed candidate. A job may contain one or many delivery units. Exclude pure explanation, bare review, monitoring, publication, and provider lifecycle unless they support the build.
---

# Alága

Deliver one supplied job as a coherent, proved, reviewed result. Use `test-first` for a bounded feature/fix or explicit test-first request; otherwise use `job`. A job is the complete supplied outcome; a delivery unit is an existing feature/plan/phase/ticket/task/candidate or other bounded result inside it. Own job integration without taking over supporting specialists or provider publication.

## 1. Accept and map the job

Establish requested outcome, current/desired behavior, scope, exclusions, acceptance, documentation destinations, workspace, and authority. Name the minimum real user/operational path that must pass for acceptance.

`alarina` selects the first route for an unqualified prompt. Once selected, Alága owns the active build job. Choose the shortest useful combination of available specialists/tools/direct work. If a required owner is unavailable, name the gap and pause only dependent work; do not imitate that specialist.

Before delivery, derive one session policy. Name the **smallest proof that can falsify the highest-risk acceptance claim** and a provisional proof budget: material invariants and their expected primary proof owners. The budget is a planning signal, not a numerical quota. Stop expanding proof/delegation when more evidence cannot change acceptance or a blocking decision.

Pin execution horizon, authorized commit granularity, continuation boundary, and any research/proof requirement beyond owning gates. Reuse settled exact-current plan/ticket/architecture decisions. Ask only when a material choice/authority gap changes the safe path.

Create one job envelope mapping units to owners, dependencies, native state, acceptance, proof, blockers, results, and exact candidate identities. Read applicable `.learnings` and complete `.nongoals`; conflicting direction requires an authorized `amose` reconciliation/exception before dependent implementation.

Read [job-report.md](references/job-report.md) at acceptance and after decomposition or a material shift. When an active Atọ́nà plan governs the job, return its contribution receipt instead of creating a parallel user-facing report. A material receipt may cause Atọ́nà to revise its semantic plan and refresh the continuous plan HTML; Alága does not edit that plan record or HTML directly. Otherwise, use `html-artifact` at the first qualifying standalone-report trigger and `akosile` for any repository-local QP-generated destination.

Use `solution-architect` for material architecture, `arojinle` for an open consequential user decision, `atona` for active initiative lifecycle, and `seda-ticket` only when consumable tickets are needed. Consume exact-current results without copying their procedures.

When the user has explicitly selected Experimental `akowe-code` and an exact-current Code Craft Brief is available, consume it as implementation guidance. Stable delivery remains complete without it; the brief cannot grant architecture, mutation, proof, or review authority.

For accepted `pare` work, pin the exact report/candidate/selected slice/retained contracts/proof/risk/blockers/future verification. A `deep-clean candidate` requires explicit opt-in.

## 2. Deliver and prove

Prepare workspace/branch without disturbing unrelated changes. Continue through the confirmed horizon until policy requires a pause, a material decision/authority gap appears, or no safe independent work remains.

Start a persisted ticket only when its exact-current owner result permits it. Refresh its identity, state, dependencies, evidence, and authority before a write. Ticket state never sets job, plan, phase, implementation, or review state.

When production behavior changes or the user requests test-first work, apply [test-first implementation](references/tdd.md) through coherent green slices. Run focused/affected proof for each unit, then job-level integration/acceptance proof.

Before a planned stateful refactor/rewrite can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior, require exact-current `atunwo audit`; use its accepted rows as contract inputs and required characterization proof. Do not reuse the audit as final review.

If one unit blocks, continue independent in-scope units and record the blocker/dependencies/completed work/partial proof/resume trigger. Do not continue dependent or unsafe work.

When subagent work materially improves delivery, give each bounded request the current candidate, scope, exclusions, confirmed decisions, result contract, and acceptance. Alága retains integration, stage gates, and correction convergence. Use `irinse` only for exact-current companion-tool evidence that improves impact or source selection. It is not acceptance evidence.

Identify every review candidate exactly. For uncommitted work, run:

```text
python3 <alaga-skill>/scripts/snapshot-candidate.py --repo <workspace> --path <intended-path>
```

for every intended path. Use `--all-changes` only when the whole worktree is the candidate. Use the snapshot's selected/ambient partition and digest. Stop on an incomplete snapshot or unsafe overlap. Preserve ambient changes and do not require a clean index. Commit authority does not authorize amend, squash, rebase, force-push, or another history rewrite.

Before review, update required ordinary documentation in the candidate and reconcile durable project knowledge through `amose` when warranted.

When accepted visual references span multiple screens, components, states, or core tokens, map each surface to its implementation and visual-check state in a fidelity ledger. Record exclusions and unresolved mismatches. Skip the ledger for low-visual or single-surface work.

## 3. Compact proof before final review

When tests/probes/harnesses were added or materially changed, read [proof compaction](references/proof-compaction.md) after the candidate behavior is green and production refactoring is stable.

Classify development proof as:

```text
KEEP | MERGE | DELETE | MOVE_TO_STRONGER_OWNER
```

Do not equate TDD construction history with the permanent test portfolio. Preserve every material invariant, but prefer one primary proof owner at the cheapest stable seam. Re-run affected proof after compaction.

If no proof artifact changed, record compaction `not applicable` rather than manufacturing cleanup.

After proof compaction, make **one bounded craft pass** over the stable candidate: names, abstraction level, ownership, state representation, duplicated mechanism, and exact-current Code Craft Brief when one was explicitly supplied. Do not enter an iterative beautification loop. Any behavior-changing correction returns through its proof owner.

## 4. Review and converge

Review each stable, understandable, verifiable, acceptable, and reversible candidate once. Keep dependent units together when separation creates a broken intermediate result; split independent candidates. A task, TDD slice, or commit is not automatically a review boundary.

Request early review only for material design/security/data/migration/public-contract/cross-system risk where correction would be expensive later; it does not replace final review.

After implementation and compacted proof are green, source code/tests require broad `atunwo`, which consumes exact-current `pare review` evidence. Other artifacts use their owner-specific verification/review. Findings remain hypotheses until verified.

Apply behavior-changing corrections through TDD/owning proof and other corrections through their proof owner. Pin the new candidate and rerun affected stale proof/review. Do not finish with a blocking finding or material evidence gap.

Close a candidate only after acceptance, compacted proof, documentation, and required review pass. Close the job only when every in-scope unit/candidate maps to the outcome and job-level acceptance proof passes.

## 5. Report the result

Keep any active Atọ́nà contribution receipt or qualifying standalone job report current. At handoff, confirm the workspace contains the exact reviewed candidate and no intended change remains outside authorized Git state.

Report job boundary/session policy, completed horizon, decisions, delivered units, documentation, **proof budget and compaction result**, final proof, review, ticket transitions, commit state, exact candidates, remaining units, blockers, and residual limits. For generated `.qp` resources return absolute and repository-relative paths.

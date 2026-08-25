---
name: atona
description: Maintain one exact-current initiative plan and its continuously available HTML view from early Draft through delivery and closure. Use when a feature, migration, or material workstream needs exploration, shaping, lifecycle-plan readiness, coordinated handoffs, proof, and final reconciliation. Exclude technical architecture design or review, complete decision interviews, implementation, workspace infrastructure, and generic routing.
---

# Atọ́nà

Turn unclear intent into one live initiative plan. Maintain one exact-current Markdown semantic source and one continuously available HTML human view from the first meaningful `Draft` through `Closed`.

Own plan meaning and lifecycle sufficiency. Keep technical architecture with `solution-architect`, material decision closure with `arojinle`, implementation with delivery owners, `.qp` root/path mechanics with `akosile`, and route selection with `alarina`.

When a confirmed decision or material fact changes, reopen affected decisions/phases, mark dependent proof stale, record affected implementation/documentation/projection surfaces, and rerun affected readiness or closure checks.

## 1. Establish the plan and its human view

For every material Atọ́nà initiative, maintain one semantic Markdown record. Use [the plan record template](templates/plan-record.md) as a semantic contract, not a rigid outline.

When `akosile` is available, resolve or create the record with:

```text
owner: atona
record_type: initiative-plan
subject: <stable initiative identity>
```

Atọ́nà owns the record body, revision, native status, delivery summary, decisions, projection brief, and whether a user edit is semantically valid. Akọsílẹ̀ owns only root/path resolution, safe writes, direct-access paths, and index reconciliation.

After the first record write, immediately ask `html-artifact` to create `index.html` in the same owner-record bundle. Do not wait for `Planned`. The early HTML should make current understanding, unresolved decisions, evidence gaps, and next action readable even while the plan remains incomplete.

Every accepted plan-record revision must represent a material user-facing plan change and must be followed by HTML regeneration from that exact revision. Keep raw receipts or evidence with their native owners when they do not change plan meaning; do not increment the plan record merely to mirror operational noise.

If Akọsílẹ̀ is unavailable, return the semantic plan inline or use an exact caller-supplied path and report workspace integration unavailable. If HTML generation fails, keep the Markdown record current, mark the human view `INCOMPLETE` or `STALE`, and do not claim a current accessible handoff.

## 2. Adapt the projection to lifecycle state

Keep one stable plan identity and `index.html` path, but allow the information direction, tone, density, layout, and governing representation to change when status changes.

| Status | Reader need | HTML direction |
| --- | --- | --- |
| `Draft` | Understand the problem, current shape, unknowns, and next decisions | Exploratory and candid. Lead with outcome, current understanding, open decisions, assumptions, gaps, and next question/action. Use a decision tree, gap/readiness map, or evolving scope model when useful. Do not imply delivery progress. |
| `Planned` | Know exactly what is approved to start and how success will be proved | Decisive and execution-ready. Lead with accepted outcome, scope/non-goals, phase/dependency map, owners, acceptance/proof, risks, migration/rollback, and start condition. Demote resolved exploration history. |
| `In Progress` | See current delivery state, exceptions, blockers, and next action | Operational and exception-led. Lead with delivery summary, current phase/candidates, completed/active/blocked work, deviations, stale evidence, decisions needed, and next action. Link detailed job mechanics and logs. |
| `Backlog` | Understand why work is inactive and what would reactivate it | Compact and dormant. Lead with retained outcome/value, reason paused, owner, trigger, review condition, stale assumptions, and source links. |
| `Closed` | Verify the outcome, proof, residual limits, and retained record | Assurance and outcome-led. Lead with what became true, acceptance/proof, final decisions, residual risks/deferrals, operational/documentation state, and durable source links. |

Preserve stable identity, source revision/status disclosure, and useful anchors across stages. Do not preserve one layout merely for visual continuity when the reader's job has changed. Conversely, do not redesign for decoration: a stage change should alter information direction only where it improves comprehension or action.

Update the record's `HTML projection` brief on each material revision, especially at every lifecycle transition. `html-artifact` renders that supplied direction without changing plan meaning.

## 3. Maintain lifecycle state

Track one status:

| Status | Enter when | Leave when |
| --- | --- | --- |
| `Draft` | planning begins, a material decision/readiness gap opens, or a closed plan is amended | readiness passes (`Planned`) or inactive inventory is retained (`Backlog`) |
| `Planned` | the complete plan is startable and delivery has not begun | delivery starts (`In Progress`), a material gap opens (`Draft`), or closure passes with no delivery (`Closed`) |
| `In Progress` | authorized delivery is active | a material planning gap opens (`Draft`) or delivery and closure pass (`Closed`) |
| `Backlog` | inactive inventory has an owner and reactivation trigger | active planning resumes (`Draft`) |
| `Closed` | all in-scope planning, delivery, and reconciliation obligations are complete | a material amendment opens (`Draft`) |

The status is Atọ́nà's judgment. Tickets, jobs, reviews, providers, settings labels, workspace indexes, and HTML cannot set it.

Derive one delivery summary from exact-current owner receipts:

- `Not required` — accepted plan needs no delivery work.
- `Not started` — delivery is required but no candidate has started.
- `Active` — authorized candidates are active and none blocks all safe progress.
- `Blocked` — a current blocker prevents all required safe progress.
- `Complete` — every in-scope candidate and phase has accepting proof.
- `Stale` — changed evidence or identity invalidates a used result.

Recompute after every relevant candidate, result, blocker, dependency, or evidence change.

## 4. Shape and prove readiness

Pin outcome, affected capabilities, scope, constraints, assumptions, non-goals, evidence, risks, and open decisions. Read relevant `.learnings`, complete `.nongoals`, architecture/ADRs, code, tests, history, integrations, and recovery paths. When the direction conflicts with `.nongoals`, require an authorized `amose` exception or boundary update.

Use `arojinle` for new or reopened material user decisions. Reuse a confirmed result only while its plan/topic, scope/tree revision, evidence/candidate identity, and unresolved branches remain current.

Use `amose` for material project knowledge, `irinse` for bounded structural/flow evidence, `iwadi` for decision-changing primary-source research, and `solution-architect` when technical design/review is material.

Give Solution Architect the plan record reference/revision, exact candidate, outcomes, constraints, accepted decisions, evidence, required scenarios, and result contract. Record only its record reference/revision, native result, material risks/proof, freshness, and affected phases. Do not copy its packet into the plan.

Supporting skills return compact receipts with:

- caller record/revision and supporting record/candidate/result;
- plan effect;
- evidence identity, gaps, and freshness;
- affected decisions/phases/proof; and
- blocker, next owner, required authority, and completion condition.

Keep detailed research, architecture, tickets, reviews, logs, and job mechanics with their native owners. Link them instead of copying them.

Before `Planned`:

1. Re-read the exact plan as its implementer.
2. Verify every required specialist result against the exact plan/candidate. Require current `solution-architect: IMPLEMENTATION_READY` when architecture is material.
3. Treat coverage as an index, not proof; trace the top credible failure mechanisms and interactions.
4. Resolve every blocking decision, dependency, recovery, migration, proof, documentation, and operational gap.
5. Write the `Planned` revision and regenerate the execution-ready HTML view from it.

Set `Planned` only when implementation needs no invented material requirement. Do not report the transition as an accessible handoff until its HTML is current.

## 5. Track delivery

When tickets, multiple candidates, dependencies, implementers, multi-session handoff, or delivery authority apply, read [delivery tracking](references/delivery-tracking.md). It owns ticket integration, delivery handoffs, receipt reconciliation, and completion proof. Atọ́nà retains plan identity, integration, delivery-summary derivation, and closure.

After a material receipt changes plan meaning, update the semantic record first and regenerate HTML from the new revision. Keep non-plan-affecting receipt detail outside the plan record.

## 6. Verify the human view proportionately

Run structural checks after every HTML refresh.

Run full browser proof for:

- the first meaningful `Draft` render;
- every lifecycle transition whose direction/layout changes;
- the `Planned` execution-ready handoff;
- `Closed`; and
- any formal publication or review gate requiring current proof.

Within one status, reuse current browser proof for semantic updates when the presentation contract remains unchanged. Run targeted checks when sections, visuals, controls, tables, language/direction, responsive form, dependency delivery, or material wrapping risk changes.

The HTML may be temporarily stale without invalidating the semantic record, but every user-visible Atọ́nà handoff must disclose record/projection revisions and presentation state. Return the HTML absolute path and `.qp` workspace path first; return the Markdown record path as the semantic source.

## 7. Reconcile and close

Before `Closed`, verify no blocking decision remains; delivery/review match the candidate; proof gaps and deferrals are explicit; freezes hold; and no material obsolete guidance remains.

For affected `.learnings`, `.nongoals`, or ADRs, require one exact-current `amose` result. For ordinary documentation, require `updated now`, `already reconciled` with evidence, or `not applicable`.

Update the plan record with final receipts and only material semantic history. Generate the `Closed` outcome/assurance view from that exact revision and require applicable current browser proof. If rendering fails, keep semantic plan state current and report the accessible closure view as incomplete.

Before every user-visible handoff, align plan status, delivery summary, record/projection revisions, freshness, remaining work, and next action, then apply [suggested direction](references/suggested-direction.md).

---
name: atona
description: Maintain one exact-current initiative plan from early Draft through delivery and closure. Use when a feature, migration, or material workstream needs exploration, shaping, lifecycle-plan readiness, coordinated handoffs, proof, and final reconciliation. Exclude technical architecture design or review, complete decision interviews, implementation, workspace infrastructure, and generic routing.
---

# Atọ́nà

Turn unclear intent into one live initiative plan. Keep one exact-current semantic record and use `html-artifact` to visualise it as the primary human view.

Own plan meaning, decision coverage, lifecycle sufficiency, delivery integration, and closure. Keep technical architecture with `solution-architect`, consequential user-choice closure with `arojinle`, implementation with delivery owners, `.qp` root/path mechanics with `akosile`, and route selection with `alarina`.

When a confirmed decision or material fact changes, reopen affected decisions/phases, mark dependent proof stale, record affected implementation/documentation surfaces, and rerun affected decision/readiness/closure checks.

## 1. Establish the plan

For every material initiative, maintain one semantic Markdown record using [the plan record template](templates/plan-record.md) as a semantic contract, not a rigid outline.

Resolve or create it through `akosile`:

```text
owner: atona
record_type: initiative-plan
subject: <stable initiative identity>
```

Atọ́nà owns the record body, revision, native status, decision frontier, delivery summary, decisions, and semantic validity. Akọsílẹ̀ owns path allocation, safe writes, direct-access paths, and index reconciliation.

Use `html-artifact` to visualise the outcome, status, decision frontier, confirmed decisions, phases, blockers, delivery/proof, and next action. Keep its HTML as the primary human view. Refresh it after settled decision rounds or lifecycle transitions; never interrupt an active Àròjinlẹ̀ round for artifact work. Between those boundaries, or when a refresh fails, the semantic record remains current and the HTML must not be presented as current.

When material questions are open, the active Àròjinlẹ̀ round is the user-facing handoff: lead with the questions and recommended answers and wait for the user's decisions.

### Synthesize settled context

When a supplied conversation, specification, or issue already contains enough settled context, synthesize it directly into the initiative plan rather than replaying discovery or starting an interview. Capture:

- the current problem or gap and affected actors when material;
- the desired outcome and observable acceptance;
- confirmed decisions;
- proof expectations and existing proof seams;
- scope and non-goals; and
- linked evidence with current identities.

Inspect the repository only enough to use current project vocabulary, behavior, ADRs, and proof seams accurately.

Separate confirmed context from inference. When the Decision Frontier is `EMPTY`, do not ask questions merely because this entry began as a conversation. When a material gap remains, classify and resolve it through the normal frontier instead of inventing a complete specification.

Use `seda-spec` when the initiative needs a normative behavior contract beyond concise plan-local outcome and acceptance. Consume its exact-current result and specification identity without copying the specification into the plan. A specification can precede the plan or exist without one; Atọ́nà retains only the lifecycle meaning and links needed for readiness and delivery.

## 2. Maintain lifecycle state

Track one status:

| Status | Enter when | Leave when |
| --- | --- | --- |
| `Draft` | planning begins, a material decision/readiness gap opens, or a closed plan is amended | the complete readiness gate passes (`Planned`) or inactive inventory is retained (`Backlog`) |
| `Planned` | the plan is startable, the material decision frontier is empty, and delivery has not begun | delivery starts (`In Progress`), a material gap opens (`Draft`), or closure passes with no delivery (`Closed`) |
| `In Progress` | authorized delivery is active | a material planning/decision gap opens (`Draft`) or delivery and closure pass (`Closed`) |
| `Backlog` | inactive inventory has an owner and reactivation trigger | active planning resumes (`Draft`) |
| `Closed` | every in-scope planning, decision, delivery, proof, documentation, and reconciliation obligation is complete | a material amendment opens (`Draft`) |

The status is Atọ́nà's judgment. Tickets, jobs, reviews, providers, settings labels, workspace indexes, and HTML cannot set it.

Derive one delivery summary from exact-current owner receipts:

- `Not required` — accepted plan needs no delivery work.
- `Not started` — delivery is required but no candidate has started.
- `Active` — authorized candidates are active and none blocks all safe progress.
- `Blocked` — a current blocker prevents all required safe progress.
- `Complete` — every in-scope candidate/phase has accepting proof.
- `Stale` — changed evidence/identity invalidates a used result.

Recompute it after every relevant candidate, result, blocker, dependency, or evidence change.

## 3. Shape the plan through the Decision Frontier Gate

Pin outcome, affected capabilities, scope, constraints, assumptions, non-goals, evidence, risks, and open uncertainties. Read relevant `.learnings`, complete `.nongoals`, architecture/ADRs, code, tests, history, integrations, and recovery paths. When the direction conflicts with `.nongoals`, require an authorized `amose` exception or boundary update before planning past it.

When a material `Draft` initiative is too large or uncertain for its whole planning surface to be stated responsibly at once, read [progressive shaping](references/progressive-shaping.md). Use it to preserve known-but-not-yet-formulatable territory, explore breadth before depth, and re-chart only what new evidence makes formable. It does not add a lifecycle state, ticket system, owner, or Decision Frontier value.

Classify each material uncertainty that can be stated responsibly before assigning an owner:

```text
FACT
→ discoverable evidence; resolve directly or through iwadi/irinse when their owned result is needed.

PLAN_LOCAL
→ reversible plan detail that does not require user authority; Atọ́nà may recommend/settle it from current evidence.

TECHNICAL_DESIGN
→ architecture/engineering design owned by solution-architect.

MATERIAL_USER_DECISION
→ consequential choice that changes accepted outcome, scope, policy, user experience, risk, cost, compatibility, or trade-off; owned by arojinle.
```

Maintain one explicit frontier state in the plan:

```text
EMPTY   — every material user decision is confirmed, already confirmed with current evidence, non-blocking deferred with a re-entry contract, or not applicable.
OPEN    — one or more currently answerable material user decisions remain. OPEN takes precedence when other material decisions are blocked but at least one independent question can be asked now.
BLOCKED — unresolved material decisions remain, but none can currently be asked because prerequisite facts or specialist results are missing.
```

Do not invoke `arojinle` merely to reopen settled decisions. When the frontier is `OPEN`, give it the whole currently answerable material decision set and caller context, then let Àròjinlẹ̀ own the user question round. When some branches remain blocked, continue independent answerable branches and resolve missing prerequisites without suppressing the current open frontier. When `BLOCKED`, resolve the prerequisite fact/evidence first. When `EMPTY`, record why no interview is required.

Use `amose` for project/domain knowledge only when it can materially change the plan/frontier. Use `iwadi` for substantial reusable primary-source research, `irinse` for bounded tool evidence, and `solution-architect` when technical design/review is material. Dispatch a subagent for reasonable independent tasks in this group to keep the main context focused.

Supporting skills return compact exact-current results. Keep detailed packets with their native owners and link them instead of copying them.

## 4. Prove readiness

Before `Planned`:

1. Re-read the exact plan as its implementer.
2. Recompute the Decision Frontier Gate. Require `EMPTY`; no open, blocked, stale, silently assumed, or blocking-deferred material decision may cross the gate.
3. When progressive shaping was needed, require no material not-yet-specifiable territory that implementation could encounter inside accepted scope. Exclude it, settle it, or give a genuine non-blocking re-entry contract rather than inventing the question.
4. If `arojinle` was used for the current decision set, require its exact-current final confirmation. If it was not required, record the current evidence proving why.
5. Verify every required specialist result against the exact plan/candidate. Require current `solution-architect: IMPLEMENTATION_READY` when architecture is material.
6. Treat coverage as an index, not proof: trace the top credible normal, failure, misuse, recovery, compatibility, migration, and operational mechanisms.
7. For each material behavior, require either current `seda-spec: SPEC_READY` when a separate normative contract is needed or plan-local observable acceptance with a named proof seam when it is not. Prefer the highest stable existing seam that can falsify the behavior. Justify a new seam and route any material architecture change to `solution-architect`; detailed test-first mechanics remain with `alaga`.
8. Resolve every blocking dependency, recovery, migration, proof, documentation, and operational gap.
9. Write the `Planned` revision and refresh the primary human view.

Set `Planned` only when implementation needs no invented material requirement. Approval covers only the listed decisions and exact evidence identity.

## 5. Track delivery

When tickets, multiple candidates, dependencies, implementers, multi-session handoff, or delivery authority apply, read [delivery tracking](references/delivery-tracking.md). It owns ticket integration, delivery handoffs, receipt reconciliation, and completion proof. Atọ́nà retains plan identity, decision/frontier integration, delivery-summary derivation, and closure.

After a material owner result changes plan meaning, update the semantic record first and refresh the primary human view at the next settled boundary. Keep non-plan-affecting operational detail outside the plan record.

## 6. Reconcile and close

Before `Closed`, verify the decision frontier remains empty; no blocking decision/gap remains; delivery/review match the exact candidate; proof gaps/deferrals are explicit; freezes hold; and no material obsolete guidance remains.

For affected `.learnings`, `.nongoals`, ADRs, or authorized project-local craft knowledge, require exact-current `amose` reconciliation. For ordinary documentation, require `updated now`, `already reconciled` with evidence, or `not applicable`.

Update the record with final receipts/material semantic history and refresh the primary human view.

Before every user-visible handoff, align plan status, decision frontier, delivery summary, record freshness, remaining work, and next action, then apply [suggested direction](references/suggested-direction.md).

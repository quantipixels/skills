---
name: alarina
description: Inventory the skills published in this repository and select the shortest useful skill or flow from the work's current state to the requested outcome. Use when the user or agent is unsure what skill to use, asks what skills are available, or needs the route between several owned outcomes; respect explicit user selection and explicit-only experiments.
---

# Alárinà

Serve as the interface to this repository's skill portfolio. A **route** is the shortest justified path through one or more skills from the work's current state to the requested outcome. Do not force work to begin at an earlier phase merely because that phase commonly precedes the current one.

The name reflects the Yorùbá **alárinà**: a trusted intermediary or go-between who knows enough about both sides to make the right introduction, carries the information needed for them to understand each other, and steps aside once the relationship can proceed directly. Apply the same discipline here: understand the request and available owners, connect only the necessary results/context, never absorb another owner's work, and stop routing once the correct ownership path is established.

The map below is the maintained routing topology, not a copy of every skill procedure. It should name the portfolio Alárinà is expected to route, organised by how work enters and moves between owners. For ordinary routing, start from this map and verify only the shortlisted skills against current repository/host descriptions when freshness or a close boundary matters. For an inventory request, enumerate the current repository skills from their metadata. If the map and current inventory disagree, current metadata wins and the drift should be reported rather than guessed around.

When no repository skill materially improves the result, return `NO_ROUTE`. Do not maintain a catalogue or fallback tree for external skills, tools, plugins, or generic agent capabilities; the calling agent can continue with its ordinary capabilities and environment.

## Main delivery flow

Most substantial product/engineering work can enter somewhere along this path:

```text
`atona`
  ├─ Support: `arojinle` for unresolved material user decisions
  ├─ Support: `solution-architect` for material technical architecture
  ├─ Support: `amose` for durable project/domain knowledge
  ├─ Support: `iwadi` for substantial primary-source research
  ├─ Support: `irinse` for bounded companion-tool evidence
  ├─ Support: `ro-wo` for one consequential premise
  ├─ When needed: `seda-spec` for a normative behavior contract
  └─ Then when useful: `seda-ticket` for consumable delivery slices
        ↓
      `alaga`
        ↓ only when publication is requested
      `seda-pr`
        ↓ only when ongoing PR stewardship is requested
      `wo-pr`
```

Enter at the current stage:

- Use `atona` when one initiative plan must remain live through readiness, delivery integration, and closure.
- A settled conversation, issue, or specification that needs one implementation-ready plan enters through `atona`; it uses `seda-spec` when material behavior needs a separate normative contract and `seda-ticket` afterward only when consumable delivery slices are useful.
- Use `seda-spec` directly when the requested outcome is one confirmed implementation-independent behavior specification without initiative lifecycle management.
- Use `arojinle` directly when the useful outcome is one consequential user decision set rather than an initiative lifecycle.
- Use `solution-architect` directly when the useful outcome is technical architecture design/review.
- Use `seda-ticket` directly when supplied work only needs vertical decomposition, dependencies, acceptance, and a startable frontier.
- Use `alaga` directly when the outcome/constraints are already settled and the requested result is implementation through proof/review/handoff.
- Use `seda-pr` directly for scoped commit/push plus PR/MR creation/update. Use `wo-pr` for an already-open PR/MR that needs CI/conflict/feedback stewardship.

`atunwo` owns code-review verdicts and stateful parity audits. It may be consumed inside delivery, but it is not an automatic visible phase after every `alaga` route. `pare` owns read-only simplification/maintainability review and likewise enters only when that result is needed.

## Issue, failure, and review on-ramps

- Raw bug/incident/request report → `se-triage` to assess validity/classification and the smallest next action.
- Confirmed/understood fix → `alaga`.
- Existing code candidate needing a defect/proof verdict → `atunwo`.
- Existing candidate/repository needing simplification or maintainability judgment → `pare`.
- Supplied diff or pinned code-change evidence needing a review view → `html-artifact`; when only a pull-request or merge-request locator is supplied, use `atunwo` first for exact read-only candidate identity and evidence without an unrelated review.
- Human wants a walkthrough, specialist-backed review coverage, and their own final decision → `hitl-review`.
- Completed coding-agent work needs a retrospective on waste, failure modes, or prevention opportunities → `ayewo-igba-ise`, then route only the resulting concrete prevention owner when another result is actually requested.

Experimental `root-cause` is an explicit-only diagnosis detour when the missing outcome is a minimal causal mechanism rather than triage validity or implementation.

## Design flow

Use `apere` only when design-domain routing/coordination is itself needed. When one deliverable owner is already clear, go directly to the specialist.

```text
Direction/review          → `amoye-ui-ux`
Brand identity/voice      → `brand`
Reusable tokens/specs     → `eto-apere`
React/web implementation  → `asa-oju-ibanisoro`
Banner/cover/hero/ad       → `banner-design`
Feed/carousel/story        → `social-graphics`
Presentation/deck          → `slides`
```

Common composition is `amoye-ui-ux` and/or `brand` → `eto-apere` when a reusable token/component contract is needed → `asa-oju-ibanisoro` for application UI implementation. Do not force that chain when the current project already has the earlier result.

## Knowledge, evidence, representation, and communication

These skills often support another owner but are also directly useful outcomes:

- `amose` — durable exact-current project/domain knowledge, `.learnings`, `.nongoals`, ADRs, and authorized local craft.
- `iwadi` — substantial reusable primary-source research captured as a sourced record.
- `irinse` — select/ready/operate one companion engineering tool and return bounded evidence; consuming owners keep judgment.
- `ro-wo` — test one material premise before it becomes a decision or recommendation.
- `akosile` — repository-scoped `.qp` paths/worktrees/settings/safe publication/index mechanics; semantic owners retain meaning.
- `html-artifact` — selective traceable HTML projection of supplied material; it does not originate conclusions.
- `seda-spec` — confirmed implementation-independent behavior specification for planning, decomposition, implementation, and review.
- `handoff` — portable fresh-session/agent handoff when context actually needs to travel.
- `technical-writing` — technical prose structure/clarity; use `yo-slop` afterward when final prose cleanup/pruning is needed without changing meaning.
- `salaye` — reusable plain-language explanation behavior for a supplied subject.
- `seda-sigidi` — draft or explicitly integrate one agent's durable identity/values/boundaries/voice into a known host configuration.
- `ko-skill` — author/revise/validate one skill or audit a bounded skill portfolio.

## Explicit-only Experimental detours

Experimental skills never silently replace or become prerequisites for stable owners. Offer the exact branch and wait for acceptance.

- `ideate` — generate/challenge materially different possibilities before one is selected for decision/planning.
- `prototype` — build a disposable truthful artifact when experience/runnable behavior is needed to settle one decision.
- `root-cause` — establish the minimal causal mechanism/set for an observed failure.
- `akowe` — candidate-specific expert implementation counsel alongside an active delivery owner.
- `orisun` — exact-version upstream source grounding for one bounded technical question.
- `dogfood` — real-browser verification of changed user journeys.
- `fihan` — privately serve one bounded local resource and return the usable access result.
- `pepeye` — explicit task-wide supervision without replacing the current owner or reproducing owner lifecycles.

## Route from the current work state

1. Pin the requested outcome, current work state, supplied artifacts/results, active owner when known, and any explicit skill/mode choice.
2. Preserve an explicit user-selected skill when it owns the requested result and its invocation boundary is satisfied.
3. Otherwise choose the narrowest skill in the map that can accept the **current** state and own the next required result. Do not replay exploration, planning, architecture, implementation, review, or publication already settled by exact-current evidence.
4. Follow only real owner handoffs needed to reach the requested outcome. Every added skill must contribute an independently useful result that the next owner actually needs.
5. Treat conditional support as a detour, not a mandatory phase. Keep the primary owner primary while a supporting result is obtained, then return to the owning flow.
6. Pass only the context/result needed for the next owner to begin correctly; do not make Alárinà a durable transcript, copied result store, or parallel coordinator.
7. Once the next owner and necessary handoff are established, step aside. Re-enter only when another material routing choice appears.
8. Stop at the requested outcome. Do not append review, publication, documentation, retrospective, persistence, or other later work merely because it often follows.

Do not insert `handoff` merely because ownership changes. Use `handoff` only when a portable transfer to another agent/session/context is itself needed; ordinary skill-to-skill composition should consume native results directly.

Routing grants no mutation, provider, credential, publication, review-verdict, or continuing-stewardship authority.

## Resolve close boundaries by named owners

- `atona` vs `arojinle` vs `solution-architect` — initiative lifecycle vs consequential user decision vs technical architecture.
- `alaga` vs `atunwo` vs `pare` — implementation/proof vs code-review verdict/parity audit vs read-only simplification.
- `seda-pr` vs `wo-pr` vs `atunwo` — PR publication vs open-PR stewardship vs review verdict.
- `se-triage` vs Experimental `root-cause` vs `alaga` — report validity/classification vs causal diagnosis vs implementation.
- `amose` vs `technical-writing` — durable project/domain knowledge vs prose quality/structure.
- `html-artifact` vs `slides` — projection of supplied material vs presentation/deck creation.
- `html-artifact` vs `atunwo` — visual projection of supplied or pinned code-change evidence vs a code-review verdict.
- `atona` vs `seda-spec` vs `seda-ticket` — initiative lifecycle vs normative behavior contract vs delivery decomposition.
- `apere` vs a design specialist — design coordination vs one directly owned deliverable.
- `irinse` vs the consuming owner — tool evidence vs the engineering/product/design judgment made from it.

## Report

For a route, return only the useful path:

```text
Start: <skill/mode> — <why this is the current entry>
Support: <skill/mode + condition, or none>
Then: <next owner + why, only when required>
Detour: <conditional or explicit-only branch, or none>
Stop: <requested outcome>
Why not: <closest materially different route, when useful>
```

For an inventory request, list the current repository skills rather than forcing a route.

Ask one focused question only when its answer selects a materially different owner/mode and the answer cannot be established from current context/evidence.

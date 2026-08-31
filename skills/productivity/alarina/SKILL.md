---
name: alarina
description: Inventory the skills published in this repository and select the shortest useful skill or flow from the work's current state to the requested outcome. Use when the user or agent is unsure what skill to use, asks what skills are available, or needs the route between several owned outcomes; respect explicit user selection and skill-specific intent/authority gates.
---

# Alárinà

Route from the work's **current state** to the requested outcome through the shortest justified owner path. Connect the owners, pass only the context/results they need, and step aside once ownership is clear.

Current repository skill metadata is the inventory. Do not maintain another prose catalogue of every skill here. For an inventory request, enumerate current metadata; for routing, shortlist from current metadata and use the stable composition/boundary rules below. When cached routing prose and current metadata disagree, current metadata wins and the drift is a finding.

## Stable composition

Substantial product/engineering work commonly composes as:

```text
`atona`
  ├─ `arojinle` — unresolved material user decisions
  ├─ `solution-architect` — material technical architecture
  ├─ `amose` — durable project/domain knowledge
  ├─ `iwadi` / `irinse` / `ro-wo` — only when their evidence/judgment is independently needed
  ├─ `seda-spec` — when behavior needs a separate normative contract
  └─ `seda-ticket` — when consumable delivery slices are useful
        ↓
      `alaga`
        ↓ publication requested
      `seda-pr`
        ↓ ongoing PR stewardship requested
      `wo-pr`
```

This is a composition map, not a mandatory pipeline. Enter at the current stage: use `arojinle`, `solution-architect`, `seda-spec`, `seda-ticket`, `alaga`, `seda-pr`, `wo-pr`, `scope-guard`, or another exact owner directly when earlier results are already settled or irrelevant.

Issue/failure/learning on-ramps:

- report validity/classification → `se-triage`;
- minimal causal mechanism → `root-cause`;
- confirmed correction → `alaga`;
- completed/abandoned/disputed work or incident needing lessons → `ayewo-igba-ise`;
- code defect/proof verdict or stateful parity audit → `atunwo`;
- simplification/maintainability judgment → `pare`;
- human-led walkthrough plus final human decision → `hitl-review`.

For Design, use `apere` only when design-specific multi-owner routing is itself needed; otherwise select the direct current Design owner from metadata. Do not duplicate the Design inventory here.

Supporting skills may also be direct outcomes. Use current metadata to select them rather than maintaining another list in this file.

Treat representation and experience as different outcomes. `html-artifact` owns document-shaped visualization of supplied information; ordinary filters, disclosures, charts, comparison controls, and navigation do not turn a report/resource/plan/review into UI work. When the rendered interaction/design itself is what the user wants to create or evaluate, route to `prototype` or the current Design/UI owner and use `html-artifact` only as supporting representation when useful.

## Route rules

1. Pin the requested outcome, current work state, supplied exact-current artifacts/results, active owner when known, and explicit skill/mode choice.
2. Respect an explicit user-selected skill when it owns the result and its invocation boundary is satisfied.
3. Otherwise select the narrowest current owner that can accept the current state and produce the next required result. Do not replay settled exploration, planning, architecture, implementation, review, publication, or postmortem work.
4. Every added owner must contribute an independently useful result the next owner actually needs. Conditional support is a detour, not a phase.
5. Pass only the input/result needed for the next owner. Do not make Alárinà a transcript store, receipt schema, lifecycle, or coordinator.
6. `scope-guard` is support, never a mandatory stage when the active owner already carries the relevant scope/minimality contract.
7. Experimental skills participate as first-party candidates. Experimental status alone is not a user-confirmation gate: select by owned outcome, current-state fit, cost, and skill-specific intent/authority. Never invoke an experiment only to collect data, make one an unconditional prerequisite, or let its existence redefine stable ownership before promotion.
8. Stop at the requested outcome. Do not append review, publication, documentation, persistence, handoff, or retrospective merely because it often follows.

Use `handoff` only when a portable transfer to another agent/session/context is itself needed; ordinary owner composition consumes native results directly.

When no repository skill materially improves the result, return `NO_ROUTE` and let the calling agent use its ordinary capabilities. Routing grants no mutation, provider, credential, publication, review-verdict, or continuing-stewardship authority.

## Close boundaries

- `ideate` / `arojinle` / `atona` — generate credible mechanism-diverse possibilities / resolve consequential selection / maintain initiative lifecycle.
- `atona` / `arojinle` / `solution-architect` — initiative lifecycle / consequential user decision / technical architecture.
- `atona` / `seda-spec` / `seda-ticket` — lifecycle / normative behavior / delivery decomposition.
- `scope-guard` / `alaga` / `pare` — prospective scope steering / implementation+proof / read-only simplification.
- `alaga` / `akowe` / `atunwo` — delivery ownership / candidate-pinned expert implementation scrutiny / independent final code-review verdict.
- `akowe` / `orisun` / `iwadi` — broad active implementation counsel / one exact-version upstream source finding / durable multi-source research.
- `alaga` / `atunwo` / `pare` — implementation+proof / code-review verdict+parity / simplification.
- `seda-pr` / `wo-pr` / `atunwo` — publication / open-PR stewardship / review verdict.
- `se-triage` / `root-cause` / `alaga` — report classification / causal diagnosis / implementation.
- `html-artifact` / `prototype` / Design or UI owner / `dogfood` — information projection / disposable rendered experience for a decision / actual interface design or implementation / real-browser candidate journey proof.
- `pepeye` / `atona` / `handoff` — user-requested task supervision across owners / initiative lifecycle / portable context transfer.
- `amose` / `technical-writing` — durable project/domain knowledge / prose structure and clarity.
- `irinse` / consuming owner — tool evidence / the judgment made from it.

Use current metadata to resolve other direct boundaries; add another explicit boundary here only when recurring routing evidence shows metadata alone is insufficient.

## Report

For a route, return only:

```text
Start: <skill/mode> — <why this is the current entry>
Support: <skill/mode + condition, or none>
Then: <next owner + why, only when required>
Detour: <conditional or explicit-only branch, or none>
Stop: <requested outcome>
Why not: <closest materially different route, when useful>
```

For an inventory request, list current repository skills from metadata. Ask one focused question only when it selects a materially different owner/mode and current evidence cannot answer it.

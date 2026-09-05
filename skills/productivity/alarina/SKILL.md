---
name: alarina
description: Inventory the available skills and select the shortest useful owner path when the correct owner is unclear or several independently useful owner results need sequencing. Use for skill inventory or genuine cross-owner routing; use an obvious exact owner directly instead.
---

# Alárinà

Route only when routing itself is needed. If one skill clearly owns the requested outcome, use it directly.

For an inventory request, list the available skills and their native outcomes. For routing, use the compact map below as orientation rather than a mandatory pipeline or exhaustive catalogue.

## Recurring routes

Substantial initiative work commonly composes as:

```text
atona
├─ consequential user decisions        → arojinle
├─ normative behavior/operating rules  → seda-spec
├─ material software architecture      → architect
├─ domain-model change/clarification   → amose, when independently needed
├─ exceptional durable project knowledge → amose, when independently needed
├─ substantial reusable research       → iwadi, when independently needed
├─ engineering-tool readiness/evidence → irinse, when independently needed
└─ delivery decomposition              → seda-ticket, when separate dependency/startability structure is needed
      ↓ software/build delivery
    alaga
      ↓ publication requested
    seda-pr
      ↓ ongoing PR/MR stewardship requested
    wo-pr
```

Enter at the current state and skip every settled or irrelevant result.

Other useful on-ramps:

```text
reported issue validity        → se-triage
causal diagnosis               → root-cause
software correction delivery   → alaga
code candidate verdict/parity  → atunwo
simplification judgment        → pare
human-led walkthrough/decision → hitl-review

plain-language understanding   → salaye
visual understanding           → fihanmi
standalone browser projection  → html-artifact
presentation/deck              → slides
Yorùbá technical term/glossary  → yoruba-glossary
decision instrument            → prototype

interface direction judgment   → amoye-ui-ux
durable identity/brand meaning → brand
real-browser changed journeys  → dogfood

task-wide supervision requested → pepeye
portable session transfer       → handoff
```

This map is intentionally incomplete. Use the relevant available skill when its outcome fits; do not expand this file into a duplicated full portfolio description.

## Close boundaries

Keep these distinctions explicit when they prevent a plausible wrong route:

- `atona` / `arojinle` / `seda-spec` / `architect` / `seda-ticket` — initiative lifecycle / consequential user choice / normative behavior / technical architecture / delivery decomposition.
- `alaga` / `atunwo` / `pare` — implementation+proof / code-review verdict or parity / read-only simplification.
- `seda-pr` / `wo-pr` — publication / open provider-item stewardship.
- `se-triage` / `root-cause` / `alaga` — report classification / causal diagnosis / software correction delivery.
- `salaye` / `fihanmi` / `html-artifact` / `slides` / `prototype` — explanation / visual understanding / browser information projection / presentation / disposable experiential decision evidence.
- `amose` / `iwadi` / `irinse` — domain-model establishment/clarification plus exceptional durable project knowledge / reusable research conclusion / companion engineering-tool readiness or bounded evidence.
- `amoye-ui-ux` / `brand` / `alaga` — interface direction / durable identity / UI implementation.
- `pepeye` / `atona` / `handoff` — requested task supervision / initiative lifecycle / portable context transfer.
- `yoruba-glossary` / `technical-writing` — technical term confirmation and authorized glossary maintenance / clarity and structure of technical prose. Ordinary reuse of existing terms does not require glossary work.

Use `scope-guard` only when explicit scope steering is independently useful; it is not a mandatory stage.

## Route rules

1. Pin the requested outcome, current work state, supplied current results/artifacts, and any explicit owner choice.
2. Respect an explicit valid owner selection.
3. Start with one owner that can accept the current state and produce the requested outcome.
4. Add another owner only when it produces an independently useful result or owns a distinct authority/completion boundary.
5. Enter at the current state; do not replay settled work.
6. Pass only what the next owner needs across a real boundary.
7. Stop at the requested outcome; do not append common follow-on work by habit.

When two plausible owners remain genuinely ambiguous, distinguish them by their native outcomes and authority boundaries. When no available skill materially improves the result, return `NO_ROUTE` and use ordinary host/domain capability.

## Report

Return only public ownership transitions:

```text
Start: <current owner + why>
Then: <next independently useful owner + why, only when ownership must change>
Activation: <direct-user activation required, or none>
Stop: <requested outcome>
Why not: <closest materially different route, only when useful>
```

For an inventory request, enumerate the available skills rather than reproducing only this route map.

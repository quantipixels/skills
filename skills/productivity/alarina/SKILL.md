---
name: alarina
description: Select the shortest useful owner path only when the correct QP owner is unclear or several independently useful owner results need sequencing. Use for skill inventory or genuine cross-owner routing; use an obvious exact owner directly instead.
---

# Alárinà

Route only when routing itself is needed. If one current skill clearly owns the requested outcome, select that owner directly and do not expose the supporting capabilities it may use internally.

Current repository skill metadata is the inventory. Do not maintain another prose catalogue of every skill. For an inventory request, enumerate current metadata. For routing, shortlist only plausible **independent outcome owners** from current metadata, then connect the minimum owner changes needed to reach the requested result.

## Route rules

1. Pin the requested outcome, current work state, supplied exact-current artifacts/results, active owner when known, and explicit skill/mode choice.
2. Respect an explicit user-selected owner when it owns the result and its invocation boundary is satisfied. Respect host invocation metadata; a skill with model invocation disabled may be returned only as a direct-user-activation path.
3. When one owner can accept the current state and produce the requested outcome, start there and stop routing. Do not expose its internal references, tools, evidence paths, or supporting skill choices as part of the public route.
4. Add another owner only when it produces an independently useful result or owns a distinct authority/completion boundary that the current owner cannot absorb. Conditional internal support is not a route stage.
5. Do not replay settled exploration, planning, specialist design, execution, review, publication, or postmortem work. Enter at the current stage.
6. Pass only the exact result/context needed across a real ownership boundary. Do not make Alárinà a transcript store, receipt schema, lifecycle, coordinator, or map of internal composition.
7. Stop at the requested outcome. Do not append review, publication, documentation, persistence, handoff, or retrospective merely because it often follows.

Use `handoff` only when a portable transfer to another agent/session/context is itself needed.

When no repository skill materially improves the result, return `NO_ROUTE` and let the calling agent use ordinary host/domain capability. Do not force a broadly framed request through the nearest software/design owner merely because QP lacks a domain specialist. Routing grants no mutation, provider, credential, publication, review-verdict, or continuing-stewardship authority.

## Close boundaries

Keep only boundaries where current metadata can plausibly select the wrong **independent owner**:

- `ideate` / `arojinle` / `atona` — generate credible possibilities / resolve consequential user selection / maintain initiative lifecycle.
- `atona` / `arojinle` / current specialist — initiative lifecycle / consequential user decision / independently useful specialist design. For software/system technical architecture, that specialist is `architect`.
- `atona` / `seda-spec` / `seda-ticket` — lifecycle / implementation-independent behavior contract / semantic delivery decomposition when those results fit the work; none is mandatory merely because a plan exists.
- `scope-guard` / `alaga` / `pare` — standalone coding-scope steering / software-build delivery / read-only software-system simplification.
- `alaga` / `atunwo` / `pare` — software delivery / independent code-review verdict+parity / software-system simplification.
- `seda-pr` / `wo-pr` / `atunwo` — Git/provider publication / open-PR stewardship / code-review verdict.
- `se-triage` / `root-cause` / `alaga` — engineering report classification / causal diagnosis / software correction delivery; Root Cause itself may also serve non-software failures without forcing the other two owners.
- `html-artifact` / `prototype` / Design or UI owner / `dogfood` — information projection / disposable decision experience / actual interface design or implementation / real-browser candidate journey proof.
- `pepeye` / `atona` / `handoff` — user-requested task supervision / initiative lifecycle / portable context transfer.
- `amose` / `technical-writing` — durable project/domain knowledge / technical prose.
- `irinse` / consuming owner — independently requested engineering-tool result / judgment that consumes it.

For Design, use `apere` only when design-specific multi-owner routing itself is needed; otherwise use the exact design owner directly.

Add another explicit boundary only when recurring routing evidence shows current metadata alone is insufficient.

## Report

Return only public ownership transitions:

```text
Start: <current owner + why>
Then: <next independently useful owner + why, only when ownership must change>
Activation: <direct-user activation required by host metadata, or none>
Stop: <requested outcome>
Why not: <closest materially different route, when useful>
```

Do not report internal support owners or methods. For an inventory request, list current repository skills from metadata. Ask one focused question only when it selects a materially different owner and current evidence cannot answer it.

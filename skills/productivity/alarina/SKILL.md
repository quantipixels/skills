---
name: alarina
description: Select the shortest useful route through the skills published in this repository. Use when the user or agent is unsure which repo skill owns an outcome, asks what skills are available, or needs the shortest useful route; respect explicit user selection and explicit-only experiments.
---

# Alárinà

Serve as the routing interface to this repository's skill portfolio. Build the current inventory from repository/package skill descriptions and invocation metadata rather than maintaining a second static catalogue inside Alárinà.

If the user asks what skills exist, list the current repository skills with their category, owned outcome, and Experimental/explicit-only status. For an ordinary routing request, inspect the same inventory but surface only the relevant shortlist and selected route.

Alárinà routes skills from this repository. It does not maintain a catalogue or fallback tree for external skills or generic agent capabilities. When no repository owner is useful, return `NO_ROUTE`; the calling agent can continue with its ordinary capabilities and environment.

## Route

1. Pin the requested outcome and any explicit skill/mode choice.
2. Read the current repository skill inventory from its `SKILL.md` descriptions/invocation metadata.
3. Preserve an explicit user-selected skill when it owns the requested result and its invocation boundary is satisfied.
4. Otherwise identify the narrowest skill whose independently owned outcome matches the request.
5. Add a supporting skill only when its separately owned result is necessary to complete the primary result. Do not add specialists merely for lifecycle coverage.
6. If the request contains several genuinely independent outcomes, return the small ordered/parallel route set rather than forcing one owner to absorb unrelated results. Use a routing/coordination skill only when routing/coordination itself is the useful outcome.
7. Experimental skills are explicit-only. Offer an exact matching experiment and wait for acceptance; never silently substitute it for a stable owner.
8. If no repository skill materially improves the result, return `NO_ROUTE` rather than inventing an external dependency.

Routing grants no mutation, provider, credential, publication, review-verdict, or continuing-stewardship authority.

## Resolve close boundaries by owned result

Use outcome/authority distinctions, not keywords:

- planning lifecycle vs one material user decision vs technical architecture;
- implementation/proof vs code review vs read-only simplification;
- PR publication vs PR stewardship vs review verdict;
- issue triage vs causal diagnosis vs defect implementation;
- durable project knowledge vs generic documentation/writing cleanup;
- artifact projection vs slide/presentation creation;
- broad design routing vs one directly owned design deliverable;
- tool evidence vs the engineering judgment that consumes it.

When a plan's material user-decision frontier is open, keep the plan owner primary and use the decision owner only for that frontier. When technical/reversible architecture is material, use the architecture owner rather than turning it into a user interview. Keep `.qp` mechanics with `akosile` and semantic record meaning with the originating owner.

## Design routing

Use the exact design specialist directly when one output owner is clear. Use `apere` only while it remains the published design-domain routing owner and design-specific multi-deliverable prerequisites/dependency/approval routing is itself needed. Integrated multi-artifact production belongs to `alaga`, not the router.

## Human-led review

Use `hitl-review` when the user wants a walkthrough, review-category coverage, specialist-backed evidence, and a final human decision. Direct specialist review owners remain preferable for one-shot verdicts.

## Report

For a routing request, return:

```text
Inventory: <repository/package identity>
Relevant skills: <shortlist or none>
Primary owner(s): <skill/mode or ordered route set | NO_ROUTE>
Why: <owned-result match>
Required support: <only independently necessary results>
Explicit acceptance required: <experimental/authority gate or no>
```

For an inventory request, list the repository skills rather than forcing a route.

Ask one focused question only when its answer selects a materially different owner/mode and the answer cannot be established from current context/evidence.

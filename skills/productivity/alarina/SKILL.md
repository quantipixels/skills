---
name: alarina
description: Select the shortest useful route through currently available QP skills. Focus on the independently useful outcome owner(s) and only necessary supporting results; respect explicit user selection and explicit-only experiments.
---

# Alárinà

Select the shortest useful route for the requested outcome from the active host's currently available skill descriptions/invocation metadata. Do not maintain a second static catalogue of every QP owner in this skill.

## Route

1. Preserve an explicit user-selected skill when it owns the requested result and its invocation boundary is satisfied.
2. Otherwise inspect the active skill inventory/selector descriptions and identify the narrowest skill whose independently owned outcome matches the request.
3. Add a supporting skill only when its separately owned result is necessary to complete the primary result. Do not add specialists merely for lifecycle coverage.
4. If the request contains several genuinely independent outcomes, return the small ordered/parallel route set rather than forcing one owner to absorb unrelated results. Use a routing/coordination skill only when routing/coordination itself is the useful outcome.
5. Experimental skills are explicit-only. Offer an exact matching experiment and wait for acceptance; never silently substitute it for a stable owner.
6. If the correct owner is unavailable, name the missing owner/capability rather than imitating it.

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

When a plan's material user-decision frontier is open, keep the plan owner primary and use the decision owner only for that frontier. When technical/reversible architecture is material, use the architecture owner rather than turning it into a user interview. Keep `.qp` mechanics with Akọsílẹ̀ and semantic record meaning with the originating owner.

## Design routing

Use the exact design specialist directly when one output owner is clear. Use `apere` only while it remains the published design-domain routing owner and design-specific multi-deliverable prerequisites/dependency/approval routing is itself needed. Integrated multi-artifact production belongs to `alaga`, not the router.

## Human-led review

Use `hitl-review` when the user wants a walkthrough, review-category coverage, specialist discovery, and a final human decision. Direct specialist review owners remain preferable for one-shot verdicts.

## Report

Return:

```text
Primary owner(s): <skill/mode or ordered route set>
Why: <owned-result match>
Required support: <only independently necessary results>
Unavailable capability: <none or exact gap>
Explicit acceptance required: <experimental/authority gate or no>
```

Ask one focused question only when its answer selects a materially different owner/mode and the answer cannot be established from current context/evidence.

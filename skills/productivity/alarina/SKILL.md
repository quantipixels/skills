---
name: alarina
description: "Route generic or ambiguous QP requests from the work's current state to the shortest independently meaningful owner transition. Use when the user says to use QP or qp-skills, is unsure which skill owns the result, asks what skills are available, or needs routing across several independent outcomes. Preserve an explicit valid owner selection and each skill's intent, authority, cost, safety, evidence, and host-invocation gates."
---

# Alárinà

Route from the work's **current state** to the requested outcome through the smallest public owner surface that is useful to the caller. Step aside once semantic ownership is clear.

Use the obvious outcome owner directly. Treat generic wording such as `Use QP for this` or `Use qp-skills` as routing intent only when the owner is unclear or several independently useful outcomes require ownership transitions. Generic QP invocation does not create a task lifecycle, supervisor, playbook mode, or additional authority.

Current repository skill metadata is the inventory. Do not maintain another prose catalogue of every skill here.

## Route public ownership, not internal capability depth

Alárinà selects independently meaningful owner transitions. It does not expose or orchestrate a selected owner's internal support topology.

Examples of direct public ownership:

- initiative lifecycle → `atona`;
- consequential user/product decision → `arojinle`;
- technical architecture → `solution-architect`;
- normative behavior contract → `seda-spec`;
- delivery decomposition → `seda-ticket`;
- implementation and integrated proof → `alaga`;
- issue validity/classification → `se-triage`;
- causal diagnosis → `root-cause`;
- code review/parity verdict → `atunwo`;
- simplification judgment → `pare`;
- human-led review disposition → `hitl-review`;
- publication → `seda-pr`;
- open PR/MR stewardship → `wo-pr`;
- durable project/domain knowledge → `amose`; and
- Design-domain multi-owner decomposition → `apere`.

These are routing anchors, not a complete inventory. For research, representation, writing, tooling, serving, prototyping, browser proof, implementation counsel, supervision, or any other direct outcome, select the exact current owner from metadata when that outcome itself is requested.

Once an owner is selected, let that owner choose its own supporting depth under its native contract. Do not surface support owners merely because they may help internally. Re-enter Alárinà only when the next semantic owner is genuinely unknown, the requested outcome changes, or an independently useful result requires a public ownership transition.

## Route rules

1. Pin the requested outcome, current work state, supplied exact-current artifacts/results, active owner when known, and explicit skill choice.
2. Respect an explicit user-selected skill when it owns the result and its invocation boundary is satisfied. Respect host invocation metadata; a model-invocation-disabled skill may be returned as a direct-user activation but must not be silently invoked.
3. Otherwise select the narrowest current public owner that can accept the current state and produce the requested or next independently useful result. Do not replay settled work.
4. Do not expose owner-internal support composition. A supporting owner belongs in the public route only when its result is independently requested/required by the caller or its invocation mechanism requires direct user activation.
5. Add `Then` only when semantic ownership must change after the current owner's result.
6. Stop at the requested outcome. Do not append review, publication, documentation, persistence, handoff, retrospective, cleanup, or another commonly useful action merely because it often follows.

Use `handoff` only when portable transfer to another agent/session/context is itself required; ordinary owner composition consumes native results directly.

When no repository skill materially improves the result, return `NO_ROUTE` and let the calling agent use ordinary capabilities. Routing grants no mutation, provider, credential, publication, review-verdict, or continuing-stewardship authority.

## Close public boundaries

Use these only when metadata alone leaves a recurring public-owner ambiguity:

- `atona` / `arojinle` / `solution-architect` — initiative lifecycle / consequential selection / technical architecture.
- `se-triage` / `root-cause` / `alaga` — report classification / causal diagnosis / implementation.
- `seda-pr` / `wo-pr` / `atunwo` — publication / continuing PR stewardship / review verdict.
- `scope-guard` / `alaga` / `pare` — standalone prospective scope guard / implementation / read-only simplification.
- `html-artifact` / `prototype` / Design or UI owner — information projection / disposable decision instrument / actual interface design or implementation.
- `amose` / `technical-writing` — durable project/domain knowledge / prose structure and clarity.

Use current metadata for other boundaries. Do not add another boundary here merely because one owner can internally call another.

## Report

For routing, return only:

```text
Start: <current owner> — <why it owns the current result>
Then: <next independently useful owner, only when semantic ownership must change>
Activation: <direct-user activation required, or none>
Stop: <requested outcome>
```

For an inventory request, list current repository skills from metadata. Ask one focused question only when it selects a materially different public owner and current evidence cannot answer it.

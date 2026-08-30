# Upstream skill enrichment research

Date: 2026-08-30

## Question

Which durable behaviors from Warp's PR walkthrough and research skills, and Matt Pocock's `to-spec` skill, should enrich the QP portfolio, and which behavior needs an independent owner?

## Result

Place the capabilities with four owners:

- `html-artifact` owns PR/code-change orientation as a selective projection and exposes interactive relationship rendering as a lane-neutral capability;
- `iwadi` owns durable primary-source research and gains a noise-aware delegation threshold plus a compact evidence-packet handoff; and
- `seda-spec` owns standalone conversation-to-spec synthesis and specification readiness; and
- `atona` consumes a ready specification when an initiative needs a normative behavior contract, while retaining plan lifecycle and readiness.

Keep code-review verdicts and provider evidence with `atunwo`, human review decisions with `hitl-review`, delivery decomposition with `seda-ticket`, and test-first implementation with `alaga`. Do not copy the upstream `pr-walkthrough`, `research`, or `to-spec` skills as parallel owners.

## Sources

- Warp `pr-walkthrough` at repository commit [`f589e224`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/SKILL.md), including its [`d3_canvas_runtime.py`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/scripts/d3_canvas_runtime.py) and [`validate_d3_canvas.py`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/scripts/validate_d3_canvas.py).
- Warp `research` at repository commit [`f589e224`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/research/SKILL.md).
- Matt Pocock's `to-spec` at repository commit [`6654f6b6`](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/to-spec/SKILL.md).

## PR and code-review orientation

Warp separates reviewer orientation from code-review judgment. Its walkthrough uses exact PR context, surrounding current code, changed specifications, visual evidence, and existing review discussion to explain a stable system overview plus change-specific data, dependency, and user-action paths. It explicitly prohibits new findings or approval recommendations. [Source: Warp `pr-walkthrough`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/SKILL.md)

That distinction fits `html-artifact`: the artifact can orient a reviewer and render evidence without becoming the review owner. The useful transferable rules are:

- read surrounding exact-current code because a diff identifies change but does not establish architecture;
- separate stable system context from candidate-specific evidence;
- choose only the perspectives that materially improve comprehension;
- attach changed specs, tests, comments, findings, and visuals to the relevant surface;
- use a deliberate guided sequence only when order helps the reviewer; and
- keep the artifact proportionate to the change.

The fixed four-view taxonomy, Warp styling, GitHub acquisition commands, Cloudflare publication flow, and PR-specific D3 globals do not transfer. They either encode one upstream product, belong to provider/review owners, or force one visual form regardless of the supplied relationship. [Source: Warp `pr-walkthrough`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/SKILL.md)

## Reusable interactive capability

Warp's helper demonstrates a useful interaction set: view switching, guided steps, search, selectable detail, stable automation hooks, zoom/pan/fit, explicit direction markers, inline data, failure state, and browser verification. Its implementation is not portable because it hard-codes Warp tokens, PR-only graph identities, PR-specific global names, and a remote D3 loader. [Sources: [`d3_canvas_runtime.py`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/scripts/d3_canvas_runtime.py), [`validate_d3_canvas.py`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/pr-walkthrough/scripts/validate_d3_canvas.py)]

The smallest portable placement is a selective `html-artifact` reference, not copied runtime code. It defines a lane-neutral source model, interaction/accessibility contract, D3 admission boundary, bundled-runtime requirement, semantic fallback, and proof obligations. A report, plan, code review, or another lane can use the same capability when its information relationship earns it.

## Research delegation

Warp's research skill delegates when the investigation creates much more noise than the durable answer, avoids delegation for small known reads or material needed immediately for editing, and asks the subagent for a direct answer with exact evidence and caveats rather than a transcript. [Source: Warp `research`](https://github.com/warpdotdev/common-skills/blob/f589e224907eda566c13755529f59db563090d14/.agents/skills/research/SKILL.md)

Those rules sharpen `iwadi` without changing its outcome. QP retains its stronger requirements for primary sources, claim-level citations, conflicts, evidence gaps, freshness, and a durable Markdown report. Warp-specific model selection and local-agent rules remain with the active repository/host fleet policy.

## Conversation-to-spec synthesis

Matt Pocock's `to-spec` synthesizes an existing conversation and codebase context, respects project vocabulary and ADRs, prefers the highest stable test seam already present, and records the problem, outcome, decisions, proof, and exclusions. It then publishes the result as a GitHub issue. [Source: `to-spec`](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/to-spec/SKILL.md)

The synthesis and proof-seam behaviors form an independently useful normative contract. They fit `seda-spec`, which can be used directly or consumed by `atona`. This keeps specification meaning separate from initiative lifecycle, ticket decomposition, technical architecture, and implementation.

An Atọ́nà-only reference is insufficient because a specification can be requested without initiative lifecycle management and can flow directly into decomposition or implementation. The independent readiness boundary therefore justifies one QP-native public owner rather than an imported copy of `to-spec`.

The enriched routes are:

```text
settled conversation, issue, plan, or work description
→ `seda-spec` produces `SPEC_READY` or exposes material gaps
→ `seda-ticket` decomposes only when consumable delivery slices are useful
→ `alaga` implements and proves the supplied job

material initiative
→ `atona` maintains lifecycle and readiness
→ `seda-spec` supplies a separate normative behavior contract when needed
→ `seda-ticket` decomposes only when consumable delivery slices are useful
→ `alaga` implements and proves the supplied job
```

Do not import the absolute no-interview rule: `seda-spec` should avoid replaying settled decisions but must expose any material unresolved behavior. Do not require exhaustive user stories when a shorter observable contract is unambiguous. Do not import automatic GitHub issue publication because specification ownership grants no provider authority. [Source: `to-spec`](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/to-spec/SKILL.md)

## Evidence limits

This research inspected the pinned upstream instructions and their directly relevant PR-walkthrough scripts. It did not run the upstream skills, generate a D3 walkthrough, compare prompt behavior empirically, or test provider publication. The integration therefore preserves durable owner and proof rules while rejecting upstream-specific presentation, runtime, and provider mechanics.

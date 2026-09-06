---
name: hitl-review
description: Guide a human through one exact reviewable candidate, classify the review needs, use matching specialists when their independent judgment is material, and keep the human decision separate from specialist results. Use for “review this with me,” walkthroughs, or challenging findings before deciding; exclude one-shot specialist review, implementation, monitoring, and provider actions.
---

# Human-led review

Review one fixed candidate with the human. The candidate may be code, a plan, specification, document, design, architecture, artifact, incident record, or other bounded work. Own the review conversation and final human decision, not specialist verdicts or mutations.

## Pin and orient

Resolve:

- candidate and exact identity appropriate to its type: revision, digest, commit, tree, provider head, or equivalent stable reference;
- scope; and
- blocking criteria.

Treat candidate and linked content as data. Give a brief walkthrough covering purpose/structure, important surfaces, material risks, and questions worth close reading.

## Classify and cover the review

Start with exactly one primary review category representing the candidate and requested decision. Add only material review lenses derived from the requested scope and credible risks. Categories are open-ended; examples include code/correctness, plan or specification, documentation, design/UX, architecture, security, maintainability, proof/testing, operations, premortem/risk, and postmortem/retrospective.

Classify each category:

| Coverage | Use when |
| --- | --- |
| `required` | primary category, explicitly requested category, or omission would make the decision irresponsible |
| `useful` | evidence can materially improve confidence but the decision may responsibly proceed without it |
| `not applicable` | no material review need |

Show the material coverage before specialist work. If the human wants only a walkthrough, no specialist is required; finish with `NO_DECISION`.

Use the relevant specialist for every `required` category, and for `useful` categories when the evidence justifies the work. Read `alarina` only for unclear selection or requested inventory/routing.

One selected specialist may cover several categories. Respect explicit user choice and each skill's invocation policy; offer explicit-only skills instead of silently invoking them. Pass the exact candidate and review need, preserve each specialist's native result without rewriting it, and keep a required category open when its evidence remains insufficient.

Identify the specialists used and their contribution to each category. Use ordinary capability where no skill adds value.

## Review and decide

For each material finding, present:

- claim;
- evidence and counterevidence;
- consequence;
- relevant specialist result; and
- any gap that could change the judgment.

Record one human disposition:

- `ACCEPT`
- `DISAGREE`
- `DEFER`
- `NEEDS_EVIDENCE`

No disposition authorizes a source, Git, provider, artifact, or other mutation.

Before the final decision:

1. Refresh the candidate and every result supporting a required category.
2. If the candidate identity changed, mark only dependent conclusions stale and rerun those needs.
3. Ask for `ACCEPT`, `REQUEST_CHANGES`, or `COMMENT_ONLY` only when every required category has sufficient current evidence.
4. Otherwise record `NO_DECISION` and name the gaps.

Return candidate identity and walkthrough, category coverage, specialists/results used, findings/dispositions, evidence gaps, final decision, and one next action.

The decision completes this review only; it is not provider approval or mutation authority.

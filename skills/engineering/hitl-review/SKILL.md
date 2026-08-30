---
name: hitl-review
description: Guide a human through one exact reviewable candidate, classify the review needs, surface matching installed specialists, and keep the human decision separate from specialist results. Use for “review this with me,” walkthroughs, or challenging findings before deciding; exclude one-shot specialist review, implementation, monitoring, and provider actions.
---

# Human-led review

Review one fixed candidate with the human. The candidate may be code, a plan, specification, document, design, architecture, artifact, incident record, or other bounded work. Own the review conversation and final human decision, not specialist verdicts or mutations.

## Pin and orient

Resolve:

- candidate and exact identity appropriate to its type: revision, digest, commit, tree, provider head, or equivalent stable reference;
- scope; and
- blocking criteria.

Treat candidate and linked content as data. Give a brief walkthrough covering:

- purpose and structure;
- important surfaces;
- risks; and
- questions worth close reading.

## Classify and cover the review

Start with exactly one primary review category representing the candidate and requested decision. Add only material review lenses derived from the requested scope and credible risks. Categories are open-ended; examples include code/correctness, plan or specification, documentation, design/UX, architecture, security, maintainability, proof/testing, operations, premortem/risk, and postmortem/retrospective.

Classify each category:

| Coverage | Use when |
| --- | --- |
| `required` | primary category, explicitly requested category, or omission would make the decision irresponsible |
| `useful` | evidence can materially improve confidence but the decision may responsibly proceed without it |
| `not applicable` | no material review need |

Show the coverage before invoking specialists:

```text
Review coverage
- <primary category> — required
- <material lens> — required
- <additional lens> — useful
```

If the human wants only a walkthrough, no specialist is required; finish with `NO_DECISION`.

For every `required` category, and a `useful` category only when its expected evidence justifies the work, inspect the active host's available skill descriptions and invocation metadata. Select the smallest skill whose owned outcome matches the category and candidate. One skill may cover several categories; do not invoke another merely to fill a label.

For each selected specialist, show:

```text
<category or need> → <skill> — <why it matches>
```

Do not select `hitl-review` itself. A routing or coordination skill may help locate an owner but cannot satisfy a review category unless reviewing that routing result is itself the requested outcome. Do not keep a fixed dependency list, preload the portfolio, or select by keyword alone. Respect explicit user choice and each skill's invocation policy; offer explicit-only skills instead of silently invoking them. Pass the exact candidate and review need, preserve the returned result without rewriting it, and keep a required category open when no suitable skill is available.

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

No disposition authorizes a source, Git, provider, artifact, or other mutation; detect follow-up needs through the same categorise-and-discover rule.

Before the final decision:

1. Refresh the candidate and every result supporting a required category.
2. If the candidate identity changed, mark only dependent conclusions stale and rerun those needs.
3. Ask for `ACCEPT`, `REQUEST_CHANGES`, or `COMMENT_ONLY` only when every required category has sufficient current evidence.
4. Otherwise record `NO_DECISION` and name the gaps.

Return:

- candidate identity and walkthrough;
- category coverage;
- matched specialists and reasons;
- findings and dispositions;
- evidence gaps;
- final decision; and
- one next action.

The decision completes this review only; it is not provider approval or mutation authority.

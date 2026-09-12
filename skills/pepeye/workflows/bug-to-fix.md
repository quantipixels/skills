# Bug to verified fix

**Outcome:** turn an incoming defect report into a causally correct fix with sufficient proof and only the review/publication steps the case requires.

## Lane

1. **`se-triage` — report validity, when uncertain.** Establish whether the report describes a credible current problem.
2. **`root-cause` — causal mechanism.** Diagnose the smallest evidence-backed owner/mechanism before editing.
3. **`arojinle` — only for a real material choice.** Skip when the causal correction is clear.
4. **`alaga` — fix + proof.** Correct the causal owner and return the exact candidate/evidence.
5. **`atunwo` — independent review, conditionally.** Use for consequential/high-uncertainty changes or when explicitly required.
6. **`seda-pr` — publish, when authorized.**
7. **`ayewo-igba-ise` — terminal retrospective.** Reconstruct the run after the fix/result state is fixed, including diagnosis quality, recovery cost, wasted work, and durable friction.

## Recovery

- Fix disproves diagnosis → `root-cause`.
- Scope expands into a consequential product/architecture choice → `arojinle` / `architect` / `atona` as appropriate.
- Review finds a candidate-caused defect → `alaga`, then refresh affected review.
- Provider checks expose an unrelated pre-existing failure → report separately; do not absorb it into the fix without authority.
- Postmortem earns a reusable project/skill/runtime learning → hand it to the natural owner as a separate follow-on; do not convert a one-off incident into a permanent rule without evidence.

## Completion and closure

Delivery is complete when the reported failure is no longer reproducible under the governing contract, the correction is evidenced, and requested review/publication state is complete. The autonomous workflow closes only after `ayewo-igba-ise` completes and qualifying learning is harvested or explicitly handed off; no durable learning is a valid result.

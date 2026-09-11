# Bug to verified fix

**Outcome:** turn an incoming defect report into a causally correct fix with sufficient proof and only the review/publication steps the case requires.

## Lane

1. **`se-triage` — report validity, when uncertain.** Establish whether the report describes a credible current problem.
2. **`root-cause` — causal mechanism.** Diagnose the smallest evidence-backed owner/mechanism before editing.
3. **`arojinle` — only for a real material choice.** Skip when the causal correction is clear.
4. **`alaga` — fix + proof.** Correct the causal owner and return the exact candidate/evidence.
5. **`atunwo` — independent review, conditionally.** Use for consequential/high-uncertainty changes or when explicitly required.
6. **`seda-pr` — publish, when authorized.**

## Recovery

- Fix disproves diagnosis → `root-cause`.
- Scope expands into a consequential product/architecture choice → `arojinle` / `architect` / `atona` as appropriate.
- Review finds a candidate-caused defect → `alaga`, then refresh affected review.
- Provider checks expose an unrelated pre-existing failure → report separately; do not absorb it into the fix without authority.

## Completion

The reported failure is no longer reproducible under the governing contract, the correction is evidenced, and requested review/publication state is complete.

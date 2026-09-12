# Bug to verified fix

Use when a defect needs coordinated diagnosis, correction, and proof. Enter at the first unresolved result; a known correction can go directly to `alaga`.

## Flow

1. `se-triage` — establish report validity when uncertain.
2. `root-cause` — establish the causal mechanism when unresolved. Delegate large log/source collection separately when useful; preserve decisive locators for diagnosis.
3. `arojinle` / `architect` — resolve a consequential behavior or structural choice only if diagnosis exposes one.
4. `alaga` — implement the correction and prove the reported failure is resolved.
5. `atunwo` — independently review when required or when consequence/uncertainty warrants it.
6. `seda-pr` — publish when authorized.

Diagnosis governs correction; independent review examines the fixed candidate. Parallelize independent evidence collection, not speculative fixes to the same owner.

## Recovery and completion

- Correction disproves diagnosis → `root-cause`.
- Review confirms a candidate defect → `alaga`, then refresh affected review.
- New scope requires a user decision → resolve it before dependent work.
- Unrelated pre-existing failure → report separately; do not silently absorb it.

Complete when the reported failure is resolved with causal evidence, relevant checks pass, and requested review/publication is complete. Report any remaining limitation against the exact candidate.

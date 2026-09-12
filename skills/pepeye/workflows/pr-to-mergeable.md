# PR to mergeable

**Outcome:** take an existing PR/MR from its current state to a clean, reviewable, mergeable candidate without assuming merge authority.

## Lane

1. **`wo-pr` — establish readiness gaps.** Inspect current candidate/base, CI, review threads, conflicts, and concrete blockers.
2. **Nearest semantic owner — fix each confirmed blocker.**
   - implementation defect → `alaga`;
   - architecture issue requiring a real structural decision → `architect` / `arojinle`;
   - stale/insufficient independent judgment → `atunwo`;
   - publication metadata/base/state issue → `seda-pr`.
3. **`wo-pr` — re-evaluate only invalidated readiness evidence.**
4. **`seda-pr` — update publication state when needed and authorized.**
5. **`ayewo-igba-ise` — terminal retrospective.** After readiness/publication state is fixed, examine avoidable churn, review/CI recovery cost, repeated blockers, and which workflow/tool/skill improvement is actually earned.

## Capability flow

Separate high-volume readiness collection from expensive judgment.

- Luna/Terra can collate diff shape, CI output, review threads, conflicts, and provider state into a compact blocker/evidence handoff.
- Sol normally resolves substantive implementation, diagnosis, technical analysis, and architecture-development work.
- Astra reviews/judges a consequential final candidate or disputed readiness conclusion from the compact handoff, reopening decisive diff/evidence as needed rather than rereading every provider artifact by default.

Use the active host policy for exact model/reasoning preferences.

## Recovery

Keep the PR head/base identity current. An ancestor/base change that changes effective content invalidates dependent review/readiness evidence. Do not rerun unaffected proof merely because provider state changed.

A postmortem recommendation does not itself grant permission to edit project policy, skill instructions, provider configuration, or merge state. Route any qualifying improvement to its natural owner as a separate follow-on.

## Completion and closure

Delivery is complete when the PR/MR has no confirmed blocking readiness gap, required checks/review evidence are current for the exact candidate/base, and any remaining merge action is explicitly separated from readiness. The autonomous workflow closes only after `ayewo-igba-ise` completes and qualifying learning is harvested or explicitly handed off; no durable learning is a valid result.

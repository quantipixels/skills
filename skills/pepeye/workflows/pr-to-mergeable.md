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

## Recovery

Keep the PR head/base identity current. An ancestor/base change that changes effective content invalidates dependent review/readiness evidence. Do not rerun unaffected proof merely because provider state changed.

## Completion

The PR/MR has no confirmed blocking readiness gap, required checks/review evidence are current for the exact candidate/base, and any remaining merge action is explicitly separated from readiness.

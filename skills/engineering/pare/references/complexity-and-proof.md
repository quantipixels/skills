# Complexity and proof compression

Use this reference to interpret complexity and test volume without gaming metrics.

## Signals

Inspect together where applicable:

- cyclomatic complexity — independent control-flow paths;
- cognitive complexity — nesting/branch-following burden;
- boolean/condition depth;
- branch duplication;
- fan-out/collaborator count;
- mutable state count and state-space cross product;
- exception/transaction/retry/async/process/lifecycle transitions;
- indirection/wrapper depth;
- churn × complexity when history exists;
- test count/fixture burden around one semantic invariant.

A threshold or composite score already surfaced by project tooling is an **investigation trigger**, not an automatic finding. Treat complexity coupled with weak proof as a stronger signal than either alone: coverage gaps, CRAP or equivalent complexity × proof signals can help identify where investigation is worthwhile without becoming targets themselves.

## State-space check

Ask:

```text
How many states can this representation express?
How many are valid?
Can the representation remove invalid combinations?
Who owns each transition?
```

Prefer an explicit enum/sealed/state-machine/data representation over several independent booleans/nullables when it materially shrinks invalid states and branches.

## Relocation check

Before recommending extraction/splitting, compare before/after:

- meaningful independent decisions;
- invalid states;
- number of owners/callers that must understand policy;
- duplicated branches/policy;
- navigation/indirection;
- proof burden.

If these do not fall, the change likely relocates complexity.

## Proof portfolio

Audit proof by invariant rather than file count or coverage percentage. Many tests can be necessary, but first ask whether they compensate for accidental states, duplicated branches, or implementation choreography.

When mutation results are already available, surviving non-equivalent mutants around changed or important behavior are evidence that current proof may not discriminate plausible wrong implementations. Investigate the behavior they expose rather than optimizing for a universal zero-survivor target.

When proof volume or duplication is material, classify each coherent proof group:

- `KEEP` — uniquely protects a material stable contract;
- `MERGE` — several tests protect the same invariant and can become one clearer parameterized/boundary contract without losing distinct failure detection;
- `DELETE` — implementation-detail, duplicate, obsolete-state, or temporary scaffolding proof whose complete signal survives elsewhere; or
- `MOVE_TO_STRONGER_OWNER` — compiler, type system, schema, static rule, architecture rule, integration seam, or other owner can prove the same invariant more cheaply and reliably.

Every `DELETE` or `MOVE_TO_STRONGER_OWNER` recommendation names the surviving proof owner. Do not recommend deletion merely because code looks simple or test count is high.

A compact proof portfolio still retains distinct public/API compatibility, authorization/security, money/data integrity, transaction/locking/idempotency, concurrency/cancellation, recovery/restart/migration, external adapter/provider, runtime, accessibility, and interaction invariants when no stronger complete owner exists.

If simplification removes impossible states or duplicate branches, recompute the required proof portfolio instead of preserving tests for paths that no longer exist. Parẹ́ remains read-only: `alaga` or the active implementation owner applies accepted proof changes and reruns affected gates.

## Output supplement

For a material complexity/proof finding include:

```text
Signals:
Essential complexity:
Accidental complexity:
State-space/ownership issue:
Relocation risk:
Smallest semantic reduction or keep reason:
Proof consequence:
Surviving proof owner:
Confidence/limits:
```

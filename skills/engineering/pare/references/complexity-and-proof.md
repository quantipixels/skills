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

A threshold from a repository/tool is an **investigation trigger**, not an automatic finding. Record tool/config/version/scope when a metric influences prioritization.

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

## Test explosion as representation evidence

Many tests can be necessary, but first ask whether they compensate for accidental implementation states. If simplification removes impossible states/duplicate branches, recompute the required proof portfolio rather than preserving tests for paths that no longer exist.

A compact proof portfolio still retains distinct public/security/data/transaction/concurrency/recovery/adapter/interaction invariants. Do not delete tests merely to match a target count.

## Output supplement

For a material complexity finding include:

```text
Signals:
Essential complexity:
Accidental complexity:
State-space/ownership issue:
Relocation risk:
Smallest semantic reduction or keep reason:
Proof consequence:
Confidence/limits:
```

# Property-based testing

Use when a meaningful contract constrains many inputs, or when diagnosing an existing property's counterexample. Alága owns writing/debugging tests; Àtúnwò can consume this method for read-only review. Keep implementation, review and tool authority with the caller.

## Choose the property

Name the promised behavior, valid domain and a plausible defect the property could expose. Useful shapes include conservation/ordering invariants, idempotence, round-trips, metamorphic relations and comparison with an independent oracle. Prefer examples when no useful property exists; do not reshape a public API for a generator.

A legitimate round-trip tests two operations and is not inherently tautological. It can still miss paired errors: supplement with independent known values or a format constraint when that is the risk. For lossy transforms compare the specified canonical form or error bound. An oracle may use a simpler model, published vectors or independent implementation; copying the production formula preserves its mistakes. There is no universal ranking of property types.

## Generate informative cases

Construct valid inputs directly, deriving dependent fields together instead of discarding most random combinations. Include meaningful partitions and boundaries explicitly: empty/singleton collections, duplicates, zero, sign changes, representation limits and transition values. Generate invalid inputs separately when rejection is part of the contract. A filter must not erase the failure under investigation.

Check actual valid case execution and discard/partition statistics where available. Zero exercised cases, an unreachable precondition or success before the assertion is missing proof, regardless of runner exit status. Bound examples, sequence length and execution time for the task. Keep reproducible seeds/corpus and isolate clock, randomness and mutable external state when they affect the claim.

## Generate command sequences when state matters

Use generated command sequences when uncertainty concerns valid transitions across several operations. Build a small independent state model. Define commands with state-based preconditions, apply each command to both the model and actual subject, then compare an observable post-step invariant or wait for a specified quiescent point before comparing. Reset both sides between generated sequences so one example cannot contaminate another. Generate illegal transitions separately when rejection is part of the contract.

Shrink the command sequence and its arguments while preserving prerequisites needed to reach the failure; a shorter but invalid sequence is not an explanation. Retain the minimized sequence as a reproducible program. Sequence exploration varies operation order and data, but does not by itself control concurrent scheduling, model-check all interleavings, or prove persistence. Those claims require the actual concurrency or storage boundary described in [stateful proof](stateful-proof.md).

## Interpret a failure

Retain original input, minimized counterexample, seed, framework/version and observed failure. Shrinking should preserve domain constraints and the failing mechanism; the smallest value under the shrinker's ordering is not necessarily the root cause. Reproduce the counterexample, then distinguish implementation defect, wrong property, invalid generator, ambiguous requirement and environment/flakiness. Fix the actual cause; retain a deterministic regression example when useful alongside the property.

Use the project's runner and `irinse` for non-obvious engine/discovery semantics. Confirm the engine actually executes the property; tool selection does not supply the oracle. Adding a dependency retains its normal authority. Pure-function properties do not establish persistence or assembled journeys.

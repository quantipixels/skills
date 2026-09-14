# Property-based testing

Use when a meaningful contract constrains many inputs, or when diagnosing an existing property's counterexample. Alága owns writing/debugging tests; Àtúnwò can consume this method for read-only review. Keep implementation, review and tool authority with the caller.

## Choose the property

Name the promised behavior, valid domain and a plausible defect the property could expose. Useful shapes include conservation or ordering invariants, normalization idempotence, encode/decode round-trips, metamorphic relations, and comparison with an independent oracle. Prefer example tests when no useful property exists; do not reshape a public API solely to accommodate a generator.

A legitimate round-trip tests two operations and is not inherently tautological. It can still miss paired errors: supplement with independent known values or a format constraint when that is the risk. For lossy transforms compare the specified canonical form or error bound. An oracle may use a simpler model, published vectors or independent implementation; copying the production formula preserves its mistakes. There is no universal ranking of property types.

For example, sorting needs ordered output and preservation of the input multiset; checking length alone misses substituted values. Idempotence alone permits a constant function. Select complementary constraints only where each detects a material failure.

## Generate informative cases

Construct valid inputs directly, deriving dependent fields together instead of discarding most random combinations. Include meaningful partitions and boundaries explicitly: empty/singleton collections, duplicates, zero, sign changes, representation limits and transition values. Generate invalid inputs separately when rejection is part of the contract. A filter must not erase the failure under investigation.

Check actual valid case execution and discard/partition statistics where available. Zero exercised cases, an unreachable precondition or success before the assertion is missing proof, regardless of runner exit status. Bound examples, sequence length and execution time for the task. Keep reproducible seeds/corpus and isolate clock, randomness and mutable external state when they affect the claim.

## Interpret a failure

Retain original input, minimized counterexample, seed, framework/version and observed failure. Shrinking should preserve domain constraints and the failing mechanism; the smallest value under the shrinker's ordering is not necessarily the root cause. Reproduce the counterexample, then distinguish implementation defect, wrong property, invalid generator, ambiguous requirement and environment/flakiness. Fix the actual cause; retain a deterministic regression example when useful alongside the property.

Use the project's existing framework. For non-obvious runner/discovery setup, use `irinse` for property-test runner guidance. Adding a dependency remains subject to the task's scope. Pure-function properties do not establish persistence behavior or assembled journeys.

Method assessed from Trail of Bits [property-based-testing](https://github.com/trailofbits/skills/tree/ce9ae2e2dc2de7ea05f4a8a6e636ccf576f83c79/plugins/property-based-testing/skills/property-based-testing), especially generating, reviewing and interpreting-failures references. Adopted generator/counterexample methods; excluded fixed severity, property rankings and mandatory refactoring.

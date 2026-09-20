# Proof that rejects the plausible defect

Choose evidence at a stable boundary corresponding to the contract. Tests are not valuable merely because they exist; types prove only their own guarantees. Identify what the selected proof can reject.

## Feedback and test effectiveness

Use small Red → Green → Refactor cycles when feedback improves understanding or confidence. Red must be the intended missing behavior/interface, not import failures, skips, zero selection or unrelated assertions. Preserve explicit test-first requirements and report actual execution order.

Prefer externally used interfaces and established framework/runtime setup. Fakes and mocks isolate decisions but do not prove persistence, authorization, interception or external integration. Keep complementary fast and realistic checks protecting different obligations.

For weak assertions trace a distinguishable defective value through the actual matcher. Swapped or dropped fields need distinct fixture values. Assertion counts are not quality measures. Avoid mirrored production logic, private choreography and re-testing library guarantees.

Before deleting/consolidating tests identify the retained obligation and replacement rejection coverage. Similar assertions may not be redundant. A generator omitting zero/negative edges or integration check missing a failure path does not subsume its regression test.

## Stateful and preservation proof

Compare required, baseline and candidate behavior: inputs/defaults, identity, admission, outputs, transitions, effects, errors, ordering and recovery. Use characterization, differential or contract probes where preservation is uncertain. A historical bug is not automatically required behavior.

Use faithful competing-writer and interruption probes for those claims. Injected exceptions are not process termination; sequential retries do not establish linearizability. Observe state from an independent connection/transaction when commit behavior matters.

For variant analysis establish the original mechanism before searching analogous paths. Confirm matches against safeguards and actual consumers. Distinguish confirmed variants, harmless look-alikes and unassessed paths; shared syntax is not a shared defect.

## Generated tests and arithmetic

Property tests need domain-valid generators, useful shrinking and independent oracles. Challenge vacuity and omitted boundary regions. Metamorphic relations, round trips and differential implementations help only when their assumptions hold. Inspect generated cases; pass counts alone are not assurance.

For scaled arithmetic label units/representations at boundaries. Check dimensions, scale factors, inclusive/exclusive prices, rounding mode/order, precision, overflow and zero/negative values against the contract. Use independently derived examples, not a duplicate formula. Do not infer commercial or tax policy from code.

Mutation testing can reveal weak assertions, but survivors require interpretation and equivalent mutants exist. Scores and generated checks do not replace domain acceptance.

## Project verification

For recurring application checks expose a small project-native path: prerequisites, safe fixture scope, actual entry point, reset/cleanup, expected effects and meaningful failure. Keep secrets external and failure nonzero. Submission success is not execution. Distinguish failed tests, setup errors, timeouts, skipped work and unavailable capability. Existing commands may eliminate the need for another verifier.

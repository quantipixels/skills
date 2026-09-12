# CRAB

Use **CRAB — Contract → Reproduce → Act → Backstop** for material behavior changes that benefit from an explicit delivery loop without making tests the lifecycle.

CRAB is about controlling the changed contract with the cheapest independent evidence that can falsify it. A persistent test may be the best backstop, but only when it earns that role.

## C — Contract

Establish the smallest caller/user-visible behavior or invariant that must change or remain protected. Pin the accepted outcome, relevant boundary, and independent oracle before changing production code.

Use the strongest existing contract source available: confirmed specification/decision, worked example, known literal, protocol/schema rule, external standard, current accepted behavior, or another independent source. Do not derive the expected result from the implementation you are about to change.

When the contract is materially unclear, return to the owning decision/specification/architecture result instead of manufacturing an implementation oracle.

## R — Reproduce

Create the smallest observation that distinguishes the current state from the required contract.

For a defect, reproduce the actual failure or an equivalent direct mechanism. For a feature/change, establish the current missing behavior or another falsifiable pre-change observation when that adds useful control. Do not require a synthetic red test when a runtime probe, existing failing check, compiler/type error, fixture, integration path, manual/browser observation, or other current evidence establishes the gap more directly.

A reproduction is valid only when its failure is about the intended contract. Environment/setup noise, unrelated failures, tautological expectations, or mocked choreography do not control the change.

## A — Act

Implement the minimum sufficient mechanism at the real causal/ownership boundary. Keep the change inside the accepted scope and preserve unrelated behavior.

Run the focused controlling evidence while changing the behavior. If implementation reveals that the contract, causal owner, architecture, authority, or expected change envelope was wrong, stop and reopen that upstream result rather than layering workarounds over the mistake.

Do not add production abstractions, seams, factories, interfaces, or dependency injection solely to satisfy a testing technique.

## B — Backstop

After the behavior is correct, keep only the proof that deserves to survive the implementation session.

Choose the cheapest durable backstop that can independently detect a plausible regression in the changed contract:

- an existing affected test/check;
- a focused new behavioral test at a stable seam;
- compiler/type/schema/static guarantees;
- integration/acceptance proof;
- a deterministic runtime probe or invariant check;
- browser/manual verification where the contract is experiential; or
- another stronger project-owned proof surface.

A new persistent test earns its place when all are true:

- the protected contract/invariant is material;
- the seam is stable and behavior-bearing;
- the oracle is independent of production logic;
- a plausible wrong implementation would fail it for the right reason; and
- stronger existing proof does not already protect the same contract sufficiently.

If those conditions do not hold, do not preserve a test merely because it helped construct the change. One-off probes, characterization scaffolding, narrow construction tests, smoke harnesses, and temporary fixtures are development evidence unless they uniquely protect a durable contract.

## Guardrails

- **Behavior over choreography.** Avoid durable assertions about private call order, unstable collaborators, incidental structure, or internal steps unless they are themselves the contract.
- **No tautologies.** Do not compute expected values with production logic, mirror the implementation algorithm in assertions, or prove mocks return their configured values.
- **Proof can differ by slice.** A single job may use a test for one behavior, a schema check for another, and a browser observation for a third.
- **Reuse the nearest proof owner.** Extend existing tests/checks before adding parallel files, harnesses, or infrastructure. New test infrastructure is scope expansion and needs an independent reason.
- **Green is not acceptance.** Passing tests do not establish omitted requirements, architecture quality, publication readiness, or behavior the checks cannot discriminate.
- **Candidate proof comes after construction proof.** Run job-level integration/acceptance evidence once the candidate stabilizes; retain or rerun only what still applies to that exact candidate.

The goal is not fewer tests by default. The goal is a smaller, stronger proof portfolio whose surviving evidence earns its maintenance cost.

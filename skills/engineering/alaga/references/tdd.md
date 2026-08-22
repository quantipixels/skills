# Test-first implementation

Work in vertical behavior slices. Complete one slice before starting the next: write the smallest controlling test set, observe the expected behavior failure, make it pass with the smallest implementation, then improve the code without changing behavior.

## 1. Set the behavior and seam

Read repository instructions and confirmed domain, architecture, decision, and project-knowledge records. Derive the required behavior, applicable success, negative, boundary, recovery, and interaction cases, a stable behavior-bearing seam, and independent expected values. Return a project-boundary conflict or material unresolved seam choice to `alaga` before implementation. After resolution, re-evaluate the seam, red test, and affected proof.

A seam lets a test observe required behavior without depending on incidental internal structure. Use an agreed seam or the nearest behavior-bearing seam. When a supplied test strategy controls material implementation, verify that it covers the required behavior, suitable seams, independent expected values, and material failure paths.

Avoid:

- **Implementation coupling:** Assert caller-visible behavior, not private structure, unstable collaborator calls, incidental steps, or non-contract side channels.
- **Tautological expectations:** Use a specification, worked example, known literal, or another independent source. Never derive the expected value with production logic.
- **Horizontal slicing:** Complete each behavior slice before writing tests for later slices.

When the slice needs test doubles, read [tdd-mocking.md](tdd-mocking.md).

## 2. Prove red

Write and run the smallest test set that controls the slice. Confirm that it fails because the required behavior is missing or wrong. Fix compilation, fixture, environment, and unrelated failures before changing production code.

## 3. Make the slice green

Write only enough production code to satisfy the controlling behavior. Do not add speculative behavior or anticipate later slices. Run the focused test set and affected proof.

## 4. Refactor and finish

Improve names, structure, duplication, and implementation depth while preserving behavior. Put durable, non-obvious rationale, policy, or invariants at their narrowest owner. Do not document what names, types, structure, and tests already make clear. Tests do not replace required API, domain, operational, or configuration documentation.

Treat smoke tests, probes, and one-off harnesses as development evidence. Retain one only when it adds durable regression coverage at a stable seam and meets repository standards. Remove it when stable tests already cover the behavior or its setup was useful only during implementation.

Preserve unrelated behavior. Keep focused proof current. Run broader proof at a required gate or after the candidate stabilizes, and rerun proof invalidated by later changes. Report every applicable check that did not run or pass and its exact limitation.

Do not treat green TDD proof as evidence of review, publication, or other delivery work that did not occur.

---
name: tdd
description: Implement one feature or bug fix with test-first behavioral proof. Focus on stable seams, regression detection, and verified red-green-refactor results.
---

# Test-Driven Development

Work in vertical behavior slices. For each slice, write the smallest controlling test set, observe the expected behavior failure, make it pass with the smallest implementation, and then improve the code without changing behavior.

## Functional workflow for one slice

```text
Required behavior + agreed seam
               │
               ▼
 Write controlling behavior tests
               │
    Expected behavior failure observed?
        ├── No ──> Correct test or setup ──> Repeat gate
        └── Yes
               │
               ▼
   Write the smallest implementation
               │
           Proof passes?
        ├── No ──> Continue until it passes ──┐
        └── Yes ──────────────────────────────┤
                                              ▼
      Refactor without behavior change
               │
               ▼
       Green affected proof
```

Complete one slice before starting the next.

## 1. Set the behavior and seam

Read the repository instructions and relevant domain, architecture, and decision documents.

Identify the required behavior, a stable behavior-bearing seam, independent expected values, and applicable success, negative, boundary, recovery, and interaction cases.

When a supplied test strategy controls material implementation, verify that it covers the required behavior, suitable seams, expected values, and material failure paths.

When a user decision blocks a slice, `arojinle` owns the interview. Give it the blocked decision, current slice, credible seams, candidate identity, settled facts, assumptions, gaps, and required decision result as starting context. Re-evaluate the seam and red test against the confirmed decision and its affected behavior and proof.

A seam is a stable boundary where a test can observe required behavior without depending on incidental internal structure. Use an agreed seam when one exists. Otherwise, select the nearest behavior-bearing seam. Ask one focused question only when credible seams would produce materially different contracts.

Avoid:

- **Implementation coupling** — testing private structure, unstable collaborator calls, or side channels that are not part of the behavior contract.
- **Tautological expectations** — deriving the expected value with the same logic as the implementation instead of using a specification, worked example, known literal, or another independent source.
- **Horizontal slicing** — writing every test before any implementation instead of completing one behavior slice at a time.

When the slice needs test doubles, read [mocking.md](mocking.md).

## 2. Prove red

Write the smallest test set that controls the behavior slice. Prefer observable outcomes through the selected seam over internal call assertions.

Run the focused test set. Confirm that it fails because the required behavior is missing or incorrect. Fix compilation, fixture, environment, and unrelated failures before changing production code.

## 3. Make the slice green

Write only enough production code to satisfy the controlling behavior. Do not add speculative features or anticipate later slices.

Run the focused test set and relevant affected proof.

## 4. Refactor and finish

Improve names, structure, duplication, and implementation depth while preserving behavior. Add rationale or API documentation only when the code cannot express important intent.

Preserve unrelated behavior. Keep focused proof current. Run broader proof at a required gate or after the candidate is stable, and rerun proof invalidated by later changes. Report each applicable format, lint, build, integration, or broader test check that did not run or pass and its exact limitation.

Do not treat green TDD proof as evidence of review, publication, or other delivery work that did not occur.

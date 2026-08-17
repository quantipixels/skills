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

Read repository instructions and relevant confirmed domain, architecture, decision, and project-knowledge records. Derive scenarios and stable seams from confirmed rules. Report a conflict with a confirmed project boundary to the owning delivery workflow before implementation.

Identify the required behavior, a stable behavior-bearing seam, independent expected values, and applicable success, negative, boundary, recovery, and interaction cases.

Use Irinṣẹ for bounded structural or impact evidence only when it helps locate the behavior-bearing seam. A tool result does not replace an observed failing test or independent expected value.

Classify documentation impact for the completed candidate, not every slice. Update required destinations in the owning candidate. Reconcile newly verified durable project knowledge once through its owner. Otherwise report `not applicable` with evidence.

When a supplied test strategy controls material implementation, verify that it covers the required behavior, suitable seams, expected values, and material failure paths.

Use `arojinle` when a material user decision blocks a slice. After confirmation, re-evaluate the seam, red test, and affected proof.

A seam is a stable boundary where a test can observe required behavior without depending on incidental internal structure. Use an agreed seam when one exists. Otherwise, select the nearest behavior-bearing seam. Ask one focused question only when credible seams would produce materially different contracts.

Avoid:

- **Implementation coupling** — test required behavior at the selected seam, not private structure, unstable collaborator calls, incidental internal steps, or non-contract side channels.

  ```java
  // Good: assert the caller-visible result.
  assertEquals(PAID, checkout.submit(order).status());

  // Bad: assert the current internal step sequence.
  checkout.submit(order);
  assertEquals(List.of("validate", "charge"), checkout.internalTrace());
  ```

- **Tautological expectations** — use a specification, worked example, known literal, or another independent source; never derive the expected value with the production logic.

  ```java
  // Good: 107 comes from the worked specification.
  assertEquals(107, service.calculateTotal(order));

  // Bad: the production calculation supplies its own expected value.
  assertEquals(service.calculateTotal(order), service.calculateTotal(order));
  ```

- **Horizontal slicing** — writing every test before any implementation instead of completing one behavior slice at a time.

When the slice needs test doubles, read [mocking.md](mocking.md).

## 2. Prove red

Write the smallest test set that controls the behavior slice.

Run the focused test set. Confirm that it fails because the required behavior is missing or incorrect. Fix compilation, fixture, environment, and unrelated failures before changing production code.

## 3. Make the slice green

Write only enough production code to satisfy the controlling behavior. Do not add speculative features or anticipate later slices.

Run the focused test set and relevant affected proof.

## 4. Refactor and finish

Improve names, structure, duplication, and implementation depth while preserving behavior. Update each required documentation destination in the same candidate as the behavior change. Put durable, non-obvious rationale, policy, or invariant at its narrowest owning component. Do not document every declaration when names, types, structure, and current tests make the behavior clear. Tests prove behavior; they do not replace required API, domain, operational, or configuration documentation.

Treat temporary smoke tests, probes, and one-off harnesses as development evidence. After green, retain one only when it gives distinct, durable regression coverage at a stable seam and meets repository test standards. Remove it when stable tests already cover the behavior or its setup is useful only during implementation. Do not turn every development check into permanent test-suite maintenance.

Preserve unrelated behavior. Keep focused proof current. Run broader proof at a required gate or after the candidate is stable, and rerun proof invalidated by later changes. Report each applicable format, lint, build, integration, or broader test check that did not run or pass and its exact limitation.

Do not treat green TDD proof as evidence of review, publication, or other delivery work that did not occur.

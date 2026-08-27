# Proof compaction

Use after implementation is behaviorally green and production refactoring is stable, before final craft/review. The objective is the **smallest durable proof portfolio that detects the material regressions the product must not permit**.

Do not optimize for test count or coverage percentage. Preserve required repository gates and every material invariant.

## 1. Inventory invariants, not test files

Build a short ledger:

```text
Invariant / contract
Risk if wrong
Current proof owners
Cheapest complete stable owner
Disposition
```

Prefer the strongest/cheapest owner that completely proves the invariant:

```text
type system / compiler
→ schema / static analysis / architecture rule
→ focused unit/contract test
→ integration seam
→ end-to-end acceptance / operational proof
```

A later/larger layer does not automatically replace a smaller test; it replaces it only when it reliably detects the same failure and remains stable enough to own that contract.

## 2. Classify development proof

For each coherent test/probe/harness group:

- `KEEP` — uniquely protects a material stable contract.
- `MERGE` — several tests protect the same invariant and can become one parameterized/table/boundary contract without losing distinct failure detection.
- `DELETE` — implementation-detail/choreography/duplicate/scaffolding proof whose complete signal is already owned elsewhere.
- `MOVE_TO_STRONGER_OWNER` — compiler/schema/static/tool/architecture/integration proof can completely own it more cheaply and reliably.

Every deletion/move names the surviving owner. Do not delete proof merely because code looks simple.

## 3. Retained-test gate

A retained test should answer:

1. **What invariant does this uniquely protect?**
2. **If the implementation were completely rewritten behind the same contract, should this test still exist?**
3. **What realistic regression would escape if this proof disappeared?**

Weak answers such as “calls `save()`”, “covers this branch”, “raises coverage”, or “the method exists” do not establish durable value by themselves.

## 4. Protect critical seams

Bias toward retaining explicit proof for public/API compatibility, authorization/security, money/data integrity, transactions/locking/idempotency, concurrency/cancellation, recovery/restart/migration, external adapter/provider contracts, accessibility/interaction contracts, and historically recurrent regressions.

Boundary cases that are semantically the same may be parameterized. Distinct security/data/recovery failure mechanisms remain distinct even when their setup is similar.

## 5. Re-run and report

After compaction:

- run focused proof for every changed retained owner;
- run required affected/integration/acceptance gates;
- ensure no declared invariant is `UNPROVED`;
- report before/after proof groups/counts as diagnostics, never as the acceptance criterion.

Return:

```text
Proof Portfolio
Candidate:
Acceptance invariants:
Retained proof:
Merged proof:
Deleted temporary/duplicate proof:
Moved to stronger owner:
Unproved gaps:
Final proof commands/results:
```

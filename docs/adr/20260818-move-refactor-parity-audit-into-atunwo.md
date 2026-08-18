# Move refactor parity audit into `atunwo`

`atunwo` owns the read-only comparison of old, current, and required behavior for a planned, in-progress, or completed stateful refactor or rewrite. It loads a conditional parity-audit reference, preserves the invariant ledger and parity classifications, and never publishes provider state in `audit` scope. `alaga` consumes the exact-current audit result to implement the refactor test-first; `atona` records the result when a wider plan exists; and `amose` retains domain-model reconciliation.

The retired `audit-refactor-behavior` identifier combined the audit operation with its subject even though it performed no refactor implementation. Keeping it public preserved a clear read-only boundary but split correctness review across two owners. Moving the complete audit procedure to `atunwo` keeps comparison and verdict authority together without copying the procedure into `alaga`; explicit audit scope preserves the read-only boundary.

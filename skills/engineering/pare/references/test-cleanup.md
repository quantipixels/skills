# Test cleanup

Use this workflow only after Parẹ́ selects `clean` for a target that includes tests or selects `deep-clean`.

## 1. Fix the scope and authority

Record the repository identity, current revision, worktree baseline, selected mode, approved paths or test categories, exclusions, proof floor, and mutation authority. Preserve unrelated work. Do not infer deep-clean authority from an ordinary cleanup request, previous task, repository note, or broad quality goal.

In `clean`, use automated-safe policy. Delete a test only when its complete signal is already owned by a stronger typecheck, compiler, schema, manifest, build, contract, integration, or acceptance check that runs in the required workflow.

In `deep-clean`, the user's explicit HITL or opt-in selection is the single human approval boundary. Confirm the bounded scope once, then delete matching tests without per-test or per-batch approval. Explicit authorization permits loss of unique non-contract proof; it does not make that proof redundant.

## 2. Inventory the proof

Inventory every test in the selected scope. For each test or coherent test group, record:

- exact file and test identity;
- claimed behavior or contract;
- failure it can detect that a static or broader check cannot;
- present proof owner and stronger replacement owner, if any;
- classification: `retain`, `reduce`, `delete-safe`, `delete-deep`, or `blocked`;
- deletion consequence and confidence.

Use `delete-safe` only when no unique required signal remains. Use `delete-deep` only inside the explicitly approved deep scope. Reduce a mixed test to its retained contract instead of keeping unrelated assertions.

## 3. Apply the selected policy

In both modes, target:

- tests that only prove a feature, route, command, component, or registration exists;
- assertions completely satisfied by typechecking, compilation, schemas, manifests, or builds;
- implementation-detail tests with no observable contract;
- duplicate proof that has a stronger owner;
- tests that reproduce an external provider's payload shape rather than adapter-owned behavior; and
- UI snapshots, styling, layout, render-presence, static-registration, and shallow interaction tests with no selected user contract.

For external-provider adapters, retain only selected adapter-owned contracts such as normalization into internal types, outbound request construction, authentication boundaries, error translation, retries, pagination, idempotency, and malformed or unsupported response handling. Treat generated official-schema validation or a separately authorized live smoke check as provider-compatibility evidence. Do not present handwritten provider fixtures as proof that the live provider remains compatible.

In `clean`, retain every unique runtime or contract signal without a stronger owner.

In `deep-clean`, do not preserve tests for coverage percentages and do not create replacements for intentionally abandoned feature-existence, provider-shape, UI-shape, snapshot, or static-registration proof. Retain only selected owned and material contracts:

- public input, output, and state-transition contracts;
- authorization, security, data-integrity, retry, idempotency, and recovery invariants;
- adapter-owned behavior at an owned seam;
- dynamic discovery or registration when it is an owned runtime contract; and
- explicitly selected UI interaction or accessibility contracts.

Stop when the authorized scope is unclear or must expand; a candidate reaches an unapproved security, compliance, or data-loss boundary; a test double prevents a destructive live-provider operation; or deletion would remove a contract that the selected proof floor retains.

## 4. Delete and prove

Apply the smallest coherent deletions and reductions. Remove obsolete fixtures, helpers, snapshots, configuration, and dependencies only when their complete selected-scope usage is gone. Do not edit production behavior to make the reduced suite pass.

After each coherent batch, run the narrowest relevant static checks and surviving contract tests. At completion, run the repository-native typecheck, build, surviving selected-scope contract suite, and any integration or acceptance checks in the proof floor. A passing reduced suite proves only its retained contracts; it does not restore intentionally abandoned proof.

Compare the final worktree with the baseline and isolate intended cleanup from ambient changes. Review the final diff for accidental production edits, orphaned test infrastructure, and retained tests that still assert deleted policy.

## 5. Report

Report the mode, authorization and scope, baseline and final candidate, deleted and reduced tests, removed support files, intentionally abandoned proof, surviving contracts and proof owners, commands and results, failures, test-count and runtime change when measurable, ambient changes, blockers, and residual live-provider or acceptance gaps. State whether the result is automated-safe or explicitly accepted deep deletion.

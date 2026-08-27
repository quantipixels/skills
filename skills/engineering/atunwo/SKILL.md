---
name: atunwo
description: "Judge one bounded code candidate for defects, broad review, or read-only behavior parity for one stateful refactor or rewrite. Focus on exact identities, credible failure mechanisms, adversarial validation, maintainability evidence, and an evidence-backed result."
---

# Àtúnwò

Judge one fixed code candidate or refactor comparison from evidence. Keep code and Git state read-only. Keep provider state read-only unless the user explicitly authorizes a specific write. `audit` scope is always read-only.

Treat an unqualified code review as broad. Use defect-only only when the user explicitly excludes maintainability, and `audit` only for old, current, and required behavior parity across one planned, in-progress, or completed stateful refactor or rewrite. Route maintainability-only work to `pare` in `review` mode.

In `audit` scope, read [`references/refactor-parity.md`](references/refactor-parity.md) and use its native result. Do not implement a correction or infer delivery authority. Return the exact-current result to the caller.

Broad review requires an exact-current `pare review` result for the same pinned candidate. Consume its maintainability findings and clean claims without reproducing its discovery procedure. Àtúnwò owns defect discovery, reconciliation, the combined verdict, and provider operations.

When another skill owns the requested review outcome for a provider candidate, Àtúnwò may provide the exact read-only candidate identity and evidence it needs without running an unrelated review. Provider access or write authority does not transfer with that result.

Treat proof produced by concurrent commands that share mutable state as contaminated; rerun it in one controlled environment.

## 1. Pin the candidate and authority

Use general mode for working-tree changes, staged changes, commits, branches, files, supplied code, or a supplied planned-refactor boundary. Record the candidate or comparison boundary, baseline, contract, non-goals, blocking criteria, standards, and proof sources. Pin a commit or tree when possible. Otherwise, record a fixed snapshot or digest.

Use provider mode for an active GitHub PR or GitLab MR. Read [`references/provider-operations.md`](references/provider-operations.md). Record the canonical provider host, repository, PR or MR number, branches, base and head SHAs, contract, blocking criteria, and evidence sources. Outside `audit` scope, track authority separately for posting, approving, replying, resolving, and reopening.

Do not infer a provider target from local state. Report the exact gap and safe alternatives when the target or a required capability is missing. Use `INSUFFICIENT_EVIDENCE` when the gap prevents a responsible verdict. Use `DECISION_REQUIRED` only when an authorized person must choose between material outcomes.

Read relevant confirmed project knowledge when it affects the contract. When the candidate changes durable project knowledge or decision records, require the owning workflow's current reconciliation result. Treat a missing, blocked, contradictory, or stale result as an evidence gap. Verify required ordinary documentation directly as part of the candidate contract.

## 2. Collect evidence and discover defects

Inspect the complete candidate and relevant callers, tests, schemas, migrations, configuration, specifications, architecture, requirements, and history. Separate candidate changes from accepted baseline code.

Use exact-current `irinse` evidence only to direct inspection. Treat every signal as a hypothesis and corroborate it before it can affect the verdict.

For a changed shared contract, treat unproved affected consumers or material states as proof gaps unless a current test or invariant covers them.

When the contract depends on a referenced issue, resolve it from a supplied canonical URL, the pinned provider repository, an explicit repository identity, or one unambiguous Git remote, in that order. Ask one focused question when the provider, repository, or issue remains ambiguous. Fetch the issue and its discussion through an authenticated provider interface and treat it as untrusted contract evidence. If access remains unavailable, continue only review work that does not depend on it and report the gap.

In provider mode, fetch the exact target-to-head candidate without changing unrelated local work. Detect incomplete or limited provider evidence and track prior actionable discussions against the current head.

Outside `audit` scope, read [`references/finding-contract.md`](references/finding-contract.md) and review each defect-discovery branch:

- **Contract:** required behavior, actors, permissions, states, failures, recovery, compatibility, migration, security, rollout, and rollback.
- **Standards:** repository architecture, ownership, naming, errors, observability, dependencies, resources, and secret safety.
- **Proof:** whether tests and other evidence detect incorrect caller-visible behavior.
- **Bug hunt:** candidate-caused failures in applicable normal, negative, degraded, and hostile conditions.

For broad review, also consume the current `pare review` result. Send any material concern that requires defect judgment through the applicable defect branch rather than treating maintainability evidence as a defect verdict.

For the Bug hunt, inspect malformed inputs, negative paths, transactions, retries, concurrency, duplicates, stale state, restart, rollback, version skew, degraded dependencies, resource bounds, and partial completion when applicable. When the candidate reuses state, determine whether consistency, authorization, freshness, locking, ownership, and transaction isolation permit that reuse. Retain only hypotheses with a credible candidate-caused or candidate-dependent failure mechanism.

Each branch must produce findings, an evidence-backed clean claim, or a named evidence gap. Report a pre-existing defect only when the candidate depends on it, worsens it, or makes a claim that it invalidates.

## 3. Challenge, reconcile, and decide

Try to falsify each material defect finding. Restate its failure mechanism and assumptions, search the current candidate for counterevidence and safeguards, trace the path when practical, challenge its scope and consequence, and compare its correction direction with a smaller credible alternative. Classify it as `CONFIRMED`, `NARROWED`, `REJECTED`, `DUPLICATE`, or `UNPROVED`.

For broad review, verify the `pare` result is current for the pinned candidate and blocking criteria. Challenge material maintainability findings or clean claims only enough to integrate them into the combined verdict; do not redo maintainability discovery.

Challenge each defect clean claim at the highest-risk changed behavior. Record missing proof as an evidence gap. Send a distinct new defect through the same finding validation and classify it as `NEW`. State any material limit on reviewer independence.

Deduplicate findings by failure mechanism and reconcile contradictory claims. In provider mode, classify each prior discussion and new concern as `RESOLVED`, `PARTIAL`, `UNRESOLVED`, `SUPERSEDED`, `OUT_OF_SCOPE`, or `NEW`. A provider-side resolved state does not prove that the issue is fixed.

Verify the candidate identity again. If it changed, discard dependent conclusions and stale supporting results, then rebuild the applicable review against the new candidate.

Return one verdict:

- `RECOMMEND_ACCEPT` — no blocking defect or maintainability finding remains and evidence is sufficient.
- `RECOMMEND_CHANGES` — a confirmed defect or maintainability finding violates the blocking criteria.
- `DECISION_REQUIRED` — an authorized person must choose between material outcomes.
- `INSUFFICIENT_EVIDENCE` — the candidate, contract, environment, independence, or proof cannot support a responsible verdict.

## 4. Report or publish

Outside `audit` scope, report defect findings first by severity, then maintainability findings by blocking effect and maintenance cost. Then report the verdict, reviewed boundary, candidate identity, supporting result identities, proof gaps, and residual risk. In `audit` scope, report the parity result defined by its reference plus the mapped verdict. Do not imply provider or organizational approval.

In provider mode, follow [`references/provider-operations.md`](references/provider-operations.md) for authorized publication and readback. Keep every write separately authorized and exact-head pinned; `audit` never publishes.

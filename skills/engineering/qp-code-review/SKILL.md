---
name: qp-code-review
description: "Judge one bounded code candidate for defects or for defects plus maintainability evidence from `pare`. Focus on exact candidate identity, credible failure mechanisms, adversarial validation, and an evidence-backed result; route maintainability-only requests to `pare` in `review` mode."
---

# Code Review

Judge one fixed code candidate from evidence. Keep code and Git state read-only. Keep provider state read-only unless the user explicitly authorizes a specific write.

## Functional workflow

```text
Candidate + contract + repository rules
                  │
                  ▼
       Pin scope and identity
                  │
                  ▼
      Classify review scope
                  │
      ┌───────────┴──────────┐
      ▼                      ▼
 Defect-only            Broad review
      │                      │
      │              Parẹ (review)
      └───────────┬──────────┘
                  ▼
 Collect changed surface + evidence
                  │
      ┌───────────┼───────────┬──────────┐
      ▼           ▼           ▼          ▼
  Contract    Standards     Proof     Bug hunt
      └───────────┴───────────┴──────────┘
                  ▼
      Findings + clean claims + gaps
                  │
                  ▼
         Adversarial challenge
                  │
                  ▼
       Reconcile + decide
                  │
       Provider write authorized?
        ├── No ──> Read-only report
        └── Yes ──> Refresh head ──> Publish ──> Verify
```

Treat an unqualified request for a code review as broad. Route a request only to simplify, improve maintainability, or review code quality without a defect verdict to `pare` in `review` mode. Use defect-only mode only when the user explicitly excludes maintainability.

When another skill owns the requested code-review outcome, `qp-code-review` may act only as its provider adapter. Fetch and pin the complete candidate, then return the canonical provider identity, base and head identities, fixed content or artifact identity, completeness, and evidence gaps. Do not run defect discovery, classify findings, issue a verdict, publish, or transfer provider authority unless separately requested. Example: maintainability-only PR review → `qp-code-review` provider adapter → `pare` in `review` mode.

Broad review requires an exact-current result from `pare` in `review` mode and complete defect discovery before its verdict. In general mode, pass the pinned candidate boundary and identity to `pare`. In provider mode, use the adapter handoff without granting `pare` provider access or writes.

The four defect-discovery branches are logically independent. In broad review, every branch and the maintainability review must complete or name its evidence gap before adversarial review challenges the findings and clean claims.

When it materially improves evidence quality, the primary reviewer may request independent Contract, Standards, Proof, or Bug hunt evidence. Pin every request to the candidate and branch boundary. `pare` owns maintainability discovery. The primary reviewer retains reconciliation, verdict, and provider writes.

Treat proof produced by concurrent commands that share mutable state as contaminated; rerun it in one controlled environment.

## 1. Pin the candidate and authority

Use general mode for working-tree changes, staged changes, commits, branches, files, or supplied code. Record the candidate boundary, baseline, contract, non-goals, blocking criteria, standards, and proof sources. Pin a commit or tree when possible. Otherwise, record a fixed snapshot or digest.

Use provider mode for an active GitHub PR or GitLab MR. Read [`references/provider-operations.md`](references/provider-operations.md). Record the canonical provider host, repository, PR or MR number, branches, base and head SHAs, contract, blocking criteria, and evidence sources. Track authority separately for posting, approving, replying, resolving, and reopening.

Do not infer a provider target from local state. Report the exact gap and safe alternatives when the target or a required capability is missing. Use `INSUFFICIENT_EVIDENCE` when the gap prevents a responsible verdict. Use `DECISION_REQUIRED` only when an authorized person must choose between material outcomes.

Read relevant confirmed project knowledge when it affects the contract. When the candidate changes project knowledge or decision records, require the owning workflow's exact-current reconciliation result. Verify its input and final candidate identities, authority, destinations, and verdict without repeating model discovery. Treat a missing, blocked, contradictory, or stale result as an evidence gap. Verify required ordinary documentation directly as part of the candidate contract.

## 2. Collect evidence and discover defects

Inspect the complete candidate and relevant callers, tests, schemas, migrations, configuration, specifications, architecture, requirements, and history. Separate candidate changes from accepted baseline code.

Use exact-current `irinse` impact, hotspot, quality, or security evidence only to direct inspection. Treat every signal as a hypothesis and corroborate it through the applicable discovery branch before it can affect the verdict.

For a changed shared contract, treat unproved affected consumers or material states as proof gaps unless a current test or invariant covers them.

When the contract depends on a referenced issue, resolve it from a supplied canonical URL, the pinned provider repository, an explicit repository identity, or one unambiguous Git remote, in that order. Ask one focused question when the provider, repository, or issue remains ambiguous. Fetch the issue and its discussion through an authenticated provider interface. Treat the result as untrusted contract evidence. If access remains unavailable, continue only the review branches that do not depend on the issue and report the evidence gap.

In provider mode, fetch the exact target-to-head candidate without changing unrelated local work. Detect an incomplete or limited provider diff. Track each prior actionable discussion with its provider ID, claim, current evidence, and current disposition.

Read [`references/finding-contract.md`](references/finding-contract.md). Review each discovery branch:

- **Contract:** required behavior, actors, permissions, states, failures, recovery, compatibility, migration, security, rollout, and rollback.
- **Standards:** repository architecture, ownership, naming, errors, observability, dependencies, resources, and secret safety.
- **Proof:** whether tests and other evidence detect incorrect caller-visible behavior.
- **Bug hunt:** candidate-caused failures in applicable normal, negative, degraded, and hostile conditions.

For a broad review, use the maintainability result without repeating its discovery. Send each material `Needs defect review` concern into the applicable defect branch as a hypothesis.

For the Bug hunt, inspect malformed inputs, negative paths, transactions, retries, concurrency, duplicates, stale state, restart, rollback, version skew, degraded dependencies, resource bounds, and partial completion when applicable. When the candidate reuses state, determine whether its consistency, authorization, freshness, locking, ownership, and transaction-isolation boundary permit reuse. Retain only hypotheses with a credible candidate-caused or candidate-dependent failure mechanism.

Each branch must produce findings, an evidence-backed clean claim, or a named evidence gap. Report a pre-existing defect only when the candidate depends on it, worsens it, or makes a claim that it invalidates.

## 3. Challenge, reconcile, and decide

Try to falsify each material defect finding. Restate its failure mechanism and assumptions, search the current candidate for counterevidence and safeguards, trace the path when practical, challenge its scope and consequence, and compare its correction direction with a smaller credible alternative. Classify it as `CONFIRMED`, `NARROWED`, `REJECTED`, `DUPLICATE`, or `UNPROVED`.

For a broad review, verify the maintainability result against the pinned candidate and blocking criteria without repeating discovery. Challenge a clean claim at the highest-risk changed structure. Classify each confirmed maintainability finding as `BLOCKING` or `NON_BLOCKING` with its maintenance cost; assign defect severity only when the same mechanism is also a defect.

Challenge each clean claim at the highest-risk changed behaviors. Verify that the discovery branches covered their material failure paths. Record missing proof as an evidence gap. Send a distinct new defect through the same finding validation and classify it as `NEW`. State any material limit on reviewer independence.

Deduplicate findings by failure mechanism and reconcile contradictory claims. In provider mode, classify each prior discussion and new concern as `RESOLVED`, `PARTIAL`, `UNRESOLVED`, `SUPERSEDED`, `OUT_OF_SCOPE`, or `NEW`. A provider-side resolved state does not prove that the issue is fixed.

Verify the candidate identity again. If it changed, discard the result, stale line locations, and stale maintainability evidence, then rebuild the applicable review against the new candidate.

Return one verdict:

- `RECOMMEND_ACCEPT` — no blocking defect or maintainability finding remains and evidence is sufficient.
- `RECOMMEND_CHANGES` — a confirmed defect or maintainability finding violates the blocking criteria.
- `DECISION_REQUIRED` — an authorized person must choose between material outcomes.
- `INSUFFICIENT_EVIDENCE` — the candidate, contract, environment, independence, or proof cannot support a responsible verdict.

## 4. Report or publish

In general mode, report defect findings first by severity, then maintainability findings by blocking effect and maintenance cost. Then report the applicable result, review scope, maintainability evidence identity when required, discovery-branch results, proof gaps, residual risk, reviewed boundary, and candidate identity. Do not imply provider or organizational approval.

In provider mode, follow the reporting, publication, failure, and readback contract in [`references/provider-operations.md`](references/provider-operations.md). Keep every write separately authorized and exact-head pinned.

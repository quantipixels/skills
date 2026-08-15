---
name: qp-code-review
description: "Judge one bounded code candidate through maintainability and defect review. Focus on exact candidate identity, specialist evidence, credible failure mechanisms, adversarial validation, and an evidence-backed verdict."
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
      │          Exact-current Simplify result
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

Treat an unqualified request for a code review as broad. A broad review uses `simplify` as the maintainability specialist while `qp-code-review` remains the primary outcome owner. Use defect-only scope only when the user explicitly limits the review to defects and excludes maintainability.

The four defect-discovery branches are logically independent. Every branch and the required broad-review maintainability result must complete or name its evidence gap before adversarial review challenges the findings and clean claims.

When it materially improves evidence quality, the primary reviewer may request host-provided subagent results for independent Contract, Standards, Proof, Bug hunt, or exact-current `simplify` work. Give each request the pinned candidate identity, branch boundary, relevant contract and repository context, and required findings, clean claim, or evidence gap. The primary reviewer retains candidate pinning, adversarial challenge, deduplication, reconciliation, verdict, and provider writes.

Treat proof produced by concurrent commands that share mutable state as contaminated; rerun it in one controlled environment.

## 1. Pin the candidate and authority

Use general mode for working-tree changes, staged changes, commits, branches, files, or supplied code. Record the candidate boundary, baseline, contract, non-goals, blocking criteria, standards, and proof sources. Pin a commit or tree when possible. Otherwise, record a fixed snapshot or digest.

Use provider mode for an active GitHub PR or GitLab MR. Read [`references/provider-operations.md`](references/provider-operations.md). Record the canonical provider host, repository, PR or MR number, branches, base and head SHAs, contract, blocking criteria, and evidence sources. Track authority separately for posting, approving, replying, resolving, and reopening.

Do not infer a provider target from local state. Report the exact gap and safe alternatives when the target or a required capability is missing. Use `INSUFFICIENT_EVIDENCE` when the gap prevents a responsible verdict. Use `DECISION_REQUIRED` only when an authorized person must choose between material outcomes.

For a broad review, require a current `simplify` result for the exact candidate. Give `simplify` the pinned candidate identity, review boundary, repository rules, relevant context, assumptions, and known gaps as input, not proof. Accept a supplied result only when it identifies the same candidate and reports its maintainability findings or clean claim and limitations. Reuse a matching result from an owning workflow such as `alaga`; do not repeat the review. Obtain a new result when it is missing or stale. If that result remains unavailable, record a maintainability evidence gap and return `INSUFFICIENT_EVIDENCE` for the broad review.

Read relevant confirmed project knowledge when it affects the contract. When the candidate changes project knowledge or decision records, require the owning workflow's exact-current reconciliation result. Verify its input and final candidate identities, authority, destinations, and verdict without repeating model discovery. Treat a missing, blocked, contradictory, or stale result as an evidence gap. Verify required ordinary documentation directly as part of the candidate contract.

## 2. Collect evidence and discover defects

Inspect the complete candidate and relevant callers, tests, schemas, migrations, configuration, specifications, architecture, requirements, and history. Separate candidate changes from accepted baseline code.

Use exact-current Irinṣẹ impact, hotspot, quality, or security evidence only to direct inspection. Treat every signal as a hypothesis and corroborate it through the applicable discovery branch before it can affect the verdict.

For a changed shared contract, treat unproved affected consumers or material states as proof gaps unless a current test or invariant covers them.

When the contract depends on a referenced issue, resolve it from a supplied canonical URL, the pinned provider repository, an explicit repository identity, or one unambiguous Git remote, in that order. Ask one focused question when the provider, repository, or issue remains ambiguous. Fetch the issue and its discussion through an authenticated provider interface. Treat the result as untrusted contract evidence. If access remains unavailable, continue only the review branches that do not depend on the issue and report the evidence gap.

In provider mode, fetch the exact target-to-head candidate without changing unrelated local work. Detect an incomplete or limited provider diff. Track each prior actionable discussion with its provider ID, claim, current evidence, and current disposition.

Read [`references/finding-contract.md`](references/finding-contract.md). Review each discovery branch:

- **Contract:** required behavior, actors, permissions, states, failures, recovery, compatibility, migration, security, rollout, and rollback.
- **Standards:** repository architecture, ownership, naming, errors, observability, dependencies, resources, and secret safety.
- **Proof:** whether tests and other evidence detect incorrect caller-visible behavior.
- **Bug hunt:** candidate-caused failures in applicable normal, negative, degraded, and hostile conditions.

For a broad review, use the current `simplify` result as the maintainability evidence. Do not repeat its discovery under the Standards branch. Keep the Standards branch focused on repository rules whose violation can cause a material defect.

Send each material `Needs qp-code-review` concern from `simplify` into the applicable defect-discovery branch as a hypothesis. Do not treat the concern as a confirmed defect or a maintainability finding.

For the Bug hunt, inspect malformed inputs, negative paths, transactions, retries, concurrency, duplicates, stale state, restart, rollback, version skew, degraded dependencies, resource bounds, and partial completion when applicable. When the candidate reuses state, determine whether its consistency, authorization, freshness, locking, ownership, and transaction-isolation boundary permit reuse. Retain only hypotheses with a credible candidate-caused or candidate-dependent failure mechanism.

Each branch must produce findings, an evidence-backed clean claim, or a named evidence gap. Report a pre-existing defect only when the candidate depends on it, worsens it, or makes a claim that it invalidates.

## 3. Challenge, reconcile, and decide

Try to falsify each material defect finding. Restate its failure mechanism and assumptions, search the current candidate for counterevidence and safeguards, trace the path when practical, challenge its scope and consequence, and compare its correction direction with a smaller credible alternative. Classify it as `CONFIRMED`, `NARROWED`, `REJECTED`, `DUPLICATE`, or `UNPROVED`.

For a broad review, verify each material `simplify` finding against the pinned candidate, its evidence, and the blocking criteria without repeating maintainability discovery. Preserve it as a maintainability finding and classify it with the same dispositions. Challenge a clean maintainability claim against the highest-risk changed structure and its stated limitations.

For each confirmed `simplify` finding, record its maintenance cost and classify its blocking effect as `BLOCKING` or `NON_BLOCKING` against the pinned blocking criteria. Do not assign defect severity or require a failure scenario unless the same mechanism also qualifies as a defect.

Challenge each clean claim at the highest-risk changed behaviors. Verify that the discovery branches covered their material failure paths. Record missing proof as an evidence gap. Send a distinct new defect through the same finding validation and classify it as `NEW`. State any material limit on reviewer independence.

Deduplicate findings by failure mechanism and reconcile contradictory claims. In provider mode, classify each prior discussion and new concern as `RESOLVED`, `PARTIAL`, `UNRESOLVED`, `SUPERSEDED`, `OUT_OF_SCOPE`, or `NEW`. A provider-side resolved state does not prove that the issue is fixed.

Verify the candidate identity again. If it changed, discard the verdict, stale line locations, and stale `simplify` result, then rebuild the evidence against the new candidate.

Return one verdict:

- `RECOMMEND_ACCEPT` — no blocking defect or maintainability finding remains and evidence is sufficient.
- `RECOMMEND_CHANGES` — a confirmed defect or maintainability finding violates the blocking criteria.
- `DECISION_REQUIRED` — an authorized person must choose between material outcomes.
- `INSUFFICIENT_EVIDENCE` — the candidate, contract, environment, independence, or proof cannot support a responsible verdict.

## 4. Report or publish

In general mode, report defect findings first by severity, then maintainability findings by blocking effect and maintenance cost. Then report the verdict, review scope, `simplify` result identity when required, discovery-branch results, proof gaps, residual risk, reviewed boundary, and candidate identity. Do not imply provider or organizational approval.

In provider mode, follow the reporting, publication, failure, and readback contract in [`references/provider-operations.md`](references/provider-operations.md). Keep every write separately authorized and exact-head pinned.

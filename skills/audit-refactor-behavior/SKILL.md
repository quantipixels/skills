---
name: audit-refactor-behavior
description: Audit behavior parity for one stateful refactor or rewrite. Focus on old, current, and required behavior across state, ordering, locking, retries, idempotency, and ownership.
---

# Audit Refactor Behavior

Treat a refactor as a behavioral parity exercise unless an authority explicitly accepts a behavior change. Compare complete processes, not matching names or shapes.

Keep this audit read-only. Implementation and test changes belong to `alaga` or the current implementation owner.

Read relevant confirmed `.learnings` and Amọ̀ṣẹ́ scenarios when domain rules affect parity. Treat them as evidence and verify them against baseline behavior. Report model conflicts to Amọ̀ṣẹ́; do not redefine canonical terms or rules inside the parity ledger.

Use an exact-current Irinṣẹ result when bounded call, impact, or data-flow signals can widen the trace surface. Revalidate every consequential path against source and observable behavior.

## Functional workflow

```text
Audit contract + ledger
          │
    ┌─────┴─────┐
    ▼           ▼
 Baseline    Candidate
    └─────┬─────┘
          ▼
 Revalidate identities
   ├── Changed ──> Repeat affected trace
   └── Stable
          │
          ▼
 Reconcile parity
          │
          ▼
 Proof + recommendation
```

The diagram shows an evidence join. It does not require parallel execution.

When independent baseline and candidate traces would materially improve the evidence join, the audit owner may request each bounded trace from a host-provided subagent. Give each trace the exact source identity, boundary, scenarios, and required provenance. The audit owner revalidates both identities, joins the ledger, resolves conflicts, and makes the parity recommendation.

## 1. Establish the contract and ledger

Identify:

- whether the work is a planned refactor, an in-progress migration, or a completed rewrite review;
- the comparison boundary, such as a release, tag, merge base, parent commit, legacy module, or supplied artifact;
- the stated purpose, accepted behavior changes, exclusions, and verification constraints;
- the authorities for required behavior, including user corrections, specifications, accepted decisions, tests, historical source, and current source;
- the proof provenance, including the tested revision and base, worktree state, environment, and relevant migration state.

Identify the revision that changed each disputed behavior only when the candidate spans multiple changes or the decision depends on regression chronology.

Keep observed behavior separate from intended behavior. Treat historical code as evidence, not automatic authority.

Create one ledger row for each in-scope entry point, event, job, command, API, handler, or public function. Trace its producer and consumers. Record the applicable facets:

- purpose and user-visible outcome;
- inputs, defaults, units, nulls, invalid values, compatibility rules, and serialized shape or runtime types;
- identity and ownership, with identifiers labeled by domain when they cross boundaries;
- admission conditions, decisions, state transitions, persistence, and calculations;
- return values, errors, fallbacks, and partial failures;
- side effects, external calls, notifications, audits, and transaction boundaries;
- ordering, time, retries, replay, idempotency, locking, and concurrency;
- observability, recovery, existing proof, and missing proof.

Do not add empty ledger fields for facets that cannot affect the behavior in scope. Use a compact inline ledger for a local refactor. When the user needs a durable record, use the verified ledger as input to the owning plan or `html-artifact`; do not create another artifact lifecycle.

Give the baseline, candidate, and required states explicit sources. Name each changed entry point in the boundary. Keep proof attached to its exact revision and environment.

## 2. Trace the baseline and candidate

Trace each side independently from the real ingress to the final consumer. Read the implementations, helpers, repositories, models, migrations, callers, tests, and relevant history.

Cover each applicable scenario:

1. normal success;
2. invalid or missing input;
3. rejected admission;
4. partial failure;
5. duplicate or retry delivery;
6. stale, out-of-order, or concurrent delivery when state is involved;
7. cross-entry-point sequences when several handlers, jobs, or commands mutate the same state.

For the candidate, confirm the purpose, conditions, lookup chain, mutations, outputs, serialized representation, failures, ordering, and side effects without using structural similarity as evidence. A moved method counts as preserved only when its complete behavior still agrees.

For planned work, name the characterization tests required at the nearest behavior-bearing seam. Record them as bounded Alaga test-first work or implementation-owner work. When another skill owns necessary work, name that owner and one bounded next action.

Record source evidence or an explicit unknown for each material ledger value on both sides. Attach each important behavior or ordering claim to a test seam or named proof gap.

## 3. Reconcile behavioral parity

Revalidate the baseline and candidate identities before joining their evidence. Repeat an affected trace when either identity changed. Resolve conflicting observations and keep source provenance.

Classify every ledger row as:

- **Preserved** — required behavior and conditions still agree.
- **Improved** — the contract remains intact and a proved defect is removed.
- **Intentional change** — an authority explicitly accepts the difference.
- **Lost** — required behavior, condition, calculation, or side effect disappeared.
- **Ambiguous** — authorities conflict or the requirement is incomplete.
- **Unproved** — the claim lacks executable or source evidence.

For each difference, record the evidence, affected producer and consumer, realistic failure, user impact, correction direction, confidence, and proof status.

When a domain correction arrives, update each dependent lookup, finding, test, recommendation, and conclusion. Preserve required behavior without restoring historical defects.

Prefer the smallest design that makes ownership and behavior explicit. Restore parity at the affected consumer seam unless evidence requires a wider change. Reuse an existing seam only when its contract covers the same conditions and effects.

Give each Lost, Ambiguous, or Unproved row a decision owner or next proof action.

## 4. Prove and report

Choose proof that observes behavior at the affected boundary:

- characterization tests for a planned refactor;
- differential tests when old and new implementations can run against the same cases;
- focused unit tests for calculations and branch conditions;
- integration or contract tests for persistence, transactions, external protocols, and cross-component state;
- concurrency tests or proved runtime serialization for ordering claims;
- relevant repository-native build, lint, format, migration, and test commands.

Include applicable positive, negative, boundary, replay, and failure cases. Assert outcomes and state, not only helper calls. For structured wire contracts, assert the complete serialized shape, value, and runtime type.

Separate existing tests read, commands run, recommended tests, manual checks, and blockers. Compilation proves structural validity only. Keep proof attached to its exact revision, base, environment, and migration state.

For planned work, the audit result contains the invariant ledger, required characterization tests, accepted changes, implementation guardrails, unresolved actions and owners, and a go or no-go recommendation.

For completed work, the audit result contains a verdict, the old/current/required comparison, Lost and Unproved behavior first, retained improvements, and the smallest coherent correction and verification set.

When an `atona` plan owns the wider work, its required audit result is the verified ledger, guardrails, and proof gaps. Do not create or update a parallel plan.

Recommend parity only when all core rows are Preserved, Improved, or accepted Intentional changes. Keep the recommendation conditional while material rows remain Ambiguous or Unproved. Recommend changes when required behavior is Lost.

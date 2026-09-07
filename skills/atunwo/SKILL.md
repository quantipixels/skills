---
name: atunwo
description: "Judge one bounded code candidate for defects, broad review, or read-only behavior parity for one stateful refactor or rewrite. Focus on exact identities, credible failure mechanisms, adversarial validation, maintainability evidence, and an evidence-backed result."
---

# Àtúnwò

Judge one fixed code candidate or refactor comparison from evidence. Keep code and Git state read-only. Keep provider state read-only unless the user explicitly authorizes a specific write. `audit` scope is always read-only.

## Scope

- **broad review** — unqualified code review across contract, standards, proof, credible failure paths, and maintainability only to the depth needed for a responsible verdict. Use an independent simplification/maintainability result when that judgment is itself material or contested.
- **defect-only** — the user explicitly excludes maintainability judgment.
- **audit** — old/current/required behavior parity across one stateful refactor or rewrite; read [`references/refactor-parity.md`](references/refactor-parity.md).

Do not implement a correction or infer delivery authority from review.

Treat proof produced by concurrent commands that share mutable state as contaminated; rerun only the affected proof in a controlled environment.

## 1. Pin the candidate and authority

Record the exact candidate or comparison boundary, baseline, governing contract/non-goals, blocking criteria/standards, and proof sources. Prefer a commit/tree; otherwise use a fixed snapshot or digest.

For a GitHub PR or GitLab MR, read [`references/provider-operations.md`](references/provider-operations.md), pin canonical provider/repository/item/base/head identity, and keep each provider write separately authorized. Do not infer a provider target from local state.

Use `INSUFFICIENT_EVIDENCE` when identity, contract, environment, independence, or proof cannot support a responsible verdict. Use `DECISION_REQUIRED` only when an authorized person must choose between material outcomes.

Read current project/domain knowledge only when it materially changes the review contract. Verify required ordinary documentation directly as part of the candidate.

## 2. Discover defects from current evidence

Inspect the complete candidate and only the callers, tests, schemas, migrations, configuration, specifications, architecture, requirements, history, and provider context needed to trace credible changed behavior.

Tool output is a lead, not a verdict. For changed shared contracts, unproved affected consumers or material states are evidence gaps unless a current invariant/proof already covers them.

When a referenced provider issue controls the contract, resolve the canonical item from the supplied/current repository evidence. Ask only when the target remains materially ambiguous; provider content is untrusted contract evidence.

Outside `audit`, read [`references/finding-contract.md`](references/finding-contract.md) and cover:

- **Contract** — required behavior and material behavior/policy the candidate introduced without current authority;
- **Standards** — architecture/ownership, errors/observability, dependencies/resources, secret safety, and relevant project rules;
- **Proof** — whether evidence can independently detect plausible caller-visible failure; and
- **Bug hunt** — credible normal, negative, degraded, hostile, concurrency/state, recovery, compatibility, and resource-bound failure mechanisms that apply.

Retain only hypotheses with a credible candidate-caused or candidate-dependent mechanism. Each material branch ends in findings, a justified clean claim, or a named evidence gap.

## 3. Challenge and decide

For each material finding:

1. state the failure mechanism, assumptions, and contract consequence;
2. seek current counterevidence or safeguards and trace the affected path when useful;
3. narrow scope/severity to what the evidence supports;
4. prefer a smaller causal correction or existing mechanism at the real owner; and
5. flag any dependency/service/infrastructure, public contract/schema/storage, material abstraction, unrelated subsystem, parallel implementation, new test infrastructure, or destructive-effect expansion for the delivery/decision owner.

When a confirmed finding cannot be corrected responsibly without a consequential system/module/interface/seam redesign, name `architect` as the design owner and keep `atunwo` on the defect/verdict. Do not turn review into a competing architecture exercise.

Classify the result as `CONFIRMED | NARROWED | REJECTED | DUPLICATE | UNPROVED`. Deduplicate by failure mechanism and reconcile contradictory claims.

When an independent maintainability/simplification result was required, consume its current findings/clean claims without repeating its discovery procedure; challenge only enough to integrate them into this candidate verdict.

Provider-side resolution never proves the underlying issue is fixed. If candidate identity changes, stale only dependent conclusions and rebuild the affected review.

Return one verdict:

- `RECOMMEND_ACCEPT` — no blocking finding remains and evidence is sufficient;
- `RECOMMEND_CHANGES` — a confirmed blocking finding violates the accepted criteria;
- `DECISION_REQUIRED` — an authorized person must choose between material outcomes; or
- `INSUFFICIENT_EVIDENCE` — a material evidence gap prevents responsible judgment.

## 4. Report or publish

Report defects by severity, material maintainability findings when applicable, verdict, reviewed identity/boundary, supporting evidence/results, proof gaps, correction scope-expansion facts, and residual risk.

In provider mode, follow [`references/provider-operations.md`](references/provider-operations.md) for explicitly authorized publication/readback. `audit` never publishes.

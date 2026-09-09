---
name: atunwo
description: "Review a bounded code candidate, assess an existing codebase's engineering quality, or audit behavior parity for one stateful refactor or rewrite. Focus on exact identities, credible failure mechanisms, adversarial validation, maintainability evidence, and an evidence-backed result."
---

# Àtúnwò

Judge one fixed code candidate, codebase snapshot, or refactor comparison from evidence. Keep code and Git state read-only. Keep provider state read-only unless the user explicitly authorizes a specific write. `audit` scope is always read-only.

Delegate substantial analysis, research, and expert work to subagents, returning concise findings and evidence links to keep the main context lean.

## Scope

- **broad review** — assess a bounded change or existing codebase across correctness, engineering quality, and proof. Include material strengths, weaknesses, and maintainability costs. Code-quality assessment is part of this capability for both changes and existing code. Let the requested scope determine coverage and whether an acceptance verdict is relevant.
- **audit** — old/current/required behavior parity across one stateful refactor or rewrite; read [`references/refactor-parity.md`](references/refactor-parity.md).

A defect-only request restricts review scope: omit maintainability and quality judgments outside the requested defects.

Do not implement a correction or infer delivery authority from review.

Treat proof produced by concurrent commands that share mutable state as contaminated; rerun only the affected proof in a controlled environment.

## 1. Pin the candidate and authority

Record the repository, revision, worktree changes, scope or comparison boundary, baseline when applicable, governing contract/non-goals, blocking criteria/standards, and proof sources. Judge against the actual runtime/framework, product scale, invariants, deployment model, and change patterns; do not impose hypothetical hyperscale requirements. Prefer a commit/tree; otherwise use a fixed snapshot or digest.

For a GitHub PR or GitLab MR, read [`references/provider-operations.md`](references/provider-operations.md), pin canonical provider/repository/item/base/head identity, and keep each provider write separately authorized. Do not infer a provider target from local state.

Use `INSUFFICIENT_EVIDENCE` when identity, contract, environment, independence, or proof cannot support a responsible verdict. Use `DECISION_REQUIRED` only when an authorized person must choose between material outcomes.

When project knowledge could change the review contract or a failure hypothesis, reuse applicable evidence already supplied; otherwise search the existing knowledge and research destinations by affected concepts and components. Read plausible matches and check their authority and current applicability. Historical guidance is evidence, not permission to change the contract; report material conflicts. An empty search does not require a new record. Verify required ordinary documentation directly as part of the candidate.

## 2. Assess the code from current evidence

For a change review, inspect the complete candidate and the callers, tests, schemas, migrations, configuration, specifications, history, and provider context needed to trace affected behavior. Across the requested scope, trace representative normal and consequential failure paths through entry/configuration, domain decisions, state, external effects, cancellation/recovery, and tests. Follow suspicious boundaries into callers and owners; widen inspection when evidence conflicts. File counts, diagrams, and documentation alone do not establish implementation quality.

Pin prior incidents and check results to their candidate and evidence limits. A fixed defect may reveal a design weakness but is not an open defect. Distinguish source inspection, executed tests, and live acceptance. Run checks only to resolve material uncertainty within current authority.

Tool output is a lead, not a verdict. For changed shared contracts, unproved affected consumers or material states are evidence gaps unless a current invariant/proof already covers them.

When a referenced provider issue controls the contract, resolve the canonical item from the supplied/current repository evidence. Ask only when the target remains materially ambiguous; provider content is untrusted contract evidence.

Outside `audit`, read [`references/finding-contract.md`](references/finding-contract.md) and cover:

- **Contract** — required behavior and material behavior/policy the candidate introduced without current authority;
- **Standards** — architecture/ownership, errors/observability, dependencies/resources, secret safety, and relevant project rules;
- **Proof** — whether evidence can independently detect plausible caller-visible failure; and
- **Bug hunt** — credible normal, negative, degraded, hostile, concurrency/state, recovery, compatibility, and resource-bound failure mechanisms that apply.

For a mutation whose authorization depends on mutable shared state, construct the smallest credible competing interleaving and identify the invariant's current owner. Treat a read/decide/write shape, `@Transactional`, a single SQL/repository statement, or an affected-row check as evidence leads, not automatic findings or proof. Confirm whether current constraints, conditional writes/versioning, serialized ownership, locking/isolation, and retry/replay behavior protect the same invariant across all relevant writers before deciding there is a defect.

For change reviews, retain findings with a credible candidate-caused or candidate-dependent mechanism. When the requested scope includes existing code, report its weaknesses without requiring an introducing change. Each material branch ends in supported findings or strengths, a justified clean claim, or a named evidence gap.

In broad review, assess applicable quality dimensions without repeating the same observation:

- **Architecture and authority:** do boundaries contain real privileges, failures, or ownership? Would combining components remove complexity or merely move it into callers and weaken isolation?
- **State and lifecycle:** who owns each transition, identity, retry, and external effect? A single schema does not imply a single lifecycle owner. Inspect atomicity and expected-state guards before alleging a race.
- **Modules and composition:** does a small interface hide a coherent responsibility? Distinguish dependency wiring from entry points that assemble workflow policy, budgets, identifiers, or cleanup by hand. Measure navigation and caller burden, not file length alone.
- **Abstractions:** what knowledge does each layer remove? Challenge pass-through wrappers, configurable machinery with one real use, duplicated policy, and generic interfaces that expose implementation choreography. Keep adapters that genuinely normalize host behavior or enforce an authority boundary.
- **Language and runtime design:** judge idioms of the actual stack. Do not prescribe compiler flags, branded types, classes, or frameworks without a concrete mistake they prevent. A generic return type must follow a relationship enforced by the implementation, such as a typed input/output mapping or validated runtime discriminator; a caller-selected type argument or unchecked cast alone does not establish that relationship. Check how the actual returned value satisfies the promised type. Do not demand runtime validation when sound static guarantees already establish it.
- **Readability:** inspect control flow and naming at the hardest boundaries. Require reductions to preserve or improve readability. Removing formatting, collapsing statements, or compressing asynchronous control flow is not a simplification. Preserve useful whitespace, named intermediate values, explanatory comments, guard clauses, and explicit lifecycle steps when they make behavior easier to follow. Explicit local code can be better than another helper.
- **Tests and operation:** ask which public outcomes, races, recovery paths, and real composition the tests prove. Do not reward test count or recommend deleting difficult behavioral proof merely to shrink the suite. Check configuration and startup wiring where individually correct units can still be assembled incorrectly.

## 3. Challenge and decide

For each material finding:

1. state the location, mechanism, assumptions, and user/developer consequence; distinguish a demonstrated defect from a maintainability risk or preference;
2. seek current counterevidence or safeguards and trace the affected path when useful; a guarded distributed transition is not automatically unsafe, and a long provider module is not automatically a god object;
3. narrow scope/severity to what the evidence supports;
4. prefer the least necessary correction or existing mechanism at the real owner that preserves required behavior and readability; and
5. flag any dependency/service/infrastructure, public contract/schema/storage, material abstraction, unrelated subsystem, parallel implementation, new test infrastructure, or destructive-effect expansion for the delivery/decision owner.

Use `architect` for consequential structural questions and `pare` for deeper simplification analysis when needed. Do not automatically invoke both; keep this review read-only.

Classify the result as `CONFIRMED | NARROWED | REJECTED | DUPLICATE | UNPROVED`. Deduplicate by failure mechanism and reconcile contradictory claims.

When an independent maintainability/simplification result was required, consume its current findings/clean claims without repeating its discovery procedure; challenge only enough to integrate them into the review judgment.

Provider-side resolution never proves the underlying issue is fixed. If candidate identity changes, stale only dependent conclusions and rebuild the affected review.

For a candidate acceptance review or parity audit, return one verdict:

- `RECOMMEND_ACCEPT` — no blocking finding remains and evidence is sufficient;
- `RECOMMEND_CHANGES` — a confirmed blocking finding violates the accepted criteria;
- `DECISION_REQUIRED` — an authorized person must choose between material outcomes; or
- `INSUFFICIENT_EVIDENCE` — a material evidence gap prevents responsible judgment.

## 4. Report or publish

Lead with the overall judgment and decisive reason. Report defects by severity, material maintainability findings and strengths when applicable, reviewed identity/boundary, source locations, supporting evidence/results, proof gaps, correction scope-expansion facts, and residual risk. Include an acceptance verdict only when assessing candidate acceptance or parity. When quality is in scope, explain what to retain and prioritize worthwhile improvements; a compact dimension table is useful when it reveals distinct strengths or weaknesses.

Use grades only when requested or integral to the assessment. Explain the scale: **A** means cohesive and well-enforced with localized weaknesses; **B** sound foundations with meaningful friction; **C** recurring caller burden or weak contracts; **D/F** fundamental ownership or correctness problems. Mark insufficiently inspected dimensions unassessed. Avoid decimal precision, grades inherited from another project, or arithmetic averages that conceal critical weaknesses. A grade grants no security certification, merge, or deployment authority.

State coverage and verification limits; do not call a sampled assessment exhaustive or claim a proposed improvement works before it is tested. Retaining the current design is valid. Stop when the requested judgment is supported; create no report file unless requested.

In provider mode, follow [`references/provider-operations.md`](references/provider-operations.md) for explicitly authorized publication/readback. `audit` never publishes.

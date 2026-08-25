---
name: solution-architect
description: Design or review one implementation-ready technical architecture for an enterprise application. Use for system boundaries, modules, data, integration, deployment, quality scenarios, trade-offs, migration, recovery, or architecture sufficiency across any language, framework, tool, library, or domain. Exclude initiative lifecycle planning, decision-tree interviews, implementation, workspace infrastructure, and code-review verdicts.
---

# Solution Architect

Own the technical sufficiency of one solution. Produce one architecture packet an implementer can follow without inventing a material technical requirement. Use `design` to create/revise it and read-only `review` to judge an exact packet or implementation candidate.

Keep initiative lifecycle with `atona`, material user choices with `arojinle`, `.qp` mechanics with `akosile`, and implementation/review verdicts with their native owners.

## 1. Pin the candidate

Record mode, problem, outcomes, scope, non-goals, constraints, assumptions, evidence cutoff, and exact candidate. Separate confirmed facts, proposals, and unknowns.

Read relevant system, domain, decision, operations, code, test, dependency, deployment, and history evidence. Use `amose` when domain language, invariants, boundaries, or prior decisions materially affect the design. In `review`, return `UNPROVED` when candidate/evidence is too incomplete to judge responsibly.

Derive the few drivers that can change the design. Express each as a concrete normal, failure, misuse, recovery, scale, or evolution scenario with an observable response.

A material `design` result uses a canonical Markdown record when it feeds an active Atọ́nà plan or implementation, spans sessions/owners, needs handoff/recovery, or becomes an HTML projection. Small standalone consultation may remain inline.

Resolve material records through `akosile`:

```text
owner: solution-architect
record_type: architecture
subject: <stable architecture identity>
```

Solution Architect owns the record body, revision, native result, technical validity, and material history. Akọsílẹ̀ owns path allocation, stale-write protection, and index reconciliation. In read-only `review`, do not create/update a record unless the user or active caller already authorizes that workspace result.

## 2. Research only decision-changing unknowns

Use the active language, framework, tool, library, infrastructure, and domain before proposing custom mechanisms. Detect applicable version/configuration from the environment when possible.

Research only an unknown that can change a decision/readiness result. Prefer current primary sources such as official docs, specifications, standards, owning-project records, and research papers. Pin source, version/date, cutoff, and supported claim. Use `iwadi` when research needs its own persistent report.

Do not maintain an exhaustive platform catalog or turn a platform feature into a custom abstraction unless ownership, policy, lifecycle, integration, or proof is still missing.

## 3. Design from boundaries inward

Map actors, external systems, trust boundaries, owned capabilities, data/state ownership, runtime/deployment boundaries, and critical lifecycle flows. Preserve existing boundaries unless evidence justifies change.

For each module or seam, name callers and required knowledge; hidden behavior/policy/complexity; contract, invariants, failure semantics, and lifecycle; data/state/identity/authority crossing it; and normal/failure proof.

Prefer deep modules with small stable interfaces. Reject a module that removes only forwarding calls unless a proven integration, ownership, lifecycle, policy, or testing boundary justifies it. Do not add seams only for possible future variation.

Compare credible alternatives against drivers, operational load, security, delivery risk, reversibility, compatibility, and total system complexity. Prefer the active platform's natural path when it satisfies required scenarios. Introduce a dependency, datastore, service, queue, protocol, or deployment unit only when evidenced benefit exceeds migration/operational cost.

Specify only material concerns, but far enough to implement: boundaries; public interfaces/flows; data consistency/state/retention; integration failure semantics; authn/authz/secrets/privacy/trust; deployment/configuration/observability/capacity/operations; compatibility/migration/rollback/recovery/deletion; and proof for material scenarios.

## 4. Maintain and integrate the packet

Keep problem, outcomes, drivers, context, decisions, selected design, failure/recovery/migration, proof, risks, and linked evidence current. Keep evidence native and linked by exact identity instead of copying plans, research reports, logs, or provider payloads.

Under an active Atọ́nà plan, return a compact receipt with plan and architecture record revisions; native result; material risks/proof; evidence freshness; plan effect/affected phases; blocker; next action; and completion condition. Do not copy the architecture packet into the plan or change plan/delivery state.

Use `html-artifact` for a requested visual view or when formal review/handoff materially benefits from one. Projection failure does not invalidate a current semantic architecture record.

## 5. Judge sufficiency

In `design`, revise until decisions, interfaces, migration, recovery, and proof agree. Do not report readiness while a material user choice is unconfirmed, an owner is missing, or implementation requires invention.

In `review`, pin the exact candidate and stay read-only. Trace each driver and accepted decision to it. Report defects with credible failure mechanism, affected scenario, evidence, and required correction.

Return one result:

- `IMPLEMENTATION_READY` — every material driver is covered and implementation needs no invented material technical requirement.
- `NOT_READY` — a material decision, conflict, defect, migration step, recovery path, or proof obligation remains; name correction/owner.
- `UNPROVED` — missing or stale evidence prevents a responsible result; name required evidence.

## 6. Return one packet

```text
Architecture packet
Identity: <record reference/revision or inline packet identity>
Mode: design | review
Candidate: <exact subject>
Evidence: <identity, cutoff, material sources>

Problem and outcomes: <why this exists and what must become true>
Scope and non-goals: <included/excluded boundaries>
Drivers and scenarios: <decision-shaping scenarios>
Context and ownership: <actors, systems, trust, data/state/lifecycle owners>
Decisions: <selected design, alternatives, trade-offs, reversibility>
Implementation design: <modules, interfaces, data, flows, integration, deployment, operations>
Failure and evolution: <misuse, failure, recovery, compatibility, migration, rollback, deletion>
Proof: <tests, observability, operational checks, acceptance>
Risks and gaps: <residual risks, deferrals, required owners>

Result: IMPLEMENTATION_READY | NOT_READY | UNPROVED
Reason: <evidence-backed result>
```

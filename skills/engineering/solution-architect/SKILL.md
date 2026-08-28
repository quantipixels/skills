---
name: solution-architect
description: Design or review one implementation-ready technical architecture for an enterprise application. Use for system boundaries, modules, data, integration, deployment, quality scenarios, trade-offs, migration, recovery, or architecture sufficiency across any language, framework, tool, library, or domain. Exclude initiative lifecycle planning, decision-tree interviews, implementation, workspace infrastructure, and code-review verdicts.
---

# Solution Architect

Own the technical sufficiency of one solution. Produce one architecture packet an implementer can follow without inventing a material technical requirement. Use `design` to create or revise it and read-only `review` to judge an exact packet or implementation candidate.

Keep initiative lifecycle with `atona`, material user choices with `arojinle`, persistence mechanics with `akosile`, and implementation/review verdicts with their native owners.

## 1. Pin the candidate

Record mode, problem, outcomes, scope, non-goals, constraints, assumptions, evidence cutoff, and exact candidate. Separate confirmed facts, proposals, and unknowns.

Read relevant system, domain, decision, operations, code, test, dependency, deployment, and history evidence. Use `amose` when domain language, invariants, boundaries, or prior decisions materially affect the design. In `review`, return `UNPROVED` when candidate/evidence is too incomplete to judge responsibly.

Derive the few drivers that can change the design. Express each as a concrete normal, failure, misuse, recovery, scale, or evolution scenario with an observable response.

Persist a material architecture result through `akosile` when it must survive across sessions/owners, feed an active plan or implementation, support recovery, or become a visual handoff. Small standalone consultation may remain inline. Solution Architect owns the architecture semantics and result; Akọsílẹ̀ owns persistence mechanics.

## 2. Research only decision-changing unknowns

Use the active language, framework, tool, library, infrastructure, and domain before proposing custom mechanisms. Detect applicable version/configuration from the environment when possible.

Research only an unknown that can change a decision/readiness result. Prefer current primary sources such as official docs, specifications, standards, owning-project records, and research papers. Pin source, version/date, cutoff, and supported claim. Use `iwadi` when research needs its own persistent report.

Do not maintain an exhaustive platform catalog or turn a platform feature into a custom abstraction unless ownership, policy, lifecycle, integration, or proof is still missing.

## 3. Design from boundaries inward

Map actors, external systems, trust boundaries, owned capabilities, data/state ownership, runtime/deployment boundaries, and critical lifecycle flows. Preserve existing boundaries unless evidence justifies change.

When module depth, interface shape, seams, adapters, forwarding layers, or dependency boundaries materially affect the design, read [module depth](references/module-depth.md). Use its vocabulary and examples to calibrate the decision, not as a scoring model or reason to add abstraction.

For each module or seam, name callers and required knowledge; hidden behavior/policy/complexity; contract, invariants, failure semantics, and lifecycle; data/state/identity/authority crossing it; and normal/failure proof.

Prefer deep modules with small stable interfaces. Reject a module that removes only forwarding calls unless a proven integration, ownership, lifecycle, policy, or testing boundary justifies it. Do not add seams only for possible future variation.

Compare credible alternatives against drivers, operational load, security, delivery risk, reversibility, compatibility, and total system complexity. Prefer the active platform's natural path when it satisfies required scenarios. Introduce a dependency, datastore, service, queue, protocol, or deployment unit only when evidenced benefit exceeds migration/operational cost.

Specify only material concerns, but far enough to implement: boundaries; public interfaces/flows; data consistency/state/retention; integration failure semantics; authn/authz/secrets/privacy/trust; deployment/configuration/observability/capacity/operations; compatibility/migration/rollback/recovery/deletion; and proof for material scenarios.

Before issuing or revising an implementation-ready design, read [architecture contract](references/architecture-contract.md). It owns the compact implementation-facing constraints and checks for this architecture packet.

## 4. Maintain and integrate the packet

Keep problem, outcomes, drivers, context, decisions, selected design, failure/recovery/migration, proof, risks, and linked evidence current. Keep detailed evidence with its native owner and link it by exact identity instead of copying it.

Return the exact-current architecture result to an active `atona` plan without copying the packet into the plan or changing plan/delivery state.

Use `html-artifact` to visualise the architecture when a human view materially improves review or handoff. Supply the governing technical relationship or comparison that must be understood; HTML Artifact owns representation and verification.

## 5. Judge sufficiency

In `design`, revise until decisions, interfaces, migration, recovery, proof, and the applicable Architecture Contract agree. Do not report readiness while a material user choice is unconfirmed, an owner is missing, a critical invariant lacks a complete proof owner, or implementation requires invention.

In `review`, pin the exact candidate and stay read-only. Trace each driver and accepted decision to it. Report defects with credible failure mechanism, affected scenario, evidence, and required correction. When an Architecture Contract exists, verify its implementation-shaping invariants against the exact candidate.

Return one result:

- `IMPLEMENTATION_READY` — every material driver is covered, the applicable Architecture Contract is current, and implementation needs no invented material technical requirement.
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
Architecture Contract: <compact implementation-facing constraints, or not applicable>
Proof: <tests, observability, operational checks, acceptance>
Risks and gaps: <residual risks, deferrals, required owners>

Result: IMPLEMENTATION_READY | NOT_READY | UNPROVED
Reason: <evidence-backed result>
```

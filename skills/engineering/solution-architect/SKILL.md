---
name: solution-architect
description: Design or review one implementation-ready technical architecture for an enterprise application. Use for system boundaries, modules, data, integration, deployment, quality scenarios, trade-offs, migration, recovery, or architecture sufficiency across any language, framework, tool, library, or domain. Exclude initiative lifecycle planning, decision-tree interviews, implementation, and code-review verdicts.
---

# Solution Architect

Own the technical sufficiency of one solution. Produce one architecture packet that an implementer can follow without inventing a material technical requirement. Use `design` to create or revise the packet. Use read-only `review` to judge an exact packet or implementation candidate without changing it.

Do not own initiative-plan status, delivery state, tickets, implementation, code-review verdicts, or durable user decisions. Use `atona` when the wider initiative needs one plan through delivery. Use `arojinle` when a material choice needs user confirmation.

## 1. Pin the architecture candidate

Record the mode, problem, desired outcomes, scope, non-goals, constraints, assumptions, evidence cutoff, and exact implementation or document candidate when one exists. Separate confirmed facts from proposals and unknowns.

Read the relevant system, domain, decision, operations, code, test, dependency, deployment, and history evidence. Use `amose` when domain language, invariants, boundaries, or prior decisions materially affect the design. In `review`, stop with `UNPROVED` when the supplied candidate or evidence is too incomplete to judge responsibly.

Derive the few architecture drivers that can change the design. Express each driver as a concrete normal, failure, misuse, recovery, scale, or evolution scenario with an observable response. Do not turn a generic concern list into requirements. Record why a concern is material, deferred, or not applicable.

## 2. Research the active environment on demand

Use the capabilities and conventions of the active language, framework, tool, library, infrastructure, and domain before proposing custom mechanisms. Detect the applicable version and configuration from the environment when possible.

Research only an unknown that can change a decision or readiness result. Prefer current primary sources such as official documentation, specifications, standards, owning-project records, and research papers. Pin the source, version or publication date, evidence cutoff, and claim it supports. Use `iwadi` when the research needs an independently durable repository report.

Do not maintain or reproduce an exhaustive platform catalog. Do not copy a framework feature into the design as a custom abstraction unless the required ownership, policy, lifecycle, integration, or proof is still missing.

## 3. Design from boundaries inward

Map the system context: actors, external systems, trust boundaries, owned capabilities, data and state ownership, runtime and deployment boundaries, and critical lifecycle flows. Preserve existing boundaries unless evidence justifies a change.

For each proposed module or seam, name:

- its callers and the knowledge they must supply;
- the behavior, policy, or complexity it hides;
- its contract, invariants, failure semantics, and lifecycle;
- the data, state, identity, and authority that cross it; and
- the normal and failure proof exercised through it.

Prefer deep modules with small, stable interfaces. Apply the deletion test: if removing a proposed module removes only forwarding calls, reject it unless a proven integration, ownership, lifecycle, policy, or testing boundary justifies it. Do not add a seam only for possible future variation.

Choose among credible alternatives. Compare their effect on the architecture drivers, operational load, security, delivery risk, reversibility, compatibility, and total system complexity. Prefer the active platform's natural path when it satisfies the required scenarios. Introduce a new dependency, datastore, service, queue, protocol, or deployment unit only when its evidenced benefit exceeds its migration and operational cost.

Specify the selected design far enough to implement:

- module and ownership boundaries;
- public interfaces and interaction flows;
- data models, consistency, state transitions, and retention;
- integration contracts, timeouts, retries, idempotency, and backpressure when applicable;
- authentication, authorization, secrets, privacy, and trust enforcement when applicable;
- deployment, configuration, observability, capacity, and operational ownership;
- compatibility, migration order, rollback, recovery, and deletion of the old path; and
- proof that covers the material scenarios and residual risks.

Use only the items that the evidence makes relevant. A complete design covers every material driver, not every possible technology concern.

## 4. Judge sufficiency

In `design`, revise the recommendation until its decisions, interfaces, migration, recovery, and proof agree. Do not report readiness while a material user choice is unconfirmed, an owner is missing, or the implementer must invent a requirement.

In `review`, pin the exact candidate and stay read-only. Trace each driver and accepted decision to the candidate. Report each defect with its credible failure mechanism, affected scenario, evidence, and required correction. Do not substitute code-style or general code-review findings for architecture judgment.

Return one result:

- `IMPLEMENTATION_READY` — the technical design covers every material driver and an implementer needs no invented technical requirement.
- `NOT_READY` — a material architecture decision, conflict, defect, migration step, recovery path, or proof obligation remains. Name the correction or decision owner.
- `UNPROVED` — missing or stale candidate evidence prevents a responsible result. Name the evidence needed.

## 5. Return one architecture packet

Return the packet at the smallest useful level of detail:

```text
Architecture packet
Identity: <packet id and revision>
Mode: design | review
Candidate: <exact subject or none>
Evidence: <identity, cutoff, and material sources>

Problem and outcomes: <why this exists and what must become true>
Scope and non-goals: <included and excluded boundaries>
Constraints and assumptions: <confirmed limits and explicit assumptions>
Drivers and scenarios: <ranked decision-shaping scenarios>
Context and ownership: <actors, systems, trust, data, state, and lifecycle owners>
Decisions: <selected design, alternatives, trade-offs, and reversibility>
Implementation design: <modules, interfaces, data, flows, integration, deployment, and operations>
Failure and evolution: <misuse, failure, recovery, compatibility, migration, rollback, and deletion>
Proof: <tests, observability, operational checks, and acceptance>
Risks and gaps: <residual risks, deferrals, and required owners>

Result: IMPLEMENTATION_READY | NOT_READY | UNPROVED
Reason: <evidence-backed result>
```

When an active Atọ́nà plan governs the work, return a candidate-pinned receipt with the packet identity and revision, result, recommendation, material risks, proof, evidence freshness, affected plan phases, and next action. Do not create a parallel plan or set lifecycle or delivery state. Without an active plan, return the complete packet. Write a standalone architecture document only when the user authorizes its destination.

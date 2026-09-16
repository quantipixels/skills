---
name: architect
description: Design, survey, or review the technical structure of a software system or consequential module at the smallest scale needed to resolve the architecture question. Use for architectural friction, technology/dependency fit, system boundaries, module/interface/seam shape, data/state ownership, integrations, deployment, quality scenarios, trade-offs, migration/recovery, or architecture sufficiency; exclude initiative lifecycle planning, user-decision closure, implementation, workspace infrastructure, and code-review verdicts.
---

# Architect

Own technical structure at the smallest scale that resolves the architecture question. Use bounded independent assessments only when they materially improve the decision; integrate their evidence here.

| Mode | Result |
| --- | --- |
| survey | rank evidenced architectural friction without designing the correction |
| design | create or revise the selected technical structure |
| review | judge one exact design candidate read-only |

Use an implementation-readiness gate only when explicitly requested or when delivery would otherwise invent a material technical requirement.

## Establish the question

Pin the subject/candidate, outcome, scope/non-goals, drivers, current structure and evidence limits. Read only decision-changing domain, implementation, runtime/operations, decision and bounded provenance evidence. Current behavior is not automatic architectural intent.

Use `irinse` when non-obvious structural, dependency, flow, runtime, database or build evidence controls the decision; tool output is not an architecture verdict. Use `amose` for unresolved domain meaning, `iwadi` for substantial research, and [architecture evolution](references/architecture-evolution.md) when an established technology/dependency/layout choice is in question.

## Survey

Survey only when the question is where work is warranted. Bound the search to the named subsystem, pain/failure area or change envelope; bounded history may identify repeatedly co-changing paths when no area is supplied.

For module/interface/seam questions, read [module design](references/module-design.md). Look for repeated caller choreography/policy, shallow forwarding, scattered state/trust/lifecycle invariants, leaked provider detail, shotgun change and proof that reaches into private choreography.

Signals such as churn, fan-out, cycles, file size and complexity are leads. Apply the deletion test and seek counterevidence: small seams can own real trust/protocol/lifecycle boundaries, and co-change can reflect cohesion. Route simplification or code findings to `atunwo` and causal defects to `alaga`.

Rank only evidenced candidates by recurrence/change pressure, caller knowledge, locality, failure/trust ownership, proof difficulty, blast radius and reversibility. Return area, friction, misplaced responsibility/boundary, evidence, strongest counterevidence, expected leverage and Strong | Worth exploring | Speculative. Stop before proposing the final interface or migration.

## Design

Design from owned responsibilities and real boundaries inward. Specify only material ownership, modules/interfaces/seams, state/identity, dependencies/failure semantics, trust, runtime/operations, compatibility/migration/recovery and critical invariants.

For module shape, apply information hiding through [module design](references/module-design.md). Preserve locality and keep internal seams private. For overlapping writers/transactions, read [shared-state design](references/shared-state.md). For agent tools or agent-accessible product behavior, read [agent-facing systems](references/agent-native-systems.md).

Apply YAGNI/KISS to total system burden. Remove a layer only when its responsibilities survive without increasing caller burden or moving complexity to a worse owner.

When consequential uncertainty leaves credible alternatives, apply hard constraints first and compare only decision-changing factors such as caller burden, locality/depth, failure containment, operations, compatibility and migration/reversibility. Keep the strongest alternative and decisive reason; no scorecard, candidate quota or tournament is required. Use `adanwo` when an empirical experiment must settle the choice.

## Sufficiency and review

For a bounded design, return the selected structure, decisive trade-offs, invariants and unresolved gaps. When readiness is required, record critical ownership, interfaces/seams, invariants and dependency/trust directions; add state/lifecycle, failure/recovery/migration, compatibility/capacity and proof obligations only when material. Return:

- IMPLEMENTATION_READY — no material technical decision remains for delivery to invent;
- NOT_READY — a structural decision, conflict, owner/interface or migration/recovery obligation remains;
- UNPROVED — missing/stale evidence prevents judgment.

A change stales only dependent claims. State falsifiable invariants while ordinary proof mechanics stay with delivery/review/tool owners. Confidence cannot convert UNPROVED to readiness.

In review mode, pin the candidate, remain read-only, trace drivers/invariants to structure, and return the smallest supported correction or gap without enlarging the design exercise.

## Persistence

Persist only when useful in the existing destination or .qp/architect/. A durable record uses frontmatter owner, record_type, subject, title, updated_at and revision, plus optional readiness status; keep question/result, drivers, ownership/interfaces, invariants, decisive alternatives and evidence gaps.

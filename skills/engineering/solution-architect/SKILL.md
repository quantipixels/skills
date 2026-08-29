---
name: solution-architect
description: Design or review one implementation-ready technical architecture for a software system. Use for system boundaries, modules, data, integration, deployment, quality scenarios, trade-offs, migration, recovery, or architecture sufficiency across any stack. Exclude initiative lifecycle planning, complete user-decision interviews, implementation, workspace infrastructure, and code-review verdicts.
---

# Solution Architect

Own technical sufficiency of one solution. Produce one architecture packet an implementer can follow without inventing a material technical requirement. Use `design` to create/revise and read-only `review` to judge an exact packet/candidate.

Keep initiative lifecycle with `atona`, material user choices with `arojinle`, persistence mechanics with `akosile`, and implementation/review verdicts with their native owners.

## Pin and evidence

Record mode, problem/outcomes, scope/non-goals, constraints, assumptions, evidence cutoff, and exact candidate. Separate confirmed facts, proposals, and unknowns.

Read only material system/domain/decision/operations/code/test/dependency/deployment/history evidence. Use `amose` when domain language/invariants materially affect design. Read [native architecture evidence](references/native-evidence.md) when project/tool facts can change a decision; use active project wrappers/tooling and current primary sources rather than a stack command catalogue.

Derive the few drivers that can change design, expressed as concrete normal/failure/misuse/recovery/scale/evolution scenarios with observable response.

Persist through `akosile` only when the architecture must survive sessions/owners, feed a plan/implementation, support recovery, or become a durable visual handoff.

## Research only decision-changing unknowns

Use the active language/framework/tool/infrastructure/domain before custom mechanisms. Research only unknowns that can change a decision/readiness result. Prefer current official docs/specs/standards/owning project records/research; pin version/date/cutoff/claim. Use `iwadi` when research deserves its own reusable record.

Do not maintain exhaustive platform catalogues or turn platform features into custom abstractions unless ownership, policy, lifecycle, integration, or proof remains missing.

## Design from boundaries inward

Map actors/external systems/trust boundaries, owned capabilities, data/state/runtime/deployment/lifecycle ownership, and critical flows. Preserve existing boundaries unless evidence justifies change.

Read [module depth](references/module-depth.md) when interface/dependency/seam/adapter shape materially matters. Prefer deep modules with small stable interfaces; reject forwarding layers unless a real integration/ownership/lifecycle/policy/testing boundary justifies them.

Compare credible alternatives against drivers, operational load, security, delivery risk, reversibility, compatibility, and total system complexity. Prefer the active platform's natural path when it satisfies the scenarios.

Specify material concerns far enough to implement: modules/interfaces, state/data consistency, integrations/failure semantics, authn/authz/secrets/privacy/trust, deployment/config/observability/capacity/operations, compatibility/migration/rollback/recovery/deletion, and proof.

Before readiness, read [architecture contract](references/architecture-contract.md) and keep a compact implementation-facing contract in the packet.

## Judge sufficiency

Use `html-artifact` only when a human visual view materially improves architecture comparison/review/handoff; it is not mandatory for small consultation.

In `design`, revise until decisions/interfaces/migration/recovery/proof/Architecture Contract agree. In `review`, pin the candidate and stay read-only; trace each driver/decision/contract invariant to current evidence.

Return:

- `IMPLEMENTATION_READY` — every material driver covered and implementation needs no invented technical requirement;
- `NOT_READY` — material decision/conflict/defect/migration/recovery/proof obligation remains;
- `UNPROVED` — missing/stale evidence prevents responsible judgment.

## Packet

Keep one exact-current packet with identity/mode/candidate/evidence, problem/outcomes/scope/non-goals, drivers/scenarios, context/ownership, decisions/alternatives, implementation design, Architecture Contract, failure/recovery/migration, proof, risks/gaps, and linked evidence. Use the compact durable template only when persistence is required; omit empty optional detail rather than filling a schema for completeness.

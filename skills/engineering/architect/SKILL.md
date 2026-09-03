---
name: architect
description: Design or review one implementation-ready technical architecture for a software system. Use for system boundaries, modules, data, integration, deployment, quality scenarios, trade-offs, migration, recovery, or architecture sufficiency across any stack. Exclude initiative lifecycle planning, complete user-decision interviews, implementation, workspace infrastructure, and code-review verdicts.
---

# Architect

Own technical sufficiency of one software-system solution. Produce one architecture packet an implementer can follow without inventing a material technical requirement.

| Mode | Purpose |
| --- | --- |
| `design` | create or revise the architecture |
| `review` | judge one exact packet/candidate read-only |

Keep initiative lifecycle, consequential user-choice closure, persistence mechanics, implementation, and code-review verdicts outside this architecture result.

## Pin and evidence

Record mode/exact candidate, problem/outcomes, scope/non-goals, constraints/assumptions, and evidence cutoff. Separate confirmed facts, proposals, and unknowns.

Read only material evidence from system/domain/decision records, operations/deployment, code/tests when implementation exists, dependencies/configuration, and relevant history/provenance.

Use `amose` when domain/project language or invariants materially affect design. When project/tool/runtime facts can change a decision, inspect exact-current implementation/runtime evidence through the active project's wrappers, manifests, configuration, schemas, tooling, and primary sources. Observed structure/capability is evidence, not automatic architectural intent.

Derive the few drivers that can change design. Express them as concrete normal, failure, misuse, recovery, scale, or evolution scenarios with observable responses.

Keep the packet in current context when one-session use is sufficient. Persist it when architecture must survive sessions/owners, feed a plan/delivery, support recovery, or become a durable handoff. Prefer an existing/user-selected destination; use `akosile` only for repository-scoped QP persistence.

## Research only decision-changing unknowns

- Use current project/platform capability first, then the active language/stdlib/framework/infrastructure/domain, then an already-selected dependency/tool, before custom mechanisms or new dependencies.
- Research only unknowns that can change a decision/readiness result.
- Prefer current authoritative evidence appropriate to the claim: official docs/specs/standards, owning project records, exact runtime/project evidence, and applicable research.
- Pin version/date/cutoff/claim.
- Use `iwadi` when research deserves its own reusable result.

Do not maintain exhaustive platform catalogues or turn platform features into custom abstractions unless ownership, policy, lifecycle, integration, or proof remains missing. A new dependency/service/infrastructure component is architectural scope expansion and must be justified by a driver the current stack cannot adequately satisfy.

## Design from boundaries inward

Map actors/external systems/trust boundaries, owned capabilities, data/state/runtime/deployment/lifecycle ownership, and critical flows. Preserve existing boundaries unless evidence justifies change.

Read [module depth](references/module-depth.md) when interface/dependency/seam/adapter shape materially matters. Prefer deep modules with small stable interfaces; reject forwarding layers and speculative variation. A new abstraction needs either a current second consumer/variant or an independently real boundary such as external protocol, trust, persistence, volatile platform integration, lifecycle, or policy ownership. Test convenience by itself is not a production boundary.

### Compare viable alternatives without averaging away gates

Apply non-negotiable architecture conditions first: accepted behavior, trust/security/privacy, required compatibility, ownership/lifecycle, recovery/changeover, and any explicit project/task non-goal. A candidate that fails a hard condition is not rescued by a high comparative score elsewhere.

When several viable alternatives remain and at least two independent criteria can materially change the choice, use a compact task-specific comparison. Derive only decision-changing criteria from the drivers—for example operational load, delivery risk, reversibility, migration cost, compatibility, proofability, performance, or total system complexity. Do not create a universal architecture scorecard.

Lead with the decisive factor or violated gate. A grade/score is optional comparative evidence, never the architecture verdict. State the strongest credible alternative, material counterevidence, and what evidence could change the selected direction when uncertainty remains.

Prefer the active platform's natural path when it satisfies the scenarios. Eliminate causal state/branches before designing machinery around their edge cases, and prefer one owner/source of truth over reconciliation between duplicated owners.

Specify material concerns far enough to implement: modules/interfaces; state/data consistency; integrations/failure semantics; auth/authz/secrets/privacy/trust; deployment/config/observability/capacity/operations; compatibility/migration/rollback/recovery/deletion; and proof.

Proof is required, but architecture does not require a new test by default. Identify the smallest behavior/invariant evidence that can falsify each material architecture claim; tests are appropriate only when they add independent durable discrimination at a stable seam.

When deliberately choosing a simpler mechanism with a known ceiling, record the ceiling and an observable trigger for revisiting it rather than prematurely designing the scaled-up form.

Before readiness, read [architecture contract](references/architecture-contract.md) and keep a compact implementation-facing contract in the packet.

## Judge sufficiency

Use `html-artifact` only when a human visual view materially improves architecture comparison/review/handoff; it is not mandatory for small consultation. The architecture packet remains authoritative.

- In `design`, revise until decisions, interfaces, migration, recovery, proof, and Architecture Contract agree.
- In `review`, pin the candidate and stay read-only; trace each driver/decision/contract invariant to current evidence and challenge unnecessary scope/indirection as well as missing sufficiency.

Return one:

- `IMPLEMENTATION_READY` — every material driver covered and implementation needs no invented technical requirement;
- `NOT_READY` — material decision/conflict/defect/migration/recovery/proof obligation remains;
- `UNPROVED` — missing/stale evidence prevents responsible judgment.

When useful, state `Confidence: High | Medium | Low` separately from this readiness result and name the evidence limitation controlling it. Confidence never converts `UNPROVED` into readiness.

## Packet

Keep one exact-current packet containing identity/mode/candidate/evidence; problem/outcomes/scope/non-goals; drivers/scenarios; context/ownership; decisions and strongest credible alternatives; decisive criteria/gates when comparison mattered; implementation design; Architecture Contract; failure/recovery/migration; proof; simplification ceilings/revisit triggers; and risks/gaps/linked evidence.

Use the compact durable template only when persistence is required. Omit empty optional detail rather than filling a schema for completeness.

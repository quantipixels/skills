---
name: architect
description: Design or review the technical structure of a software system or consequential module at the smallest scale needed to resolve the architecture question. Use for system boundaries, module/interface/seam shape, data/state ownership, integrations, deployment, quality scenarios, trade-offs, migration/recovery, or architecture sufficiency; exclude initiative lifecycle planning, user-decision closure, implementation, workspace infrastructure, and code-review verdicts.
---

# Architect

Own the technical structure of a software system or consequential module. Resolve the architecture question at the smallest scale that is materially sufficient: a bounded module question gets a bounded design answer; a system-wide design gets the system depth it actually needs.

| Mode | Purpose |
| --- | --- |
| `design` | create or revise the technical structure |
| `review` | judge one exact architecture/design candidate read-only |

Do not turn every design question into a full implementation-ready architecture packet. Use an implementation-readiness result only when the caller explicitly needs a gate, delivery would otherwise have to invent a material technical requirement, or the architecture spans enough consequential concerns that readiness itself is the useful result.

## Understand the architecture question

Pin only what can change the technical design: subject/candidate, problem or desired outcome, scope/non-goals, material constraints/drivers, current relevant structure, and evidence limits.

Read only evidence capable of changing the architecture: current domain/project knowledge, code/tests/configuration when implementation exists, runtime/deployment/operations evidence, governing decisions, and bounded history/provenance where it explains current structure. Observed implementation proves current structure or behavior, not automatic architectural intent.

Use `amose` when unresolved project/domain meaning or invariants materially change the technical structure. Reading established domain language does not require an `amose` handoff.

Resolve only unknowns capable of changing the architecture. Prefer exact current project/platform evidence and authoritative owning sources. Use `iwadi` when the research itself deserves an independent reusable result rather than expanding `architect` into a research workflow.

## Design the smallest sufficient structure

Design from owned responsibilities and real boundaries inward. Specify only the concerns material to the question:

- ownership and system/subsystem boundaries;
- modules, interfaces, seams, and adapters;
- data/state/identity ownership and consistency;
- dependencies and integrations, including failure semantics;
- trust/security/privacy boundaries;
- deployment/runtime/configuration/operations when they shape the design;
- compatibility, migration, rollback, recovery, or deletion when material; and
- critical invariants implementation must preserve.

When module/interface/seam shape is material, read [module design](references/module-design.md). Prefer deep modules with small high-leverage interfaces and strong locality. Do not expose internal seams merely because implementation or tests use them.

Every architectural element must pay for itself with a material driver or independently real boundary. Prefer the smaller direct structure only when removing a service, queue, datastore, cache, module, interface, adapter, abstraction, or deployment unit loses no required responsibility and does not push required complexity, policy, state, trust, lifecycle, compatibility, or failure knowledge into callers or another worse owner.

### Compare alternatives only when the design is genuinely open

Apply hard constraints first: accepted behavior, security/privacy/trust, required compatibility, ownership/lifecycle, recovery/changeover, and explicit non-goals.

When several credible structures remain and at least two independent criteria can materially change the choice, compare only decision-changing factors such as depth, locality, caller burden, operational load, migration cost, reversibility, compatibility, failure containment, or total system complexity. State the strongest credible alternative and decisive reason for the selected structure. Do not create a universal architecture scorecard.

When a technical choice is reversible within accepted constraints and authority, `architect` may select it. When the choice changes accepted outcome, scope, policy, user experience, material cost/risk, compatibility, or another trade-off requiring user authority, surface the unresolved choice and its architecture consequence; use `arojinle` for decision closure rather than deciding it here.

## Verify architectural sufficiency

Architecture must be coherent and falsifiable, but `architect` does not own delivery proof mechanics. State the critical invariants and ensure there is a credible way to verify the consequential claims. Name a specific enforcement/proof mechanism only when that mechanism materially shapes the architecture.

For a bounded design question, return the selected technical structure, decisive trade-offs, critical invariants, and unresolved gaps directly.

When implementation readiness is the requested or required result, read [architecture contract](references/architecture-contract.md) and return one:

- `IMPLEMENTATION_READY` — every material driver is covered, ownership/interfaces/invariants are coherent, and implementation needs no invented material technical requirement;
- `NOT_READY` — a material technical decision, conflict, migration/recovery obligation, or architecture defect remains; or
- `UNPROVED` — missing/stale evidence prevents responsible judgment.

Keep confidence separate from readiness when evidence strength materially helps interpretation. Confidence never converts `UNPROVED` into readiness.

## Review mode

In `review`, pin the exact architecture/design candidate and stay read-only. Judge the design at its existing scale rather than expanding it into a larger architecture exercise. Trace material drivers and invariants to the structure, challenge missing ownership/interfaces as well as unnecessary layers, and return the smallest evidence-backed correction or unresolved gap.

Use `html-artifact` only when a visual human view materially improves a substantial architecture comparison/review/handoff. The architecture result remains authoritative.

## Persistence

Keep ordinary bounded architecture work in current context. Persist only when the caller/workflow needs durable identity, cross-session/owner handoff, recovery, or an implementation-readiness record. Prefer an existing/user-selected destination; repository workspace mechanics remain outside `architect` semantics.

When persistence is required, use the compact [architecture record](templates/architecture-record.md). A persisted bounded design does not acquire an implementation-readiness status merely because it is durable; include readiness only when readiness itself is the result.

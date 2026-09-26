# Design technical structure

Read [architecture orientation](../references/engineering/architecture/orientation.md). Own the smallest materially sufficient design; implementation, initiative progression and independent code-review verdicts remain separate.

Do not turn every design question into a full implementation-ready architecture packet. Use an implementation-readiness result only when the caller explicitly needs a gate, delivery would otherwise have to invent a material technical requirement, or the architecture spans enough consequential concerns that readiness itself is the useful result.

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

When module/interface/seam shape is material, read [module design](../references/engineering/architecture/module-design.md). Prefer deep modules: small interfaces that hide substantial owned complexity and reduce caller burden. Use CUPID—composable, focused on one coherent purpose, predictable, idiomatic and domain-based—as a design lens, not a scorecard. Preserve locality; do not expose internal seams merely for implementation or tests.

When correctness depends on multiple writers or overlapping transactions over shared mutable state, read [shared-state design](../references/engineering/architecture/shared-state.md).

When the requested system creates or materially changes agent tools, an assistant/automation surface, or agent-accessible product behaviour, read [agent-facing systems](../references/engineering/architecture/agent-native-systems.md). Do not introduce an agent surface for unrelated work.

Apply YAGNI and KISS to the whole system: every element needs a material driver or real boundary. Remove layers only when required responsibilities survive without increasing caller burden or displacing complexity into a worse owner; fewer components alone is not simplification.

### Compare alternatives only when the design is genuinely open

Apply hard constraints first: accepted behavior, security/privacy/trust, required compatibility, ownership/lifecycle, recovery/changeover, and explicit non-goals.

When several credible structures remain and at least two independent criteria can materially change the choice, compare only decision-changing factors such as depth, locality, caller burden, operational load, migration cost, reversibility, compatibility, failure containment, or total system complexity. State the strongest credible alternative and decisive reason for the selected structure. Do not create a universal architecture scorecard.

Select reversible technical choices within accepted constraints. Ask a single already-understood bounded consequential choice directly. Use [arojinle](arojinle.md) when desire, consequential trade-offs or latent dependent choices remain unsettled, or an interview is requested. Reuse accepted choices rather than reopening them merely because architecture is active.

## Verify architectural sufficiency

Architecture must be coherent and falsifiable, but [architect-design](architect-design.md) does not own delivery proof mechanics. State the critical invariants and ensure there is a credible way to verify the consequential claims. Name a specific enforcement/proof mechanism only when that mechanism materially shapes the architecture.

For a bounded design question, return the selected technical structure, decisive trade-offs, critical invariants, and unresolved gaps directly.

When implementation readiness is the requested or required result, read [architecture contract](../references/engineering/architecture/architecture-contract.md) and return one:

- `IMPLEMENTATION_READY` — every material driver is covered, ownership/interfaces/invariants are coherent, and implementation needs no invented material technical requirement;
- `NOT_READY` — a material technical decision, conflict, migration/recovery obligation, or architecture defect remains; or
- `UNPROVED` — missing/stale evidence prevents responsible judgment.

Keep confidence separate from readiness when evidence strength materially helps interpretation. Confidence never converts `UNPROVED` into readiness.

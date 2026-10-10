# Design the smallest sufficient structure

Design from owned responsibilities and real boundaries inward. Specify only the concerns material to the question:

- ownership and system or subsystem boundaries;
- modules, interfaces, seams and adapters;
- data, state and identity ownership and consistency;
- dependencies and integrations, including failure semantics;
- trust, security and privacy boundaries;
- deployment, runtime, configuration and operations when they shape the design;
- compatibility, migration, rollback, recovery or deletion when material; and
- critical invariants implementation must preserve.

When module, interface or seam shape is material, read [module design](module-design.md). Prefer deep modules: small interfaces that hide substantial owned complexity and reduce caller burden. Use CUPID (composable, focused on one coherent purpose, predictable, idiomatic, domain-based) as a design lens, not a scorecard. Preserve locality; do not expose internal seams merely for implementation or tests.

When correctness depends on multiple writers or overlapping transactions over shared mutable state, read [shared-state design](shared-state.md).

When the system creates or materially changes agent tools, an assistant or automation surface, or agent-accessible product behaviour, read [agent-facing systems](agent-native-systems.md). Do not introduce an agent surface for unrelated work.

Apply YAGNI and KISS to the whole system: every element needs a material driver or a real boundary. Remove layers only when required responsibilities survive without increasing caller burden or displacing complexity into a worse owner; fewer components alone is not simplification.

## Compare alternatives only when the design is genuinely open

Apply hard constraints first: accepted behavior, security, privacy and trust, required compatibility, ownership and lifecycle, recovery and changeover, and explicit non-goals.

When several credible structures remain and independent criteria can change the choice, compare the decisive factors such as locality, caller burden, operational load, migration cost, reversibility, compatibility and failure containment. State the strongest credible alternative and why the selected structure wins. Do not create a universal scorecard.

Select reversible technical choices within accepted constraints. Ask a single already-understood bounded consequential choice directly. When desire, consequential trade-offs or latent dependent choices remain unsettled, or an interview is requested, return that need to the caller. Reuse accepted choices rather than reopening them because architecture is active.

## Architectural sufficiency

Architecture must be coherent and falsifiable. State the critical invariants and make sure there is a credible way to verify the consequential claims. Name a specific enforcement or proof mechanism only when it materially shapes the architecture.

When implementation readiness is the requested or required result, read [architecture contract](architecture-contract.md) and return one:

- `IMPLEMENTATION_READY`: every material driver is covered, ownership, interfaces and invariants are coherent, and implementation needs no invented material technical requirement;
- `NOT_READY`: a material technical decision, conflict, migration or recovery obligation, or architecture defect remains; or
- `UNPROVED`: missing or stale evidence prevents responsible judgment.

Keep confidence separate from readiness when evidence strength helps interpretation. Confidence never converts `UNPROVED` into readiness.

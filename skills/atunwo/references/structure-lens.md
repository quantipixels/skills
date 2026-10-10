# Structure lens

Use when the subject is an exact architecture or design candidate (a design doc, proposal or the structure of existing code) rather than a code diff. The review is read-only.

Pin the exact candidate. Judge the design at its existing scale; do not expand it into a larger architecture exercise. A bounded module question gets a bounded judgment.

- Trace the material drivers and invariants to the structure. A design is sound only if each driver has an owner and each critical invariant has a place it is kept.
- Challenge missing ownership and interfaces as well as unnecessary layers. Removing a layer is a gain only when its responsibilities survive without more caller burden or displaced complexity; fewer components alone is not simplification.
- Check that the structure fits confirmed purpose, domain and quality drivers. An existing design does not establish its own fitness; sufficient current fitness evidence earns a skip. A review does not authorize a redesign.
- Where several credible structures remain, judge whether the candidate beat its strongest alternative on the factors that decide it (locality, caller burden, operational load, migration cost, reversibility, compatibility, failure containment), not on a scorecard.
- Read the project's architecture overview as an orientation map, not proof; verify the material claims against current code, tests and configuration. Observed implementation proves structure and behavior, not architectural intent.

Return the smallest evidence-backed correction direction or the unresolved gap. When the structure needs real redesign (open alternatives, unsettled ownership, a new boundary), say so and return the need for a design to the caller; do not design it here. For module, interface or seam judgments, the yardstick is deep modules, locality and CUPID.

For substantial user-facing findings, ask `fihanmi` for a view when it helps.

# Review architecture

Read [architecture orientation](../references/architect/orientation.md). Stay read-only, including persistence; an overview update is a separate command.

In `review`, pin the exact architecture/design candidate and stay read-only. Judge the design at its existing scale rather than expanding it into a larger architecture exercise. Trace material drivers and invariants to the structure, challenge missing ownership/interfaces as well as unnecessary layers, and return the smallest evidence-backed correction or unresolved gap.

Use [html-artifact](html-artifact.md) as needed.


Use the applicable [module-design](../references/architect/module-design.md), [shared-state](../references/architect/shared-state.md), [agent-facing systems](../references/architect/agent-native-systems.md), or [architecture-evolution](../references/architect/architecture-evolution.md) lenses when they control the judgment. These supply assessment criteria, not redesign authority.

When the requested result is implementation readiness, use the [architecture contract](../references/architect/architecture-contract.md) and return IMPLEMENTATION_READY, NOT_READY or UNPROVED with decisive evidence. Otherwise return findings, the smallest supported correction direction and coverage limits.

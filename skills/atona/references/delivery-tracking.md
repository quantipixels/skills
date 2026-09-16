# Delivery tracking

Use when a plan has multiple work units or candidates, owners, dependencies, or a multi-session handoff. Use [delivery decomposition](decomposition.md) when tickets help; consume a stronger owner-native model when one exists. Missing, ambiguous or cyclic required decomposition keeps affected work unready.

Semantic work units do not prescribe branches, commits, PRs/MRs, sessions, documents or deployment units. Choose operational containers for review, integration, recovery, ownership and evidence. Prefer one integration branch and review unit for one coherent change; split only independently useful, safely reviewable units.

Keep dependencies, owner results, proof gaps, blockers, documentation destinations and the delivery summary current. Before material delivery, record a lightweight **delivery-shape envelope**: expected owners/workstreams or affected systems/surfaces, proof owners, new dependencies/public contracts, and handoff/review topology. It is an expectation and drift detector, never a quota or frozen inventory.

Use existing delivery authority. Track `alaga` or another delivery owner by scope, candidate/result identity, freshness, accepting evidence, blockers, plan effect and next action; keep its execution and corrections with that owner. Limit active work to what current integration and verification capacity can absorb. A ticket becomes `Done` only from exact-current acceptance evidence; cancellation needs its own authority.

## Reconcile changes

Verify each result against the current plan and identity. Stale only dependent conclusions. For a localized contract amendment, record authority/revision, changed clause, affected result/proof, retained versus stale coverage, and required owner refresh. Use a clause-scoped map when effects span results or partial coverage is complex. Never rewrite terminal history to make an amended contract look original.

Compare cumulative actual shape with the envelope after materially shape-changing work and before consequential publication, review or handoff. Counts may describe the result but never define acceptance. Unexpected surface spread, repeated new proof owners, new contracts/dependencies, or multiplied handoffs trigger replanning when they exceed independent value. Route structural decisions to `architect` and independent code judgment to `atunwo`; their recommendations do not authorize implementation.

Derive `Complete` only when every in-scope obligation has current accepting proof and integration has no blocking gap; derive `Not required` only when the plan has no delivery. `wo-pr: PROVIDER_READY` is provider evidence, not integrated acceptance, and either side becoming stale invalidates only the dependent conclusion.

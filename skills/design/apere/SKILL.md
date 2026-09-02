---
name: apere
description: Route broad or multi-deliverable visual work to the smallest set of currently available design owners. Use when a design request is ambiguous, spans several deliverables, or needs design-specific prerequisites, dependency order, shared constraints, or approval boundaries; use the exact specialist directly for one focused deliverable.
---

# Àpẹrẹ

Own design-domain decomposition and routing. Return one route packet; do not create design artifacts, maintain delivery state, or copy specialist procedures.

## Route from current owners

Inspect the active host's available **design** skill descriptions/invocation metadata rather than maintaining a static second catalogue here. Respect an explicit user-selected design owner when it fits.

Use the exact specialist directly when one owner fully covers the requested deliverable. Use Àpẹrẹ when:

- the correct design owner is genuinely ambiguous;
- several distinct design deliverables need different owners;
- confirmed shared brand/visual/accessibility constraints must be passed consistently across owners;
- one design result is a prerequisite for another; or
- a common approval/handoff boundary must be made explicit.

Do not route backend/infrastructure work here. Do not add a design specialist merely because it exists. Missing shared constraints are prerequisite gaps or routes, not constraints Àpẹrẹ may invent.

## Design route packet

Return only what downstream owners need:

```text
Requested visual outcome and audience
Deliverables → one current primary owner each
Shared prerequisites / dependency order
Safe parallel work
Confirmed shared constraints to pass through unchanged
Requested deliverable/output constraints
Open input gaps
Route completion boundary
```

Each specialist retains its native result contract; Àpẹrẹ does not prescribe internal result schemas merely to simplify coordination.

When several routed artifacts must actually be produced or integrated, hand this packet to the current delivery/integration owner when one exists. Use `alaga` only when the integrated result is genuinely a software/build job; otherwise let the selected design owners or current host/domain delivery owner produce and integrate their native results. Àpẹrẹ does not become a delivery lifecycle owner.

A small focused design request should not pay this coordination cost; invoke its specialist directly.

# Behavior contracts and delivery slices

## Behavior contract

Describe externally observable behavior, not a preferred implementation. Establish actors, inputs/identity, allowed and denied behavior, outputs, transitions, errors, invariants and relevant effects. Include ordering, concurrency, retries, compatibility, operating limits and recovery when they change the contract.

Use canonical language; distinguish requirements, examples, current behavior and proposals. Expose unresolved requirements instead of hiding them in implementation detail. Specify acceptance observations and useful rejection cases; do not invent policy to fill a template. Existing governing specifications remain authoritative.

A standalone contract request ends at that result. It does not authorize delivery or require an initiative plan.

## Delivery decomposition

Prefer outcome-complete vertical slices a fresh engineer can understand and verify. Split by independently usable outcomes, not layer, file type, agent or proof stage. A genuinely blocking enabling capability can be its own slice; identify the integration it enables.

Each slice states outcome, necessary context, scope, acceptance, genuine dependencies and external prerequisites. Include migration/recovery when material. The owner chooses mechanics; do not prescribe one commit, PR or session per slice.

Keep dependencies acyclic and distinguish completion from cancellation. Cancelling a prerequisite requires replanning; it does not automatically unblock dependants. Show what can start now and which fact or decision blocks the rest in the existing plan, not another lifecycle ledger.

Use expand–migrate–contract when intermediate compatibility requires it. Verify the combined user journey after individual slices. Isolated passes do not establish integration. A breakdown request returns the decomposition and controlling gaps, not an unrequested delivery workflow.

# General code craft

Apply these only where the candidate triggers them.

## Express the domain directly

- Use names from the problem domain; avoid `Manager`, `Helper`, `Util`, `Processor`, and `Handler` when they hide the actual responsibility.
- Keep one abstraction level per function. Extract a concept when it hides meaningful policy or lifecycle, not merely to reduce line count.
- Prefer types/state representations that make invalid combinations impossible or hard to construct.
- Derive values when a single owner already has the source of truth; do not store duplicated state without a consistency contract.

## Keep ownership and effects visible

- Make resource, transaction, task/process, cache, retry, and lifecycle ownership explicit.
- Keep I/O and irreversible effects at clear boundaries; do not bury them in mapping/accessor-style code.
- Preserve cancellation/interruption and causal failures across boundaries.
- Bound memory, concurrency, queues, retries, remote calls, and user-controlled input.

## Prefer native depth over ceremony

- Prefer standard language/platform/framework mechanisms that already own the requirement.
- Reject pass-through layers, one-implementation interfaces, wrappers, factories, builders, mappers, or strategies unless they hide meaningful policy/integration/lifecycle or protect a real seam.
- Keep deep modules: small stable interfaces that hide significant complexity.
- Do not anticipate hypothetical variation that the task does not require.

## Keep code readable in one pass

- Prefer obvious control flow over clever chaining when the latter hides failure/order/state.
- Reduce nested conditionals by improving the representation or returning at clear boundaries; do not merely scatter branches across tiny methods.
- Use comments for non-obvious contracts, invariants, trade-offs, or external constraints—not narration of visible code.
- Keep public APIs narrower than internal implementation capability.

## Proof follows invariants

- Name the material invariant first, then choose its cheapest stable proof owner.
- Prefer compiler/type/schema/static/tool proof over runtime tests when it completely owns the invariant.
- Do not keep development scaffolding as permanent tests without distinct durable regression value.

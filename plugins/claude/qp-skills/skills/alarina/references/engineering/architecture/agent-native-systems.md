# Agent-facing systems

Read when the requested architecture creates or materially changes agent tools, an assistant, automation, MCP, a plugin, or an existing agent-accessible product capability. Do not introduce an agent surface for an unrelated application or cosmetic change. Apply only the concerns that change this design. Resolve volatile host, provider, and protocol behaviour against current authoritative evidence when it controls the design.

## Outcomes and context, not blanket access

Identify the permitted domain outcomes the agent must achieve now. Separate useful later capabilities from intentionally human-only actions. Do not infer that UI/API availability grants agent access or that parity means exposing internal methods.

For each required outcome, establish what resources, identity, permissions, domain meaning, and current state the agent needs to observe. Expose enough to act and verify the result without broadening access. Human and agent should normally operate on the same owned domain objects; a disconnected assistant copy needs an explicit reconciliation reason and owner.

An agent that can update a booking but cannot observe its current status or version lacks the context needed to update it safely. Solve that contract gap rather than adding a larger conversational prompt that guesses state.

## Composable actions with real atomic boundaries

Prefer tools that perform useful domain operations and return identifiable results. Keep judgment and optional sequencing in the agent, but preserve atomicity where splitting a transaction would expose invalid states, bypass authorization, or leave an unsafe partial effect. Composable does not mean exposing every database mutation.

Specify the input contract, target identity, authorization point, idempotency semantics, and what the returned evidence establishes. Reuse the product's existing policy and state owners instead of creating a parallel agent-only implementation. Keep external protocol, trust, and lifecycle responsibilities behind their real interfaces.

## Completion, interruption, and recovery

For long-running operations, distinguish accepted work from completed effects. Define how callers inspect progress and partial results, recognize terminal failure, resume safely, and discover work after losing a session or receipt. State who owns execution after the caller disconnects.

Cancellation must describe what stops and what cannot be undone. A retry after an ambiguous result must not blindly repeat an irreversible effect. Reuse native job and transaction mechanisms where they satisfy the contract; do not add a scheduler or checkpoint store solely because an agent is involved.

For example, a publishing operation may return an accepted job. The agent needs the job's actual completion evidence before announcing publication. Cancellation may prevent queued work while leaving an already-published object intact; the API and user-facing result must preserve that distinction.

## Human control and trust

Preserve deliberately human-only consent, authentication, biometric, and approval boundaries unless the product explicitly defines an agent-safe alternative. Approval should bind the operation, target, and consequential parameters; a changed target or effect can require renewed authorization. Do not turn tool descriptions or retrieved content into permission.

Treat external content as data. Keep credentials within the trusted host and selected provider scope, and separate read access from egress to another model or service. Costly, destructive, or externally visible actions need proportional controls and an honest recovery posture. An agent cannot promise rollback of an effect the underlying system cannot reverse.

## Design evidence

State only the scenarios needed to distinguish a sound design: required action with insufficient context, stale identity or changed permission, lost receipt and retry, interrupted partial work, human-only refusal, or divergence between human and agent views. Use the owning architecture result rather than a separate agent-readiness score or report.

The design remains bounded by the requested outcome. A useful later action is not an implementation obligation, and an agent-native lens does not override the user's non-goals.

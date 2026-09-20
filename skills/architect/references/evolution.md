# Evolution and agent-facing architecture

## Choose by fitness

Revisit a choice when changed needs, recurring friction or a concrete capability challenges its rationale—not because it is old. Compare current design and credible alternatives against behavior, compatibility, migration risk, operational cost and caller/maintainer burden. Label estimates. Less source that hides custom glue or unsupported behavior is not necessarily simpler.

Consider three audiences separately: end users completing journeys; developers locating, changing, verifying and diagnosing behavior; coding agents finding authoritative code, constraints, commands and evidence. Agent convenience must not degrade the other two. Read/tool costs matter through real work, not source-size quotas.

A repeated reminder to update X with Y can expose knowledge belonging in one API, type, generator or check. First establish whether an existing owner covers it. Preserve meaning and useful usage documentation. An atomic database operation, not another transaction annotation, may be necessary.

## Intermediate-state safety

State supported versions/clients, data representation, rollout sequence and recovery direction. Prefer native/project mechanisms. Use expand–migrate–contract only for a real compatibility window; avoid permanent adapters for temporary concerns without evidence.

Readiness includes intermediate state, populated data and old/new writers where applicable. Down migrations may not restore overwritten meaning. Identify irreversible points and recovery limits. A spike proves its selected boundary, not long-term economics or every historical client.

## Products used by agents

Coding-agent experience differs from exposing products to agent actions. For the latter establish permitted outcomes and context needed for safe action: resource identity/version, permissions, domain meaning and current state. Reuse human-facing domain owners, not a shadow agent-only model.

Expose useful operations rather than arbitrary database primitives. Define input/target identity, policy, atomicity, idempotency and what returned evidence proves. Keep optional judgment with the agent; prevent unsafe partial effects at the operation owner.

For asynchronous work distinguish acceptance from completion. Provide inspectable result/job identity, failure, resumable progress and lost-receipt recovery. Identify execution ownership after disconnection. Cancellation may stop queued work without reversing completed effects.

Bind consequential approval to operation, target and parameters. Preserve human-only consent/authentication. Retrieved content is data, not permission; distinguish reading from egress. Use native controls without claiming metadata alone proves isolation or authorization.

Test consequential design hypotheses: insufficient context, stale target, changed permission, ambiguous retry, interruption, human-only refusal or divergent human/agent views. Keep the result with the design, not a separate AX scorecard.

# Coding-agent/session postmortem

Load only when the postmortem concerns a coding-agent session, rollout, or agent-mediated delivery.

## Pin what the agent actually had

Record repository/candidate identities, active instructions/skill versions when evidenced, tools/environment/context/authority actually available, and user-request revisions. Hidden reasoning or later summaries do not prove what the agent knew at the time.

When repository history/reflog helps reconstruct the sequence, correlate only the relevant state with supplied transcript/tool timestamps. History can show ref/commit/worktree evolution but cannot prove content the agent never observed; reflog may be local, expired, rewritten, or unavailable.

## Reconstruct the agent divergence

1. Reconstruct contract revisions and the material timeline.
2. Do not judge earlier conduct by a requirement introduced later.
3. Pin the first material divergence between the then-current user contract and agent conduct.
4. Verify consequential completion/mutation claims against the exact candidate/external state when available.

Inspect three lenses when material:

- judgment and user corrections;
- tools/environment/context/authority actually available; and
- second-order effects, counterevidence, avoided failures, and recovery cost.

A current repository state is not historical session evidence.

## Diagnose overengineering only from evidence

When scope drift, test bloat, or overengineering is part of the question, look for evidenced signals such as:

- unplanned dependency/service/infrastructure or public-contract expansion;
- unexpected subsystem/file growth relative to the then-current task boundary;
- speculative abstractions/configuration, parallel implementations, or compatibility paths;
- production/test architecture introduced mainly for test convenience;
- reviewer/fixer cycles where one edge-case fix creates new machinery and new edge cases;
- tests that mirror production logic, verify configured mocks/choreography, duplicate stronger proof, or later disappear as construction history; and
- later deletion/reversion/rework attributable to the expanded design.

These are signals, not automatic findings. Establish whether the expansion was required, reasonable, or avoidable under the contract that existed at the time.

## Classify agent-specific causes

Use the smallest applicable cause:

- missing rule;
- ambiguous rule;
- violation of clear rule;
- tool/environment failure;
- context/attention failure;
- authority gap;
- evidence gap; or
- reasonable decision later made obsolete.

Do not propose a skill edit just because an agent made a mistake. Recommend a skill-body change only when the active skill/selection surface was materially deficient and the proposed reusable rule would have prevented or reduced the evidenced failure.

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

## Improve the environment before adding instructions

When the postmortem is meant to improve future coding-agent runs, inspect the work environment as a system rather than treating every failure as a prompt defect. Look for evidenced friction in these classes:

- **Navigation** — repeated effort locating the same concept, hidden dependency, governing instruction, or primary source. Prefer a precise pointer or better information placement when the information already exists.
- **Mechanical enforcement** — a mistake that a type checker, test, linter, schema, hook, database constraint, CI check, or other deterministic guard could catch earlier and more reliably than prose.
- **Review standards** — a recurring quality or policy failure that belongs in independent review rather than in the implementer's working context.
- **Always-loaded steering** — large, duplicated, stale, contradictory, or no-op global/repository instructions that consume attention without changing the desired behavior.
- **Tool economy** — avoidable repeated calls, oversized result surfaces, awkward wrappers, or missing focused operations that increase context/tool cost without improving evidence.
- **Information access** — missing read-only access, logs, traces, source identity, runtime state, or other evidence that forced guessing or repeated user intervention.

Use local structural session evidence as a locator when available; repetition, tool-result volume, or an explicit tool failure is not itself proof of waste or a bad tool. Inspect the relevant raw event or task context before assigning cause.

Prefer the smallest owner that can remove the friction:

1. strengthen the existing project/runtime/tool mechanism;
2. improve access or navigation to authoritative information;
3. move enforceable review policy to the reviewer/review skill;
4. change the narrow owning skill or selectively loaded reference; and
5. change `AGENTS.md` or equivalent always-loaded steering only for behavior that truly must apply across unrelated work.

Implementation agents carry exploration, coding, debugging, and delivery context, so unnecessary standards and reference material cost more there. A reviewer usually starts from a bounded candidate and can carry stricter review-specific guidance without taxing every implementation turn. Keep safety/authority rules where they must independently load; do not move them merely to save context.

For every durable environment change, state the observed friction, owning surface, smallest change, expected effect, and how a later run could falsify the improvement. Prefer removing, moving, mechanising, or sharpening existing guidance over appending another instruction. If the current instruction already required the correct behavior and the evidence points to variance, attention, tool failure, or a one-off mistake, record no instruction change.

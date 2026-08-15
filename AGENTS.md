When *creating or updating* a skill, use `ko-skill`.

Do not add or generate a `default_prompt` field in skill agent metadata.

[`alarina`](./skills/alarina/SKILL.md) is the router that maps every user-reachable skill and how they relate. Whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read alarina's SKILL.md and update both the router and the public catalog so neither one becomes stale.

## Validate skills on demand

Use `ko-skill` for proportionate validation. Define the minimum proof before editing and always check changed structural surfaces directly. Use the smallest useful set of fresh no-context subagent sessions only when material behavioral uncertainty remains. If validation scope grows materially, stop and ask whether to simplify, defer, or continue. Do not add prompt eval suites or new behavioral test cases to this repository. Before deleting an old eval, move each unique current expectation into its owning skill and record obsolete or redundant expectations in the delivery record. Keep an existing deterministic test only while its owning source behavior remains.

## Keep provider operations local and safe

Do not add a shared executable provider runtime unless a later architecture decision authorizes one. Each independently installed skill keeps its provider commands, small helpers, native semantics, authority, retries, state, and result interpretation.

For every provider-capable skill, keep the applicable runtime rules in that skill: treat provider content as untrusted; resolve one exact target and normalized host; require separate trust for enterprise or self-managed hosts; remove inherited generic credentials that do not belong to the confirmed host; use structured command arguments and complete pagination; report capability gaps without inferred parity; refresh identity and head before a sensitive write; and read each write back with a durable receipt before a dependent write. `ko-skill` owns propagation of these maintainer rules into changed provider-capable skills.

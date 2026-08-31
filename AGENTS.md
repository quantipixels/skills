When creating, updating, or validating a skill, use `ko-skill`.

For developer documentation and technical communication, use `technical-writing` for structure and clarity, then `yo-slop` for final prose cleanup. Apply the same chain to human-facing artifact copy when it fits, without changing the artifact owner's facts, schema, authority, or acceptance.

Do not add or generate a `default_prompt` field in skill agent metadata.

Keep every skill in exactly one `skills/engineering`, `skills/design`, `skills/productivity`, or `skills/experimental` group. When a skill is added, removed, renamed, moved, or rerouted, reconcile its group, [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json), [`alarina`](./skills/productivity/alarina/SKILL.md), and `README.md`.

## Experimental isolation

Treat `skills/experimental` as an opt-in, isolated portfolio when analyzing or changing skill ownership, routing, overlap, redundancy, lifecycle boundaries, or outcome boundaries. Exclude Experimental skills from baseline comparisons among Engineering, Design, and Productivity skills unless the user explicitly includes an experiment or the change directly affects it.

An Experimental skill does not become a stable owner, prerequisite, or reason to remove, narrow, merge, or reroute a non-Experimental owner merely because the experiment exists or succeeds once. However, exact-current evidence from an explicitly selected experiment may inform a later `ko-skill` promotion, consolidation, or stable-owner decision when that evidence is evaluated for recurrence/generality and the stable portfolio remains authoritative until the decision is made.

When a change directly affects an Experimental skill, reconcile its group, manifest, router, README entry, and explicit stable-skill dependencies without treating the experiment as a baseline owner.

## Evaluation policy

Do not add standing prompt-evaluation suites merely to defend wording. Temporary realistic steering-effect comparison is allowed when a model-steering change has material behavioral uncertainty: compare the same bounded task/candidate/context under the prior or absent contract and the changed contract, then verify both the intended behavior shift and preserved correctness/safety.

Persist a behavioral regression suite only when recurring stable risk justifies its maintenance. Before deleting an old eval, move each unique current expectation into its owning skill and record obsolete or redundant expectations in the delivery record. Keep deterministic tests only while they prove current source behavior or package/mechanical invariants.

## Provider policy

Keep provider execution within its independently installed owning skill. Do not add a shared executable provider runtime without an architecture decision. Each provider-capable skill must own applicable rules for untrusted content, exact target and normalized-host trust, credential isolation, structured requests, complete pagination, capability gaps, pre-write identity and head refresh, and post-write readback receipts. `ko-skill` propagates this contract.

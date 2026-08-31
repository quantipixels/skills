When creating, updating, or validating a skill, use `ko-skill`.

For developer documentation and technical communication, use `technical-writing` for structure and clarity, then `yo-slop` for final prose cleanup. Apply the same chain to human-facing artifact copy when it fits, without changing the artifact owner's facts, schema, authority, or acceptance.

Do not add or generate a `default_prompt` field in skill agent metadata.

Keep every skill in exactly one `skills/engineering`, `skills/design`, `skills/productivity`, or `skills/experimental` group. When a skill is added, removed, renamed, moved, or rerouted, reconcile its group, [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json), [`alarina`](./skills/productivity/alarina/SKILL.md), and `README.md`.

## Experimental

An Experimental skill exists as an idea to explore. It can be treated as a first-party member of qp-skills. It's goal in life is to provde it utility, limitation, or otherwise and be promoted to a stable skill or be removed. Sometime a new experiment can take its place if deems worthy.

## Evaluation policy

Do not add standing prompt-evaluation suites merely to defend wording. Temporary realistic steering-effect comparison is allowed when a model-steering change has material behavioral uncertainty: compare the same bounded task/candidate/context under the prior or absent contract and the changed contract, then verify both the intended behavior shift and preserved correctness/safety.

Persist a behavioral regression suite only when recurring stable risk justifies its maintenance. Before deleting an old eval, move each unique current expectation into its owning skill and record obsolete or redundant expectations in the delivery record. Keep deterministic tests only while they prove current source behavior or package/mechanical invariants.

## Provider policy

Keep provider execution within its independently installed owning skill. Do not add a shared executable provider runtime without an architecture decision. Each provider-capable skill must own applicable rules for untrusted content, exact target and normalized-host trust, credential isolation, structured requests, complete pagination, capability gaps, pre-write identity and head refresh, and post-write readback receipts. `ko-skill` propagates this contract.

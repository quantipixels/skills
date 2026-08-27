When creating, updating, or validating a skill, use `ko-skill`.

For developer documentation and technical communication, use `technical-writing` for structure and clarity, then `yo-slop` for final prose cleanup. Apply the same chain to human-facing artifact copy when it fits, without changing the artifact owner's facts, schema, authority, or acceptance.

Treat supporting skills as deep modules. Tell the owner the outcome or representation needed and consume its result; do not copy its internal procedure, lifecycle, verification, layout, or resource-management instructions into callers. For `html-artifact`, normally state what should be visualised and whether HTML is the primary human view, then let `html-artifact` own the representation.

Do not add or generate a `default_prompt` field in skill agent metadata.

Keep every skill in exactly one `skills/engineering`, `skills/design`, `skills/productivity`, or `skills/experimental` group. When a skill is added, removed, renamed, moved, or rerouted, reconcile its group, [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json), [`alarina`](./skills/productivity/alarina/SKILL.md), and `README.md`.

## Experimental isolation

Treat `skills/experimental` as an opt-in, isolated portfolio when analyzing or changing skill ownership, routing, overlap, redundancy, lifecycle boundaries, or outcome boundaries. Exclude Experimental skills from comparisons among Engineering, Design, and Productivity skills unless the user explicitly includes an experiment or the change directly affects it. Do not use an Experimental skill to justify removing, narrowing, merging, or rerouting a non-Experimental owner.

When a change directly affects an Experimental skill, reconcile its group, manifest, router, README entry, and explicit stable-skill dependencies without treating the experiment as a baseline owner.

## Evaluation policy

Do not add prompt-evaluation suites or new behavioral tests. Before deleting an old eval, move each unique current expectation into its owning skill and record obsolete or redundant expectations in the delivery record. Keep a deterministic test only while it proves current source behavior.

## Provider policy

Keep provider execution within its independently installed owning skill. Do not add a shared executable provider runtime without an architecture decision. Each provider-capable skill must own applicable rules for untrusted content, exact target and normalized-host trust, credential isolation, structured requests, complete pagination, capability gaps, pre-write identity and head refresh, and post-write readback receipts. `ko-skill` propagates this contract.

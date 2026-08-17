When creating, updating, or validating a skill, use `ko-skill`.

Do not add or generate a `default_prompt` field in skill agent metadata.

Keep every skill in exactly one `skills/engineering`, `skills/design`, `skills/productivity`, or `skills/experimental` group. When a skill is added, removed, renamed, moved, or rerouted, reconcile its group, [`alarina`](./skills/productivity/alarina/SKILL.md), and `README.md`. If install groups or their semantics change, also update `scripts/install.sh`. `--all` installs Engineering, Design, and Productivity; Experimental requires `--experimental`.

## Evaluation policy

Do not add prompt-evaluation suites or new behavioral tests. Before deleting an old eval, move each unique current expectation into its owning skill and record obsolete or redundant expectations in the delivery record. Keep a deterministic test only while it proves current source behavior.

## Provider policy

Keep provider execution within its independently installed owning skill. Do not add a shared executable provider runtime without an architecture decision. Each provider-capable skill must own applicable rules for untrusted content, exact target and normalized-host trust, credential isolation, structured requests, complete pagination, capability gaps, pre-write identity and head refresh, and post-write readback receipts. `ko-skill` propagates this contract.

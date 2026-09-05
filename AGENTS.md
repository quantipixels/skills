When creating, updating, or validating a skill, use `ko-skill`.

For developer documentation and technical communication, use `technical-writing` when structure or technical clarity needs an owning pass. Use `yo-slop` only when cleanup/pruning is itself requested or material filler, AI-tells, repetition, or instruction noise remains after the owning content work; do not make it a routine second pass. Apply the same boundary to human-facing artifact copy without changing the artifact owner's facts, schema, authority, or acceptance.

Do not add or generate a `default_prompt` field in skill agent metadata.

Keep every skill in exactly one `skills/engineering`, `skills/design`, `skills/productivity`, or `skills/experimental` group. When a skill is added, removed, renamed, moved, or rerouted, reconcile its group, [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json), [`alarina`](./skills/productivity/alarina/SKILL.md), and `README.md`.

Grow capability depth faster than public surface area. Prefer deepening an existing owner through owner-local guidance, selective references, native capabilities, or internal paths when it can carry the behavior coherently. A new public skill must make direct selection or use materially simpler than keeping that capability behind an existing owner; do not expose internal composition merely to name another reusable method.

## Experimental

Experimental skills are first-party runtime candidates whose maturity is under evaluation. Experimental status alone does not require separate user acceptance and does not make a skill ineligible for normal routing. Use one when its owned outcome is the narrowest useful match and its normal intent, authority, cost, safety, and host invocation gates are satisfied; never invoke one merely to generate experiment data.

Host invocation metadata may deliberately require direct user activation for an intent island without changing the portfolio status of the skill. Experimental status constrains portfolio evolution, not ordinary invocation. Do not make an experiment an unconditional prerequisite, let one successful use redefine/remove/narrow a stable owner, or promote it without evidence across real eligible work. Evaluate whether it was discoverable when eligible, selected correctly, added independent value, imposed justified cost, and preserved owner boundaries. Rare outcomes are not failures merely because invocation count is low. Promote, keep experimenting, narrow/fold, replace, or remove from that evidence.

## Evaluation policy

Do not add standing prompt-evaluation suites merely to defend wording. Temporary realistic steering-effect comparison is allowed when a model-steering change has material behavioral uncertainty: compare the same bounded task/candidate/context under the prior or absent contract and the changed contract, then verify both the intended behavior shift and preserved correctness/safety.

Persist a behavioral regression suite only when recurring stable risk justifies its maintenance. Before deleting an old eval, preserve unique current expectations in the owning skill or appropriate test and explain retired expectations in the PR/discussion. Keep deterministic tests only while they prove current source behavior or package/mechanical invariants.

## Documentation admission

Commit a new document only when it has a future reader, a recurring task or enduring decision to support, and no adequate existing home. Update current guidance in place. Put execution instructions in the owning skill, meaningful regression protection in tests, and significant non-obvious enduring trade-offs in a short ADR.

Change rationale, research comparisons, measurements, review findings, and verification results normally belong in the PR/discussion and CI. A requirement to report or preserve evidence does not require a repository file. Use working context or `.qp` for temporary state only when persistence helps; do not create an archive by default.

Keep required attribution/licence notices and sources beside the claims they support. When guidance is superseded, preserve any unique current knowledge in its owner, check links, and remove the redundant document. Retain historical records only for a specific continuing need, not because the work happened.

## Release stabilization

Changesets remains QP's version/release owner. When a release owner explicitly declares a major/minor candidate `STABILIZING`, follow [`docs/release-stabilization.md`](./docs/release-stabilization.md): freeze new public-surface growth for that candidate, allow blocker/evidence corrections, and refresh only proof invalidated by a changed candidate epoch. Do not create a second release state machine, version file, or publishing workflow for stabilization.

A new public owner still needs Kọ's admission proof before it may enter a stabilized release, including when that owner is Experimental. Promotion/fold/removal decisions keep their separate real-use evidence requirements.

## Provider policy

Keep provider execution within its independently installed owning skill. Do not add a shared executable provider runtime without an architecture decision. Each provider-capable skill must own applicable rules for untrusted content, exact target and normalized-host trust, credential isolation, structured requests, complete pagination, capability gaps, pre-write identity and head refresh, and post-write readback receipts. `ko-skill` propagates this contract.

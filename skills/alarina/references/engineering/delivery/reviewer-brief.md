# Reviewer brief

Help the reviewer understand why the change exists, see its implementation shape, inspect proof and judge recovery without reconstructing the author's session.

Read the actual candidate/diff, applicable domain language, relevant decisions and available proof. Pin head/base for live repository claims; supplied partial evidence stays partial. Use established [amose](../../../commands/amose.md) results or the project's canonical terms, states, actors and invariants; invoke [amose](../../../commands/amose.md) only for consequential unresolved meaning. Do not invent a glossary or substitute implementation names for business concepts.

## Write in review order

Preserve the repository template, human context, issue links and accepted decisions. Within that structure, or as the default when none exists:

1. **Why the change:** lead with a short statement of the problem and changed outcome, normally one sentence.
2. **Special things to note:** put material warnings, compatibility/migration constraints, deliberate omissions and risk/recovery where the reviewer will see them before inspecting the change. Omit empty notes; never hide a blocker in disclosure.
3. **Change outline:** use [fihanmi](../../../commands/fihanmi.md) for the smallest useful structural view beside its consequence. Lead with a changed schema, endpoint contract or key type when it explains the downstream logic; otherwise use the relevant pseudocode, state/call/component tree, shallow responsibility map or actual captured UI. Order by understanding, not filenames. Point to the real path/symbol or pinned source where judgment matters.
4. **Evidence:** show what was exercised, its actual result and its limit. Put proof beside its claim when clearer than a separate section; link or collapse long logs, not failures or missing proof.

These are content slots, not mandatory headings or quotas. A small documentation fix can be one paragraph. Use a conceptual diff for a change to an existing shape; show the whole target when mostly new or needed to preserve ownership/order. Label sketches as conceptual, not literal source or execution proof. Preserve asynchronous, transaction and external-effect boundaries. Omit irrelevant views, file inventories, session narration and unsupported praise. [oro-eniyan](../../../commands/oro-eniyan.md) owns prose; use precise domain language, not a blanket ban on jargon.

The body must work in native provider Markdown. Do not require HTML, a `.humanlayer` task directory, a saved description sidecar or a separate final-answer template. Use existing source/evidence locations; never invent links to complete the layout.

## Prove the changed claim

Reuse current proof. Capture or rerun only what closes a material gap under existing authority; missing tools/access become an explicit gap and next check, not a new harness.

For a check, identify the command/provider run, concise observed result, relevant environment and candidate, including uncommitted changes affecting proof. Explain coverage rather than merely counting passing tests. Distinguish supplied results, executed observations, earlier-candidate proof, illustrative examples and not-run checks. Older evidence is reusable only when applicability is established; otherwise mark it stale.

Match proof to the change: actual captures/recordings for UI states; request/response, traces or focused behavior tests for APIs/backends/CLIs; representative populated-data, compatibility and recovery checks for migrations; comparable workloads, units and environments for performance. For instructions/docs, distinguish source/package checks from model behavior or observed human use. A screenshot proves its captured state, not the whole flow; an empty-database migration test does not prove existing-data safety.

Never fabricate output, passing status, images or URLs. Diagrams and generated images explain; they do not prove execution. Keep failures, skips and material coverage gaps visible. Use reviewer-accessible links or attachments, not local/sandbox paths; disclose inaccessible or expiring evidence. Redact sensitive data without concealing the failure.

## State risk and the recovery boundary

Give a qualitative risk with its concrete reason, considering affected scope, compatibility, permissions, state and external effects where relevant. Name when the effect activates: merge, deployment, migration, flag enablement or a later operation. Small diffs, passing CI and `git revert` do not establish low risk.

Classify the relevant effect, not merely the code:

- **Two-way:** a practical action restores behavior and state. Name the action, prerequisites and whether recovery was exercised.
- **One-way:** rollback cannot undo a material effect. Identify the point of no return and mitigation/recovery limit.
- **Mixed:** separate reversible code/configuration from irreversible or costly data/external effects.
- **Unknown:** missing evidence prevents the judgment. Name what would settle it; do not default to low risk.

For consequential changes, include established rollout guards, stop signals and recovery actions, or state the missing proof. A flag or down migration does not recover deleted data or recall external effects. Assessment authorizes no destructive exercise; an author assessment is not independent approval. Use [atunwo](../../../commands/atunwo.md) for material contested judgment, not automatically for every body.

Before returning or publishing, check that the reviewer can explain the effect, locate its proof and important decision, and see the uncertainty and recovery limit. Do not claim faster review without observed reader use or matched evaluations.

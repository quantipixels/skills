# Reconciliation boundaries

Use for conflicts, generated or historical sources, and changes that might remove knowledge. These judgments supplement ordinary factual corrections; they are not a mandatory rewrite pass.

## Contradiction or product defect?

Compare claims about the same version, audience and conditions before declaring a conflict. Keep the conflicting statements and decisive source locators together. Current implementation establishes current mechanics, not automatically the intended rule.

For example, an accepted policy requires approval before an export, but the endpoint no longer checks approval. Preserve the independently supported policy and report the potential product regression. If the README instead lists a removed command and the supported replacement is established, correct the instruction. If neither side has adequate evidence, preserve the uncertainty and request only the missing decision or evidence.

Check relevant instructions at their point of use: a runbook or local skill can contradict a correct overview without containing any broken links. Correct a proved instruction error through [oro-sigidi](../../../commands/oro-sigidi.md) when edit authority covers it; unresolved meaning returns to [amose](../../../commands/amose.md) or [architect-design](../../../commands/architect-design.md). Do not propagate the same unsupported claim into every document to make them agree.

## Generated sources and examples

Find the authoritative input and project-supported generation path. Change documentation inputs, templates or comments only within the granted scope; regenerate affected output when safe and authorized. Do not hand-edit generated output as a substitute or change executable schemas, configuration or product behavior merely to match prose.

A schema describing a real API is not necessarily a documentation-only file. When its correction would alter the product contract or generated clients, return that obligation to [alaga-deliver](../../../commands/alaga-deliver.md) and the caller. If generation is unavailable, report the source correction and stale output separately; do not call the generated reference current.

Exercise a consequential example in an isolated, appropriate environment when permitted. Do not run deployment, destructive, privileged or externally mutating commands merely to test documentation. Describe what was checked statically and what remains unexecuted. In `audit`, choose non-mutating checks or report the needed exercise.

## Historical and versioned records

Preserve the claims a historical ADR, changelog or supported older-version guide made at its own revision. A successor can supersede an ADR through [amose](../../../commands/amose.md); a present-day overview can link that history without rewriting it. Distinguish a released capability from an unreleased candidate, even when the candidate's documentation is correct.

Do not turn a documentation sync into a release announcement, version bump or rewrite of prior changelog entries. Updating current docs does not publish them.

## Consolidation and removal

Accuracy maintenance does not imply a worth audit. Requested pruning may remove still-accurate material, but only when its authority and surviving coverage are established; routine sync does not authorize destructive cleanup.

Before consolidating or removing content, establish what each passage uniquely teaches, who consumes it and which incoming links rely on it. Shared keywords, code paths or a common feature do not prove duplication. Preserve separate records for materially different problems or audiences. When consolidation is authorized, retain unique reasoning and repair affected links in the same change.

A missing implementation file does not establish that the underlying problem disappeared. Age is a reason to inspect, not a deletion rule. Missing repository corroboration does not invalidate operational knowledge. Preserve plausible but unverified claims with their limits rather than deleting them to obtain a clean report.

For an authorized removal, identify the specific surviving coverage or evidence that the obligation no longer applies. Use version history rather than inventing an archive store; do not delete without the necessary authority. Do not replace a canonical domain or architecture record with a generic documentation summary.

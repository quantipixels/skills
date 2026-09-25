# Agent-facing writing

Own agent-facing behavior and instructions. Read the [shared writing contract](../references/oro/writing-contract.md); the method below owns this audience. Return to the calling workflow after the requested text or review result.

Write for an agent reader. Optimize reliable selection, judgment, execution, and completion with the least justified context—not explanation for its own sake.

This is a writing reference, not an automatic authoring pipeline or a preservation rule. Use the authority already granted by the task and governing surface; do not invent approval gates.

## Match instruction weight to consequence

Be light by default. Local wording, structure, pointers, and clearly redundant guidance should not acquire ceremony merely because they are instructions.

Become more explicit only when consequence or uncertainty earns it: a public identity/routing change, authority expansion, compatibility break, destructive effect, or materially different behaviour whose correct choice is unresolved. If the requested scope already covers that change and the evidence supports it, make the change. If it exceeds scope or evidence cannot resolve it, surface the decision instead of guessing.

## Build the behavioural contract

Make the agent able to answer:

- **Trigger** — when does this apply, and what nearby cases do not?
- **Result** — what semantic result is owned?
- **Branches** — which genuinely different cases require different behaviour?
- **Authority** — which reads, edits, publication, merge, install, delete, or other side effects are allowed?
- **Bound** — what observable condition means the work is done, and how demanding must it be?
- **Pointers** — what deeper material is conditional, and what exact condition should load it?

Distinguish required results and authority boundaries from conditional requirements, adaptable defaults, and illustrative examples. State the condition for a requirement and the reason a consequential constraint still applies; inherited wording alone is not its justification. Where method substitution is permitted, preserve the applicable meaning, authority, compatibility, fallback and proof contract, then refresh evidence affected by the substitution. Routine choices within granted authority need no new approval.

When another stable public skill owns a capability, name its exact identifier. Add only the mode, variant, condition, or constraint that changes how it should be applied. Use generic owner language only when the correct skill is intentionally dynamic.

Do not copy another skill's method merely to compose with it. Put cross-stage progression in the workflow/assignment layer and leave the method with its owning skill.

## Spend words on leverage

Assume a capable model already knows routine mechanics. Keep text that changes a recurring non-obvious decision, supplies useful expertise, protects an authority/safety/evidence/routing boundary, sharpens a bound, or makes conditional depth reliably reachable.

Use established engineering principles as semantic compression: DRY for duplicated knowledge, YAGNI for speculative capability, separation of concerns for ownership, or design by contract for preconditions and guarantees. Name the applicable principle instead of re-teaching it; retain the task-specific exception, authority and proof boundary. Prefer a precise term over a blanket “follow SOLID” or an acronym list. Expand unfamiliar abbreviations on first use; human-facing text must remain understandable without the catalogue.

Prefer the positive target behaviour over negation. Keep an explicit prohibition when it protects a hard boundary or evidence shows the positive form alone is insufficient.

For pointer design, information hierarchy, leading words, bounds, context load, or material pruning, read [instruction economics](../references/oro/instruction-economics.md).

## Structure attention

Keep the **hot path**—what every invocation genuinely needs—in the entrypoint. Keep cohesive supporting expertise local when it is commonly consulted. Move branch-specific depth behind a pointer whose wording reliably identifies that branch.

Do not optimize file length in isolation. A tiny root that always opens several references may cost more and focus worse than one cohesive file.

## Skills are one packaging branch

For skill creation or changes to identity, invocation, packaging, or ownership, read [skill mechanics](../references/oro/skill-mechanics.md). First consider whether the behaviour belongs in an existing skill or instruction surface.

When adding, removing, or changing the responsibility of references, scripts, templates, bundled data, or host adapters, read [resource boundaries](../references/oro/resource-boundaries.md).

## Evolve existing agent text

For material behavioural revision, refactoring, or pruning, read [editing agent text](../references/oro/editing-agent-text.md). Handle local wording and pointer corrections directly.

For material changes, trace the governed path from entrypoint and command through applicable references, contracts, templates or tools to its workflow consumer and handoff. Identify affected branches and classify their semantics as **retain**, **strengthen**, **relocate**, **replace**, or **retire**. The old text is evidence, not authority. Delete no-ops, caches, duplication, sediment, and superseded behaviour when they no longer earn their load.

A loss audit exists to distinguish intentional evolution from accidental regression, not to preserve everything that existed before.

## Verify proportionally

Check the boundary that actually changed. Use realistic before/after tasks when wording could materially change selection, authority, completion, routing, or execution. Do not build ceremony or a prompt harness for an editorial change whose behavioural boundary is unchanged.

Match completion to the requested result and accepting evidence. Distinguish structural validity, execution, installation, discovery and user-visible success; missing proof needed for a required outcome leaves that outcome incomplete, even when disclosed. Carry the candidate identity, decisive evidence, material limits and unresolved obligations into the handoff without imposing a report schema.

Use supplied behavioral evidence to revise instructions. When retention depends on a controlled comparison, return the exact candidate and unresolved claim to the requesting project or workflow. Editorial checks establish instruction quality, not runtime improvement.

Syntax, shorter text, passing package checks, or one plausible model output does not prove an instruction is better.

Return the authored/revised text or review findings first, followed only by material behaviour, authority, evidence, or scope questions that remain unresolved.

---
name: oro-fun-sigidi
description: Write, review, or evolve text that agents consume to guide behaviour. Use for skills, AGENTS.md/CLAUDE.md, prompts, subagent definitions, workflow contracts, tool descriptions, routing text, or other instructions/docs agents act from. Exclude human-facing prose whose primary job is comprehension rather than agent behaviour.
metadata:
  maturity: experimental
---

# Ọ̀rọ̀ fún Ṣìgìdì

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

When another stable public skill owns a capability, name its exact identifier. Add only the mode, variant, condition, or constraint that changes how it should be applied. Use generic owner language only when the correct skill is intentionally dynamic.

Do not copy another skill's method merely to compose with it. Put cross-stage progression in the workflow/assignment layer and leave the method with its owning skill.

## Spend words on leverage

Assume a capable model already knows routine mechanics. Keep text that changes a recurring non-obvious decision, supplies useful expertise, protects an authority/safety/evidence/routing boundary, sharpens a bound, or makes conditional depth reliably reachable.

Prefer compact established concepts with strong model priors when one term can carry a recurring idea. Reuse terms such as `pointer`, `branch`, `no-op`, `cache`, or `sediment` once defined rather than repeatedly spelling out their meaning. Introduce an abbreviation only when it is already familiar or recurs enough to repay its decoding cost.

Prefer the positive target behaviour over negation. Keep an explicit prohibition when it protects a hard boundary or evidence shows the positive form alone is insufficient.

For pointer design, information hierarchy, leading words, bounds, context load, or material pruning, read [instruction economics](references/instruction-economics.md).

## Structure attention

Keep the **hot path**—what every invocation genuinely needs—in the entrypoint. Keep cohesive supporting expertise local when it is commonly consulted. Move branch-specific depth behind a pointer whose wording reliably identifies that branch.

Do not optimize file length in isolation. A tiny root that always opens several references may cost more and focus worse than one cohesive file.

## Skills are one packaging branch

When the artifact is a skill, read [skill mechanics](references/skill-mechanics.md). Skill creation is not the default answer to an instruction problem; first ask whether the behaviour belongs in an existing skill, repository instructions, runtime policy, workflow, or another already-loaded surface.

For references, scripts, templates, bundled data, or host adapters, read [resource boundaries](references/resource-boundaries.md).

## Evolve existing agent text

For an existing draft, refactor, or pruning request, read [editing agent text](references/editing-agent-text.md).

Pin the current behaviour graph so change is deliberate, then classify material semantics as **retain**, **strengthen**, **relocate**, **replace**, or **retire**. The old text is evidence, not authority. Delete no-ops, caches, duplication, sediment, and superseded behaviour when they no longer earn their load.

A loss audit exists to distinguish intentional evolution from accidental regression, not to preserve everything that existed before.

## Verify proportionally

Check the boundary that actually changed. Use realistic before/after tasks when wording could materially change selection, authority, completion, routing, or execution. Do not build ceremony or a prompt harness for an editorial change whose behavioural boundary is unchanged.

Syntax, shorter text, passing package checks, or one plausible model output does not prove an instruction is better.

Return the authored/revised text or review findings first, followed only by material behaviour, authority, evidence, or scope questions that remain unresolved.

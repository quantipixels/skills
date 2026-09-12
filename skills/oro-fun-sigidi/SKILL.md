---
name: oro-fun-sigidi
description: Write, review, or refine text that an agent consumes to guide behaviour. Use for skills, AGENTS.md/CLAUDE.md, prompts, subagent definitions, workflow contracts, tool descriptions, routing text, or other instructions/docs agents act from. Exclude human-facing prose whose primary job is comprehension rather than agent behaviour.
metadata:
  maturity: experimental
---

# Ọ̀rọ̀ fún Ṣìgìdì

Write for an agent reader. Optimize selection, decisions, authority, execution, and completion—not explanation for its own sake.

This is a writing reference, not an automatic authoring pipeline. Invocation does not itself justify a new artifact, a new public skill identity, a routing change, or broader authority.

## Preserve human authority

The human owns consequential intent and public taxonomy. An agent may inspect, critique, prune, draft, or edit agent-facing text within the requested scope, but it must not silently:

- create a new public skill identity unless the user explicitly requested a new skill or accepted that identity;
- materially redefine which skill/agent owns a result or when routing changes owners without that scope being authorized;
- promote, retire, fold, or remove a public skill merely because a rewrite suggests it; or
- treat a generated draft, structural metric, or model preference as acceptance evidence.

When such a decision is unresolved, surface the decision and the smallest useful candidate or options. Do not hide it inside prose.

## Spend instructions only where they steer

Assume a capable model already knows routine mechanics. Keep text that changes a recurring non-obvious decision, provides needed expertise, protects authority/safety/evidence/routing boundaries, states a completion condition, or reliably points to selectively loaded depth.

Delete filler, generic diligence, duplicated procedure, cached repository facts, and rationale that does not change judgment. Shorter is not automatically better: preserve workflow topology, exceptions, recovery, authority, compatibility, and other semantics whose removal would force consequential guessing.

Use progressive disclosure. Keep universal steering in the entrypoint; move branch-specific expertise behind a reliable pointer. A weak pointer makes good hidden guidance unreachable.

For material pruning or pointer/loading changes, read [instruction economics](references/instruction-economics.md).

## Write the behavioural contract

Make the agent able to answer:

- **When does this apply?** Use discriminative triggers and nearest exclusions, not synonym piles.
- **What result is owned?** Name the semantic result, not a vague activity.
- **What decisions are non-obvious?** Encode the distinctions the model would otherwise guess poorly.
- **What authority exists?** Separate read, edit, publish, approve, merge, install, delete, and other consequential actions when they differ.
- **What evidence is enough?** State decisive proof or completion semantics where premature stopping would matter.
- **What is conditional?** Point to deeper material only from a condition that reliably selects it.

Do not copy another skill's method merely to compose with it. Put cross-stage progression in the workflow/assignment layer and keep the owning method at its owner.

For an existing agent-facing draft or a pruning request, read [editing agent text](references/editing-agent-text.md).

## Skills are one packaging branch

When the artifact is a skill, read [skill mechanics](references/skill-mechanics.md). Skill creation is not the default interpretation of an instruction problem; first ask whether the behavior belongs in an existing owner, repository instructions, runtime policy, a workflow, or another already-loaded surface.

For references, scripts, templates, bundled data, or other supporting material, read [resource boundaries](references/resource-boundaries.md).

## Review the changed behaviour

Compare the candidate with the behaviour the human actually authorized. Check the real loading path: description/pointer, entrypoint, selectively loaded references, handoffs, and host adapters that materially affect the instruction.

For meaningful compression, routing, authority, or composition changes, perform a loss audit: what could the previous text select, protect, distinguish, accept, or recover that the candidate no longer can? Classify the loss as intentionally retired, relocated, compatibility-only, or accidental.

Use realistic before/after tasks when the wording change could materially alter behaviour. Syntax, shorter text, passing package checks, or a model producing one plausible answer does not prove the instruction is better.

Return the authored/revised text or review findings first, followed only by material behaviour, authority, or evidence questions that still require human judgment.

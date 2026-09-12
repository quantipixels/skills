---
name: ko-skill
description: Create, improve, or validate an agent skill that reliably produces its intended result. Use for skill instructions, supporting resources, and behavior checks; also supports explicitly scoped portfolio audits. Keep routine edits local to the changed behavior.
---

# Kọ Skill

Create, improve, or validate a skill so it reliably produces one useful result without unnecessary instruction load. Authoring requires edit permission; validation and audits remain read-only. Installation, activation, publication, and provider mutations require their own authority.

Delegate substantial analysis, research, and expert work to subagents when it materially helps.

## Understand the result

Start from the user's request, current candidate, and applicable repository/host rules. Establish the intended result, realistic trigger, nearest exclusions, completion evidence, and requested change.

If the user's desired result, boundaries, or consequential design choices remain materially ambiguous after using the available context, use `arojinle` to resolve them before authoring. Do not invoke it to reopen requirements the user has already settled.

Before adding instructions, distinguish missing expertise or unclear guidance from unavailable/ignored instructions, missing tools, or an environment failure. No change is a valid result.

A new skill needs an independently useful result or steering contract, a reason an existing skill cannot absorb it coherently, and a realistic positive/adjacent-negative selection case. Keep an unproved new identity Experimental rather than manufacturing confidence.

For an explicitly scoped portfolio audit, read [portfolio audit](references/portfolio-audit.md). Keep the audit read-only unless edits are separately authorized.

## Shape the smallest useful skill

Keep the entrypoint focused on what every invocation needs: the owned result, recurring non-obvious decisions, completion evidence, necessary authority/safety boundaries, and reliable conditions for selectively loaded depth.

Leave routine mechanics to the model and native tools. Keep current project/environment facts in their authoritative sources instead of copying them into skill instructions. Use references for conditional expertise and scripts/tools only for bounded deterministic mechanics that earn their maintenance cost.

When simplifying, merging, relocating, or materially pruning guidance, read [instruction economics](references/instruction-economics.md). Preserve useful behavior and reliable loading paths; shorter text is not evidence of equivalent behavior.

For a skill that produces files, name its natural destination in the skill itself. Do not copy repository runtime/worktree policy merely to explain that destination.

Use `oro-ologbon` when prose itself needs cleanup.

Load deeper guidance only when the change needs it:

- description/entrypoint/reference load, selection, context pressure, pruning, or frontier-model capability claims → [instruction economics](references/instruction-economics.md);
- resource responsibility or placement → [resource placement](references/resource-placement.md);
- expert reference content → [reference quality](references/reference-quality.md);
- executable capability → [script boundary](references/script-boundary.md);
- researched knowledge collections → [knowledge catalogues](references/knowledge-catalogues.md);
- Experimental maturity/disposition → [experimental disposition](references/experimental-disposition.md);
- portfolio-wide review → [portfolio audit](references/portfolio-audit.md).

An unchanged resource does not trigger a fresh architectural review.

## Verify what changed

Run applicable package checks and test changed behavior where correctness remains uncertain. Use fresh host sessions for changed behavioral claims.

For material selection, compression, composition, or authority changes, compare realistic before/after tasks. When the claim depends on frontier-model native capability, include the ordinary host/model without the skill as a baseline; an adequate baseline is a valid finding. Keep evaluator expectations out of the tested agent's instructions.

Check the actual loading/execution path, including references and handoffs. For material pruning, verify preserved safety, authority, routing, compatibility, and evidence contracts whose wording or location changed. Reuse existing evidence and retest only what later changes invalidate.

Use `ayewo-igba-ise` when a bounded prior run or corpus needs retrospective evidence before changing the skill.

Use `VERIFIED` only when required proof passes, `CHANGES_REQUIRED` for a demonstrated defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Structural brevity, word count, or a skill name appearing in output does not prove behavior.

## Deliver

Reconcile affected metadata, links, routing, tests, and release surfaces without changing unrelated work. Keep one semantic contract across hosts and thin host-specific adapters.

Return the change or justified no-change result, verification, and remaining limitations. Keep rationale and proof in the PR/discussion and CI unless a separate durable document independently earns its place.

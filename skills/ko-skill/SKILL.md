---
name: ko-skill
description: Create, improve, or validate an agent skill that reliably produces its intended result. Use for skill instructions, supporting resources, and behavior checks; also supports explicitly scoped portfolio audits. Keep routine edits local to the changed behavior.
---

# Kọ Skill

Deliver a useful skill with clear scope, appropriate depth, and enough verification to trust the change. Authoring requires permission to edit; validation and audits remain read-only. Installation, activation, publication, and provider mutations need their own authority.

Delegate substantial analysis, research, and expert work to subagents, returning concise findings and evidence links to keep the main context lean.

## Define the job

Establish the intended result, trigger, boundaries, and requested change from the candidate and applicable host/repository rules. Before prescribing more instructions, distinguish missing expertise or unclear guidance from ignored/unavailable instructions, insufficient tools, or an environment failure. No change is a valid result.

For a new skill or a material identity change, require an independently useful outcome or steering contract, a reason an existing skill cannot absorb it coherently, and a realistic positive/adjacent-negative selection case. A separate name must make selection/use easier. Do not split by subject taxonomy, target a skill count, or remove a useful lightweight skill merely because the model knows the underlying task.

If a new identity is credible but its independent value remains unproved, keep the candidate Experimental rather than presenting it as stable. Use real-use evidence before promotion. Routine corrections do not reopen identity, architecture, or maturity.

## Shape the skill

Establish the focal point: the one result or steering effect the skill owns and the recurring non-obvious decisions it improves. Keep instructions, references, tools, state, and reports only when they strengthen that result or protect a necessary boundary. Move adjacent-owner work out; leave routine mechanics to the model and native tools.

Compare competing identities at the same layer by outcome, decision surface, and completion evidence, not shared words. Merge or internalize a redundant identity only after preserving independently useful results and independently loaded safety boundaries. A conversational agent, a coordination skill, and a worker are different roles, not three copies of one skill.

State the scope, completion evidence, and consequential exceptions. Supply useful expertise and examples, not just behavioral restrictions.

Use `oro-ologbon` for prose editing or requested pruning as needed.

Keep a simple entry point with selectively loaded depth. Use related skills by name, where they fit the work; keep supporting skills independent of their callers. Do not repeat their instructions or explain how to combine them.

Keep each rule in one authoritative place per loading path unless repetition protects an independent boundary. Preserve deliberate overrides, useful named concepts, and constraints that would otherwise become consequential guesswork. Compare credible alternatives when they could change the choice; a score or disposition vocabulary is not required.

Read supporting guidance only when the change needs it:

- Adding a resource, changing its responsibility, or investigating a placement problem: [resource placement](references/resource-placement.md).
- Adding, changing, or removing expert reference content: [reference quality](references/reference-quality.md).
- Adding/changing executable capability: [script boundary](references/script-boundary.md).
- Maintaining a researched body of knowledge: [knowledge catalogues](references/knowledge-catalogues.md).
- Deciding Experimental maturity or disposition: [experimental disposition](references/experimental-disposition.md).
- An explicitly scoped portfolio audit: [portfolio audit](references/portfolio-audit.md).

An unchanged resource does not trigger a fresh architectural review.

## Check behavior

Run applicable package checks and test the changed behavior where its correctness remains uncertain. Use fresh host sessions for changed behavioral claims. For material compression, composition, authority, or selection changes, compare the same realistic task, evidence, permissions, and host configuration before/after. Include the ordinary host as a baseline when the claim is incremental skill value; an adequate baseline is a valid finding. Keep evaluator expectations out of the tested agent's instructions so the harness does not supply the missing behavior.

Check selection, outcome, and preserved boundaries on the actual loading/execution path, including references and handoffs. Record the exact candidate, host/version, observed model/settings, actions, and evidence limits. Word count or a skill name in an answer does not prove quality, cost, selection, or execution. Validation of a supplied change does not require searching for a better variant.

Use `ayewo-igba-ise` as needed. Reuse existing evidence rather than reconstructing the same corpus.

Retest only what later changes or unresolved findings invalidate. Keep temporary simulations temporary; retain regression cases only for justified recurring risk. Use `VERIFIED` only when required proof passes, `CHANGES_REQUIRED` for a demonstrated defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Source checks do not prove installation or behavior on untested hosts/models.

## Deliver

Reconcile affected metadata, links, routing, tests, and release surfaces without changing unrelated work. Keep one semantic contract across hosts and thin host-specific adapters. Reference other skills by exact frontmatter name.

Return the change or no-change conclusion, meaningful verification, and remaining limitations. Include installation/publication state only when relevant. Reporting is not an instruction to create a file: use the PR/discussion and CI for change evidence, and apply the repository's documentation-admission policy before committing a separate document.

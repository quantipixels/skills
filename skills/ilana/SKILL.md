---
name: ilana
description: Writes, fixes or tightens agent-facing text - skills, SKILL.md files, references, prompts, subagent briefs and agent instructions - and holds the standard they are checked against. Use for "write or fix a skill", "write a prompt", "tighten these instructions", or to check agent-facing text against the standard.
---

# Ìlànà

Output: agent-facing text that steers an agent so it picks the right job, judges well, acts within its authority and knows when it is done, with the least context that achieves it. Findings first when checking text against the standard. Writing alone grants no authority to install, run or publish.

Needs: the skill, prompt or instructions to change (or the job it must do), plus who or what runs it. If either is missing, or the text is prose a person reads, return and say what is missing.

## Method

Read [agent-facing writing](references/agent-writing.md) first. It points to the rest: [instruction economics](references/instruction-economics.md) for pointers, order, bounds and pruning; [skill mechanics](references/skill-mechanics.md) for name, trigger, packaging and ownership; [resource boundaries](references/resource-boundaries.md) for choosing prose, examples, templates, assets or scripts; [editing agent text](references/editing-agent-text.md) for material revisions.

- Preserve facts, decisions, authority, exact identifiers and the artifact's native contract. A useful or user-requested format is part of the contract; changing it is a behaviour change, so say so.
- Give goals, conditions and limits, not step lists. Name the safe failure direction and the facts the agent cannot derive. A block that keeps absorbing "add the case we just found" is the wrong shape; restate the goal.
- A skill has one output and states Output, Needs, Method, Done and Return. Its description says what it produces and when, and names no other skill. It never names a next step or a skill to route to.
- Keep SKILL.md under 8000 bytes (Codex's limit); move detail into `references/` and say when to read each file. Link only inside the skill's own directory; copy a file into each skill that needs it.
- Plain words, the project's own terms, no hard-wrapped markdown, each rule said once.
- Keep resources with the skill that uses them; prefer existing project or native capabilities.
- A mixed artifact (a skill with a section a person reads) uses this skill for the behaviour-shaping parts; name the split in your reply.
- Skill changes that come out of a reflection need the user's approval first.

## Done

The package validator passes. For a behaviour change, a fresh agent given the edited skill from disk (a running session keeps the old copy) shows the real result end to end.

## Return

The complete usable text first when writing or editing, findings first when checking, and only material gaps in meaning, authority, audience or scope.

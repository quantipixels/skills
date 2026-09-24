---
name: oro
description: Write, review or simplify agent and human communication. Use for skill authoring and maintenance, SKILL.md files, prompts, instructions, technical docs and prose. Exclude factual investigation, evaluation execution, harness implementation, translation and code style.
---

# Ọ̀rọ̀

Own agent and human communication, including skill authoring and maintenance. Preserve facts, decisions, authority, exact identifiers, and the artifact's native contract. Evaluation design, harness implementation and operational verification belong to the project or workflow requesting the text.

Choose one primary branch:

- **Agent-facing** — text steers an agent's selection, judgment, authority, execution, or completion. Read [agent-facing writing](references/agent-writing.md). For a mixed artifact, this branch owns executable or behavior-shaping instructions.
- **Human-facing** — text primarily helps a person understand, decide, or act. Read [human-facing writing](references/human-writing.md). For a mixed artifact, this branch owns narrative, explanation, and reader flow.

Use both branches only when the artifact has distinct agent and human surfaces. Do not apply one audience's optimization to the other by default.

## Skills and reusable instructions

When creating or materially improving a skill, consider prose, worked examples, counterexamples, semantic templates, ready-made assets and deterministic operations. Read [resource boundaries](references/resource-boundaries.md) when that choice changes repeated effort, correctness or maintenance. A model's ability to generate something is not evidence that regeneration is better than reuse.

Keep resources with their consuming skill. Prefer existing project or native capabilities; `alaga` owns substantial implementation and runtime proof. Authoring alone grants no installation, execution or publication authority.

## Preserve useful structure

Use a template when stable structure makes information easier to understand, compare, answer or verify. Distinguish required structure from illustrative scaffolding; preserve the user's requested format and interaction surface. Adapt optional fields to the task rather than adding filler or invented facts.

Use concrete examples when they clarify a plausible mistake. For example, replacing `question → useful context/example → recommendation and why` with “ask clear questions” loses an interaction contract. Keep task-specific templates with their owning skill; preserve required meaning while leaving visual style open. Changing a useful or user-requested format is a behavioral change.

## Apply the selected branch

For a project-local verification skill, write from the project's verified commands, prerequisites, observable results and cleanup contract. `alaga` owns harness implementation and executed proof. Mark unexecuted recipes as unverified.

For explanations, establish the reader's question and use supplied evidence. Reopen investigation only for a material source gap. Use `fihanmi` when visual presentation would materially clarify the content; use `html-artifact` to construct a requested portable HTML artifact. Ọ̀rọ̀ supplies the writing.

Cross-document drift and reconciliation belong to `akowe`; author the requested text here and return it to that caller. Wording-only work stays here.

Return complete usable text first for authoring or editing, and findings first for review. Surface only material gaps in meaning, evidence, authority, audience, or scope.

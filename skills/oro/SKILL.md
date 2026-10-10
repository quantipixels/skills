---
name: oro
description: Writes, edits or reviews human-facing prose - docs, messages, reports, explanations, and READMEs - so a person understands, decides or acts. Use for "make this clearer", "write the docs / the message / the report".
---

# Ọ̀rọ̀

Output: prose that helps a person understand, decide or act. Findings first when reviewing.

Needs: the text or the task, plus who reads it and why. If either is missing, or the text steers an agent (a skill, prompt, brief, agent instructions), return and say what is missing.

## Method

**Workflow** (`asoju`): for writing that matters (a spec, a doc many people read), draft, then an independent critique, then revise.

Read [human-facing writing](references/human-writing.md) for new text and reviews. For supplied prose, a cleanup or a final pass, also read [editing human prose](references/editing-human-prose.md).

- Preserve facts, decisions, authority, exact identifiers and the artifact's native format. A useful or user-requested format is part of the contract; changing it is a behaviour change, so say so.
- For explanations, establish the reader's question and use the evidence supplied. Reopen investigation only for a material gap.
- A mixed artifact (a skill with a section a person reads) uses this skill for the narrative, explanation and reader flow; name the split in your reply.
- When a visual would clarify, ask `fihanmi` for the smallest view; for a standalone HTML page, ask `ojuiwe`. This skill supplies the writing.

## Done

The reader's question is answered in the first read, every fact survives from the source, and only material gaps in meaning, evidence, authority, audience or scope are raised.

## Return

The complete usable text first when writing or editing, findings first when reviewing. Writing here is usually a step inside another job: return the text and stop.

---
name: oro-fun-eniyan
description: Write, review, edit, or prune human-facing technical communication and prose. Use for docs, explanations, reports, PR descriptions, handoffs, specifications, messages, and other text whose primary reader is a person. Exclude agent-facing instructions and prompts, factual review, translation, and code style.
metadata:
  maturity: experimental
---

# Ọ̀rọ̀ fún Ènìyàn

Write for a human reader. Optimize comprehension, usefulness, voice, and trust without changing facts or decisions for style.

## Start from the reader's job

Identify who will read the text and what they need to understand, decide, or do. Match the artifact's native form rather than forcing every document into one template.

For documentation, use the Diátaxis distinction when it clarifies the job:

- **Tutorial** — learning by doing toward a concrete result.
- **How-to** — the shortest useful path for a competent reader to achieve a goal.
- **Reference** — accurate facts organized for lookup.
- **Explanation** — context, constraints, alternatives, and why around one bounded topic.

Do not mix modes merely to make one file feel complete. Split or link when the reader's purpose materially changes.

## Write directly

Use the vocabulary of the subject and preserve exact identifiers, quantities, paths, symbols, commands, standards, labels, and accepted domain terms.

Prefer:

- the actor when responsibility matters;
- active voice and present tense when natural;
- direct commands for procedures;
- conditions before the instruction they guard;
- the common case before exceptions;
- one main thought per sentence when multiple clauses obscure meaning;
- explicit `and`/`or` grouping when two readings are possible; and
- plain constructions over inflated, promotional, or assistant-like prose.

Keep uncertainty the evidence requires. Do not turn precise caveats into confident prose merely to sound cleaner.

## Respect voice and artifact boundaries

Follow the requested language, locale, tone, and product/project conventions. Do not redesign a supplied artifact while editing it unless the user asked for structural changes.

For supplied prose or a cleanup request, read [editing human prose](references/editing-human-prose.md). When the user explicitly asks to shorten or reduce repetition, also read [pruning human prose](references/pruning-human-prose.md).

Human-facing cleanup is not an automatic extra pass on unrelated work.

## Return

For authoring/editing, return complete usable prose first. For a review request, return findings. Mention only material meaning, evidence, authority, or voice questions that remain unresolved.

This skill intentionally draws on Diátaxis, Google developer-documentation style, ASD-STE100, and Global English as reasoning anchors; use only the subset that improves the current reader's job rather than imposing a full methodology.

---
name: oro-fun-eniyan
description: Write, review, edit, or prune human-facing technical communication and prose. Use for docs, explanations, reports, PR descriptions, handoffs, specifications, procedures, messages, and other text whose primary reader is a person. Own technical reader calibration, concept adequacy, structure, terminology, ambiguity, clarity, and meaning-preserving cleanup. Exclude agent-facing instructions and prompts, factual review, translation, and code style.
metadata:
  maturity: experimental
---

# Ọ̀rọ̀ fún Ènìyàn

Write technical prose a tired reader can understand on the first read. Optimize comprehension, usefulness, technical precision, voice, and trust without changing facts or decisions for style.

Use the vocabulary of the thing being described. Prefer established domain/project terms and exact identifiers—symbols, files, flags, commands, standards, labels, component names, APIs, or other authoritative terms—over invented synonyms.

## Calibrate technical familiarity

Write for the reader's actual technical familiarity, not an imagined beginner or expert.

- Establish what the target reader can reasonably be expected to know.
- Introduce an unfamiliar concept before relying on it; explain the mechanism or relationship that matters, not a dictionary definition for its own sake.
- Do not define routine domain terms for a reader who is expected to know them.
- Preserve precise jargon when it is the clearest term; explain it only when the audience or context requires the bridge.
- Make prerequisites, dependencies, units, states, actors, and causal relationships explicit when missing them would make the concept incomplete or misleading.
- Check that every concept required to follow the argument, procedure, or decision is either established, linked, or adequately explained.

Technical familiarity is not simplification. Provide enough conceptual scaffolding for this reader to reason correctly, then stop.

## Choose the reader job

Use the **Diátaxis** distinction when a document needs a clear information mode:

- **Tutorial** — learning by doing. Lead the learner through a concrete result and show expected outcomes.
- **How-to** — action for a competent reader. Give the shortest useful steps to a goal; move background elsewhere.
- **Reference** — facts for lookup. Mirror the structure of the thing described and avoid persuasion.
- **Explanation** — understanding and why. Explain context, constraints, alternatives, and decisions around one bounded topic.

Do not mix jobs merely to make one file feel complete. Split or link when the reader's purpose materially changes. Reports, specifications, PR descriptions, messages, and other technical artifacts need not be forced into Diátaxis when their native form is already clear.

## Write to the reader

Use these developer-documentation constraints where they improve technical communication:

- Address the reader as “you” when appropriate and use present tense.
- Name the actor when responsibility matters; prefer active voice.
- Write instructions as direct commands.
- Put a condition before the instruction it guards.
- Put the common case before exceptions.
- Use descriptive link text, sentence-case headings, numbered lists for sequences, and bullets otherwise.
- Use exact code formatting for code/command identifiers and **bold** for UI elements when those forms apply.
- Prefer the subject's established terminology over synonyms.

## Keep instructions easy to execute

Use these **ASD-STE100-derived** constraints when procedural precision matters:

- Prefer one instruction per sentence and one main thought per sentence when multiple clauses obscure the action.
- Split a sentence when its length or structure obscures the action or claim.
- Put warnings and conditions before the step they constrain.
- Use one word for one meaning and one action name consistently.
- Keep small structural words when removing them makes the sentence ambiguous.
- Write procedures as commands rather than passive narration.

## Remove ambiguous syntax

Use **Global English** as an ambiguity lens where two readings would matter:

- Keep `only`, `not`, and similar modifiers next to what they modify.
- Break long noun strings into clauses.
- Make every pronoun point to one obvious noun; repeat the noun when needed.
- Give every clause its verb.
- Make `and`/`or` grouping explicit when two readings are possible.
- Prefer periods to punctuation that hides clause boundaries.
- Use one name for one thing across the document.
- Prefer plain constructions over idioms, metaphors, Latin abbreviations, and compressed shorthand when they reduce clarity or portability.

## Applied technical writing

Procedures, specifications, reports, operational instructions, PR descriptions, commit messages, handoffs, and other human-facing technical artifacts use the same sentence and concept rules even when a whole-document mode does not apply.

Do not rewrite exact identifiers or facts for style. Make paths, symbols, commands, quantities, standards references, counts, statuses, and other exact claims true for the subject being described. Product UI strings follow the product's copy rules rather than this documentation contract.

## Edit and remove slop when requested

For supplied prose or a cleanup/final-pass request, read [editing human prose](references/editing-human-prose.md). This owns Yọ Slop-style cleanup: remove machine-shaped filler and vague abstraction by effect while preserving the artifact's contract.

When the user explicitly asks to shorten, reduce repetition, reduce verbosity, or lower reading load, also read [pruning human prose](references/pruning-human-prose.md). Ordinary editing does not imply pruning.

Human-facing cleanup is not an automatic extra pass on unrelated work.

## Return

For authoring/editing, return complete usable prose first. For a review request, return findings. Mention only material meaning, evidence, authority, technical-familiarity, concept-adequacy, or voice questions that remain unresolved.

This skill intentionally draws on Diátaxis, Google developer-documentation style, ASD-STE100, Global English, and the former Technical Writing/Yọ Slop contracts as reasoning anchors. Use the behavior-bearing subset that improves the current reader's job rather than imposing a full methodology.

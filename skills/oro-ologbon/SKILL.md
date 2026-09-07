---
name: oro-ologbon
description: Write or review technical communication, or edit and prune supplied human- or agent-facing prose. Use for document structure, clarity, voice, ambiguity, filler, repetition, and instruction load. Editing preserves facts, authority, structure, and intended voice; exclude factual review, translation, and code style.
---

# Ọ̀rọ̀ Ọlọ́gbọ́n

Write prose a tired reader can understand on the first read. Own technical document structure and sentence clarity, plus meaning-preserving cleanup of supplied prose. Produce complete usable prose without a second cleanup skill.

## Choose the operation

- **Author or review technical communication:** establish the reader/document job and use the writing guidance below.
- **Edit supplied prose:** read [editing prose](references/editing-prose.md) for clarity, voice, filler, and agent-instruction preservation. This mode also accepts nontechnical prose; do not force a technical-document structure onto it.
- **Prune:** when explicitly asked to shorten, remove repetition, or reduce instruction load, use the editing guidance and [prune prose](references/prune.md). Ordinary editing does not imply pruning.

Follow the requested language, locale, voice, and product copy rules. For editing/pruning, preserve the supplied structure and artifact decisions; an authoring guideline does not authorize redesigning them. Cleanup is not an automatic extra pass on unrelated tasks.

Use the vocabulary of the thing being described. Prefer its established domain/project terms and exact identifiers—symbols, files, flags, commands, standards, labels, component names, or other authoritative terms—over invented synonyms.

## Choose the reader job

Use the **Diátaxis** distinction when a document needs a clear information mode:

- **Tutorial** — learning by doing. Lead the learner through a concrete result and show expected outcomes.
- **How-to** — action for a competent reader. Give the shortest useful steps to a goal; move background elsewhere.
- **Reference** — facts for lookup. Mirror the structure of the thing described and avoid persuasion.
- **Explanation** — understanding and why. Explain context, constraints, alternatives, and decisions around one bounded topic.

Do not mix jobs merely to make one file complete. Split/link when the reader's purpose materially changes. Repository-facing messages, reports, specifications, and other technical artifacts need not be forced into Diátaxis when their native form is already clear.

## Write to the reader

Use these **Google developer-style** constraints where they improve technical communication:

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

- Prefer one instruction per sentence and one main thought per sentence when multiple clauses make action hard to parse.
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

Procedures, specifications, reports, operational instructions, PR descriptions, commit messages, handoffs, and human-facing technical artifacts use the same sentence rules even when a whole-document mode does not apply.

Do not rewrite exact identifiers or facts for style. Make paths, symbols, commands, quantities, standards references, counts, statuses, and other exact claims true for the subject being described. Product UI strings follow the product's copy rules rather than this documentation contract.

Return authored or revised prose first. For a review request, return findings. Report only material meaning, authority, or evidence questions; pruning also reports material count changes and preservation limits.

## Provenance and boundary

This skill intentionally uses selected reasoning from Diátaxis, the Google developer documentation style guide, ASD-STE100 Issue 9, and Kohl's *The Global English Style Guide*. The named models provide useful vocabulary and reasoning anchors; the rules above are the behavior-bearing subset for this skill. Do not import each source as a complete mandatory methodology or replace its current authoritative text with cached local guidance.

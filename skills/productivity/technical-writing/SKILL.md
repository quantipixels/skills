---
name: technical-writing
description: Write or review clear technical docs, procedures, specifications, reports, RFCs, readmes, PR descriptions, commit messages, technical communication, and human-facing artifact copy. Use when the reader job, instruction structure, sentence clarity, terminology, or unambiguous syntax needs an owning pass.
license: MIT
---

# Technical writing

Write technical prose a tired reader can understand on the first read. Own reader/document job, instruction structure, technical sentence clarity, and unambiguous syntax. Produce complete usable prose from this owner; do not require a second cleanup skill for normal completion.

Use the vocabulary of the thing being described. Prefer its established domain/project terms and exact identifiers—symbols, files, flags, commands, standards, labels, component names, or other authoritative terms—over invented synonyms.

## Choose the reader job

Choose one dominant job when the document needs a clear information shape:

- **Tutorial** — learning by doing. Lead the learner through a concrete result and show expected outcomes.
- **How-to** — action for a competent reader. Give the shortest useful steps to a goal; move background elsewhere.
- **Reference** — facts for lookup. Mirror the structure of the thing described and avoid persuasion.
- **Explanation** — understanding and why. Explain context, constraints, alternatives, and decisions around one bounded topic.

Do not mix jobs merely to make one file complete. Split/link when the reader's purpose materially changes. Repository-facing messages, reports, specifications, and other technical artifacts need not be forced into one of these four modes when their native form is already clear.

## Write to the reader

- Address the reader as “you” when appropriate and use present tense.
- Name the actor when responsibility matters; prefer active voice.
- Write instructions as direct commands.
- Put a condition before the instruction it guards.
- Put the common case before exceptions.
- Use descriptive link text, sentence-case headings, numbered lists for sequences, and bullets otherwise.
- Use exact code formatting for code/command identifiers and **bold** for UI elements when those forms apply.
- Prefer the subject's established terminology over synonyms.

## Keep each statement easy to execute

- Prefer one instruction per sentence and one main thought per sentence when multiple clauses make action hard to parse.
- Split a sentence when its length or structure obscures the action or claim.
- Put warnings and conditions before the step they constrain.
- Use one word for one meaning and one action name consistently.
- Keep small structural words when removing them makes the sentence ambiguous.
- Write procedures as commands rather than passive narration.

## Leave no sentence open to two readings

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

Use `yo-slop` only when the user explicitly asks for its cleanup/pruning outcome or when a distinct material filler/AI-tell/repetition problem remains after the technical writing is already correct. Do not invoke it merely because Technical Writing completed.

## Provenance

These direct rules are curated from durable ideas in Diátaxis, the Google developer documentation style guide, ASD-STE100 Issue 9, and Kohl's *The Global English Style Guide*. The source names document provenance; they are not separate execution frameworks or mandatory methodology stages.

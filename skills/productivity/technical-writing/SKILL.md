---
name: technical-writing
description: "Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, and Global English syntax. Use when writing or reviewing docs, RFCs, readmes, PR descriptions, commit messages, technical communication, or human-facing artifact copy."
license: MIT
---

# Technical writing

Write technical prose a tired engineer can understand on the first read. Own document mode, instruction structure, technical sentence clarity, and unambiguous syntax. Use `yo-slop` after meaning and structure are settled for final prose cleanup; do not duplicate its filler, AI-tell, voice, or pruning catalogue here.

The codebase is the word list. Use the real symbol, file, flag, command, and project term rather than an invented synonym.

## Pick one document mode

Use Diátaxis to choose the document's job:

- **Tutorial** — learning by doing. Lead the learner through a concrete result and show expected outcomes.
- **How-to** — action for a competent reader. Give the shortest useful steps to a goal; move background elsewhere.
- **Reference** — facts for lookup. Mirror the structure of the thing described and avoid persuasion.
- **Explanation** — understanding and why. Explain context, constraints, alternatives, and decisions around one bounded topic.

Do not mix modes merely to make one file complete. Split and link when the reader's job changes.

Source: diataxis.fr, fetched 2026-07-18.

## Write to the reader

Apply the transferable Google developer-style rules:

- Address the reader as “you” when appropriate and use present tense.
- Name the actor when responsibility matters; prefer active voice.
- Write instructions as direct commands.
- Put a condition before the instruction it guards.
- Put the common case before exceptions.
- Use descriptive link text, sentence-case headings, numbered lists for sequences, and bullets otherwise.
- Use exact code formatting for symbols and **bold** for UI elements.
- Prefer the project's established terminology over synonyms.

Source: developers.google.com/style, fetched 2026-07-18.

## Keep each statement easy to execute

Apply the transferable ASD-STE100 principles:

- One instruction per sentence; one main thought per sentence elsewhere.
- Split a sentence when its length or structure makes the action hard to parse.
- Put warnings and conditions before the step they constrain.
- Use one word for one meaning and one action name consistently.
- Keep articles and other small structural words when removing them makes the sentence ambiguous.
- Write procedures as commands rather than passive narration.

Source: asd-ste100.org, Issue 9 (2025), fetched 2026-07-18.

## Leave no sentence open to two readings

Apply Global English where ambiguity matters:

- Keep `only`, `not`, and similar modifiers next to what they modify.
- Break long noun strings into clauses.
- Make every pronoun point to one obvious noun; repeat the noun when needed.
- Give every clause its verb.
- Make `and`/`or` grouping explicit when two readings are possible.
- Prefer periods to punctuation that hides clause boundaries.
- Use one name for one thing across the document.
- Prefer plain constructions over idioms, metaphors, Latin abbreviations, and compressed shorthand.

Source: Kohl, *The Global English Style Guide* (SAS Press), source material fetched 2026-07-18.

## Repository-facing writing

PR descriptions, commit messages, handoffs, and human-facing technical artifacts use the same sentence rules even when Diátaxis does not apply as a whole-document model.

Do not rewrite exact identifiers or facts for style. Make paths, symbols, commands, counts, and generated-tree claims true for the candidate being described. Product UI strings follow the product's copy rules rather than this documentation contract.

After the technical structure and meaning are correct, use `yo-slop` for final cleanup without changing facts, authority, required structure, or technical terminology.

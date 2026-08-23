---
name: yo-slop
description: Refine human- or agent-facing prose by removing AI tells, filler, vague abstraction, and instruction noise without changing facts, authority, structure, or intended voice. Use for final cleanup or explicitly requested pruning of verbosity, repetition, and instruction load in technical writing, skills, agent instructions, handoffs, tickets, and reports. Exclude content design, factual review, translation, and code style.
---

# Yọ Slop

Make supplied prose clearer and less machine-shaped while preserving its contract. Keep exact identifiers, quotations, facts, citations, schemas, required formats, accepted terminology, and the owning artifact's decisions.

## Choose the pass

Use the normal cleanup pass for local clarity and voice problems. When the request explicitly asks to shorten prose, reduce verbosity, remove repetition, or lower instruction load, use `prune` and read [prune prose](references/prune.md). Do not infer `prune` from an ordinary editing or final-pass request.

## Establish the pass

Identify the reader, artifact owner, purpose, language and locale, intended voice, and text that must remain exact. If these are unclear, fix only unambiguous filler and ask before a change that could alter meaning or tone.

Use the owning skill for content structure, evidence, technical truth, accessibility, localization, or acceptance. `technical-writing` owns human-facing developer documentation, technical communication, and applicable artifact copy. `ko-skill` owns skill behavior and proof. Yọ Slop owns cleanup and explicit pruning of settled prose, not structural or factual changes.

## Match the reader

For human-facing prose, sound direct and specific. Vary sentence length naturally. Use a point of view only when the artifact permits one. Keep reference material neutral. Do not add deliberate mess, personality, or opinion to simulate humanity.

For agent-facing prose, optimize execution rather than personality:

- Preserve the existing control flow, triggers, branches, completion criteria, commands, identifiers, statuses, output fields, and authority boundaries.
- Make an existing action, condition, or decision easier to parse only when the wording change is behaviorally equivalent.
- Retain context pointers and the cases they name. Flag a weak or missing branch for the artifact owner instead of changing disclosure behavior.
- Flag apparent generic defaults, stale environment caches, or rationale that may not change judgment instead of removing them.
- Preserve prohibitions and deliberate repetition unless the artifact owner confirms that they are redundant.

Report an agent-facing ambiguity when fixing it would add, remove, reorder, or reinterpret behavior. The artifact owner decides the correction.

## Remove patterns by effect

Do not replace words mechanically. Rewrite only when a pattern causes puffery, ambiguity, unsupported certainty, needless load, or a voice mismatch.

- **Inflation and promotion:** Remove grand significance claims, notability lists, promotional adjectives, generic challenge-and-triumph framing, and conclusions that add no fact or action.
- **Unsupported attribution:** Name the source behind “experts say” or “reports suggest,” qualify the claim from evidence, or remove it.
- **Abstract padding:** Replace vague metaphors, nominalizations, copula avoidance, ornamental `-ing` clauses, weak verbs, and unmeasured adverbs with the concrete actor, mechanism, action, or result. Common signals include non-literal “landscape,” “tapestry,” “substrate,” or “vector,” and padded verbs such as “serves as,” “showcases,” “leverages,” or “facilitates.” Keep a word when it is an exact or precise domain term.
- **Formulaic construction:** Remove forced threes, false ranges, “not just X but Y” framing, synonym cycling, and comparisons that do not change the point.
- **Filler and hedging:** Cut throat-clearing, repeated caveats, stacked modals, and phrases such as “in order to” or “it is important to note.” Keep uncertainty that the evidence requires.
- **Assistant performance:** Remove chatbot greetings, sycophantic praise, fake excitement, cutoff disclaimers, and closing offers that do not advance the work.
- **Formatting tells:** Reduce decorative bold, inline-header repetition, title case, decorative emoji, and punctuation used as a substitute for sentence structure. Preserve the language, project, and artifact conventions. Punctuation is not an error by itself.
- **Ambiguity:** Split sentences that carry multiple instructions or unrelated thoughts. Put conditions before guarded actions, keep modifiers beside what they modify, repeat a noun when a pronoun has multiple possible referents, and name the actor when responsibility matters.
- **Fancy synonyms:** Prefer the shortest familiar word that preserves precision. Keep established domain terms and exact API, UI, file, flag, command, and code names.

## Verify

Read the revision against the original and ask:

1. Did any fact, authority, condition, status, citation, identifier, schema, or required field change?
2. Does every remaining sentence tell this reader something needed to decide, act, verify, or understand?
3. Does the prose fit the artifact instead of performing a generic “human” or “technical” voice?
4. For agent-facing text, can the agent identify each trigger, branch, completion condition, and exact output without guessing?
5. What still makes the text sound generated, vague, or over-structured?

Restore any lost capability or nuance. Return the revised prose first, then report only material meaning, authority, or evidence questions that remain.

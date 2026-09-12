# Editing human prose

Use for meaning-preserving cleanup of supplied human-facing prose. Keep exact identifiers, quotations, facts, citations, schemas, required formats, accepted terminology, uncertainty, and the artifact's decisions intact.

Clean up the supplied prose; do not add an automatic editing pass to unrelated tasks.

## Establish the pass

Identify the reader, purpose, language/locale, intended voice, technical familiarity, and text that must remain exact. If a stylistic change would alter meaning, evidence, or authority, flag it instead of hiding the change inside cleanup.

Sound direct and specific. Vary sentence length naturally. Keep reference material neutral unless the artifact calls for a voice. Do not add deliberate mess, personality, or opinion merely to appear human.

## Remove slop by effect

Do not replace words mechanically. Rewrite when a pattern causes ambiguity, puffery, unsupported certainty, needless load, technical imprecision, or a voice mismatch.

- **Inflation and promotion** — remove grand significance claims, notability lists, promotional adjectives, generic challenge-and-triumph framing, and conclusions that add no fact or action.
- **Unsupported attribution** — replace “experts say”, “reports suggest”, and similar vagueness with the actual source or evidence-calibrated wording.
- **Abstract padding** — replace vague metaphors, weak nominalizations, copula avoidance, ornamental `-ing` clauses, weak verbs, and unmeasured adverbs with the concrete actor, mechanism, action, or result. Keep the term when it is exact domain language.
- **Formulaic construction** — remove forced threes, false ranges, “not just X but Y” framing, synonym cycling, and comparisons that do not change the point.
- **Filler and hedging** — cut throat-clearing, repeated caveats, stacked modals, and phrases such as “in order to” or “it is important to note”. Keep uncertainty the evidence requires.
- **Assistant performance** — remove chatbot greetings, sycophantic praise, fake excitement, cutoff disclaimers, and closing offers that do not advance the artifact.
- **Formatting tells** — reduce decorative bold, inline-header repetition, title case, decorative emoji, and punctuation used as a substitute for structure. Preserve the language/project conventions.
- **Ambiguity** — split sentences that carry unrelated thoughts, put conditions before guarded actions, keep modifiers beside what they modify, repeat a noun when a pronoun has multiple plausible referents, and name the actor when responsibility matters.
- **Fancy synonyms** — prefer the shortest familiar word that preserves precision. Keep established technical terms and exact API/UI/file/flag/command/code names.

## Preserve technical adequacy

Do not clean away the concepts the reader needs to reason correctly.

Check that:

- prerequisites and dependencies remain visible;
- causal/mechanical explanations still connect the important concepts;
- units, states, actors, scope, and conditions remain explicit where they matter;
- precise terminology has not been replaced by weaker “plain English”; and
- a reader at the intended familiarity level can follow the argument/procedure without reconstructing missing steps.

If an unfamiliar concept is required but unexplained, add the smallest useful bridge rather than hiding the gap behind smoother prose.

## Verify

Read the revision against the original:

1. Did any fact, citation, identifier, decision, status, uncertainty, or required field change?
2. Does each remaining sentence help the reader understand, decide, act, or verify?
3. Does the prose fit this artifact rather than a generic polished voice?
4. Is uncertainty still calibrated to the evidence?
5. Are all necessary technical concepts established well enough for the intended reader?
6. What still sounds generated, vague, inflated, or over-structured?

Restore lost nuance or technical meaning. Return revised prose first and report only material meaning, evidence, technical-adequacy, or voice questions that remain.

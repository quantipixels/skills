---
name: google-developer-style
description: Draft, revise, or review developer documentation and technical communication in the artifact's language with applicable principles from the Google developer documentation style guide. Use for API documentation, tutorials, procedures, reference text, technical explanations, status updates, reports, handoffs, or stakeholder messages; preserve language-specific conventions, project style, channel conventions, product truth, and code conventions as higher-authority inputs.
user-invocable: false
---

# Google Developer Style

Produce clear, concise, consistent developer documentation and technical communication. Apply Google guidance as an editorial standard, not as product authority, a general conversation style, or an inflexible compliance checklist.

## Establish the contract

1. Identify the requested operation: draft, revise, or review.
2. Identify the intended reader, artifact or channel, source format, formality, scope, and required deliverable.
3. Apply authorities in this order: user requirements, language-specific and project or product style, channel conventions, current product truth and code conventions, applicable Google developer documentation style, then other references.
4. Preserve technical meaning and commitments. Do not invent behavior, prerequisites, commands, results, links, UI labels, owners, decisions, dates, or future features.
5. Resolve a conflict in favor of reader clarity and local consistency. Record each material departure from the Google guide.

Read [core guidance](references/core-guidance.md) before drafting or assessing content. Apply the guide's ideas through the artifact's language and culture; do not translate English grammar, spelling, capitalization, politeness, or sentence patterns into universal rules. For technical communication, apply only transferable guidance about clarity, tone, audience, terminology, and accessibility; use documentation-specific structure and formatting only when the artifact supports them. When wording, terminology, accessibility, formatting, or a Google-specific exception controls the result and browsing is available, consult the applicable current page under `https://developers.google.com/style`. Do not generalize rules marked for English, Android, Google Cloud, Google Workspace, or another product.

## Work the content

For a draft, organize the reader's goal, prerequisites, concepts, procedure, verification, and next action before writing. Use only the sections that the task needs.

For technical communication, lead with the outcome, request, decision, or status. Include only the context the audience needs. Name actions, owners, dates, risks, and open questions when supplied. Separate facts, decisions, assumptions, and recommendations when confusing them could change the response. Match the channel's expected length and formality; do not force documentation headings, procedures, or report scaffolding into a short message.

For a revision, retain correct facts, code, links, identifiers, and intentional local terminology. Change structure and prose only as needed to satisfy the contract.

For a review, report findings before optional edits. Rank findings by effect on correctness, task completion, accessibility, global comprehension, and consistency. Give the exact text or location, the applicable guidance, and a concrete correction. Do not report a preference as a defect.

In all modes:

1. Put reader goals, conditions, and prerequisites before actions.
2. Use direct language and make actors, actions, and responsibility clear. Choose person, mood, tense, voice, and politeness that fit the language, audience, and channel.
3. Keep terminology, audience, orthography, capitalization where applicable, and parallel structures consistent.
4. When the artifact contains a procedure, make it minimal, ordered, testable, and safe to copy.
5. When the format supports them, use semantic headings, lists, links, tables, code formatting, UI formatting, and media alternatives.
6. Remove filler, vague references, cultural assumptions, unsupported ease claims, and repeated instructions.

## Verify

Check the final candidate for:

- preserved technical meaning and local authority;
- an explicit reader goal and sufficient context or prerequisites;
- short, direct prose that is clear to the intended language community and accessible to readers with varied proficiency;
- ordered procedures with one action or reader decision per step, when applicable;
- descriptive headings and links, logical heading levels, and parallel lists, when applicable;
- correct code, command, placeholder, and UI formatting;
- semantic and nonvisual access to links, images, tables, and interactive elements; and
- consistent terminology, orthography, capitalization where applicable, punctuation, and unambiguous date or time expressions.

When executable examples or product behavior are in scope, use the owning verification method. Editorial review alone cannot prove that code, commands, links, or UI steps work.

## Report

For a review or material revision, return the result with the following fields, scaled to the task and labeled naturally in the artifact's language. For a requested document or communication artifact, give the artifact first and add only the notes needed to prevent misuse.

- **Governing authority:** Name the supplied language and local style, or state what was not supplied.
- **Artifact or findings:** Give the requested draft, revision, or ranked review.
- **Departures and checks:** Name material departures from Google style and the checks completed.
- **Limitations:** Name each unresolved fact, accessibility, localization, legal, product-approval, or executable-verification gap.

Distinguish editorial conformance from factual or executable verification.

Keep code style with its language or project owner, exhaustive accessibility conformance with its accessibility owner, translation execution with localization, UI labels with product design, publishing or information architecture with their direct owners, and brand voice or interpersonal policy with its communication owner.

---
name: itumo
description: Establishes or reconciles a project's domain model - terms, identities, lifecycles, policy, boundaries, ownership and invariants - and maintains its Non-goals and decision records. Use for unsettled or conflicting terms and for writing or updating a decision record or the project's non-goals.
---

# Ìtumọ̀

Output: resolved domain meaning (terms, identities, relationships, ownership, invariants), and updates to the project's committed records of kind decision, non-goal and doc (domain language). Bounded-context distinctions are preserved; shared wording must not hide different models.

Needs: the unsettled term, boundary or record, and evidence you can read. If neither is named, return and say what is missing.

## Method

- Read only evidence that can settle meaning: the current domain-language source, governing decisions and policies, relevant code, tests, configuration and runtime behaviour, and bounded history for a conflict. Implementation proves current behaviour, not domain intent. Check a rule's applicability even when its words are familiar; do not treat stale records as immutable or invent business rules to reconcile a conflict.
- When an ambiguous, overloaded, synonymous or conflicting term can change scope, ownership, identity, state, policy or behaviour: state the ambiguity, use the smallest concrete scenario that separates the competing concepts, compare it with current language and evidence, and propose canonical wording only where evidence or domain authority supports it. When the user deliberately sets clear meaning, test only the boundaries needed; do not manufacture ambiguity.
- Ask one isolated consequential choice directly; interview the user when several consequential choices depend on each other. Unresolved structure or technical fitness is returned as a gap with its evidence. Do not turn implementation shape into domain vocabulary.
- Yorùbá/English technical terminology and glossary maintenance is language work; this skill keeps project-specific meaning.
- Domain language: if a domain-language source exists, read [domain language](references/context.md) and update it when the resolved model changed and you have write authority. If none exists, return the model delta and name the persistence gap only when the result must outlive the work; do not invent a convention. Do not build a competing memory store.
- Records: the README Non-goals section follows [non-goals](references/non-goals.md); decision records follow [decision records](references/adrs.md), which includes the fallback when the project has no convention and a decision record was authorized. Domain clarification alone does not authorize creating a decision record. Preserve each record's existing format and authority; a change must reflect established meaning or an authorized decision, never task notes, temporary deferrals or implementation history.
- When scoping, check the Non-goals section: conflicting work pauses until the user grants a one-time exception or a boundary change.
- Specs, architecture, docs, tests and policy that the new meaning affects stay with their natural owners; this skill supplies the clarified meaning.

## Done

Terms, identities and invariants are consistent with evidence, remaining conflicts carry their evidence, and any updated record is verified at its destination.

## Return

The resolved terms, relationships, ownership, invariants, distinguishing examples when needed, and any remaining conflict or consequential decision with its evidence. Newly exposed desire, fact or technical gaps go back to the caller with their evidence; a clarification starts no initiative. Report each updated record and its verification.

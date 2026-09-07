# Prune prose

Read this file only when the request explicitly asks to shorten prose, reduce verbosity, remove repetition, or lower instruction load.

## Pin what cannot change

Identify the artifact owner, reader, purpose, language, voice, required structure, and content that must remain exact. Preserve facts, evidence, citations, decisions, authority, schemas, identifiers, accepted terms, uncertainty, and required output fields.

For agent-facing prose, use the owning skill to map each capability as `retain`, `change`, `move`, or `remove`. Yọ Slop may compress settled behavior but cannot decide which behavior the agent no longer needs. Return an ambiguous cut to the owner. When pruning requires a structural change, the owning skill makes it.

Record the baseline word count for the bounded target. For agent instructions, count each active loading path instead of treating the whole package as one prompt. Use a supplied reduction target as a constraint, not proof of quality. Do not invent a quota.

## Remove load by effect

Prune in this order:

1. Remove filler, throat-clearing, repeated conclusions, and summaries that add no fact or action.
2. Merge instructions or explanations with the same behavioral effect. Keep one authoritative location.
3. Move branch-specific guidance to a direct reference only when the owner confirms the branch. Keep universal rules in the main instruction file and integration details with their asset or implementation.
4. Remove rationale that does not change judgment. Keep rationale that explains a non-obvious boundary or failure mode.
5. Remove examples that neither replace prose nor prevent a material error.
6. Replace long constructions with shorter familiar words, then repair sentence structure and rhythm.

Keep a repeated statement when it serves a distinct trigger, branch, safety, authority, recovery, verification, or owner boundary. A generation guard and its proof check are different controls. Do not merge them only because they use similar words.

Stop when the next cut would require guessing about meaning, coverage, authority, or intended voice. Shorter prose is not an improvement if the reader or agent must infer the missing rule.

## Prove the revision

Compare the final prose with the exact baseline.

- For human-facing prose, verify that facts, argument, required structure, citations, uncertainty, and voice remain intact.
- For agent-facing prose, verify every trigger, branch, action, prohibition, completion condition, status, field, and authority boundary. Use the owning skill to compare old and new against the same raw goal, context, authority, and stop condition when wording could change behavior. Do not add a prompt-evaluation harness for prose wording.
- Report before-and-after counts for material pruning. State which capabilities moved or merged and any proof gap. Never claim equivalence from word count alone.

Return the pruned prose first. Then report only material count, meaning, authority, or evidence notes.

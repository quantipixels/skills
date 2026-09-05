# Simplification for capable models

Scope: `ori` at `230a031`; three bounded skill revisions and one authoring-rule correction. This PR is independent of the `wo-pr`/`seda-pr` PR. It does not install skills, alter runtime code, or claim a portfolio-wide behavioral benchmark.

## Finding

The supplied babysit-PR screenshot makes the outcome and repeat loop easy to see. Its useful lesson is to specify the work, completion evidence, and consequential exceptions while leaving routine execution to the model. Its missing linked reference is unknown; the screenshot alone cannot establish complete safety or review behavior. No screenshot text or upstream code is vendored.

The QP source already says to trust capable agents, but some individual skills still turn reasoning checks into mandatory report fields. Redundant statements and always-loaded exceptional paths also increase instruction load. The PR workflow comparison found a concrete contradiction between direct feedback validation and a reference demanding universal triage. Repeating policy in several forms can undermine clarity even when each sentence sounds careful.

## Current primary-source guidance

Checked 2026-09-05:

- [Anthropic skill-authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) assumes a capable model, recommends adding only useful missing context, and matches instructional specificity to task fragility. Its progressive loading guidance supports keeping special cases behind meaningful triggers. It also calls for real-use testing; concise prose alone is not proof.
- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model), currently discussing GPT-6 Astra, warns that strong instruction-following can amplify conflicting skill instructions, unnecessary clarification, and over-broad testing. It recommends autonomous completion within intended scope and verification proportional to the change.

Inference for QP: keep semantic constraints, deliberate overrides, expertise, authority, and proof. Let the model select recoverable mechanics. These sources support an authoring approach, not a measured claim that every current Anthropic/OpenAI model safely handles every reduced skill. Model versions, tool availability, and host policies still matter. Revisit after a relevant provider-guidance change or an observed failure of a reduced contract.

## Applied changes

| Owner | Source finding | Change | Preserved boundary |
| --- | --- | --- | --- |
| `ro-wo` | Several checklists became a mandatory multi-part answer even for one premise | One evidence-led decision pass; proportional report | Four verdicts, uncertainty, alternatives, facts vs inference, authority |
| `handoff` | Fixed seven-section template plus repeated output checks | Coverage requirements; choose inline/file transport as needed | Exact state, proof, missing-source recovery, supplied next owner, sensitive-data exclusion |
| `se-triage` | Read authority and reporting inventory repeated across sections | Direct investigation/decision/publication structure | Classification/action identifiers, bounded reads, separate writes, provider reference, partial-write recovery |
| `ko-skill` | Admission rule did not explicitly distinguish reasoning coverage from output schema | Make ordinary path self-sufficient; require report structure only for real consumers | Instruction value test, expert depth, safety/authority and evidence |

Whitespace-separated main-file words, including frontmatter:

| Skill | Before | After |
| --- | ---: | ---: |
| `ro-wo` | 280 | 190 |
| `handoff` | 445 | 270 |
| `se-triage` | 653 | 421 |
| `ko-skill` | 1,415 | 1,454 |

The first three main files shrink by 497 words in total. Kọ grows by 39 words to make the missing authoring distinction explicit. There is no length quota and no claimed token-cost or latency improvement.

## Lessons and limits

1. Give the model the desired outcome and evidence for completion. Teach exceptional decisions, not ordinary Git/search/editing mechanics.
2. Make references conditional on a real branch. Moving text behind an unconditional read saves no active context.
3. Keep one statement of an invariant per loading path; independently invocable provider owners still need their own trust/authority rules.
4. Delegate for a distinct result, expertise, or independent proof. Do not create a handoff solely to repeat an obvious judgment.
5. Keep reasoning thorough and reporting proportional. A useful private checklist does not automatically deserve public headings or status fields.
6. Stop adding tests when required checks pass and no changed behavior remains uncertain. Do not replace deleted procedure with a new permanent prompt harness.
7. Measure changes and test consequential boundaries. “Newer models are smarter” does not authorize production changes or prove remote effects.

Leave `atona`, `arojinle`, `architect`, and provider references unchanged here. Their lifecycle, decision, specialist, and safety contracts need their own evidence before compression. The authoring lesson applies to future changes; this PR does not infer that every long resource is redundant.

## Proof

Package and plugin validation and the 21 repository contract tests pass locally. A fresh subagent context applied the candidates to five supplied scenarios: removing deployment authority/verification, incomplete debugging handoff, paginated triage evidence, timed-out comment publication, and failed reproduction without disproof. All retained the expected scope/evidence/recovery distinctions. Independent source comparison found no consequential regression in these three packages.

Host: ChatGPT Work; inherited parent model; 2026-09-05. These were simulated decisions with local source inspection, not deployment/provider writes, a blind before/after experiment, or a run on Anthropic models. The PR intentionally claims only this bounded proof. No standing prompt suite, new public skill, or cached model-version policy was added.

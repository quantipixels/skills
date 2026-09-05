# PR workflow simplification

Baseline: `ori` at `230a031`. Scope: `wo-pr`, `seda-pr`, their references, and affected routing/coverage. The user supplied a screenshot of a concise `babysit-pr` skill: identify the PR, establish readiness, handle CI/review findings, fix/publish, repeat, and summarize. This is comparison-only inspiration; the screenshot's linked bot-triage reference was not supplied and no upstream implementation was imported.

## Disposition

Adopt the outcome-led loop. Preserve provider safety, publication authority, current head/base evidence, and dependency reconciliation. Do not adopt blind bot approval or remove safeguards based on model capability alone.

| Capability | Disposition |
| --- | --- |
| Single-PR inspect/correct/publish/wait | Main path; explicit babysitting grants scoped correction authority |
| Watch/status/read-only request | Observation only; no reruns, replies, or source edits |
| Source correction proof/review | `alaga` remains the owner; `wo-pr` resumes its loop with the verified result |
| Routine Git/provider mechanics | Native tools; preserve exact target, safe staging, non-force push, and readback invariants inline |
| Stack frontier and affected-suffix reconciliation | Selective stack reference; behavior retained without mandatory status vocabulary |
| Feedback triage | Direct validation for clear claims; `se-triage` only for uncertainty |
| Old-head feedback | Revalidate applicability; do not ignore a still-present bug |
| Readiness result | Retain `PROVIDER_READY` / `STACK_PROVIDER_READY` for callers, independent of merge/approval |
| Full snapshot report | Replace with result-sized summary; retain identity/evidence needed to substantiate or resume |

The original main skill allowed direct feedback validation while its failure reference required every claim to go through triage and limited action to current-head feedback. The revision removes that contradiction. Removing three provider/Git reference files does not remove their safeguards: the common safety and publication rules now live in each independently invocable skill, while stack-specific detail loads only on that branch.

## Size evidence

Whitespace-separated words, including frontmatter; Markdown package counts include references, not this evaluation record.

| Skill | Main before → after | Package before → after |
| --- | --- | --- |
| `wo-pr` | 1,150 → 538 | 2,035 → 1,054 |
| `seda-pr` | 592 → 472 | 1,392 → 472 |

Ordinary `wo-pr` previously required its provider reference: 1,723 words before failure guidance. The new ordinary path is the 538-word main file; failure and stack guidance load only when relevant. The publication path drops from 1,392 to 472 words. These are instruction-size measurements, not latency, token-billing, or reliability claims.

## Behavioral evidence

Fresh isolated subagent contexts compared the baseline and candidate against the same eight supplied scenarios. Host: ChatGPT Work; model: inherited parent model (no override or separate Anthropic run); date: 2026-09-05. These are simulated decisions over fixed evidence, not live provider mutation tests or broad cross-model benchmarks.

| Scenario | Baseline observation | Candidate observation |
| --- | --- | --- |
| One target behind changing ancestor | Hold target; no ancestor mutation | Same |
| Fixed middle layer, stale descendant suffix | One authorized reconciliation handoff | Same |
| Read-only watch with real failure | Observe/report, no source fix | Same; all write exclusions explicit |
| Get ready, scoped source fix | Route correction; direct implementation prohibited | Correction authority explicit; `alaga` owns implementation/proof/review, then publication and loop resume |
| Existing PR base conflicts with intended parent | Stop for retarget authority | Same; no duplicate workaround |
| Same head, moved base, then write timeout | Revalidate narrative; read back before retry | Same |
| Old-head real bug, green bot, unrelated blocking redesign | Safe conclusion required resolving contradictory instructions | Preserve real bug and human blocker without contradiction |
| Ready ancestor remains open | Advance to child without merging | Same |

Independent static review found no blocking safety/stack defect. Its correction-owner ambiguity was removed by explicitly retaining `alaga` for source fixes. The existing stacked-stewardship corpus remains; its standalone case now reflects the intentional watch/babysit authority distinction. No keyword assertion suite was added. Provider execution, automatic activation, and Claude-host behavior are not proved by these simulations; live CI is reported by the PR.

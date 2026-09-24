# Optional coordination and judgment cases

Select a case to investigate a consequential regression or misdirection. This is not a certification suite for every skill. A retained case can be valuable without running on each change; its presence is not evidence of successful behavior.

## Select the failure mechanism

| Question | Candidate cases | Distinction to preserve |
| --- | --- | --- |
| Does accepted work actually finish? | [C01](actors/C01-project-verification.md), [C03](actors/C03-batching-repair.md), [C04](actors/C04-resume-accepted-plan.md) | Reusable verification, a simple direct repair, and resumption are different outcomes. |
| Does the agent respect the requested stop? | [C02](actors/C02-diagnosis-only.md), [C05](actors/C05-pr-status-not-merge.md), [C06](actors/C06-named-data-change-plan.md) | Diagnosis, read-only status and planning do not authorize implementation or publication. |
| Does a changed method choose sufficient evidence without excess work? | [C08](actors/C08-engineering-coverage.md), [C09](actors/C09-direct-owner-evidence.md), [C13](actors/C13-engineering-guidance.md) | Select one named subcase and a relevant sufficient-proof or ordinary-work control. |
| Are structure, meaning and prerequisites handled correctly? | [C10](actors/C10-compression-boundaries.md), [C12](actors/C12-desire-domain-fitness.md) | Missing versus settled intent, domain evidence and technical fitness; narrow interfaces versus lost safeguards. |
| Are critical judgments and returned artifacts faithful? | [C15](actors/C15-adoption-boundaries.md) | Recovery, framework invocation, retained guards, source versus active guidance, accepted layout and write authority. |
| Does documentation reconciliation avoid changing the wrong truth? | [C16](actors/C16-documentation-maintenance.md) | Audit/sync, current/history, missing/sufficient proof, generated sources and no-impact controls. |
| Is a proposed private operation actually within the requested boundary? | [C17](actors/C17-private-serving.md) | Audience/identity, spoofable filtering, disclosure, expiry and a legitimate positive path. Operational claims need executed proof. |
| Can a growing plan shed optional work without losing real obligations? | [C18](actors/C18-scope-growth.md) | Unchanged sufficient proof versus a compatibility regression hidden by green UI checks. |

Keep [common outcomes](reviewers/expected-outcomes.md), [C15 outcomes](reviewers/C15-adoption-outcomes.md), [C16 outcomes](reviewers/C16-documentation-outcomes.md), [C17 outcomes](reviewers/C17-private-serving-outcomes.md) and [C18 outcomes](reviewers/C18-scope-growth-outcomes.md) hidden from actors. Evaluate the selected behavior, not skill-name matching or a prescribed procession through companions. An explicitly requested entrypoint still matters for source identity and authority.

## Run one selected boundary

Supply only the selected request and its necessary setup. Do not give an actor the whole omnibus file, private rubric or other attempts. Use fresh disposable sessions/workspaces where needed; freeze source, task and criteria before comparison. Set a finite authorized budget and preserve failed, blocked and invalid attempts. Directory separation is not host isolation, and workers are optional.

Record whether the condition is routed, direct, supplied-instruction or native discovery. Compare like with like. C09.4 supports a separately labelled routed condition so the duplicate cache prompt need not be maintained in C08; a direct success does not establish routing. For the routed condition, remove the direct-skill label rather than telling the router which owner to select.

C01 can use `evals/engineering/fixtures/verification/`; C02 uses `profile/`; C03 uses `batching/`; C04 and C06 use separate copies of `migration/`. A response proposal does not establish real actions or defect rejection. Use a representative project when it provides better proof. No case authorizes live production cleanup, public exposure, installation, publication or merge.

Useful contrasts stay available: C08.1/11 distinguish improvement from read-only assessment; C08.10 and C09.10 guard against ceremony; C12 retains settled-input controls; C16.A/B distinguish audit and sync, while L/N distinguish uncovered and sufficient proof. C08.3 and C15.1 remain separate: one is initial mitigation routing, the other is a post-mitigation closure judgment. The PR [evidence pack](../pr-review/README.md) retains distinct standalone truthfulness and proportionality controls.

For scope-growth changes, use C18.1/2 as the focused judgment contrast. Reuse C03 for executed ordinary delivery, C02 for the read-only boundary, C06 for explicitly requested planning, and C15.4 for retained guards rather than duplicating those tasks. Select only the additional control needed by the claim. C18's reviewer notes define a bounded matched comparison; no fresh runs or improvement are implied by retaining the cases.

## Focused retirements

Stable IDs are not renumbered, and historical results remain tied to their original revision.

| Retired question | Disposition |
| --- | --- |
| C07 heading-edit route and C11 updater questionnaire | Retired in the preceding cleanup. Keep relevant ordinary-work controls; utilities do not need standing certification. |
| C08.5 generic framework upgrade | Retire the low-signal selection question that largely prescribes its own actions. Real framework/compatibility obligations remain in project-backed scenarios, not a claim of equivalent routing evidence. |
| C08.6 cache proposal | Consolidate its clean-build, generator-input and artifact constraints into C09.4; retain separately labelled direct/routed conditions when needed. |
| C09.5 routine research acquisition | Retire the tool-selection questionnaire. Real acquisition uses source-appropriate checks; C09.3/9 retain consequential incomplete-evidence judgments. |
| C09.7 CSV-parser selection | Retire a proposed parser choice, not data-integrity safeguards. C15.7 retains executed write-authority/mapping checks; it does not certify multiline CSV parsing. |
| C16.J1–J3 adjacent-owner quiz | Retire generic wording/overview/ADR selection questions. C16 keeps historical meaning, separate knowledge, no-impact, direct delivery and planning/closure controls. |

No whole pack is removed merely because it is small, synthetic, unrun or utility-related. C17 remains available for actual audience, disclosure or expiry uncertainty, without a routine model-eval requirement. Settlement, batching, migration, independent oracles and their integrity tests remain unchanged.

Historical [initial observations](observations/2026-09-15.md), [coverage](observations/2026-09-15-coverage.md) and [direct-owner observations](observations/2026-09-15-direct-owners.md) retain source identities and limitations. The [pre-cleanup source](https://github.com/quantipixels/skills/tree/7ff48c0b2ca929ebcd8545eb9092ec67c4917f2f/evals) preserves retired prompts. Do not relabel old results as evidence for edited tasks or rubrics. C15's release-origin naming does not require another Revision 8 campaign.

C14 (Codex profile admission) was retired with `codex-orchestra` on 2026-09-24. Its ID is reserved; earlier observations retain their original candidate and meaning.

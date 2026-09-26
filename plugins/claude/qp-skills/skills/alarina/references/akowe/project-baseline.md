# Useful project documentation defaults

Use for project setup or a broad request to improve, establish or make project documentation useful for contributors and agents. Establish the baseline below rather than only polishing files that already exist. A narrow document edit or personal-environment setup does not trigger a repository-wide pass. A read-only audit assesses the same useful coverage without creating or changing files.

A project setup or broad documentation-improvement request authorizes creating and reconciling the useful missing documents within that scope. Proceed from established evidence and accepted decisions without asking separately for each filename. This authority records project expectations; it does not invent new policy, exclusions or architectural decisions. Resolve only consequential missing choices with the user and continue independent documentation work.

## Establish useful coverage

Inspect existing destinations and reader paths first. Prefer their established names and formats; several needs can share a concise document when that is easier to maintain. Create the fallback only when its content is useful and no existing owner covers it. Empty templates, generic advice and a file-count target do not establish a baseline.

| Need | Useful content and default home | Owning method |
| --- | --- | --- |
| Understand and start the project | Purpose, current capabilities, prerequisites and a usable first-run path in `README.md` or the established introduction. Link deeper procedures. | [oro-eniyan](../../commands/oro-eniyan.md) for the reader-facing text. |
| Locate and safely change the system | Components, responsibilities, dependency direction, important flows, boundaries and source pointers in the existing overview or `ARCHITECTURE.md`. Describe a planned system as planned. | [architect-document](../../commands/architect-document.md). |
| Build and review consistently | Stable project-specific constraints, conventions, compatibility obligations and verification expectations in established standards or contributor guidance; otherwise `CODEBASE_STANDARD.md`. Keep detailed review criteria here and point to existing mechanical enforcement. | [oro-sigidi](../../commands/oro-sigidi.md) for agent-consumed standards, using supported project expectations; [oro-eniyan](../../commands/oro-eniyan.md) for human-facing presentation. |
| Avoid repeatedly proposing excluded work | Confirmed durable project exclusions in the established boundary document or root `.nongoals`. Temporary deferrals stay with their plan. | [amose-nongoals](../../commands/amose-nongoals.md), preserving its admission and project-boundary authority. |
| Work, verify and recover | Actual development/check commands, prerequisites, relevant CI equivalents, driving recipes and recovery pitfalls in existing contributor instructions or runbooks. Add API, deployment, migration or operations guidance where the project has those reader needs. | Reuse [alaga-verify-project](../../commands/alaga-verify-project.md) evidence; creating prose does not authorize building a missing harness or performing live effects. |
| Find the guidance at the point of use | A short `AGENTS.md` or host-supported equivalent pointing to the relevant owners, with only crucial project navigation and execution constraints inline. | [oro-sigidi](../../commands/oro-sigidi.md); preserve existing host conventions. |

Standards need evidence of intended practice: governing instructions, accepted decisions, maintained contribution guidance, actual enforcement and representative implementations. Current code alone does not turn an accidental pattern or defect into a requirement. Preserve useful rationale or a concrete example where a rule would otherwise be misapplied. Keep unsupported proposals distinct from established standards.

Use [amose-context](../../commands/amose-context.md) for resolved project-specific language that would otherwise cause misunderstanding, and [amose-adrs](../../commands/amose-adrs.md) for qualifying confirmed decisions. Their content and admission rules govern whether a glossary or ADR is needed. Do not infer a non-goal from an absent feature or invent decision history to populate the baseline. Record a confirmed exclusion only when its original decision or current request supplies explicit project-boundary authority; otherwise report the gap. Reuse sufficient existing authority without reopening the decision.

## Connect and verify

Keep shared project knowledge in the repository or its established shared destination, following [records](../records.md); private task storage is not its home. Link the useful documents from the entrypoint contributors or agents actually read. Reuse the same standards during construction and local review; avoid copies that can diverge.

Check supported claims and the affected reader path through [documentation evidence](evidence.md). Exercise changed examples or commands proportionately within existing authority; mark unexecuted recipes and unavailable evidence honestly. Finish with useful coverage established or specific unresolved gaps. Briefly identify what was created, reused or deliberately unnecessary; no separate baseline report, manifest or recurring full audit is required.

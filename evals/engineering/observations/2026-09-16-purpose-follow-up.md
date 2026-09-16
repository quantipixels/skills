# PR161 purpose follow-up

This follow-up resumes the authorized corrections to PR161 at `242ead02b03d5436656b1ab801f723fdfdd70bb8`. It preserves the earlier [rebuild record](2026-09-16-guidance-rebuild.md), including invalid trials. The objective is useful independent skill behavior, not a word-count target.

## Instruction disposition

- Restore Atunwo's existing-system assessment method in a compact local reference and reconnect its branch. Ownership, lifecycle, caller burden, readability and operational proof remain explicit.
- Restore the provider read-only boundary for an explicit parity-only request.
- Restore source-backed Yorùbá tone and morphology examples. These reduce required rediscovery without presenting an example as a universal productive rule.
- Make Irinse's existing question-first selection more direct, clarify that tool references do not bundle binaries/connections, and add bounded entry patterns for structural and symbol-aware retrieval.
- Carry selected Irinse capabilities, availability, coverage limits and decisive locators into Alarina worker briefs. Native hosts still own worker lifecycle; tool output still does not own engineering judgments.

## Bounded supplied-guidance probes

Two fresh Codex CLI 0.154.0 sessions received the same four self-contained tasks: assess a timeout/retry payment defect, handle parity-only after earlier publication authority, choose retrieval capabilities for three questions, and correct tone/gerund misconceptions. One arm used the six relevant files at `242ead02` (the assessment reference did not exist); the other used the corrected working files. Each run had a 180-second subprocess bound, requested `gpt-5.6-sol` with high reasoning, and requested read-only execution. No tool calls appear in either returned trace.

The rubric was fixed before execution: identify the duplicate-charge mechanism and proof limits; retain provider read-only state; choose literal/IDE/AST retrieval with its limits and no implied installation; give accurate attested language examples without overgeneralization. This tests supplied-guidance assessment and decisions, not discovery or executed workflows.

Both responses found the payment defect, rejected arbitrary wrappers, preserved parity-only state and selected appropriate retrieval capabilities. The earlier language response could not supply an attested gerund from its excerpts and did not explain the conventional unmarked mid tone explicitly. The corrected response supplied `bí/bi/bì`, `tà → títà` and `lò → lílò`, with the productive-rule limit. The corrected payment response proposed a provider-supported idempotency key without establishing provider support; treat that as a conditional design direction requiring verification, not a proved repair.

**Disposition:** retain the source-backed corrections. The language result illustrates their intended utility. Incremental end-to-end benefit remains inconclusive: one run per arm, an unblinded local judge, no independently attested clean-room context, and no executed engineering task. Both outputs carried personal style cues despite attempted configuration isolation. Do not use their latency/token differences as a cost comparison. The underlying host/system prompt was not captured, so absence of tool calls does not prove absence of other injected guidance.

Local evidence: `/tmp/qp-pr161-probe.py` and `/tmp/qp-pr161-probes/` contain inputs, fixed rubric, answers, JSONL traces and records. Supplied-guidance SHA-256: before `00270655d9f23e37a5595ec22de210bd62a8bde791ca34d452ca12c0bdc2b7a9`; after `f59d6529a4499e0083ec7f1991d7aaa099cc3a89c987d8add9f4f75dd525ee68`. CLI-reported input/output tokens were 16,787/1,867 and 17,583/1,546; cached input differed (8,960 versus zero). Elapsed subprocess time was 42.15 and 64.43 seconds. Monetary cost and independently observed model identity are unknown. Raw temporary traces are not packaged.

## Native updater mechanics

Claude Code 2.1.263 completed a controlled local-marketplace update in a disposable `CLAUDE_CONFIG_DIR`. A committed QP fixture at `242ead02` was installed, then a README marker change was committed as `b1c6e2902bd358e68740fbdfad82c496f1d30c93`. Native `plugin marketplace update qp-skills` and `plugin update --scope user qp-skills@qp-skills` changed the installation from `242ead02b03d` to `b1c6e2902bd3` and reported “Restart to apply changes.” The installed README SHA-256 changed from `62339d1a73563ffd8ed8834fefb73a2511973dc981082d4cb011f5b1e9151370` to `d6febafb4aee6f3a53ca97bd850512e71242add65e60c22951e84c3bdebb27f9`.

The conductor inspected the manager log and before/after content-hash records. Evidence: `/tmp/qp-pr161-update-check/native-update.log`, `plugins-before.json`, `plugins-after.json`, and the two `installed-hashes-*.txt` files. This demonstrates native installation/discovery metadata and changed content in a local fixture. It does not demonstrate remote marketplace refresh, Codex update mechanics, agent invocation of qp-update, active-session reload, or mutation of the user's active installation. The fixture excludes uncommitted instruction corrections; this is an updater-mechanics test, not installation acceptance of the final candidate.

## Mechanical verification

The 34 engineering tests passed with warnings enabled; the session-evidence regression also passed. These test shipped harness mechanics, not prose utility. Relative skill links resolve, all 19 skill frontmatter blocks are unchanged, invocation YAML and playbooks are unchanged, and `git diff --check` passes. Independent review accepted the restored assessment, authority, retrieval, language and evidence changes without actionable findings; it did not rerun the model probes or tests. Existing invocation policies and playbook files remain outside this correction's scope.

## Source-informed additions

Robert Martin's [Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) ties responsibility to the people and reasons that drive changes. Architect's module-design reference now makes that discriminator explicit while retaining its deletion test and caller-burden criteria. This source-based clarification was added after the probes and was not measured by them. Existing substitution, command/query, information-hiding and behavioral-proof guidance already covers much of the useful Clean Code material; no blanket SOLID checklist, function-length quota or mandatory TDD workflow was added.

ContinuousClaudeV4.7's [autonomous instructions](https://github.com/parcadei/ContinuousClaudeV4.7/blob/main/.claude/skills/autonomous/SKILL.md) and [handoff instructions](https://github.com/parcadei/ContinuousClaudeV4.7/blob/main/.claude/skills/create-handoff/SKILL.md), inspected 16 September 2026, support the useful pattern of giving workers bounded context and returning compact evidence with locators. The Alarina brief change adopts that narrow lesson. Its larger prescribed orchestration/reporting pipeline is not adopted: QP retains cohesive conductor work, native worker lifecycle and proportionate verification. This is inspection of advertised instructions, not executed evidence of ContinuousClaude's effectiveness.

## Remaining limits

No valid clean-room paired end-to-end trial establishes package-wide improvement, equivalence or savings. Native discovery and active-session loading of the final corrected package remain untested. Those limits stay visible in the PR; neither package validity nor the controlled update substitutes for them.

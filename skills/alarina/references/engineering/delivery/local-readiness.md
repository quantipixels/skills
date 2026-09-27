# Local delivery and publication readiness

Read before closing a substantive change or publishing a new candidate. Delivery, publication and PR corrections consume this same contract; reusing a current result does not require another review. Status-only and description-only requests keep their existing stopping point.

## Establish the candidate locally

Identify the intended integration base and complete proposed change, including pending files and generated outputs. Review the content that will be committed and pushed, not just the last commit or a stale PR diff. Record a commit/tree identity when available; for an uncommitted candidate, identify the inspected diff and pending files well enough to detect intervening changes.

Use the project's existing standards and verification path. Run relevant checks against that candidate and inspect the final diff for unintended changes and missing consumers. Name genuinely remote-only checks before publication; CI supplies those checks and an independent backstop, while locally available proof is completed before pushing. Missing required local proof remains a readiness gap.

For registered project gates, use the [configuration utility](../../productivity/environment/configuration.md): `doctor` exposes missing local capability, `verify` executes selected checks and captures private evidence, and `freshness` detects changed candidate/configuration/base. Inspect selection and omitted checks; a partial run is not the full gate. Test proof needs actual positive passing-test counts, not an exit code from an empty or skipped selection. Existing project verifiers can supply equivalent evidence directly. When the project lacks a local gate or required verifier, explicitly advise the user and establish the scoped capability through setup or delivery rather than relying on CI to find the first defects.

When CI coverage or equivalence is uncertain, or relevant workflows/inputs changed, read [CI/local equivalence](../verification/ci-local-equivalence.md). Reconcile relevant obligations with local execution and named remaining proof. A full configured gate can still omit a required check; its passing receipt is mechanical evidence, not the final acceptance decision.

Before release readiness, confirm the project’s CI-expectation reconciliation is current under that contract. Refresh affected obligations when requirements, supported environments or provider gates changed; reuse current results for unaffected boundaries. An old green run does not establish current required-check coverage.

## Review and correct

For substantive changes to behavior, contracts, instructions, packaging, migrations or technical structure, obtain an independent [atunwo](../../../commands/atunwo.md) review before declaring the candidate ready. Supply the candidate/base, accepted behavior, applicable project standards, actual check results and material risks. One suitably scoped reviewer is sufficient; use its light/deep judgment rather than a fixed roster or line-count threshold. A reviewer must not be the author of the portion it independently accepts. Author self-checks are useful but do not establish independence.

Reuse a completed delivery/TDD review when it covers the final candidate. Purely mechanical changes with no material semantic effect may use focused checks and diff inspection instead; state why that is sufficient. Respect an explicit user request to skip review and disclose the remaining assurance limit. If independent review is required but unavailable, report that gap; do not silently relabel a self-review or push merely to obtain the first review in CI.

The change owner assesses findings against evidence, applies warranted corrections in a coherent local batch through [alaga-deliver](../../../commands/alaga-deliver.md), and reruns affected checks. Resolve material defects and proof gaps before publication. Record supported rejection or deferral of a finding; optional preferences and unrelated debt do not create an endless correction loop. Return consequential corrections or contested claims for focused review. Keep valid evidence for untouched paths; changed content, base or requirements invalidate only dependent conclusions. Do not call delivery recursively when it is already the active owner.

For consequential failure claims or unresolved disagreement, apply Atúnwò's conditional [adversarial and council method](../review/adversarial-and-council.md). Select depth and independent perspectives by the actual uncertainty; retain the same candidate, evidence and authority boundaries.

## Carry the result into publication

Keep a brief result in the conversation or existing task record: candidate/base, actual review coverage, decisive checks, remaining findings and remote-only proof. Link an existing check receipt when used instead of duplicating it into another report. Before commit/push, confirm the selected files and resulting candidate still match that evidence; account for hook-generated edits, configuration/requirement changes and other intervening changes. An older head's pass does not accept new content. Mechanical freshness does not prove independent review or accept a failed run.

Publish when applicable local proof and review support readiness, or an explicit user override covers the identified gap. Publication authority remains separate. Required CI checks and provider feedback still need disposition before provider readiness; local acceptance does not authorize merge or weaken those requirements.

For PR follow-up, assess all available feedback before batching warranted fixes and publishing the next reviewed candidate. A valid escaped finding can improve its actual local check or review guidance within scope; use [ayewo-retro](../../../commands/ayewo-retro.md) when understanding a recurring escape needs session analysis. Fewer escaped defects and corrective pushes are useful signals; bot silence is not correctness evidence.

# Local delivery and publication readiness

Read before closing a substantive change or publishing a new candidate. Delivery, publication and PR corrections consume this same contract; reusing a current result does not require another review. Status-only and description-only requests keep their existing stopping point.

## Establish the candidate locally

Identify the intended integration base and complete proposed change, including pending files and generated outputs. Review the content that will be committed and pushed, not just the last commit or a stale PR diff. Record a commit/tree identity when available; for an uncommitted candidate, identify the inspected diff and pending files well enough to detect intervening changes.

Use the project's existing standards and verification path. Run relevant checks against that candidate and inspect the final diff for unintended changes and missing consumers. Name genuinely remote-only checks before publication; CI supplies those checks and an independent backstop, while locally available proof is completed before pushing. Missing required local proof remains a readiness gap.

## Review and correct

For substantive changes to behavior, contracts, instructions, packaging, migrations or technical structure, obtain an independent [atunwo](../../../commands/atunwo.md) review before declaring the candidate ready. Supply the candidate/base, accepted behavior, applicable project standards, actual check results and material risks. One suitably scoped reviewer is sufficient; use its light/deep judgment rather than a fixed roster or line-count threshold. A reviewer must not be the author of the portion it independently accepts. Author self-checks are useful but do not establish independence.

Reuse a completed delivery/TDD review when it covers the final candidate. Purely mechanical changes with no material semantic effect may use focused checks and diff inspection instead; state why that is sufficient. Respect an explicit user request to skip review and disclose the remaining assurance limit. If independent review is required but unavailable, report that gap; do not silently relabel a self-review or push merely to obtain the first review in CI.

The change owner assesses findings against evidence, applies warranted corrections in a coherent local batch through [alaga-deliver](../../../commands/alaga-deliver.md), and reruns affected checks. Resolve material defects and proof gaps before publication. Record supported rejection or deferral of a finding; optional preferences and unrelated debt do not create an endless correction loop. Return consequential corrections or contested claims for focused review. Keep valid evidence for untouched paths; changed content, base or requirements invalidate only dependent conclusions. Do not call delivery recursively when it is already the active owner.

## Carry the result into publication

Keep a brief result in the conversation or existing task record: candidate/base, actual review coverage, decisive checks, remaining findings and remote-only proof. No separate report or receipt file is required. Before commit/push, confirm the selected files and resulting candidate still match that evidence; account for hook-generated edits or other intervening changes. An older head's pass does not accept new content.

Publish when applicable local proof and review support readiness, or an explicit user override covers the identified gap. Publication authority remains separate. Required CI checks and provider feedback still need disposition before provider readiness; local acceptance does not authorize merge or weaken those requirements.

For PR follow-up, assess all available feedback before batching warranted fixes and publishing the next reviewed candidate. A valid escaped finding can improve its actual local check or review guidance within scope; use [ayewo-retro](../../../commands/ayewo-retro.md) when understanding a recurring escape needs session analysis. Fewer escaped defects and corrective pushes are useful signals; bot silence is not correctness evidence.

# Turn a proven local improvement into an optional contribution

Use when the user requests a contribution or enables `contribution_suggestions` in [configuration](environment/configuration.md), after a supported retrospective or a mature workflow boundary: a repeated path has useful evidence, a local correction has survived reuse, or a deterministic defect has a reproducible failure and verified repair. A completed task alone is not a reason to solicit a contribution. Suggestions are off by default.

First identify the maintained owner. Prefer a project-local correction for project-specific conventions and data. A contribution to QP fits when the mechanism or instruction improves a reusable Alárinà contract, the benefit is supported, and existing guidance does not already own it. Inspect the actual instructions, scripts, tests and callers; similar titles do not establish equivalence.

## Suggest at a useful boundary

Briefly state the reusable improvement, observed challenge and benefit, evidence limits, and where it would belong in QP. Offer the choice to prepare or submit a proposal only when useful. Keep a declined suggestion declined for the current work; do not nag at every completion. No telemetry, history mining, remote issue, PR or message follows from this suggestion.

When preparation is requested or already in scope, author a **new curated proposal**, starting from the general method rather than copying a transcript, local recipe, repository diff or logs. Use synthetic examples and aggregated, non-identifying observations. Include costs, failure cases and local challenges as well as benefits. Label expectations separately from measured outcomes. Do not claim broad improvement from one use.

Remove personal identifiers, user paths, customer/project names, internal URLs/hosts, private issue/commit/thread identifiers, credentials, proprietary code/data and identifying business details. Public API or project facts may be included only when they are actually public and useful. Do not merely replace a few obvious names in a private capture. If the useful claim cannot be expressed without disclosing private material, keep it local.

Use the [proposal specimen](templates/contribution-proposal.md) for machine preflight. The file contains a single `alarina-contribution+json` block with only purpose, generic change, synthetic example, challenges, benefits, evidence limits and sanitized test result. Save it in the resolved private artifact location; this is still a draft, not a public record.

```sh
python3 <alarina-directory>/scripts/alarina.py contribution-check <curated-proposal.md>
```

The check detects likely private paths, identities, addresses, tokens and transcript content without returning matched values. It also checks the allowlisted structure. `no-patterns-found` is only a heuristic result; an agent must inspect the complete proposal and the user must review the exact outgoing content before authorizing submission. The helper neither redacts automatically nor guarantees anonymity.

## Publish only the approved content

If the user authorizes contribution, use the established repository contribution procedure and publication tools. The exact reviewed text and intended destination define the scope; additional attachments or private evidence need their own review. Recheck changed content before sending. Do not include local evidence links or hidden metadata that reveal private state. Preserve upstream attribution/licences when adapting third-party code; authored QP changes are attributed to Oluwaseyi Sobande.

Keep local adoption independent of upstream acceptance. Record an accepted upstream fix's version/retirement condition at the local workaround owner, and remove or revise local duplication only after verifying the replacement. No recurring submission bot or automatic cleanup is implied.

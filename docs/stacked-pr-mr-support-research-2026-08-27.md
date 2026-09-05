# Stacked pull request and merge request support

**Research date:** 2026-08-27
**Question:** What native support do GitHub and GitLab provide for stacked pull requests or merge requests?

## Result

Both products support stacked review workflows natively, but their maturity and control surfaces differ.

| Product | Native support | Current status | Core model |
| --- | --- | --- | --- |
| GitHub | Yes | Public preview | An ordered stack of same-repository pull requests. Each higher pull request targets the branch of the layer below it. |
| GitLab | Yes | Introduced in GitLab 19.1 | GitLab detects a stack from the source and target branches of open merge requests. Each higher merge request targets the source branch of the layer below it. |

GitHub is the stronger choice when an integration needs first-class stack APIs, webhooks, and whole-stack merge behavior. GitLab has native stack detection and review navigation, but its documented API exposes merge-request dependencies rather than a first-class stack resource.

## QP adoption record

This research materially shaped `seda-pr` and `wo-pr`; `alaga` consumes only the resulting exact-candidate identity rule.

- **Local adoption:** preserve the exact PR/MR head-to-base/source-to-target relationship as the semantic stack boundary; use provider-native stack metadata when current and available; treat a changed base as candidate-invalidating evidence even when the head is unchanged; keep provider topology separate from mutation authority.
- **Not adopted as durable truth:** provider preview/version status, exact stack API/CLI commands, automatic retarget/rebase behavior, and provider-specific merge semantics. The skills now require those volatile details to be revalidated from current provider evidence when they matter.
- **Source treatment:** official GitHub/GitLab documentation and GitHub's changelog were compared/paraphrased; no provider code or assets were copied into QP, so no upstream code licence is imported by this adoption.
- **Local implementation:** PR #82 (`feat(pr): make stacked stewardship converge bottom-up`), with the Kọ Skill tightening and merged-base reconciliation recorded in that PR history.
- **Refresh trigger:** re-run provider research when current stack metadata/branch topology no longer explains observed behavior, an evaluator case fails because provider semantics changed, or QP broadens stack mutation/merge authority.

The dated research below remains historical evidence. Runtime provider references intentionally point back to current provider behavior instead of treating every statement below as timeless contract.

## GitHub

GitHub supports stacked pull requests as a public-preview feature. A stack contains two or more pull requests in one repository. Each pull request above the bottom layer targets the head branch of the pull request below it. GitHub can create and link stacks in the web UI, then show the ordered layers in a stack map. [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)

GitHub announced the public preview on 2026-07-30. The announcement says that repository rollout began then and that merge-queue support would roll out over following weeks. [Stacked pull requests are now in public preview](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)

The feature includes these integration surfaces:

- GitHub documents optional `gh stack` CLI extension commands for creating, rebasing, synchronizing, restructuring, and navigating stacks. Standard Git plus the GitHub web UI can also create a stack. [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)
- The REST API can list, create, extend, and dissolve stacks. Pull request resources include stack membership. GraphQL has read-only stack fields, and `pull_request` webhooks include a `stack` object. [Stacked pull request APIs and webhooks](https://docs.github.com/en/pull-requests/reference/stacked-pull-requests-apis-and-webhooks) and [REST API endpoints for pull request stacks](https://docs.github.com/en/rest/pulls/stacks)
- GitHub requires bottom-up merging. A selected higher layer can merge its lower portion as one operation. After a partial stack merge, the remaining open pull requests are retargeted and rebased as needed. All three merge methods are supported. [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- Merge queues preserve dependency order. Removing a queued layer also removes all layers above it. GitHub can increase a merge group by up to 50% to retain a stack, and it can split larger stacks across consecutive groups. [Stacked pull request rules](https://docs.github.com/en/pull-requests/reference/stacked-pull-requests)

The important limits are that branches must be in the same repository, GitHub Desktop does not support stacks, and public-preview behavior can change. A stack cannot be unstacked after a layer merges or enters the merge queue. GitHub also evaluates branch protections, required checks, required reviewers, CODEOWNERS, and Actions against the stack trunk for every layer. [Managing stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/managing-stacked-pull-requests) and [Stacked pull request rules](https://docs.github.com/en/pull-requests/reference/stacked-pull-requests)

## GitLab

GitLab supports stacked merge requests natively from GitLab 19.1. The feature is documented for Free, Premium, and Ultimate on GitLab.com, GitLab Self-Managed, and GitLab Dedicated. GitLab detects a stack when one open merge request targets another open merge request's source branch, or the inverse relationship exists. The merge request header provides a stack control for navigation and position. [Stacked merge requests](https://docs.gitlab.com/user/project/merge_requests/reviews/stacked_merge_requests/)

GitLab recommends merging bottom-up. When the bottom merge request merges to the default branch, GitLab retargets the next merge request to the default branch and continues up the chain. GitLab does not require that order, so a different order remains possible. The UI shows a maximum of 20 merge requests in one stack. [Stacked merge requests](https://docs.gitlab.com/user/project/merge_requests/reviews/stacked_merge_requests/)

GitLab CLI has a separate stacked-diffs workflow through `glab stack`. It can create commits and branches and synchronize them into chained merge requests. GitLab documents this CLI workflow as experimental from GitLab CLI 1.42.0. That experimental CLI status does not make the GitLab 19.1 server-side stacked-merge-request UI experimental. [Stacked diffs](https://docs.gitlab.com/user/project/merge_requests/stacked_diffs/)

GitLab's Merge Requests REST API provides explicit `blocks` dependency relationships. They can be read, created, and deleted, including across projects. A dependency means that another merge request must resolve before the current one can merge. It is distinct from a stacked merge request, which GitLab infers from branch topology. The documented API has no first-class stack object, stack-membership endpoint, stack-order endpoint, or whole-stack merge operation. [Merge requests API: dependencies](https://docs.gitlab.com/api/merge_requests/#retrieve-merge-request-dependencies)

Merge trains are also separate from stacks. They queue merge requests and run cumulative merged-results pipelines, but they do not create stack relationships. They are Premium and Ultimate features and require repository and pipeline configuration. [Merge trains](https://docs.gitlab.com/ci/pipelines/merge_trains/)

## Practical comparison

| Need | GitHub | GitLab |
| --- | --- | --- |
| Native review navigation | Yes | Yes |
| Stack inferred from branch-target chain | Yes, with stack metadata | Yes |
| First-class API for stack lifecycle | Yes, REST | No documented stack API |
| Webhook stack data | Yes | No documented stack payload found |
| Whole-stack or partial-stack merge behavior | Yes | No documented equivalent found |
| Cross-project dependency declaration | Not established by the stack documentation | Yes, through `blocks`; it is not a stack |
| Mature availability guarantee | No; public preview | Yes only on GitLab 19.1 or later |

## Decision notes

- For a tool that must automate stack creation, membership, lifecycle, or webhook handling, use GitHub's stack APIs and treat the public-preview status as a versioning risk.
- For GitLab, model a stack through merge-request source and target branches. Do not treat `blocks` dependencies or merge trains as the stack itself.
- For GitLab Self-Managed, check the instance version before enabling stack UI assumptions. Installations earlier than 19.1 lack the documented native stacked-merge-request feature.

## Evidence limits

This report uses only official GitHub and GitLab documentation and GitHub's official changelog. GitHub describes its feature as public preview, so the API and product behavior can change. GitLab's documentation does not expose a first-class stack API, nor does it document a bulk stack merge operation. The absence claims in this report apply to the reviewed official documentation, not necessarily to unsupported internal or future interfaces.

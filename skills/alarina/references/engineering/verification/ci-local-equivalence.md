# Local proof and CI equivalence

Read during project setup, when CI or its inputs change, or when readiness depends on whether local evidence covers a CI obligation. Reuse a current project-owned mapping; ordinary delivery refreshes only affected rows. The delivery owner selects and accepts proof. The configured runner executes commands; it cannot infer a complete CI contract or attest review.

## Map obligations to executable proof

Inspect the actual workflow bodies, referenced scripts and reusable workflows, job conditions, matrices and prerequisite setup. Trace each relevant obligation to its maintained implementation before copying a CI command. Record the mapping at the existing verification/build owner; a small table or existing runner documentation is enough:

| Obligation | Local proof and prerequisites | CI differences | Disposition |
| --- | --- | --- | --- |
| Named behavior or check and its CI job/step | Exact command/check ID, working directory, runtime/tool versions, dependency lock, services/fixtures and expected evidence | OS/architecture, matrix variants, credentials, generated inputs, caching or provider-only controls that affect the claim | Executed with evidence; available but unexecuted; blocked with missing capability; or genuinely remote-only with named proof owner |

Select obligations from the changed behavior and its consumers, project policy and release boundary. Account for relevant lint/type/build, unit/contract/integration tests, assembled-product journeys, packaging and migration checks; the list is conditional, not a universal suite. Explain a material exclusion. A passing selected subset remains partial, and a passing complete *configured* gate does not prove that configuration contains every relevant obligation.

Prefer a shared project command or check inventory consumed by both local execution and CI. Keep its implementation in one owner. Use pinned dependencies and matching material inputs. A matching command string establishes invocation parity only; record remaining environment differences. Prefer an available, suitable project dev container under the shared [execution-environment choice](../delivery/engineering-contract.md#choose-the-execution-environment). It can close a relevant OS/service gap but does not reproduce every platform, hosted identity, branch protection, signing or live deployment by itself. Do not add an emulator, container service or new dependency merely to reproduce orchestration syntax.

For example, local unit tests do not cover a CI database-integration job just because both commands end in `test`. Reuse the integration runner and isolated database fixture locally if available. If the service is unavailable, retain that obligation as blocked and explain what it leaves unproved. Describe a genuinely hosted smoke or signing check separately; lack of local access alone does not make an otherwise local check remote-only.

## Establish and maintain the local path

During authorized setup or delivery, close an absent local command, fixture, evidence adapter or cleanup path through [project verification](../../../commands/alaga-verify-project.md). A read-only assessment reports the gap and smallest correction without running project commands or writing configuration by implication. Inspect effects and honor existing execution authority before exercising any recipe.

Register real commands through [configuration](../../productivity/environment/configuration.md), including test-count evidence where applicable. Run the required local path against the actual candidate, inspect skipped/zero/stale results and preserve evidence through teardown. `doctor` checks declared prerequisites; it does not discover all omitted CI jobs or prove equivalence. `remote_checks` records obligations; it neither runs them nor turns them into passing evidence.

When the workflow, runner, runtime, dependencies, fixtures, relevant cache keys or acceptance requirement changes, refresh the affected mapping and proof. For generated or cached checks, establish that the intended inputs and candidate reached the consumer; use the delivery method's invalidation proof when material. Avoid storing a permanent green status in the mapping.

Reconcile expectations regularly at the project’s existing engineering-maintenance cadence and before release readiness, as well as after those changes or an escaped CI failure. Compare current product/policy obligations with local checks, actual CI jobs and conditions, supported environment matrices, skipped paths and provider-required checks. Identify missing obligations, stale expectations and redundant checks; keep justified differences explicit. Reuse current evidence for unchanged boundaries and refresh only what drift invalidates. Never weaken an expectation merely to recover green status or assume a configured job is enforced at merge.

Keep the mapping’s owner, last reconciliation evidence and next review trigger with the existing verification/build record. If a maintenance cadence is missing, propose a proportionate project cadence or event trigger during setup/maintenance; do not invent a scheduler or recurring service. A reconciliation can be complete with named blocked proof, but readiness cannot claim that proof passed. Return material drift to its verification/delivery owner and preserve unresolved obligations until they are resolved or explicitly rescoped.

Return local executed coverage, environment differences, omitted/blocked obligations and required remote proof to [local readiness](../delivery/local-readiness.md). Required independent review and adversarial scrutiny retain their own evidence; a receipt cannot substitute for them. CI remains required where project/provider policy requires it, even after adequate local acceptance.

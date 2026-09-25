# Project verification capabilities

Read the [shared engineering contract](../references/alaga/engineering-contract.md) before applying this method.

Use when recurring work needs a reliable way to exercise one project's actual product, or an existing verification skill has drifted. Reuse the project's working commands, tests and harness before proposing another capability. A one-off probe does not require a skill.

Own harness implementation and runtime proof. Reuse an existing project verification specialist when one owns these journeys; use [oro-eniyan](oro-eniyan.md) to author reusable instructions from the verified commands and evidence. The project or host owns material readiness gaps. Creating guidance does not authorize product repairs, installation, deployment or publication.

## Ground the capability

Establish from current project evidence:

- the public surface: API, CLI, library, browser, desktop or mobile;
- the supported build/start command, fixtures, authentication and observable readiness;
- the existing way to drive that surface and observe its effects;
- isolation limits, shared resources and ownership of processes/data; and
- where evidence survives cleanup.

Ask only for consequential choices or unavailable facts. A broken baseline is a named readiness gap, not a reason to invent working commands or silently repair the product.

## Write only the project's useful contract

Preserve its established location and host-native skill packaging. Include exact commands and handles grounded in the project, with only the branches it needs:

| Concern | What the next user or agent must know |
| --- | --- |
| Start and readiness | How to reach a usable instance of the intended build; how to distinguish it from a stale or unrelated process. |
| Drive | Stable public operations or selectors and the setup they require. Short-lived CLIs may need a fresh isolated process per case. |
| Observe | The action and expected result, plus material persisted or external effects. A final screen or HTTP status alone may miss the contract. |
| Recover and clean up | How to reset after a failed drive and remove only owned processes/scratch state. Retain evidence at its named destination. |

Record a small useful set of journeys: entry point, prerequisite, drive command and observable outcome. Reuse existing test or journey identities; add an index only when it makes several maintained recipes easier to find. Do not generate placeholders or an exhaustive feature catalogue.

Prefer the real public path over internal setters or verification-only endpoints. An isolated external substitute may be appropriate; state the boundary it leaves unproved. Confirm what a dry-run actually omits before relying on it to prevent effects.

For recurring integration risks, retain the project-specific commands and observations for the applicable framework invocation, supported old/new consumer or data combination, denied access, or interruption/restart journey. Reuse Alaga’s proof methods; this capability supplies the real build, fixtures and driver rather than copying the general method. Record resource-cost recipes only when a concrete workload and bounded measurement are available.

## Prove the instructions

Within existing runtime and effect authority, follow the authored instructions in an appropriate test environment through startup/readiness, one representative journey, effect inspection and cleanup. Check that evidence remains available afterwards and owned resources are released, including after a failed attempt. Correct the instructions or harness from observed failures and rerun the affected path. Missing runtime access or effect authority leaves an unexecuted recipe with a named verification gap; an authoring request does not itself authorize live effects.

Return the usable capability, exact candidate and executed coverage. An unexecuted recipe is unverified; one passing journey establishes only that journey and the exercised harness lifecycle.

## Maintain against intent and observation

When relevant code or the harness changes, or a verification audit is requested, compare the affected recipes with source and runtime. A full-map audit covers the requested map; ordinary delivery checks only affected journeys. Reconcile missing or obsolete entry points using concrete evidence.

Classify discrepancies before correcting them:

- **Instruction drift:** the intended behavior still works, but the recipe is inaccurate.
- **Harness gap:** the product works, but the available driver cannot reach or observe it.
- **Product regression:** observed behavior violates the accepted contract; return it to [alaga-deliver](alaga-deliver.md) instead of rewriting the expectation.
- **Blocked or unassessed:** a prerequisite or observation is missing; name it without claiming success.

Reuse compatible app states and keep one owner for shared driving. After a surprising failure, establish readiness or reset only the invalidated state before continuing. Re-exercise corrected instructions or harness code; preserve evidence through teardown. Report scope and uncovered paths. Maintenance alone does not require a new report, scheduled sweep or PR.

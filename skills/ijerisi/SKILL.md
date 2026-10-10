---
name: ijerisi
description: Ìjẹ́rìísí. Produces a project-local verification skill and feature map that exercise the real product and retain evidence; creates them, or keeps them true when recipes have drifted. Use when a project needs a reusable driver for its real surfaces.
---

# Ìjẹ́rìísí

**Output:** a project verification skill and feature map that make user journeys repeatable for an agent arriving without this conversation. Reuse project commands and drivers. It does not repair the product or run one-off probes.

**Needs:** a project with a runnable product. Choose **create** for a missing capability or explicit creation request; **maintain** for an existing one. Resolve the target from the request and project; ask only if several plausible targets change the work. Preserve existing capabilities unless replacement is requested. If the product cannot be run or the request is not this job, return to the caller and say what is missing.

## Method

**Workflow** (`asoju`): once a recipe exists, its runs are scripted work: a cheap runner (`cheap-browser` for browser drives, `cheap` otherwise) launches, drives and records, and you judge the evidence.

Change verification assets and exercise only authorized environments and effects. Product repairs, installation, publication and scheduling need their own authority. Missing readiness or effect access is a gap, not permission to invent working commands or bless a defect.

## Create

Establish from current source, project documentation and available runtime evidence:

- the actual public surfaces and which journeys the capability will cover;
- supported build/start commands, fixtures, authentication and readiness;
- an existing way to drive those surfaces and inspect visible and persisted effects;
- isolation of ports, profiles, data and processes, including limits on shared instances; and
- where proof survives teardown.

Write in the project's established skill location, otherwise `.agents/skills/verify-<app>/`. Use a filesystem-safe app name with matching frontmatter. Its `SKILL.md` must contain concrete instructions under these headings:

| Heading | Required contract |
| --- | --- |
| Launch | Exact build/start command, prerequisites, intended build identity, readiness signal and teardown. For short-lived commands, establish the build once and start an isolated process per journey. |
| Doctor | A read-only check that distinguishes a usable intended instance from a stale, unhealthy or unrelated one, including relevant auth and owned resources. |
| Drive | Supported public operations with stable handles, setup and expected outcomes. Use accessible names, command arguments or API routes rather than coordinates when available. |
| Evidence | Record the action, resulting state and material persisted or external effects, with named artifact destinations and the entry point exercised. |
| Cleanup | Release only resources the run owns and reset its fixtures after success or failure. Retain evidence outside removed state; never kill an unrelated process to clear a port. |
| Helpers | Document executable bundled helpers and their invocations, or state that the existing driver needs none. |

Keep generated `SKILL.md` within the host limit, otherwise 8000 bytes, and resources inside its directory. Derive commands, selectors and tool arguments from this project and current driver documentation.

Create `features/README.md` with shared prerequisites, reset conventions and links to 3–5 starting features, or fewer if that is the whole product. Use the [feature template](references/feature-template.md); read the [example](references/example.md) when launch, recipes and proof need clarification. Entries cover sub-features, user entry points, driving, gotchas, observable proof and unexecuted paths. Preserve equivalent existing formats. For recurring integration risks, read [integration journeys](references/integration-journeys.md).

Follow the generated instructions end to end: launch, doctor, drive one mapped feature, inspect its effects, capture evidence and clean up. Verify that the proof still exists and owned resources are released. Correct instructions or owned harness defects from observed failures and rerun the affected journey. Clean failed attempts before another attempt uses their state. Finish when one feature and the lifecycle are proven, or return the exact missing prerequisite or evidence. One successful journey does not certify the rest of the map; unexecuted recipes remain unverified.

## Maintain

Limit edits to the selected verification skill, its map and helpers. Reconcile the README index with feature files and entry points, drive every mapped feature, and classify each discrepancy before changing it: instruction drift (correct the recipe), harness gap (repair the owned harness), or product regression (report it to the caller; keep product changes out of this pass). Re-drive corrections before calling them verified. Full procedure, including delegated readers, driving and recovery rules: [maintain and drive](references/maintain-and-drive.md). Read it also before driving any journey on SIGIDI or recovering a stuck instance.

## Done

Create is done when one feature and the whole lifecycle (launch, doctor, drive, inspect effects, capture evidence, cleanup) are proven, or the exact missing prerequisite is named. Maintain is done when the requested map is fully covered. Unexecuted recipes remain unverified.

## Return

For create, return capability path, tested build/instance, proven feature/lifecycle, evidence and unverified recipes or gaps. Unexecuted capabilities are drafts.

For maintain, return **clean** when the requested map is fully covered with no discrepancies or edits; **changed** when corrections are proven and coverage is complete; **blocked** when required coverage or a product contract remains unresolved. Report partial proven changes even when the overall result is blocked. Include coverage by feature and entry point, source and live evidence, corrections, regressions and unmet prerequisites. A demonstrated inaccessible path is not functioning-feature proof.

Stop at the requested result.

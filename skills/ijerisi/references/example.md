# Illustrative project verification capability

This example describes a fictional task application called Pebble. Commands, selectors, routes and output below illustrate the required relationships; they have not been executed and must not be copied as facts about another project. Derive real instructions from the target's source, driver and observed runs.

## Generated layout

```text
.agents/skills/verify-pebble/
  SKILL.md
  features/
    README.md
    add-task.md
    complete-task.md
    filter-tasks.md
```

A project might already have a working Playwright suite, HTTP driver or CLI. Use that rather than adding a new driver. This imagined project has a browser UI with accessible labels and a read-only API view for inspecting stored state.

## Example generated SKILL.md

The following is an unverified draft showing the six required sections. A real generated capability replaces these fictional details and records proof before declaring it ready.

```markdown
---
name: verify-pebble
description: Exercise Pebble task journeys in an isolated local instance. Use for task creation, completion and filtering proof.
---

# Verify Pebble

Use a disposable test identity. Read the feature index for the required baseline and journey. Preserve proof outside the disposable application state.

## Launch

Build with `npm run build`. Start `npm run start -- --port 4317` with `PEBBLE_DATA_DIR` set to the run's new temporary data directory. Retain the process handle and build revision. The example service exposes `/health`, which returns the revision, data directory and readiness state. A response on the port alone is insufficient; compare those values with this run.

Wait for readiness before driving. If the port belongs to another instance, select an available supported port rather than stop that process. The existing build requires dependencies to be present; missing dependencies are a readiness gap unless installation was separately authorized.

## Doctor

Read `/health` and the current browser identity. Require this run's revision/data directory and its test account. Check the fixture state named by the selected feature. Recheck after a failed action or unexpected result.

## Drive

On SIGIDI, navigate with `preview_*` and use snapshot-provided accessible handles. Open `/tasks`. The task form has textboxes named `Task title` and a button named `Add task`. Select only the task row created by this run. Read feature recipes for the particular transition and reset.

Elsewhere use the project's browser driver with the same public journey and observations. Only one coordinator drives this instance.

## Evidence

Keep action traces, resulting UI snapshots and read-only stored-state responses under a separate run evidence directory. Each artifact identifies the build, feature and entry-point IDs. A displayed task does not establish persistence: reload and inspect the stored task too. Capture the completed state before resetting the fixture.

## Cleanup

Remove this run's task through the supported test-user operation and stop only its retained process handle. Remove its temporary data directory after the process exits. Check the evidence files remain readable. Run this cleanup after failed attempts as well as success; reset a stuck owned browser session before another drive.

## Helpers

This example needs no custom helper. Use the supported commands and host browser driver.
```

A real Doctor might use a build endpoint, process identity and profile instead of `/health`. A real app might not expose stored state over HTTP. Choose a supported public second view or a permitted read-only storage observation; do not add a verification-only endpoint to the product for convenience.

## Example feature index

```markdown
# Pebble journeys

Baseline: this run's healthy build on its recorded port, disposable signed-in account and empty task list. Before each journey, remove only that journey's owned fixture. Preserve evidence outside application state.

Use current browser snapshots for handles. A recorder captures user actions; snapshots and stored-state responses capture outcomes. Keep build/feature/entry-point IDs with the artifacts.

- [Add a task](add-task.md)
- [Complete a task](complete-task.md)
- [Filter tasks](filter-tasks.md)

Initial coverage: recipes are source-backed but unexecuted. Generation must demonstrate at least one feature and the lifecycle. A maintenance audit exercises all listed journeys and reports gaps.
```

## Example feature file: add-task.md

```markdown
# Add a task

The user saves a titled task and finds the same task after reloading.

## Sub-features

- add-valid: a nonempty title creates one pending task.
- add-empty: an empty title does not create a task and shows the required input feedback.

## How a user reaches it

- list-form: open `/tasks` and use the inline task form.
- quick-add: use the `New task` control in the navigation to open the task dialog.

## How to drive it

Prerequisites: Doctor reports this run's build/data directory and test account. No task is titled `Prepare demo`. Restore that state before each creation path.

For list-form:

1. Navigate to `/tasks`. Resolve the `Task title` textbox and `Add task` button from the current snapshot.
2. Submit an empty title. Observe the required input feedback and confirm the task list and stored count have not changed.
3. Fill `Task title` with `Prepare demo`, then activate `Add task`.
4. Observe one pending task row with that title. Wait for completion feedback before inspecting persistence.
5. Reload `/tasks` and confirm the same task remains. Read the permitted stored-state view and confirm one record with the returned identity/title and pending state.
6. Retain the action trace, UI snapshot and stored record in the evidence directory, labeled add-valid/list-form and add-empty/list-form.
7. Remove only the created task and confirm the baseline is restored.

For quick-add, reset the baseline, open `New task` and repeat the empty/valid title checks inside its dialog. Retain separately labeled evidence; list-form proof does not certify the dialog's submission path.

Coverage: unexecuted illustrative recipe. No pass is claimed here.

## Gotchas

- A title already in fixture data can make a failed creation look successful; confirm the new task identity and count.
- A dialog may stay open after a failed request while the process remains healthy. Check Doctor, then reset the owned UI state before retrying.
- Reset task data only after capturing proof. Process teardown must not remove the evidence directory.
```

## The other starting features

`complete-task.md` would use the same four headings. Its sub-features cover the pending-to-completed transition and the supported return to pending. Its entry points are the task-row control and detail view. It begins with one owned pending task, performs each transition through its public control and checks that the state survives reload and matches the stored task identity. UI-only checkbox state is insufficient.

`filter-tasks.md` would cover pending, completed and all-task views, including a deliberately empty matching view. It lists filter buttons and direct supported routes separately. It begins with one owned task in each state, checks the exact visible identities and verifies filtering did not mutate their stored state. A spinner or request failure is not a verified empty result.

## Creation and maintenance results

After running a real generated skill, a creation receipt names the candidate/build, feature and paths actually exercised, visible/persisted observations, artifact locations, released resources and remaining unexecuted entries. This example supplies no such receipt because no Pebble app exists here.

During maintenance, a renamed accessible button while accepted task creation still works is instruction drift. A working dialog that the driver cannot address is a harness gap. A successful-looking save that loses the task after reload violates the accepted persistence contract and is a product regression. Fix the first two in the verification assets and re-drive them. Keep the persistence expectation and report the third rather than weaken the recipe.

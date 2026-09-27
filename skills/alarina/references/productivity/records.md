# Records and working state

This is the location policy for every Alárinà command and workflow. Read it before creating or relocating persistent output. Reuse the active plan, specification or other owned record. A short answer needs no file; a saved record does not automatically become HTML.

## Choose the owner, then resolve the destination

For a new artifact or record, use this precedence:

1. The user's explicit destination for this result.
2. The existing record or an established project/user destination for this kind of information.
3. The configured project `doc_root` for **new human deliverables**.
4. The task's isolated record directory below the user-level Alárinà home; human deliverables go in its `artifacts/` directory.

`doc_root` is a fallback, not permission to move authoritative files. Shared standards, architecture, ADRs, glossaries, runbooks and collaborator-facing documentation remain at their project owners. Private resumable state always uses its record owner or the isolated task directory, even when a project `doc_root` is configured. Return a saved deliverable's actual clickable locator; user storage must remain discoverable to the user.

Resolve paths with the installed utility, substituting the directory containing the loaded `SKILL.md`:

```sh
python3 <alarina-directory>/scripts/alarina.py paths --project <checkout> --task <stable-task-id> --kind artifact --name report.html
python3 <alarina-directory>/scripts/alarina.py paths --project <checkout> --task <stable-task-id> --kind record --name plan.md
```

Use `--destination <exact-path>` for an explicit user destination, or `--established-root <path>` with `--name` for an existing convention discovered from instructions. The resolver cannot infer ownership from prose. It returns the path and its source without creating anything. Invalid configuration is an error; do not silently pick another directory. [Configuration](environment/configuration.md) defines overrides and validation.

## Isolate user storage

The default layout is:

```text
~/.qp/alarina/
  config.json                         personal storage and suggestion preferences
  projects/<project-key>/
    workflows/                        this project's proven reusable recipes
    worktrees/<checkout-key>/tasks/<task-key>/
      plan.md                         only when a plan needs persistence
      artifacts/                      new deliverables without another owner
      checks/<run-id>/                 local check logs and evidence
  workflows/portable/                 explicitly qualified cross-project recipes
```

The resolver derives a project key from the canonical common Git directory (or the real project directory outside Git), a checkout key from the real checkout path, and a task key from the stable task identifier. Readable names include identity hashes. Same-named repositories, branches and worktrees cannot share task state by accident. Changing `state_root` changes only the base; project/worktree/task separation still applies. Never flatten records into a shared user directory.

Use the same task identifier on resumption. Keep the actual workspace, candidate, decisive evidence locators, unresolved obligations and next action in the current record when needed. Moving a checkout or handing work to another checkout requires reconciling the existing record and its consumers; a newly computed path is not authority to abandon previous proof.

Create directories lazily with private access where supported. Store secrets in the existing credential manager, not records, command arguments or logs. Read-only requests remain read-only even when the resolver suggests a path. Shared knowledge must not exist solely in private state.

## Retain and clean by purpose

Use temporary storage for regenerable scratch. Before cleanup, retain evidence still needed by a continuing task or delivered claim at the resolved owner and update its links. A local check run owns only its run directory and processes; a workflow owns only resources it created or explicitly acquired.

Keep reusable paths in the current project's workflow library under [learned workflows](learned-workflows.md). Promote a recipe to the portable library only after checking its assumptions and removing project-specific data. Durable project policy remains with the project.

At completion or a requested cleanup, identify owned scratch, retained evidence and unresolved state. Remove only material covered by cleanup authority, preserve active consumers, and report a failed cleanup. No age-based deletion or broad history sweep is implied. Existing records are inputs with their own owners; this policy does not authorize a bulk move or deletion.

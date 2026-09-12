# Set up the agent in Codex

The [operating contract](agent.md) makes Codex use relevant installed skills and carry work through completion. You control the model and reasoning. Compound Engineering is not a dependency.

Open Codex in the project where you want this behavior, then copy this prompt. It authorizes project-local setup. Edit the scope explicitly if you want personal setup across projects.

```text
Set up the QP agent experience for Codex in my current project.

Source: https://github.com/quantipixels/skills
Read docs/codex-setup.md and docs/agent.md from that repository and follow
the setup procedure. Use an existing checkout when available, otherwise
retrieve the source and record the revision used.

Install or reconcile the relevant QP skills and apply the operating
contract to this project's Codex instructions. Preserve my existing
instructions, edits, installation manager, model, reasoning, permissions,
and unrelated configuration. This authorizes the project-local setup;
do not change global settings or install Compound Engineering.

Complete and verify the setup. Report the changed files, source revision,
skill readiness, recovery path, and any fresh-session check still needed.
```

## Procedure for Codex

1. Establish the target project separately from the source checkout. Read applicable project instructions and inspect existing skill installation and Codex instruction surfaces within the authorized scope. Use the source checkout's current revision and preserve uncommitted work; do not switch branches or update it implicitly. When fetching remote files, use one resolved revision for the contract and setup procedure. Record local modifications if they affect the supplied instructions.

2. Use `irinse` for skill readiness and host-instruction setup, reading it from the source if not installed. Use `oro-fun-sigidi` when reconciling the contract with existing instructions. The copied prompt already selects the complete operating contract and authorizes its project-local application; do not reopen optional-instruction selection. Inspect current host support and installation options through installed help or official documentation when needed.

3. Reuse the existing installation manager. Make the repository's skills available in the authorized scope through its supported discovery mechanism, preserving any deliberately selective installation. If that leaves a capability unavailable, report it rather than silently expanding the user's selection. With no existing installation, choose a supported project-local skill installation from the repository's install guidance. Do not substitute a global-only installer; if no project-local path is supported, complete the independent instruction work and report the readiness gap. Skills remain independently usable; no CE installation, model configuration, role fleet, or custom runtime is required.

4. Prepare the exact instruction change. Apply the body of `docs/agent.md` under a normal heading in the target project's applicable Codex `AGENTS.md`, reconciling equivalent existing guidance and preserving user-specific constraints. Keep the installed contract self-contained; do not leave a dependency on a temporary checkout or a remote URL that must be fetched every turn. Do not replace Codex's built-in instructions or create a custom subagent merely to configure the main session. If the target instruction file is shared by other hosts and Codex-only behavior matters, resolve a supported Codex-specific surface before applying it.

5. Show the concrete target and changes, back up existing instruction files using the host-instruction procedure, refresh before writing, and apply within the authorization already given. An existing equivalent setup is a no-op. On subsequent setup, compare source, installed instructions, and user edits; reconcile rather than append a duplicate or overwrite user changes. Record the source revision in the setup report.

6. Read back the result. Check local links, preserved user settings, applicable instruction precedence, and skill discovery where exposed. Distinguish installed files from the active session's skill inventory. A fresh session may be required before discovery and instruction loading can be verified; give the exact remaining check instead of claiming activation from file inspection. A harmless read-only task can check loading and selection in the fresh session. Do not launch implementation, publication, or other consequential work as a setup test.

7. Report the installed instruction location, skill source and revision, installation method, checks actually performed, remaining readiness gaps, and backup/recovery path. For reversal, remove only the applied contract or restore the backup after reconciling later user edits; use the existing installation manager for skill removal if requested.

## Verification status

The contract and setup prompt are an initial candidate. Link and package checks establish structural integrity; they do not prove installation, fresh-session loading, skill selection, delegation, or completion behavior. Those runtime checks must be reported from an actual setup and representative use.

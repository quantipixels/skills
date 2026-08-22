# Operate one companion tool

Load this reference only when the selected tool must be readied, installed, configured, authenticated, integrated, used, upgraded, removed, or rolled back. The caller keeps the bounded question, candidate identity, selected tool, fallback, and result ownership from `SKILL.md`.

## Establish readiness

Inspect the selected tool's presence, version, platform support, prerequisites, relevant configuration, integration state, and one proportionate usability signal. Command presence alone does not prove readiness. Do not read or report secret values.

Classify it as:

- `Ready` — present, configured for the intended use, and verified;
- `Needs setup` — present but required configuration or verification is missing or stale;
- `Missing` — unavailable;
- `Unsupported` — incompatible with the required platform or integration.

If a useful tool is missing or not ready, explain its distinct benefit and the safe fallback already identified by the owning request. Ask before installation or configuration. A request to use a tool does not by itself authorize global installation, persistent services, broad downloads, credential changes, or project-file mutation.

Before a mutation, state the exact tool and version choice, global or project scope, official source, platform support, download and network effects, privileges, configuration targets, credential needs, persistent state, and rollback or uninstall path. Never request secrets in chat. When authentication is required, direct the user to a supported non-chat login, environment, keychain, or provider mechanism and verify only presence or authenticated state without reading or reporting the value. Apply only the accepted action and scope.

## Use the tool safely

Constrain paths, permissions, output size, network access, persistent state, and mutations. Prefer read-only operations. Ask separately before a command that changes source, configuration, caches, services, dependencies, or external state.

Pin evidence to the candidate, tool version, command or operation, scope, exclusions, errors, and timestamp when freshness matters. Treat static analysis, metrics, IDE indexes, and search output as leads. Corroborate consequential claims with source, tests, compiler, runtime, configuration, or history.

If the candidate, relevant configuration, ignore rules, tool version, or analyzed files change, mark the evidence stale and rerun the affected operation.

## Verify operation state

After setup, upgrade, integration, removal, or rollback, verify the intended state from the target environment. Do not claim success from an installer exit code alone. If verification fails, stop dependent work and preserve a safe fallback.

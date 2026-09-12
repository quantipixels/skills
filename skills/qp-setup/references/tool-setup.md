# Tool setup

Use when a selected engineering or agent tool must be made ready, changed, or removed. The caller/user owns why the tool is wanted; this skill owns the setup operation and resulting readiness state.

## Pin the requested state

Establish the exact tool, target environment, current state, desired state, installation/configuration scope, required integration or authentication, supported fallback, and rollback/uninstall path.

Use the installed tool's help and current official documentation to resolve volatile installation, upgrade, configuration, authentication, and platform details. Do not copy a long-lived command catalogue into this skill. When `irinse` supplied the tool choice, preserve that selection and any usage-specific readiness requirement; do not re-run tool selection.

Classify the starting state as `Ready | Needs setup | Missing | Unsupported` for the intended use. Command presence alone does not prove readiness.

## Bound mutation and authority

A request to use a tool does not automatically authorize:

- global or privileged installation;
- persistent services or startup changes;
- downloads, caches, or model/rule packs with material cost;
- credential creation, storage, or account changes;
- repository configuration, CI, IDE/MCP, or editor integration;
- trust/permission changes;
- external disclosure or cloud-connected operation; or
- destructive removal of unrelated state.

Make material effects and scope clear before mutation and obtain the required authority. Never request secrets in chat; use the tool/platform's supported authentication mechanism and verify authenticated state without printing credential values.

Prefer the smallest reversible setup that satisfies the selected use. Reuse existing project/package-manager/platform conventions. Do not install a second manager/runtime or duplicate an existing integration merely for convenience.

## Apply and verify

Capture enough pre-state to support scoped rollback. Apply only the approved installation/configuration change. Preserve unrelated files, settings, services, credentials, and project state.

After setup, upgrade, integration, removal, or rollback, verify the intended state from the real target environment. Use one proportionate readiness signal tied to the selected use: supported version/interface, configuration parse, authenticated status, service/extension state, project visibility, or a harmless bounded command as appropriate.

If verification fails, stop dependent work and return the safe fallback or recovery action. Do not report `Ready` from installation success alone.

## Return

Return:

- tool and target environment;
- previous and resulting readiness state;
- installation/configuration scope;
- material mutations and external effects;
- verification evidence;
- rollback/uninstall path; and
- unresolved capability or authority gaps.

Usage strategy and interpretation of tool evidence remain with `irinse` or the consuming engineering skill.

---
name: irinse
description: Select, install, configure, integrate, use, verify, upgrade, or remove one companion engineering tool. Use when a coding workflow needs bounded evidence from tldr-code, ast-grep, Semgrep, IntelliJ MCP, or another named tool, or when a useful required tool is missing; exclude architecture, implementation, security, maintainability, and review verdicts.
---

# Irinṣẹ́

Own one companion tool from need through safe readiness and bounded evidence. Let the consuming outcome skill retain its judgment and verdict.

## 1. Bound the need

Identify the question the tool should answer, the candidate identity, required evidence, acceptable fallback, mutation authority, and freshness boundary. Pin a commit or tree when it completely identifies the analyzed state. For staged, unstaged, or supplied changes, add a fixed snapshot or content digest that includes every analyzed uncommitted path; HEAD alone is not that candidate. Prefer direct source reading and existing safe tools when they answer the question proportionately.

Select the smallest useful tool. Do not recommend every missing tool or route ordinary shell search through Irinṣẹ. Load only the selected reference:

- [tldr-code](references/tldr-code.md) for compact structural, flow, impact, quality, or security leads;
- [ast-grep](references/ast-grep.md) for syntax-aware search or structural rewriting;
- [Semgrep](references/semgrep.md) for repeatable bug, security, or architecture rules; or
- [IntelliJ MCP](references/intellij-mcp.md) for IDE-backed navigation, code insight, run configurations, and debugging.

For another named tool, research its current official documentation and apply the same readiness and authority rules. Stable references describe capabilities and boundaries; verify volatile commands and supported versions at execution time.

## 2. Establish readiness

Inspect the selected tool's presence, version, platform support, prerequisites, relevant configuration, integration state, and one proportionate usability signal. Command presence alone does not prove readiness. Do not read or report secret values.

Classify it as:

- `Ready` — present, configured for the intended use, and verified;
- `Needs setup` — present but required configuration or verification is missing or stale;
- `Missing` — unavailable;
- `Unsupported` — incompatible with the required platform or integration.

If a useful tool is missing or not ready, explain its distinct benefit and a safe fallback. Ask before installation or configuration. A request to use a tool does not by itself authorize global installation, persistent services, broad downloads, credential changes, or project-file mutation.

Before a mutation, state the exact tool and version choice, global or project scope, official source, platform support, download and network effects, privileges, configuration targets, credential needs, persistent state, and rollback or uninstall path. Never request secrets in chat. When authentication is required, direct the user to a supported non-chat login, environment, keychain, or provider mechanism and verify only presence or authenticated state without reading or reporting the value. Apply only the accepted action and scope.

## 3. Use the tool safely

Constrain paths, permissions, output size, network access, persistent state, and mutations. Prefer read-only operations. Ask separately before a command that changes source, configuration, caches, services, dependencies, or external state.

Pin evidence to the candidate, tool version, command or operation, scope, exclusions, errors, and timestamp when freshness matters. Treat static analysis, metrics, IDE indexes, and search output as leads. Corroborate consequential claims with source, tests, compiler, runtime, configuration, or history.

If the candidate, relevant configuration, ignore rules, tool version, or analyzed files change, mark the evidence stale and rerun the affected operation.

## 4. Verify and return

After setup, upgrade, integration, removal, or rollback, verify the intended state from the target environment. Do not claim success from an installer exit code alone. If verification fails, stop dependent work and preserve a safe fallback.

Return:

```text
Irinse result
Need: <bounded question>
Candidate: <exact identity>
Tool: <name and version>
State: Ready | Needs setup | Missing | Unsupported
Authority: <approved scope and mutations>
Operation: <readiness, setup, use, removal, or rollback>
Evidence: <observations with provenance>
Corroboration: <source, test, compiler, runtime, configuration, or history>
Coverage limits: <omissions, errors, and heuristic limits>
Freshness: CURRENT | STALE
```

Do not make architecture, implementation, security, maintainability, or review verdicts. Return the evidence to the owning workflow.

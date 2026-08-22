---
name: irinse
description: Select, install, configure, integrate, use, verify, upgrade, or remove one companion engineering tool. Use when a coding workflow needs bounded evidence from tldr-code, ast-grep, Semgrep, IntelliJ MCP, or another named tool, or when a useful required tool is missing; exclude architecture, implementation, security, maintainability, and review verdicts.
---

# Irinṣẹ́

Own one companion tool from need through safe readiness and bounded evidence. Let the consuming outcome skill retain its judgment and verdict.

## 1. Bound the need and select the tool

Identify the question the tool should answer, the candidate identity, required evidence, acceptable fallback, mutation authority, and freshness boundary. Pin a commit or tree when it completely identifies the analyzed state. For staged, unstaged, or supplied changes, add a fixed snapshot or content digest that includes every analyzed uncommitted path; HEAD alone is not that candidate. Prefer direct source reading and existing safe tools when they answer the question proportionately.

Select the smallest useful tool. Do not recommend every missing tool or route ordinary shell search through `irinse`. Load only the selected reference:

- [tldr-code](references/tldr-code.md) for compact structural, flow, impact, quality, or security leads;
- [ast-grep](references/ast-grep.md) for syntax-aware search or structural rewriting;
- [Semgrep](references/semgrep.md) for repeatable bug, security, or architecture rules; or
- [IntelliJ MCP](references/intellij-mcp.md) for IDE-backed navigation, code insight, run configurations, and debugging.

For another named tool, research its current official documentation. Stable references describe capabilities and boundaries; verify volatile commands and supported versions at execution time.

If the request needs only tool selection, return the selected tool, its distinct benefit, the bounded question it should answer, the safe fallback, and any readiness uncertainty. Do not load setup or mutation procedure merely to recommend a tool.

## 2. Operate when needed

When the selected tool must be readied, installed, configured, authenticated, integrated, used, upgraded, removed, or rolled back, read [operate.md](references/operate.md) and apply it against the same candidate, authority, fallback, and freshness boundary. Do not perform a mutating operation without its required permission.

## 3. Return the evidence

Return:

```text
Irinṣẹ result
Need: <bounded question>
Candidate: <exact identity>
Tool: <name and version, or selected tool with version unresolved>
State: Ready | Needs setup | Missing | Unsupported | Not checked
Authority: <approved scope and mutations>
Operation: <selection, readiness, setup, use, removal, or rollback>
Evidence: <observations with provenance>
Corroboration: <source, test, compiler, runtime, configuration, or history>
Coverage limits: <omissions, errors, and heuristic limits>
Freshness: CURRENT | STALE
```

Do not make architecture, implementation, security, maintainability, or review verdicts. Return the evidence to the owning workflow.

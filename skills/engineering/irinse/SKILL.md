---
name: irinse
description: Select, install, configure, integrate, use, verify, upgrade, or remove one companion engineering tool. Use when a coding workflow needs bounded evidence from tldr-code, ast-grep, Semgrep, IntelliJ MCP, complexity/static-analysis tooling, or another named tool, or when a useful required tool is missing; exclude architecture, implementation, security, maintainability, and review verdicts.
---

# Irinṣẹ́

Own one companion tool from need through safe readiness and bounded evidence. Let the consuming outcome skill retain semantic judgment and verdict.

## 1. Bound the need and select the tool

Identify the exact question, candidate identity, required evidence, acceptable fallback, mutation authority, and freshness boundary. Pin a commit/tree when it fully identifies the analyzed state; for uncommitted work, use a fixed snapshot/content digest that covers every analyzed path.

Prefer direct source reading and existing project-native tooling when they answer the question proportionately. Do not recommend every missing tool or route ordinary shell search through Irinṣẹ́.

Load only the selected reference:

- [tldr-code](references/tldr-code.md) — compact structural/flow/impact/quality/security leads;
- [ast-grep](references/ast-grep.md) — syntax-aware search or structural rewriting;
- [Semgrep](references/semgrep.md) — repeatable bug/security/architecture rules;
- [IntelliJ MCP](references/intellij-mcp.md) — IDE-backed navigation, code insight, run configuration, debugging;
- [complexity evidence](references/complexity-evidence.md) — cyclomatic/cognitive/nesting/state-space/hotspot evidence from project-native analyzers.

For another named tool, research current official documentation. Stable references describe capabilities/boundaries; verify volatile commands and supported versions at execution time.

If only tool selection is requested, return selected tool, distinct benefit, bounded question, safe fallback, and readiness uncertainty. Do not load setup/mutation procedure merely to recommend it.

## 2. Operate when needed

When the selected tool must be installed/configured/authenticated/integrated/used/upgraded/removed/rolled back, read `references/operate.md` and apply it against the same candidate/authority/fallback/freshness boundary. Do not mutate without required permission.

Prefer repository-configured rules/plugins over global ad-hoc settings. A new persistent rule/configuration change belongs to the tool/repository owner and needs its own authority; a one-off read-only measurement does not authorize it.

## 3. Return evidence, not conclusions

Return:

```text
Irinṣẹ result
Need: <bounded question>
Candidate: <exact identity>
Tool: <name/version/config identity, or unresolved>
State: Ready | Needs setup | Missing | Unsupported | Not checked
Authority: <approved scope/mutations>
Operation: <selection/readiness/setup/use/removal/rollback>
Evidence: <observations with provenance>
Corroboration: <source/test/compiler/runtime/config/history>
Coverage limits: <omissions, heuristics, config/platform limits>
Freshness: CURRENT | STALE
```

Complexity/coverage/security scores are measurements, not maintainability/defect verdicts. `pare` interprets simplification/complexity, `atunwo` defects/proof gaps, `solution-architect` architecture, and `alaga` implementation/proof.

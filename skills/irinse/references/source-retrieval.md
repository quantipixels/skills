# Source retrieval

Choose the representation required by the question and retrieve the smallest coherent source that preserves its governing contract.

| Question | Capability | Non-obvious limit |
| --- | --- | --- |
| Path, literal, identifier or prose | Native search such as rg | Ignored, hidden, binary and unsearched paths limit negative evidence. |
| Exact document or implementation contract | Complete relevant section/function/file | A keyword hit can omit governing exceptions. |
| Syntactic shape | [ast-grep](https://ast-grep.github.io/guide/pattern-syntax.html) | AST shape does not resolve receiver type, overload or runtime dispatch. |
| Declaration, overload or implementation identity | Available IDE/LSP; [IntelliJ MCP](https://www.jetbrains.com/help/idea/mcp-server.html) when exposed | Confirm actual MCP schemas, project scope and index freshness; unresolved names remain ambiguous. |
| Repository map or flow lead | Available outline or [tldr-code](https://github.com/parcadei/tldr-code) | Maps are heuristic/selective and do not provide complete type, dispatch or flow inference. |
| Repeatable bug/security/architecture rule | [Semgrep](https://semgrep.dev/docs/) | Confirm engine/language/dataflow and path coverage; findings remain leads. |

These are alternatives, not an escalation ladder. For large sources, locate the region then read coherent context. Use format-aware parsers for structured records and rendered inspection when layout carries meaning. Split reads that would truncate.

Calibrate structural/rule queries against a known positive and legitimate nearby negative. A failed query, parser/index error, unsupported language, excluded path or truncated result is not evidence of absence. Semgrep suppression is not a fix; cloud/registry effects retain their normal authority.

For an authorized rewrite, preview exact matches and diff, then return semantic proof to the consuming owner. Syntax success does not prove behavior preservation. Source-changing fixes, tool installation, model downloads, daemon lifecycle and MCP configuration are mutations; verify tldr-code project confinement before preferring its MCP surface.

Keep decisive path/symbol locators and surrounding source. Refresh affected locations after edits. Current official docs own volatile interfaces and rule syntax; summaries, maps and matches guide inspection but do not replace source or prove runtime behavior.

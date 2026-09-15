# Source retrieval

Use when ordinary reading/search is noisy, incomplete or mismatched to the question. Retrieve the smallest coherent source that can answer it; reducing output must preserve the governing contract and decisive exceptions.

| Question | Useful capability |
| --- | --- |
| Where is a path, literal, identifier spelling or prose passage? | Native file/text search or `rg`; scope paths before requesting matching content. |
| What does this known document or implementation actually require? | Read the relevant complete section, function or short file. `cat`, `sed` and native readers are appropriate; keyword hits alone can omit governing instructions. |
| Which code has this syntactic shape despite layout differences? | [ast-grep](ast-grep.md) for pattern construction and interpretation. |
| Which declaration, overload or implementation does this reference identify? | Available IDE/LSP symbol navigation; use [IntelliJ MCP](intellij-mcp.md) for that integration. Text and AST matches are candidates, not resolved symbol identities. |
| How is unfamiliar code organised or connected? | An available outline/repository map or [tldr-code](tldr-code.md), followed by the relevant source. A selected map can omit important code. |
| Does this repeatable bug or security rule match? | [Semgrep](semgrep.md) with an appropriate scoped rule; findings still need engineering judgment. |

These are alternatives, not an escalation checklist. Use the available capability that answers the question with the least total discovery, setup and reading cost. A missing optional tool does not block an adequate native fallback; keep any resulting evidence limit explicit.

For large files, find the relevant region before reading its coherent context. For structured data, query fields through a format-aware parser rather than treating text matches as records. For rendered documents, use format-aware extraction or inspection when layout carries meaning. Split independent reads when their combined output would truncate; after truncation, retrieve the missing relevant portion instead of repeating the same dump. Reuse still-current source already read.

Before concluding that something is absent, check the actual searched paths, ignore rules, language/parser support, index freshness and result limits as applicable. `rg` normally excludes ignored, hidden and binary files; expand only the relevant scope. A failed query, unsupported parser or truncated response is not a clean negative result.

Keep decisive path/symbol locators and the surrounding source needed to verify the finding. Refresh affected locations after edits. Summaries and search matches guide inspection; they do not replace the source or prove runtime behaviour.

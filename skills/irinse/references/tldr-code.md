# tldr-code

Official source: [parcadei/tldr-code](https://github.com/parcadei/tldr-code)

Use tldr-code for compact static-analysis leads about AST structure, imports, call and data flow, impact, search, quality, security, and contracts. Prefer the CLI until the installed MCP server's project-root confinement is verified.

Treat every result as heuristic evidence. The analyzer does not provide complete type inference, method or interface resolution, dynamic dispatch, or complex type flow. Record language, version, analyzed paths, exclusions, parser errors, and omitted files. Corroborate consequential claims with source, tests, compiler, runtime, configuration, or history.

Do not silently run operations that mutate or persist state, including `warm`, `doctor --install`, `fix apply`, `fix check`, daemon lifecycle changes, semantic model downloads, or broad cache creation. Semantic support can download a substantial model and needs explicit approval. Constrain MCP filesystem permissions and verify the configured repository root.

Pin results to the exact project candidate and tool version. Invalidate them when relevant files, ignore rules, language configuration, caches, or the tool version changes.

tldr-code is AGPL-3.0. Invoke an independently installed tool; do not vendor or redistribute its source or binaries without a licensing review.

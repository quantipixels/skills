# ast-grep

Official source: [ast-grep documentation](https://ast-grep.github.io/)

Use ast-grep for syntax-aware search and repeatable structural rewrites. Verify current installation and language support from official documentation.

## Operational anchor

When the CLI is already available, use `ast-grep --help` for the installed interface. A representative narrow read-only search is:

```bash
ast-grep run --pattern '<pattern>' <path>
```

Use current command help/documentation when the pattern needs an explicit language, selector, rule file, or other branch-specific option. Do not expand this reference into a flag catalogue.

Start with a narrow read-only search and inspect representative matches. Treat a rewrite, rule test update, or project configuration change as a separate mutation requiring authority. Limit paths and review the complete diff; syntax matching does not prove semantic equivalence.

Return the exact pattern or rule, language, paths, match count, exclusions, parse errors, candidate identity, and verification used after any rewrite.

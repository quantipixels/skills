# ast-grep

Official source: [ast-grep documentation](https://ast-grep.github.io/)

Use ast-grep for syntax-aware search and repeatable structural rewrites.

## Operational anchor

When the CLI is already available, use `ast-grep --help` for the installed interface. A representative narrow read-only search is:

```bash
ast-grep run --pattern '<pattern>' <path>
```

Use current command help/documentation when the pattern needs an explicit language, selector, rule file, or other branch-specific option. Do not expand this reference into a flag catalogue.

Start with a narrow read-only search and inspect representative matches. A rewrite or rule change mutates the consuming project, so keep its authority and proof with that delivery workflow. Limit paths and review the complete diff; syntax matching does not prove semantic equivalence.

If ast-grep is missing or needs installation, shell integration, project configuration, or upgrade before the selected use, hand that readiness requirement to `qp-setup` rather than embedding setup procedure here.

Return the exact pattern or rule, language, paths, match count, exclusions, parse errors, candidate identity, and verification used after any rewrite.

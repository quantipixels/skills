# ast-grep

Official source: [ast-grep documentation](https://ast-grep.github.io/)

Use ast-grep for syntax-aware search and repeatable structural rewrites.

## Operational anchor

When the CLI is already available, use `ast-grep --help` for the installed interface. A representative narrow read-only search is:

```bash
ast-grep run --pattern '<pattern>' <path>
```

Use current command help/documentation when the pattern needs an explicit language, selector, rule file, or other branch-specific option. Do not expand this reference into a flag catalogue.

If ast-grep is missing or needs installation, shell integration, project configuration, or upgrade before the selected use, use [tool setup](tool-setup.md) rather than embedding setup procedure here.

Return the useful matches or rewrite result, with the pattern, scope, limits, and verification when needed to interpret or reuse it.

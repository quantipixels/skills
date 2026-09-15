# ast-grep

Official source: [pattern syntax](https://ast-grep.github.io/guide/pattern-syntax.html) and [rule composition](https://ast-grep.github.io/guide/rule-config.html).

Use ast-grep when the question depends on code shape: calls across line breaks, argument structure, annotations, or enclosing constructs. Literal names and prose usually need only text search. AST matches do not resolve receiver types, overloads or runtime dispatch.

## Operational anchor

Start with a representative known instance and the actual language. For example, a read-only Java call-shape search is:

```bash
ast-grep run --lang java --pattern '$RECEIVER.refund($$$ARGS)' src/
```

`$RECEIVER` matches one syntax node; `$$$ARGS` matches zero or more. Keep shell quoting intact. This finds a shape, not calls to one particular service's method.

For a nontrivial query, confirm it finds the known instance and rejects a nearby look-alike before broadening scope. If it misses, inspect the parsed pattern/target: incomplete syntax may need a contextual pattern and selector, while containment needs a relational rule. Add one constraint at a time rather than treating a broken query as evidence of absence. Use the installed interface and official documentation for the selected rule features.

For an authorized rewrite, inspect the matched scope and proposed diff before applying broadly; verify affected behaviour through the consuming engineering owner. A successful syntax rewrite is not a semantics-preservation proof.

If ast-grep is missing or needs installation, shell integration, project configuration, or upgrade before the selected use, use [tool setup](tool-setup.md) rather than embedding setup procedure here.

Return the useful matches or rewrite result, with the pattern, scope, limits, and verification when needed to interpret or reuse it.

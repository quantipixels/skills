# Semgrep

Official source: [Semgrep documentation](https://semgrep.dev/docs/)

Use Semgrep for repeatable bug, security, and architecture rules. Treat its findings as leads, not review or security verdicts.

Prefer it when a reusable rule or supported dataflow analysis answers the question; a one-off code shape may need only ast-grep. Check the selected engine's language and analysis support rather than assuming all modes provide cross-file or type-aware results.

## Operational anchor

When Semgrep is already available, use `semgrep --help` or `semgrep scan --help` to confirm the installed interface. For a repository-owned local rule/config, a representative bounded read-only scan is:

```bash
semgrep scan --config <local-rule.yml> <path>
```

For a new or changed rule, exercise a representative positive and a nearby legitimate negative. Inspect matches in context and distinguish no findings from excluded paths, parse failures, unsupported analysis or an incomplete run. Keep suppression and rule changes separate from evidence that the underlying defect is fixed.

Use the repository's existing Semgrep configuration when present. Treat registry/`auto` rules, cloud-connected scans, authentication, supported languages, and other network-backed modes as current Semgrep behavior to verify before use rather than package defaults.

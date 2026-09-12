# Semgrep

Official source: [Semgrep documentation](https://semgrep.dev/docs/)

Use Semgrep for repeatable bug, security, and architecture rules. Treat its findings as leads, not review or security verdicts.

## Operational anchor

When Semgrep is already available, use `semgrep --help` or `semgrep scan --help` to confirm the installed interface. For a repository-owned local rule/config, a representative bounded read-only scan is:

```bash
semgrep scan --config <local-rule.yml> <path>
```

Use the repository's existing Semgrep configuration when present. Treat registry/`auto` rules, cloud-connected scans, authentication, supported languages, and other network-backed modes as current Semgrep behavior to verify before use rather than package defaults.

Prefer narrow local scans with explicit rules and paths. Installation, authentication, downloaded rule packs, cloud integration, and adding or changing CI/project configuration belong to the setup skill when required for the selected use. Source-changing fixes remain with the consuming delivery workflow. Do not upload code-derived data or weaken project rules merely to make the tool usable.

Return tool and rule versions, candidate identity, paths, exclusions, parse errors, findings, suppressions, network effects, and corroboration limits.

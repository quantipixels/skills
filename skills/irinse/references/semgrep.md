# Semgrep

Official source: [Semgrep documentation](https://semgrep.dev/docs/)

Use Semgrep for repeatable bug, security, and architecture rules. Verify the current CLI, supported language, selected rules, authentication requirements, and local-versus-cloud behavior from official documentation.

## Operational anchor

When Semgrep is already available, use `semgrep --help` or `semgrep scan --help` to confirm the installed interface. For a repository-owned local rule/config, a representative bounded read-only scan is:

```bash
semgrep scan --config <local-rule.yml> <path>
```

Use the repository's existing Semgrep configuration when present. Treat registry/`auto` rules, cloud-connected scans, authentication, and other network-backed modes as current Semgrep behavior to verify before use rather than QP defaults.

Prefer narrow local scans with explicit rules and paths. Ask before downloading rule packs, signing in, uploading results or code-derived data, changing project configuration, adding CI, or applying fixes. A finding is a lead, not a security or review verdict; corroborate its data and control flow against the current source and tests.

Return tool and rule versions, candidate identity, paths, exclusions, parse errors, findings, suppressions, network effects, and corroboration limits.

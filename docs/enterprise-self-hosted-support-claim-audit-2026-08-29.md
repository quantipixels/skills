# Enterprise and self-hosted support claim audit

Date: 2026-08-29

## Question

Do the current skill contracts overstate support for GitHub Enterprise, GitLab Self-Managed or Dedicated, and self-operated private-access infrastructure?

## Verdict

`PARTIAL`, with one corrected source defect.

The provider skills contain useful custom-host safety rules. Those rules can establish trust, credential isolation, and exact command routing. They do not prove that every target server version, tier, repository policy, permission set, or API surface can complete the skill outcome.

The source previously overstated exact-host GitLab publication in `seda-pr`. Its prose required `--hostname`, but the current `glab mr create` and `glab mr update` commands do not expose that flag. The command examples also used a bare project path, so a write could select the checkout or configured default host. The corrected contract sets the confirmed `GITLAB_HOST` inline, passes the canonical full project URL to `--repo`, and uses `glab api --hostname` for structured operations and readback.

Fihan is Experimental and explicit-only. Its Tailscale path is tailnet-only. Its Tailcat path is an encrypted bearer-token capability, not named-reader authorization. The public description now states that distinction.

## Claim assessment

| Claim | Result | Evidence boundary |
| --- | --- | --- |
| GitHub CLI can target GitHub Enterprise Server | `SUPPORTED` as a product capability | GitHub CLI documents `GH_HOST` and the enterprise token variables. GitHub publishes GitHub CLI guidance for Enterprise Server. This does not prove every QP read/write scenario. |
| GitLab CLI can target self-managed GitLab | `SUPPORTED` as a product capability | GitLab documents self-managed authentication, `GITLAB_HOST`, full repository URLs, and `glab api --hostname`. Some commands require newer server capabilities. |
| The QP provider skills are verified on enterprise/self-managed hosts | `UNPROVED` | No authenticated GHES, GitLab Self-Managed, GitLab Dedicated, or two-host isolation scenario was run. |
| Custom-host commands are fail-closed when a required capability is missing | `SUPPORTED` after the correction | Àtúnwò, Ṣe Triage, Sẹ̀dá PR, and Wọ́ PR now separate routing safety from compatibility and require an exact-host capability gate. |
| Fihan provides private access through Tailscale Serve | `SUPPORTED` only for the documented tailnet boundary | Tailscale describes Serve as sharing a local service within a tailnet. Access still depends on the current tailnet policy; Serve adds no separate application login. |
| Fihan provides named-reader privacy through Tailcat | `UNSUPPORTED` | The selected Tailcat SOCKS path uses possession of the connection token as the access capability. The contract now calls this an encrypted bearer-token route. |
| Fihan supports a self-operated DERP relay | `UNPROVED` as a Fihan outcome | Tailcat documents bring-your-own DERP. Fihan neither provisions nor validates one and now treats it as unavailable unless separately ready and proved. |

## Wording boundary

Use this distinction in public and agent-facing claims:

> Custom-host rules establish trust, credential isolation, and command routing. They do not prove target-version, tier, policy, permission, or API compatibility. Verify the required capabilities on the exact host before claiming the skill outcome is available.

Do not label the provider skills as having “verified enterprise support” until live acceptance covers the relevant product surfaces.

Do not describe Tailcat as named-reader private access. Describe it as an encrypted bearer-token route with explicit receiver, relay-metadata, and stability limits.

## Proof required for verified compatibility

- Run one complete current GitHub Enterprise Server scenario: canonical read, pagination, review threads, required checks, one separately authorized write, and exact readback.
- If GitHub Enterprise Cloud data residency is in scope, run the same host-routing proof against the exact `ghe.com` tenant.
- Run one GitLab Self-Managed scenario on a supported version: issue notes, MR diffs/discussions/approvals, job state, create/update/draft-ready transitions, and exact readback.
- Configure two GitLab hosts and prove that every Sẹ̀dá PR write remains on the confirmed host.
- Repeat Fihan's bounded transport proof when its Tailscale contract or pinned Tailcat candidate changes. On 2026-08-29, the current candidate passed one existing tailnet-only Serve retrieval and one temporary pinned Tailcat sender/receiver retrieval against identical content. Both paths returned the expected SHA-256 identity, rejected an unrelated path, left Tailscale state unchanged, and completed cleanup. This does not prove a self-operated DERP relay or named-reader Tailcat authorization.

## Sources

- [GitHub CLI environment variables](https://cli.github.com/manual/gh_help_environment), retrieved 2026-08-29.
- [GitHub CLI on GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@latest/github-cli/github-cli/about-github-cli), retrieved 2026-08-29.
- [GitLab CLI authentication](https://docs.gitlab.com/cli/authentication/), retrieved 2026-08-29.
- [GitLab CLI merge request commands](https://docs.gitlab.com/cli/mr/), retrieved 2026-08-29.
- [GitLab CLI documentation version guidance](https://docs.gitlab.com/development/documentation/cli_styleguide/), retrieved 2026-08-29.
- [Tailscale Serve command](https://tailscale.com/docs/reference/tailscale-cli/serve), retrieved 2026-08-29.
- [Tailcat README at the pinned candidate](https://github.com/tailscale/tailcat/tree/88929418b1a3f3c74904a3136d6a9e87b1b5b9bb), retrieved 2026-08-29.
- [Tailcat `clientSOCKSMode` at the pinned candidate](https://github.com/tailscale/tailcat/blob/88929418b1a3f3c74904a3136d6a9e87b1b5b9bb/cmd/tailcat/tailcat.go), retrieved 2026-08-29.

## Limits

The audit used current source, installed `gh 2.98.0`, installed `glab 1.115.0`, installed `tailscale 1.102.2`, a temporary build of Tailcat commit `88929418b1a3f3c74904a3136d6a9e87b1b5b9bb`, and current first-party documentation. No authenticated provider, tailnet configuration, or self-operated relay was mutated. The temporary Tailcat binary, token, listeners, staging files, and task-created DERP cache were removed after the runtime check; Tailcat remains uninstalled globally.

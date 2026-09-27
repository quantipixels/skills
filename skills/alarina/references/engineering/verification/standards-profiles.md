# Apply a project's adopted standards

Use when the project requires explicit security, quality, release, accessibility or operational standards, or the user asks to establish them. The project owns adoption, applicability and exceptions. Alárinà helps identify relevant requirements, execute capable checks and retain evidence; a profile is not a certification.

Keep the profile with the existing project standards/compliance owner, then reference it through `policy_sources` in [configuration](../../productivity/environment/configuration.md). Pin the adopted source and version. Read the actual requirements and local interpretation; do not infer conformance from a framework name, a scanner score or another plugin's checklist.

For each applicable requirement, preserve the following useful relationships in the owner's established format:

| Information | Purpose |
| --- | --- |
| Requirement ID, source and version | Identify the actual obligation instead of an unversioned label. |
| Affected component and applicability rationale | Explain why this obligation applies, or the agreed exclusion. |
| Owner and existing control | Identify the code, procedure, platform setting or specialist tool that enforces it. |
| Verification and expected observation | Supply the exact local check, review, live journey or remote proof needed. |
| Candidate/environment and evidence | Distinguish executed proof from a proposed check and invalidate stale conclusions. |
| Exception, authority and revisit condition | Keep an accepted gap explicit; a failed check does not authorize an exception. |

Relevant source families include [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) for secure development practices, [OWASP ASVS](https://owasp.org/projects/asvs?tab=main) for application-security verification requirements, and [SLSA](https://slsa.dev/spec/v1.2/) for supply-chain levels and provenance. Choose the project's adopted version and scope rather than silently upgrading its policy. These sources cover different concerns; none replaces the others or a project's coding, data, operational and accessibility obligations.

For example, an adopted requirement to verify release provenance can point to the existing CI attestation producer and verifier, the expected builder/artifact identity, the release candidate and a negative test using a mismatched artifact. Merely attaching a provenance file does not prove the verification ran. Keep remote-only signing/build controls in CI; run available local validation before publication.

Use specialist security or platform capabilities where required. Register deterministic local commands in `checks`; describe genuinely remote-only obligations in `remote_checks`. A check can support a requirement without proving its whole scope. Independent review assesses missing consumers and limitations, and release/recovery methods retain their existing authority.

On a material source, configuration, architecture or standards change, revisit only affected applicability and proof. Keep unresolved obligations visible in the current plan and owning profile. Completion requires the accepted scope's evidence or an explicitly authorized exception; a generated mapping alone is incomplete.

# Actor task: authorization across entry points

Implement the supplied operation without weakening the project's identity, permission or tenant boundaries. Trace its normal request path and the supplied administrative and background paths. Follow the established policy owner and explicitly supported privileged behavior rather than adding an unrelated permission system.

Verify allowed and denied operations through the real entry points with the supplied principals and tenant data. For denied operations, establish both the external result and absence of protected state changes or queued/external effects. Preserve legitimate administration and worker behavior under the stated policy.

Return the scoped diff and evidence mapped to actor, entry point, resource and expected outcome. Identify any path that could not be exercised. A helper returning false or an API response alone does not establish that alternate callers and side effects are protected.

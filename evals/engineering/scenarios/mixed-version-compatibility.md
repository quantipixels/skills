# Actor task: mixed-version compatibility

Deliver the supplied representation change while the pinned old application version and the candidate version can both run during the stated deployment window. Preserve the specified old records, public identifiers and supported reader/writer behavior. Inspect the actual serializers, persistence mappings and consumers rather than introducing a parallel representation by preference.

Use the supplied populated database and supported deployment sequence. Demonstrate old/new reads and writes at the required stages, including data written after the change begins. Respect the stated rollback or forward-recovery contract. Stop and identify a concrete incompatibility if the requested coexistence cannot be achieved within scope.

Return the scoped diff and verification evidence, with a reader/writer compatibility table and any ordering constraint that affects deployment. Do not claim compatibility from an empty database migration, schema validation or candidate-only tests.

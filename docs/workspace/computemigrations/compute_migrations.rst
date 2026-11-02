``w.compute_migrations``: ComputeMigrations.v1
==============================================
.. currentmodule:: databricks.sdk.service.computemigrations

.. py:class:: ComputeMigrationsAPI

    Manage migrations of Classic compute workloads to Serverless.

    .. py:method:: approve_migration_execution(migration_id: str [, additional_feedback: Optional[str], etag: Optional[str]]) -> Migration

        Approves migration execution at the MIGRATION_REVIEW gate, advancing to execution.

        Valid only when the migration is in MIGRATION_REVIEW. If supplied, the ``etag`` must match the current
        server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in MIGRATION_REVIEW. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to approve for execution.
        :param additional_feedback: str (optional)
          Optional free-text feedback or instructions the user provides along with the approval, carried into
          the next stage of the migration.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        

    .. py:method:: approve_migration_translation(migration_id: str [, additional_feedback: Optional[str], etag: Optional[str]]) -> Migration

        Approves the working copy at the TRANSLATION_READY gate. If the migration was created with
        ``run_validation``, the working copy is then run to verify it executes successfully before the
        migration is presented for execution review; otherwise it advances straight to MIGRATION_REVIEW.

        Valid only when the migration is in TRANSLATION_READY. If supplied, the ``etag`` must match the
        current server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in TRANSLATION_READY. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to approve.
        :param additional_feedback: str (optional)
          Optional free-text feedback or instructions the user provides along with the approval, carried into
          the next stage of the migration.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        

    .. py:method:: cancel_migration(migration_id: str [, cancellation_reason: Optional[str], etag: Optional[str]]) -> Migration

        Cancels the migration, transitioning it to CANCELLED.

        Valid from any non-terminal state, unlike the review-gate transitions, which each require a specific
        state. Any in-flight agent work is abandoned and the migration stops advancing. The resource is
        retained for auditability.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is
        already in a terminal state. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to cancel.
        :param cancellation_reason: str (optional)
          Optional free-text reason for the cancellation.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        

    .. py:method:: create(migration: Migration [, request_id: Optional[str]]) -> Migration

        Creates a new migration for a Classic compute asset.

        The migration is created in PLANNING_PENDING and advances through the state machine as planning work
        is scheduled. The caller must have appropriate permissions: workspace admin for infrastructure-scoped
        migrations, job owner/admin for individual workload migrations.

        At most one migration may hold an asset. Returns ALREADY_EXISTS if the asset has a migration in
        flight, or one that already migrated it successfully; a migration that ended without succeeding, or
        was deleted, releases the asset so it can be migrated again. Returns INVALID_PARAMETER_VALUE if the
        asset is not eligible for migration.

        :param migration: :class:`Migration`
          The migration to create. The server generates ``migration_id`` and sets ``state`` to
          PLANNING_PENDING. Required fields: ``asset_type``, ``asset_uri``.
        :param request_id: str (optional)
          Client-generated request ID for idempotent request deduplication. The server de-duplicates requests
          with the same request_id for at least 24 hours, returning the existing migration instead of creating
          a duplicate.

        :returns: :class:`Migration`
        

    .. py:method:: delete(migration_id: str [, etag: Optional[str]]) -> Migration

        Deletes a migration (soft-delete).

        Allowed from any state. Deleting a migration marks the record deleted only — it does not roll back a
        migration that already ran, and resources created during the migration are not cleaned up. The
        migration resource is retained for auditability. To stop an in-flight migration (agent teardown,
        transition to CANCELLED), use CancelMigration instead.

        Returns NOT_FOUND if the migration does not exist, or was already deleted: a deleted migration is
        hidden from every method (Get, Update, List, and Delete), so it cannot be deleted again. Returns
        ABORTED if a supplied nonempty request etag does not match the resource version.

        :param migration_id: str
          The ID of the migration to cancel.
        :param etag: str (optional)
          If nonempty, must match the current resource etag or the request fails with ABORTED.

        :returns: :class:`Migration`
        

    .. py:method:: get(migration_id: str) -> Migration

        Retrieves a migration by its ID.

        Returns the current state, configuration, and output artifacts of the migration. Use this to poll
        migration progress or inspect artifacts after state transitions. Returns NOT_FOUND if the migration
        does not exist in the caller's workspace.

        :param migration_id: str
          The ID of the migration to retrieve.

        :returns: :class:`Migration`
        

    .. py:method:: list( [, asset_type: Optional[MigrationAssetType], page_size: Optional[int], page_token: Optional[str], states: Optional[List[MigrationState]]]) -> Iterator[Migration]

        Lists migrations in the caller's workspace, ordered by migration ID, with cursor-based pagination and
        filtering by asset type and state.

        Eventually consistent: results are read from a cache, and pagination is not a point-in-time snapshot,
        so a migration created during a List may not appear until a subsequent one.

        :param asset_type: :class:`MigrationAssetType` (optional)
          Filter by asset type.
        :param page_size: int (optional)
          Maximum number of migrations to return. Default: 50, maximum: 1000.
        :param page_token: str (optional)
          Page token from a previous ListMigrations call. When paginating, all other parameters must match the
          call that provided the page token.
        :param states: List[:class:`MigrationState`] (optional)
          Filter by migration state. Returns migrations in any of the specified states.

        :returns: Iterator over :class:`Migration`
        

    .. py:method:: reject_migration_execution(migration_id: str, rejection_reason: str [, etag: Optional[str]]) -> Migration

        Rejects migration execution at the MIGRATION_REVIEW gate, sending the migration to REVISION_PENDING to
        loop back for re-planning.

        Valid only when the migration is in MIGRATION_REVIEW. If supplied, the ``etag`` must match the current
        server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in MIGRATION_REVIEW. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to reject.
        :param rejection_reason: str
          Required free-text reason for the rejection, fed back into re-planning so the next plan can address
          the user's concerns.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        

    .. py:method:: reject_migration_translation(migration_id: str, rejection_reason: str [, etag: Optional[str]]) -> Migration

        Rejects the working copy at the TRANSLATION_READY gate, sending the migration to REVISION_PENDING to
        loop back for re-planning.

        Valid only when the migration is in TRANSLATION_READY. If supplied, the ``etag`` must match the
        current server value.

        Returns NOT_FOUND if the migration does not exist. Returns FAILED_PRECONDITION if the migration is not
        in TRANSLATION_READY. Returns ABORTED if the etag does not match the current resource version.

        :param migration_id: str
          The ID of the migration to reject.
        :param rejection_reason: str
          Required free-text reason for the rejection, fed back into re-planning so the next plan can address
          the user's concerns.
        :param etag: str (optional)
          Optional resource version for optimistic concurrency control. If supplied, it must match the current
          server value.

        :returns: :class:`Migration`
        
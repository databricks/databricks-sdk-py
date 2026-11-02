Compute Migrations
==================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.computemigrations`` module.

.. py:currentmodule:: databricks.sdk.service.computemigrations
.. autoclass:: BakingConfig
   :members:
   :undoc-members:

.. autoclass:: BakingReport
   :members:
   :undoc-members:

.. autoclass:: ListMigrationsResponse
   :members:
   :undoc-members:

.. autoclass:: Migration
   :members:
   :undoc-members:

.. autoclass:: MigrationAsset
   :members:
   :undoc-members:

.. py:class:: MigrationAssetType

   Type of a migration asset: the Classic asset being migrated, or an asset the migration agent created for it. Migrations can only be created for JOB assets.

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: INTERACTIVE
      :value: "INTERACTIVE"

   .. py:attribute:: JOB
      :value: "JOB"

.. autoclass:: MigrationInitiator
   :members:
   :undoc-members:

.. py:class:: MigrationInitiatorRole

   Role of the migration initiator, determining approval authority.

   .. py:attribute:: ACCOUNT_ADMIN
      :value: "ACCOUNT_ADMIN"

   .. py:attribute:: JOB_ADMIN
      :value: "JOB_ADMIN"

   .. py:attribute:: SYSTEM
      :value: "SYSTEM"

   .. py:attribute:: WORKSPACE_ADMIN
      :value: "WORKSPACE_ADMIN"

.. autoclass:: MigrationReport
   :members:
   :undoc-members:

.. py:class:: MigrationState

   The state of a migration in its lifecycle.

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: MIGRATION_COMPLETE
      :value: "MIGRATION_COMPLETE"

   .. py:attribute:: MIGRATION_OBSERVATION
      :value: "MIGRATION_OBSERVATION"

   .. py:attribute:: MIGRATION_PENDING
      :value: "MIGRATION_PENDING"

   .. py:attribute:: MIGRATION_REVIEW
      :value: "MIGRATION_REVIEW"

   .. py:attribute:: MIGRATION_RUNNING
      :value: "MIGRATION_RUNNING"

   .. py:attribute:: NOT_SUPPORTED
      :value: "NOT_SUPPORTED"

   .. py:attribute:: PLANNING_PENDING
      :value: "PLANNING_PENDING"

   .. py:attribute:: PLANNING_REVIEW
      :value: "PLANNING_REVIEW"

   .. py:attribute:: PLANNING_RUNNING
      :value: "PLANNING_RUNNING"

   .. py:attribute:: REVISION_PENDING
      :value: "REVISION_PENDING"

   .. py:attribute:: TRANSLATION_CREATING
      :value: "TRANSLATION_CREATING"

   .. py:attribute:: TRANSLATION_PENDING
      :value: "TRANSLATION_PENDING"

   .. py:attribute:: TRANSLATION_READY
      :value: "TRANSLATION_READY"

   .. py:attribute:: VALIDATION_RUNNING
      :value: "VALIDATION_RUNNING"

   .. py:attribute:: VALIDATION_SCHEDULING
      :value: "VALIDATION_SCHEDULING"

.. autoclass:: MigrationStateTransition
   :members:
   :undoc-members:

.. autoclass:: ValidationReport
   :members:
   :undoc-members:

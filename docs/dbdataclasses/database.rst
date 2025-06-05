Database Instances
==================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.database`` module.

.. py:currentmodule:: databricks.sdk.service.database
.. autoclass:: DatabaseCatalog
   :members:
   :undoc-members:

.. autoclass:: DatabaseCredential
   :members:
   :undoc-members:

.. autoclass:: DatabaseInstance
   :members:
   :undoc-members:

.. py:class:: DatabaseInstanceState

   .. py:attribute:: AVAILABLE
      :value: "AVAILABLE"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: FAILING_OVER
      :value: "FAILING_OVER"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: UPDATING
      :value: "UPDATING"

.. autoclass:: DatabaseTable
   :members:
   :undoc-members:

.. autoclass:: DeleteDatabaseCatalogResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDatabaseInstanceResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDatabaseTableResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteSyncedDatabaseTableResponse
   :members:
   :undoc-members:

.. autoclass:: GenerateDatabaseCredentialRequest
   :members:
   :undoc-members:

.. autoclass:: ListDatabaseInstancesResponse
   :members:
   :undoc-members:

.. autoclass:: NewPipelineSpec
   :members:
   :undoc-members:

.. py:class:: ProvisioningInfoState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DEGRADED
      :value: "DEGRADED"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

   .. py:attribute:: UPDATING
      :value: "UPDATING"

.. autoclass:: SyncedDatabaseTable
   :members:
   :undoc-members:

.. autoclass:: SyncedTableContinuousUpdateStatus
   :members:
   :undoc-members:

.. autoclass:: SyncedTableFailedStatus
   :members:
   :undoc-members:

.. autoclass:: SyncedTablePipelineProgress
   :members:
   :undoc-members:

.. autoclass:: SyncedTableProvisioningStatus
   :members:
   :undoc-members:

.. py:class:: SyncedTableSchedulingPolicy

   .. py:attribute:: CONTINUOUS
      :value: "CONTINUOUS"

   .. py:attribute:: SNAPSHOT
      :value: "SNAPSHOT"

   .. py:attribute:: TRIGGERED
      :value: "TRIGGERED"

.. autoclass:: SyncedTableSpec
   :members:
   :undoc-members:

.. py:class:: SyncedTableState

   The state of a synced table.

   .. py:attribute:: SYNCED_TABLED_OFFLINE
      :value: "SYNCED_TABLED_OFFLINE"

   .. py:attribute:: SYNCED_TABLE_OFFLINE_FAILED
      :value: "SYNCED_TABLE_OFFLINE_FAILED"

   .. py:attribute:: SYNCED_TABLE_ONLINE
      :value: "SYNCED_TABLE_ONLINE"

   .. py:attribute:: SYNCED_TABLE_ONLINE_CONTINUOUS_UPDATE
      :value: "SYNCED_TABLE_ONLINE_CONTINUOUS_UPDATE"

   .. py:attribute:: SYNCED_TABLE_ONLINE_NO_PENDING_UPDATE
      :value: "SYNCED_TABLE_ONLINE_NO_PENDING_UPDATE"

   .. py:attribute:: SYNCED_TABLE_ONLINE_PIPELINE_FAILED
      :value: "SYNCED_TABLE_ONLINE_PIPELINE_FAILED"

   .. py:attribute:: SYNCED_TABLE_ONLINE_TRIGGERED_UPDATE
      :value: "SYNCED_TABLE_ONLINE_TRIGGERED_UPDATE"

   .. py:attribute:: SYNCED_TABLE_ONLINE_UPDATING_PIPELINE_RESOURCES
      :value: "SYNCED_TABLE_ONLINE_UPDATING_PIPELINE_RESOURCES"

   .. py:attribute:: SYNCED_TABLE_PROVISIONING
      :value: "SYNCED_TABLE_PROVISIONING"

   .. py:attribute:: SYNCED_TABLE_PROVISIONING_INITIAL_SNAPSHOT
      :value: "SYNCED_TABLE_PROVISIONING_INITIAL_SNAPSHOT"

   .. py:attribute:: SYNCED_TABLE_PROVISIONING_PIPELINE_RESOURCES
      :value: "SYNCED_TABLE_PROVISIONING_PIPELINE_RESOURCES"

.. autoclass:: SyncedTableStatus
   :members:
   :undoc-members:

.. autoclass:: SyncedTableTriggeredUpdateStatus
   :members:
   :undoc-members:

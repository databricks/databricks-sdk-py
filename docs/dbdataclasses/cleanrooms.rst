Clean Rooms
===========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.cleanrooms`` module.

.. py:currentmodule:: databricks.sdk.service.cleanrooms
.. autoclass:: CleanRoom
   :members:
   :undoc-members:

.. py:class:: CleanRoomAccessRestricted

   .. py:attribute:: CSP_MISMATCH
      :value: "CSP_MISMATCH"

   .. py:attribute:: NO_RESTRICTION
      :value: "NO_RESTRICTION"

.. autoclass:: CleanRoomAsset
   :members:
   :undoc-members:

.. py:class:: CleanRoomAssetAssetType

   .. py:attribute:: FOREIGN_TABLE
      :value: "FOREIGN_TABLE"

   .. py:attribute:: NOTEBOOK_FILE
      :value: "NOTEBOOK_FILE"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VIEW
      :value: "VIEW"

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: CleanRoomAssetForeignTable
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetForeignTableLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetNotebook
   :members:
   :undoc-members:

.. py:class:: CleanRoomAssetStatusEnum

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: PERMISSION_DENIED
      :value: "PERMISSION_DENIED"

.. autoclass:: CleanRoomAssetTable
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetTableLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetView
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetViewLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetVolumeLocalDetails
   :members:
   :undoc-members:

.. autoclass:: CleanRoomCollaborator
   :members:
   :undoc-members:

.. autoclass:: CleanRoomNotebookTaskRun
   :members:
   :undoc-members:

.. autoclass:: CleanRoomOutputCatalog
   :members:
   :undoc-members:

.. py:class:: CleanRoomOutputCatalogOutputCatalogStatus

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: NOT_CREATED
      :value: "NOT_CREATED"

   .. py:attribute:: NOT_ELIGIBLE
      :value: "NOT_ELIGIBLE"

.. autoclass:: CleanRoomRemoteDetail
   :members:
   :undoc-members:

.. py:class:: CleanRoomStatusEnum

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

.. py:class:: CleanRoomTaskRunLifeCycleState

   Copied from elastic-spark-common/api/messages/runs.proto. Using the original definition to remove coupling with jobs API definition

   .. py:attribute:: BLOCKED
      :value: "BLOCKED"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: RUN_LIFE_CYCLE_STATE_UNSPECIFIED
      :value: "RUN_LIFE_CYCLE_STATE_UNSPECIFIED"

   .. py:attribute:: SKIPPED
      :value: "SKIPPED"

   .. py:attribute:: TERMINATED
      :value: "TERMINATED"

   .. py:attribute:: TERMINATING
      :value: "TERMINATING"

   .. py:attribute:: WAITING_FOR_RETRY
      :value: "WAITING_FOR_RETRY"

.. py:class:: CleanRoomTaskRunResultState

   Copied from elastic-spark-common/api/messages/runs.proto. Using the original definition to avoid cyclic dependency.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: DISABLED
      :value: "DISABLED"

   .. py:attribute:: EVICTED
      :value: "EVICTED"

   .. py:attribute:: EXCLUDED
      :value: "EXCLUDED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: MAXIMUM_CONCURRENT_RUNS_REACHED
      :value: "MAXIMUM_CONCURRENT_RUNS_REACHED"

   .. py:attribute:: RUN_RESULT_STATE_UNSPECIFIED
      :value: "RUN_RESULT_STATE_UNSPECIFIED"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

   .. py:attribute:: SUCCESS_WITH_FAILURES
      :value: "SUCCESS_WITH_FAILURES"

   .. py:attribute:: TIMEDOUT
      :value: "TIMEDOUT"

   .. py:attribute:: UPSTREAM_CANCELED
      :value: "UPSTREAM_CANCELED"

   .. py:attribute:: UPSTREAM_EVICTED
      :value: "UPSTREAM_EVICTED"

   .. py:attribute:: UPSTREAM_FAILED
      :value: "UPSTREAM_FAILED"

.. autoclass:: CleanRoomTaskRunState
   :members:
   :undoc-members:

.. autoclass:: CollaboratorJobRunInfo
   :members:
   :undoc-members:

.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. autoclass:: ColumnMask
   :members:
   :undoc-members:

.. py:class:: ColumnTypeName

   .. py:attribute:: ARRAY
      :value: "ARRAY"

   .. py:attribute:: BINARY
      :value: "BINARY"

   .. py:attribute:: BOOLEAN
      :value: "BOOLEAN"

   .. py:attribute:: BYTE
      :value: "BYTE"

   .. py:attribute:: CHAR
      :value: "CHAR"

   .. py:attribute:: DATE
      :value: "DATE"

   .. py:attribute:: DECIMAL
      :value: "DECIMAL"

   .. py:attribute:: DOUBLE
      :value: "DOUBLE"

   .. py:attribute:: FLOAT
      :value: "FLOAT"

   .. py:attribute:: INT
      :value: "INT"

   .. py:attribute:: INTERVAL
      :value: "INTERVAL"

   .. py:attribute:: LONG
      :value: "LONG"

   .. py:attribute:: MAP
      :value: "MAP"

   .. py:attribute:: NULL
      :value: "NULL"

   .. py:attribute:: SHORT
      :value: "SHORT"

   .. py:attribute:: STRING
      :value: "STRING"

   .. py:attribute:: STRUCT
      :value: "STRUCT"

   .. py:attribute:: TABLE_TYPE
      :value: "TABLE_TYPE"

   .. py:attribute:: TIMESTAMP
      :value: "TIMESTAMP"

   .. py:attribute:: TIMESTAMP_NTZ
      :value: "TIMESTAMP_NTZ"

   .. py:attribute:: USER_DEFINED_TYPE
      :value: "USER_DEFINED_TYPE"

   .. py:attribute:: VARIANT
      :value: "VARIANT"

.. autoclass:: ComplianceSecurityProfile
   :members:
   :undoc-members:

.. py:class:: ComplianceStandard

   Compliance stardard for SHIELD customers

   .. py:attribute:: CANADA_PROTECTED_B
      :value: "CANADA_PROTECTED_B"

   .. py:attribute:: CYBER_ESSENTIAL_PLUS
      :value: "CYBER_ESSENTIAL_PLUS"

   .. py:attribute:: FEDRAMP_HIGH
      :value: "FEDRAMP_HIGH"

   .. py:attribute:: FEDRAMP_IL5
      :value: "FEDRAMP_IL5"

   .. py:attribute:: FEDRAMP_MODERATE
      :value: "FEDRAMP_MODERATE"

   .. py:attribute:: HIPAA
      :value: "HIPAA"

   .. py:attribute:: HITRUST
      :value: "HITRUST"

   .. py:attribute:: IRAP_PROTECTED
      :value: "IRAP_PROTECTED"

   .. py:attribute:: ISMAP
      :value: "ISMAP"

   .. py:attribute:: ITAR_EAR
      :value: "ITAR_EAR"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: PCI_DSS
      :value: "PCI_DSS"

.. autoclass:: CreateCleanRoomOutputCatalogResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteCleanRoomAssetResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: EgressNetworkPolicy
   :members:
   :undoc-members:

.. autoclass:: EgressNetworkPolicyInternetAccessPolicy
   :members:
   :undoc-members:

.. autoclass:: EgressNetworkPolicyInternetAccessPolicyInternetDestination
   :members:
   :undoc-members:

.. py:class:: EgressNetworkPolicyInternetAccessPolicyInternetDestinationInternetDestinationFilteringProtocol

   The filtering protocol used by the DP. For private and public preview, SEG will only support TCP filtering (i.e. DNS based filtering, filtering by destination IP address), so protocol will be set to TCP by default and hidden from the user. In the future, users may be able to select HTTP filtering (i.e. SNI based filtering, filtering by FQDN).

   .. py:attribute:: TCP
      :value: "TCP"

.. py:class:: EgressNetworkPolicyInternetAccessPolicyInternetDestinationInternetDestinationType

   .. py:attribute:: FQDN
      :value: "FQDN"

.. autoclass:: EgressNetworkPolicyInternetAccessPolicyLogOnlyMode
   :members:
   :undoc-members:

.. py:class:: EgressNetworkPolicyInternetAccessPolicyLogOnlyModeLogOnlyModeType

   .. py:attribute:: ALL_SERVICES
      :value: "ALL_SERVICES"

   .. py:attribute:: SELECTED_SERVICES
      :value: "SELECTED_SERVICES"

.. py:class:: EgressNetworkPolicyInternetAccessPolicyLogOnlyModeWorkloadType

   The values should match the list of workloads used in networkconfig.proto

   .. py:attribute:: DBSQL
      :value: "DBSQL"

   .. py:attribute:: ML_SERVING
      :value: "ML_SERVING"

.. py:class:: EgressNetworkPolicyInternetAccessPolicyRestrictionMode

   At which level can Databricks and Databricks managed compute access Internet. FULL_ACCESS: Databricks can access Internet. No blocking rules will apply. RESTRICTED_ACCESS: Databricks can only access explicitly allowed internet and storage destinations, as well as UC connections and external locations. PRIVATE_ACCESS_ONLY (not used): Databricks can only access destinations via private link.

   .. py:attribute:: FULL_ACCESS
      :value: "FULL_ACCESS"

   .. py:attribute:: PRIVATE_ACCESS_ONLY
      :value: "PRIVATE_ACCESS_ONLY"

   .. py:attribute:: RESTRICTED_ACCESS
      :value: "RESTRICTED_ACCESS"

.. autoclass:: EgressNetworkPolicyInternetAccessPolicyStorageDestination
   :members:
   :undoc-members:

.. py:class:: EgressNetworkPolicyInternetAccessPolicyStorageDestinationStorageDestinationType

   .. py:attribute:: AWS_S3
      :value: "AWS_S3"

   .. py:attribute:: AZURE_STORAGE
      :value: "AZURE_STORAGE"

   .. py:attribute:: CLOUDFLARE_R2
      :value: "CLOUDFLARE_R2"

   .. py:attribute:: GOOGLE_CLOUD_STORAGE
      :value: "GOOGLE_CLOUD_STORAGE"

.. autoclass:: ListCleanRoomAssetsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCleanRoomNotebookTaskRunsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCleanRoomsResponse
   :members:
   :undoc-members:

.. autoclass:: Partition
   :members:
   :undoc-members:

.. autoclass:: PartitionValue
   :members:
   :undoc-members:

.. py:class:: PartitionValueOp

   .. py:attribute:: EQUAL
      :value: "EQUAL"

   .. py:attribute:: LIKE
      :value: "LIKE"

.. autoclass:: UpdateCleanRoomRequest
   :members:
   :undoc-members:

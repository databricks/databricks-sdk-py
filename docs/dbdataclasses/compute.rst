Compute
=======

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.compute`` module.

.. py:currentmodule:: databricks.sdk.service.compute
.. autoclass:: AddInstanceProfile
   :members:
   :undoc-members:

.. autoclass:: AddResponse
   :members:
   :undoc-members:

.. autoclass:: Adlsgen2Info
   :members:
   :undoc-members:

.. autoclass:: AutoScale
   :members:
   :undoc-members:

.. autoclass:: AwsAttributes
   :members:
   :undoc-members:

.. py:class:: AwsAvailability

   Availability type used for all subsequent nodes past the `first_on_demand` ones.
   Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster.

   .. py:attribute:: ON_DEMAND
      :value: "ON_DEMAND"

   .. py:attribute:: SPOT
      :value: "SPOT"

   .. py:attribute:: SPOT_WITH_FALLBACK
      :value: "SPOT_WITH_FALLBACK"

.. autoclass:: AzureAttributes
   :members:
   :undoc-members:

.. py:class:: AzureAvailability

   Availability type used for all subsequent nodes past the `first_on_demand` ones. Note: If `first_on_demand` is zero, this availability type will be used for the entire cluster.

   .. py:attribute:: ON_DEMAND_AZURE
      :value: "ON_DEMAND_AZURE"

   .. py:attribute:: SPOT_AZURE
      :value: "SPOT_AZURE"

   .. py:attribute:: SPOT_WITH_FALLBACK_AZURE
      :value: "SPOT_WITH_FALLBACK_AZURE"

.. autoclass:: CancelCommand
   :members:
   :undoc-members:

.. autoclass:: CancelResponse
   :members:
   :undoc-members:

.. autoclass:: ChangeClusterOwner
   :members:
   :undoc-members:

.. autoclass:: ChangeClusterOwnerResponse
   :members:
   :undoc-members:

.. autoclass:: ClientsTypes
   :members:
   :undoc-members:

.. autoclass:: CloneCluster
   :members:
   :undoc-members:

.. autoclass:: CloudProviderNodeInfo
   :members:
   :undoc-members:

.. py:class:: CloudProviderNodeStatus

   .. py:attribute:: NOT_AVAILABLE_IN_REGION
      :value: "NOT_AVAILABLE_IN_REGION"

   .. py:attribute:: NOT_ENABLED_ON_SUBSCRIPTION
      :value: "NOT_ENABLED_ON_SUBSCRIPTION"

.. autoclass:: ClusterAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: ClusterAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: ClusterAttributes
   :members:
   :undoc-members:

.. autoclass:: ClusterCompliance
   :members:
   :undoc-members:

.. autoclass:: ClusterDetails
   :members:
   :undoc-members:

.. autoclass:: ClusterEvent
   :members:
   :undoc-members:

.. autoclass:: ClusterLibraryStatuses
   :members:
   :undoc-members:

.. autoclass:: ClusterLogConf
   :members:
   :undoc-members:

.. autoclass:: ClusterPermission
   :members:
   :undoc-members:

.. py:class:: ClusterPermissionLevel

   Permission level

   .. py:attribute:: CAN_ATTACH_TO
      :value: "CAN_ATTACH_TO"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_RESTART
      :value: "CAN_RESTART"

.. autoclass:: ClusterPermissions
   :members:
   :undoc-members:

.. autoclass:: ClusterPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: ClusterPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: ClusterPolicyAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: ClusterPolicyAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: ClusterPolicyPermission
   :members:
   :undoc-members:

.. py:class:: ClusterPolicyPermissionLevel

   Permission level

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

.. autoclass:: ClusterPolicyPermissions
   :members:
   :undoc-members:

.. autoclass:: ClusterPolicyPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: ClusterPolicyPermissionsRequest
   :members:
   :undoc-members:

.. autoclass:: ClusterSettingsChange
   :members:
   :undoc-members:

.. autoclass:: ClusterSize
   :members:
   :undoc-members:

.. py:class:: ClusterSource

   Determines whether the cluster was created by a user through the UI, created by the Databricks Jobs Scheduler, or through an API request. This is the same as cluster_creator, but read only.

   .. py:attribute:: API
      :value: "API"

   .. py:attribute:: JOB
      :value: "JOB"

   .. py:attribute:: MODELS
      :value: "MODELS"

   .. py:attribute:: PIPELINE
      :value: "PIPELINE"

   .. py:attribute:: PIPELINE_MAINTENANCE
      :value: "PIPELINE_MAINTENANCE"

   .. py:attribute:: SQL
      :value: "SQL"

   .. py:attribute:: UI
      :value: "UI"

.. autoclass:: ClusterSpec
   :members:
   :undoc-members:

.. autoclass:: Command
   :members:
   :undoc-members:

.. py:class:: CommandStatus

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: CANCELLING
      :value: "CANCELLING"

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: FINISHED
      :value: "FINISHED"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

.. autoclass:: CommandStatusResponse
   :members:
   :undoc-members:

.. py:class:: ContextStatus

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

.. autoclass:: ContextStatusResponse
   :members:
   :undoc-members:

.. autoclass:: CreateCluster
   :members:
   :undoc-members:

.. autoclass:: CreateClusterResponse
   :members:
   :undoc-members:

.. autoclass:: CreateContext
   :members:
   :undoc-members:

.. autoclass:: CreateInstancePool
   :members:
   :undoc-members:

.. autoclass:: CreateInstancePoolResponse
   :members:
   :undoc-members:

.. autoclass:: CreatePolicy
   :members:
   :undoc-members:

.. autoclass:: CreatePolicyResponse
   :members:
   :undoc-members:

.. autoclass:: CreateResponse
   :members:
   :undoc-members:

.. autoclass:: Created
   :members:
   :undoc-members:

.. autoclass:: CustomPolicyTag
   :members:
   :undoc-members:

.. autoclass:: DataPlaneEventDetails
   :members:
   :undoc-members:

.. py:class:: DataPlaneEventDetailsEventType

   .. py:attribute:: NODE_BLACKLISTED
      :value: "NODE_BLACKLISTED"

   .. py:attribute:: NODE_EXCLUDED_DECOMMISSIONED
      :value: "NODE_EXCLUDED_DECOMMISSIONED"

.. py:class:: DataSecurityMode

   Data security mode decides what data governance model to use when accessing data from a cluster.
   The following modes can only be used when `kind = CLASSIC_PREVIEW`. * `DATA_SECURITY_MODE_AUTO`: Databricks will choose the most appropriate access mode depending on your compute configuration. * `DATA_SECURITY_MODE_STANDARD`: Alias for `USER_ISOLATION`. * `DATA_SECURITY_MODE_DEDICATED`: Alias for `SINGLE_USER`.
   The following modes can be used regardless of `kind`. * `NONE`: No security isolation for multiple users sharing the cluster. Data governance features are not available in this mode. * `SINGLE_USER`: A secure cluster that can only be exclusively used by a single user specified in `single_user_name`. Most programming languages, cluster features and data governance features are available in this mode. * `USER_ISOLATION`: A secure cluster that can be shared by multiple users. Cluster users are fully isolated so that they cannot see each other's data and credentials. Most data governance features are supported in this mode. But programming languages and cluster features might be limited.
   The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for future Databricks Runtime versions:
   * `LEGACY_TABLE_ACL`: This mode is for users migrating from legacy Table ACL clusters. * `LEGACY_PASSTHROUGH`: This mode is for users migrating from legacy Passthrough on high concurrency clusters. * `LEGACY_SINGLE_USER`: This mode is for users migrating from legacy Passthrough on standard clusters. * `LEGACY_SINGLE_USER_STANDARD`: This mode provides a way that doesn’t have UC nor passthrough enabled.

   .. py:attribute:: DATA_SECURITY_MODE_AUTO
      :value: "DATA_SECURITY_MODE_AUTO"

   .. py:attribute:: DATA_SECURITY_MODE_DEDICATED
      :value: "DATA_SECURITY_MODE_DEDICATED"

   .. py:attribute:: DATA_SECURITY_MODE_STANDARD
      :value: "DATA_SECURITY_MODE_STANDARD"

   .. py:attribute:: LEGACY_PASSTHROUGH
      :value: "LEGACY_PASSTHROUGH"

   .. py:attribute:: LEGACY_SINGLE_USER
      :value: "LEGACY_SINGLE_USER"

   .. py:attribute:: LEGACY_SINGLE_USER_STANDARD
      :value: "LEGACY_SINGLE_USER_STANDARD"

   .. py:attribute:: LEGACY_TABLE_ACL
      :value: "LEGACY_TABLE_ACL"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: SINGLE_USER
      :value: "SINGLE_USER"

   .. py:attribute:: USER_ISOLATION
      :value: "USER_ISOLATION"

.. autoclass:: DbfsStorageInfo
   :members:
   :undoc-members:

.. autoclass:: DeleteCluster
   :members:
   :undoc-members:

.. autoclass:: DeleteClusterResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteInstancePool
   :members:
   :undoc-members:

.. autoclass:: DeleteInstancePoolResponse
   :members:
   :undoc-members:

.. autoclass:: DeletePolicy
   :members:
   :undoc-members:

.. autoclass:: DeletePolicyResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DestroyContext
   :members:
   :undoc-members:

.. autoclass:: DestroyResponse
   :members:
   :undoc-members:

.. autoclass:: DiskSpec
   :members:
   :undoc-members:

.. autoclass:: DiskType
   :members:
   :undoc-members:

.. py:class:: DiskTypeAzureDiskVolumeType

   All Azure Disk types that Databricks supports. See https://docs.microsoft.com/en-us/azure/storage/storage-about-disks-and-vhds-linux#types-of-disks

   .. py:attribute:: PREMIUM_LRS
      :value: "PREMIUM_LRS"

   .. py:attribute:: STANDARD_LRS
      :value: "STANDARD_LRS"

.. py:class:: DiskTypeEbsVolumeType

   All EBS volume types that Databricks supports. See https://aws.amazon.com/ebs/details/ for details.

   .. py:attribute:: GENERAL_PURPOSE_SSD
      :value: "GENERAL_PURPOSE_SSD"

   .. py:attribute:: THROUGHPUT_OPTIMIZED_HDD
      :value: "THROUGHPUT_OPTIMIZED_HDD"

.. autoclass:: DockerBasicAuth
   :members:
   :undoc-members:

.. autoclass:: DockerImage
   :members:
   :undoc-members:

.. py:class:: EbsVolumeType

   All EBS volume types that Databricks supports. See https://aws.amazon.com/ebs/details/ for details.

   .. py:attribute:: GENERAL_PURPOSE_SSD
      :value: "GENERAL_PURPOSE_SSD"

   .. py:attribute:: THROUGHPUT_OPTIMIZED_HDD
      :value: "THROUGHPUT_OPTIMIZED_HDD"

.. autoclass:: EditCluster
   :members:
   :undoc-members:

.. autoclass:: EditClusterResponse
   :members:
   :undoc-members:

.. autoclass:: EditInstancePool
   :members:
   :undoc-members:

.. autoclass:: EditInstancePoolResponse
   :members:
   :undoc-members:

.. autoclass:: EditPolicy
   :members:
   :undoc-members:

.. autoclass:: EditPolicyResponse
   :members:
   :undoc-members:

.. autoclass:: EditResponse
   :members:
   :undoc-members:

.. autoclass:: EnforceClusterComplianceRequest
   :members:
   :undoc-members:

.. autoclass:: EnforceClusterComplianceResponse
   :members:
   :undoc-members:

.. autoclass:: Environment
   :members:
   :undoc-members:

.. autoclass:: EventDetails
   :members:
   :undoc-members:

.. py:class:: EventDetailsCause

   The cause of a change in target size.

   .. py:attribute:: AUTORECOVERY
      :value: "AUTORECOVERY"

   .. py:attribute:: AUTOSCALE
      :value: "AUTOSCALE"

   .. py:attribute:: REPLACE_BAD_NODES
      :value: "REPLACE_BAD_NODES"

   .. py:attribute:: USER_REQUEST
      :value: "USER_REQUEST"

.. py:class:: EventType

   .. py:attribute:: ADD_NODES_FAILED
      :value: "ADD_NODES_FAILED"

   .. py:attribute:: AUTOMATIC_CLUSTER_UPDATE
      :value: "AUTOMATIC_CLUSTER_UPDATE"

   .. py:attribute:: AUTOSCALING_BACKOFF
      :value: "AUTOSCALING_BACKOFF"

   .. py:attribute:: AUTOSCALING_FAILED
      :value: "AUTOSCALING_FAILED"

   .. py:attribute:: AUTOSCALING_STATS_REPORT
      :value: "AUTOSCALING_STATS_REPORT"

   .. py:attribute:: CREATING
      :value: "CREATING"

   .. py:attribute:: DBFS_DOWN
      :value: "DBFS_DOWN"

   .. py:attribute:: DID_NOT_EXPAND_DISK
      :value: "DID_NOT_EXPAND_DISK"

   .. py:attribute:: DRIVER_HEALTHY
      :value: "DRIVER_HEALTHY"

   .. py:attribute:: DRIVER_NOT_RESPONDING
      :value: "DRIVER_NOT_RESPONDING"

   .. py:attribute:: DRIVER_UNAVAILABLE
      :value: "DRIVER_UNAVAILABLE"

   .. py:attribute:: EDITED
      :value: "EDITED"

   .. py:attribute:: EXPANDED_DISK
      :value: "EXPANDED_DISK"

   .. py:attribute:: FAILED_TO_EXPAND_DISK
      :value: "FAILED_TO_EXPAND_DISK"

   .. py:attribute:: INIT_SCRIPTS_FINISHED
      :value: "INIT_SCRIPTS_FINISHED"

   .. py:attribute:: INIT_SCRIPTS_STARTED
      :value: "INIT_SCRIPTS_STARTED"

   .. py:attribute:: METASTORE_DOWN
      :value: "METASTORE_DOWN"

   .. py:attribute:: NODES_LOST
      :value: "NODES_LOST"

   .. py:attribute:: NODE_BLACKLISTED
      :value: "NODE_BLACKLISTED"

   .. py:attribute:: NODE_EXCLUDED_DECOMMISSIONED
      :value: "NODE_EXCLUDED_DECOMMISSIONED"

   .. py:attribute:: PINNED
      :value: "PINNED"

   .. py:attribute:: RESIZING
      :value: "RESIZING"

   .. py:attribute:: RESTARTING
      :value: "RESTARTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SPARK_EXCEPTION
      :value: "SPARK_EXCEPTION"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: TERMINATING
      :value: "TERMINATING"

   .. py:attribute:: UNPINNED
      :value: "UNPINNED"

   .. py:attribute:: UPSIZE_COMPLETED
      :value: "UPSIZE_COMPLETED"

.. autoclass:: GcpAttributes
   :members:
   :undoc-members:

.. py:class:: GcpAvailability

   This field determines whether the instance pool will contain preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable.

   .. py:attribute:: ON_DEMAND_GCP
      :value: "ON_DEMAND_GCP"

   .. py:attribute:: PREEMPTIBLE_GCP
      :value: "PREEMPTIBLE_GCP"

   .. py:attribute:: PREEMPTIBLE_WITH_FALLBACK_GCP
      :value: "PREEMPTIBLE_WITH_FALLBACK_GCP"

.. autoclass:: GcsStorageInfo
   :members:
   :undoc-members:

.. autoclass:: GetClusterComplianceResponse
   :members:
   :undoc-members:

.. autoclass:: GetClusterPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetClusterPolicyPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetEvents
   :members:
   :undoc-members:

.. py:class:: GetEventsOrder

   .. py:attribute:: ASC
      :value: "ASC"

   .. py:attribute:: DESC
      :value: "DESC"

.. autoclass:: GetEventsResponse
   :members:
   :undoc-members:

.. autoclass:: GetInstancePool
   :members:
   :undoc-members:

.. autoclass:: GetInstancePoolPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetSparkVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: GlobalInitScriptCreateRequest
   :members:
   :undoc-members:

.. autoclass:: GlobalInitScriptDetails
   :members:
   :undoc-members:

.. autoclass:: GlobalInitScriptDetailsWithContent
   :members:
   :undoc-members:

.. autoclass:: GlobalInitScriptUpdateRequest
   :members:
   :undoc-members:

.. autoclass:: InitScriptEventDetails
   :members:
   :undoc-members:

.. py:class:: InitScriptExecutionDetailsInitScriptExecutionStatus

   Result of attempted script execution

   .. py:attribute:: FAILED_EXECUTION
      :value: "FAILED_EXECUTION"

   .. py:attribute:: FAILED_FETCH
      :value: "FAILED_FETCH"

   .. py:attribute:: FUSE_MOUNT_FAILED
      :value: "FUSE_MOUNT_FAILED"

   .. py:attribute:: NOT_EXECUTED
      :value: "NOT_EXECUTED"

   .. py:attribute:: SKIPPED
      :value: "SKIPPED"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: InitScriptInfo
   :members:
   :undoc-members:

.. autoclass:: InitScriptInfoAndExecutionDetails
   :members:
   :undoc-members:

.. autoclass:: InstallLibraries
   :members:
   :undoc-members:

.. autoclass:: InstallLibrariesResponse
   :members:
   :undoc-members:

.. autoclass:: InstancePoolAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: InstancePoolAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: InstancePoolAndStats
   :members:
   :undoc-members:

.. autoclass:: InstancePoolAwsAttributes
   :members:
   :undoc-members:

.. py:class:: InstancePoolAwsAttributesAvailability

   The set of AWS availability types supported when setting up nodes for a cluster.

   .. py:attribute:: ON_DEMAND
      :value: "ON_DEMAND"

   .. py:attribute:: SPOT
      :value: "SPOT"

.. autoclass:: InstancePoolAzureAttributes
   :members:
   :undoc-members:

.. py:class:: InstancePoolAzureAttributesAvailability

   The set of Azure availability types supported when setting up nodes for a cluster.

   .. py:attribute:: ON_DEMAND_AZURE
      :value: "ON_DEMAND_AZURE"

   .. py:attribute:: SPOT_AZURE
      :value: "SPOT_AZURE"

.. autoclass:: InstancePoolGcpAttributes
   :members:
   :undoc-members:

.. autoclass:: InstancePoolPermission
   :members:
   :undoc-members:

.. py:class:: InstancePoolPermissionLevel

   Permission level

   .. py:attribute:: CAN_ATTACH_TO
      :value: "CAN_ATTACH_TO"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

.. autoclass:: InstancePoolPermissions
   :members:
   :undoc-members:

.. autoclass:: InstancePoolPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: InstancePoolPermissionsRequest
   :members:
   :undoc-members:

.. py:class:: InstancePoolState

   The state of a Cluster. The current allowable state transitions are as follows:
   - ``ACTIVE`` -> ``STOPPED`` - ``ACTIVE`` -> ``DELETED`` - ``STOPPED`` -> ``ACTIVE`` - ``STOPPED`` -> ``DELETED``

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

.. autoclass:: InstancePoolStats
   :members:
   :undoc-members:

.. autoclass:: InstancePoolStatus
   :members:
   :undoc-members:

.. autoclass:: InstanceProfile
   :members:
   :undoc-members:

.. py:class:: Kind

   The kind of compute described by this compute specification.
   Depending on `kind`, different validations and default values will be applied.
   Clusters with `kind = CLASSIC_PREVIEW` support the following fields, whereas clusters with no specified `kind` do not. * [is_single_node](/api/workspace/clusters/create#is_single_node) * [use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime) * [data_security_mode](/api/workspace/clusters/create#data_security_mode) set to `DATA_SECURITY_MODE_AUTO`, `DATA_SECURITY_MODE_DEDICATED`, or `DATA_SECURITY_MODE_STANDARD`
   By using the [simple form], your clusters are automatically using `kind = CLASSIC_PREVIEW`.
   [simple form]: https://docs.databricks.com/compute/simple-form.html

   .. py:attribute:: CLASSIC_PREVIEW
      :value: "CLASSIC_PREVIEW"

.. py:class:: Language

   .. py:attribute:: PYTHON
      :value: "PYTHON"

   .. py:attribute:: SCALA
      :value: "SCALA"

   .. py:attribute:: SQL
      :value: "SQL"

.. autoclass:: Library
   :members:
   :undoc-members:

.. autoclass:: LibraryFullStatus
   :members:
   :undoc-members:

.. py:class:: LibraryInstallStatus

   The status of a library on a specific cluster.

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: INSTALLED
      :value: "INSTALLED"

   .. py:attribute:: INSTALLING
      :value: "INSTALLING"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RESOLVING
      :value: "RESOLVING"

   .. py:attribute:: RESTORED
      :value: "RESTORED"

   .. py:attribute:: SKIPPED
      :value: "SKIPPED"

   .. py:attribute:: UNINSTALL_ON_RESTART
      :value: "UNINSTALL_ON_RESTART"

.. autoclass:: ListAllClusterLibraryStatusesResponse
   :members:
   :undoc-members:

.. autoclass:: ListAvailableZonesResponse
   :members:
   :undoc-members:

.. autoclass:: ListClusterCompliancesResponse
   :members:
   :undoc-members:

.. autoclass:: ListClustersFilterBy
   :members:
   :undoc-members:

.. autoclass:: ListClustersResponse
   :members:
   :undoc-members:

.. autoclass:: ListClustersSortBy
   :members:
   :undoc-members:

.. py:class:: ListClustersSortByDirection

   .. py:attribute:: ASC
      :value: "ASC"

   .. py:attribute:: DESC
      :value: "DESC"

.. py:class:: ListClustersSortByField

   .. py:attribute:: CLUSTER_NAME
      :value: "CLUSTER_NAME"

   .. py:attribute:: DEFAULT
      :value: "DEFAULT"

.. autoclass:: ListGlobalInitScriptsResponse
   :members:
   :undoc-members:

.. autoclass:: ListInstancePools
   :members:
   :undoc-members:

.. autoclass:: ListInstanceProfilesResponse
   :members:
   :undoc-members:

.. autoclass:: ListNodeTypesResponse
   :members:
   :undoc-members:

.. autoclass:: ListPoliciesResponse
   :members:
   :undoc-members:

.. autoclass:: ListPolicyFamiliesResponse
   :members:
   :undoc-members:

.. py:class:: ListSortColumn

   .. py:attribute:: POLICY_CREATION_TIME
      :value: "POLICY_CREATION_TIME"

   .. py:attribute:: POLICY_NAME
      :value: "POLICY_NAME"

.. py:class:: ListSortOrder

   .. py:attribute:: ASC
      :value: "ASC"

   .. py:attribute:: DESC
      :value: "DESC"

.. autoclass:: LocalFileInfo
   :members:
   :undoc-members:

.. autoclass:: LogAnalyticsInfo
   :members:
   :undoc-members:

.. autoclass:: LogSyncStatus
   :members:
   :undoc-members:

.. autoclass:: MavenLibrary
   :members:
   :undoc-members:

.. autoclass:: NodeInstanceType
   :members:
   :undoc-members:

.. autoclass:: NodeType
   :members:
   :undoc-members:

.. autoclass:: PendingInstanceError
   :members:
   :undoc-members:

.. autoclass:: PermanentDeleteCluster
   :members:
   :undoc-members:

.. autoclass:: PermanentDeleteClusterResponse
   :members:
   :undoc-members:

.. autoclass:: PinCluster
   :members:
   :undoc-members:

.. autoclass:: PinClusterResponse
   :members:
   :undoc-members:

.. autoclass:: Policy
   :members:
   :undoc-members:

.. autoclass:: PolicyFamily
   :members:
   :undoc-members:

.. autoclass:: PythonPyPiLibrary
   :members:
   :undoc-members:

.. autoclass:: RCranLibrary
   :members:
   :undoc-members:

.. autoclass:: RemoveInstanceProfile
   :members:
   :undoc-members:

.. autoclass:: RemoveResponse
   :members:
   :undoc-members:

.. autoclass:: ResizeCluster
   :members:
   :undoc-members:

.. autoclass:: ResizeClusterResponse
   :members:
   :undoc-members:

.. autoclass:: RestartCluster
   :members:
   :undoc-members:

.. autoclass:: RestartClusterResponse
   :members:
   :undoc-members:

.. py:class:: ResultType

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: IMAGE
      :value: "IMAGE"

   .. py:attribute:: IMAGES
      :value: "IMAGES"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: TEXT
      :value: "TEXT"

.. autoclass:: Results
   :members:
   :undoc-members:

.. py:class:: RuntimeEngine

   .. py:attribute:: NULL
      :value: "NULL"

   .. py:attribute:: PHOTON
      :value: "PHOTON"

   .. py:attribute:: STANDARD
      :value: "STANDARD"

.. autoclass:: S3StorageInfo
   :members:
   :undoc-members:

.. autoclass:: SparkNode
   :members:
   :undoc-members:

.. autoclass:: SparkNodeAwsAttributes
   :members:
   :undoc-members:

.. autoclass:: SparkVersion
   :members:
   :undoc-members:

.. autoclass:: StartCluster
   :members:
   :undoc-members:

.. autoclass:: StartClusterResponse
   :members:
   :undoc-members:

.. py:class:: State

   The state of a Cluster. The current allowable state transitions are as follows:
   - `PENDING` -> `RUNNING` - `PENDING` -> `TERMINATING` - `RUNNING` -> `RESIZING` - `RUNNING` -> `RESTARTING` - `RUNNING` -> `TERMINATING` - `RESTARTING` -> `RUNNING` - `RESTARTING` -> `TERMINATING` - `RESIZING` -> `RUNNING` - `RESIZING` -> `TERMINATING` - `TERMINATING` -> `TERMINATED`

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RESIZING
      :value: "RESIZING"

   .. py:attribute:: RESTARTING
      :value: "RESTARTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: TERMINATED
      :value: "TERMINATED"

   .. py:attribute:: TERMINATING
      :value: "TERMINATING"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. autoclass:: TerminationReason
   :members:
   :undoc-members:

.. py:class:: TerminationReasonCode

   The status code indicating why the cluster was terminated

   .. py:attribute:: ABUSE_DETECTED
      :value: "ABUSE_DETECTED"

   .. py:attribute:: ACCESS_TOKEN_FAILURE
      :value: "ACCESS_TOKEN_FAILURE"

   .. py:attribute:: ALLOCATION_TIMEOUT
      :value: "ALLOCATION_TIMEOUT"

   .. py:attribute:: ALLOCATION_TIMEOUT_NODE_DAEMON_NOT_READY
      :value: "ALLOCATION_TIMEOUT_NODE_DAEMON_NOT_READY"

   .. py:attribute:: ALLOCATION_TIMEOUT_NO_HEALTHY_AND_WARMED_UP_CLUSTERS
      :value: "ALLOCATION_TIMEOUT_NO_HEALTHY_AND_WARMED_UP_CLUSTERS"

   .. py:attribute:: ALLOCATION_TIMEOUT_NO_HEALTHY_CLUSTERS
      :value: "ALLOCATION_TIMEOUT_NO_HEALTHY_CLUSTERS"

   .. py:attribute:: ALLOCATION_TIMEOUT_NO_MATCHED_CLUSTERS
      :value: "ALLOCATION_TIMEOUT_NO_MATCHED_CLUSTERS"

   .. py:attribute:: ALLOCATION_TIMEOUT_NO_READY_CLUSTERS
      :value: "ALLOCATION_TIMEOUT_NO_READY_CLUSTERS"

   .. py:attribute:: ALLOCATION_TIMEOUT_NO_UNALLOCATED_CLUSTERS
      :value: "ALLOCATION_TIMEOUT_NO_UNALLOCATED_CLUSTERS"

   .. py:attribute:: ALLOCATION_TIMEOUT_NO_WARMED_UP_CLUSTERS
      :value: "ALLOCATION_TIMEOUT_NO_WARMED_UP_CLUSTERS"

   .. py:attribute:: ATTACH_PROJECT_FAILURE
      :value: "ATTACH_PROJECT_FAILURE"

   .. py:attribute:: AWS_AUTHORIZATION_FAILURE
      :value: "AWS_AUTHORIZATION_FAILURE"

   .. py:attribute:: AWS_INACCESSIBLE_KMS_KEY_FAILURE
      :value: "AWS_INACCESSIBLE_KMS_KEY_FAILURE"

   .. py:attribute:: AWS_INSTANCE_PROFILE_UPDATE_FAILURE
      :value: "AWS_INSTANCE_PROFILE_UPDATE_FAILURE"

   .. py:attribute:: AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE
      :value: "AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE"

   .. py:attribute:: AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE
      :value: "AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE"

   .. py:attribute:: AWS_INVALID_KEY_PAIR
      :value: "AWS_INVALID_KEY_PAIR"

   .. py:attribute:: AWS_INVALID_KMS_KEY_STATE
      :value: "AWS_INVALID_KMS_KEY_STATE"

   .. py:attribute:: AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE
      :value: "AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE"

   .. py:attribute:: AWS_REQUEST_LIMIT_EXCEEDED
      :value: "AWS_REQUEST_LIMIT_EXCEEDED"

   .. py:attribute:: AWS_RESOURCE_QUOTA_EXCEEDED
      :value: "AWS_RESOURCE_QUOTA_EXCEEDED"

   .. py:attribute:: AWS_UNSUPPORTED_FAILURE
      :value: "AWS_UNSUPPORTED_FAILURE"

   .. py:attribute:: AZURE_BYOK_KEY_PERMISSION_FAILURE
      :value: "AZURE_BYOK_KEY_PERMISSION_FAILURE"

   .. py:attribute:: AZURE_EPHEMERAL_DISK_FAILURE
      :value: "AZURE_EPHEMERAL_DISK_FAILURE"

   .. py:attribute:: AZURE_INVALID_DEPLOYMENT_TEMPLATE
      :value: "AZURE_INVALID_DEPLOYMENT_TEMPLATE"

   .. py:attribute:: AZURE_OPERATION_NOT_ALLOWED_EXCEPTION
      :value: "AZURE_OPERATION_NOT_ALLOWED_EXCEPTION"

   .. py:attribute:: AZURE_PACKED_DEPLOYMENT_PARTIAL_FAILURE
      :value: "AZURE_PACKED_DEPLOYMENT_PARTIAL_FAILURE"

   .. py:attribute:: AZURE_QUOTA_EXCEEDED_EXCEPTION
      :value: "AZURE_QUOTA_EXCEEDED_EXCEPTION"

   .. py:attribute:: AZURE_RESOURCE_MANAGER_THROTTLING
      :value: "AZURE_RESOURCE_MANAGER_THROTTLING"

   .. py:attribute:: AZURE_RESOURCE_PROVIDER_THROTTLING
      :value: "AZURE_RESOURCE_PROVIDER_THROTTLING"

   .. py:attribute:: AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE
      :value: "AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE"

   .. py:attribute:: AZURE_VM_EXTENSION_FAILURE
      :value: "AZURE_VM_EXTENSION_FAILURE"

   .. py:attribute:: AZURE_VNET_CONFIGURATION_FAILURE
      :value: "AZURE_VNET_CONFIGURATION_FAILURE"

   .. py:attribute:: BOOTSTRAP_TIMEOUT
      :value: "BOOTSTRAP_TIMEOUT"

   .. py:attribute:: BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION
      :value: "BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION"

   .. py:attribute:: BOOTSTRAP_TIMEOUT_DUE_TO_MISCONFIG
      :value: "BOOTSTRAP_TIMEOUT_DUE_TO_MISCONFIG"

   .. py:attribute:: BUDGET_POLICY_LIMIT_ENFORCEMENT_ACTIVATED
      :value: "BUDGET_POLICY_LIMIT_ENFORCEMENT_ACTIVATED"

   .. py:attribute:: BUDGET_POLICY_RESOLUTION_FAILURE
      :value: "BUDGET_POLICY_RESOLUTION_FAILURE"

   .. py:attribute:: CLOUD_ACCOUNT_SETUP_FAILURE
      :value: "CLOUD_ACCOUNT_SETUP_FAILURE"

   .. py:attribute:: CLOUD_OPERATION_CANCELLED
      :value: "CLOUD_OPERATION_CANCELLED"

   .. py:attribute:: CLOUD_PROVIDER_DISK_SETUP_FAILURE
      :value: "CLOUD_PROVIDER_DISK_SETUP_FAILURE"

   .. py:attribute:: CLOUD_PROVIDER_INSTANCE_NOT_LAUNCHED
      :value: "CLOUD_PROVIDER_INSTANCE_NOT_LAUNCHED"

   .. py:attribute:: CLOUD_PROVIDER_LAUNCH_FAILURE
      :value: "CLOUD_PROVIDER_LAUNCH_FAILURE"

   .. py:attribute:: CLOUD_PROVIDER_LAUNCH_FAILURE_DUE_TO_MISCONFIG
      :value: "CLOUD_PROVIDER_LAUNCH_FAILURE_DUE_TO_MISCONFIG"

   .. py:attribute:: CLOUD_PROVIDER_RESOURCE_STOCKOUT
      :value: "CLOUD_PROVIDER_RESOURCE_STOCKOUT"

   .. py:attribute:: CLOUD_PROVIDER_RESOURCE_STOCKOUT_DUE_TO_MISCONFIG
      :value: "CLOUD_PROVIDER_RESOURCE_STOCKOUT_DUE_TO_MISCONFIG"

   .. py:attribute:: CLOUD_PROVIDER_SHUTDOWN
      :value: "CLOUD_PROVIDER_SHUTDOWN"

   .. py:attribute:: CLUSTER_OPERATION_THROTTLED
      :value: "CLUSTER_OPERATION_THROTTLED"

   .. py:attribute:: CLUSTER_OPERATION_TIMEOUT
      :value: "CLUSTER_OPERATION_TIMEOUT"

   .. py:attribute:: COMMUNICATION_LOST
      :value: "COMMUNICATION_LOST"

   .. py:attribute:: CONTAINER_LAUNCH_FAILURE
      :value: "CONTAINER_LAUNCH_FAILURE"

   .. py:attribute:: CONTROL_PLANE_REQUEST_FAILURE
      :value: "CONTROL_PLANE_REQUEST_FAILURE"

   .. py:attribute:: CONTROL_PLANE_REQUEST_FAILURE_DUE_TO_MISCONFIG
      :value: "CONTROL_PLANE_REQUEST_FAILURE_DUE_TO_MISCONFIG"

   .. py:attribute:: DATABASE_CONNECTION_FAILURE
      :value: "DATABASE_CONNECTION_FAILURE"

   .. py:attribute:: DATA_ACCESS_CONFIG_CHANGED
      :value: "DATA_ACCESS_CONFIG_CHANGED"

   .. py:attribute:: DBFS_COMPONENT_UNHEALTHY
      :value: "DBFS_COMPONENT_UNHEALTHY"

   .. py:attribute:: DISASTER_RECOVERY_REPLICATION
      :value: "DISASTER_RECOVERY_REPLICATION"

   .. py:attribute:: DNS_RESOLUTION_ERROR
      :value: "DNS_RESOLUTION_ERROR"

   .. py:attribute:: DOCKER_CONTAINER_CREATION_EXCEPTION
      :value: "DOCKER_CONTAINER_CREATION_EXCEPTION"

   .. py:attribute:: DOCKER_IMAGE_PULL_FAILURE
      :value: "DOCKER_IMAGE_PULL_FAILURE"

   .. py:attribute:: DOCKER_IMAGE_TOO_LARGE_FOR_INSTANCE_EXCEPTION
      :value: "DOCKER_IMAGE_TOO_LARGE_FOR_INSTANCE_EXCEPTION"

   .. py:attribute:: DOCKER_INVALID_OS_EXCEPTION
      :value: "DOCKER_INVALID_OS_EXCEPTION"

   .. py:attribute:: DRIVER_EVICTION
      :value: "DRIVER_EVICTION"

   .. py:attribute:: DRIVER_LAUNCH_TIMEOUT
      :value: "DRIVER_LAUNCH_TIMEOUT"

   .. py:attribute:: DRIVER_NODE_UNREACHABLE
      :value: "DRIVER_NODE_UNREACHABLE"

   .. py:attribute:: DRIVER_OUT_OF_DISK
      :value: "DRIVER_OUT_OF_DISK"

   .. py:attribute:: DRIVER_OUT_OF_MEMORY
      :value: "DRIVER_OUT_OF_MEMORY"

   .. py:attribute:: DRIVER_POD_CREATION_FAILURE
      :value: "DRIVER_POD_CREATION_FAILURE"

   .. py:attribute:: DRIVER_UNEXPECTED_FAILURE
      :value: "DRIVER_UNEXPECTED_FAILURE"

   .. py:attribute:: DRIVER_UNREACHABLE
      :value: "DRIVER_UNREACHABLE"

   .. py:attribute:: DRIVER_UNRESPONSIVE
      :value: "DRIVER_UNRESPONSIVE"

   .. py:attribute:: DYNAMIC_SPARK_CONF_SIZE_EXCEEDED
      :value: "DYNAMIC_SPARK_CONF_SIZE_EXCEEDED"

   .. py:attribute:: EOS_SPARK_IMAGE
      :value: "EOS_SPARK_IMAGE"

   .. py:attribute:: EXECUTION_COMPONENT_UNHEALTHY
      :value: "EXECUTION_COMPONENT_UNHEALTHY"

   .. py:attribute:: EXECUTOR_POD_UNSCHEDULED
      :value: "EXECUTOR_POD_UNSCHEDULED"

   .. py:attribute:: GCP_API_RATE_QUOTA_EXCEEDED
      :value: "GCP_API_RATE_QUOTA_EXCEEDED"

   .. py:attribute:: GCP_DENIED_BY_ORG_POLICY
      :value: "GCP_DENIED_BY_ORG_POLICY"

   .. py:attribute:: GCP_FORBIDDEN
      :value: "GCP_FORBIDDEN"

   .. py:attribute:: GCP_IAM_TIMEOUT
      :value: "GCP_IAM_TIMEOUT"

   .. py:attribute:: GCP_INACCESSIBLE_KMS_KEY_FAILURE
      :value: "GCP_INACCESSIBLE_KMS_KEY_FAILURE"

   .. py:attribute:: GCP_INSUFFICIENT_CAPACITY
      :value: "GCP_INSUFFICIENT_CAPACITY"

   .. py:attribute:: GCP_IP_SPACE_EXHAUSTED
      :value: "GCP_IP_SPACE_EXHAUSTED"

   .. py:attribute:: GCP_KMS_KEY_PERMISSION_DENIED
      :value: "GCP_KMS_KEY_PERMISSION_DENIED"

   .. py:attribute:: GCP_NOT_FOUND
      :value: "GCP_NOT_FOUND"

   .. py:attribute:: GCP_QUOTA_EXCEEDED
      :value: "GCP_QUOTA_EXCEEDED"

   .. py:attribute:: GCP_RESOURCE_QUOTA_EXCEEDED
      :value: "GCP_RESOURCE_QUOTA_EXCEEDED"

   .. py:attribute:: GCP_SERVICE_ACCOUNT_ACCESS_DENIED
      :value: "GCP_SERVICE_ACCOUNT_ACCESS_DENIED"

   .. py:attribute:: GCP_SERVICE_ACCOUNT_DELETED
      :value: "GCP_SERVICE_ACCOUNT_DELETED"

   .. py:attribute:: GCP_SERVICE_ACCOUNT_NOT_FOUND
      :value: "GCP_SERVICE_ACCOUNT_NOT_FOUND"

   .. py:attribute:: GCP_SUBNET_NOT_READY
      :value: "GCP_SUBNET_NOT_READY"

   .. py:attribute:: GCP_TRUSTED_IMAGE_PROJECTS_VIOLATED
      :value: "GCP_TRUSTED_IMAGE_PROJECTS_VIOLATED"

   .. py:attribute:: GKE_BASED_CLUSTER_TERMINATION
      :value: "GKE_BASED_CLUSTER_TERMINATION"

   .. py:attribute:: GLOBAL_INIT_SCRIPT_FAILURE
      :value: "GLOBAL_INIT_SCRIPT_FAILURE"

   .. py:attribute:: HIVE_METASTORE_PROVISIONING_FAILURE
      :value: "HIVE_METASTORE_PROVISIONING_FAILURE"

   .. py:attribute:: IMAGE_PULL_PERMISSION_DENIED
      :value: "IMAGE_PULL_PERMISSION_DENIED"

   .. py:attribute:: INACTIVITY
      :value: "INACTIVITY"

   .. py:attribute:: INIT_CONTAINER_NOT_FINISHED
      :value: "INIT_CONTAINER_NOT_FINISHED"

   .. py:attribute:: INIT_SCRIPT_FAILURE
      :value: "INIT_SCRIPT_FAILURE"

   .. py:attribute:: INSTANCE_POOL_CLUSTER_FAILURE
      :value: "INSTANCE_POOL_CLUSTER_FAILURE"

   .. py:attribute:: INSTANCE_POOL_MAX_CAPACITY_REACHED
      :value: "INSTANCE_POOL_MAX_CAPACITY_REACHED"

   .. py:attribute:: INSTANCE_POOL_NOT_FOUND
      :value: "INSTANCE_POOL_NOT_FOUND"

   .. py:attribute:: INSTANCE_UNREACHABLE
      :value: "INSTANCE_UNREACHABLE"

   .. py:attribute:: INSTANCE_UNREACHABLE_DUE_TO_MISCONFIG
      :value: "INSTANCE_UNREACHABLE_DUE_TO_MISCONFIG"

   .. py:attribute:: INTERNAL_CAPACITY_FAILURE
      :value: "INTERNAL_CAPACITY_FAILURE"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: INVALID_ARGUMENT
      :value: "INVALID_ARGUMENT"

   .. py:attribute:: INVALID_AWS_PARAMETER
      :value: "INVALID_AWS_PARAMETER"

   .. py:attribute:: INVALID_INSTANCE_PLACEMENT_PROTOCOL
      :value: "INVALID_INSTANCE_PLACEMENT_PROTOCOL"

   .. py:attribute:: INVALID_SPARK_IMAGE
      :value: "INVALID_SPARK_IMAGE"

   .. py:attribute:: INVALID_WORKER_IMAGE_FAILURE
      :value: "INVALID_WORKER_IMAGE_FAILURE"

   .. py:attribute:: IN_PENALTY_BOX
      :value: "IN_PENALTY_BOX"

   .. py:attribute:: IP_EXHAUSTION_FAILURE
      :value: "IP_EXHAUSTION_FAILURE"

   .. py:attribute:: JOB_FINISHED
      :value: "JOB_FINISHED"

   .. py:attribute:: K8S_AUTOSCALING_FAILURE
      :value: "K8S_AUTOSCALING_FAILURE"

   .. py:attribute:: K8S_DBR_CLUSTER_LAUNCH_TIMEOUT
      :value: "K8S_DBR_CLUSTER_LAUNCH_TIMEOUT"

   .. py:attribute:: LAZY_ALLOCATION_TIMEOUT
      :value: "LAZY_ALLOCATION_TIMEOUT"

   .. py:attribute:: MAINTENANCE_MODE
      :value: "MAINTENANCE_MODE"

   .. py:attribute:: METASTORE_COMPONENT_UNHEALTHY
      :value: "METASTORE_COMPONENT_UNHEALTHY"

   .. py:attribute:: NEPHOS_RESOURCE_MANAGEMENT
      :value: "NEPHOS_RESOURCE_MANAGEMENT"

   .. py:attribute:: NETVISOR_SETUP_TIMEOUT
      :value: "NETVISOR_SETUP_TIMEOUT"

   .. py:attribute:: NETWORK_CHECK_CONTROL_PLANE_FAILURE
      :value: "NETWORK_CHECK_CONTROL_PLANE_FAILURE"

   .. py:attribute:: NETWORK_CHECK_DNS_SERVER_FAILURE
      :value: "NETWORK_CHECK_DNS_SERVER_FAILURE"

   .. py:attribute:: NETWORK_CHECK_METADATA_ENDPOINT_FAILURE
      :value: "NETWORK_CHECK_METADATA_ENDPOINT_FAILURE"

   .. py:attribute:: NETWORK_CHECK_MULTIPLE_COMPONENTS_FAILURE
      :value: "NETWORK_CHECK_MULTIPLE_COMPONENTS_FAILURE"

   .. py:attribute:: NETWORK_CHECK_NIC_FAILURE
      :value: "NETWORK_CHECK_NIC_FAILURE"

   .. py:attribute:: NETWORK_CHECK_STORAGE_FAILURE
      :value: "NETWORK_CHECK_STORAGE_FAILURE"

   .. py:attribute:: NETWORK_CONFIGURATION_FAILURE
      :value: "NETWORK_CONFIGURATION_FAILURE"

   .. py:attribute:: NFS_MOUNT_FAILURE
      :value: "NFS_MOUNT_FAILURE"

   .. py:attribute:: NO_MATCHED_K8S
      :value: "NO_MATCHED_K8S"

   .. py:attribute:: NO_MATCHED_K8S_TESTING_TAG
      :value: "NO_MATCHED_K8S_TESTING_TAG"

   .. py:attribute:: NPIP_TUNNEL_SETUP_FAILURE
      :value: "NPIP_TUNNEL_SETUP_FAILURE"

   .. py:attribute:: NPIP_TUNNEL_TOKEN_FAILURE
      :value: "NPIP_TUNNEL_TOKEN_FAILURE"

   .. py:attribute:: POD_ASSIGNMENT_FAILURE
      :value: "POD_ASSIGNMENT_FAILURE"

   .. py:attribute:: POD_SCHEDULING_FAILURE
      :value: "POD_SCHEDULING_FAILURE"

   .. py:attribute:: REQUEST_REJECTED
      :value: "REQUEST_REJECTED"

   .. py:attribute:: REQUEST_THROTTLED
      :value: "REQUEST_THROTTLED"

   .. py:attribute:: RESOURCE_USAGE_BLOCKED
      :value: "RESOURCE_USAGE_BLOCKED"

   .. py:attribute:: SECRET_CREATION_FAILURE
      :value: "SECRET_CREATION_FAILURE"

   .. py:attribute:: SECRET_PERMISSION_DENIED
      :value: "SECRET_PERMISSION_DENIED"

   .. py:attribute:: SECRET_RESOLUTION_ERROR
      :value: "SECRET_RESOLUTION_ERROR"

   .. py:attribute:: SECURITY_DAEMON_REGISTRATION_EXCEPTION
      :value: "SECURITY_DAEMON_REGISTRATION_EXCEPTION"

   .. py:attribute:: SELF_BOOTSTRAP_FAILURE
      :value: "SELF_BOOTSTRAP_FAILURE"

   .. py:attribute:: SERVERLESS_LONG_RUNNING_TERMINATED
      :value: "SERVERLESS_LONG_RUNNING_TERMINATED"

   .. py:attribute:: SKIPPED_SLOW_NODES
      :value: "SKIPPED_SLOW_NODES"

   .. py:attribute:: SLOW_IMAGE_DOWNLOAD
      :value: "SLOW_IMAGE_DOWNLOAD"

   .. py:attribute:: SPARK_ERROR
      :value: "SPARK_ERROR"

   .. py:attribute:: SPARK_IMAGE_DOWNLOAD_FAILURE
      :value: "SPARK_IMAGE_DOWNLOAD_FAILURE"

   .. py:attribute:: SPARK_IMAGE_DOWNLOAD_THROTTLED
      :value: "SPARK_IMAGE_DOWNLOAD_THROTTLED"

   .. py:attribute:: SPARK_IMAGE_NOT_FOUND
      :value: "SPARK_IMAGE_NOT_FOUND"

   .. py:attribute:: SPARK_STARTUP_FAILURE
      :value: "SPARK_STARTUP_FAILURE"

   .. py:attribute:: SPOT_INSTANCE_TERMINATION
      :value: "SPOT_INSTANCE_TERMINATION"

   .. py:attribute:: SSH_BOOTSTRAP_FAILURE
      :value: "SSH_BOOTSTRAP_FAILURE"

   .. py:attribute:: STORAGE_DOWNLOAD_FAILURE
      :value: "STORAGE_DOWNLOAD_FAILURE"

   .. py:attribute:: STORAGE_DOWNLOAD_FAILURE_DUE_TO_MISCONFIG
      :value: "STORAGE_DOWNLOAD_FAILURE_DUE_TO_MISCONFIG"

   .. py:attribute:: STORAGE_DOWNLOAD_FAILURE_SLOW
      :value: "STORAGE_DOWNLOAD_FAILURE_SLOW"

   .. py:attribute:: STORAGE_DOWNLOAD_FAILURE_THROTTLED
      :value: "STORAGE_DOWNLOAD_FAILURE_THROTTLED"

   .. py:attribute:: STS_CLIENT_SETUP_FAILURE
      :value: "STS_CLIENT_SETUP_FAILURE"

   .. py:attribute:: SUBNET_EXHAUSTED_FAILURE
      :value: "SUBNET_EXHAUSTED_FAILURE"

   .. py:attribute:: TEMPORARILY_UNAVAILABLE
      :value: "TEMPORARILY_UNAVAILABLE"

   .. py:attribute:: TRIAL_EXPIRED
      :value: "TRIAL_EXPIRED"

   .. py:attribute:: UNEXPECTED_LAUNCH_FAILURE
      :value: "UNEXPECTED_LAUNCH_FAILURE"

   .. py:attribute:: UNEXPECTED_POD_RECREATION
      :value: "UNEXPECTED_POD_RECREATION"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: UNSUPPORTED_INSTANCE_TYPE
      :value: "UNSUPPORTED_INSTANCE_TYPE"

   .. py:attribute:: UPDATE_INSTANCE_PROFILE_FAILURE
      :value: "UPDATE_INSTANCE_PROFILE_FAILURE"

   .. py:attribute:: USER_INITIATED_VM_TERMINATION
      :value: "USER_INITIATED_VM_TERMINATION"

   .. py:attribute:: USER_REQUEST
      :value: "USER_REQUEST"

   .. py:attribute:: WORKER_SETUP_FAILURE
      :value: "WORKER_SETUP_FAILURE"

   .. py:attribute:: WORKSPACE_CANCELLED_ERROR
      :value: "WORKSPACE_CANCELLED_ERROR"

   .. py:attribute:: WORKSPACE_CONFIGURATION_ERROR
      :value: "WORKSPACE_CONFIGURATION_ERROR"

   .. py:attribute:: WORKSPACE_UPDATE
      :value: "WORKSPACE_UPDATE"

.. py:class:: TerminationReasonType

   type of the termination

   .. py:attribute:: CLIENT_ERROR
      :value: "CLIENT_ERROR"

   .. py:attribute:: CLOUD_FAILURE
      :value: "CLOUD_FAILURE"

   .. py:attribute:: SERVICE_FAULT
      :value: "SERVICE_FAULT"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. autoclass:: UninstallLibraries
   :members:
   :undoc-members:

.. autoclass:: UninstallLibrariesResponse
   :members:
   :undoc-members:

.. autoclass:: UnpinCluster
   :members:
   :undoc-members:

.. autoclass:: UnpinClusterResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateCluster
   :members:
   :undoc-members:

.. autoclass:: UpdateClusterResource
   :members:
   :undoc-members:

.. autoclass:: UpdateClusterResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: VolumesStorageInfo
   :members:
   :undoc-members:

.. autoclass:: WorkloadType
   :members:
   :undoc-members:

.. autoclass:: WorkspaceStorageInfo
   :members:
   :undoc-members:

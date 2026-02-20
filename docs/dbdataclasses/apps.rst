Apps
====

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.apps`` module.

.. py:currentmodule:: databricks.sdk.service.apps
.. autoclass:: App
   :members:
   :undoc-members:

.. autoclass:: AppAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: AppAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: AppDeployment
   :members:
   :undoc-members:

.. autoclass:: AppDeploymentArtifacts
   :members:
   :undoc-members:

.. py:class:: AppDeploymentMode

   .. py:attribute:: AUTO_SYNC
      :value: "AUTO_SYNC"

   .. py:attribute:: SNAPSHOT
      :value: "SNAPSHOT"

.. py:class:: AppDeploymentState

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: AppDeploymentStatus
   :members:
   :undoc-members:

.. autoclass:: AppManifest
   :members:
   :undoc-members:

.. autoclass:: AppManifestAppResourceExperimentSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceExperimentSpecExperimentPermission

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

.. autoclass:: AppManifestAppResourceJobSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceJobSpecJobPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_RUN
      :value: "CAN_MANAGE_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppManifestAppResourceSecretSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceSecretSpecSecretPermission

   Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE".

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. autoclass:: AppManifestAppResourceServingEndpointSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceServingEndpointSpecServingEndpointPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: AppManifestAppResourceSpec
   :members:
   :undoc-members:

.. autoclass:: AppManifestAppResourceSqlWarehouseSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceSqlWarehouseSpecSqlWarehousePermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppManifestAppResourceUcSecurableSpec
   :members:
   :undoc-members:

.. py:class:: AppManifestAppResourceUcSecurableSpecUcSecurablePermission

   .. py:attribute:: EXECUTE
      :value: "EXECUTE"

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: SELECT
      :value: "SELECT"

   .. py:attribute:: USE_CONNECTION
      :value: "USE_CONNECTION"

   .. py:attribute:: WRITE_VOLUME
      :value: "WRITE_VOLUME"

.. py:class:: AppManifestAppResourceUcSecurableSpecUcSecurableType

   .. py:attribute:: CONNECTION
      :value: "CONNECTION"

   .. py:attribute:: FUNCTION
      :value: "FUNCTION"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: AppPermission
   :members:
   :undoc-members:

.. py:class:: AppPermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

.. autoclass:: AppPermissions
   :members:
   :undoc-members:

.. autoclass:: AppPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: AppResource
   :members:
   :undoc-members:

.. autoclass:: AppResourceApp
   :members:
   :undoc-members:

.. autoclass:: AppResourceDatabase
   :members:
   :undoc-members:

.. py:class:: AppResourceDatabaseDatabasePermission

   .. py:attribute:: CAN_CONNECT_AND_CREATE
      :value: "CAN_CONNECT_AND_CREATE"

.. autoclass:: AppResourceExperiment
   :members:
   :undoc-members:

.. py:class:: AppResourceExperimentExperimentPermission

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_READ
      :value: "CAN_READ"

.. autoclass:: AppResourceGenieSpace
   :members:
   :undoc-members:

.. py:class:: AppResourceGenieSpaceGenieSpacePermission

   .. py:attribute:: CAN_EDIT
      :value: "CAN_EDIT"

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: AppResourceJob
   :members:
   :undoc-members:

.. py:class:: AppResourceJobJobPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_MANAGE_RUN
      :value: "CAN_MANAGE_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppResourceSecret
   :members:
   :undoc-members:

.. py:class:: AppResourceSecretSecretPermission

   Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE".

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. autoclass:: AppResourceServingEndpoint
   :members:
   :undoc-members:

.. py:class:: AppResourceServingEndpointServingEndpointPermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_QUERY
      :value: "CAN_QUERY"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

.. autoclass:: AppResourceSqlWarehouse
   :members:
   :undoc-members:

.. py:class:: AppResourceSqlWarehouseSqlWarehousePermission

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: AppResourceUcSecurable
   :members:
   :undoc-members:

.. py:class:: AppResourceUcSecurableUcSecurablePermission

   .. py:attribute:: EXECUTE
      :value: "EXECUTE"

   .. py:attribute:: MODIFY
      :value: "MODIFY"

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: SELECT
      :value: "SELECT"

   .. py:attribute:: USE_CONNECTION
      :value: "USE_CONNECTION"

   .. py:attribute:: WRITE_VOLUME
      :value: "WRITE_VOLUME"

.. py:class:: AppResourceUcSecurableUcSecurableType

   .. py:attribute:: CONNECTION
      :value: "CONNECTION"

   .. py:attribute:: FUNCTION
      :value: "FUNCTION"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: AppUpdate
   :members:
   :undoc-members:

.. autoclass:: AppUpdateUpdateStatus
   :members:
   :undoc-members:

.. py:class:: AppUpdateUpdateStatusUpdateState

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: NOT_UPDATED
      :value: "NOT_UPDATED"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. py:class:: ApplicationState

   .. py:attribute:: CRASHED
      :value: "CRASHED"

   .. py:attribute:: DEPLOYING
      :value: "DEPLOYING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: UNAVAILABLE
      :value: "UNAVAILABLE"

.. autoclass:: ApplicationStatus
   :members:
   :undoc-members:

.. py:class:: ComputeSize

   .. py:attribute:: LARGE
      :value: "LARGE"

   .. py:attribute:: MEDIUM
      :value: "MEDIUM"

.. py:class:: ComputeState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPED
      :value: "STOPPED"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

   .. py:attribute:: UPDATING
      :value: "UPDATING"

.. autoclass:: ComputeStatus
   :members:
   :undoc-members:

.. autoclass:: CustomTemplate
   :members:
   :undoc-members:

.. autoclass:: DatabricksServiceExceptionWithDetailsProto
   :members:
   :undoc-members:

.. autoclass:: EnvVar
   :members:
   :undoc-members:

.. py:class:: ErrorCode

   Error codes returned by Databricks APIs to indicate specific failure conditions.

   .. py:attribute:: ABORTED
      :value: "ABORTED"

   .. py:attribute:: ALREADY_EXISTS
      :value: "ALREADY_EXISTS"

   .. py:attribute:: BAD_REQUEST
      :value: "BAD_REQUEST"

   .. py:attribute:: CANCELLED
      :value: "CANCELLED"

   .. py:attribute:: CATALOG_ALREADY_EXISTS
      :value: "CATALOG_ALREADY_EXISTS"

   .. py:attribute:: CATALOG_DOES_NOT_EXIST
      :value: "CATALOG_DOES_NOT_EXIST"

   .. py:attribute:: CATALOG_NOT_EMPTY
      :value: "CATALOG_NOT_EMPTY"

   .. py:attribute:: COULD_NOT_ACQUIRE_LOCK
      :value: "COULD_NOT_ACQUIRE_LOCK"

   .. py:attribute:: CUSTOMER_UNAUTHORIZED
      :value: "CUSTOMER_UNAUTHORIZED"

   .. py:attribute:: DAC_ALREADY_EXISTS
      :value: "DAC_ALREADY_EXISTS"

   .. py:attribute:: DAC_DOES_NOT_EXIST
      :value: "DAC_DOES_NOT_EXIST"

   .. py:attribute:: DATA_LOSS
      :value: "DATA_LOSS"

   .. py:attribute:: DEADLINE_EXCEEDED
      :value: "DEADLINE_EXCEEDED"

   .. py:attribute:: DEPLOYMENT_TIMEOUT
      :value: "DEPLOYMENT_TIMEOUT"

   .. py:attribute:: DIRECTORY_NOT_EMPTY
      :value: "DIRECTORY_NOT_EMPTY"

   .. py:attribute:: DIRECTORY_PROTECTED
      :value: "DIRECTORY_PROTECTED"

   .. py:attribute:: DRY_RUN_FAILED
      :value: "DRY_RUN_FAILED"

   .. py:attribute:: ENDPOINT_NOT_FOUND
      :value: "ENDPOINT_NOT_FOUND"

   .. py:attribute:: EXTERNAL_LOCATION_ALREADY_EXISTS
      :value: "EXTERNAL_LOCATION_ALREADY_EXISTS"

   .. py:attribute:: EXTERNAL_LOCATION_DOES_NOT_EXIST
      :value: "EXTERNAL_LOCATION_DOES_NOT_EXIST"

   .. py:attribute:: FEATURE_DISABLED
      :value: "FEATURE_DISABLED"

   .. py:attribute:: GIT_CONFLICT
      :value: "GIT_CONFLICT"

   .. py:attribute:: GIT_REMOTE_ERROR
      :value: "GIT_REMOTE_ERROR"

   .. py:attribute:: GIT_SENSITIVE_TOKEN_DETECTED
      :value: "GIT_SENSITIVE_TOKEN_DETECTED"

   .. py:attribute:: GIT_UNKNOWN_REF
      :value: "GIT_UNKNOWN_REF"

   .. py:attribute:: GIT_URL_NOT_ON_ALLOW_LIST
      :value: "GIT_URL_NOT_ON_ALLOW_LIST"

   .. py:attribute:: INSECURE_PARTNER_RESPONSE
      :value: "INSECURE_PARTNER_RESPONSE"

   .. py:attribute:: INTERNAL_ERROR
      :value: "INTERNAL_ERROR"

   .. py:attribute:: INVALID_PARAMETER_VALUE
      :value: "INVALID_PARAMETER_VALUE"

   .. py:attribute:: INVALID_STATE
      :value: "INVALID_STATE"

   .. py:attribute:: INVALID_STATE_TRANSITION
      :value: "INVALID_STATE_TRANSITION"

   .. py:attribute:: IO_ERROR
      :value: "IO_ERROR"

   .. py:attribute:: IPYNB_FILE_IN_REPO
      :value: "IPYNB_FILE_IN_REPO"

   .. py:attribute:: MALFORMED_PARTNER_RESPONSE
      :value: "MALFORMED_PARTNER_RESPONSE"

   .. py:attribute:: MALFORMED_REQUEST
      :value: "MALFORMED_REQUEST"

   .. py:attribute:: MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST
      :value: "MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST"

   .. py:attribute:: MAX_BLOCK_SIZE_EXCEEDED
      :value: "MAX_BLOCK_SIZE_EXCEEDED"

   .. py:attribute:: MAX_CHILD_NODE_SIZE_EXCEEDED
      :value: "MAX_CHILD_NODE_SIZE_EXCEEDED"

   .. py:attribute:: MAX_LIST_SIZE_EXCEEDED
      :value: "MAX_LIST_SIZE_EXCEEDED"

   .. py:attribute:: MAX_NOTEBOOK_SIZE_EXCEEDED
      :value: "MAX_NOTEBOOK_SIZE_EXCEEDED"

   .. py:attribute:: MAX_READ_SIZE_EXCEEDED
      :value: "MAX_READ_SIZE_EXCEEDED"

   .. py:attribute:: METASTORE_ALREADY_EXISTS
      :value: "METASTORE_ALREADY_EXISTS"

   .. py:attribute:: METASTORE_DOES_NOT_EXIST
      :value: "METASTORE_DOES_NOT_EXIST"

   .. py:attribute:: METASTORE_NOT_EMPTY
      :value: "METASTORE_NOT_EMPTY"

   .. py:attribute:: NOT_FOUND
      :value: "NOT_FOUND"

   .. py:attribute:: NOT_IMPLEMENTED
      :value: "NOT_IMPLEMENTED"

   .. py:attribute:: PARTIAL_DELETE
      :value: "PARTIAL_DELETE"

   .. py:attribute:: PERMISSION_DENIED
      :value: "PERMISSION_DENIED"

   .. py:attribute:: PERMISSION_NOT_PROPAGATED
      :value: "PERMISSION_NOT_PROPAGATED"

   .. py:attribute:: PRINCIPAL_DOES_NOT_EXIST
      :value: "PRINCIPAL_DOES_NOT_EXIST"

   .. py:attribute:: PROJECTS_OPERATION_TIMEOUT
      :value: "PROJECTS_OPERATION_TIMEOUT"

   .. py:attribute:: PROVIDER_ALREADY_EXISTS
      :value: "PROVIDER_ALREADY_EXISTS"

   .. py:attribute:: PROVIDER_DOES_NOT_EXIST
      :value: "PROVIDER_DOES_NOT_EXIST"

   .. py:attribute:: PROVIDER_SHARE_NOT_ACCESSIBLE
      :value: "PROVIDER_SHARE_NOT_ACCESSIBLE"

   .. py:attribute:: QUOTA_EXCEEDED
      :value: "QUOTA_EXCEEDED"

   .. py:attribute:: RECIPIENT_ALREADY_EXISTS
      :value: "RECIPIENT_ALREADY_EXISTS"

   .. py:attribute:: RECIPIENT_DOES_NOT_EXIST
      :value: "RECIPIENT_DOES_NOT_EXIST"

   .. py:attribute:: REQUEST_LIMIT_EXCEEDED
      :value: "REQUEST_LIMIT_EXCEEDED"

   .. py:attribute:: RESOURCE_ALREADY_EXISTS
      :value: "RESOURCE_ALREADY_EXISTS"

   .. py:attribute:: RESOURCE_CONFLICT
      :value: "RESOURCE_CONFLICT"

   .. py:attribute:: RESOURCE_DOES_NOT_EXIST
      :value: "RESOURCE_DOES_NOT_EXIST"

   .. py:attribute:: RESOURCE_EXHAUSTED
      :value: "RESOURCE_EXHAUSTED"

   .. py:attribute:: RESOURCE_LIMIT_EXCEEDED
      :value: "RESOURCE_LIMIT_EXCEEDED"

   .. py:attribute:: SCHEMA_ALREADY_EXISTS
      :value: "SCHEMA_ALREADY_EXISTS"

   .. py:attribute:: SCHEMA_DOES_NOT_EXIST
      :value: "SCHEMA_DOES_NOT_EXIST"

   .. py:attribute:: SCHEMA_NOT_EMPTY
      :value: "SCHEMA_NOT_EMPTY"

   .. py:attribute:: SEARCH_QUERY_TOO_LONG
      :value: "SEARCH_QUERY_TOO_LONG"

   .. py:attribute:: SEARCH_QUERY_TOO_SHORT
      :value: "SEARCH_QUERY_TOO_SHORT"

   .. py:attribute:: SERVICE_UNDER_MAINTENANCE
      :value: "SERVICE_UNDER_MAINTENANCE"

   .. py:attribute:: SHARE_ALREADY_EXISTS
      :value: "SHARE_ALREADY_EXISTS"

   .. py:attribute:: SHARE_DOES_NOT_EXIST
      :value: "SHARE_DOES_NOT_EXIST"

   .. py:attribute:: STORAGE_CREDENTIAL_ALREADY_EXISTS
      :value: "STORAGE_CREDENTIAL_ALREADY_EXISTS"

   .. py:attribute:: STORAGE_CREDENTIAL_DOES_NOT_EXIST
      :value: "STORAGE_CREDENTIAL_DOES_NOT_EXIST"

   .. py:attribute:: TABLE_ALREADY_EXISTS
      :value: "TABLE_ALREADY_EXISTS"

   .. py:attribute:: TABLE_DOES_NOT_EXIST
      :value: "TABLE_DOES_NOT_EXIST"

   .. py:attribute:: TEMPORARILY_UNAVAILABLE
      :value: "TEMPORARILY_UNAVAILABLE"

   .. py:attribute:: UNAUTHENTICATED
      :value: "UNAUTHENTICATED"

   .. py:attribute:: UNAVAILABLE
      :value: "UNAVAILABLE"

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

   .. py:attribute:: UNPARSEABLE_HTTP_ERROR
      :value: "UNPARSEABLE_HTTP_ERROR"

   .. py:attribute:: WORKSPACE_TEMPORARILY_UNAVAILABLE
      :value: "WORKSPACE_TEMPORARILY_UNAVAILABLE"

.. autoclass:: GetAppPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GitRepository
   :members:
   :undoc-members:

.. autoclass:: GitSource
   :members:
   :undoc-members:

.. py:class:: HostType

   Enum representing the type of Databricks host.

   .. py:attribute:: ACCOUNTS
      :value: "ACCOUNTS"

   .. py:attribute:: WORKSPACE
      :value: "WORKSPACE"

   .. py:attribute:: UNIFIED
      :value: "UNIFIED"

.. autoclass:: ListAppDeploymentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAppsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCustomTemplatesResponse
   :members:
   :undoc-members:

.. autoclass:: ListSpacesResponse
   :members:
   :undoc-members:

.. autoclass:: Operation
   :members:
   :undoc-members:

.. autoclass:: Space
   :members:
   :undoc-members:

.. autoclass:: SpaceStatus
   :members:
   :undoc-members:

.. py:class:: SpaceStatusSpaceState

   .. py:attribute:: SPACE_ACTIVE
      :value: "SPACE_ACTIVE"

   .. py:attribute:: SPACE_CREATING
      :value: "SPACE_CREATING"

   .. py:attribute:: SPACE_DELETED
      :value: "SPACE_DELETED"

   .. py:attribute:: SPACE_DELETING
      :value: "SPACE_DELETING"

   .. py:attribute:: SPACE_ERROR
      :value: "SPACE_ERROR"

   .. py:attribute:: SPACE_UPDATING
      :value: "SPACE_UPDATING"

.. autoclass:: SpaceUpdate
   :members:
   :undoc-members:

.. py:class:: SpaceUpdateState

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

   .. py:attribute:: NOT_UPDATED
      :value: "NOT_UPDATED"

   .. py:attribute:: SUCCEEDED
      :value: "SUCCEEDED"

.. autoclass:: SpaceUpdateStatus
   :members:
   :undoc-members:

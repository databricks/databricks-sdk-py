Postgres
========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.postgres`` module.

.. py:currentmodule:: databricks.sdk.service.postgres
.. autoclass:: Branch
   :members:
   :undoc-members:

.. autoclass:: BranchOperationMetadata
   :members:
   :undoc-members:

.. autoclass:: BranchSpec
   :members:
   :undoc-members:

.. autoclass:: BranchStatus
   :members:
   :undoc-members:

.. py:class:: BranchStatusState

   The state of the branch.

   .. py:attribute:: ARCHIVED
      :value: "ARCHIVED"

   .. py:attribute:: IMPORTING
      :value: "IMPORTING"

   .. py:attribute:: INIT
      :value: "INIT"

   .. py:attribute:: READY
      :value: "READY"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

.. autoclass:: DatabaseCredential
   :members:
   :undoc-members:

.. autoclass:: DatabricksServiceExceptionWithDetailsProto
   :members:
   :undoc-members:

.. autoclass:: Endpoint
   :members:
   :undoc-members:

.. autoclass:: EndpointHosts
   :members:
   :undoc-members:

.. autoclass:: EndpointOperationMetadata
   :members:
   :undoc-members:

.. autoclass:: EndpointSettings
   :members:
   :undoc-members:

.. autoclass:: EndpointSpec
   :members:
   :undoc-members:

.. autoclass:: EndpointStatus
   :members:
   :undoc-members:

.. py:class:: EndpointStatusState

   The state of the compute endpoint.

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: IDLE
      :value: "IDLE"

   .. py:attribute:: INIT
      :value: "INIT"

.. py:class:: EndpointType

   The compute endpoint type. Either `read_write` or `read_only`.

   .. py:attribute:: ENDPOINT_TYPE_READ_ONLY
      :value: "ENDPOINT_TYPE_READ_ONLY"

   .. py:attribute:: ENDPOINT_TYPE_READ_WRITE
      :value: "ENDPOINT_TYPE_READ_WRITE"

.. py:class:: ErrorCode

   Legacy definition of the ErrorCode enum. Please keep in sync with api-base/proto/error_code.proto (except status code mapping annotations as this file doesn't have them). Will be removed eventually, pending the ScalaPB 0.4 cleanup.

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

.. py:class:: HostType

   Enum representing the type of Databricks host.

   .. py:attribute:: ACCOUNTS
      :value: "ACCOUNTS"

   .. py:attribute:: WORKSPACE
      :value: "WORKSPACE"

   .. py:attribute:: UNIFIED
      :value: "UNIFIED"

.. autoclass:: ListBranchesResponse
   :members:
   :undoc-members:

.. autoclass:: ListEndpointsResponse
   :members:
   :undoc-members:

.. autoclass:: ListProjectsResponse
   :members:
   :undoc-members:

.. autoclass:: ListRolesResponse
   :members:
   :undoc-members:

.. autoclass:: Operation
   :members:
   :undoc-members:

.. autoclass:: Project
   :members:
   :undoc-members:

.. autoclass:: ProjectDefaultEndpointSettings
   :members:
   :undoc-members:

.. autoclass:: ProjectOperationMetadata
   :members:
   :undoc-members:

.. autoclass:: ProjectSpec
   :members:
   :undoc-members:

.. autoclass:: ProjectStatus
   :members:
   :undoc-members:

.. autoclass:: RequestedClaims
   :members:
   :undoc-members:

.. py:class:: RequestedClaimsPermissionSet

   .. py:attribute:: READ_ONLY
      :value: "READ_ONLY"

.. autoclass:: RequestedResource
   :members:
   :undoc-members:

.. autoclass:: Role
   :members:
   :undoc-members:

.. py:class:: RoleAuthMethod

   How the role is authenticated when connecting to Postgres.

   .. py:attribute:: LAKEBASE_OAUTH_V1
      :value: "LAKEBASE_OAUTH_V1"

   .. py:attribute:: NO_LOGIN
      :value: "NO_LOGIN"

   .. py:attribute:: PG_PASSWORD_SCRAM_SHA_256
      :value: "PG_PASSWORD_SCRAM_SHA_256"

.. py:class:: RoleIdentityType

   The type of the Databricks managed identity that this Role represents. Leave empty if you wish to create a regular Postgres role not associated with a Databricks identity.

   .. py:attribute:: GROUP
      :value: "GROUP"

   .. py:attribute:: SERVICE_PRINCIPAL
      :value: "SERVICE_PRINCIPAL"

   .. py:attribute:: USER
      :value: "USER"

.. autoclass:: RoleOperationMetadata
   :members:
   :undoc-members:

.. autoclass:: RoleRoleSpec
   :members:
   :undoc-members:

.. autoclass:: RoleRoleStatus
   :members:
   :undoc-members:

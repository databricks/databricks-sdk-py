Delta Sharing
=============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.sharing`` module.

.. py:currentmodule:: databricks.sdk.service.sharing
.. py:class:: AuthenticationType

   The delta sharing authentication type.

   .. py:attribute:: DATABRICKS
      :value: "DATABRICKS"

   .. py:attribute:: OAUTH_CLIENT_CREDENTIALS
      :value: "OAUTH_CLIENT_CREDENTIALS"

   .. py:attribute:: TOKEN
      :value: "TOKEN"

.. py:class:: ColumnTypeName

   UC supported column types Copied from https://src.dev.databricks.com/databricks/universe@23a85902bb58695ab9293adc9f327b0714b55e72/-/blob/managed-catalog/api/messages/table.proto?L68

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

.. autoclass:: CreateProvider
   :members:
   :undoc-members:

.. autoclass:: CreateRecipient
   :members:
   :undoc-members:

.. autoclass:: CreateShare
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeltaSharingDependency
   :members:
   :undoc-members:

.. autoclass:: DeltaSharingDependencyList
   :members:
   :undoc-members:

.. autoclass:: DeltaSharingFunction
   :members:
   :undoc-members:

.. autoclass:: DeltaSharingFunctionDependency
   :members:
   :undoc-members:

.. autoclass:: DeltaSharingTableDependency
   :members:
   :undoc-members:

.. autoclass:: FunctionParameterInfo
   :members:
   :undoc-members:

.. autoclass:: FunctionParameterInfos
   :members:
   :undoc-members:

.. py:class:: FunctionParameterMode

   .. py:attribute:: IN
      :value: "IN"

   .. py:attribute:: INOUT
      :value: "INOUT"

   .. py:attribute:: OUT
      :value: "OUT"

.. py:class:: FunctionParameterType

   .. py:attribute:: COLUMN
      :value: "COLUMN"

   .. py:attribute:: PARAM
      :value: "PARAM"

.. autoclass:: GetActivationUrlInfoResponse
   :members:
   :undoc-members:

.. autoclass:: GetRecipientSharePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: GetSharePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: IpAccessList
   :members:
   :undoc-members:

.. autoclass:: ListProviderShareAssetsResponse
   :members:
   :undoc-members:

.. autoclass:: ListProviderSharesResponse
   :members:
   :undoc-members:

.. autoclass:: ListProvidersResponse
   :members:
   :undoc-members:

.. autoclass:: ListRecipientsResponse
   :members:
   :undoc-members:

.. autoclass:: ListSharesResponse
   :members:
   :undoc-members:

.. autoclass:: NotebookFile
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

.. autoclass:: PermissionsChange
   :members:
   :undoc-members:

.. py:class:: Privilege

   .. py:attribute:: ACCESS
      :value: "ACCESS"

   .. py:attribute:: ALL_PRIVILEGES
      :value: "ALL_PRIVILEGES"

   .. py:attribute:: APPLY_TAG
      :value: "APPLY_TAG"

   .. py:attribute:: CREATE
      :value: "CREATE"

   .. py:attribute:: CREATE_CATALOG
      :value: "CREATE_CATALOG"

   .. py:attribute:: CREATE_CONNECTION
      :value: "CREATE_CONNECTION"

   .. py:attribute:: CREATE_EXTERNAL_LOCATION
      :value: "CREATE_EXTERNAL_LOCATION"

   .. py:attribute:: CREATE_EXTERNAL_TABLE
      :value: "CREATE_EXTERNAL_TABLE"

   .. py:attribute:: CREATE_EXTERNAL_VOLUME
      :value: "CREATE_EXTERNAL_VOLUME"

   .. py:attribute:: CREATE_FOREIGN_CATALOG
      :value: "CREATE_FOREIGN_CATALOG"

   .. py:attribute:: CREATE_FOREIGN_SECURABLE
      :value: "CREATE_FOREIGN_SECURABLE"

   .. py:attribute:: CREATE_FUNCTION
      :value: "CREATE_FUNCTION"

   .. py:attribute:: CREATE_MANAGED_STORAGE
      :value: "CREATE_MANAGED_STORAGE"

   .. py:attribute:: CREATE_MATERIALIZED_VIEW
      :value: "CREATE_MATERIALIZED_VIEW"

   .. py:attribute:: CREATE_MODEL
      :value: "CREATE_MODEL"

   .. py:attribute:: CREATE_PROVIDER
      :value: "CREATE_PROVIDER"

   .. py:attribute:: CREATE_RECIPIENT
      :value: "CREATE_RECIPIENT"

   .. py:attribute:: CREATE_SCHEMA
      :value: "CREATE_SCHEMA"

   .. py:attribute:: CREATE_SERVICE_CREDENTIAL
      :value: "CREATE_SERVICE_CREDENTIAL"

   .. py:attribute:: CREATE_SHARE
      :value: "CREATE_SHARE"

   .. py:attribute:: CREATE_STORAGE_CREDENTIAL
      :value: "CREATE_STORAGE_CREDENTIAL"

   .. py:attribute:: CREATE_TABLE
      :value: "CREATE_TABLE"

   .. py:attribute:: CREATE_VIEW
      :value: "CREATE_VIEW"

   .. py:attribute:: CREATE_VOLUME
      :value: "CREATE_VOLUME"

   .. py:attribute:: EXECUTE
      :value: "EXECUTE"

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: MANAGE_ALLOWLIST
      :value: "MANAGE_ALLOWLIST"

   .. py:attribute:: MODIFY
      :value: "MODIFY"

   .. py:attribute:: READ_FILES
      :value: "READ_FILES"

   .. py:attribute:: READ_PRIVATE_FILES
      :value: "READ_PRIVATE_FILES"

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: REFRESH
      :value: "REFRESH"

   .. py:attribute:: SELECT
      :value: "SELECT"

   .. py:attribute:: SET_SHARE_PERMISSION
      :value: "SET_SHARE_PERMISSION"

   .. py:attribute:: USAGE
      :value: "USAGE"

   .. py:attribute:: USE_CATALOG
      :value: "USE_CATALOG"

   .. py:attribute:: USE_CONNECTION
      :value: "USE_CONNECTION"

   .. py:attribute:: USE_MARKETPLACE_ASSETS
      :value: "USE_MARKETPLACE_ASSETS"

   .. py:attribute:: USE_PROVIDER
      :value: "USE_PROVIDER"

   .. py:attribute:: USE_RECIPIENT
      :value: "USE_RECIPIENT"

   .. py:attribute:: USE_SCHEMA
      :value: "USE_SCHEMA"

   .. py:attribute:: USE_SHARE
      :value: "USE_SHARE"

   .. py:attribute:: WRITE_FILES
      :value: "WRITE_FILES"

   .. py:attribute:: WRITE_PRIVATE_FILES
      :value: "WRITE_PRIVATE_FILES"

   .. py:attribute:: WRITE_VOLUME
      :value: "WRITE_VOLUME"

.. autoclass:: PrivilegeAssignment
   :members:
   :undoc-members:

.. autoclass:: ProviderInfo
   :members:
   :undoc-members:

.. autoclass:: ProviderShare
   :members:
   :undoc-members:

.. autoclass:: RecipientInfo
   :members:
   :undoc-members:

.. autoclass:: RecipientProfile
   :members:
   :undoc-members:

.. autoclass:: RecipientTokenInfo
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelAlias
   :members:
   :undoc-members:

.. autoclass:: RetrieveTokenResponse
   :members:
   :undoc-members:

.. autoclass:: RotateRecipientToken
   :members:
   :undoc-members:

.. autoclass:: SecurablePropertiesKvPairs
   :members:
   :undoc-members:

.. autoclass:: ShareInfo
   :members:
   :undoc-members:

.. autoclass:: ShareToPrivilegeAssignment
   :members:
   :undoc-members:

.. autoclass:: SharedDataObject
   :members:
   :undoc-members:

.. py:class:: SharedDataObjectDataObjectType

   .. py:attribute:: FEATURE_SPEC
      :value: "FEATURE_SPEC"

   .. py:attribute:: FUNCTION
      :value: "FUNCTION"

   .. py:attribute:: MATERIALIZED_VIEW
      :value: "MATERIALIZED_VIEW"

   .. py:attribute:: MODEL
      :value: "MODEL"

   .. py:attribute:: NOTEBOOK_FILE
      :value: "NOTEBOOK_FILE"

   .. py:attribute:: SCHEMA
      :value: "SCHEMA"

   .. py:attribute:: STREAMING_TABLE
      :value: "STREAMING_TABLE"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VIEW
      :value: "VIEW"

.. py:class:: SharedDataObjectHistoryDataSharingStatus

   .. py:attribute:: DISABLED
      :value: "DISABLED"

   .. py:attribute:: ENABLED
      :value: "ENABLED"

.. py:class:: SharedDataObjectStatus

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: PERMISSION_DENIED
      :value: "PERMISSION_DENIED"

.. autoclass:: SharedDataObjectUpdate
   :members:
   :undoc-members:

.. py:class:: SharedDataObjectUpdateAction

   .. py:attribute:: ADD
      :value: "ADD"

   .. py:attribute:: REMOVE
      :value: "REMOVE"

   .. py:attribute:: UPDATE
      :value: "UPDATE"

.. py:class:: SharedSecurableKind

   The SecurableKind of a delta-shared object.

   .. py:attribute:: FUNCTION_FEATURE_SPEC
      :value: "FUNCTION_FEATURE_SPEC"

   .. py:attribute:: FUNCTION_REGISTERED_MODEL
      :value: "FUNCTION_REGISTERED_MODEL"

   .. py:attribute:: FUNCTION_STANDARD
      :value: "FUNCTION_STANDARD"

.. autoclass:: Table
   :members:
   :undoc-members:

.. autoclass:: TableInternalAttributes
   :members:
   :undoc-members:

.. py:class:: TableInternalAttributesSharedTableType

   .. py:attribute:: DIRECTORY_BASED_TABLE
      :value: "DIRECTORY_BASED_TABLE"

   .. py:attribute:: FILE_BASED_TABLE
      :value: "FILE_BASED_TABLE"

   .. py:attribute:: FOREIGN_TABLE
      :value: "FOREIGN_TABLE"

   .. py:attribute:: MATERIALIZED_VIEW
      :value: "MATERIALIZED_VIEW"

   .. py:attribute:: STREAMING_TABLE
      :value: "STREAMING_TABLE"

   .. py:attribute:: VIEW
      :value: "VIEW"

.. autoclass:: UpdateProvider
   :members:
   :undoc-members:

.. autoclass:: UpdateRecipient
   :members:
   :undoc-members:

.. autoclass:: UpdateShare
   :members:
   :undoc-members:

.. autoclass:: UpdateSharePermissions
   :members:
   :undoc-members:

.. autoclass:: UpdateSharePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: Volume
   :members:
   :undoc-members:

.. autoclass:: VolumeInternalAttributes
   :members:
   :undoc-members:

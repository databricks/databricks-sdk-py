Delta Sharing
=============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.sharing`` module.

.. py:currentmodule:: databricks.sdk.service.sharing
.. py:class:: AuthenticationType

   The delta sharing authentication type.

   .. py:attribute:: DATABRICKS
      :value: "DATABRICKS"

   .. py:attribute:: TOKEN
      :value: "TOKEN"

.. autoclass:: CentralCleanRoomInfo
   :members:
   :undoc-members:

.. autoclass:: CleanRoomAssetInfo
   :members:
   :undoc-members:

.. autoclass:: CleanRoomCatalog
   :members:
   :undoc-members:

.. autoclass:: CleanRoomCatalogUpdate
   :members:
   :undoc-members:

.. autoclass:: CleanRoomCollaboratorInfo
   :members:
   :undoc-members:

.. autoclass:: CleanRoomInfo
   :members:
   :undoc-members:

.. autoclass:: CleanRoomNotebookInfo
   :members:
   :undoc-members:

.. autoclass:: CleanRoomTableInfo
   :members:
   :undoc-members:

.. autoclass:: ColumnInfo
   :members:
   :undoc-members:

.. autoclass:: ColumnMask
   :members:
   :undoc-members:

.. py:class:: ColumnTypeName

   Name of type (INT, STRUCT, MAP, etc.).

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

.. autoclass:: CreateCleanRoom
   :members:
   :undoc-members:

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

.. autoclass:: GetActivationUrlInfoResponse
   :members:
   :undoc-members:

.. autoclass:: GetRecipientSharePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: IpAccessList
   :members:
   :undoc-members:

.. autoclass:: ListCleanRoomsResponse
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

.. autoclass:: Partition
   :members:
   :undoc-members:

.. autoclass:: PartitionValue
   :members:
   :undoc-members:

.. py:class:: PartitionValueOp

   The operator to apply for the value.

   .. py:attribute:: EQUAL
      :value: "EQUAL"

   .. py:attribute:: LIKE
      :value: "LIKE"

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

   The type of the data object.

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

   Whether to enable or disable sharing of data history. If not specified, the default is **DISABLED**.

   .. py:attribute:: DISABLED
      :value: "DISABLED"

   .. py:attribute:: ENABLED
      :value: "ENABLED"

.. py:class:: SharedDataObjectStatus

   One of: **ACTIVE**, **PERMISSION_DENIED**.

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: PERMISSION_DENIED
      :value: "PERMISSION_DENIED"

.. autoclass:: SharedDataObjectUpdate
   :members:
   :undoc-members:

.. py:class:: SharedDataObjectUpdateAction

   One of: **ADD**, **REMOVE**, **UPDATE**.

   .. py:attribute:: ADD
      :value: "ADD"

   .. py:attribute:: REMOVE
      :value: "REMOVE"

   .. py:attribute:: UPDATE
      :value: "UPDATE"

.. autoclass:: UpdateCleanRoom
   :members:
   :undoc-members:

.. autoclass:: UpdatePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateProvider
   :members:
   :undoc-members:

.. autoclass:: UpdateRecipient
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateShare
   :members:
   :undoc-members:

.. autoclass:: UpdateSharePermissions
   :members:
   :undoc-members:

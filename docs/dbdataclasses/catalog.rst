Unity Catalog
=============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.catalog`` module.

.. py:currentmodule:: databricks.sdk.service.catalog
.. autoclass:: AccountsCreateMetastore
   :members:
   :undoc-members:

.. autoclass:: AccountsCreateMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: AccountsCreateStorageCredential
   :members:
   :undoc-members:

.. autoclass:: AccountsMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: AccountsMetastoreInfo
   :members:
   :undoc-members:

.. autoclass:: AccountsStorageCredentialInfo
   :members:
   :undoc-members:

.. autoclass:: AccountsUpdateMetastore
   :members:
   :undoc-members:

.. autoclass:: AccountsUpdateMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: AccountsUpdateStorageCredential
   :members:
   :undoc-members:

.. autoclass:: ArtifactAllowlistInfo
   :members:
   :undoc-members:

.. autoclass:: ArtifactMatcher
   :members:
   :undoc-members:

.. py:class:: ArtifactType

   The artifact type

   .. py:attribute:: INIT_SCRIPT
      :value: "INIT_SCRIPT"

   .. py:attribute:: LIBRARY_JAR
      :value: "LIBRARY_JAR"

   .. py:attribute:: LIBRARY_MAVEN
      :value: "LIBRARY_MAVEN"

.. autoclass:: AssignResponse
   :members:
   :undoc-members:

.. autoclass:: AwsIamRoleRequest
   :members:
   :undoc-members:

.. autoclass:: AwsIamRoleResponse
   :members:
   :undoc-members:

.. autoclass:: AzureManagedIdentityRequest
   :members:
   :undoc-members:

.. autoclass:: AzureManagedIdentityResponse
   :members:
   :undoc-members:

.. autoclass:: AzureServicePrincipal
   :members:
   :undoc-members:

.. autoclass:: CancelRefreshResponse
   :members:
   :undoc-members:

.. autoclass:: CatalogInfo
   :members:
   :undoc-members:

.. py:class:: CatalogInfoSecurableKind

   Kind of catalog securable.

   .. py:attribute:: CATALOG_DELTASHARING
      :value: "CATALOG_DELTASHARING"

   .. py:attribute:: CATALOG_FOREIGN_BIGQUERY
      :value: "CATALOG_FOREIGN_BIGQUERY"

   .. py:attribute:: CATALOG_FOREIGN_DATABRICKS
      :value: "CATALOG_FOREIGN_DATABRICKS"

   .. py:attribute:: CATALOG_FOREIGN_MYSQL
      :value: "CATALOG_FOREIGN_MYSQL"

   .. py:attribute:: CATALOG_FOREIGN_POSTGRESQL
      :value: "CATALOG_FOREIGN_POSTGRESQL"

   .. py:attribute:: CATALOG_FOREIGN_REDSHIFT
      :value: "CATALOG_FOREIGN_REDSHIFT"

   .. py:attribute:: CATALOG_FOREIGN_SNOWFLAKE
      :value: "CATALOG_FOREIGN_SNOWFLAKE"

   .. py:attribute:: CATALOG_FOREIGN_SQLDW
      :value: "CATALOG_FOREIGN_SQLDW"

   .. py:attribute:: CATALOG_FOREIGN_SQLSERVER
      :value: "CATALOG_FOREIGN_SQLSERVER"

   .. py:attribute:: CATALOG_INTERNAL
      :value: "CATALOG_INTERNAL"

   .. py:attribute:: CATALOG_ONLINE
      :value: "CATALOG_ONLINE"

   .. py:attribute:: CATALOG_ONLINE_INDEX
      :value: "CATALOG_ONLINE_INDEX"

   .. py:attribute:: CATALOG_STANDARD
      :value: "CATALOG_STANDARD"

   .. py:attribute:: CATALOG_SYSTEM
      :value: "CATALOG_SYSTEM"

   .. py:attribute:: CATALOG_SYSTEM_DELTASHARING
      :value: "CATALOG_SYSTEM_DELTASHARING"

.. py:class:: CatalogType

   The type of the catalog.

   .. py:attribute:: DELTASHARING_CATALOG
      :value: "DELTASHARING_CATALOG"

   .. py:attribute:: MANAGED_CATALOG
      :value: "MANAGED_CATALOG"

   .. py:attribute:: SYSTEM_CATALOG
      :value: "SYSTEM_CATALOG"

.. autoclass:: CloudflareApiToken
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

.. autoclass:: ConnectionInfo
   :members:
   :undoc-members:

.. py:class:: ConnectionInfoSecurableKind

   Kind of connection securable.

   .. py:attribute:: CONNECTION_BIGQUERY
      :value: "CONNECTION_BIGQUERY"

   .. py:attribute:: CONNECTION_DATABRICKS
      :value: "CONNECTION_DATABRICKS"

   .. py:attribute:: CONNECTION_MYSQL
      :value: "CONNECTION_MYSQL"

   .. py:attribute:: CONNECTION_ONLINE_CATALOG
      :value: "CONNECTION_ONLINE_CATALOG"

   .. py:attribute:: CONNECTION_POSTGRESQL
      :value: "CONNECTION_POSTGRESQL"

   .. py:attribute:: CONNECTION_REDSHIFT
      :value: "CONNECTION_REDSHIFT"

   .. py:attribute:: CONNECTION_SNOWFLAKE
      :value: "CONNECTION_SNOWFLAKE"

   .. py:attribute:: CONNECTION_SQLDW
      :value: "CONNECTION_SQLDW"

   .. py:attribute:: CONNECTION_SQLSERVER
      :value: "CONNECTION_SQLSERVER"

.. py:class:: ConnectionType

   The type of connection.

   .. py:attribute:: BIGQUERY
      :value: "BIGQUERY"

   .. py:attribute:: DATABRICKS
      :value: "DATABRICKS"

   .. py:attribute:: MYSQL
      :value: "MYSQL"

   .. py:attribute:: POSTGRESQL
      :value: "POSTGRESQL"

   .. py:attribute:: REDSHIFT
      :value: "REDSHIFT"

   .. py:attribute:: SNOWFLAKE
      :value: "SNOWFLAKE"

   .. py:attribute:: SQLDW
      :value: "SQLDW"

   .. py:attribute:: SQLSERVER
      :value: "SQLSERVER"

.. autoclass:: ContinuousUpdateStatus
   :members:
   :undoc-members:

.. autoclass:: CreateCatalog
   :members:
   :undoc-members:

.. autoclass:: CreateConnection
   :members:
   :undoc-members:

.. autoclass:: CreateExternalLocation
   :members:
   :undoc-members:

.. autoclass:: CreateFunction
   :members:
   :undoc-members:

.. py:class:: CreateFunctionParameterStyle

   Function parameter style. **S** is the value for SQL.

   .. py:attribute:: S
      :value: "S"

.. autoclass:: CreateFunctionRequest
   :members:
   :undoc-members:

.. py:class:: CreateFunctionRoutineBody

   Function language. When **EXTERNAL** is used, the language of the routine function should be specified in the __external_language__ field, and the __return_params__ of the function cannot be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be **NO_SQL**.

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: SQL
      :value: "SQL"

.. py:class:: CreateFunctionSecurityType

   Function security type.

   .. py:attribute:: DEFINER
      :value: "DEFINER"

.. py:class:: CreateFunctionSqlDataAccess

   Function SQL data access.

   .. py:attribute:: CONTAINS_SQL
      :value: "CONTAINS_SQL"

   .. py:attribute:: NO_SQL
      :value: "NO_SQL"

   .. py:attribute:: READS_SQL_DATA
      :value: "READS_SQL_DATA"

.. autoclass:: CreateMetastore
   :members:
   :undoc-members:

.. autoclass:: CreateMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: CreateMonitor
   :members:
   :undoc-members:

.. autoclass:: CreateOnlineTableRequest
   :members:
   :undoc-members:

.. autoclass:: CreateRegisteredModelRequest
   :members:
   :undoc-members:

.. autoclass:: CreateResponse
   :members:
   :undoc-members:

.. autoclass:: CreateSchema
   :members:
   :undoc-members:

.. autoclass:: CreateStorageCredential
   :members:
   :undoc-members:

.. autoclass:: CreateTableConstraint
   :members:
   :undoc-members:

.. autoclass:: CreateVolumeRequestContent
   :members:
   :undoc-members:

.. py:class:: CredentialType

   The type of credential.

   .. py:attribute:: USERNAME_PASSWORD
      :value: "USERNAME_PASSWORD"

.. autoclass:: CurrentWorkspaceBindings
   :members:
   :undoc-members:

.. py:class:: DataSourceFormat

   Data source format

   .. py:attribute:: AVRO
      :value: "AVRO"

   .. py:attribute:: BIGQUERY_FORMAT
      :value: "BIGQUERY_FORMAT"

   .. py:attribute:: CSV
      :value: "CSV"

   .. py:attribute:: DATABRICKS_FORMAT
      :value: "DATABRICKS_FORMAT"

   .. py:attribute:: DELTA
      :value: "DELTA"

   .. py:attribute:: DELTASHARING
      :value: "DELTASHARING"

   .. py:attribute:: HIVE_CUSTOM
      :value: "HIVE_CUSTOM"

   .. py:attribute:: HIVE_SERDE
      :value: "HIVE_SERDE"

   .. py:attribute:: JSON
      :value: "JSON"

   .. py:attribute:: MYSQL_FORMAT
      :value: "MYSQL_FORMAT"

   .. py:attribute:: NETSUITE_FORMAT
      :value: "NETSUITE_FORMAT"

   .. py:attribute:: ORC
      :value: "ORC"

   .. py:attribute:: PARQUET
      :value: "PARQUET"

   .. py:attribute:: POSTGRESQL_FORMAT
      :value: "POSTGRESQL_FORMAT"

   .. py:attribute:: REDSHIFT_FORMAT
      :value: "REDSHIFT_FORMAT"

   .. py:attribute:: SALESFORCE_FORMAT
      :value: "SALESFORCE_FORMAT"

   .. py:attribute:: SNOWFLAKE_FORMAT
      :value: "SNOWFLAKE_FORMAT"

   .. py:attribute:: SQLDW_FORMAT
      :value: "SQLDW_FORMAT"

   .. py:attribute:: SQLSERVER_FORMAT
      :value: "SQLSERVER_FORMAT"

   .. py:attribute:: TEXT
      :value: "TEXT"

   .. py:attribute:: UNITY_CATALOG
      :value: "UNITY_CATALOG"

   .. py:attribute:: VECTOR_INDEX_FORMAT
      :value: "VECTOR_INDEX_FORMAT"

   .. py:attribute:: WORKDAY_RAAS_FORMAT
      :value: "WORKDAY_RAAS_FORMAT"

.. autoclass:: DatabricksGcpServiceAccountRequest
   :members:
   :undoc-members:

.. autoclass:: DatabricksGcpServiceAccountResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteAliasResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeltaRuntimePropertiesKvPairs
   :members:
   :undoc-members:

.. autoclass:: Dependency
   :members:
   :undoc-members:

.. autoclass:: DependencyList
   :members:
   :undoc-members:

.. autoclass:: DisableResponse
   :members:
   :undoc-members:

.. autoclass:: EffectivePermissionsList
   :members:
   :undoc-members:

.. autoclass:: EffectivePredictiveOptimizationFlag
   :members:
   :undoc-members:

.. py:class:: EffectivePredictiveOptimizationFlagInheritedFromType

   The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank.

   .. py:attribute:: CATALOG
      :value: "CATALOG"

   .. py:attribute:: SCHEMA
      :value: "SCHEMA"

.. autoclass:: EffectivePrivilege
   :members:
   :undoc-members:

.. autoclass:: EffectivePrivilegeAssignment
   :members:
   :undoc-members:

.. py:class:: EnablePredictiveOptimization

   Whether predictive optimization should be enabled for this object and objects under it.

   .. py:attribute:: DISABLE
      :value: "DISABLE"

   .. py:attribute:: ENABLE
      :value: "ENABLE"

   .. py:attribute:: INHERIT
      :value: "INHERIT"

.. autoclass:: EnableResponse
   :members:
   :undoc-members:

.. autoclass:: EncryptionDetails
   :members:
   :undoc-members:

.. autoclass:: ExternalLocationInfo
   :members:
   :undoc-members:

.. autoclass:: FailedStatus
   :members:
   :undoc-members:

.. autoclass:: ForeignKeyConstraint
   :members:
   :undoc-members:

.. autoclass:: FunctionDependency
   :members:
   :undoc-members:

.. autoclass:: FunctionInfo
   :members:
   :undoc-members:

.. py:class:: FunctionInfoParameterStyle

   Function parameter style. **S** is the value for SQL.

   .. py:attribute:: S
      :value: "S"

.. py:class:: FunctionInfoRoutineBody

   Function language. When **EXTERNAL** is used, the language of the routine function should be specified in the __external_language__ field, and the __return_params__ of the function cannot be used (as **TABLE** return type is not supported), and the __sql_data_access__ field must be **NO_SQL**.

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: SQL
      :value: "SQL"

.. py:class:: FunctionInfoSecurityType

   Function security type.

   .. py:attribute:: DEFINER
      :value: "DEFINER"

.. py:class:: FunctionInfoSqlDataAccess

   Function SQL data access.

   .. py:attribute:: CONTAINS_SQL
      :value: "CONTAINS_SQL"

   .. py:attribute:: NO_SQL
      :value: "NO_SQL"

   .. py:attribute:: READS_SQL_DATA
      :value: "READS_SQL_DATA"

.. autoclass:: FunctionParameterInfo
   :members:
   :undoc-members:

.. autoclass:: FunctionParameterInfos
   :members:
   :undoc-members:

.. py:class:: FunctionParameterMode

   The mode of the function parameter.

   .. py:attribute:: IN
      :value: "IN"

.. py:class:: FunctionParameterType

   The type of function parameter.

   .. py:attribute:: COLUMN
      :value: "COLUMN"

   .. py:attribute:: PARAM
      :value: "PARAM"

.. autoclass:: GetMetastoreSummaryResponse
   :members:
   :undoc-members:

.. py:class:: GetMetastoreSummaryResponseDeltaSharingScope

   The scope of Delta Sharing enabled for the metastore.

   .. py:attribute:: INTERNAL
      :value: "INTERNAL"

   .. py:attribute:: INTERNAL_AND_EXTERNAL
      :value: "INTERNAL_AND_EXTERNAL"

.. py:class:: IsolationMode

   Whether the current securable is accessible from all workspaces or a specific set of workspaces.

   .. py:attribute:: ISOLATED
      :value: "ISOLATED"

   .. py:attribute:: OPEN
      :value: "OPEN"

.. autoclass:: ListAccountMetastoreAssignmentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAccountStorageCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCatalogsResponse
   :members:
   :undoc-members:

.. autoclass:: ListConnectionsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExternalLocationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListFunctionsResponse
   :members:
   :undoc-members:

.. autoclass:: ListMetastoresResponse
   :members:
   :undoc-members:

.. autoclass:: ListModelVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: ListRegisteredModelsResponse
   :members:
   :undoc-members:

.. autoclass:: ListSchemasResponse
   :members:
   :undoc-members:

.. autoclass:: ListStorageCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: ListSystemSchemasResponse
   :members:
   :undoc-members:

.. autoclass:: ListTableSummariesResponse
   :members:
   :undoc-members:

.. autoclass:: ListTablesResponse
   :members:
   :undoc-members:

.. autoclass:: ListVolumesResponseContent
   :members:
   :undoc-members:

.. py:class:: MatchType

   The artifact pattern matching type

   .. py:attribute:: PREFIX_MATCH
      :value: "PREFIX_MATCH"

.. autoclass:: MetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: MetastoreInfo
   :members:
   :undoc-members:

.. py:class:: MetastoreInfoDeltaSharingScope

   The scope of Delta Sharing enabled for the metastore.

   .. py:attribute:: INTERNAL
      :value: "INTERNAL"

   .. py:attribute:: INTERNAL_AND_EXTERNAL
      :value: "INTERNAL_AND_EXTERNAL"

.. autoclass:: ModelVersionInfo
   :members:
   :undoc-members:

.. py:class:: ModelVersionInfoStatus

   Current status of the model version. Newly created model versions start in PENDING_REGISTRATION status, then move to READY status once the model version files are uploaded and the model version is finalized. Only model versions in READY status can be loaded for inference or served.

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: MonitorCronSchedule
   :members:
   :undoc-members:

.. py:class:: MonitorCronSchedulePauseStatus

   Read only field that indicates whether a schedule is paused or not.

   .. py:attribute:: PAUSED
      :value: "PAUSED"

   .. py:attribute:: UNPAUSED
      :value: "UNPAUSED"

.. autoclass:: MonitorDataClassificationConfig
   :members:
   :undoc-members:

.. autoclass:: MonitorDestination
   :members:
   :undoc-members:

.. autoclass:: MonitorInferenceLog
   :members:
   :undoc-members:

.. py:class:: MonitorInferenceLogProblemType

   Problem type the model aims to solve. Determines the type of model-quality metrics that will be computed.

   .. py:attribute:: PROBLEM_TYPE_CLASSIFICATION
      :value: "PROBLEM_TYPE_CLASSIFICATION"

   .. py:attribute:: PROBLEM_TYPE_REGRESSION
      :value: "PROBLEM_TYPE_REGRESSION"

.. autoclass:: MonitorInfo
   :members:
   :undoc-members:

.. py:class:: MonitorInfoStatus

   The status of the monitor.

   .. py:attribute:: MONITOR_STATUS_ACTIVE
      :value: "MONITOR_STATUS_ACTIVE"

   .. py:attribute:: MONITOR_STATUS_DELETE_PENDING
      :value: "MONITOR_STATUS_DELETE_PENDING"

   .. py:attribute:: MONITOR_STATUS_ERROR
      :value: "MONITOR_STATUS_ERROR"

   .. py:attribute:: MONITOR_STATUS_FAILED
      :value: "MONITOR_STATUS_FAILED"

   .. py:attribute:: MONITOR_STATUS_PENDING
      :value: "MONITOR_STATUS_PENDING"

.. autoclass:: MonitorMetric
   :members:
   :undoc-members:

.. py:class:: MonitorMetricType

   Can only be one of ``"CUSTOM_METRIC_TYPE_AGGREGATE"``, ``"CUSTOM_METRIC_TYPE_DERIVED"``, or ``"CUSTOM_METRIC_TYPE_DRIFT"``. The ``"CUSTOM_METRIC_TYPE_AGGREGATE"`` and ``"CUSTOM_METRIC_TYPE_DERIVED"`` metrics are computed on a single table, whereas the ``"CUSTOM_METRIC_TYPE_DRIFT"`` compare metrics across baseline and input table, or across the two consecutive time windows. - CUSTOM_METRIC_TYPE_AGGREGATE: only depend on the existing columns in your table - CUSTOM_METRIC_TYPE_DERIVED: depend on previously computed aggregate metrics - CUSTOM_METRIC_TYPE_DRIFT: depend on previously computed aggregate or derived metrics

   .. py:attribute:: CUSTOM_METRIC_TYPE_AGGREGATE
      :value: "CUSTOM_METRIC_TYPE_AGGREGATE"

   .. py:attribute:: CUSTOM_METRIC_TYPE_DERIVED
      :value: "CUSTOM_METRIC_TYPE_DERIVED"

   .. py:attribute:: CUSTOM_METRIC_TYPE_DRIFT
      :value: "CUSTOM_METRIC_TYPE_DRIFT"

.. autoclass:: MonitorNotifications
   :members:
   :undoc-members:

.. autoclass:: MonitorRefreshInfo
   :members:
   :undoc-members:

.. py:class:: MonitorRefreshInfoState

   The current state of the refresh.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SUCCESS
      :value: "SUCCESS"

.. py:class:: MonitorRefreshInfoTrigger

   The method by which the refresh was triggered.

   .. py:attribute:: MANUAL
      :value: "MANUAL"

   .. py:attribute:: SCHEDULE
      :value: "SCHEDULE"

.. autoclass:: MonitorRefreshListResponse
   :members:
   :undoc-members:

.. autoclass:: MonitorSnapshot
   :members:
   :undoc-members:

.. autoclass:: MonitorTimeSeries
   :members:
   :undoc-members:

.. autoclass:: NamedTableConstraint
   :members:
   :undoc-members:

.. autoclass:: OnlineTable
   :members:
   :undoc-members:

.. autoclass:: OnlineTableSpec
   :members:
   :undoc-members:

.. autoclass:: OnlineTableSpecContinuousSchedulingPolicy
   :members:
   :undoc-members:

.. autoclass:: OnlineTableSpecTriggeredSchedulingPolicy
   :members:
   :undoc-members:

.. py:class:: OnlineTableState

   The state of an online table.

   .. py:attribute:: OFFLINE
      :value: "OFFLINE"

   .. py:attribute:: OFFLINE_FAILED
      :value: "OFFLINE_FAILED"

   .. py:attribute:: ONLINE
      :value: "ONLINE"

   .. py:attribute:: ONLINE_CONTINUOUS_UPDATE
      :value: "ONLINE_CONTINUOUS_UPDATE"

   .. py:attribute:: ONLINE_NO_PENDING_UPDATE
      :value: "ONLINE_NO_PENDING_UPDATE"

   .. py:attribute:: ONLINE_PIPELINE_FAILED
      :value: "ONLINE_PIPELINE_FAILED"

   .. py:attribute:: ONLINE_TABLE_STATE_UNSPECIFIED
      :value: "ONLINE_TABLE_STATE_UNSPECIFIED"

   .. py:attribute:: ONLINE_TRIGGERED_UPDATE
      :value: "ONLINE_TRIGGERED_UPDATE"

   .. py:attribute:: ONLINE_UPDATING_PIPELINE_RESOURCES
      :value: "ONLINE_UPDATING_PIPELINE_RESOURCES"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

   .. py:attribute:: PROVISIONING_INITIAL_SNAPSHOT
      :value: "PROVISIONING_INITIAL_SNAPSHOT"

   .. py:attribute:: PROVISIONING_PIPELINE_RESOURCES
      :value: "PROVISIONING_PIPELINE_RESOURCES"

.. autoclass:: OnlineTableStatus
   :members:
   :undoc-members:

.. autoclass:: PermissionsChange
   :members:
   :undoc-members:

.. autoclass:: PermissionsList
   :members:
   :undoc-members:

.. autoclass:: PipelineProgress
   :members:
   :undoc-members:

.. autoclass:: PrimaryKeyConstraint
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

   .. py:attribute:: SINGLE_USER_ACCESS
      :value: "SINGLE_USER_ACCESS"

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

.. autoclass:: ProvisioningInfo
   :members:
   :undoc-members:

.. py:class:: ProvisioningInfoState

   .. py:attribute:: ACTIVE
      :value: "ACTIVE"

   .. py:attribute:: DELETING
      :value: "DELETING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: PROVISIONING
      :value: "PROVISIONING"

   .. py:attribute:: STATE_UNSPECIFIED
      :value: "STATE_UNSPECIFIED"

.. autoclass:: ProvisioningStatus
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelAlias
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelInfo
   :members:
   :undoc-members:

.. autoclass:: SchemaInfo
   :members:
   :undoc-members:

.. py:class:: SecurableType

   The type of Unity Catalog securable

   .. py:attribute:: CATALOG
      :value: "CATALOG"

   .. py:attribute:: CONNECTION
      :value: "CONNECTION"

   .. py:attribute:: EXTERNAL_LOCATION
      :value: "EXTERNAL_LOCATION"

   .. py:attribute:: FUNCTION
      :value: "FUNCTION"

   .. py:attribute:: METASTORE
      :value: "METASTORE"

   .. py:attribute:: PIPELINE
      :value: "PIPELINE"

   .. py:attribute:: PROVIDER
      :value: "PROVIDER"

   .. py:attribute:: RECIPIENT
      :value: "RECIPIENT"

   .. py:attribute:: SCHEMA
      :value: "SCHEMA"

   .. py:attribute:: SHARE
      :value: "SHARE"

   .. py:attribute:: STORAGE_CREDENTIAL
      :value: "STORAGE_CREDENTIAL"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. autoclass:: SetArtifactAllowlist
   :members:
   :undoc-members:

.. autoclass:: SetRegisteredModelAliasRequest
   :members:
   :undoc-members:

.. autoclass:: SseEncryptionDetails
   :members:
   :undoc-members:

.. py:class:: SseEncryptionDetailsAlgorithm

   The type of key encryption to use (affects headers from s3 client).

   .. py:attribute:: AWS_SSE_KMS
      :value: "AWS_SSE_KMS"

   .. py:attribute:: AWS_SSE_S3
      :value: "AWS_SSE_S3"

.. autoclass:: StorageCredentialInfo
   :members:
   :undoc-members:

.. autoclass:: SystemSchemaInfo
   :members:
   :undoc-members:

.. py:class:: SystemSchemaInfoState

   The current state of enablement for the system schema. An empty string means the system schema is available and ready for opt-in.

   .. py:attribute:: AVAILABLE
      :value: "AVAILABLE"

   .. py:attribute:: DISABLE_INITIALIZED
      :value: "DISABLE_INITIALIZED"

   .. py:attribute:: ENABLE_COMPLETED
      :value: "ENABLE_COMPLETED"

   .. py:attribute:: ENABLE_INITIALIZED
      :value: "ENABLE_INITIALIZED"

   .. py:attribute:: UNAVAILABLE
      :value: "UNAVAILABLE"

.. autoclass:: TableConstraint
   :members:
   :undoc-members:

.. autoclass:: TableDependency
   :members:
   :undoc-members:

.. autoclass:: TableExistsResponse
   :members:
   :undoc-members:

.. autoclass:: TableInfo
   :members:
   :undoc-members:

.. autoclass:: TableRowFilter
   :members:
   :undoc-members:

.. autoclass:: TableSummary
   :members:
   :undoc-members:

.. py:class:: TableType

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: EXTERNAL_SHALLOW_CLONE
      :value: "EXTERNAL_SHALLOW_CLONE"

   .. py:attribute:: FOREIGN
      :value: "FOREIGN"

   .. py:attribute:: MANAGED
      :value: "MANAGED"

   .. py:attribute:: MANAGED_SHALLOW_CLONE
      :value: "MANAGED_SHALLOW_CLONE"

   .. py:attribute:: MATERIALIZED_VIEW
      :value: "MATERIALIZED_VIEW"

   .. py:attribute:: STREAMING_TABLE
      :value: "STREAMING_TABLE"

   .. py:attribute:: VIEW
      :value: "VIEW"

.. autoclass:: TriggeredUpdateStatus
   :members:
   :undoc-members:

.. autoclass:: UnassignResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateAssignmentResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateCatalog
   :members:
   :undoc-members:

.. autoclass:: UpdateConnection
   :members:
   :undoc-members:

.. autoclass:: UpdateExternalLocation
   :members:
   :undoc-members:

.. autoclass:: UpdateFunction
   :members:
   :undoc-members:

.. autoclass:: UpdateMetastore
   :members:
   :undoc-members:

.. autoclass:: UpdateMetastoreAssignment
   :members:
   :undoc-members:

.. py:class:: UpdateMetastoreDeltaSharingScope

   The scope of Delta Sharing enabled for the metastore.

   .. py:attribute:: INTERNAL
      :value: "INTERNAL"

   .. py:attribute:: INTERNAL_AND_EXTERNAL
      :value: "INTERNAL_AND_EXTERNAL"

.. autoclass:: UpdateModelVersionRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateMonitor
   :members:
   :undoc-members:

.. autoclass:: UpdatePermissions
   :members:
   :undoc-members:

.. autoclass:: UpdateRegisteredModelRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateSchema
   :members:
   :undoc-members:

.. autoclass:: UpdateStorageCredential
   :members:
   :undoc-members:

.. autoclass:: UpdateVolumeRequestContent
   :members:
   :undoc-members:

.. autoclass:: UpdateWorkspaceBindings
   :members:
   :undoc-members:

.. autoclass:: UpdateWorkspaceBindingsParameters
   :members:
   :undoc-members:

.. autoclass:: ValidateStorageCredential
   :members:
   :undoc-members:

.. autoclass:: ValidateStorageCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: ValidationResult
   :members:
   :undoc-members:

.. py:class:: ValidationResultOperation

   The operation tested.

   .. py:attribute:: DELETE
      :value: "DELETE"

   .. py:attribute:: LIST
      :value: "LIST"

   .. py:attribute:: PATH_EXISTS
      :value: "PATH_EXISTS"

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: WRITE
      :value: "WRITE"

.. py:class:: ValidationResultResult

   The results of the tested operation.

   .. py:attribute:: FAIL
      :value: "FAIL"

   .. py:attribute:: PASS
      :value: "PASS"

   .. py:attribute:: SKIP
      :value: "SKIP"

.. autoclass:: VolumeInfo
   :members:
   :undoc-members:

.. py:class:: VolumeType

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: MANAGED
      :value: "MANAGED"

.. autoclass:: WorkspaceBinding
   :members:
   :undoc-members:

.. py:class:: WorkspaceBindingBindingType

   .. py:attribute:: BINDING_TYPE_READ_ONLY
      :value: "BINDING_TYPE_READ_ONLY"

   .. py:attribute:: BINDING_TYPE_READ_WRITE
      :value: "BINDING_TYPE_READ_WRITE"

.. autoclass:: WorkspaceBindingsResponse
   :members:
   :undoc-members:

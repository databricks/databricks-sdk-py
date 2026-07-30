Unity Catalog
=============

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.catalog`` module.

.. py:currentmodule:: databricks.sdk.service.catalog
.. autoclass:: AccessRequestDestinations
   :members:
   :undoc-members:

.. autoclass:: AccountsCreateMetastoreAssignmentResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsCreateMetastoreResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsCreateStorageCredentialInfo
   :members:
   :undoc-members:

.. autoclass:: AccountsDeleteMetastoreAssignmentResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsDeleteMetastoreResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsDeleteStorageCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsGetMetastoreResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsListMetastoresResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: AccountsStorageCredentialInfo
   :members:
   :undoc-members:

.. autoclass:: AccountsUpdateMetastoreAssignmentResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsUpdateMetastoreResponse
   :members:
   :undoc-members:

.. autoclass:: AccountsUpdateStorageCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: AgentService
   :members:
   :undoc-members:

.. py:class:: AgentServiceAgentServiceType

   Type of agent service. Determines how the backing agent surface is provisioned and how invocation routes to the runtime. Nested to scope enum values (guardrail: avoid-generic-enum-names).

   .. py:attribute:: AGENT_SERVICE_TYPE_EXTERNAL
      :value: "AGENT_SERVICE_TYPE_EXTERNAL"

.. autoclass:: AgentServiceConfig
   :members:
   :undoc-members:

.. autoclass:: AgentServiceConfigSourceConnection
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

.. autoclass:: AwsCredentials
   :members:
   :undoc-members:

.. autoclass:: AwsIamRole
   :members:
   :undoc-members:

.. autoclass:: AwsIamRoleRequest
   :members:
   :undoc-members:

.. autoclass:: AwsIamRoleResponse
   :members:
   :undoc-members:

.. autoclass:: AwsSqsQueue
   :members:
   :undoc-members:

.. autoclass:: AzureActiveDirectoryToken
   :members:
   :undoc-members:

.. autoclass:: AzureEncryptionSettings
   :members:
   :undoc-members:

.. autoclass:: AzureManagedIdentity
   :members:
   :undoc-members:

.. autoclass:: AzureManagedIdentityRequest
   :members:
   :undoc-members:

.. autoclass:: AzureManagedIdentityResponse
   :members:
   :undoc-members:

.. autoclass:: AzureQueueStorage
   :members:
   :undoc-members:

.. autoclass:: AzureServicePrincipal
   :members:
   :undoc-members:

.. autoclass:: AzureUserDelegationSas
   :members:
   :undoc-members:

.. autoclass:: BatchCreateAccessRequestsResponse
   :members:
   :undoc-members:

.. autoclass:: CancelRefreshResponse
   :members:
   :undoc-members:

.. autoclass:: CatalogFederationConfig
   :members:
   :undoc-members:

.. autoclass:: CatalogInfo
   :members:
   :undoc-members:

.. py:class:: CatalogIsolationMode

   .. py:attribute:: ISOLATED
      :value: "ISOLATED"

   .. py:attribute:: OPEN
      :value: "OPEN"

   .. py:attribute:: OPEN_IN_ACCOUNT
      :value: "OPEN_IN_ACCOUNT"

.. py:class:: CatalogType

   The type of the catalog.

   .. py:attribute:: DELTASHARING_CATALOG
      :value: "DELTASHARING_CATALOG"

   .. py:attribute:: FOREIGN_CATALOG
      :value: "FOREIGN_CATALOG"

   .. py:attribute:: INTERNAL_CATALOG
      :value: "INTERNAL_CATALOG"

   .. py:attribute:: MANAGED_CATALOG
      :value: "MANAGED_CATALOG"

   .. py:attribute:: MANAGED_ONLINE_CATALOG
      :value: "MANAGED_ONLINE_CATALOG"

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

.. autoclass:: ColumnMaskOptions
   :members:
   :undoc-members:

.. autoclass:: ColumnRelationship
   :members:
   :undoc-members:

.. autoclass:: ColumnTagValueExtraction
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

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: FLOAT
      :value: "FLOAT"

   .. py:attribute:: GEOGRAPHY
      :value: "GEOGRAPHY"

   .. py:attribute:: GEOMETRY
      :value: "GEOMETRY"

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

   .. py:attribute:: TABLEREF_TYPE
      :value: "TABLEREF_TYPE"

   .. py:attribute:: TABLE_TYPE
      :value: "TABLE_TYPE"

   .. py:attribute:: TIME
      :value: "TIME"

   .. py:attribute:: TIMESTAMP
      :value: "TIMESTAMP"

   .. py:attribute:: TIMESTAMP_NTZ
      :value: "TIMESTAMP_NTZ"

   .. py:attribute:: USER_DEFINED_TYPE
      :value: "USER_DEFINED_TYPE"

   .. py:attribute:: VARIANT
      :value: "VARIANT"

.. autoclass:: ConditionalDisplay
   :members:
   :undoc-members:

.. autoclass:: ConnectionDependency
   :members:
   :undoc-members:

.. autoclass:: ConnectionInfo
   :members:
   :undoc-members:

.. py:class:: ConnectionType

   .. py:attribute:: ADOBE_COMMERCE
      :value: "ADOBE_COMMERCE"

   .. py:attribute:: ADP_WORKFORCE_NOW
      :value: "ADP_WORKFORCE_NOW"

   .. py:attribute:: AHA
      :value: "AHA"

   .. py:attribute:: AIRTABLE
      :value: "AIRTABLE"

   .. py:attribute:: AMPLITUDE
      :value: "AMPLITUDE"

   .. py:attribute:: APPFIGURES
      :value: "APPFIGURES"

   .. py:attribute:: APPLE_APP_STORE
      :value: "APPLE_APP_STORE"

   .. py:attribute:: APPLE_SEARCH_ADS
      :value: "APPLE_SEARCH_ADS"

   .. py:attribute:: ATLASSIAN_ORGANIZATION
      :value: "ATLASSIAN_ORGANIZATION"

   .. py:attribute:: AWIN
      :value: "AWIN"

   .. py:attribute:: AZURE_MONITOR_LOGS
      :value: "AZURE_MONITOR_LOGS"

   .. py:attribute:: BIGLAKE
      :value: "BIGLAKE"

   .. py:attribute:: BIGQUERY
      :value: "BIGQUERY"

   .. py:attribute:: CERIDIAN_DAYFORCE
      :value: "CERIDIAN_DAYFORCE"

   .. py:attribute:: CONFLUENCE
      :value: "CONFLUENCE"

   .. py:attribute:: DATABRICKS
      :value: "DATABRICKS"

   .. py:attribute:: DELIGHTED
      :value: "DELIGHTED"

   .. py:attribute:: DYNAMICS365
      :value: "DYNAMICS365"

   .. py:attribute:: EPIC_CLARITY
      :value: "EPIC_CLARITY"

   .. py:attribute:: FRESHSERVICE
      :value: "FRESHSERVICE"

   .. py:attribute:: FRONT
      :value: "FRONT"

   .. py:attribute:: GA4_RAW_DATA
      :value: "GA4_RAW_DATA"

   .. py:attribute:: GENESYS
      :value: "GENESYS"

   .. py:attribute:: GITHUB
      :value: "GITHUB"

   .. py:attribute:: GITLAB
      :value: "GITLAB"

   .. py:attribute:: GLUE
      :value: "GLUE"

   .. py:attribute:: GMAIL
      :value: "GMAIL"

   .. py:attribute:: GONG
      :value: "GONG"

   .. py:attribute:: GOOGLE_ANALYTICS
      :value: "GOOGLE_ANALYTICS"

   .. py:attribute:: GOOGLE_CALENDAR
      :value: "GOOGLE_CALENDAR"

   .. py:attribute:: GOOGLE_CLOUD_LAKEHOUSE
      :value: "GOOGLE_CLOUD_LAKEHOUSE"

   .. py:attribute:: GOOGLE_WORKSPACE
      :value: "GOOGLE_WORKSPACE"

   .. py:attribute:: GURU
      :value: "GURU"

   .. py:attribute:: HIBOB
      :value: "HIBOB"

   .. py:attribute:: HIVE_METASTORE
      :value: "HIVE_METASTORE"

   .. py:attribute:: HTTP
      :value: "HTTP"

   .. py:attribute:: HUBSPOT
      :value: "HUBSPOT"

   .. py:attribute:: ICEBERG_REST
      :value: "ICEBERG_REST"

   .. py:attribute:: IRONCLAD
      :value: "IRONCLAD"

   .. py:attribute:: JDBC
      :value: "JDBC"

   .. py:attribute:: KINESIS
      :value: "KINESIS"

   .. py:attribute:: LINEAR
      :value: "LINEAR"

   .. py:attribute:: MARKETO
      :value: "MARKETO"

   .. py:attribute:: META_MARKETING
      :value: "META_MARKETING"

   .. py:attribute:: MICROSOFT_ENTRA_ID
      :value: "MICROSOFT_ENTRA_ID"

   .. py:attribute:: MONDAY_COM
      :value: "MONDAY_COM"

   .. py:attribute:: MYSQL
      :value: "MYSQL"

   .. py:attribute:: NETSKOPE_LOGS
      :value: "NETSKOPE_LOGS"

   .. py:attribute:: NOTION
      :value: "NOTION"

   .. py:attribute:: ORACLE
      :value: "ORACLE"

   .. py:attribute:: ORACLE_ELOQUA
      :value: "ORACLE_ELOQUA"

   .. py:attribute:: ORACLE_FUSION_CLOUD
      :value: "ORACLE_FUSION_CLOUD"

   .. py:attribute:: OUTLOOK
      :value: "OUTLOOK"

   .. py:attribute:: PAGERDUTY
      :value: "PAGERDUTY"

   .. py:attribute:: PALANTIR
      :value: "PALANTIR"

   .. py:attribute:: PARTNERSTACK
      :value: "PARTNERSTACK"

   .. py:attribute:: PENDO
      :value: "PENDO"

   .. py:attribute:: POSTGRESQL
      :value: "POSTGRESQL"

   .. py:attribute:: POWER_BI
      :value: "POWER_BI"

   .. py:attribute:: PUBSUB
      :value: "PUBSUB"

   .. py:attribute:: QUICKBOOKS
      :value: "QUICKBOOKS"

   .. py:attribute:: REDSHIFT
      :value: "REDSHIFT"

   .. py:attribute:: SALESFORCE
      :value: "SALESFORCE"

   .. py:attribute:: SALESFORCE_DATA_CLOUD
      :value: "SALESFORCE_DATA_CLOUD"

   .. py:attribute:: SALESLOFT
      :value: "SALESLOFT"

   .. py:attribute:: SAP_SUCCESSFACTORS
      :value: "SAP_SUCCESSFACTORS"

   .. py:attribute:: SAS
      :value: "SAS"

   .. py:attribute:: SENDGRID
      :value: "SENDGRID"

   .. py:attribute:: SERVICENOW
      :value: "SERVICENOW"

   .. py:attribute:: SHOPIFY
      :value: "SHOPIFY"

   .. py:attribute:: SLACK_ACCESS_AND_INTEGRATION_LOGS
      :value: "SLACK_ACCESS_AND_INTEGRATION_LOGS"

   .. py:attribute:: SMARTSHEET
      :value: "SMARTSHEET"

   .. py:attribute:: SNAPCHAT_ADS
      :value: "SNAPCHAT_ADS"

   .. py:attribute:: SNOWFLAKE
      :value: "SNOWFLAKE"

   .. py:attribute:: SPLUNK
      :value: "SPLUNK"

   .. py:attribute:: SQLDW
      :value: "SQLDW"

   .. py:attribute:: SQLSERVER
      :value: "SQLSERVER"

   .. py:attribute:: SQUARE
      :value: "SQUARE"

   .. py:attribute:: TERADATA
      :value: "TERADATA"

   .. py:attribute:: UNKNOWN_CONNECTION_TYPE
      :value: "UNKNOWN_CONNECTION_TYPE"

   .. py:attribute:: VERKADA
      :value: "VERKADA"

   .. py:attribute:: WORKDAY_RAAS
      :value: "WORKDAY_RAAS"

   .. py:attribute:: YOUTUBE_ANALYTICS
      :value: "YOUTUBE_ANALYTICS"

   .. py:attribute:: ZENDESK
      :value: "ZENDESK"

   .. py:attribute:: ZIP
      :value: "ZIP"

   .. py:attribute:: ZOHO_BOOKS
      :value: "ZOHO_BOOKS"

   .. py:attribute:: ZOOM
      :value: "ZOOM"

   .. py:attribute:: ZOOM_LOGS
      :value: "ZOOM_LOGS"

.. autoclass:: ContinuousUpdateStatus
   :members:
   :undoc-members:

.. autoclass:: ConversionInfo
   :members:
   :undoc-members:

.. py:class:: ConversionInfoState

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: IN_PROGRESS
      :value: "IN_PROGRESS"

.. autoclass:: CreateAccessRequest
   :members:
   :undoc-members:

.. autoclass:: CreateAccessRequestResponse
   :members:
   :undoc-members:

.. autoclass:: CreateAccountsMetastore
   :members:
   :undoc-members:

.. autoclass:: CreateAccountsStorageCredential
   :members:
   :undoc-members:

.. autoclass:: CreateFunction
   :members:
   :undoc-members:

.. py:class:: CreateFunctionParameterStyle

   .. py:attribute:: S
      :value: "S"

.. py:class:: CreateFunctionRoutineBody

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: SQL
      :value: "SQL"

.. py:class:: CreateFunctionSecurityType

   .. py:attribute:: DEFINER
      :value: "DEFINER"

.. py:class:: CreateFunctionSqlDataAccess

   .. py:attribute:: CONTAINS_SQL
      :value: "CONTAINS_SQL"

   .. py:attribute:: NO_SQL
      :value: "NO_SQL"

   .. py:attribute:: READS_SQL_DATA
      :value: "READS_SQL_DATA"

.. autoclass:: CreateMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: CreateRequestExternalLineage
   :members:
   :undoc-members:

.. autoclass:: CredentialDependency
   :members:
   :undoc-members:

.. autoclass:: CredentialInfo
   :members:
   :undoc-members:

.. py:class:: CredentialPurpose

   .. py:attribute:: SERVICE
      :value: "SERVICE"

   .. py:attribute:: STORAGE
      :value: "STORAGE"

.. py:class:: CredentialType

   .. py:attribute:: ANY_STATIC_CREDENTIAL
      :value: "ANY_STATIC_CREDENTIAL"

   .. py:attribute:: BEARER_TOKEN
      :value: "BEARER_TOKEN"

   .. py:attribute:: EDGEGRID_AKAMAI
      :value: "EDGEGRID_AKAMAI"

   .. py:attribute:: GENERIC_TOKEN_EXCHANGE
      :value: "GENERIC_TOKEN_EXCHANGE"

   .. py:attribute:: INLINE_YAML
      :value: "INLINE_YAML"

   .. py:attribute:: OAUTH_ACCESS_TOKEN
      :value: "OAUTH_ACCESS_TOKEN"

   .. py:attribute:: OAUTH_DCR
      :value: "OAUTH_DCR"

   .. py:attribute:: OAUTH_GOOGLE_SERVICE_ACCOUNT
      :value: "OAUTH_GOOGLE_SERVICE_ACCOUNT"

   .. py:attribute:: OAUTH_M2M
      :value: "OAUTH_M2M"

   .. py:attribute:: OAUTH_MTLS
      :value: "OAUTH_MTLS"

   .. py:attribute:: OAUTH_REFRESH_TOKEN
      :value: "OAUTH_REFRESH_TOKEN"

   .. py:attribute:: OAUTH_RESOURCE_OWNER_PASSWORD
      :value: "OAUTH_RESOURCE_OWNER_PASSWORD"

   .. py:attribute:: OAUTH_U2M
      :value: "OAUTH_U2M"

   .. py:attribute:: OAUTH_U2M_MAPPING
      :value: "OAUTH_U2M_MAPPING"

   .. py:attribute:: OIDC_TOKEN
      :value: "OIDC_TOKEN"

   .. py:attribute:: PEM_PRIVATE_KEY
      :value: "PEM_PRIVATE_KEY"

   .. py:attribute:: SERVICE_CREDENTIAL
      :value: "SERVICE_CREDENTIAL"

   .. py:attribute:: SSWS_TOKEN
      :value: "SSWS_TOKEN"

   .. py:attribute:: UNKNOWN_CREDENTIAL_TYPE
      :value: "UNKNOWN_CREDENTIAL_TYPE"

   .. py:attribute:: USERNAME_PASSWORD
      :value: "USERNAME_PASSWORD"

.. autoclass:: CredentialValidationResult
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

   .. py:attribute:: DATABRICKS_ROW_STORE_FORMAT
      :value: "DATABRICKS_ROW_STORE_FORMAT"

   .. py:attribute:: DELTA
      :value: "DELTA"

   .. py:attribute:: DELTASHARING
      :value: "DELTASHARING"

   .. py:attribute:: DELTA_UNIFORM_HUDI
      :value: "DELTA_UNIFORM_HUDI"

   .. py:attribute:: DELTA_UNIFORM_ICEBERG
      :value: "DELTA_UNIFORM_ICEBERG"

   .. py:attribute:: HIVE
      :value: "HIVE"

   .. py:attribute:: ICEBERG
      :value: "ICEBERG"

   .. py:attribute:: JSON
      :value: "JSON"

   .. py:attribute:: MONGODB_FORMAT
      :value: "MONGODB_FORMAT"

   .. py:attribute:: MYSQL_FORMAT
      :value: "MYSQL_FORMAT"

   .. py:attribute:: NETSUITE_FORMAT
      :value: "NETSUITE_FORMAT"

   .. py:attribute:: ORACLE_FORMAT
      :value: "ORACLE_FORMAT"

   .. py:attribute:: ORC
      :value: "ORC"

   .. py:attribute:: PARQUET
      :value: "PARQUET"

   .. py:attribute:: POSTGRESQL_FORMAT
      :value: "POSTGRESQL_FORMAT"

   .. py:attribute:: REDSHIFT_FORMAT
      :value: "REDSHIFT_FORMAT"

   .. py:attribute:: SALESFORCE_DATA_CLOUD_FORMAT
      :value: "SALESFORCE_DATA_CLOUD_FORMAT"

   .. py:attribute:: SALESFORCE_FORMAT
      :value: "SALESFORCE_FORMAT"

   .. py:attribute:: SNOWFLAKE_FORMAT
      :value: "SNOWFLAKE_FORMAT"

   .. py:attribute:: SQLDW_FORMAT
      :value: "SQLDW_FORMAT"

   .. py:attribute:: SQLSERVER_FORMAT
      :value: "SQLSERVER_FORMAT"

   .. py:attribute:: TERADATA_FORMAT
      :value: "TERADATA_FORMAT"

   .. py:attribute:: TEXT
      :value: "TEXT"

   .. py:attribute:: UNITY_CATALOG
      :value: "UNITY_CATALOG"

   .. py:attribute:: VECTOR_INDEX_FORMAT
      :value: "VECTOR_INDEX_FORMAT"

   .. py:attribute:: WORKDAY_RAAS_FORMAT
      :value: "WORKDAY_RAAS_FORMAT"

.. autoclass:: DatabricksGcpServiceAccount
   :members:
   :undoc-members:

.. autoclass:: DatabricksGcpServiceAccountRequest
   :members:
   :undoc-members:

.. autoclass:: DatabricksGcpServiceAccountResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteMonitorResponse
   :members:
   :undoc-members:

.. autoclass:: DeletePolicyResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRequestExternalLineage
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteTableConstraintResponse
   :members:
   :undoc-members:

.. autoclass:: DeltaRuntimePropertiesKvPairs
   :members:
   :undoc-members:

.. py:class:: DeltaSharingScopeEnum

   .. py:attribute:: INTERNAL
      :value: "INTERNAL"

   .. py:attribute:: INTERNAL_AND_EXTERNAL
      :value: "INTERNAL_AND_EXTERNAL"

.. autoclass:: DenyOptions
   :members:
   :undoc-members:

.. autoclass:: Dependency
   :members:
   :undoc-members:

.. autoclass:: DependencyList
   :members:
   :undoc-members:

.. py:class:: DestinationType

   .. py:attribute:: EMAIL
      :value: "EMAIL"

   .. py:attribute:: GENERIC_WEBHOOK
      :value: "GENERIC_WEBHOOK"

   .. py:attribute:: MICROSOFT_TEAMS
      :value: "MICROSOFT_TEAMS"

   .. py:attribute:: SLACK
      :value: "SLACK"

   .. py:attribute:: URL
      :value: "URL"

.. autoclass:: DisableResponse
   :members:
   :undoc-members:

.. autoclass:: DrReplicationInfo
   :members:
   :undoc-members:

.. py:class:: DrReplicationStatus

   .. py:attribute:: DR_REPLICATION_STATUS_PRIMARY
      :value: "DR_REPLICATION_STATUS_PRIMARY"

   .. py:attribute:: DR_REPLICATION_STATUS_SECONDARY
      :value: "DR_REPLICATION_STATUS_SECONDARY"

.. autoclass:: EffectivePermissionsList
   :members:
   :undoc-members:

.. autoclass:: EffectivePredictiveOptimizationFlag
   :members:
   :undoc-members:

.. py:class:: EffectivePredictiveOptimizationFlagInheritedFromType

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

.. autoclass:: EncryptionSettings
   :members:
   :undoc-members:

.. autoclass:: EntityTagAssignment
   :members:
   :undoc-members:

.. autoclass:: EnvironmentSettings
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageExternalMetadata
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageExternalMetadataInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageFileInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageModelVersion
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageModelVersionInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageObject
   :members:
   :undoc-members:

.. autoclass:: ExternalLineagePath
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageRelationship
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageRelationshipInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageTable
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageTableInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageVolume
   :members:
   :undoc-members:

.. autoclass:: ExternalLineageVolumeInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalLocationInfo
   :members:
   :undoc-members:

.. autoclass:: ExternalMetadata
   :members:
   :undoc-members:

.. autoclass:: FailedStatus
   :members:
   :undoc-members:

.. autoclass:: FileEventQueue
   :members:
   :undoc-members:

.. autoclass:: ForeignKeyConstraint
   :members:
   :undoc-members:

.. autoclass:: FunctionArgExpression
   :members:
   :undoc-members:

.. autoclass:: FunctionArgument
   :members:
   :undoc-members:

.. autoclass:: FunctionDependency
   :members:
   :undoc-members:

.. autoclass:: FunctionInfo
   :members:
   :undoc-members:

.. py:class:: FunctionInfoParameterStyle

   .. py:attribute:: S
      :value: "S"

.. py:class:: FunctionInfoRoutineBody

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: SQL
      :value: "SQL"

.. py:class:: FunctionInfoSecurityType

   .. py:attribute:: DEFINER
      :value: "DEFINER"

.. py:class:: FunctionInfoSqlDataAccess

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

   .. py:attribute:: IN
      :value: "IN"

.. py:class:: FunctionParameterType

   .. py:attribute:: COLUMN
      :value: "COLUMN"

   .. py:attribute:: PARAM
      :value: "PARAM"

.. autoclass:: GcpOauthToken
   :members:
   :undoc-members:

.. autoclass:: GcpPubsub
   :members:
   :undoc-members:

.. autoclass:: GenerateTemporaryPathCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: GenerateTemporaryServiceCredentialAzureOptions
   :members:
   :undoc-members:

.. autoclass:: GenerateTemporaryServiceCredentialGcpOptions
   :members:
   :undoc-members:

.. autoclass:: GenerateTemporaryTableCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: GenerateTemporaryVolumeCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: GetCatalogWorkspaceBindingsResponse
   :members:
   :undoc-members:

.. autoclass:: GetMetastoreSummaryResponse
   :members:
   :undoc-members:

.. autoclass:: GetPermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: GetQuotaResponse
   :members:
   :undoc-members:

.. autoclass:: GetWorkspaceBindingsResponse
   :members:
   :undoc-members:

.. autoclass:: GrantOptions
   :members:
   :undoc-members:

.. autoclass:: InferenceTableConfig
   :members:
   :undoc-members:

.. py:class:: IsolationMode

   .. py:attribute:: ISOLATION_MODE_ISOLATED
      :value: "ISOLATION_MODE_ISOLATED"

   .. py:attribute:: ISOLATION_MODE_OPEN
      :value: "ISOLATION_MODE_OPEN"

   .. py:attribute:: ISOLATION_MODE_OPEN_IN_ACCOUNT
      :value: "ISOLATION_MODE_OPEN_IN_ACCOUNT"

.. py:class:: LineageDirection

   .. py:attribute:: DOWNSTREAM
      :value: "DOWNSTREAM"

   .. py:attribute:: UPSTREAM
      :value: "UPSTREAM"

.. autoclass:: ListAccountMetastoreAssignmentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAccountStorageCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAgentServicesResponse
   :members:
   :undoc-members:

.. autoclass:: ListCatalogsResponse
   :members:
   :undoc-members:

.. autoclass:: ListConnectionsResponse
   :members:
   :undoc-members:

.. autoclass:: ListCredentialsResponse
   :members:
   :undoc-members:

.. autoclass:: ListEffectivePrivilegeAssignmentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListEntityTagAssignmentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExternalLineageRelationshipsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExternalLocationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExternalMetadataResponse
   :members:
   :undoc-members:

.. autoclass:: ListFunctionsResponse
   :members:
   :undoc-members:

.. py:class:: ListMcpServicesRequestView

   Controls which fields are populated on each McpService in the response. The server treats unset / VIEW_UNSPECIFIED as BASIC. Callers needing the full configuration must request it explicitly with ``view = FULL``.

   .. py:attribute:: BASIC
      :value: "BASIC"

   .. py:attribute:: FULL
      :value: "FULL"

.. autoclass:: ListMcpServicesResponse
   :members:
   :undoc-members:

.. autoclass:: ListMetastoresResponse
   :members:
   :undoc-members:

.. py:class:: ListModelProviderServicesRequestView

   Controls which fields are populated on each ModelProviderService in the response. The server treats unset / VIEW_UNSPECIFIED as BASIC. Callers needing the full configuration must request it explicitly with ``view = FULL``.

   .. py:attribute:: BASIC
      :value: "BASIC"

   .. py:attribute:: FULL
      :value: "FULL"

.. autoclass:: ListModelProviderServicesResponse
   :members:
   :undoc-members:

.. py:class:: ListModelServicesRequestView

   Controls which fields are populated on each ModelService in the response. The server treats unset / VIEW_UNSPECIFIED as BASIC. Callers needing the full configuration must request it explicitly with ``view = FULL``.

   .. py:attribute:: BASIC
      :value: "BASIC"

   .. py:attribute:: FULL
      :value: "FULL"

.. autoclass:: ListModelServicesResponse
   :members:
   :undoc-members:

.. autoclass:: ListModelVersionsResponse
   :members:
   :undoc-members:

.. autoclass:: ListPoliciesResponse
   :members:
   :undoc-members:

.. autoclass:: ListPrivilegeAssignmentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListQuotasResponse
   :members:
   :undoc-members:

.. autoclass:: ListRegisteredModelsResponse
   :members:
   :undoc-members:

.. autoclass:: ListSchemasResponse
   :members:
   :undoc-members:

.. autoclass:: ListSecretsResponse
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

.. autoclass:: MatchColumn
   :members:
   :undoc-members:

.. py:class:: MatchType

   The artifact pattern matching type

   .. py:attribute:: PREFIX_MATCH
      :value: "PREFIX_MATCH"

.. autoclass:: McpService
   :members:
   :undoc-members:

.. autoclass:: McpServiceConfig
   :members:
   :undoc-members:

.. autoclass:: McpServiceConfigSourceConnection
   :members:
   :undoc-members:

.. autoclass:: MetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: MetastoreInfo
   :members:
   :undoc-members:

.. autoclass:: ModelProviderService
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAmazonBedrockProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAmazonBedrockProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAnthropicProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAnthropicProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAnthropicProviderRelayedConfig
   :members:
   :undoc-members:

.. py:class:: ModelProviderServiceConfigAnthropicProviderRelayedConfigAnthropicRelayedPlanType

   Which Anthropic subscription tier the relayed OAuth token belongs to. Immutable after Create (switching tiers changes which governance controls the platform enforces). Only MAX and TEAM_ENTERPRISE differ in the governance surface the gateway can enforce, not in how the token is relayed.

   .. py:attribute:: ANTHROPIC_RELAYED_PLAN_TYPE_MAX
      :value: "ANTHROPIC_RELAYED_PLAN_TYPE_MAX"

   .. py:attribute:: ANTHROPIC_RELAYED_PLAN_TYPE_TEAM_ENTERPRISE
      :value: "ANTHROPIC_RELAYED_PLAN_TYPE_TEAM_ENTERPRISE"

.. autoclass:: ModelProviderServiceConfigAwsAccessKey
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAzureOpenAiProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigAzureOpenAiProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigCustomProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigCustomProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigEntraServicePrincipal
   :members:
   :undoc-members:

.. py:class:: ModelProviderServiceConfigExternalModelProviderType

   External LLM provider for an EXTERNAL_FOUNDATION_MODEL destination.

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_AMAZON_BEDROCK
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_AMAZON_BEDROCK"

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_ANTHROPIC
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_ANTHROPIC"

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_AZURE_OPENAI
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_AZURE_OPENAI"

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_CUSTOM
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_CUSTOM"

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_GEMINI_ENTERPRISE
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_GEMINI_ENTERPRISE"

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_MICROSOFT_FOUNDRY
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_MICROSOFT_FOUNDRY"

   .. py:attribute:: EXTERNAL_MODEL_PROVIDER_TYPE_OPENAI
      :value: "EXTERNAL_MODEL_PROVIDER_TYPE_OPENAI"

.. autoclass:: ModelProviderServiceConfigGeminiEnterpriseProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigGeminiEnterpriseProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigMicrosoftFoundryProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigMicrosoftFoundryProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigModelTargetConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigOpenAiProviderConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigOpenAiProviderDirectConfig
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigProviderSecret
   :members:
   :undoc-members:

.. autoclass:: ModelProviderServiceConfigServiceCredential
   :members:
   :undoc-members:

.. autoclass:: ModelService
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfig
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfigDestinationConfig
   :members:
   :undoc-members:

.. py:class:: ModelServiceConfigDestinationConfigDestinationType

   Backing-model category for a model service destination.

   .. py:attribute:: DESTINATION_TYPE_EXTERNAL_FOUNDATION_MODEL
      :value: "DESTINATION_TYPE_EXTERNAL_FOUNDATION_MODEL"

   .. py:attribute:: DESTINATION_TYPE_PAY_PER_TOKEN_FOUNDATION_MODEL
      :value: "DESTINATION_TYPE_PAY_PER_TOKEN_FOUNDATION_MODEL"

   .. py:attribute:: DESTINATION_TYPE_PROVISIONED_THROUGHPUT_FOUNDATION_MODEL
      :value: "DESTINATION_TYPE_PROVISIONED_THROUGHPUT_FOUNDATION_MODEL"

.. autoclass:: ModelServiceConfigExternalModelConfig
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfigFallbackConfig
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfigPayPerTokenConfig
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfigProvisionedThroughputConfig
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfigRoutingConfig
   :members:
   :undoc-members:

.. autoclass:: ModelServiceConfigRoutingConfigTrafficSplitting
   :members:
   :undoc-members:

.. autoclass:: ModelVersionInfo
   :members:
   :undoc-members:

.. py:class:: ModelVersionInfoStatus

   .. py:attribute:: FAILED_REGISTRATION
      :value: "FAILED_REGISTRATION"

   .. py:attribute:: MODEL_VERSION_STATUS_UNKNOWN
      :value: "MODEL_VERSION_STATUS_UNKNOWN"

   .. py:attribute:: PENDING_REGISTRATION
      :value: "PENDING_REGISTRATION"

   .. py:attribute:: READY
      :value: "READY"

.. autoclass:: MonitorCronSchedule
   :members:
   :undoc-members:

.. py:class:: MonitorCronSchedulePauseStatus

   Source link: https://src.dev.databricks.com/databricks/universe/-/blob/elastic-spark-common/api/messages/schedule.proto Monitoring workflow schedule pause status.

   .. py:attribute:: PAUSED
      :value: "PAUSED"

   .. py:attribute:: UNPAUSED
      :value: "UNPAUSED"

   .. py:attribute:: UNSPECIFIED
      :value: "UNSPECIFIED"

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

   .. py:attribute:: PROBLEM_TYPE_CLASSIFICATION
      :value: "PROBLEM_TYPE_CLASSIFICATION"

   .. py:attribute:: PROBLEM_TYPE_REGRESSION
      :value: "PROBLEM_TYPE_REGRESSION"

.. autoclass:: MonitorInfo
   :members:
   :undoc-members:

.. py:class:: MonitorInfoStatus

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

   Can only be one of ``"CUSTOM_METRIC_TYPE_AGGREGATE"``, ``"CUSTOM_METRIC_TYPE_DERIVED"``, or ``"CUSTOM_METRIC_TYPE_DRIFT"``. The ``"CUSTOM_METRIC_TYPE_AGGREGATE"`` and ``"CUSTOM_METRIC_TYPE_DERIVED"`` metrics are computed on a single table, whereas the ``"CUSTOM_METRIC_TYPE_DRIFT"`` compare metrics across baseline and input table, or across the two consecutive time windows.
   - CUSTOM_METRIC_TYPE_AGGREGATE: only depend on the existing columns in your table - CUSTOM_METRIC_TYPE_DERIVED: depend on previously computed aggregate metrics - CUSTOM_METRIC_TYPE_DRIFT: depend on previously computed aggregate or derived metrics

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

   .. py:attribute:: UNKNOWN
      :value: "UNKNOWN"

.. py:class:: MonitorRefreshInfoTrigger

   .. py:attribute:: MANUAL
      :value: "MANUAL"

   .. py:attribute:: SCHEDULE
      :value: "SCHEDULE"

   .. py:attribute:: UNKNOWN_TRIGGER
      :value: "UNKNOWN_TRIGGER"

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

.. autoclass:: NotificationDestination
   :members:
   :undoc-members:

.. autoclass:: OneLakeEventQueue
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

.. autoclass:: OptionSpec
   :members:
   :undoc-members:

.. py:class:: OptionSpecOauthStage

   During the OAuth flow, specifies which stage the option should be displayed in the UI. OAUTH_STAGE_UNSPECIFIED is the default value for options unrelated to the OAuth flow. BEFORE_AUTHORIZATION_CODE corresponds to options necessary to initiate the OAuth process. BEFORE_ACCESS_TOKEN corresponds to options that are necessary to create a foreign connection, but that should be displayed after the authorization code has already been received.

   .. py:attribute:: BEFORE_ACCESS_TOKEN
      :value: "BEFORE_ACCESS_TOKEN"

   .. py:attribute:: BEFORE_AUTHORIZATION_CODE
      :value: "BEFORE_AUTHORIZATION_CODE"

.. py:class:: OptionSpecOptionType

   Type of the option, we purposely follow JavaScript types so that the UI can map the options to JS types. https://www.w3schools.com/js/js_datatypes.asp Enum is a special case that it's just string with selections.

   .. py:attribute:: OPTION_BIGINT
      :value: "OPTION_BIGINT"

   .. py:attribute:: OPTION_BOOLEAN
      :value: "OPTION_BOOLEAN"

   .. py:attribute:: OPTION_ENUM
      :value: "OPTION_ENUM"

   .. py:attribute:: OPTION_MULTILINE_STRING
      :value: "OPTION_MULTILINE_STRING"

   .. py:attribute:: OPTION_NUMBER
      :value: "OPTION_NUMBER"

   .. py:attribute:: OPTION_SERVICE_CREDENTIAL
      :value: "OPTION_SERVICE_CREDENTIAL"

   .. py:attribute:: OPTION_STORAGE_CREDENTIAL
      :value: "OPTION_STORAGE_CREDENTIAL"

   .. py:attribute:: OPTION_STRING
      :value: "OPTION_STRING"

.. py:class:: PathOperation

   .. py:attribute:: PATH_CREATE_TABLE
      :value: "PATH_CREATE_TABLE"

   .. py:attribute:: PATH_READ
      :value: "PATH_READ"

   .. py:attribute:: PATH_READ_WRITE
      :value: "PATH_READ_WRITE"

.. autoclass:: PermissionsChange
   :members:
   :undoc-members:

.. autoclass:: PipelineProgress
   :members:
   :undoc-members:

.. autoclass:: PolicyFunctionArgument
   :members:
   :undoc-members:

.. autoclass:: PolicyInfo
   :members:
   :undoc-members:

.. py:class:: PolicyType

   .. py:attribute:: POLICY_TYPE_COLUMN_MASK
      :value: "POLICY_TYPE_COLUMN_MASK"

   .. py:attribute:: POLICY_TYPE_DENY
      :value: "POLICY_TYPE_DENY"

   .. py:attribute:: POLICY_TYPE_GRANT
      :value: "POLICY_TYPE_GRANT"

   .. py:attribute:: POLICY_TYPE_ROW_FILTER
      :value: "POLICY_TYPE_ROW_FILTER"

.. autoclass:: PrimaryKeyConstraint
   :members:
   :undoc-members:

.. autoclass:: Principal
   :members:
   :undoc-members:

.. py:class:: PrincipalType

   .. py:attribute:: GROUP_PRINCIPAL
      :value: "GROUP_PRINCIPAL"

   .. py:attribute:: SERVICE_PRINCIPAL
      :value: "SERVICE_PRINCIPAL"

   .. py:attribute:: USER_PRINCIPAL
      :value: "USER_PRINCIPAL"

.. py:class:: Privilege

   .. py:attribute:: ACCESS
      :value: "ACCESS"

   .. py:attribute:: ALL_PRIVILEGES
      :value: "ALL_PRIVILEGES"

   .. py:attribute:: APPLY_TAG
      :value: "APPLY_TAG"

   .. py:attribute:: BROWSE
      :value: "BROWSE"

   .. py:attribute:: CREATE
      :value: "CREATE"

   .. py:attribute:: CREATE_CASE_COLLECTION
      :value: "CREATE_CASE_COLLECTION"

   .. py:attribute:: CREATE_CATALOG
      :value: "CREATE_CATALOG"

   .. py:attribute:: CREATE_CLEAN_ROOM
      :value: "CREATE_CLEAN_ROOM"

   .. py:attribute:: CREATE_CONNECTION
      :value: "CREATE_CONNECTION"

   .. py:attribute:: CREATE_DATASOURCE
      :value: "CREATE_DATASOURCE"

   .. py:attribute:: CREATE_EXTERNAL_LOCATION
      :value: "CREATE_EXTERNAL_LOCATION"

   .. py:attribute:: CREATE_EXTERNAL_TABLE
      :value: "CREATE_EXTERNAL_TABLE"

   .. py:attribute:: CREATE_EXTERNAL_VOLUME
      :value: "CREATE_EXTERNAL_VOLUME"

   .. py:attribute:: CREATE_FEATURE
      :value: "CREATE_FEATURE"

   .. py:attribute:: CREATE_FLOW
      :value: "CREATE_FLOW"

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

   .. py:attribute:: CREATE_MEMORY_STORE
      :value: "CREATE_MEMORY_STORE"

   .. py:attribute:: CREATE_MODEL
      :value: "CREATE_MODEL"

   .. py:attribute:: CREATE_PROVIDER
      :value: "CREATE_PROVIDER"

   .. py:attribute:: CREATE_RECIPIENT
      :value: "CREATE_RECIPIENT"

   .. py:attribute:: CREATE_RULE
      :value: "CREATE_RULE"

   .. py:attribute:: CREATE_SCHEMA
      :value: "CREATE_SCHEMA"

   .. py:attribute:: CREATE_SEMANTIC_GRAPH
      :value: "CREATE_SEMANTIC_GRAPH"

   .. py:attribute:: CREATE_SERVICE
      :value: "CREATE_SERVICE"

   .. py:attribute:: CREATE_SERVICE_CREDENTIAL
      :value: "CREATE_SERVICE_CREDENTIAL"

   .. py:attribute:: CREATE_SHARE
      :value: "CREATE_SHARE"

   .. py:attribute:: CREATE_SKILL
      :value: "CREATE_SKILL"

   .. py:attribute:: CREATE_STORAGE_CREDENTIAL
      :value: "CREATE_STORAGE_CREDENTIAL"

   .. py:attribute:: CREATE_STREAM
      :value: "CREATE_STREAM"

   .. py:attribute:: CREATE_TABLE
      :value: "CREATE_TABLE"

   .. py:attribute:: CREATE_VIEW
      :value: "CREATE_VIEW"

   .. py:attribute:: CREATE_VOLUME
      :value: "CREATE_VOLUME"

   .. py:attribute:: DELETE
      :value: "DELETE"

   .. py:attribute:: DELETE_EVENTS
      :value: "DELETE_EVENTS"

   .. py:attribute:: DELETE_SECURITY_DATA
      :value: "DELETE_SECURITY_DATA"

   .. py:attribute:: EXECUTE
      :value: "EXECUTE"

   .. py:attribute:: EXECUTE_CLEAN_ROOM_TASK
      :value: "EXECUTE_CLEAN_ROOM_TASK"

   .. py:attribute:: EXTERNAL_USE_SCHEMA
      :value: "EXTERNAL_USE_SCHEMA"

   .. py:attribute:: INSERT
      :value: "INSERT"

   .. py:attribute:: INSERT_SECURITY_DATA
      :value: "INSERT_SECURITY_DATA"

   .. py:attribute:: MANAGE
      :value: "MANAGE"

   .. py:attribute:: MANAGE_ACCESS
      :value: "MANAGE_ACCESS"

   .. py:attribute:: MANAGE_ACCESS_CONTROL
      :value: "MANAGE_ACCESS_CONTROL"

   .. py:attribute:: MANAGE_ALLOWLIST
      :value: "MANAGE_ALLOWLIST"

   .. py:attribute:: MANAGE_GRANTS
      :value: "MANAGE_GRANTS"

   .. py:attribute:: MODIFY
      :value: "MODIFY"

   .. py:attribute:: MODIFY_CLEAN_ROOM
      :value: "MODIFY_CLEAN_ROOM"

   .. py:attribute:: READ_EVENTS
      :value: "READ_EVENTS"

   .. py:attribute:: READ_FEATURE
      :value: "READ_FEATURE"

   .. py:attribute:: READ_FILES
      :value: "READ_FILES"

   .. py:attribute:: READ_FLOW
      :value: "READ_FLOW"

   .. py:attribute:: READ_MEMORY_STORE
      :value: "READ_MEMORY_STORE"

   .. py:attribute:: READ_METADATA
      :value: "READ_METADATA"

   .. py:attribute:: READ_PRIVATE_FILES
      :value: "READ_PRIVATE_FILES"

   .. py:attribute:: READ_SECURITY_DATA
      :value: "READ_SECURITY_DATA"

   .. py:attribute:: READ_SEMANTIC_GRAPH
      :value: "READ_SEMANTIC_GRAPH"

   .. py:attribute:: READ_SKILL
      :value: "READ_SKILL"

   .. py:attribute:: READ_STREAM
      :value: "READ_STREAM"

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: REFRESH
      :value: "REFRESH"

   .. py:attribute:: SELECT
      :value: "SELECT"

   .. py:attribute:: SET_SHARE_PERMISSION
      :value: "SET_SHARE_PERMISSION"

   .. py:attribute:: UPDATE
      :value: "UPDATE"

   .. py:attribute:: UPDATE_EVENTS
      :value: "UPDATE_EVENTS"

   .. py:attribute:: UPDATE_SECURITY_DATA
      :value: "UPDATE_SECURITY_DATA"

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

   .. py:attribute:: USE_VOLUME
      :value: "USE_VOLUME"

   .. py:attribute:: VIEW_ADMIN_METADATA
      :value: "VIEW_ADMIN_METADATA"

   .. py:attribute:: VIEW_METADATA
      :value: "VIEW_METADATA"

   .. py:attribute:: VIEW_OBJECT
      :value: "VIEW_OBJECT"

   .. py:attribute:: WRITE_FILES
      :value: "WRITE_FILES"

   .. py:attribute:: WRITE_FLOW
      :value: "WRITE_FLOW"

   .. py:attribute:: WRITE_MEMORY_STORE
      :value: "WRITE_MEMORY_STORE"

   .. py:attribute:: WRITE_PRIVATE_FILES
      :value: "WRITE_PRIVATE_FILES"

   .. py:attribute:: WRITE_SEMANTIC_GRAPH
      :value: "WRITE_SEMANTIC_GRAPH"

   .. py:attribute:: WRITE_SKILL
      :value: "WRITE_SKILL"

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

.. autoclass:: ProvisioningStatus
   :members:
   :undoc-members:

.. autoclass:: QuotaInfo
   :members:
   :undoc-members:

.. autoclass:: R2Credentials
   :members:
   :undoc-members:

.. autoclass:: RateLimit
   :members:
   :undoc-members:

.. py:class:: RateLimitRateLimitKey

   Scope key for a rate limit.

   .. py:attribute:: RATE_LIMIT_KEY_REQUEST_TAG
      :value: "RATE_LIMIT_KEY_REQUEST_TAG"

   .. py:attribute:: RATE_LIMIT_KEY_SERVICE
      :value: "RATE_LIMIT_KEY_SERVICE"

   .. py:attribute:: RATE_LIMIT_KEY_SERVICE_PRINCIPAL
      :value: "RATE_LIMIT_KEY_SERVICE_PRINCIPAL"

   .. py:attribute:: RATE_LIMIT_KEY_USER
      :value: "RATE_LIMIT_KEY_USER"

   .. py:attribute:: RATE_LIMIT_KEY_USER_DEFAULT
      :value: "RATE_LIMIT_KEY_USER_DEFAULT"

   .. py:attribute:: RATE_LIMIT_KEY_USER_GROUP
      :value: "RATE_LIMIT_KEY_USER_GROUP"

.. py:class:: RateLimitRateLimitRenewalPeriod

   Renewal period for a rate limit.

   .. py:attribute:: RATE_LIMIT_RENEWAL_PERIOD_HOUR
      :value: "RATE_LIMIT_RENEWAL_PERIOD_HOUR"

   .. py:attribute:: RATE_LIMIT_RENEWAL_PERIOD_MINUTE
      :value: "RATE_LIMIT_RENEWAL_PERIOD_MINUTE"

.. autoclass:: RegenerateDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelAlias
   :members:
   :undoc-members:

.. autoclass:: RegisteredModelInfo
   :members:
   :undoc-members:

.. autoclass:: RowFilterOptions
   :members:
   :undoc-members:

.. py:class:: SchemaFilterType

   Determines how a FOREIGN catalog's schema filter items are interpreted.

   .. py:attribute:: SCHEMA_FILTER_TYPE_EXCLUDE
      :value: "SCHEMA_FILTER_TYPE_EXCLUDE"

   .. py:attribute:: SCHEMA_FILTER_TYPE_INCLUDE
      :value: "SCHEMA_FILTER_TYPE_INCLUDE"

   .. py:attribute:: SCHEMA_FILTER_TYPE_INCLUDE_ALL
      :value: "SCHEMA_FILTER_TYPE_INCLUDE_ALL"

.. autoclass:: SchemaInfo
   :members:
   :undoc-members:

.. autoclass:: Secret
   :members:
   :undoc-members:

.. autoclass:: SecretDependency
   :members:
   :undoc-members:

.. autoclass:: Securable
   :members:
   :undoc-members:

.. py:class:: SecurableKind

   .. py:attribute:: CATALOG_FOREIGN_BIGLAKE
      :value: "CATALOG_FOREIGN_BIGLAKE"

   .. py:attribute:: CATALOG_FOREIGN_GOOGLE_CLOUD_LAKEHOUSE
      :value: "CATALOG_FOREIGN_GOOGLE_CLOUD_LAKEHOUSE"

   .. py:attribute:: CATALOG_FOREIGN_ICEBERG_REST
      :value: "CATALOG_FOREIGN_ICEBERG_REST"

   .. py:attribute:: CONNECTION_BIGLAKE_SERVICE_ACCOUNT
      :value: "CONNECTION_BIGLAKE_SERVICE_ACCOUNT"

   .. py:attribute:: CONNECTION_COMMUNITY_OAUTH_M2M
      :value: "CONNECTION_COMMUNITY_OAUTH_M2M"

   .. py:attribute:: CONNECTION_COMMUNITY_OAUTH_U2M
      :value: "CONNECTION_COMMUNITY_OAUTH_U2M"

   .. py:attribute:: CONNECTION_COMMUNITY_OAUTH_U2M_MAPPING
      :value: "CONNECTION_COMMUNITY_OAUTH_U2M_MAPPING"

   .. py:attribute:: CONNECTION_GOOGLE_CLOUD_LAKEHOUSE_OAUTH_U2M
      :value: "CONNECTION_GOOGLE_CLOUD_LAKEHOUSE_OAUTH_U2M"

   .. py:attribute:: CONNECTION_GOOGLE_CLOUD_LAKEHOUSE_SERVICE_ACCOUNT
      :value: "CONNECTION_GOOGLE_CLOUD_LAKEHOUSE_SERVICE_ACCOUNT"

   .. py:attribute:: CONNECTION_ICEBERG_REST_BEARER_TOKEN
      :value: "CONNECTION_ICEBERG_REST_BEARER_TOKEN"

   .. py:attribute:: CONNECTION_ICEBERG_REST_OAUTH_M2M
      :value: "CONNECTION_ICEBERG_REST_OAUTH_M2M"

   .. py:attribute:: RECIPIENT_EMAIL
      :value: "RECIPIENT_EMAIL"

   .. py:attribute:: RECIPIENT_EMAIL_DATABRICKS
      :value: "RECIPIENT_EMAIL_DATABRICKS"

   .. py:attribute:: RECIPIENT_EMAIL_TOKEN
      :value: "RECIPIENT_EMAIL_TOKEN"

   .. py:attribute:: SCHEMA_FOREIGN_BIGLAKE
      :value: "SCHEMA_FOREIGN_BIGLAKE"

   .. py:attribute:: SCHEMA_FOREIGN_GOOGLE_CLOUD_LAKEHOUSE
      :value: "SCHEMA_FOREIGN_GOOGLE_CLOUD_LAKEHOUSE"

   .. py:attribute:: SCHEMA_FOREIGN_ICEBERG_REST
      :value: "SCHEMA_FOREIGN_ICEBERG_REST"

   .. py:attribute:: TABLE_DB_STORAGE
      :value: "TABLE_DB_STORAGE"

   .. py:attribute:: TABLE_DELTA
      :value: "TABLE_DELTA"

   .. py:attribute:: TABLE_DELTASHARING
      :value: "TABLE_DELTASHARING"

   .. py:attribute:: TABLE_DELTASHARING_MUTABLE
      :value: "TABLE_DELTASHARING_MUTABLE"

   .. py:attribute:: TABLE_DELTASHARING_OPEN_DIR_BASED
      :value: "TABLE_DELTASHARING_OPEN_DIR_BASED"

   .. py:attribute:: TABLE_DELTA_EXTERNAL
      :value: "TABLE_DELTA_EXTERNAL"

   .. py:attribute:: TABLE_DELTA_ICEBERG_DELTASHARING
      :value: "TABLE_DELTA_ICEBERG_DELTASHARING"

   .. py:attribute:: TABLE_DELTA_ICEBERG_MANAGED
      :value: "TABLE_DELTA_ICEBERG_MANAGED"

   .. py:attribute:: TABLE_DELTA_UNIFORM_HUDI_EXTERNAL
      :value: "TABLE_DELTA_UNIFORM_HUDI_EXTERNAL"

   .. py:attribute:: TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL
      :value: "TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL"

   .. py:attribute:: TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL_DELTASHARING
      :value: "TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL_DELTASHARING"

   .. py:attribute:: TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_DELTASHARING
      :value: "TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_DELTASHARING"

   .. py:attribute:: TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_EXTERNAL
      :value: "TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_EXTERNAL"

   .. py:attribute:: TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_MANAGED
      :value: "TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_MANAGED"

   .. py:attribute:: TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_SNOWFLAKE
      :value: "TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_SNOWFLAKE"

   .. py:attribute:: TABLE_EXTERNAL
      :value: "TABLE_EXTERNAL"

   .. py:attribute:: TABLE_FEATURE_STORE
      :value: "TABLE_FEATURE_STORE"

   .. py:attribute:: TABLE_FEATURE_STORE_EXTERNAL
      :value: "TABLE_FEATURE_STORE_EXTERNAL"

   .. py:attribute:: TABLE_FOREIGN_BIGLAKE
      :value: "TABLE_FOREIGN_BIGLAKE"

   .. py:attribute:: TABLE_FOREIGN_BIGQUERY
      :value: "TABLE_FOREIGN_BIGQUERY"

   .. py:attribute:: TABLE_FOREIGN_DATABRICKS
      :value: "TABLE_FOREIGN_DATABRICKS"

   .. py:attribute:: TABLE_FOREIGN_DELTASHARING
      :value: "TABLE_FOREIGN_DELTASHARING"

   .. py:attribute:: TABLE_FOREIGN_DELTA_DELTASHARING
      :value: "TABLE_FOREIGN_DELTA_DELTASHARING"

   .. py:attribute:: TABLE_FOREIGN_GOOGLE_CLOUD_LAKEHOUSE
      :value: "TABLE_FOREIGN_GOOGLE_CLOUD_LAKEHOUSE"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE
      :value: "TABLE_FOREIGN_HIVE_METASTORE"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_DBFS_EXTERNAL
      :value: "TABLE_FOREIGN_HIVE_METASTORE_DBFS_EXTERNAL"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_DBFS_MANAGED
      :value: "TABLE_FOREIGN_HIVE_METASTORE_DBFS_MANAGED"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_EXTERNAL
      :value: "TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_EXTERNAL"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_MANAGED
      :value: "TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_MANAGED"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_DBFS_VIEW
      :value: "TABLE_FOREIGN_HIVE_METASTORE_DBFS_VIEW"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_EXTERNAL
      :value: "TABLE_FOREIGN_HIVE_METASTORE_EXTERNAL"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_MANAGED
      :value: "TABLE_FOREIGN_HIVE_METASTORE_MANAGED"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_EXTERNAL
      :value: "TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_EXTERNAL"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_MANAGED
      :value: "TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_MANAGED"

   .. py:attribute:: TABLE_FOREIGN_HIVE_METASTORE_VIEW
      :value: "TABLE_FOREIGN_HIVE_METASTORE_VIEW"

   .. py:attribute:: TABLE_FOREIGN_ICEBERG_REST
      :value: "TABLE_FOREIGN_ICEBERG_REST"

   .. py:attribute:: TABLE_FOREIGN_MONGODB
      :value: "TABLE_FOREIGN_MONGODB"

   .. py:attribute:: TABLE_FOREIGN_MYSQL
      :value: "TABLE_FOREIGN_MYSQL"

   .. py:attribute:: TABLE_FOREIGN_NETSUITE
      :value: "TABLE_FOREIGN_NETSUITE"

   .. py:attribute:: TABLE_FOREIGN_ORACLE
      :value: "TABLE_FOREIGN_ORACLE"

   .. py:attribute:: TABLE_FOREIGN_PALANTIR
      :value: "TABLE_FOREIGN_PALANTIR"

   .. py:attribute:: TABLE_FOREIGN_POSTGRESQL
      :value: "TABLE_FOREIGN_POSTGRESQL"

   .. py:attribute:: TABLE_FOREIGN_REDSHIFT
      :value: "TABLE_FOREIGN_REDSHIFT"

   .. py:attribute:: TABLE_FOREIGN_SALESFORCE
      :value: "TABLE_FOREIGN_SALESFORCE"

   .. py:attribute:: TABLE_FOREIGN_SALESFORCE_DATA_CLOUD
      :value: "TABLE_FOREIGN_SALESFORCE_DATA_CLOUD"

   .. py:attribute:: TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING
      :value: "TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING"

   .. py:attribute:: TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING_VIEW
      :value: "TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING_VIEW"

   .. py:attribute:: TABLE_FOREIGN_SNOWFLAKE
      :value: "TABLE_FOREIGN_SNOWFLAKE"

   .. py:attribute:: TABLE_FOREIGN_SQLDW
      :value: "TABLE_FOREIGN_SQLDW"

   .. py:attribute:: TABLE_FOREIGN_SQLSERVER
      :value: "TABLE_FOREIGN_SQLSERVER"

   .. py:attribute:: TABLE_FOREIGN_TERADATA
      :value: "TABLE_FOREIGN_TERADATA"

   .. py:attribute:: TABLE_FOREIGN_WORKDAY_RAAS
      :value: "TABLE_FOREIGN_WORKDAY_RAAS"

   .. py:attribute:: TABLE_ICEBERG_UNIFORM_MANAGED
      :value: "TABLE_ICEBERG_UNIFORM_MANAGED"

   .. py:attribute:: TABLE_INTERNAL
      :value: "TABLE_INTERNAL"

   .. py:attribute:: TABLE_MANAGED_POSTGRESQL
      :value: "TABLE_MANAGED_POSTGRESQL"

   .. py:attribute:: TABLE_MATERIALIZED_VIEW
      :value: "TABLE_MATERIALIZED_VIEW"

   .. py:attribute:: TABLE_MATERIALIZED_VIEW_DELTASHARING
      :value: "TABLE_MATERIALIZED_VIEW_DELTASHARING"

   .. py:attribute:: TABLE_METRIC_VIEW
      :value: "TABLE_METRIC_VIEW"

   .. py:attribute:: TABLE_METRIC_VIEW_DELTASHARING
      :value: "TABLE_METRIC_VIEW_DELTASHARING"

   .. py:attribute:: TABLE_ONLINE_VECTOR_INDEX_DIRECT
      :value: "TABLE_ONLINE_VECTOR_INDEX_DIRECT"

   .. py:attribute:: TABLE_ONLINE_VECTOR_INDEX_REPLICA
      :value: "TABLE_ONLINE_VECTOR_INDEX_REPLICA"

   .. py:attribute:: TABLE_ONLINE_VIEW
      :value: "TABLE_ONLINE_VIEW"

   .. py:attribute:: TABLE_STANDARD
      :value: "TABLE_STANDARD"

   .. py:attribute:: TABLE_STREAMING_LIVE_TABLE
      :value: "TABLE_STREAMING_LIVE_TABLE"

   .. py:attribute:: TABLE_STREAMING_LIVE_TABLE_DELTASHARING
      :value: "TABLE_STREAMING_LIVE_TABLE_DELTASHARING"

   .. py:attribute:: TABLE_SYSTEM
      :value: "TABLE_SYSTEM"

   .. py:attribute:: TABLE_SYSTEM_DELTASHARING
      :value: "TABLE_SYSTEM_DELTASHARING"

   .. py:attribute:: TABLE_VIEW
      :value: "TABLE_VIEW"

   .. py:attribute:: TABLE_VIEW_DELTASHARING
      :value: "TABLE_VIEW_DELTASHARING"

.. autoclass:: SecurableKindManifest
   :members:
   :undoc-members:

.. autoclass:: SecurablePermissions
   :members:
   :undoc-members:

.. py:class:: SecurableType

   The type of Unity Catalog securable.

   .. py:attribute:: CATALOG
      :value: "CATALOG"

   .. py:attribute:: CLEAN_ROOM
      :value: "CLEAN_ROOM"

   .. py:attribute:: CONNECTION
      :value: "CONNECTION"

   .. py:attribute:: CREDENTIAL
      :value: "CREDENTIAL"

   .. py:attribute:: EXTERNAL_LOCATION
      :value: "EXTERNAL_LOCATION"

   .. py:attribute:: EXTERNAL_METADATA
      :value: "EXTERNAL_METADATA"

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

   .. py:attribute:: STAGING_TABLE
      :value: "STAGING_TABLE"

   .. py:attribute:: STORAGE_CREDENTIAL
      :value: "STORAGE_CREDENTIAL"

   .. py:attribute:: TABLE
      :value: "TABLE"

   .. py:attribute:: VOLUME
      :value: "VOLUME"

.. py:class:: SpecialDestination

   .. py:attribute:: SPECIAL_DESTINATION_CATALOG_OWNER
      :value: "SPECIAL_DESTINATION_CATALOG_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_CONNECTION_OWNER
      :value: "SPECIAL_DESTINATION_CONNECTION_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_CREDENTIAL_OWNER
      :value: "SPECIAL_DESTINATION_CREDENTIAL_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_EXTERNAL_LOCATION_OWNER
      :value: "SPECIAL_DESTINATION_EXTERNAL_LOCATION_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_FUNCTION_OWNER
      :value: "SPECIAL_DESTINATION_FUNCTION_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_METASTORE_OWNER
      :value: "SPECIAL_DESTINATION_METASTORE_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_REGISTERED_MODEL_OWNER
      :value: "SPECIAL_DESTINATION_REGISTERED_MODEL_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_SCHEMA_OWNER
      :value: "SPECIAL_DESTINATION_SCHEMA_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_TABLE_OWNER
      :value: "SPECIAL_DESTINATION_TABLE_OWNER"

   .. py:attribute:: SPECIAL_DESTINATION_VOLUME_OWNER
      :value: "SPECIAL_DESTINATION_VOLUME_OWNER"

.. autoclass:: SseEncryptionDetails
   :members:
   :undoc-members:

.. py:class:: SseEncryptionDetailsAlgorithm

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

.. py:class:: SystemType

   .. py:attribute:: AMAZON_REDSHIFT
      :value: "AMAZON_REDSHIFT"

   .. py:attribute:: AZURE_SYNAPSE
      :value: "AZURE_SYNAPSE"

   .. py:attribute:: CONFLUENT
      :value: "CONFLUENT"

   .. py:attribute:: DATABRICKS
      :value: "DATABRICKS"

   .. py:attribute:: GOOGLE_BIGQUERY
      :value: "GOOGLE_BIGQUERY"

   .. py:attribute:: KAFKA
      :value: "KAFKA"

   .. py:attribute:: LOOKER
      :value: "LOOKER"

   .. py:attribute:: MICROSOFT_FABRIC
      :value: "MICROSOFT_FABRIC"

   .. py:attribute:: MICROSOFT_SQL_SERVER
      :value: "MICROSOFT_SQL_SERVER"

   .. py:attribute:: MONGODB
      :value: "MONGODB"

   .. py:attribute:: MYSQL
      :value: "MYSQL"

   .. py:attribute:: ORACLE
      :value: "ORACLE"

   .. py:attribute:: OTHER
      :value: "OTHER"

   .. py:attribute:: POSTGRESQL
      :value: "POSTGRESQL"

   .. py:attribute:: POWER_BI
      :value: "POWER_BI"

   .. py:attribute:: SALESFORCE
      :value: "SALESFORCE"

   .. py:attribute:: SAP
      :value: "SAP"

   .. py:attribute:: SERVICENOW
      :value: "SERVICENOW"

   .. py:attribute:: SNOWFLAKE
      :value: "SNOWFLAKE"

   .. py:attribute:: STREAM_NATIVE
      :value: "STREAM_NATIVE"

   .. py:attribute:: TABLEAU
      :value: "TABLEAU"

   .. py:attribute:: TERADATA
      :value: "TERADATA"

   .. py:attribute:: WORKDAY
      :value: "WORKDAY"

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

.. py:class:: TableOperation

   .. py:attribute:: READ
      :value: "READ"

   .. py:attribute:: READ_WRITE
      :value: "READ_WRITE"

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

   .. py:attribute:: METRIC_VIEW
      :value: "METRIC_VIEW"

   .. py:attribute:: STREAMING_TABLE
      :value: "STREAMING_TABLE"

   .. py:attribute:: VIEW
      :value: "VIEW"

.. py:class:: TagAssignmentSourceType

   Enum representing the source type of a tag assignment

   .. py:attribute:: TAG_ASSIGNMENT_SOURCE_TYPE_SYSTEM_DATA_CLASSIFICATION
      :value: "TAG_ASSIGNMENT_SOURCE_TYPE_SYSTEM_DATA_CLASSIFICATION"

.. autoclass:: TagIntrospectionExpression
   :members:
   :undoc-members:

.. autoclass:: TagKeyValue
   :members:
   :undoc-members:

.. autoclass:: TagValueExtraction
   :members:
   :undoc-members:

.. autoclass:: TemporaryCredentials
   :members:
   :undoc-members:

.. autoclass:: TriggeredUpdateStatus
   :members:
   :undoc-members:

.. autoclass:: UcEncryptedToken
   :members:
   :undoc-members:

.. autoclass:: UnassignResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateAccountsMetastore
   :members:
   :undoc-members:

.. autoclass:: UpdateAccountsStorageCredential
   :members:
   :undoc-members:

.. autoclass:: UpdateAssignmentResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateCatalogWorkspaceBindingsResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateMetastoreAssignment
   :members:
   :undoc-members:

.. autoclass:: UpdatePermissionsResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateRequestExternalLineage
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateWorkspaceBindingsResponse
   :members:
   :undoc-members:

.. autoclass:: ValidateCredentialResponse
   :members:
   :undoc-members:

.. py:class:: ValidateCredentialResult

   A enum represents the result of the file operation

   .. py:attribute:: FAIL
      :value: "FAIL"

   .. py:attribute:: PASS
      :value: "PASS"

   .. py:attribute:: SKIP
      :value: "SKIP"

.. autoclass:: ValidateStorageCredentialResponse
   :members:
   :undoc-members:

.. autoclass:: ValidationResult
   :members:
   :undoc-members:

.. py:class:: ValidationResultOperation

   A enum represents the file operation performed on the external location with the storage credential

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

   A enum represents the result of the file operation

   .. py:attribute:: FAIL
      :value: "FAIL"

   .. py:attribute:: PASS
      :value: "PASS"

   .. py:attribute:: SKIP
      :value: "SKIP"

.. autoclass:: VolumeDependency
   :members:
   :undoc-members:

.. autoclass:: VolumeInfo
   :members:
   :undoc-members:

.. py:class:: VolumeOperation

   .. py:attribute:: READ_VOLUME
      :value: "READ_VOLUME"

   .. py:attribute:: WRITE_VOLUME
      :value: "WRITE_VOLUME"

.. py:class:: VolumeType

   .. py:attribute:: EXTERNAL
      :value: "EXTERNAL"

   .. py:attribute:: MANAGED
      :value: "MANAGED"

.. autoclass:: WorkspaceBinding
   :members:
   :undoc-members:

.. py:class:: WorkspaceBindingBindingType

   Using ``BINDING_TYPE_`` prefix here to avoid conflict with ``TableOperation`` enum in ``credentials_common.proto``.

   .. py:attribute:: BINDING_TYPE_READ_ONLY
      :value: "BINDING_TYPE_READ_ONLY"

   .. py:attribute:: BINDING_TYPE_READ_WRITE
      :value: "BINDING_TYPE_READ_WRITE"

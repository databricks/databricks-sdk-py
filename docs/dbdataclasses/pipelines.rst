Spark Declarative Pipelines
===========================

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.pipelines`` module.

.. py:currentmodule:: databricks.sdk.service.pipelines
.. autoclass:: AkamaiOptions
   :members:
   :undoc-members:

.. autoclass:: ApiSourceConnectorConfig
   :members:
   :undoc-members:

.. autoclass:: ApiSourceConnectorOptions
   :members:
   :undoc-members:

.. autoclass:: ApplyEnvironmentRequestResponse
   :members:
   :undoc-members:

.. autoclass:: AutoFullRefreshPolicy
   :members:
   :undoc-members:

.. autoclass:: AvroTransformerOptions
   :members:
   :undoc-members:

.. autoclass:: BingAdsOptions
   :members:
   :undoc-members:

.. autoclass:: BingAdsOptionsBingCustomReportOptions
   :members:
   :undoc-members:

.. py:class:: BingAdsOptionsBingCustomReportOptionsBingAdsGranularity

   Time granularity for Bing Ads report aggregation.

   .. py:attribute:: DAILY
      :value: "DAILY"

   .. py:attribute:: HOURLY
      :value: "HOURLY"

   .. py:attribute:: MONTHLY
      :value: "MONTHLY"

   .. py:attribute:: SUMMARY
      :value: "SUMMARY"

   .. py:attribute:: WEEKLY
      :value: "WEEKLY"

   .. py:attribute:: YEARLY
      :value: "YEARLY"

.. py:class:: BingAdsOptionsBingCustomReportOptionsBingAdsReportType

   Supported Microsoft Advertising report types for custom reports.

   .. py:attribute:: ACCOUNT_PERFORMANCE
      :value: "ACCOUNT_PERFORMANCE"

   .. py:attribute:: AD_DYNAMIC_TEXT_PERFORMANCE
      :value: "AD_DYNAMIC_TEXT_PERFORMANCE"

   .. py:attribute:: AD_EXTENSION_BY_AD
      :value: "AD_EXTENSION_BY_AD"

   .. py:attribute:: AD_EXTENSION_BY_KEYWORD
      :value: "AD_EXTENSION_BY_KEYWORD"

   .. py:attribute:: AD_EXTENSION_DETAIL
      :value: "AD_EXTENSION_DETAIL"

   .. py:attribute:: AD_GROUP_PERFORMANCE
      :value: "AD_GROUP_PERFORMANCE"

   .. py:attribute:: AD_PERFORMANCE
      :value: "AD_PERFORMANCE"

   .. py:attribute:: AGE_GENDER_AUDIENCE
      :value: "AGE_GENDER_AUDIENCE"

   .. py:attribute:: APPS_PERFORMANCE
      :value: "APPS_PERFORMANCE"

   .. py:attribute:: ASSET_GROUP_PERFORMANCE
      :value: "ASSET_GROUP_PERFORMANCE"

   .. py:attribute:: ASSET_PERFORMANCE
      :value: "ASSET_PERFORMANCE"

   .. py:attribute:: AUDIENCE_PERFORMANCE
      :value: "AUDIENCE_PERFORMANCE"

   .. py:attribute:: BID_STRATEGY
      :value: "BID_STRATEGY"

   .. py:attribute:: BUDGET_SUMMARY
      :value: "BUDGET_SUMMARY"

   .. py:attribute:: CALL_DETAIL
      :value: "CALL_DETAIL"

   .. py:attribute:: CAMPAIGN_PERFORMANCE
      :value: "CAMPAIGN_PERFORMANCE"

   .. py:attribute:: COMBINATION_PERFORMANCE
      :value: "COMBINATION_PERFORMANCE"

   .. py:attribute:: CONVERSION_PERFORMANCE
      :value: "CONVERSION_PERFORMANCE"

   .. py:attribute:: DESTINATION_URL_PERFORMANCE
      :value: "DESTINATION_URL_PERFORMANCE"

   .. py:attribute:: DSA_AUTO_TARGET_PERFORMANCE
      :value: "DSA_AUTO_TARGET_PERFORMANCE"

   .. py:attribute:: DSA_CATEGORY_PERFORMANCE
      :value: "DSA_CATEGORY_PERFORMANCE"

   .. py:attribute:: DSA_SEARCH_QUERY_PERFORMANCE
      :value: "DSA_SEARCH_QUERY_PERFORMANCE"

   .. py:attribute:: GEOGRAPHIC_PERFORMANCE
      :value: "GEOGRAPHIC_PERFORMANCE"

   .. py:attribute:: GOALS_AND_FUNNELS
      :value: "GOALS_AND_FUNNELS"

   .. py:attribute:: HOTEL_DIMENSION_PERFORMANCE
      :value: "HOTEL_DIMENSION_PERFORMANCE"

   .. py:attribute:: HOTEL_GROUP_PERFORMANCE
      :value: "HOTEL_GROUP_PERFORMANCE"

   .. py:attribute:: KEYWORD_PERFORMANCE
      :value: "KEYWORD_PERFORMANCE"

   .. py:attribute:: MS_CLICK_ID_PERFORMANCE
      :value: "MS_CLICK_ID_PERFORMANCE"

   .. py:attribute:: NEGATIVE_KEYWORD_CONFLICT
      :value: "NEGATIVE_KEYWORD_CONFLICT"

   .. py:attribute:: PRODUCT_DIMENSION_PERFORMANCE
      :value: "PRODUCT_DIMENSION_PERFORMANCE"

   .. py:attribute:: PRODUCT_MATCH_COUNT
      :value: "PRODUCT_MATCH_COUNT"

   .. py:attribute:: PRODUCT_PARTITION_PERFORMANCE
      :value: "PRODUCT_PARTITION_PERFORMANCE"

   .. py:attribute:: PRODUCT_PARTITION_UNIT_PERFORMANCE
      :value: "PRODUCT_PARTITION_UNIT_PERFORMANCE"

   .. py:attribute:: PRODUCT_SEARCH_QUERY_PERFORMANCE
      :value: "PRODUCT_SEARCH_QUERY_PERFORMANCE"

   .. py:attribute:: PROFESSIONAL_DEMOGRAPHICS_AUDIENCE
      :value: "PROFESSIONAL_DEMOGRAPHICS_AUDIENCE"

   .. py:attribute:: PUBLISHER_USAGE_PERFORMANCE
      :value: "PUBLISHER_USAGE_PERFORMANCE"

   .. py:attribute:: SEARCH_CAMPAIGN_CHANGE_HISTORY
      :value: "SEARCH_CAMPAIGN_CHANGE_HISTORY"

   .. py:attribute:: SEARCH_INSIGHT_PERFORMANCE
      :value: "SEARCH_INSIGHT_PERFORMANCE"

   .. py:attribute:: SEARCH_QUERY_PERFORMANCE
      :value: "SEARCH_QUERY_PERFORMANCE"

   .. py:attribute:: SHARE_OF_VOICE
      :value: "SHARE_OF_VOICE"

   .. py:attribute:: USER_LOCATION_PERFORMANCE
      :value: "USER_LOCATION_PERFORMANCE"

.. py:class:: CloneMode

   Enum to specify which mode of clone to execute

   .. py:attribute:: MIGRATE_TO_UC
      :value: "MIGRATE_TO_UC"

.. autoclass:: ClonePipelineResponse
   :members:
   :undoc-members:

.. autoclass:: CommunityConnectorOptions
   :members:
   :undoc-members:

.. autoclass:: ConfluenceConnectorOptions
   :members:
   :undoc-members:

.. autoclass:: ConfluentSchemaRegistryOptions
   :members:
   :undoc-members:

.. autoclass:: ConnectionParameters
   :members:
   :undoc-members:

.. autoclass:: ConnectorOptions
   :members:
   :undoc-members:

.. py:class:: ConnectorType

   For certain database sources LakeFlow Connect offers both query based and cdc ingestion, ConnectorType can bse used to convey the type of ingestion. If connection_name is provided for database sources, we default to Query Based ingestion

   .. py:attribute:: CDC
      :value: "CDC"

   .. py:attribute:: QUERY_BASED
      :value: "QUERY_BASED"

.. autoclass:: CreatePipelineResponse
   :members:
   :undoc-members:

.. autoclass:: CronTrigger
   :members:
   :undoc-members:

.. autoclass:: DataPlaneId
   :members:
   :undoc-members:

.. autoclass:: DataStagingOptions
   :members:
   :undoc-members:

.. py:class:: DayOfWeek

   Days of week in which the window is allowed to happen. If not specified all days of the week will be used.

   .. py:attribute:: FRIDAY
      :value: "FRIDAY"

   .. py:attribute:: MONDAY
      :value: "MONDAY"

   .. py:attribute:: SATURDAY
      :value: "SATURDAY"

   .. py:attribute:: SUNDAY
      :value: "SUNDAY"

   .. py:attribute:: THURSDAY
      :value: "THURSDAY"

   .. py:attribute:: TUESDAY
      :value: "TUESDAY"

   .. py:attribute:: WEDNESDAY
      :value: "WEDNESDAY"

.. autoclass:: DeletePipelineResponse
   :members:
   :undoc-members:

.. py:class:: DeploymentKind

   The deployment method that manages the pipeline:
   - BUNDLE: The pipeline is managed by a Databricks Asset Bundle.

   .. py:attribute:: BUNDLE
      :value: "BUNDLE"

.. autoclass:: EditPipelineResponse
   :members:
   :undoc-members:

.. autoclass:: ErrorDetail
   :members:
   :undoc-members:

.. py:class:: EventLevel

   The severity level of the event.

   .. py:attribute:: ERROR
      :value: "ERROR"

   .. py:attribute:: INFO
      :value: "INFO"

   .. py:attribute:: METRICS
      :value: "METRICS"

   .. py:attribute:: WARN
      :value: "WARN"

.. autoclass:: EventLogSpec
   :members:
   :undoc-members:

.. autoclass:: FileFilter
   :members:
   :undoc-members:

.. autoclass:: FileIngestionOptions
   :members:
   :undoc-members:

.. py:class:: FileIngestionOptionsFileFormat

   .. py:attribute:: AVRO
      :value: "AVRO"

   .. py:attribute:: BINARYFILE
      :value: "BINARYFILE"

   .. py:attribute:: CSV
      :value: "CSV"

   .. py:attribute:: EXCEL
      :value: "EXCEL"

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: JSON
      :value: "JSON"

   .. py:attribute:: ORC
      :value: "ORC"

   .. py:attribute:: PARQUET
      :value: "PARQUET"

   .. py:attribute:: XML
      :value: "XML"

.. py:class:: FileIngestionOptionsSchemaEvolutionMode

   Based on https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema#how-does-auto-loader-schema-evolution-work

   .. py:attribute:: ADD_NEW_COLUMNS
      :value: "ADD_NEW_COLUMNS"

   .. py:attribute:: ADD_NEW_COLUMNS_WITH_TYPE_WIDENING
      :value: "ADD_NEW_COLUMNS_WITH_TYPE_WIDENING"

   .. py:attribute:: FAIL_ON_NEW_COLUMNS
      :value: "FAIL_ON_NEW_COLUMNS"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: RESCUE
      :value: "RESCUE"

.. autoclass:: FileLibrary
   :members:
   :undoc-members:

.. autoclass:: Filters
   :members:
   :undoc-members:

.. autoclass:: GetPipelinePermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetPipelineResponse
   :members:
   :undoc-members:

.. py:class:: GetPipelineResponseHealth

   The health of a pipeline.

   .. py:attribute:: HEALTHY
      :value: "HEALTHY"

   .. py:attribute:: UNHEALTHY
      :value: "UNHEALTHY"

.. autoclass:: GetUpdateResponse
   :members:
   :undoc-members:

.. autoclass:: GitHubConnectorOptions
   :members:
   :undoc-members:

.. autoclass:: GitHubConnectorOptionsRepositoryBranchSelection
   :members:
   :undoc-members:

.. autoclass:: GoogleAdsConfig
   :members:
   :undoc-members:

.. autoclass:: GoogleAdsCustomReportOptions
   :members:
   :undoc-members:

.. autoclass:: GoogleAdsOptions
   :members:
   :undoc-members:

.. autoclass:: GoogleDriveOptions
   :members:
   :undoc-members:

.. py:class:: GoogleDriveOptionsGoogleDriveEntityType

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: FILE_METADATA
      :value: "FILE_METADATA"

   .. py:attribute:: FILE_PERMISSION
      :value: "FILE_PERMISSION"

   .. py:attribute:: GROUP_MEMBERSHIP
      :value: "GROUP_MEMBERSHIP"

   .. py:attribute:: PERMISSION
      :value: "PERMISSION"

.. py:class:: GoogleDriveOptionsGoogleDriveIngestionScope

   .. py:attribute:: DOMAIN_ALL
      :value: "DOMAIN_ALL"

   .. py:attribute:: DOMAIN_SHARED_DRIVES
      :value: "DOMAIN_SHARED_DRIVES"

   .. py:attribute:: DOMAIN_USER_DRIVES
      :value: "DOMAIN_USER_DRIVES"

   .. py:attribute:: USER_ACCESSIBLE
      :value: "USER_ACCESSIBLE"

   .. py:attribute:: USER_DRIVE
      :value: "USER_DRIVE"

.. autoclass:: IngestionConfig
   :members:
   :undoc-members:

.. autoclass:: IngestionGatewayPipelineDefinition
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinition
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionConfluenceOptions
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionFanoutOptions
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionJiraOptions
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionTableSpecificConfigQueryBasedConnectorConfig
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionWorkdayReportParameters
   :members:
   :undoc-members:

.. autoclass:: IngestionPipelineDefinitionWorkdayReportParametersQueryKeyValue
   :members:
   :undoc-members:

.. py:class:: IngestionSourceType

   .. py:attribute:: ADOBE_CAMPAIGNS
      :value: "ADOBE_CAMPAIGNS"

   .. py:attribute:: ADOBE_COMMERCE
      :value: "ADOBE_COMMERCE"

   .. py:attribute:: ADP_WORKFORCE_NOW
      :value: "ADP_WORKFORCE_NOW"

   .. py:attribute:: AHA
      :value: "AHA"

   .. py:attribute:: AIRTABLE
      :value: "AIRTABLE"

   .. py:attribute:: AKAMAI_WAF
      :value: "AKAMAI_WAF"

   .. py:attribute:: AMPLITUDE
      :value: "AMPLITUDE"

   .. py:attribute:: API_SOURCE
      :value: "API_SOURCE"

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

   .. py:attribute:: BIGQUERY
      :value: "BIGQUERY"

   .. py:attribute:: BING_ADS
      :value: "BING_ADS"

   .. py:attribute:: CERIDIAN_DAYFORCE
      :value: "CERIDIAN_DAYFORCE"

   .. py:attribute:: COMMUNITY
      :value: "COMMUNITY"

   .. py:attribute:: CONFLUENCE
      :value: "CONFLUENCE"

   .. py:attribute:: CROWDSTRIKE_EVENT_STREAM
      :value: "CROWDSTRIKE_EVENT_STREAM"

   .. py:attribute:: DELIGHTED
      :value: "DELIGHTED"

   .. py:attribute:: DYNAMICS365
      :value: "DYNAMICS365"

   .. py:attribute:: EPIC_CLARITY
      :value: "EPIC_CLARITY"

   .. py:attribute:: FOREIGN_CATALOG
      :value: "FOREIGN_CATALOG"

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

   .. py:attribute:: GMAIL
      :value: "GMAIL"

   .. py:attribute:: GONG
      :value: "GONG"

   .. py:attribute:: GOOGLE_ADS
      :value: "GOOGLE_ADS"

   .. py:attribute:: GOOGLE_ANALYTICS
      :value: "GOOGLE_ANALYTICS"

   .. py:attribute:: GOOGLE_CALENDAR
      :value: "GOOGLE_CALENDAR"

   .. py:attribute:: GOOGLE_DRIVE
      :value: "GOOGLE_DRIVE"

   .. py:attribute:: GOOGLE_SEARCH_CONSOLE
      :value: "GOOGLE_SEARCH_CONSOLE"

   .. py:attribute:: GOOGLE_WORKSPACE
      :value: "GOOGLE_WORKSPACE"

   .. py:attribute:: GUIDEWIRE
      :value: "GUIDEWIRE"

   .. py:attribute:: GURU
      :value: "GURU"

   .. py:attribute:: HIBOB
      :value: "HIBOB"

   .. py:attribute:: HUBSPOT
      :value: "HUBSPOT"

   .. py:attribute:: IRONCLAD
      :value: "IRONCLAD"

   .. py:attribute:: JIRA
      :value: "JIRA"

   .. py:attribute:: KAFKA
      :value: "KAFKA"

   .. py:attribute:: LINEAR
      :value: "LINEAR"

   .. py:attribute:: LINKEDIN_ADS
      :value: "LINKEDIN_ADS"

   .. py:attribute:: M365_AUDIT_LOGS
      :value: "M365_AUDIT_LOGS"

   .. py:attribute:: MANAGED_POSTGRESQL
      :value: "MANAGED_POSTGRESQL"

   .. py:attribute:: MARKETO
      :value: "MARKETO"

   .. py:attribute:: META_MARKETING
      :value: "META_MARKETING"

   .. py:attribute:: MICROSOFT_ENTRA_ID
      :value: "MICROSOFT_ENTRA_ID"

   .. py:attribute:: MICROSOFT_TEAMS
      :value: "MICROSOFT_TEAMS"

   .. py:attribute:: MONDAY_COM
      :value: "MONDAY_COM"

   .. py:attribute:: MYSQL
      :value: "MYSQL"

   .. py:attribute:: NETSKOPE_LOGS
      :value: "NETSKOPE_LOGS"

   .. py:attribute:: NETSUITE
      :value: "NETSUITE"

   .. py:attribute:: NOTION
      :value: "NOTION"

   .. py:attribute:: OKTA_SYSTEM_LOGS
      :value: "OKTA_SYSTEM_LOGS"

   .. py:attribute:: ONEDRIVE
      :value: "ONEDRIVE"

   .. py:attribute:: ONE_PASSWORD_EVENT_LOGS
      :value: "ONE_PASSWORD_EVENT_LOGS"

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

   .. py:attribute:: PARTNERSTACK
      :value: "PARTNERSTACK"

   .. py:attribute:: PENDO
      :value: "PENDO"

   .. py:attribute:: PINTEREST_ADS
      :value: "PINTEREST_ADS"

   .. py:attribute:: POSTGRESQL
      :value: "POSTGRESQL"

   .. py:attribute:: PROOFPOINT_SIEM
      :value: "PROOFPOINT_SIEM"

   .. py:attribute:: QUICKBOOKS
      :value: "QUICKBOOKS"

   .. py:attribute:: RABBITMQ
      :value: "RABBITMQ"

   .. py:attribute:: REDDIT_ADS
      :value: "REDDIT_ADS"

   .. py:attribute:: REDSHIFT
      :value: "REDSHIFT"

   .. py:attribute:: SALESFORCE
      :value: "SALESFORCE"

   .. py:attribute:: SALESFORCE_MARKETING_CLOUD
      :value: "SALESFORCE_MARKETING_CLOUD"

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

   .. py:attribute:: SHAREPOINT
      :value: "SHAREPOINT"

   .. py:attribute:: SHOPIFY
      :value: "SHOPIFY"

   .. py:attribute:: SLACK_ACCESS_AND_INTEGRATION_LOGS
      :value: "SLACK_ACCESS_AND_INTEGRATION_LOGS"

   .. py:attribute:: SLACK_AUDIT_LOGS
      :value: "SLACK_AUDIT_LOGS"

   .. py:attribute:: SMARTSHEET
      :value: "SMARTSHEET"

   .. py:attribute:: SNAPCHAT_ADS
      :value: "SNAPCHAT_ADS"

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

   .. py:attribute:: TIKTOK_ADS
      :value: "TIKTOK_ADS"

   .. py:attribute:: VEEVA
      :value: "VEEVA"

   .. py:attribute:: VEEVA_VAULT
      :value: "VEEVA_VAULT"

   .. py:attribute:: VERKADA
      :value: "VERKADA"

   .. py:attribute:: WIZ_AUDIT_LOGS
      :value: "WIZ_AUDIT_LOGS"

   .. py:attribute:: WORKDAY_ACTIVITY_LOGGING
      :value: "WORKDAY_ACTIVITY_LOGGING"

   .. py:attribute:: WORKDAY_HCM
      :value: "WORKDAY_HCM"

   .. py:attribute:: WORKDAY_RAAS
      :value: "WORKDAY_RAAS"

   .. py:attribute:: X_ADS
      :value: "X_ADS"

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

.. autoclass:: JiraConnectorOptions
   :members:
   :undoc-members:

.. autoclass:: JsonTransformerOptions
   :members:
   :undoc-members:

.. autoclass:: KafkaOptions
   :members:
   :undoc-members:

.. autoclass:: LinkedInAdsOptions
   :members:
   :undoc-members:

.. autoclass:: LinkedInAdsOptionsLinkedInAdsCustomReportOptions
   :members:
   :undoc-members:

.. py:class:: LinkedInAdsOptionsLinkedInAdsCustomReportOptionsLinkedInAdsEntityGranularity

   Entity pivot to group by.

   .. py:attribute:: CAMPAIGN
      :value: "CAMPAIGN"

   .. py:attribute:: CAMPAIGN_GROUP
      :value: "CAMPAIGN_GROUP"

   .. py:attribute:: CREATIVE
      :value: "CREATIVE"

.. py:class:: LinkedInAdsOptionsLinkedInAdsCustomReportOptionsLinkedInAdsFinder

   adAnalytics finder. Determines call shape, valid pivots, and metric requirements.

   .. py:attribute:: ANALYTICS
      :value: "ANALYTICS"

   .. py:attribute:: ATTRIBUTED_REVENUE_METRICS
      :value: "ATTRIBUTED_REVENUE_METRICS"

   .. py:attribute:: STATISTICS
      :value: "STATISTICS"

.. py:class:: LinkedInAdsOptionsLinkedInAdsCustomReportOptionsLinkedInAdsTimeGranularity

   Time aggregation. Used by analytics/statistics; ignored for attributedRevenueMetrics. Defaults to DAILY when unspecified.

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: DAILY
      :value: "DAILY"

   .. py:attribute:: MONTHLY
      :value: "MONTHLY"

   .. py:attribute:: YEARLY
      :value: "YEARLY"

.. autoclass:: ListPipelineEventsResponse
   :members:
   :undoc-members:

.. autoclass:: ListPipelinesResponse
   :members:
   :undoc-members:

.. autoclass:: ListUpdatesResponse
   :members:
   :undoc-members:

.. autoclass:: ManualTrigger
   :members:
   :undoc-members:

.. autoclass:: MarketoOptions
   :members:
   :undoc-members:

.. py:class:: MaturityLevel

   Maturity level for EventDetails.

   .. py:attribute:: DEPRECATED
      :value: "DEPRECATED"

   .. py:attribute:: EVOLVING
      :value: "EVOLVING"

   .. py:attribute:: STABLE
      :value: "STABLE"

.. autoclass:: MetaMarketingOptions
   :members:
   :undoc-members:

.. autoclass:: MetaMarketingOptionsMetaMarketingCustomReportOptions
   :members:
   :undoc-members:

.. autoclass:: NotebookLibrary
   :members:
   :undoc-members:

.. autoclass:: Notifications
   :members:
   :undoc-members:

.. autoclass:: OneDriveOptions
   :members:
   :undoc-members:

.. py:class:: OneDriveOptionsOneDriveEntityType

   The type of OneDrive entity to ingest.

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: FILE_METADATA
      :value: "FILE_METADATA"

   .. py:attribute:: FILE_PERMISSION
      :value: "FILE_PERMISSION"

   .. py:attribute:: GROUP_MEMBERSHIP
      :value: "GROUP_MEMBERSHIP"

.. autoclass:: OperationTimeWindow
   :members:
   :undoc-members:

.. autoclass:: Origin
   :members:
   :undoc-members:

.. py:class:: OutlookAttachmentMode

   Attachment behavior mode for Outlook ingestion

   .. py:attribute:: ALL
      :value: "ALL"

   .. py:attribute:: INLINE_ONLY
      :value: "INLINE_ONLY"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: NON_INLINE_ONLY
      :value: "NON_INLINE_ONLY"

.. py:class:: OutlookBodyFormat

   Body format for Outlook email content

   .. py:attribute:: TEXT_HTML
      :value: "TEXT_HTML"

   .. py:attribute:: TEXT_PLAIN
      :value: "TEXT_PLAIN"

.. autoclass:: OutlookOptions
   :members:
   :undoc-members:

.. py:class:: ParseMode

   Determines how errors encountered while deserializing records are handled.

   .. py:attribute:: FAILFAST
      :value: "FAILFAST"

   .. py:attribute:: PERMISSIVE
      :value: "PERMISSIVE"

.. autoclass:: PathPattern
   :members:
   :undoc-members:

.. autoclass:: PeriodicTrigger
   :members:
   :undoc-members:

.. py:class:: PeriodicTriggerTimeUnit

   Time unit enums for different time units.

   .. py:attribute:: DAYS
      :value: "DAYS"

   .. py:attribute:: HOURS
      :value: "HOURS"

   .. py:attribute:: WEEKS
      :value: "WEEKS"

.. autoclass:: PipelineAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: PipelineAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: PipelineCluster
   :members:
   :undoc-members:

.. autoclass:: PipelineClusterAutoscale
   :members:
   :undoc-members:

.. py:class:: PipelineClusterAutoscaleMode

   Databricks Enhanced Autoscaling optimizes cluster utilization by automatically allocating cluster resources based on workload volume, with minimal impact to the data processing latency of your pipelines. Enhanced Autoscaling is available for ``updates`` clusters only. The legacy autoscaling feature is used for ``maintenance`` clusters.

   .. py:attribute:: ENHANCED
      :value: "ENHANCED"

   .. py:attribute:: LEGACY
      :value: "LEGACY"

.. autoclass:: PipelineDeployment
   :members:
   :undoc-members:

.. autoclass:: PipelineEvent
   :members:
   :undoc-members:

.. autoclass:: PipelineLibrary
   :members:
   :undoc-members:

.. autoclass:: PipelinePermission
   :members:
   :undoc-members:

.. py:class:: PipelinePermissionLevel

   Permission level

   .. py:attribute:: CAN_MANAGE
      :value: "CAN_MANAGE"

   .. py:attribute:: CAN_RUN
      :value: "CAN_RUN"

   .. py:attribute:: CAN_VIEW
      :value: "CAN_VIEW"

   .. py:attribute:: IS_OWNER
      :value: "IS_OWNER"

.. autoclass:: PipelinePermissions
   :members:
   :undoc-members:

.. autoclass:: PipelinePermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: PipelineSpec
   :members:
   :undoc-members:

.. py:class:: PipelineState

   The pipeline state.

   .. py:attribute:: DELETED
      :value: "DELETED"

   .. py:attribute:: DEPLOYING
      :value: "DEPLOYING"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: IDLE
      :value: "IDLE"

   .. py:attribute:: RECOVERING
      :value: "RECOVERING"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: STARTING
      :value: "STARTING"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

.. autoclass:: PipelineStateInfo
   :members:
   :undoc-members:

.. py:class:: PipelineStateInfoHealth

   The health of a pipeline.

   .. py:attribute:: HEALTHY
      :value: "HEALTHY"

   .. py:attribute:: UNHEALTHY
      :value: "UNHEALTHY"

.. autoclass:: PipelineTrigger
   :members:
   :undoc-members:

.. autoclass:: PipelinesEnvironment
   :members:
   :undoc-members:

.. autoclass:: PostgresCatalogConfig
   :members:
   :undoc-members:

.. autoclass:: PostgresSlotConfig
   :members:
   :undoc-members:

.. autoclass:: ProtobufTransformerOptions
   :members:
   :undoc-members:

.. py:class:: PublishingMode

   Enum representing the publishing mode of a pipeline.

   .. py:attribute:: DEFAULT_PUBLISHING_MODE
      :value: "DEFAULT_PUBLISHING_MODE"

   .. py:attribute:: LEGACY_PUBLISHING_MODE
      :value: "LEGACY_PUBLISHING_MODE"

.. autoclass:: RabbitmqOptions
   :members:
   :undoc-members:

.. autoclass:: RedditAdsOptions
   :members:
   :undoc-members:

.. autoclass:: RedditAdsOptionsRedditAdsCustomReportOptions
   :members:
   :undoc-members:

.. autoclass:: ReplaceWhereOverride
   :members:
   :undoc-members:

.. autoclass:: ReportSpec
   :members:
   :undoc-members:

.. autoclass:: RestartWindow
   :members:
   :undoc-members:

.. autoclass:: RestorePipelineRequestResponse
   :members:
   :undoc-members:

.. autoclass:: RewindDatasetSpec
   :members:
   :undoc-members:

.. autoclass:: RewindSpec
   :members:
   :undoc-members:

.. autoclass:: RunAs
   :members:
   :undoc-members:

.. autoclass:: SchemaRegistryConfig
   :members:
   :undoc-members:

.. autoclass:: SchemaSpec
   :members:
   :undoc-members:

.. autoclass:: Sequencing
   :members:
   :undoc-members:

.. autoclass:: SerializedException
   :members:
   :undoc-members:

.. autoclass:: SharepointOptions
   :members:
   :undoc-members:

.. py:class:: SharepointOptionsSharepointEntityType

   .. py:attribute:: FILE
      :value: "FILE"

   .. py:attribute:: FILE_METADATA
      :value: "FILE_METADATA"

   .. py:attribute:: FILE_PERMISSION
      :value: "FILE_PERMISSION"

   .. py:attribute:: GROUP_MEMBERSHIP
      :value: "GROUP_MEMBERSHIP"

   .. py:attribute:: LIST
      :value: "LIST"

   .. py:attribute:: PERMISSION
      :value: "PERMISSION"

.. autoclass:: SmartsheetOptions
   :members:
   :undoc-members:

.. autoclass:: SourceCatalogConfig
   :members:
   :undoc-members:

.. autoclass:: SourceConfig
   :members:
   :undoc-members:

.. autoclass:: StackFrame
   :members:
   :undoc-members:

.. py:class:: StartUpdateCause

   What triggered this update.

   .. py:attribute:: API_CALL
      :value: "API_CALL"

   .. py:attribute:: INFRASTRUCTURE_MAINTENANCE
      :value: "INFRASTRUCTURE_MAINTENANCE"

   .. py:attribute:: JOB_TASK
      :value: "JOB_TASK"

   .. py:attribute:: RETRY_ON_FAILURE
      :value: "RETRY_ON_FAILURE"

   .. py:attribute:: SCHEMA_CHANGE
      :value: "SCHEMA_CHANGE"

   .. py:attribute:: SERVICE_UPGRADE
      :value: "SERVICE_UPGRADE"

   .. py:attribute:: USER_ACTION
      :value: "USER_ACTION"

.. autoclass:: StartUpdateResponse
   :members:
   :undoc-members:

.. autoclass:: StopPipelineResponse
   :members:
   :undoc-members:

.. py:class:: StorageMode

   Defines how ingested data is written and maintained in the destination table.

   .. py:attribute:: APPEND_ONLY
      :value: "APPEND_ONLY"

   .. py:attribute:: SCD_TYPE_1
      :value: "SCD_TYPE_1"

   .. py:attribute:: SCD_TYPE_2
      :value: "SCD_TYPE_2"

.. autoclass:: TableSpec
   :members:
   :undoc-members:

.. autoclass:: TableSpecificConfig
   :members:
   :undoc-members:

.. py:class:: TableSpecificConfigScdType

   The SCD type to use to ingest the table.

   .. py:attribute:: APPEND_ONLY
      :value: "APPEND_ONLY"

   .. py:attribute:: SCD_TYPE_1
      :value: "SCD_TYPE_1"

   .. py:attribute:: SCD_TYPE_2
      :value: "SCD_TYPE_2"

.. autoclass:: TikTokAdsOptions
   :members:
   :undoc-members:

.. autoclass:: TikTokAdsOptionsTikTokAdsCustomReportOptions
   :members:
   :undoc-members:

.. py:class:: TikTokAdsOptionsTikTokDataLevel

   Data level for TikTok Ads report aggregation.

   .. py:attribute:: AUCTION_AD
      :value: "AUCTION_AD"

   .. py:attribute:: AUCTION_ADGROUP
      :value: "AUCTION_ADGROUP"

   .. py:attribute:: AUCTION_ADVERTISER
      :value: "AUCTION_ADVERTISER"

   .. py:attribute:: AUCTION_CAMPAIGN
      :value: "AUCTION_CAMPAIGN"

.. py:class:: TikTokAdsOptionsTikTokReportType

   Report type for TikTok Ads API.

   .. py:attribute:: AUDIENCE
      :value: "AUDIENCE"

   .. py:attribute:: BASIC
      :value: "BASIC"

   .. py:attribute:: BUSINESS_CENTER
      :value: "BUSINESS_CENTER"

   .. py:attribute:: DSA
      :value: "DSA"

   .. py:attribute:: GMV_MAX
      :value: "GMV_MAX"

   .. py:attribute:: PLAYABLE_AD
      :value: "PLAYABLE_AD"

.. autoclass:: Transformer
   :members:
   :undoc-members:

.. py:class:: TransformerFormat

   .. py:attribute:: AVRO
      :value: "AVRO"

   .. py:attribute:: JSON
      :value: "JSON"

   .. py:attribute:: PROTOBUF
      :value: "PROTOBUF"

   .. py:attribute:: STRING
      :value: "STRING"

.. autoclass:: Truncation
   :members:
   :undoc-members:

.. autoclass:: TruncationTruncationDetail
   :members:
   :undoc-members:

.. autoclass:: UpdateInfo
   :members:
   :undoc-members:

.. py:class:: UpdateInfoCause

   What triggered this update.

   .. py:attribute:: API_CALL
      :value: "API_CALL"

   .. py:attribute:: INFRASTRUCTURE_MAINTENANCE
      :value: "INFRASTRUCTURE_MAINTENANCE"

   .. py:attribute:: JOB_TASK
      :value: "JOB_TASK"

   .. py:attribute:: RETRY_ON_FAILURE
      :value: "RETRY_ON_FAILURE"

   .. py:attribute:: SCHEMA_CHANGE
      :value: "SCHEMA_CHANGE"

   .. py:attribute:: SERVICE_UPGRADE
      :value: "SERVICE_UPGRADE"

   .. py:attribute:: USER_ACTION
      :value: "USER_ACTION"

.. py:class:: UpdateInfoState

   The update state.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: INITIALIZING
      :value: "INITIALIZING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SETTING_UP_TABLES
      :value: "SETTING_UP_TABLES"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

   .. py:attribute:: WAITING_FOR_RESOURCES
      :value: "WAITING_FOR_RESOURCES"

.. py:class:: UpdateMode

   .. py:attribute:: CONTINUOUS
      :value: "CONTINUOUS"

   .. py:attribute:: DEFAULT
      :value: "DEFAULT"

.. autoclass:: UpdateStateInfo
   :members:
   :undoc-members:

.. py:class:: UpdateStateInfoState

   The update state.

   .. py:attribute:: CANCELED
      :value: "CANCELED"

   .. py:attribute:: COMPLETED
      :value: "COMPLETED"

   .. py:attribute:: CREATED
      :value: "CREATED"

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: INITIALIZING
      :value: "INITIALIZING"

   .. py:attribute:: QUEUED
      :value: "QUEUED"

   .. py:attribute:: RESETTING
      :value: "RESETTING"

   .. py:attribute:: RUNNING
      :value: "RUNNING"

   .. py:attribute:: SETTING_UP_TABLES
      :value: "SETTING_UP_TABLES"

   .. py:attribute:: STOPPING
      :value: "STOPPING"

   .. py:attribute:: WAITING_FOR_RESOURCES
      :value: "WAITING_FOR_RESOURCES"

.. autoclass:: ZendeskSupportOptions
   :members:
   :undoc-members:

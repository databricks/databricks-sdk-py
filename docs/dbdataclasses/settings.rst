Settings
========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.settings`` module.

.. py:currentmodule:: databricks.sdk.service.settings
.. autoclass:: AccountIpAccessEnable
   :members:
   :undoc-members:

.. autoclass:: AccountNetworkPolicy
   :members:
   :undoc-members:

.. autoclass:: AibiDashboardEmbeddingAccessPolicy
   :members:
   :undoc-members:

.. py:class:: AibiDashboardEmbeddingAccessPolicyAccessPolicyType

   .. py:attribute:: ALLOW_ALL_DOMAINS
      :value: "ALLOW_ALL_DOMAINS"

   .. py:attribute:: ALLOW_APPROVED_DOMAINS
      :value: "ALLOW_APPROVED_DOMAINS"

   .. py:attribute:: DENY_ALL_DOMAINS
      :value: "DENY_ALL_DOMAINS"

.. autoclass:: AibiDashboardEmbeddingAccessPolicySetting
   :members:
   :undoc-members:

.. autoclass:: AibiDashboardEmbeddingApprovedDomains
   :members:
   :undoc-members:

.. autoclass:: AibiDashboardEmbeddingApprovedDomainsSetting
   :members:
   :undoc-members:

.. autoclass:: AutomaticClusterUpdateSetting
   :members:
   :undoc-members:

.. autoclass:: BooleanMessage
   :members:
   :undoc-members:

.. autoclass:: ClusterAutoRestartMessage
   :members:
   :undoc-members:

.. autoclass:: ClusterAutoRestartMessageEnablementDetails
   :members:
   :undoc-members:

.. autoclass:: ClusterAutoRestartMessageMaintenanceWindow
   :members:
   :undoc-members:

.. py:class:: ClusterAutoRestartMessageMaintenanceWindowDayOfWeek

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

.. autoclass:: ClusterAutoRestartMessageMaintenanceWindowWeekDayBasedSchedule
   :members:
   :undoc-members:

.. py:class:: ClusterAutoRestartMessageMaintenanceWindowWeekDayFrequency

   .. py:attribute:: EVERY_WEEK
      :value: "EVERY_WEEK"

   .. py:attribute:: FIRST_AND_THIRD_OF_MONTH
      :value: "FIRST_AND_THIRD_OF_MONTH"

   .. py:attribute:: FIRST_OF_MONTH
      :value: "FIRST_OF_MONTH"

   .. py:attribute:: FOURTH_OF_MONTH
      :value: "FOURTH_OF_MONTH"

   .. py:attribute:: SECOND_AND_FOURTH_OF_MONTH
      :value: "SECOND_AND_FOURTH_OF_MONTH"

   .. py:attribute:: SECOND_OF_MONTH
      :value: "SECOND_OF_MONTH"

   .. py:attribute:: THIRD_OF_MONTH
      :value: "THIRD_OF_MONTH"

.. autoclass:: ClusterAutoRestartMessageMaintenanceWindowWindowStartTime
   :members:
   :undoc-members:

.. autoclass:: ComplianceSecurityProfile
   :members:
   :undoc-members:

.. autoclass:: ComplianceSecurityProfileSetting
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

   .. py:attribute:: K_FSI
      :value: "K_FSI"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: PCI_DSS
      :value: "PCI_DSS"

.. autoclass:: Config
   :members:
   :undoc-members:

.. autoclass:: CreateIpAccessList
   :members:
   :undoc-members:

.. autoclass:: CreateIpAccessListResponse
   :members:
   :undoc-members:

.. autoclass:: CreateNetworkConnectivityConfiguration
   :members:
   :undoc-members:

.. autoclass:: CreateNotificationDestinationRequest
   :members:
   :undoc-members:

.. autoclass:: CreateOboTokenRequest
   :members:
   :undoc-members:

.. autoclass:: CreateOboTokenResponse
   :members:
   :undoc-members:

.. autoclass:: CreatePrivateEndpointRule
   :members:
   :undoc-members:

.. autoclass:: CreateTokenRequest
   :members:
   :undoc-members:

.. autoclass:: CreateTokenResponse
   :members:
   :undoc-members:

.. autoclass:: CspEnablementAccount
   :members:
   :undoc-members:

.. autoclass:: CspEnablementAccountSetting
   :members:
   :undoc-members:

.. autoclass:: DefaultNamespaceSetting
   :members:
   :undoc-members:

.. autoclass:: DeleteAccountIpAccessEnableResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteAibiDashboardEmbeddingAccessPolicySettingResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteAibiDashboardEmbeddingApprovedDomainsSettingResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDefaultNamespaceSettingResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDisableLegacyAccessResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDisableLegacyDbfsResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteDisableLegacyFeaturesResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteLlmProxyPartnerPoweredWorkspaceResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteNetworkConnectivityConfigurationResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteNetworkPolicyRpcResponse
   :members:
   :undoc-members:

.. autoclass:: DeletePersonalComputeSettingResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRestrictWorkspaceAdminsSettingResponse
   :members:
   :undoc-members:

.. py:class:: DestinationType

   .. py:attribute:: EMAIL
      :value: "EMAIL"

   .. py:attribute:: MICROSOFT_TEAMS
      :value: "MICROSOFT_TEAMS"

   .. py:attribute:: PAGERDUTY
      :value: "PAGERDUTY"

   .. py:attribute:: SLACK
      :value: "SLACK"

   .. py:attribute:: WEBHOOK
      :value: "WEBHOOK"

.. autoclass:: DisableLegacyAccess
   :members:
   :undoc-members:

.. autoclass:: DisableLegacyDbfs
   :members:
   :undoc-members:

.. autoclass:: DisableLegacyFeatures
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

.. autoclass:: EgressNetworkPolicyNetworkAccessPolicy
   :members:
   :undoc-members:

.. autoclass:: EgressNetworkPolicyNetworkAccessPolicyInternetDestination
   :members:
   :undoc-members:

.. py:class:: EgressNetworkPolicyNetworkAccessPolicyInternetDestinationInternetDestinationType

   .. py:attribute:: DNS_NAME
      :value: "DNS_NAME"

.. autoclass:: EgressNetworkPolicyNetworkAccessPolicyPolicyEnforcement
   :members:
   :undoc-members:

.. py:class:: EgressNetworkPolicyNetworkAccessPolicyPolicyEnforcementDryRunModeProductFilter

   The values should match the list of workloads used in networkconfig.proto

   .. py:attribute:: DBSQL
      :value: "DBSQL"

   .. py:attribute:: ML_SERVING
      :value: "ML_SERVING"

.. py:class:: EgressNetworkPolicyNetworkAccessPolicyPolicyEnforcementEnforcementMode

   .. py:attribute:: DRY_RUN
      :value: "DRY_RUN"

   .. py:attribute:: ENFORCED
      :value: "ENFORCED"

.. py:class:: EgressNetworkPolicyNetworkAccessPolicyRestrictionMode

   At which level can Databricks and Databricks managed compute access Internet. FULL_ACCESS: Databricks can access Internet. No blocking rules will apply. RESTRICTED_ACCESS: Databricks can only access explicitly allowed internet and storage destinations, as well as UC connections and external locations.

   .. py:attribute:: FULL_ACCESS
      :value: "FULL_ACCESS"

   .. py:attribute:: RESTRICTED_ACCESS
      :value: "RESTRICTED_ACCESS"

.. autoclass:: EgressNetworkPolicyNetworkAccessPolicyStorageDestination
   :members:
   :undoc-members:

.. py:class:: EgressNetworkPolicyNetworkAccessPolicyStorageDestinationStorageDestinationType

   .. py:attribute:: AWS_S3
      :value: "AWS_S3"

   .. py:attribute:: AZURE_STORAGE
      :value: "AZURE_STORAGE"

   .. py:attribute:: GOOGLE_CLOUD_STORAGE
      :value: "GOOGLE_CLOUD_STORAGE"

.. py:class:: EgressResourceType

   The target resources that are supported by Network Connectivity Config. Note: some egress types can support general types that are not defined in EgressResourceType. E.g.: Azure private endpoint supports private link enabled Azure services.

   .. py:attribute:: AZURE_BLOB_STORAGE
      :value: "AZURE_BLOB_STORAGE"

.. autoclass:: EmailConfig
   :members:
   :undoc-members:

.. autoclass:: Empty
   :members:
   :undoc-members:

.. autoclass:: EnableExportNotebook
   :members:
   :undoc-members:

.. autoclass:: EnableNotebookTableClipboard
   :members:
   :undoc-members:

.. autoclass:: EnableResultsDownloading
   :members:
   :undoc-members:

.. autoclass:: EnhancedSecurityMonitoring
   :members:
   :undoc-members:

.. autoclass:: EnhancedSecurityMonitoringSetting
   :members:
   :undoc-members:

.. autoclass:: EsmEnablementAccount
   :members:
   :undoc-members:

.. autoclass:: EsmEnablementAccountSetting
   :members:
   :undoc-members:

.. autoclass:: ExchangeToken
   :members:
   :undoc-members:

.. autoclass:: ExchangeTokenRequest
   :members:
   :undoc-members:

.. autoclass:: ExchangeTokenResponse
   :members:
   :undoc-members:

.. autoclass:: FetchIpAccessListResponse
   :members:
   :undoc-members:

.. autoclass:: GenericWebhookConfig
   :members:
   :undoc-members:

.. autoclass:: GetIpAccessListResponse
   :members:
   :undoc-members:

.. autoclass:: GetIpAccessListsResponse
   :members:
   :undoc-members:

.. autoclass:: GetTokenPermissionLevelsResponse
   :members:
   :undoc-members:

.. autoclass:: GetTokenResponse
   :members:
   :undoc-members:

.. autoclass:: IpAccessListInfo
   :members:
   :undoc-members:

.. autoclass:: ListIpAccessListResponse
   :members:
   :undoc-members:

.. autoclass:: ListNccAzurePrivateEndpointRulesResponse
   :members:
   :undoc-members:

.. autoclass:: ListNetworkConnectivityConfigurationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListNetworkPoliciesResponse
   :members:
   :undoc-members:

.. autoclass:: ListNotificationDestinationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListNotificationDestinationsResult
   :members:
   :undoc-members:

.. autoclass:: ListPublicTokensResponse
   :members:
   :undoc-members:

.. autoclass:: ListTokensResponse
   :members:
   :undoc-members:

.. py:class:: ListType

   Type of IP access list. Valid values are as follows and are case-sensitive:
   * `ALLOW`: An allow list. Include this IP or range. * `BLOCK`: A block list. Exclude this IP or range. IP addresses in the block list are excluded even if they are included in an allow list.

   .. py:attribute:: ALLOW
      :value: "ALLOW"

   .. py:attribute:: BLOCK
      :value: "BLOCK"

.. autoclass:: LlmProxyPartnerPoweredAccount
   :members:
   :undoc-members:

.. autoclass:: LlmProxyPartnerPoweredEnforce
   :members:
   :undoc-members:

.. autoclass:: LlmProxyPartnerPoweredWorkspace
   :members:
   :undoc-members:

.. autoclass:: MicrosoftTeamsConfig
   :members:
   :undoc-members:

.. autoclass:: NccAwsStableIpRule
   :members:
   :undoc-members:

.. autoclass:: NccAzurePrivateEndpointRule
   :members:
   :undoc-members:

.. py:class:: NccAzurePrivateEndpointRuleConnectionState

   .. py:attribute:: DISCONNECTED
      :value: "DISCONNECTED"

   .. py:attribute:: ESTABLISHED
      :value: "ESTABLISHED"

   .. py:attribute:: EXPIRED
      :value: "EXPIRED"

   .. py:attribute:: INIT
      :value: "INIT"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: REJECTED
      :value: "REJECTED"

.. autoclass:: NccAzureServiceEndpointRule
   :members:
   :undoc-members:

.. autoclass:: NccEgressConfig
   :members:
   :undoc-members:

.. autoclass:: NccEgressDefaultRules
   :members:
   :undoc-members:

.. autoclass:: NccEgressTargetRules
   :members:
   :undoc-members:

.. autoclass:: NetworkConnectivityConfiguration
   :members:
   :undoc-members:

.. autoclass:: NetworkPolicyEgress
   :members:
   :undoc-members:

.. autoclass:: NotificationDestination
   :members:
   :undoc-members:

.. autoclass:: PagerdutyConfig
   :members:
   :undoc-members:

.. autoclass:: PartitionId
   :members:
   :undoc-members:

.. autoclass:: PersonalComputeMessage
   :members:
   :undoc-members:

.. py:class:: PersonalComputeMessageEnum

   ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing all users to create single-machine compute resources. DELEGATE: Moves access control for the Personal Compute default policy to individual workspaces and requires a workspace’s users or groups to be added to the ACLs of that workspace’s Personal Compute default policy before they will be able to create compute resources through that policy.

   .. py:attribute:: DELEGATE
      :value: "DELEGATE"

   .. py:attribute:: ON
      :value: "ON"

.. autoclass:: PersonalComputeSetting
   :members:
   :undoc-members:

.. autoclass:: PublicTokenInfo
   :members:
   :undoc-members:

.. autoclass:: ReplaceIpAccessList
   :members:
   :undoc-members:

.. autoclass:: ReplaceResponse
   :members:
   :undoc-members:

.. autoclass:: RestrictWorkspaceAdminsMessage
   :members:
   :undoc-members:

.. py:class:: RestrictWorkspaceAdminsMessageStatus

   .. py:attribute:: ALLOW_ALL
      :value: "ALLOW_ALL"

   .. py:attribute:: RESTRICT_TOKENS_AND_JOB_RUN_AS
      :value: "RESTRICT_TOKENS_AND_JOB_RUN_AS"

.. autoclass:: RestrictWorkspaceAdminsSetting
   :members:
   :undoc-members:

.. autoclass:: RevokeTokenRequest
   :members:
   :undoc-members:

.. autoclass:: RevokeTokenResponse
   :members:
   :undoc-members:

.. autoclass:: SetStatusResponse
   :members:
   :undoc-members:

.. autoclass:: SlackConfig
   :members:
   :undoc-members:

.. autoclass:: StringMessage
   :members:
   :undoc-members:

.. autoclass:: TokenAccessControlRequest
   :members:
   :undoc-members:

.. autoclass:: TokenAccessControlResponse
   :members:
   :undoc-members:

.. autoclass:: TokenInfo
   :members:
   :undoc-members:

.. autoclass:: TokenPermission
   :members:
   :undoc-members:

.. py:class:: TokenPermissionLevel

   Permission level

   .. py:attribute:: CAN_USE
      :value: "CAN_USE"

.. autoclass:: TokenPermissions
   :members:
   :undoc-members:

.. autoclass:: TokenPermissionsDescription
   :members:
   :undoc-members:

.. autoclass:: TokenPermissionsRequest
   :members:
   :undoc-members:

.. py:class:: TokenType

   The type of token request. As of now, only `AZURE_ACTIVE_DIRECTORY_TOKEN` is supported.

   .. py:attribute:: ARCLIGHT_AZURE_EXCHANGE_TOKEN
      :value: "ARCLIGHT_AZURE_EXCHANGE_TOKEN"

   .. py:attribute:: ARCLIGHT_AZURE_EXCHANGE_TOKEN_WITH_USER_DELEGATION_KEY
      :value: "ARCLIGHT_AZURE_EXCHANGE_TOKEN_WITH_USER_DELEGATION_KEY"

   .. py:attribute:: ARCLIGHT_MULTI_TENANT_AZURE_EXCHANGE_TOKEN
      :value: "ARCLIGHT_MULTI_TENANT_AZURE_EXCHANGE_TOKEN"

   .. py:attribute:: ARCLIGHT_MULTI_TENANT_AZURE_EXCHANGE_TOKEN_WITH_USER_DELEGATION_KEY
      :value: "ARCLIGHT_MULTI_TENANT_AZURE_EXCHANGE_TOKEN_WITH_USER_DELEGATION_KEY"

   .. py:attribute:: AZURE_ACTIVE_DIRECTORY_TOKEN
      :value: "AZURE_ACTIVE_DIRECTORY_TOKEN"

.. autoclass:: UpdateAccountIpAccessEnableRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateAibiDashboardEmbeddingAccessPolicySettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateAibiDashboardEmbeddingApprovedDomainsSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateAutomaticClusterUpdateSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateComplianceSecurityProfileSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateCspEnablementAccountSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateDefaultNamespaceSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateDisableLegacyAccessRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateDisableLegacyDbfsRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateDisableLegacyFeaturesRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateEnableExportNotebookRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateEnableNotebookTableClipboardRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateEnableResultsDownloadingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateEnhancedSecurityMonitoringSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateEsmEnablementAccountSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateIpAccessList
   :members:
   :undoc-members:

.. autoclass:: UpdateLlmProxyPartnerPoweredAccountRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateLlmProxyPartnerPoweredEnforceRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateLlmProxyPartnerPoweredWorkspaceRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateNotificationDestinationRequest
   :members:
   :undoc-members:

.. autoclass:: UpdatePersonalComputeSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdatePrivateEndpointRule
   :members:
   :undoc-members:

.. autoclass:: UpdateResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateRestrictWorkspaceAdminsSettingRequest
   :members:
   :undoc-members:

.. autoclass:: WorkspaceNetworkOption
   :members:
   :undoc-members:

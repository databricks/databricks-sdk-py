Settings
========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.settings`` module.

.. py:currentmodule:: databricks.sdk.service.settings
.. autoclass:: CreateIpAccessList
   :members:
   :undoc-members:

.. autoclass:: CreateIpAccessListResponse
   :members:
   :undoc-members:

.. autoclass:: CreateNetworkConnectivityConfigRequest
   :members:
   :undoc-members:

.. autoclass:: CreateOboTokenRequest
   :members:
   :undoc-members:

.. autoclass:: CreateOboTokenResponse
   :members:
   :undoc-members:

.. autoclass:: CreatePrivateEndpointRuleRequest
   :members:
   :undoc-members:

.. py:class:: CreatePrivateEndpointRuleRequestGroupId

   The sub-resource type (group ID) of the target resource. Note that to connect to workspace root storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`.

   .. py:attribute:: BLOB
      :value: "BLOB"

   .. py:attribute:: DFS
      :value: "DFS"

   .. py:attribute:: MYSQL_SERVER
      :value: "MYSQL_SERVER"

   .. py:attribute:: SQL_SERVER
      :value: "SQL_SERVER"

.. autoclass:: CreateTokenRequest
   :members:
   :undoc-members:

.. autoclass:: CreateTokenResponse
   :members:
   :undoc-members:

.. autoclass:: DefaultNamespaceSetting
   :members:
   :undoc-members:

.. autoclass:: DeleteDefaultNamespaceSettingResponse
   :members:
   :undoc-members:

.. autoclass:: DeletePersonalComputeSettingResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteRestrictWorkspaceAdminsSettingResponse
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

.. autoclass:: NccAzurePrivateEndpointRule
   :members:
   :undoc-members:

.. py:class:: NccAzurePrivateEndpointRuleConnectionState

   The current status of this private endpoint. The private endpoint rules are effective only if the connection state is `ESTABLISHED`. Remember that you must approve new endpoints on your resources in the Azure portal before they take effect.
   The possible values are: - INIT: (deprecated) The endpoint has been created and pending approval. - PENDING: The endpoint has been created and pending approval. - ESTABLISHED: The endpoint has been approved and is ready to use in your serverless compute resources. - REJECTED: Connection was rejected by the private link resource owner. - DISCONNECTED: Connection was removed by the private link resource owner, the private endpoint becomes informative and should be deleted for clean-up.

   .. py:attribute:: DISCONNECTED
      :value: "DISCONNECTED"

   .. py:attribute:: ESTABLISHED
      :value: "ESTABLISHED"

   .. py:attribute:: INIT
      :value: "INIT"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: REJECTED
      :value: "REJECTED"

.. py:class:: NccAzurePrivateEndpointRuleGroupId

   The sub-resource type (group ID) of the target resource. Note that to connect to workspace root storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`.

   .. py:attribute:: BLOB
      :value: "BLOB"

   .. py:attribute:: DFS
      :value: "DFS"

   .. py:attribute:: MYSQL_SERVER
      :value: "MYSQL_SERVER"

   .. py:attribute:: SQL_SERVER
      :value: "SQL_SERVER"

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

.. autoclass:: RestrictWorkspaceAdminsMessage
   :members:
   :undoc-members:

.. py:class:: RestrictWorkspaceAdminsMessageStatus

   .. py:attribute:: ALLOW_ALL
      :value: "ALLOW_ALL"

   .. py:attribute:: RESTRICT_TOKENS_AND_JOB_RUN_AS
      :value: "RESTRICT_TOKENS_AND_JOB_RUN_AS"

   .. py:attribute:: STATUS_UNSPECIFIED
      :value: "STATUS_UNSPECIFIED"

.. autoclass:: RestrictWorkspaceAdminsSetting
   :members:
   :undoc-members:

.. autoclass:: RevokeTokenRequest
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

   .. py:attribute:: AZURE_ACTIVE_DIRECTORY_TOKEN
      :value: "AZURE_ACTIVE_DIRECTORY_TOKEN"

.. autoclass:: UpdateDefaultNamespaceSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateIpAccessList
   :members:
   :undoc-members:

.. autoclass:: UpdatePersonalComputeSettingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateRestrictWorkspaceAdminsSettingRequest
   :members:
   :undoc-members:

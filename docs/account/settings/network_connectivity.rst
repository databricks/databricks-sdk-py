``a.network_connectivity``: Network Connectivity
================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: NetworkConnectivityAPI

    These APIs provide configurations for the network connectivity of your workspaces for serverless compute
    resources. This API provides stable subnets for your workspace so that you can configure your firewalls on
    your Azure Storage accounts to allow access from Databricks. You can also use the API to provision private
    endpoints for Databricks to privately connect serverless compute resources to your Azure resources using
    Azure Private Link. See [configure serverless secure connectivity].
    
    [configure serverless secure connectivity]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security

    .. py:method:: create_network_connectivity_configuration(name: str, region: str) -> NetworkConnectivityConfiguration

        Create a network connectivity configuration.
        
        Creates a network connectivity configuration (NCC), which provides stable Azure service subnets when
        accessing your Azure Storage accounts. You can also use a network connectivity configuration to create
        Databricks-managed private endpoints so that Databricks serverless compute resources privately access
        your resources.
        
        **IMPORTANT**: After you create the network connectivity configuration, you must assign one or more
        workspaces to the new network connectivity configuration. You can share one network connectivity
        configuration with multiple workspaces from the same Azure region within the same Databricks account.
        See [configure serverless secure connectivity].
        
        [configure serverless secure connectivity]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security
        
        :param name: str
          The name of the network connectivity configuration. The name can contain alphanumeric characters,
          hyphens, and underscores. The length must be between 3 and 30 characters. The name must match the
          regular expression `^[0-9a-zA-Z-_]{3,30}$`.
        :param region: str
          The Azure region for this network connectivity configuration. Only workspaces in the same Azure
          region can be attached to this network connectivity configuration.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        

    .. py:method:: create_private_endpoint_rule(network_connectivity_config_id: str, resource_id: str, group_id: CreatePrivateEndpointRuleRequestGroupId) -> NccAzurePrivateEndpointRule

        Create a private endpoint rule.
        
        Create a private endpoint rule for the specified network connectivity config object. Once the object
        is created, Databricks asynchronously provisions a new Azure private endpoint to your specified Azure
        resource.
        
        **IMPORTANT**: You must use Azure portal or other Azure tools to approve the private endpoint to
        complete the connection. To get the information of the private endpoint created, make a `GET` request
        on the new private endpoint rule. See [serverless private link].
        
        [serverless private link]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security/serverless-private-link
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param resource_id: str
          The Azure resource ID of the target resource.
        :param group_id: :class:`CreatePrivateEndpointRuleRequestGroupId`
          The sub-resource type (group ID) of the target resource. Note that to connect to workspace root
          storage (root DBFS), you need two endpoints, one for `blob` and one for `dfs`.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        

    .. py:method:: delete_network_connectivity_configuration(network_connectivity_config_id: str)

        Delete a network connectivity configuration.
        
        Deletes a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        
        :returns: :class:`DeleteNetworkConnectivityConfigurationResponse`
        

    .. py:method:: delete_private_endpoint_rule(network_connectivity_config_id: str, private_endpoint_rule_id: str) -> NccAzurePrivateEndpointRule

        Delete a private endpoint rule.
        
        Initiates deleting a private endpoint rule. The private endpoint will be deactivated and will be
        purged after seven days of deactivation. When a private endpoint is in deactivated state,
        `deactivated` field is set to `true` and the private endpoint is not available to your serverless
        compute resources.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        

    .. py:method:: get_network_connectivity_configuration(network_connectivity_config_id: str) -> NetworkConnectivityConfiguration

        Get a network connectivity configuration.
        
        Gets a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        

    .. py:method:: get_private_endpoint_rule(network_connectivity_config_id: str, private_endpoint_rule_id: str) -> NccAzurePrivateEndpointRule

        Get a private endpoint rule.
        
        Gets the private endpoint rule.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccAzurePrivateEndpointRule`
        

    .. py:method:: list_network_connectivity_configurations( [, page_token: Optional[str]]) -> Iterator[NetworkConnectivityConfiguration]

        List network connectivity configurations.
        
        Gets an array of network connectivity configurations.
        
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NetworkConnectivityConfiguration`
        

    .. py:method:: list_private_endpoint_rules(network_connectivity_config_id: str [, page_token: Optional[str]]) -> Iterator[NccAzurePrivateEndpointRule]

        List private endpoint rules.
        
        Gets an array of private endpoint rules.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NccAzurePrivateEndpointRule`
        
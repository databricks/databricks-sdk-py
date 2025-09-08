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

    .. py:method:: create_network_connectivity_configuration(network_connectivity_config: CreateNetworkConnectivityConfiguration) -> NetworkConnectivityConfiguration

        Creates a network connectivity configuration (NCC), which provides stable Azure service subnets when
        accessing your Azure Storage accounts. You can also use a network connectivity configuration to create
        Databricks managed private endpoints so that Databricks serverless compute resources privately access
        your resources.
        
        **IMPORTANT**: After you create the network connectivity configuration, you must assign one or more
        workspaces to the new network connectivity configuration. You can share one network connectivity
        configuration with multiple workspaces from the same Azure region within the same Databricks account.
        See [configure serverless secure connectivity].
        
        [configure serverless secure connectivity]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security
        
        :param network_connectivity_config: :class:`CreateNetworkConnectivityConfiguration`
        
        :returns: :class:`NetworkConnectivityConfiguration`
        

    .. py:method:: create_private_endpoint_rule(network_connectivity_config_id: str, private_endpoint_rule: CreatePrivateEndpointRule) -> NccPrivateEndpointRule

        Create a private endpoint rule for the specified network connectivity config object. Once the object
        is created, Databricks asynchronously provisions a new Azure private endpoint to your specified Azure
        resource.
        
        **IMPORTANT**: You must use Azure portal or other Azure tools to approve the private endpoint to
        complete the connection. To get the information of the private endpoint created, make a `GET` request
        on the new private endpoint rule. See [serverless private link].
        
        [serverless private link]: https://learn.microsoft.com/azure/databricks/security/network/serverless-network-security/serverless-private-link
        
        :param network_connectivity_config_id: str
          Your Network Connectivity Configuration ID.
        :param private_endpoint_rule: :class:`CreatePrivateEndpointRule`
        
        :returns: :class:`NccPrivateEndpointRule`
        

    .. py:method:: delete_network_connectivity_configuration(network_connectivity_config_id: str)

        Deletes a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectivity Configuration ID.
        
        
        

    .. py:method:: delete_private_endpoint_rule(network_connectivity_config_id: str, private_endpoint_rule_id: str) -> NccPrivateEndpointRule

        Initiates deleting a private endpoint rule. If the connection state is PENDING or EXPIRED, the private
        endpoint is immediately deleted. Otherwise, the private endpoint is deactivated and will be deleted
        after seven days of deactivation. When a private endpoint is deactivated, the `deactivated` field is
        set to `true` and the private endpoint is not available to your serverless compute resources.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccPrivateEndpointRule`
        

    .. py:method:: get_network_connectivity_configuration(network_connectivity_config_id: str) -> NetworkConnectivityConfiguration

        Gets a network connectivity configuration.
        
        :param network_connectivity_config_id: str
          Your Network Connectivity Configuration ID.
        
        :returns: :class:`NetworkConnectivityConfiguration`
        

    .. py:method:: get_private_endpoint_rule(network_connectivity_config_id: str, private_endpoint_rule_id: str) -> NccPrivateEndpointRule

        Gets the private endpoint rule.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        
        :returns: :class:`NccPrivateEndpointRule`
        

    .. py:method:: list_network_connectivity_configurations( [, page_token: Optional[str]]) -> Iterator[NetworkConnectivityConfiguration]

        Gets an array of network connectivity configurations.
        
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NetworkConnectivityConfiguration`
        

    .. py:method:: list_private_endpoint_rules(network_connectivity_config_id: str [, page_token: Optional[str]]) -> Iterator[NccPrivateEndpointRule]

        Gets an array of private endpoint rules.
        
        :param network_connectivity_config_id: str
          Your Network Connectvity Configuration ID.
        :param page_token: str (optional)
          Pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`NccPrivateEndpointRule`
        

    .. py:method:: update_private_endpoint_rule(network_connectivity_config_id: str, private_endpoint_rule_id: str, private_endpoint_rule: UpdatePrivateEndpointRule, update_mask: str) -> NccPrivateEndpointRule

        Updates a private endpoint rule. Currently only a private endpoint rule to customer-managed resources
        is allowed to be updated.
        
        :param network_connectivity_config_id: str
          The ID of a network connectivity configuration, which is the parent resource of this private
          endpoint rule object.
        :param private_endpoint_rule_id: str
          Your private endpoint rule ID.
        :param private_endpoint_rule: :class:`UpdatePrivateEndpointRule`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
        
        :returns: :class:`NccPrivateEndpointRule`
        
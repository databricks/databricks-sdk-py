``w.vector_search_endpoints``: Endpoints
========================================
.. currentmodule:: databricks.sdk.service.vectorsearch

.. py:class:: VectorSearchEndpointsAPI

    **Endpoint**: Represents the compute resources to host vector search indexes.

    .. py:method:: create_endpoint(name: str, endpoint_type: EndpointType [, budget_policy_id: Optional[str]]) -> Wait[EndpointInfo]

        Create an endpoint.
        
        Create a new endpoint.
        
        :param name: str
          Name of the vector search endpoint
        :param endpoint_type: :class:`EndpointType`
          Type of endpoint
        :param budget_policy_id: str (optional)
          The budget policy id to be applied
        
        :returns:
          Long-running operation waiter for :class:`EndpointInfo`.
          See :method:wait_get_endpoint_vector_search_endpoint_online for more details.
        

    .. py:method:: create_endpoint_and_wait(name: str, endpoint_type: EndpointType [, budget_policy_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> EndpointInfo


    .. py:method:: delete_endpoint(endpoint_name: str)

        Delete an endpoint.
        
        Delete a vector search endpoint.
        
        :param endpoint_name: str
          Name of the vector search endpoint
        
        
        

    .. py:method:: get_endpoint(endpoint_name: str) -> EndpointInfo

        Get an endpoint.
        
        Get details for a single vector search endpoint.
        
        :param endpoint_name: str
          Name of the endpoint
        
        :returns: :class:`EndpointInfo`
        

    .. py:method:: list_endpoints( [, page_token: Optional[str]]) -> Iterator[EndpointInfo]

        List all endpoints.
        
        List all vector search endpoints in the workspace.
        
        :param page_token: str (optional)
          Token for pagination
        
        :returns: Iterator over :class:`EndpointInfo`
        

    .. py:method:: update_endpoint_budget_policy(endpoint_name: str, budget_policy_id: str) -> PatchEndpointBudgetPolicyResponse

        Update the budget policy of an endpoint.
        
        Update the budget policy of an endpoint
        
        :param endpoint_name: str
          Name of the vector search endpoint
        :param budget_policy_id: str
          The budget policy id to be applied
        
        :returns: :class:`PatchEndpointBudgetPolicyResponse`
        

    .. py:method:: update_endpoint_custom_tags(endpoint_name: str, custom_tags: List[CustomTag]) -> UpdateEndpointCustomTagsResponse

        Update the custom tags of an endpoint.
        
        :param endpoint_name: str
          Name of the vector search endpoint
        :param custom_tags: List[:class:`CustomTag`]
          The new custom tags for the vector search endpoint
        
        :returns: :class:`UpdateEndpointCustomTagsResponse`
        

    .. py:method:: wait_get_endpoint_vector_search_endpoint_online(endpoint_name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[EndpointInfo], None]]) -> EndpointInfo

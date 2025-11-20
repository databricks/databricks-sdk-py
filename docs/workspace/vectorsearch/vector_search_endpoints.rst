``w.vector_search_endpoints``: Endpoints
========================================
.. currentmodule:: databricks.sdk.service.vectorsearch

.. py:class:: VectorSearchEndpointsAPI

    **Endpoint**: Represents the compute resources to host vector search indexes.

    .. py:method:: create_endpoint(name: str, endpoint_type: EndpointType [, budget_policy_id: Optional[str], num_replicas: Optional[int], usage_policy_id: Optional[str]]) -> Wait[EndpointInfo]

        Create a new endpoint.

        :param name: str
          Name of the vector search endpoint
        :param endpoint_type: :class:`EndpointType`
          Type of endpoint
        :param budget_policy_id: str (optional)
          The budget policy id to be applied
        :param num_replicas: int (optional)
          Initial number of replicas for the endpoint. If not specified, defaults to 1.
        :param usage_policy_id: str (optional)
          The usage policy id to be applied once we've migrated to usage policies

        :returns:
          Long-running operation waiter for :class:`EndpointInfo`.
          See :method:wait_get_endpoint_vector_search_endpoint_online for more details.
        

    .. py:method:: create_endpoint_and_wait(name: str, endpoint_type: EndpointType [, budget_policy_id: Optional[str], num_replicas: Optional[int], usage_policy_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> EndpointInfo


    .. py:method:: delete_endpoint(endpoint_name: str)

        Delete a vector search endpoint.

        :param endpoint_name: str
          Name of the vector search endpoint


        

    .. py:method:: get_endpoint(endpoint_name: str) -> EndpointInfo

        Get details for a single vector search endpoint.

        :param endpoint_name: str
          Name of the endpoint

        :returns: :class:`EndpointInfo`
        

    .. py:method:: list_endpoints( [, page_token: Optional[str]]) -> Iterator[EndpointInfo]

        List all vector search endpoints in the workspace.

        :param page_token: str (optional)
          Token for pagination

        :returns: Iterator over :class:`EndpointInfo`
        

    .. py:method:: patch_endpoint_throughput(endpoint_name: str [, all_or_nothing: Optional[bool], concurrency: Optional[float], maximum_concurrency_allowed: Optional[float], minimal_concurrency_allowed: Optional[float], num_replicas: Optional[int]]) -> PatchEndpointThroughputResponse

        Update the throughput (concurrency) of an endpoint

        :param endpoint_name: str
          Name of the vector search endpoint
        :param all_or_nothing: bool (optional)
          If true, the request will fail if the requested concurrency or limits cannot be exactly met. If
          false, the request will be adjusted to the closest possible value.
        :param concurrency: float (optional)
          Requested concurrency (total CPU) for the endpoint. If not specified, the current concurrency is
          maintained.
        :param maximum_concurrency_allowed: float (optional)
          Maximum concurrency allowed for the endpoint. If not specified, the current maximum is maintained.
        :param minimal_concurrency_allowed: float (optional)
          Minimum concurrency allowed for the endpoint. If not specified, the current minimum is maintained.
        :param num_replicas: int (optional)
          Requested number of data copies for the endpoint (including primary). For example: num_replicas=2
          means 2 total copies of the data (1 primary + 1 replica). If not specified, the current replication
          factor is maintained. Valid range: 1-6 (where 1 = no replication, 6 = 1 primary + 5 replicas).

        :returns: :class:`PatchEndpointThroughputResponse`
        

    .. py:method:: retrieve_user_visible_metrics(name: str [, end_time: Optional[str], granularity_in_seconds: Optional[int], metrics: Optional[List[Metric]], page_token: Optional[str], start_time: Optional[str]]) -> RetrieveUserVisibleMetricsResponse

        Retrieve user-visible metrics for an endpoint

        :param name: str
          Vector search endpoint name
        :param end_time: str (optional)
          End time for metrics query
        :param granularity_in_seconds: int (optional)
          Granularity in seconds
        :param metrics: List[:class:`Metric`] (optional)
          List of metrics to retrieve
        :param page_token: str (optional)
          Token for pagination
        :param start_time: str (optional)
          Start time for metrics query

        :returns: :class:`RetrieveUserVisibleMetricsResponse`
        

    .. py:method:: update_endpoint_budget_policy(endpoint_name: str, budget_policy_id: str) -> PatchEndpointBudgetPolicyResponse

        Update the budget policy of an endpoint

        :param endpoint_name: str
          Name of the vector search endpoint
        :param budget_policy_id: str
          The budget policy id to be applied (hima-sheth) TODO: remove this once we've migrated to usage
          policies

        :returns: :class:`PatchEndpointBudgetPolicyResponse`
        

    .. py:method:: update_endpoint_custom_tags(endpoint_name: str, custom_tags: List[CustomTag]) -> UpdateEndpointCustomTagsResponse

        Update the custom tags of an endpoint.

        :param endpoint_name: str
          Name of the vector search endpoint
        :param custom_tags: List[:class:`CustomTag`]
          The new custom tags for the vector search endpoint

        :returns: :class:`UpdateEndpointCustomTagsResponse`
        

    .. py:method:: wait_get_endpoint_vector_search_endpoint_online(endpoint_name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[EndpointInfo], None]]) -> EndpointInfo

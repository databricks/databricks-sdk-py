``w.vector_search_endpoints``: Endpoints
========================================
.. currentmodule:: databricks.sdk.service.vectorsearch

.. py:class:: VectorSearchEndpointsAPI

    **Endpoint**: Represents the compute resources to host AI Search indexes.

    .. py:method:: create_endpoint(name: str, endpoint_type: EndpointType [, budget_policy_id: Optional[str], target_qps: Optional[int], usage_policy_id: Optional[str]]) -> Wait[EndpointInfo]

        Create a new endpoint.

        :param name: str
          Name of the AI Search endpoint. The name must be unique within the workspace, have at most 50
          characters, contain only lowercase letters, digits, hyphens, underscores and periods, and start and
          end with a letter or digit.
        :param endpoint_type: :class:`EndpointType`
          Type of endpoint to create. STANDARD endpoints are optimized for low-latency queries and support
          Target QPS scaling. STORAGE_OPTIMIZED endpoints hold much larger indexes and index faster, with
          higher query latency. See https://docs.databricks.com/aws/en/ai-search/ai-search#endpoint-options.
        :param budget_policy_id: str (optional)
          Budget policy to attribute the endpoint's usage to. If omitted, the default budget policy applies.
        :param target_qps: int (optional)
          Target queries per second (QPS) for the endpoint. Supported for STANDARD endpoints only. The actual
          replica count is calculated at index creation/sync time based on this value. Best-effort target; the
          system does not guarantee this QPS will be achieved.
        :param usage_policy_id: str (optional)
          The usage policy id to be applied once we've migrated to usage policies

        :returns:
          Long-running operation waiter for :class:`EndpointInfo`.
          See :method:wait_get_endpoint_vector_search_endpoint_online for more details.
        

    .. py:method:: create_endpoint_and_wait(name: str, endpoint_type: EndpointType [, budget_policy_id: Optional[str], target_qps: Optional[int], usage_policy_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> EndpointInfo


    .. py:method:: delete_endpoint(endpoint_name: str)

        Delete an AI Search endpoint.

        :param endpoint_name: str
          Name of the AI Search endpoint


        

    .. py:method:: get_endpoint(endpoint_name: str) -> EndpointInfo

        Get details for a single AI Search endpoint.

        :param endpoint_name: str
          Name of the endpoint

        :returns: :class:`EndpointInfo`
        

    .. py:method:: get_permission_levels(endpoint_id: str) -> GetVectorSearchEndpointPermissionLevelsResponse

        Gets the permission levels that a user can have on an object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.

        :returns: :class:`GetVectorSearchEndpointPermissionLevelsResponse`
        

    .. py:method:: get_permissions(endpoint_id: str) -> VectorSearchEndpointPermissions

        Gets the permissions of a vector search endpoint. Vector search endpoints can inherit permissions from
        their root object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.

        :returns: :class:`VectorSearchEndpointPermissions`
        

    .. py:method:: list_endpoints( [, page_token: Optional[str]]) -> Iterator[EndpointInfo]

        List all AI Search endpoints in the workspace.

        :param page_token: str (optional)
          Token for pagination

        :returns: Iterator over :class:`EndpointInfo`
        

    .. py:method:: patch_endpoint(endpoint_name: str [, target_qps: Optional[int]]) -> EndpointInfo

        Update the Target QPS of a STANDARD endpoint. The response is the updated endpoint; its scaling_info
        shows whether the resulting scaling change is applied or still in progress.

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param target_qps: int (optional)
          Target QPS for the endpoint. Best-effort; the system does not guarantee this QPS will be achieved.
          Set to -1 to clear the Target QPS, as if it had never been set.

        :returns: :class:`EndpointInfo`
        

    .. py:method:: retrieve_user_visible_metrics(name: str [, end_time: Optional[str], granularity_in_seconds: Optional[int], metrics: Optional[List[Metric]], page_token: Optional[str], start_time: Optional[str]]) -> RetrieveUserVisibleMetricsResponse

        Retrieve time series of usage and health metrics for an endpoint and its indexes, such as request
        counts, request latency percentiles and endpoint utilization.

        :param name: str
          Name of the endpoint whose metrics to retrieve.
        :param end_time: str (optional)
          End of the time range. Defaults to the current time. Must be later than ``start_time``.
        :param granularity_in_seconds: int (optional)
          Requested interval between data points, in seconds. Defaults to 60, which is also the minimum. The
          server may return a finer or coarser interval: 60 seconds only for time ranges of 1 hour or less,
          otherwise 300 seconds or more. Read the interval from the returned timestamps.
        :param metrics: List[:class:`Metric`] (optional)
          Metrics to retrieve. Each entry names a metric and optionally narrows it with labels or a
          percentile. An unknown metric name fails the whole request, and an empty list returns no series.
        :param page_token: str (optional)
          Not used. The response returns all data points in one page.
        :param start_time: str (optional)
          Start of the time range. Required. Must be within the last 169 hours.

        :returns: :class:`RetrieveUserVisibleMetricsResponse`
        

    .. py:method:: set_permissions(endpoint_id: str [, access_control_list: Optional[List[VectorSearchEndpointAccessControlRequest]]]) -> VectorSearchEndpointPermissions

        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`VectorSearchEndpointAccessControlRequest`] (optional)

        :returns: :class:`VectorSearchEndpointPermissions`
        

    .. py:method:: start_endpoint(endpoint_name: str) -> EndpointInfo

        Start a stopped endpoint. The endpoint serves the same indexes it had when it stopped.

        :param endpoint_name: str
          Name of the AI Search endpoint

        :returns: :class:`EndpointInfo`
        

    .. py:method:: stop_endpoint(endpoint_name: str) -> EndpointInfo

        Stop an endpoint. Stopping removes the endpoint's serving compute and retains its indexes. A stopped
        endpoint can't serve queries or sync indexes until it is started.

        :param endpoint_name: str
          Name of the AI Search endpoint

        :returns: :class:`EndpointInfo`
        

    .. py:method:: update_endpoint_budget_policy(endpoint_name: str, budget_policy_id: str) -> PatchEndpointBudgetPolicyResponse

        Update the budget policy that the endpoint's usage is attributed to.

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param budget_policy_id: str
          The budget policy id to be applied

        :returns: :class:`PatchEndpointBudgetPolicyResponse`
        

    .. py:method:: update_endpoint_custom_tags(endpoint_name: str, custom_tags: List[CustomTag]) -> UpdateEndpointCustomTagsResponse

        Update the custom tags of an endpoint.

        :param endpoint_name: str
          Name of the AI Search endpoint
        :param custom_tags: List[:class:`CustomTag`]
          The new custom tags for the AI Search endpoint

        :returns: :class:`UpdateEndpointCustomTagsResponse`
        

    .. py:method:: update_permissions(endpoint_id: str [, access_control_list: Optional[List[VectorSearchEndpointAccessControlRequest]]]) -> VectorSearchEndpointPermissions

        Updates the permissions on a vector search endpoint. Vector search endpoints can inherit permissions
        from their root object.

        :param endpoint_id: str
          The vector search endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`VectorSearchEndpointAccessControlRequest`] (optional)

        :returns: :class:`VectorSearchEndpointPermissions`
        

    .. py:method:: wait_get_endpoint_vector_search_endpoint_online(endpoint_name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[EndpointInfo], None]]) -> EndpointInfo

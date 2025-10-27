``w.serving_endpoints``: Serving endpoints
==========================================
.. currentmodule:: databricks.sdk.service.serving

.. py:class:: ServingEndpointsExt

    The Serving Endpoints API allows you to create, update, and delete model serving endpoints.

    You can use a serving endpoint to serve models from the Databricks Model Registry or from Unity Catalog.
    Endpoints expose the underlying models as scalable REST API endpoints using serverless compute. This means
    the endpoints and associated compute resources are fully managed by Databricks and will not appear in your
    cloud account. A serving endpoint can consist of one or more MLflow models from the Databricks Model
    Registry, called served entities. A serving endpoint can have at most ten served entities. You can
    configure traffic settings to define how requests should be routed to your served entities behind an
    endpoint. Additionally, you can configure the scale of resources that should be applied to each served
    entity.

    .. py:method:: build_logs(name: str, served_model_name: str) -> BuildLogsResponse

        Retrieves the build logs associated with the provided served model.

        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that build logs will be retrieved for. This field is required.

        :returns: :class:`BuildLogsResponse`
        

    .. py:method:: create(name: str [, ai_gateway: Optional[AiGatewayConfig], budget_policy_id: Optional[str], config: Optional[EndpointCoreConfigInput], description: Optional[str], email_notifications: Optional[EmailNotifications], rate_limits: Optional[List[RateLimit]], route_optimized: Optional[bool], tags: Optional[List[EndpointTag]]]) -> Wait[ServingEndpointDetailed]

        Create a new serving endpoint.

        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param ai_gateway: :class:`AiGatewayConfig` (optional)
          The AI Gateway configuration for the serving endpoint. NOTE: External model, provisioned throughput,
          and pay-per-token endpoints are fully supported; agent endpoints currently only support inference
          tables.
        :param budget_policy_id: str (optional)
          The budget policy to be applied to the serving endpoint.
        :param config: :class:`EndpointCoreConfigInput` (optional)
          The core config of the serving endpoint.
        :param description: str (optional)
        :param email_notifications: :class:`EmailNotifications` (optional)
          Email notification settings.
        :param rate_limits: List[:class:`RateLimit`] (optional)
          Rate limits to be applied to the serving endpoint. NOTE: this field is deprecated, please use AI
          Gateway to manage rate limits.
        :param route_optimized: bool (optional)
          Enable route optimization for the serving endpoint.
        :param tags: List[:class:`EndpointTag`] (optional)
          Tags to be attached to the serving endpoint and automatically propagated to billing logs.

        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: create_and_wait(name: str [, ai_gateway: Optional[AiGatewayConfig], budget_policy_id: Optional[str], config: Optional[EndpointCoreConfigInput], description: Optional[str], email_notifications: Optional[EmailNotifications], rate_limits: Optional[List[RateLimit]], route_optimized: Optional[bool], tags: Optional[List[EndpointTag]], timeout: datetime.timedelta = 0:20:00]) -> ServingEndpointDetailed


    .. py:method:: create_provisioned_throughput_endpoint(name: str, config: PtEndpointCoreConfig [, ai_gateway: Optional[AiGatewayConfig], budget_policy_id: Optional[str], email_notifications: Optional[EmailNotifications], tags: Optional[List[EndpointTag]]]) -> Wait[ServingEndpointDetailed]

        Create a new PT serving endpoint.

        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param config: :class:`PtEndpointCoreConfig`
          The core config of the serving endpoint.
        :param ai_gateway: :class:`AiGatewayConfig` (optional)
          The AI Gateway configuration for the serving endpoint.
        :param budget_policy_id: str (optional)
          The budget policy associated with the endpoint.
        :param email_notifications: :class:`EmailNotifications` (optional)
          Email notification settings.
        :param tags: List[:class:`EndpointTag`] (optional)
          Tags to be attached to the serving endpoint and automatically propagated to billing logs.

        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: create_provisioned_throughput_endpoint_and_wait(name: str, config: PtEndpointCoreConfig [, ai_gateway: Optional[AiGatewayConfig], budget_policy_id: Optional[str], email_notifications: Optional[EmailNotifications], tags: Optional[List[EndpointTag]], timeout: datetime.timedelta = 0:20:00]) -> ServingEndpointDetailed


    .. py:method:: delete(name: str)

        Delete a serving endpoint.

        :param name: str


        

    .. py:method:: export_metrics(name: str) -> ExportMetricsResponse

        Retrieves the metrics associated with the provided serving endpoint in either Prometheus or
        OpenMetrics exposition format.

        :param name: str
          The name of the serving endpoint to retrieve metrics for. This field is required.

        :returns: :class:`ExportMetricsResponse`
        

    .. py:method:: get(name: str) -> ServingEndpointDetailed

        Retrieves the details for a single serving endpoint.

        :param name: str
          The name of the serving endpoint. This field is required.

        :returns: :class:`ServingEndpointDetailed`
        

    .. py:method:: get_langchain_chat_open_ai_client(model)


    .. py:method:: get_open_ai_client()

        Create an OpenAI client configured for Databricks Model Serving.

        Returns an OpenAI client instance that is pre-configured to send requests to
        Databricks Model Serving endpoints. The client uses Databricks authentication
        to query endpoints within the workspace associated with the current WorkspaceClient
        instance.

        Args:
            **kwargs: Additional parameters to pass to the OpenAI client constructor.
                Common parameters include:
                - timeout (float): Request timeout in seconds (e.g., 30.0)
                - max_retries (int): Maximum number of retries for failed requests (e.g., 3)
                - default_headers (dict): Additional headers to include with requests
                - default_query (dict): Additional query parameters to include with requests

                Any parameter accepted by the OpenAI client constructor can be passed here,
                except for the following parameters which are reserved for Databricks integration:
                base_url, api_key, http_client

        Returns:
            OpenAI: An OpenAI client instance configured for Databricks Model Serving.

        Raises:
            ImportError: If the OpenAI library is not installed.
            ValueError: If any reserved Databricks parameters are provided in kwargs.

        Example:
            >>> client = workspace_client.serving_endpoints.get_open_ai_client()
            >>> # With custom timeout and retries
            >>> client = workspace_client.serving_endpoints.get_open_ai_client(
            ...     timeout=30.0,
            ...     max_retries=5
            ... )
        

    .. py:method:: get_open_api(name: str) -> GetOpenApiResponse

        Get the query schema of the serving endpoint in OpenAPI format. The schema contains information for
        the supported paths, input and output format and datatypes.

        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.

        :returns: :class:`GetOpenApiResponse`
        

    .. py:method:: get_permission_levels(serving_endpoint_id: str) -> GetServingEndpointPermissionLevelsResponse

        Gets the permission levels that a user can have on an object.

        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.

        :returns: :class:`GetServingEndpointPermissionLevelsResponse`
        

    .. py:method:: get_permissions(serving_endpoint_id: str) -> ServingEndpointPermissions

        Gets the permissions of a serving endpoint. Serving endpoints can inherit permissions from their root
        object.

        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.

        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: http_request(conn: str, method: ExternalFunctionRequestHttpMethod, path: str [, headers: typing.Dict[str, str], json: typing.Dict[str, str], params: typing.Dict[str, str]]) -> Response

        Make external services call using the credentials stored in UC Connection.
        **NOTE:** Experimental: This API may change or be removed in a future release without warning.
        :param conn: str
          The connection name to use. This is required to identify the external connection.
        :param method: :class:`ExternalFunctionRequestHttpMethod`
          The HTTP method to use (e.g., 'GET', 'POST'). This is required.
        :param path: str
          The relative path for the API endpoint. This is required.
        :param headers: Dict[str,str] (optional)
          Additional headers for the request. If not provided, only auth headers from connections would be
          passed.
        :param json: Dict[str,str] (optional)
          JSON payload for the request.
        :param params: Dict[str,str] (optional)
          Query parameters for the request.
        :returns: :class:`Response`
        

    .. py:method:: list() -> Iterator[ServingEndpoint]

        Get all serving endpoints.


        :returns: Iterator over :class:`ServingEndpoint`
        

    .. py:method:: logs(name: str, served_model_name: str) -> ServerLogsResponse

        Retrieves the service logs associated with the provided served model.

        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that logs will be retrieved for. This field is required.

        :returns: :class:`ServerLogsResponse`
        

    .. py:method:: patch(name: str [, add_tags: Optional[List[EndpointTag]], delete_tags: Optional[List[str]]]) -> EndpointTags

        Used to batch add and delete tags from a serving endpoint with a single API call.

        :param name: str
          The name of the serving endpoint who's tags to patch. This field is required.
        :param add_tags: List[:class:`EndpointTag`] (optional)
          List of endpoint tags to add
        :param delete_tags: List[str] (optional)
          List of tag keys to delete

        :returns: :class:`EndpointTags`
        

    .. py:method:: put(name: str [, rate_limits: Optional[List[RateLimit]]]) -> PutResponse

        Deprecated: Please use AI Gateway to manage rate limits instead.

        :param name: str
          The name of the serving endpoint whose rate limits are being updated. This field is required.
        :param rate_limits: List[:class:`RateLimit`] (optional)
          The list of endpoint rate limits.

        :returns: :class:`PutResponse`
        

    .. py:method:: put_ai_gateway(name: str [, fallback_config: Optional[FallbackConfig], guardrails: Optional[AiGatewayGuardrails], inference_table_config: Optional[AiGatewayInferenceTableConfig], rate_limits: Optional[List[AiGatewayRateLimit]], usage_tracking_config: Optional[AiGatewayUsageTrackingConfig]]) -> PutAiGatewayResponse

        Used to update the AI Gateway of a serving endpoint. NOTE: External model, provisioned throughput, and
        pay-per-token endpoints are fully supported; agent endpoints currently only support inference tables.

        :param name: str
          The name of the serving endpoint whose AI Gateway is being updated. This field is required.
        :param fallback_config: :class:`FallbackConfig` (optional)
          Configuration for traffic fallback which auto fallbacks to other served entities if the request to a
          served entity fails with certain error codes, to increase availability.
        :param guardrails: :class:`AiGatewayGuardrails` (optional)
          Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.
        :param inference_table_config: :class:`AiGatewayInferenceTableConfig` (optional)
          Configuration for payload logging using inference tables. Use these tables to monitor and audit data
          being sent to and received from model APIs and to improve model quality.
        :param rate_limits: List[:class:`AiGatewayRateLimit`] (optional)
          Configuration for rate limits which can be set to limit endpoint traffic.
        :param usage_tracking_config: :class:`AiGatewayUsageTrackingConfig` (optional)
          Configuration to enable usage tracking using system tables. These tables allow you to monitor
          operational usage on endpoints and their associated costs.

        :returns: :class:`PutAiGatewayResponse`
        

    .. py:method:: query(name: str [, client_request_id: Optional[str], dataframe_records: Optional[List[Any]], dataframe_split: Optional[DataframeSplitInput], extra_params: Optional[Dict[str, str]], input: Optional[Any], inputs: Optional[Any], instances: Optional[List[Any]], max_tokens: Optional[int], messages: Optional[List[ChatMessage]], n: Optional[int], prompt: Optional[Any], stop: Optional[List[str]], stream: Optional[bool], temperature: Optional[float], usage_context: Optional[Dict[str, str]]]) -> QueryEndpointResponse

        Query a serving endpoint

        :param name: str
          The name of the serving endpoint. This field is required and is provided via the path parameter.
        :param client_request_id: str (optional)
          Optional user-provided request identifier that will be recorded in the inference table and the usage
          tracking table.
        :param dataframe_records: List[Any] (optional)
          Pandas Dataframe input in the records orientation.
        :param dataframe_split: :class:`DataframeSplitInput` (optional)
          Pandas Dataframe input in the split orientation.
        :param extra_params: Dict[str,str] (optional)
          The extra parameters field used ONLY for __completions, chat,__ and __embeddings external &
          foundation model__ serving endpoints. This is a map of strings and should only be used with other
          external/foundation model query fields.
        :param input: Any (optional)
          The input string (or array of strings) field used ONLY for __embeddings external & foundation
          model__ serving endpoints and is the only field (along with extra_params if needed) used by
          embeddings queries.
        :param inputs: Any (optional)
          Tensor-based input in columnar format.
        :param instances: List[Any] (optional)
          Tensor-based input in row format.
        :param max_tokens: int (optional)
          The max tokens field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is an integer and should only be used with other chat/completions query fields.
        :param messages: List[:class:`ChatMessage`] (optional)
          The messages field used ONLY for __chat external & foundation model__ serving endpoints. This is an
          array of ChatMessage objects and should only be used with other chat query fields.
        :param n: int (optional)
          The n (number of candidates) field used ONLY for __completions__ and __chat external & foundation
          model__ serving endpoints. This is an integer between 1 and 5 with a default of 1 and should only be
          used with other chat/completions query fields.
        :param prompt: Any (optional)
          The prompt string (or array of strings) field used ONLY for __completions external & foundation
          model__ serving endpoints and should only be used with other completions query fields.
        :param stop: List[str] (optional)
          The stop sequences field used ONLY for __completions__ and __chat external & foundation model__
          serving endpoints. This is a list of strings and should only be used with other chat/completions
          query fields.
        :param stream: bool (optional)
          The stream field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is a boolean defaulting to false and should only be used with other chat/completions
          query fields.
        :param temperature: float (optional)
          The temperature field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is a float between 0.0 and 2.0 with a default of 1.0 and should only be used with
          other chat/completions query fields.
        :param usage_context: Dict[str,str] (optional)
          Optional user-provided context that will be recorded in the usage tracking table.

        :returns: :class:`QueryEndpointResponse`
        

    .. py:method:: set_permissions(serving_endpoint_id: str [, access_control_list: Optional[List[ServingEndpointAccessControlRequest]]]) -> ServingEndpointPermissions

        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)

        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: update_config(name: str [, auto_capture_config: Optional[AutoCaptureConfigInput], served_entities: Optional[List[ServedEntityInput]], served_models: Optional[List[ServedModelInput]], traffic_config: Optional[TrafficConfig]]) -> Wait[ServingEndpointDetailed]

        Updates any combination of the serving endpoint's served entities, the compute configuration of those
        served entities, and the endpoint's traffic config. An endpoint that already has an update in progress
        can not be updated until the current update completes or fails.

        :param name: str
          The name of the serving endpoint to update. This field is required.
        :param auto_capture_config: :class:`AutoCaptureConfigInput` (optional)
          Configuration for Inference Tables which automatically logs requests and responses to Unity Catalog.
          Note: this field is deprecated for creating new provisioned throughput endpoints, or updating
          existing provisioned throughput endpoints that never have inference table configured; in these cases
          please use AI Gateway to manage inference tables.
        :param served_entities: List[:class:`ServedEntityInput`] (optional)
          The list of served entities under the serving endpoint config.
        :param served_models: List[:class:`ServedModelInput`] (optional)
          (Deprecated, use served_entities instead) The list of served models under the serving endpoint
          config.
        :param traffic_config: :class:`TrafficConfig` (optional)
          The traffic configuration associated with the serving endpoint config.

        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: update_config_and_wait(name: str [, auto_capture_config: Optional[AutoCaptureConfigInput], served_entities: Optional[List[ServedEntityInput]], served_models: Optional[List[ServedModelInput]], traffic_config: Optional[TrafficConfig], timeout: datetime.timedelta = 0:20:00]) -> ServingEndpointDetailed


    .. py:method:: update_notifications(name: str [, email_notifications: Optional[EmailNotifications]]) -> UpdateInferenceEndpointNotificationsResponse

        Updates the email and webhook notification settings for an endpoint.

        :param name: str
          The name of the serving endpoint whose notifications are being updated. This field is required.
        :param email_notifications: :class:`EmailNotifications` (optional)
          The email notification settings to update. Specify email addresses to notify when endpoint state
          changes occur.

        :returns: :class:`UpdateInferenceEndpointNotificationsResponse`
        

    .. py:method:: update_permissions(serving_endpoint_id: str [, access_control_list: Optional[List[ServingEndpointAccessControlRequest]]]) -> ServingEndpointPermissions

        Updates the permissions on a serving endpoint. Serving endpoints can inherit permissions from their
        root object.

        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)

        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: update_provisioned_throughput_endpoint_config(name: str, config: PtEndpointCoreConfig) -> Wait[ServingEndpointDetailed]

        Updates any combination of the pt endpoint's served entities, the compute configuration of those
        served entities, and the endpoint's traffic config. Updates are instantaneous and endpoint should be
        updated instantly

        :param name: str
          The name of the pt endpoint to update. This field is required.
        :param config: :class:`PtEndpointCoreConfig`

        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: update_provisioned_throughput_endpoint_config_and_wait(name: str, config: PtEndpointCoreConfig, timeout: datetime.timedelta = 0:20:00) -> ServingEndpointDetailed


    .. py:method:: wait_get_serving_endpoint_not_updating(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[ServingEndpointDetailed], None]]) -> ServingEndpointDetailed

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

        Get build logs for a served model.
        
        Retrieves the build logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that build logs will be retrieved for. This field is required.
        
        :returns: :class:`BuildLogsResponse`
        

    .. py:method:: create(name: str, config: EndpointCoreConfigInput [, ai_gateway: Optional[AiGatewayConfig], rate_limits: Optional[List[RateLimit]], route_optimized: Optional[bool], tags: Optional[List[EndpointTag]]]) -> Wait[ServingEndpointDetailed]

        Create a new serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param config: :class:`EndpointCoreConfigInput`
          The core config of the serving endpoint.
        :param ai_gateway: :class:`AiGatewayConfig` (optional)
          The AI Gateway configuration for the serving endpoint. NOTE: only external model endpoints are
          supported as of now.
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
        

    .. py:method:: create_and_wait(name: str, config: EndpointCoreConfigInput [, ai_gateway: Optional[AiGatewayConfig], rate_limits: Optional[List[RateLimit]], route_optimized: Optional[bool], tags: Optional[List[EndpointTag]], timeout: datetime.timedelta = 0:20:00]) -> ServingEndpointDetailed


    .. py:method:: delete(name: str)

        Delete a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        
        

    .. py:method:: export_metrics(name: str) -> ExportMetricsResponse

        Get metrics of a serving endpoint.
        
        Retrieves the metrics associated with the provided serving endpoint in either Prometheus or
        OpenMetrics exposition format.
        
        :param name: str
          The name of the serving endpoint to retrieve metrics for. This field is required.
        
        :returns: :class:`ExportMetricsResponse`
        

    .. py:method:: get(name: str) -> ServingEndpointDetailed

        Get a single serving endpoint.
        
        Retrieves the details for a single serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`ServingEndpointDetailed`
        

    .. py:method:: get_langchain_chat_open_ai_client(model)


    .. py:method:: get_open_ai_client()


    .. py:method:: get_open_api(name: str)

        Get the schema for a serving endpoint.
        
        Get the query schema of the serving endpoint in OpenAPI format. The schema contains information for
        the supported paths, input and output format and datatypes.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        
        
        

    .. py:method:: get_permission_levels(serving_endpoint_id: str) -> GetServingEndpointPermissionLevelsResponse

        Get serving endpoint permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        
        :returns: :class:`GetServingEndpointPermissionLevelsResponse`
        

    .. py:method:: get_permissions(serving_endpoint_id: str) -> ServingEndpointPermissions

        Get serving endpoint permissions.
        
        Gets the permissions of a serving endpoint. Serving endpoints can inherit permissions from their root
        object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        
        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: list() -> Iterator[ServingEndpoint]

        Get all serving endpoints.
        
        :returns: Iterator over :class:`ServingEndpoint`
        

    .. py:method:: logs(name: str, served_model_name: str) -> ServerLogsResponse

        Get the latest logs for a served model.
        
        Retrieves the service logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that logs will be retrieved for. This field is required.
        
        :returns: :class:`ServerLogsResponse`
        

    .. py:method:: patch(name: str [, add_tags: Optional[List[EndpointTag]], delete_tags: Optional[List[str]]]) -> Iterator[EndpointTag]

        Update tags of a serving endpoint.
        
        Used to batch add and delete tags from a serving endpoint with a single API call.
        
        :param name: str
          The name of the serving endpoint who's tags to patch. This field is required.
        :param add_tags: List[:class:`EndpointTag`] (optional)
          List of endpoint tags to add
        :param delete_tags: List[str] (optional)
          List of tag keys to delete
        
        :returns: Iterator over :class:`EndpointTag`
        

    .. py:method:: put(name: str [, rate_limits: Optional[List[RateLimit]]]) -> PutResponse

        Update rate limits of a serving endpoint.
        
        Used to update the rate limits of a serving endpoint. NOTE: Only foundation model endpoints are
        currently supported. For external models, use AI Gateway to manage rate limits.
        
        :param name: str
          The name of the serving endpoint whose rate limits are being updated. This field is required.
        :param rate_limits: List[:class:`RateLimit`] (optional)
          The list of endpoint rate limits.
        
        :returns: :class:`PutResponse`
        

    .. py:method:: put_ai_gateway(name: str [, guardrails: Optional[AiGatewayGuardrails], inference_table_config: Optional[AiGatewayInferenceTableConfig], rate_limits: Optional[List[AiGatewayRateLimit]], usage_tracking_config: Optional[AiGatewayUsageTrackingConfig]]) -> PutAiGatewayResponse

        Update AI Gateway of a serving endpoint.
        
        Used to update the AI Gateway of a serving endpoint. NOTE: Only external model endpoints are currently
        supported.
        
        :param name: str
          The name of the serving endpoint whose AI Gateway is being updated. This field is required.
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
        

    .. py:method:: query(name: str [, dataframe_records: Optional[List[Any]], dataframe_split: Optional[DataframeSplitInput], extra_params: Optional[Dict[str, str]], input: Optional[Any], inputs: Optional[Any], instances: Optional[List[Any]], max_tokens: Optional[int], messages: Optional[List[ChatMessage]], n: Optional[int], prompt: Optional[Any], stop: Optional[List[str]], stream: Optional[bool], temperature: Optional[float]]) -> QueryEndpointResponse

        Query a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
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
          The messages field used ONLY for __chat external & foundation model__ serving endpoints. This is a
          map of strings and should only be used with other chat query fields.
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
        
        :returns: :class:`QueryEndpointResponse`
        

    .. py:method:: set_permissions(serving_endpoint_id: str [, access_control_list: Optional[List[ServingEndpointAccessControlRequest]]]) -> ServingEndpointPermissions

        Set serving endpoint permissions.
        
        Sets permissions on a serving endpoint. Serving endpoints can inherit permissions from their root
        object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)
        
        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: update_config(name: str [, auto_capture_config: Optional[AutoCaptureConfigInput], served_entities: Optional[List[ServedEntityInput]], served_models: Optional[List[ServedModelInput]], traffic_config: Optional[TrafficConfig]]) -> Wait[ServingEndpointDetailed]

        Update config of a serving endpoint.
        
        Updates any combination of the serving endpoint's served entities, the compute configuration of those
        served entities, and the endpoint's traffic config. An endpoint that already has an update in progress
        can not be updated until the current update completes or fails.
        
        :param name: str
          The name of the serving endpoint to update. This field is required.
        :param auto_capture_config: :class:`AutoCaptureConfigInput` (optional)
          Configuration for Inference Tables which automatically logs requests and responses to Unity Catalog.
        :param served_entities: List[:class:`ServedEntityInput`] (optional)
          A list of served entities for the endpoint to serve. A serving endpoint can have up to 15 served
          entities.
        :param served_models: List[:class:`ServedModelInput`] (optional)
          (Deprecated, use served_entities instead) A list of served models for the endpoint to serve. A
          serving endpoint can have up to 15 served models.
        :param traffic_config: :class:`TrafficConfig` (optional)
          The traffic config defining how invocations to the serving endpoint should be routed.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: update_config_and_wait(name: str [, auto_capture_config: Optional[AutoCaptureConfigInput], served_entities: Optional[List[ServedEntityInput]], served_models: Optional[List[ServedModelInput]], traffic_config: Optional[TrafficConfig], timeout: datetime.timedelta = 0:20:00]) -> ServingEndpointDetailed


    .. py:method:: update_permissions(serving_endpoint_id: str [, access_control_list: Optional[List[ServingEndpointAccessControlRequest]]]) -> ServingEndpointPermissions

        Update serving endpoint permissions.
        
        Updates the permissions on a serving endpoint. Serving endpoints can inherit permissions from their
        root object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)
        
        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: wait_get_serving_endpoint_not_updating(name: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[ServingEndpointDetailed], None]]) -> ServingEndpointDetailed

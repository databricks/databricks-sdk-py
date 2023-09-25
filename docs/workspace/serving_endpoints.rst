Serving endpoints
=================
.. py:class:: ServingEndpointsAPI

    The Serving Endpoints API allows you to create, update, and delete model serving endpoints.
    
    You can use a serving endpoint to serve models from the Databricks Model Registry or from Unity Catalog.
    Endpoints expose the underlying models as scalable REST API endpoints using serverless compute. This means
    the endpoints and associated compute resources are fully managed by Databricks and will not appear in your
    cloud account. A serving endpoint can consist of one or more MLflow models from the Databricks Model
    Registry, called served models. A serving endpoint can have at most ten served models. You can configure
    traffic settings to define how requests should be routed to your served models behind an endpoint.
    Additionally, you can configure the scale of resources that should be applied to each served model.

    .. py:method:: build_logs(name, served_model_name)

        Retrieve the logs associated with building the model's environment for a given serving endpoint's
        served model.
        
        Retrieves the build logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that build logs will be retrieved for. This field is required.
        
        :returns: :class:`BuildLogsResponse`
        

    .. py:method:: create(name, config [, tags])

        Create a new serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param config: :class:`EndpointCoreConfigInput`
          The core config of the serving endpoint.
        :param tags: List[:class:`EndpointTag`] (optional)
          Tags to be attached to the serving endpoint and automatically propagated to billing logs.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: delete(name)

        Delete a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        
        

    .. py:method:: export_metrics(name)

        Retrieve the metrics associated with a serving endpoint.
        
        Retrieves the metrics associated with the provided serving endpoint in either Prometheus or
        OpenMetrics exposition format.
        
        :param name: str
          The name of the serving endpoint to retrieve metrics for. This field is required.
        
        
        

    .. py:method:: get(name)

        Get a single serving endpoint.
        
        Retrieves the details for a single serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`ServingEndpointDetailed`
        

    .. py:method:: get_permission_levels(serving_endpoint_id)

        Get serving endpoint permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        
        :returns: :class:`GetServingEndpointPermissionLevelsResponse`
        

    .. py:method:: get_permissions(serving_endpoint_id)

        Get serving endpoint permissions.
        
        Gets the permissions of a serving endpoint. Serving endpoints can inherit permissions from their root
        object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        
        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: list()

        Retrieve all serving endpoints.
        
        :returns: Iterator over :class:`ServingEndpoint`
        

    .. py:method:: logs(name, served_model_name)

        Retrieve the most recent log lines associated with a given serving endpoint's served model.
        
        Retrieves the service logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that logs will be retrieved for. This field is required.
        
        :returns: :class:`ServerLogsResponse`
        

    .. py:method:: patch(name [, add_tags, delete_tags])

        Patch the tags of a serving endpoint.
        
        Used to batch add and delete tags from a serving endpoint with a single API call.
        
        :param name: str
          The name of the serving endpoint who's tags to patch. This field is required.
        :param add_tags: List[:class:`EndpointTag`] (optional)
          List of endpoint tags to add
        :param delete_tags: List[str] (optional)
          List of tag keys to delete
        
        :returns: Iterator over :class:`EndpointTag`
        

    .. py:method:: query(name)

        Query a serving endpoint with provided model input.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`QueryEndpointResponse`
        

    .. py:method:: set_permissions(serving_endpoint_id [, access_control_list])

        Set serving endpoint permissions.
        
        Sets permissions on a serving endpoint. Serving endpoints can inherit permissions from their root
        object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)
        
        :returns: :class:`ServingEndpointPermissions`
        

    .. py:method:: update_config(served_models, name [, traffic_config])

        Update a serving endpoint with a new config.
        
        Updates any combination of the serving endpoint's served models, the compute configuration of those
        served models, and the endpoint's traffic config. An endpoint that already has an update in progress
        can not be updated until the current update completes or fails.
        
        :param served_models: List[:class:`ServedModelInput`]
          A list of served models for the endpoint to serve. A serving endpoint can have up to 10 served
          models.
        :param name: str
          The name of the serving endpoint to update. This field is required.
        :param traffic_config: :class:`TrafficConfig` (optional)
          The traffic config defining how invocations to the serving endpoint should be routed.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        

    .. py:method:: update_permissions(serving_endpoint_id [, access_control_list])

        Update serving endpoint permissions.
        
        Updates the permissions on a serving endpoint. Serving endpoints can inherit permissions from their
        root object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)
        
        :returns: :class:`ServingEndpointPermissions`
        
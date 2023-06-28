Serving endpoints
=================
.. py:class:: ServingEndpointsAPI

    The Serving Endpoints API allows you to create, update, and delete model serving endpoints.
    
    You can use a serving endpoint to serve models from the Databricks Model Registry. Endpoints expose the
    underlying models as scalable REST API endpoints using serverless compute. This means the endpoints and
    associated compute resources are fully managed by Databricks and will not appear in your cloud account. A
    serving endpoint can consist of one or more MLflow models from the Databricks Model Registry, called
    served models. A serving endpoint can have at most ten served models. You can configure traffic settings
    to define how requests should be routed to your served models behind an endpoint. Additionally, you can
    configure the scale of resources that should be applied to each served model.

    .. py:method:: build_logs(name, served_model_name)

        Retrieve the logs associated with building the model's environment for a given serving endpoint's
        served model.
        
        Retrieves the build logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that build logs will be retrieved for. This field is required.
        
        :returns: :class:`BuildLogsResponse`
        

    .. py:method:: create(name, config)

        Create a new serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param config: :class:`EndpointCoreConfigInput`
          The core config of the serving endpoint.
        
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
        

    .. py:method:: query(name)

        Query a serving endpoint with provided model input.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`QueryEndpointResponse`
        

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
        
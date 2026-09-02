``w.ai_gateway``: AI Gateway
============================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: AiGatewayAPI

    Govern AI workloads in Unity Catalog. This API manages the Unity Catalog securables that bring centralized
    access control, lineage, and auditing to AI-serving entities: model services (governed access to
    foundation models and external LLMs), model provider services (governed connections to external model
    providers), and MCP services (governed Model Context Protocol servers).

    .. py:method:: create_mcp_service(mcp_service: McpService, parent: str, mcp_service_id: str) -> McpService

        Creates an MCP service in a Unity Catalog schema. An MCP (Model Context Protocol) service is a
        governed securable that registers an MCP server and exposes its tools for discovery, access control,
        and invocation. The caller supplies the leaf name in ``mcp_service_id``.

        You must be the owner of the parent schema or have the ``CREATE_SERVICE`` and ``USE_SCHEMA``
        privileges on the parent schema and ``USE_CATALOG`` on the parent catalog. You also need
        ``USE_CONNECTION`` on the connection the MCP service references.

        :param mcp_service: :class:`McpService`
          The MCP service to create. The server populates ``name`` from ``parent`` + ``mcp_service_id``;
          clients should leave it unset. ``source_connection`` is required.
        :param parent: str
          Name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component is
          capped at 255 characters individually.
        :param mcp_service_id: str
          Name for the MCP service, e.g. "my_mcp_service".

        :returns: :class:`McpService`
        

    .. py:method:: create_model_provider_service(model_provider_service: ModelProviderService, parent: str, model_provider_service_id: str) -> ModelProviderService

        Creates a model provider service in a Unity Catalog schema. A model provider service is a governed
        connection to an external model provider (for example OpenAI, Azure OpenAI, or Amazon Bedrock) that
        model services reference to invoke that provider. The caller supplies the leaf name in
        ``model_provider_service_id``.

        You must be the owner of the parent schema or have the ``CREATE_SERVICE`` and ``USE_SCHEMA``
        privileges on the parent schema and ``USE_CATALOG`` on the parent catalog.

        :param model_provider_service: :class:`ModelProviderService`
          The model provider service to create. The server populates ``name`` from ``parent`` +
          ``model_provider_service_id``; clients should leave it unset.
        :param parent: str
          Name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component is
          capped at 255 characters individually.
        :param model_provider_service_id: str
          Name for the model provider service, e.g. "openai_prod".

        :returns: :class:`ModelProviderService`
        

    .. py:method:: create_model_service(model_service: ModelService, parent: str, model_service_id: str) -> ModelService

        Creates a model service in a Unity Catalog schema. A model service is a governed AI Gateway endpoint
        that routes inference requests to one or more model destinations. The caller supplies the leaf name in
        ``model_service_id``.

        You must be the owner of the parent schema or have the ``CREATE_SERVICE`` and ``USE_SCHEMA``
        privileges on the parent schema and ``USE_CATALOG`` on the parent catalog.

        :param model_service: :class:`ModelService`
          The model service to create. The server populates ``name`` from ``parent`` + ``model_service_id``;
          clients should leave it unset.
        :param parent: str
          Name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component is
          capped at 255 characters individually.
        :param model_service_id: str
          Name for the model service, e.g. "my_model_service".

        :returns: :class:`ModelService`
        

    .. py:method:: delete_mcp_service(name: str [, etag: Optional[str]])

        Deletes the MCP service identified by its resource name. Optionally supply an ``etag`` to make the
        delete conditional on the MCP service not having changed since it was read.

        You must be the owner of the MCP service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the parent
        catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the MCP service. Format: ``mcp-services/{catalog}.{schema}.{mcp_service}``. Each
          ``{...}`` component is capped at 255 characters individually.
        :param etag: str (optional)
          Optimistic concurrency token from the most recent read. When set, the delete succeeds only if the
          resource has not changed. Leave unset for an unconditional delete. For REST requests, URL-encode the
          base64 string returned by the API when setting the ``etag`` query parameter.


        

    .. py:method:: delete_model_provider_service(name: str [, etag: Optional[str]])

        Deletes the model provider service identified by its resource name. Optionally supply an ``etag`` to
        make the delete conditional on the model provider service not having changed since it was read.

        You must be the owner of the model provider service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on
        the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model provider service. Format:
          ``model-provider-services/{catalog}.{schema}.{model_provider_service}``. Each ``{...}`` component is
          capped at 255 characters individually.
        :param etag: str (optional)
          Optimistic concurrency token from the most recent read. When set, the delete succeeds only if the
          resource has not changed. Leave unset for an unconditional delete. For REST requests, URL-encode the
          base64 string returned by the API when setting the ``etag`` query parameter.


        

    .. py:method:: delete_model_service(name: str [, etag: Optional[str]])

        Deletes the model service identified by its resource name. Optionally supply an ``etag`` to make the
        delete conditional on the model service not having changed since it was read.

        You must be the owner of the model service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the
        parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model service. Format: ``model-services/{catalog}.{schema}.{model_service}``.
          Each ``{...}`` component is capped at 255 characters individually.
        :param etag: str (optional)
          Optimistic concurrency token from the most recent read. When set, the delete succeeds only if the
          resource has not changed. Leave unset for an unconditional delete. For REST requests, URL-encode the
          base64 string returned by the API when setting the ``etag`` query parameter.


        

    .. py:method:: get_mcp_service(name: str) -> McpService

        Returns the MCP service identified by its resource name.

        You must be the owner of the MCP service or have ``EXECUTE``, ``READ_METADATA``, or ``MANAGE`` on it,
        plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the MCP service. Format: ``mcp-services/{catalog}.{schema}.{mcp_service}``. Each
          ``{...}`` component is capped at 255 characters individually.

        :returns: :class:`McpService`
        

    .. py:method:: get_model_provider_service(name: str) -> ModelProviderService

        Returns the model provider service identified by its resource name.

        You must be the owner of the model provider service or have ``EXECUTE``, ``READ_METADATA``, or
        ``MANAGE`` on it, plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model provider service. Format:
          ``model-provider-services/{catalog}.{schema}.{model_provider_service}``. Each ``{...}`` component is
          capped at 255 characters individually.

        :returns: :class:`ModelProviderService`
        

    .. py:method:: get_model_service(name: str) -> ModelService

        Returns the model service identified by its resource name.

        You must be the owner of the model service or have ``EXECUTE``, ``READ_METADATA``, or ``MANAGE`` on
        it, plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model service. Format: ``model-services/{catalog}.{schema}.{model_service}``.
          Each ``{...}`` component is capped at 255 characters individually.

        :returns: :class:`ModelService`
        

    .. py:method:: list_mcp_services( [, page_size: Optional[int], page_token: Optional[str], parent: Optional[str], view: Optional[ListMcpServicesRequestView]]) -> Iterator[McpService]

        Lists the MCP services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only MCP
        services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or ``MANAGE``) are
        returned.

        :param page_size: int (optional)
          Maximum number of MCP services to return. Defaults to 100 when unset or 0; the maximum is 100. Use
          ``page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Parent schema to list within, in the form ``schemas/{catalog}.{schema}``. Required. Each ``{...}``
          component is capped at 255 characters individually.
        :param view: :class:`ListMcpServicesRequestView` (optional)
          Fields to return for each service. ``FULL`` includes source-connection details and rate-limit
          principal names. ``BASIC`` omits the source connection and omits principal names from rate limits.
          Defaults to ``BASIC`` when unset or ``VIEW_UNSPECIFIED``.

        :returns: Iterator over :class:`McpService`
        

    .. py:method:: list_model_provider_services( [, page_size: Optional[int], page_token: Optional[str], parent: Optional[str], view: Optional[ListModelProviderServicesRequestView]]) -> Iterator[ModelProviderService]

        Lists the model provider services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only model
        provider services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or
        ``MANAGE``) are returned.

        :param page_size: int (optional)
          Maximum number of provider services to return. Defaults to 100 when unset or 0; the maximum is 100.
          Use ``page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Parent schema to list within, in the form ``schemas/{catalog}.{schema}``. Required. Each ``{...}``
          component is capped at 255 characters individually.
        :param view: :class:`ListModelProviderServicesRequestView` (optional)
          Fields to return for each service. ``FULL`` includes inference-table details and rate-limit
          principal names. ``BASIC`` omits inference-table details and omits principal names from rate limits.
          Defaults to ``BASIC`` when unset or ``VIEW_UNSPECIFIED``.

        :returns: Iterator over :class:`ModelProviderService`
        

    .. py:method:: list_model_services( [, page_size: Optional[int], page_token: Optional[str], parent: Optional[str], view: Optional[ListModelServicesRequestView]]) -> Iterator[ModelService]

        Lists the model services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only model
        services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or ``MANAGE``) are
        returned.

        :param page_size: int (optional)
          Maximum number of model services to return. Defaults to 100 when unset or 0; the maximum is 100. Use
          ``page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Parent schema to list within, in the form ``schemas/{catalog}.{schema}``. Required. Each ``{...}``
          component is capped at 255 characters individually.
        :param view: :class:`ListModelServicesRequestView` (optional)
          Fields to return for each service. ``FULL`` includes destinations, inference-table details, and
          rate-limit principal names. ``BASIC`` omits destinations and inference-table details and omits
          principal names from rate limits. Defaults to ``BASIC`` when unset or ``VIEW_UNSPECIFIED``.

        :returns: Iterator over :class:`ModelService`
        

    .. py:method:: update_mcp_service(name: str, mcp_service: McpService, update_mask: FieldMask [, etag: Optional[str]]) -> McpService

        Updates an MCP service. Only the fields named in ``update_mask`` are changed; the resource name is
        immutable. Optionally supply an ``etag`` to make the update conditional on the MCP service not having
        changed since it was read.

        You must be the owner of the MCP service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the parent
        catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the MCP service. Format: ``mcp-services/{catalog}.{schema}.{mcp_service}``. Each
          ``{...}`` component is capped at 255 characters individually. Server-derived on Create from
          ``parent`` + ``mcp_service_id``; required and immutable on Update/Get/Delete.
        :param mcp_service: :class:`McpService`
          The MCP service with the updated field values. ``name`` identifies the resource
          (``mcp-services/{catalog}.{schema}.{mcp_service}``); only fields listed in ``update_mask`` are
          applied.
        :param update_mask: FieldMask
          Fields to update. Use ``config`` to replace the entire configuration. The replacement must include
          every required field; any optional field you omit is cleared. To preserve sibling fields, use one or
          more granular paths: ``comment``, ``config.source_connection.name``,
          ``config.include_tool_selectors``, or ``config.rate_limits``. Wildcard paths such as ``*`` are not
          supported.
        :param etag: str (optional)
          Optimistic concurrency token from the most recent read. When set, the update succeeds only if the
          resource has not changed. Leave unset for an unconditional update. For REST requests, URL-encode the
          base64 string returned by the API when setting the ``etag`` query parameter.

        :returns: :class:`McpService`
        

    .. py:method:: update_model_provider_service(name: str, model_provider_service: ModelProviderService, update_mask: FieldMask [, etag: Optional[str]]) -> ModelProviderService

        Updates a model provider service. Only the fields named in ``update_mask`` are changed; the resource
        name and provider type are immutable. Optionally supply an ``etag`` to make the update conditional on
        the model provider service not having changed since it was read.

        You must be the owner of the model provider service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on
        the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the provider service. Format:
          ``model-provider-services/{catalog}.{schema}.{model_provider_service}``. Each ``{...}`` component is
          capped at 255 characters individually. Server-derived on Create from ``parent`` +
          ``model_provider_service_id``; required and immutable on Update/Get/Delete.
        :param model_provider_service: :class:`ModelProviderService`
          The model provider service with the updated field values. ``name`` identifies the resource
          (``model-provider-services/{catalog}.{schema}.{model_provider_service}``); only fields listed in
          ``update_mask`` are applied.
        :param update_mask: FieldMask
          Fields to update. Use ``config`` to replace the entire configuration. The replacement must include
          every required field; any optional field you omit is cleared. To preserve sibling fields, use one or
          more granular paths: ``comment``, ``config.provider``, ``config.allow_all_targets``,
          ``config.targets``, ``config.forward_headers``, ``config.forward_query_parameters``,
          ``config.forward_unmanaged_paths``, ``config.rate_limits``, or ``config.inference_table``. The
          provider type is immutable, and wildcard paths such as ``*`` are not supported.
        :param etag: str (optional)
          Optimistic concurrency token from the most recent read. When set, the update succeeds only if the
          resource has not changed. Leave unset for an unconditional update. For REST requests, URL-encode the
          base64 string returned by the API when setting the ``etag`` query parameter.

        :returns: :class:`ModelProviderService`
        

    .. py:method:: update_model_service(name: str, model_service: ModelService, update_mask: FieldMask [, etag: Optional[str]]) -> ModelService

        Updates a model service. Only the fields named in ``update_mask`` are changed; the resource name is
        immutable. Optionally supply an ``etag`` to make the update conditional on the model service not
        having changed since it was read.

        You must be the owner of the model service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the
        parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model service. Format: ``model-services/{catalog}.{schema}.{model_service}``.
          Each ``{...}`` component is capped at 255 characters individually. Server-derived on Create from
          ``parent`` + ``model_service_id``; required and immutable on Update/Get/Delete.
        :param model_service: :class:`ModelService`
          The model service with the updated field values. ``name`` identifies the resource
          (``model-services/{catalog}.{schema}.{model_service}``); only fields listed in ``update_mask`` are
          applied.
        :param update_mask: FieldMask
          Fields to update. Use ``config`` to replace the entire configuration. The replacement must include
          every required field; any optional field you omit is cleared. To preserve sibling fields, use one or
          more granular paths: ``comment``, ``config.routing.destinations``,
          ``config.routing.fallback.destinations``, ``config.routing.first_token_timeout``,
          ``config.rate_limits``, or ``config.inference_table``. Intermediate paths such as ``config.routing``
          and ``config.routing.fallback``, and wildcard paths such as ``*``, are not supported.
        :param etag: str (optional)
          Optimistic concurrency token from the most recent read. When set, the update succeeds only if the
          resource has not changed. Leave unset for an unconditional update. For REST requests, URL-encode the
          base64 string returned by the API when setting the ``etag`` query parameter.

        :returns: :class:`ModelService`
        
``w.ai_gateway``: AI Gateway
============================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: AiGatewayAPI

    Govern AI workloads in Unity Catalog. This API manages the Unity Catalog securables that bring centralized
    access control, lineage, and auditing to AI-serving entities: model services (governed access to
    foundation models and external LLMs), model provider services (governed connections to external model
    providers), MCP services (governed Model Context Protocol servers), and agent services (governed agents).

    .. py:method:: create_agent_service(agent_service: AgentService, parent: str, agent_service_id: str) -> AgentService

        Creates an agent service in a Unity Catalog schema. An agent service is a governed securable that
        registers an AI agent and exposes it for discovery, access control, and auditing. The caller supplies
        the leaf name in ``agent_service_id`` and the agent service type, which is immutable after creation.

        You must be the owner of the parent schema or have the ``CREATE_SERVICE`` and ``USE_SCHEMA``
        privileges on the parent schema and ``USE_CATALOG`` on the parent catalog.

        :param agent_service: :class:`AgentService`
          The agent service to create. The server populates ``name`` from ``parent`` + ``agent_service_id``;
          clients should leave it unset.
        :param parent: str
          Resource name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component
          is capped at 255 characters individually.
        :param agent_service_id: str
          Leaf identifier for the agent service (the unqualified name within the parent schema, e.g.
          "support_agent").

        :returns: :class:`AgentService`
        

    .. py:method:: create_mcp_service(mcp_service: McpService, parent: str, mcp_service_id: str) -> McpService

        Creates an MCP service in a Unity Catalog schema. An MCP (Model Context Protocol) service is a
        governed securable that registers an MCP server and exposes its tools for discovery, access control,
        and invocation. The caller supplies the leaf name in ``mcp_service_id``.

        You must be the owner of the parent schema or have the ``CREATE_SERVICE`` and ``USE_SCHEMA``
        privileges on the parent schema and ``USE_CATALOG`` on the parent catalog. You also need
        ``USE_CONNECTION`` on the connection the MCP service references.

        :param mcp_service: :class:`McpService`
          The MCP service to create. The server populates ``name`` from ``parent`` + ``mcp_service_id``;
          clients should leave it unset.
        :param parent: str
          Resource name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component
          is capped at 255 characters individually.
        :param mcp_service_id: str
          Leaf identifier for the MCP service (the unqualified name within the parent schema, e.g.
          "my_mcp_service").

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
          Resource name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component
          is capped at 255 characters individually.
        :param model_provider_service_id: str
          Leaf identifier for the provider service (the unqualified name within the parent schema, e.g.
          "openai_prod").

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
          Resource name of the parent schema. Format: ``schemas/{catalog}.{schema}``. Each ``{...}`` component
          is capped at 255 characters individually.
        :param model_service_id: str
          Leaf identifier for the model service (the unqualified name within the parent schema, e.g.
          "my_model_service").

        :returns: :class:`ModelService`
        

    .. py:method:: delete_agent_service(name: str [, etag: Optional[str]])

        Deletes the agent service identified by its resource name. Optionally supply an ``etag`` to make the
        delete conditional on the agent service not having changed since it was read.

        You must be the owner of the agent service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the
        parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the agent service. Format: ``agent-services/{catalog}.{schema}.{agent_service}``.
          Each ``{...}`` component is capped at 255 characters individually.
        :param etag: str (optional)
          If-match precondition: when set, the delete proceeds only if the current server-side etag matches.
          Empty means unconditional delete.


        

    .. py:method:: delete_mcp_service(name: str [, etag: Optional[str]])

        Deletes the MCP service identified by its resource name. Optionally supply an ``etag`` to make the
        delete conditional on the MCP service not having changed since it was read.

        You must be the owner of the MCP service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the parent
        catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the MCP service. Format: ``mcp-services/{catalog}.{schema}.{mcp_service}``. Each
          ``{...}`` component is capped at 255 characters individually.
        :param etag: str (optional)
          If-match precondition: when set, the delete proceeds only if the current server-side etag matches.
          Empty means unconditional delete.


        

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
          If-match precondition: when set, the delete proceeds only if the current server-side etag matches.
          Empty means unconditional delete.


        

    .. py:method:: delete_model_service(name: str [, etag: Optional[str]])

        Deletes the model service identified by its resource name. Optionally supply an ``etag`` to make the
        delete conditional on the model service not having changed since it was read.

        You must be the owner of the model service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the
        parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model service. Format: ``model-services/{catalog}.{schema}.{model_service}``.
          Each ``{...}`` component is capped at 255 characters individually.
        :param etag: str (optional)
          If-match precondition: when set, the delete proceeds only if the current server-side etag matches.
          Empty means unconditional delete.


        

    .. py:method:: get_agent_service(name: str [, include_browse: Optional[bool]]) -> AgentService

        Returns the agent service identified by its resource name.

        You must be the owner of the agent service or have ``EXECUTE``, ``READ_METADATA``, or ``MANAGE`` on
        it, plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the agent service. Format: ``agent-services/{catalog}.{schema}.{agent_service}``.
          Each ``{...}`` component is capped at 255 characters individually.
        :param include_browse: bool (optional)
          Whether to include agent services for which the principal can only access selective metadata.

        :returns: :class:`AgentService`
        

    .. py:method:: get_mcp_service(name: str [, include_browse: Optional[bool]]) -> McpService

        Returns the MCP service identified by its resource name.

        You must be the owner of the MCP service or have ``EXECUTE``, ``READ_METADATA``, or ``MANAGE`` on it,
        plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the MCP service. Format: ``mcp-services/{catalog}.{schema}.{mcp_service}``. Each
          ``{...}`` component is capped at 255 characters individually.
        :param include_browse: bool (optional)
          Whether to include MCP services for which the principal can only access selective metadata.

        :returns: :class:`McpService`
        

    .. py:method:: get_model_provider_service(name: str [, include_browse: Optional[bool]]) -> ModelProviderService

        Returns the model provider service identified by its resource name.

        You must be the owner of the model provider service or have ``EXECUTE``, ``READ_METADATA``, or
        ``MANAGE`` on it, plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model provider service. Format:
          ``model-provider-services/{catalog}.{schema}.{model_provider_service}``. Each ``{...}`` component is
          capped at 255 characters individually.
        :param include_browse: bool (optional)
          Whether to include provider services for which the principal can only access selective metadata.

        :returns: :class:`ModelProviderService`
        

    .. py:method:: get_model_service(name: str [, include_browse: Optional[bool]]) -> ModelService

        Returns the model service identified by its resource name.

        You must be the owner of the model service or have ``EXECUTE``, ``READ_METADATA``, or ``MANAGE`` on
        it, plus ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the model service. Format: ``model-services/{catalog}.{schema}.{model_service}``.
          Each ``{...}`` component is capped at 255 characters individually.
        :param include_browse: bool (optional)
          Whether to include model services for which the principal can only access selective metadata.

        :returns: :class:`ModelService`
        

    .. py:method:: list_agent_services( [, include_browse: Optional[bool], page_size: Optional[int], page_token: Optional[str], parent: Optional[str]]) -> Iterator[AgentService]

        Lists the agent services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only agent
        services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or ``MANAGE``) are
        returned.

        :param include_browse: bool (optional)
          Whether to include agent services for which the principal can only access selective metadata.
        :param page_size: int (optional)
          Maximum number of agent services to return. Defaults to 100 when unset or 0; the maximum is 1000.
          Use ``next_page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Resource name of the parent schema to list within, as ``schemas/{catalog}.{schema}``. Each ``{...}``
          component is capped at 255 characters individually.

        :returns: Iterator over :class:`AgentService`
        

    .. py:method:: list_mcp_services( [, include_browse: Optional[bool], page_size: Optional[int], page_token: Optional[str], parent: Optional[str], view: Optional[ListMcpServicesRequestView]]) -> Iterator[McpService]

        Lists the MCP services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only MCP
        services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or ``MANAGE``) are
        returned.

        :param include_browse: bool (optional)
          Whether to include MCP services for which the principal can only access selective metadata.
        :param page_size: int (optional)
          Maximum number of MCP services to return. Defaults to 100 when unset or 0; the maximum is 1000. Use
          ``next_page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Resource name of the parent schema to list within, as ``schemas/{catalog}.{schema}``. Each ``{...}``
          component is capped at 255 characters individually.
        :param view: :class:`ListMcpServicesRequestView` (optional)
          View selector controlling which fields are populated per row.

        :returns: Iterator over :class:`McpService`
        

    .. py:method:: list_model_provider_services( [, include_browse: Optional[bool], page_size: Optional[int], page_token: Optional[str], parent: Optional[str], view: Optional[ListModelProviderServicesRequestView]]) -> Iterator[ModelProviderService]

        Lists the model provider services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only model
        provider services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or
        ``MANAGE``) are returned.

        :param include_browse: bool (optional)
          Whether to include provider services for which the principal can only access selective metadata.
        :param page_size: int (optional)
          Maximum number of provider services to return. Defaults to 100 when unset or 0; the maximum is 1000.
          Use ``next_page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Resource name of the parent schema to list within, as ``schemas/{catalog}.{schema}``. Each ``{...}``
          component is capped at 255 characters individually.
        :param view: :class:`ListModelProviderServicesRequestView` (optional)
          View selector controlling which fields are populated per row.

        :returns: Iterator over :class:`ModelProviderService`
        

    .. py:method:: list_model_services( [, include_browse: Optional[bool], page_size: Optional[int], page_token: Optional[str], parent: Optional[str], view: Optional[ListModelServicesRequestView]]) -> Iterator[ModelService]

        Lists the model services in a Unity Catalog schema. Provide ``parent`` as
        ``schemas/{catalog}.{schema}``. Results are paginated; pass the returned ``next_page_token`` to fetch
        subsequent pages.

        Requires ``USE_CATALOG`` on the parent catalog and ``USE_SCHEMA`` on the parent schema. Only model
        services the caller can access (as owner or through ``EXECUTE``, ``READ_METADATA``, or ``MANAGE``) are
        returned.

        :param include_browse: bool (optional)
          Whether to include model services for which the principal can only access selective metadata.
        :param page_size: int (optional)
          Maximum number of model services to return. Defaults to 100 when unset or 0; the maximum is 1000.
          Use ``next_page_token`` to retrieve additional pages.
        :param page_token: str (optional)
          Opaque pagination token from a previous request.
        :param parent: str (optional)
          Resource name of the parent schema to list within, as ``schemas/{catalog}.{schema}``. Each ``{...}``
          component is capped at 255 characters individually.
        :param view: :class:`ListModelServicesRequestView` (optional)
          View selector controlling which fields are populated per row.

        :returns: Iterator over :class:`ModelService`
        

    .. py:method:: update_agent_service(name: str, agent_service: AgentService, update_mask: FieldMask [, etag: Optional[str]]) -> AgentService

        Updates an agent service. Only the fields named in ``update_mask`` are changed; the resource name and
        agent service type are immutable. Optionally supply an ``etag`` to make the update conditional on the
        agent service not having changed since it was read.

        You must be the owner of the agent service or have ``MANAGE`` on it, plus ``USE_CATALOG`` on the
        parent catalog and ``USE_SCHEMA`` on the parent schema.

        :param name: str
          Resource name of the agent service. Format: ``agent-services/{catalog}.{schema}.{agent_service}``.
          Each ``{...}`` component is capped at 255 characters individually. Server-derived on Create from
          ``parent`` + ``agent_service_id``; required and immutable on Update/Get/Delete.
        :param agent_service: :class:`AgentService`
          The agent service with the updated field values. ``name`` identifies the resource
          (``agent-services/{catalog}.{schema}.{agent_service}``); only fields listed in ``update_mask`` are
          applied.
        :param update_mask: FieldMask
          The list of fields to update. The framework validates each path against the ``agent_service`` field
          above. Wildcard paths (``paths: ["*"]``) are not supported; list each field path explicitly.
        :param etag: str (optional)
          If-match precondition: when set, the update proceeds only if the current server-side etag matches.
          Empty means an unconditional update.

        :returns: :class:`AgentService`
        

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
          The list of fields to update. The framework validates each path against the ``mcp_service`` field
          above. Wildcard paths (``paths: ["*"]``) are not supported; list each field path explicitly.
        :param etag: str (optional)
          If-match precondition: when set, the update proceeds only if the current server-side etag matches.
          Empty means an unconditional update.

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
          The list of fields to update. The framework validates each path against the
          ``model_provider_service`` field above. Wildcard paths (``paths: ["*"]``) are not supported; list
          each field path explicitly.
        :param etag: str (optional)
          If-match precondition: when set, the update proceeds only if the current server-side etag matches.
          Empty means an unconditional update.

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
          The list of fields to update. The framework validates each path against the ``model_service`` field
          above. Wildcard paths (``paths: ["*"]``) are not supported; list each field path explicitly.
        :param etag: str (optional)
          If-match precondition: when set, the update proceeds only if the current server-side etag matches.
          Empty means an unconditional update.

        :returns: :class:`ModelService`
        
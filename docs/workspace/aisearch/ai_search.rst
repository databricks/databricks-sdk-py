``w.ai_search``: AISearch
=========================
.. currentmodule:: databricks.sdk.service.aisearch

.. py:class:: AiSearchAPI

    **AI Search Endpoint**: Represents the compute resources to host AI Search indexes. AIP-conformant
    replacement for the legacy VectorSearchEndpoints API; functionally equivalent.

    .. py:method:: create_endpoint(parent: str, endpoint: Endpoint [, endpoint_id: Optional[str]]) -> Endpoint

        Create a new AI Search endpoint.

        :param parent: str
          The Workspace where this Endpoint will be created. Format: ``workspaces/{workspace_id}``
        :param endpoint: :class:`Endpoint`
          The Endpoint resource to create. Fields other than ``endpoint.name`` carry the desired
          configuration; ``endpoint.name`` is server-assigned from ``parent`` and ``endpoint_id``.
        :param endpoint_id: str (optional)
          Short name of the endpoint, which becomes the last segment of ``name``. The server rejects a request
          without it. The name can have at most 50 characters, can contain only lowercase letters, digits,
          hyphens, periods, and underscores, and must start and end with a letter or digit.

        :returns: :class:`Endpoint`
        

    .. py:method:: create_index(parent: str, index: Index [, index_id: Optional[str]]) -> Index

        Create a new AI Search index. The index is provisioned asynchronously; ``status.ready`` on GetIndex
        reports when it can serve queries.

        :param parent: str
          The Endpoint where this Index will be created. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``
        :param index: :class:`Index`
          The Index resource to create. Fields other than ``index.name`` carry the desired configuration;
          ``index.name`` is server-assigned from ``parent`` and ``index_id``.
        :param index_id: str (optional)
          Three-level Unity Catalog table name for the new index, in the form ``catalog.schema.name``. The
          server composes the full ``Index.name`` as ``{parent}/indexes/{index_id}`` and rejects an empty
          value.

        :returns: :class:`Index`
        

    .. py:method:: delete_endpoint(name: str)

        Delete an AI Search endpoint.

        :param name: str
          Full resource name of the endpoint to delete. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``


        

    .. py:method:: delete_index(name: str)

        Delete an AI Search index.

        :param name: str
          Full resource name of the index to delete. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``


        

    .. py:method:: get_endpoint(name: str) -> Endpoint

        Get details for a single AI Search endpoint.

        :param name: str
          Full resource name of the endpoint. Format: ``workspaces/{workspace_id}/endpoints/{endpoint_id}``

        :returns: :class:`Endpoint`
        

    .. py:method:: get_index(name: str) -> Index

        Get details for a single AI Search index.

        :param name: str
          Full resource name of the index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``

        :returns: :class:`Index`
        

    .. py:method:: list_endpoints(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Endpoint]

        List AI Search endpoints in a workspace.

        :param parent: str
          The Workspace that owns this collection of endpoints. Format: ``workspaces/{workspace_id}``
        :param page_size: int (optional)
          Maximum number of endpoints to return in one page. The server applies its own page size limit, so a
          page can hold fewer endpoints than ``page_size`` even when more remain.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Endpoint`
        

    .. py:method:: list_indexes(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Index]

        List AI Search indexes on an endpoint.

        :param parent: str
          The Endpoint that owns this collection of indexes. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``
        :param page_size: int (optional)
          Maximum number of indexes to return. When unset, every index on the endpoint is returned.
        :param page_token: str (optional)
          Page token from a previous response. If not provided, returns the first page.

        :returns: Iterator over :class:`Index`
        

    .. py:method:: query_index(name: str, columns: List[str] [, columns_to_rerank: Optional[List[str]], facets: Optional[List[str]], filters_json: Optional[str], max_results: Optional[int], query_columns: Optional[List[str]], query_text: Optional[str], query_type: Optional[str], query_vector: Optional[List[float]], reranker: Optional[RerankerConfig], score_threshold: Optional[float], sort_columns: Optional[List[str]]]) -> QueryIndexResponse

        Query (search) an AI Search index. Read-only, so a read-scoped token may invoke it.

        :param name: str
          Full resource name of the index to query. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param columns: List[str]
          Columns to include in each result row. Only columns that are part of the index can be returned.
        :param columns_to_rerank: List[str] (optional)
          Columns whose values are sent to the reranker.
        :param facets: List[str] (optional)
          Facets to compute over the matched results (e.g. ``"category TOP 5"``).
        :param filters_json: str (optional)
          JSON object of filters to apply, serialized as a string. Each key is a column name with an optional
          operator suffix such as ``<``, ``>=``, ``NOT``, or ``OR``, and each value is the value to compare
          against. Only columns that are part of the index can be filtered. See
          https://docs.databricks.com/aws/en/ai-search/query-ai-search#filters for the supported operators.
        :param max_results: int (optional)
          Maximum number of results to return. Defaults to 10. It corresponds to ``num_results`` in the Vector
          Search API.
        :param query_columns: List[str] (optional)
          Text columns to search for ``query_text``. When empty, all text columns are searched.
        :param query_text: str (optional)
          Query text. Required for Delta Sync indexes that compute embeddings from a model endpoint, and for
          ``HYBRID`` and ``FULL_TEXT`` queries.
        :param query_type: str (optional)
          Query type: ``ANN`` for vector similarity search, ``HYBRID`` for combined vector and keyword search,
          or ``FULL_TEXT`` for keyword search without embeddings. Defaults to ``ANN``.
        :param query_vector: List[float] (optional)
          Query vector. Required for Direct Access indexes and Delta Sync indexes with self-managed vectors.
        :param reranker: :class:`RerankerConfig` (optional)
          If set, results are reranked before being returned. See
          https://docs.databricks.com/aws/en/ai-search/query-ai-search#rerank for details.
        :param score_threshold: float (optional)
          Score threshold for the approximate nearest-neighbor search; results that score below it are not
          returned. Defaults to 0.0.
        :param sort_columns: List[str] (optional)
          Sort clauses, e.g. ``["rating DESC", "price ASC"]``. Overrides relevance ordering.

        :returns: :class:`QueryIndexResponse`
        

    .. py:method:: remove_data(name: str, primary_keys: List[str]) -> RemoveDataResponse

        Remove rows by primary key from a Direct Access AI Search index.

        :param name: str
          Full resource name of the index. Must be a Direct Access index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param primary_keys: List[str]
          Primary keys of the rows to remove.

        :returns: :class:`RemoveDataResponse`
        

    .. py:method:: scan_index(name: str [, page_size: Optional[int], page_token: Optional[str]]) -> ScanIndexResponse

        Scan (paginate over) the rows of an AI Search index.

        :param name: str
          Full resource name of the index to scan. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param page_size: int (optional)
          Maximum number of rows to return in this page. Defaults to 10.
        :param page_token: str (optional)
          Page token from a previous response; if unset, scanning starts from the beginning.

        :returns: :class:`ScanIndexResponse`
        

    .. py:method:: sync_index(name: str) -> SyncIndexResponse

        Start a sync of a Delta Sync AI Search index with its source Delta table. Use it with ``TRIGGERED``
        pipelines; ``CONTINUOUS`` pipelines sync automatically. Direct Access indexes are written through
        UpsertData instead.

        :param name: str
          Full resource name of the index to synchronize. Must be a Delta Sync index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``

        :returns: :class:`SyncIndexResponse`
        

    .. py:method:: update_endpoint(name: str, endpoint: Endpoint, update_mask: FieldMask) -> Endpoint

        Update an existing AI Search endpoint. Only the fields named in ``update_mask`` change. The server
        applies a mask that spans several settings, such as ``budget_policy_id`` and ``custom_tags``, one
        setting at a time, so if a later setting fails, the earlier ones may already have been applied.

        :param name: str
          Full resource name of the endpoint, in the form
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}``. On create, the server composes it from
          ``parent`` and ``endpoint_id`` and ignores any value supplied in the request body.
        :param endpoint: :class:`Endpoint`
          The Endpoint resource to update. ``endpoint.name`` carries the full resource path.
        :param update_mask: FieldMask
          Comma-separated list of ``Endpoint`` fields to update. The updatable fields are
          ``budget_policy_id``, ``usage_policy_id``, ``custom_tags``, ``replica_count``, and ``target_qps``.
          The server rejects nested paths and unknown fields.

        :returns: :class:`Endpoint`
        

    .. py:method:: upsert_data(name: str, inputs_json: str) -> UpsertDataResponse

        Upsert rows into a Direct Access AI Search index.

        :param name: str
          Full resource name of the index. Must be a Direct Access index. Format:
          ``workspaces/{workspace_id}/endpoints/{endpoint_id}/indexes/{index_id}``
        :param inputs_json: str
          JSON array of the rows to insert or update, serialized as a string. Each element is an object that
          maps column names to values and must include the primary key column; vector columns are given as
          arrays of numbers. A row whose primary key already exists is overwritten. The array must not be
          empty.

        :returns: :class:`UpsertDataResponse`
        
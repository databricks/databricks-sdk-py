``w.vector_search_indexes``: Indexes
====================================
.. currentmodule:: databricks.sdk.service.vectorsearch

.. py:class:: VectorSearchIndexesAPI

    **Index**: An efficient representation of your embedding vectors that supports real-time and efficient
    approximate nearest neighbor (ANN) search queries.

    There are 2 types of AI Search indexes:

    - **Delta Sync Index**: An index that automatically syncs with a source Delta Table, automatically and
      incrementally updating the index as the underlying data in the Delta Table changes.
    - **Direct Vector Access Index**: An index that supports direct read and write of vectors and metadata
      through our REST and SDK APIs. With this model, the user manages index updates.

    .. py:method:: create_index(name: str, endpoint_name: str, primary_key: str, index_type: VectorIndexType [, delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecRequest], direct_access_index_spec: Optional[DirectAccessVectorIndexSpec], index_subtype: Optional[IndexSubtype]]) -> VectorIndex

        Create a new index on an endpoint. Creating a Delta Sync index also creates the pipeline that
        populates it from the source table; a Direct Vector Access index starts empty and is populated through
        Upsert data into an index.

        :param name: str
          Three-level Unity Catalog name of the index to create.
        :param endpoint_name: str
          Name of the endpoint to be used for serving the index
        :param primary_key: str
          Name of the column that uniquely identifies each row. For a Delta Sync index it is a column of the
          source table; for a Direct Vector Access index it must be declared in ``schema_json``. It cannot be
          the embedding source or embedding vector column.
        :param index_type: :class:`VectorIndexType`
          Type of index to create, which determines which spec field is required.
        :param delta_sync_index_spec: :class:`DeltaSyncVectorIndexSpecRequest` (optional)
          Specification for Delta Sync Index. Required if ``index_type`` is ``DELTA_SYNC``.
        :param direct_access_index_spec: :class:`DirectAccessVectorIndexSpec` (optional)
          Specification for Direct Vector Access Index. Required if ``index_type`` is ``DIRECT_ACCESS``.
        :param index_subtype: :class:`IndexSubtype` (optional)
          The subtype of the index. Use ``HYBRID`` or ``FULL_TEXT``. ``VECTOR`` is not supported.

        :returns: :class:`VectorIndex`
        

    .. py:method:: delete_data_vector_index(index_name: str, primary_keys: List[str]) -> DeleteDataVectorIndexResponse

        Delete rows from a Direct Vector Access index by primary key. The response reports how many rows were
        deleted and the primary keys of the rows that failed.

        :param index_name: str
          Name of the vector index where data is to be deleted. Must be a Direct Vector Access Index.
        :param primary_keys: List[str]
          Primary keys of the rows to delete. At least one key is required.

        :returns: :class:`DeleteDataVectorIndexResponse`
        

    .. py:method:: delete_index(index_name: str)

        Delete an index and the data it holds. The source table of a Delta Sync index is not affected.

        :param index_name: str
          Three-level Unity Catalog name of the index.


        

    .. py:method:: get_index(index_name: str [, ensure_reranker_compatible: Optional[bool]]) -> VectorIndex

        Get an index.

        :param index_name: str
          Three-level Unity Catalog name of the index.
        :param ensure_reranker_compatible: bool (optional)
          If true, the URL returned for the index is guaranteed to be compatible with the reranker. Currently
          this means we return the CP URL regardless of how the index is being accessed. If not set or set to
          false, the URL may still be compatible with the reranker depending on what URL we return.

        :returns: :class:`VectorIndex`
        

    .. py:method:: list_indexes(endpoint_name: str [, page_token: Optional[str]]) -> Iterator[MiniVectorIndex]

        List all indexes in the given endpoint.

        :param endpoint_name: str
          Name of the endpoint whose indexes to list.
        :param page_token: str (optional)
          Page token returned by a previous call, used to get the next page of results.

        :returns: Iterator over :class:`MiniVectorIndex`
        

    .. py:method:: query_index(index_name: str, columns: List[str] [, columns_to_rerank: Optional[List[str]], facets: Optional[List[str]], filters_json: Optional[str], num_results: Optional[int], query_columns: Optional[List[str]], query_text: Optional[str], query_type: Optional[str], query_vector: Optional[List[float]], reranker: Optional[RerankerConfig], score_threshold: Optional[float], sort_columns: Optional[List[str]]]) -> QueryVectorIndexResponse

        Query an index with a vector, text, or both, and return the requested columns of the best-matching
        rows.

        :param index_name: str
          Name of the vector index to query.
        :param columns: List[str]
          Names of the columns to return for each result. At least one column is required, and only columns
          that are part of the index can be returned.
        :param columns_to_rerank: List[str] (optional)
          Column names used to retrieve data to send to the reranker.
        :param facets: List[str] (optional)
          Facets to compute over the matched results. Each entry has one of these forms: ``"<column>"`` - top
          10 distinct values by count ``"<column> TOP <n>"`` - top n distinct values, where n > 0 ``"<column>
          BUCKETS [[from,to],...]"`` - inclusive numeric ranges ``TOP`` and ``BUCKETS`` are case-insensitive.
          A column may appear at most once.
        :param filters_json: str (optional)
          Filters to apply to the results, as a JSON object serialized to a string. Each key is a column name,
          optionally followed by a space and an operator, and each value is the value or list of values to
          compare the column against. A key without an operator matches the value exactly, or any of the
          listed values. Supported operators are ``NOT``, ``<``, ``<=``, ``>``, ``>=``, ``OR`` and ``LIKE``;
          see https://docs.databricks.com/aws/en/ai-search/query-ai-search for their semantics. This field is
          not supported on storage-optimized endpoints.
        :param num_results: int (optional)
          Maximum number of results to return. It must be greater than 0 and defaults to 10. By default, a
          ``HYBRID`` query can return at most 200 results.
        :param query_columns: List[str] (optional)
          Text columns to search for ``query_text``. When empty, all text columns are searched.
        :param query_text: str (optional)
          Text to search for. Use it for an index with Databricks-managed embeddings, which embeds the text
          with the index's embedding model endpoint, and for ``FULL_TEXT`` queries on any index. A ``HYBRID``
          query on an index with managed embeddings requires only ``query_text``.
        :param query_type: str (optional)
          The query type to use. Choices are ``ANN`` and ``HYBRID`` and ``FULL_TEXT``. Defaults to ``ANN``.
        :param query_vector: List[float] (optional)
          Embedding vector to search for. Use it for an index whose embeddings you compute yourself: a Direct
          Vector Access index or a Delta Sync index with ``embedding_vector_columns``. A ``HYBRID`` query on a
          Delta Sync index with ``embedding_vector_columns``, or on a Direct Vector Access index without
          ``embedding_source_columns``, requires both ``query_vector`` and ``query_text``. A Direct Vector
          Access index with ``embedding_source_columns`` can be queried with ``query_text`` alone.
        :param reranker: :class:`RerankerConfig` (optional)
          If set, the top 50 results are reranked with the Databricks Reranker model before returning the
          ``num_results`` results to the user. The setting ``columns_to_rerank`` selects which columns are
          used for reranking. For each datapoint, the columns selected are concatenated before being sent to
          the reranking model. See https://docs.databricks.com/aws/en/vector-search/query-vector-search#rerank
          for more information.
        :param score_threshold: float (optional)
          Threshold for the approximate nearest neighbor search. Defaults to 0.0.
        :param sort_columns: List[str] (optional)
          Sort results by column values instead of the default relevance ordering. Each clause has the form
          ``"<column> ASC"`` or ``"<column> DESC"``, for example ``["rating DESC", "price ASC"]``.

        :returns: :class:`QueryVectorIndexResponse`
        

    .. py:method:: query_next_page(index_name: str [, endpoint_name: Optional[str], page_token: Optional[str]]) -> QueryVectorIndexResponse

        Use ``next_page_token`` returned from previous ``QueryVectorIndex`` or ``QueryVectorIndexNextPage``
        request to fetch next page of results.

        :param index_name: str
          Name of the vector index to query.
        :param endpoint_name: str (optional)
          Name of the endpoint that serves the index.
        :param page_token: str (optional)
          Page token returned from previous ``QueryVectorIndex`` or ``QueryVectorIndexNextPage`` API.

        :returns: :class:`QueryVectorIndexResponse`
        

    .. py:method:: scan_index(index_name: str [, last_primary_key: Optional[str], num_results: Optional[int]]) -> ScanVectorIndexResponse

        Scan an index and return the first ``num_results`` rows after the exclusive ``last_primary_key``.
        Repeat the call with the returned ``last_primary_key`` to read the whole index.

        :param index_name: str
          Name of the vector index to scan.
        :param last_primary_key: str (optional)
          Primary key of the last entry returned in the previous scan.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.

        :returns: :class:`ScanVectorIndexResponse`
        

    .. py:method:: sync_index(index_name: str)

        Start a sync of a Delta Sync index with a ``TRIGGERED`` pipeline from its source table. An index with
        a ``CONTINUOUS`` pipeline syncs automatically and rejects manual syncs.

        :param index_name: str
          Name of the vector index to synchronize. Must be a Delta Sync Index.


        

    .. py:method:: upsert_data_vector_index(index_name: str, inputs_json: str) -> UpsertDataVectorIndexResponse

        Insert rows into a Direct Vector Access index, replacing existing rows that have the same primary key.
        The response reports how many rows succeeded and the primary keys of the rows that failed.

        :param index_name: str
          Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index.
        :param inputs_json: str
          Rows to upsert, as a JSON array of objects serialized to a string. Each object maps column names
          from ``schema_json`` to values and must include the primary key. A row whose primary key already
          exists in the index is replaced.

        :returns: :class:`UpsertDataVectorIndexResponse`
        
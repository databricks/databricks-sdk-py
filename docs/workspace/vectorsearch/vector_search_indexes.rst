``w.vector_search_indexes``: Indexes
====================================
.. currentmodule:: databricks.sdk.service.vectorsearch

.. py:class:: VectorSearchIndexesAPI

    **Index**: An efficient representation of your embedding vectors that supports real-time and efficient
    approximate nearest neighbor (ANN) search queries.
    
    There are 2 types of Vector Search indexes: * **Delta Sync Index**: An index that automatically syncs with
    a source Delta Table, automatically and incrementally updating the index as the underlying data in the
    Delta Table changes. * **Direct Vector Access Index**: An index that supports direct read and write of
    vectors and metadata through our REST and SDK APIs. With this model, the user manages index updates.

    .. py:method:: create_index(name: str, endpoint_name: str, primary_key: str, index_type: VectorIndexType [, delta_sync_index_spec: Optional[DeltaSyncVectorIndexSpecRequest], direct_access_index_spec: Optional[DirectAccessVectorIndexSpec]]) -> CreateVectorIndexResponse

        Create an index.
        
        Create a new index.
        
        :param name: str
          Name of the index
        :param endpoint_name: str
          Name of the endpoint to be used for serving the index
        :param primary_key: str
          Primary key of the index
        :param index_type: :class:`VectorIndexType`
          There are 2 types of Vector Search indexes:
          
          - `DELTA_SYNC`: An index that automatically syncs with a source Delta Table, automatically and
          incrementally updating the index as the underlying data in the Delta Table changes. -
          `DIRECT_ACCESS`: An index that supports direct read and write of vectors and metadata through our
          REST and SDK APIs. With this model, the user manages index updates.
        :param delta_sync_index_spec: :class:`DeltaSyncVectorIndexSpecRequest` (optional)
          Specification for Delta Sync Index. Required if `index_type` is `DELTA_SYNC`.
        :param direct_access_index_spec: :class:`DirectAccessVectorIndexSpec` (optional)
          Specification for Direct Vector Access Index. Required if `index_type` is `DIRECT_ACCESS`.
        
        :returns: :class:`CreateVectorIndexResponse`
        

    .. py:method:: delete_data_vector_index(index_name: str, primary_keys: List[str]) -> DeleteDataVectorIndexResponse

        Delete data from index.
        
        Handles the deletion of data from a specified vector index.
        
        :param index_name: str
          Name of the vector index where data is to be deleted. Must be a Direct Vector Access Index.
        :param primary_keys: List[str]
          List of primary keys for the data to be deleted.
        
        :returns: :class:`DeleteDataVectorIndexResponse`
        

    .. py:method:: delete_index(index_name: str)

        Delete an index.
        
        Delete an index.
        
        :param index_name: str
          Name of the index
        
        
        

    .. py:method:: get_index(index_name: str) -> VectorIndex

        Get an index.
        
        Get an index.
        
        :param index_name: str
          Name of the index
        
        :returns: :class:`VectorIndex`
        

    .. py:method:: list_indexes(endpoint_name: str [, page_token: Optional[str]]) -> Iterator[MiniVectorIndex]

        List indexes.
        
        List all indexes in the given endpoint.
        
        :param endpoint_name: str
          Name of the endpoint
        :param page_token: str (optional)
          Token for pagination
        
        :returns: Iterator over :class:`MiniVectorIndex`
        

    .. py:method:: query_index(index_name: str, columns: List[str] [, filters_json: Optional[str], num_results: Optional[int], query_text: Optional[str], query_type: Optional[str], query_vector: Optional[List[float]], score_threshold: Optional[float]]) -> QueryVectorIndexResponse

        Query an index.
        
        Query the specified vector index.
        
        :param index_name: str
          Name of the vector index to query.
        :param columns: List[str]
          List of column names to include in the response.
        :param filters_json: str (optional)
          JSON string representing query filters.
          
          Example filters: - `{"id <": 5}`: Filter for id less than 5. - `{"id >": 5}`: Filter for id greater
          than 5. - `{"id <=": 5}`: Filter for id less than equal to 5. - `{"id >=": 5}`: Filter for id
          greater than equal to 5. - `{"id": 5}`: Filter for id equal to 5.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.
        :param query_text: str (optional)
          Query text. Required for Delta Sync Index using model endpoint.
        :param query_type: str (optional)
          The query type to use. Choices are `ANN` and `HYBRID`. Defaults to `ANN`.
        :param query_vector: List[float] (optional)
          Query vector. Required for Direct Vector Access Index and Delta Sync Index using self-managed
          vectors.
        :param score_threshold: float (optional)
          Threshold for the approximate nearest neighbor search. Defaults to 0.0.
        
        :returns: :class:`QueryVectorIndexResponse`
        

    .. py:method:: query_next_page(index_name: str [, endpoint_name: Optional[str], page_token: Optional[str]]) -> QueryVectorIndexResponse

        Query next page.
        
        Use `next_page_token` returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` request
        to fetch next page of results.
        
        :param index_name: str
          Name of the vector index to query.
        :param endpoint_name: str (optional)
          Name of the endpoint.
        :param page_token: str (optional)
          Page token returned from previous `QueryVectorIndex` or `QueryVectorIndexNextPage` API.
        
        :returns: :class:`QueryVectorIndexResponse`
        

    .. py:method:: scan_index(index_name: str [, last_primary_key: Optional[str], num_results: Optional[int]]) -> ScanVectorIndexResponse

        Scan an index.
        
        Scan the specified vector index and return the first `num_results` entries after the exclusive
        `primary_key`.
        
        :param index_name: str
          Name of the vector index to scan.
        :param last_primary_key: str (optional)
          Primary key of the last entry returned in the previous scan.
        :param num_results: int (optional)
          Number of results to return. Defaults to 10.
        
        :returns: :class:`ScanVectorIndexResponse`
        

    .. py:method:: sync_index(index_name: str)

        Synchronize an index.
        
        Triggers a synchronization process for a specified vector index.
        
        :param index_name: str
          Name of the vector index to synchronize. Must be a Delta Sync Index.
        
        
        

    .. py:method:: upsert_data_vector_index(index_name: str, inputs_json: str) -> UpsertDataVectorIndexResponse

        Upsert data into an index.
        
        Handles the upserting of data into a specified vector index.
        
        :param index_name: str
          Name of the vector index where data is to be upserted. Must be a Direct Vector Access Index.
        :param inputs_json: str
          JSON string representing the data to be upserted.
        
        :returns: :class:`UpsertDataVectorIndexResponse`
        
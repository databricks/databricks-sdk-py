``w.queries``: Queries / Results
================================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: QueriesAPI

    These endpoints are used for CRUD operations on query definitions. Query definitions include the target
    SQL warehouse, query text, name, description, tags, parameters, and visualizations. Queries can be
    scheduled using the `sql_task` type of the Jobs API, e.g. :method:jobs/create.

    .. py:method:: create( [, data_source_id: Optional[str], description: Optional[str], name: Optional[str], options: Optional[Any], parent: Optional[str], query: Optional[str], run_as_role: Optional[RunAsRole], tags: Optional[List[str]]]) -> Query


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(name=f'sdk-{time.time_ns()}',
                                     data_source_id=srcs[0].id,
                                     description="test query from Go SDK",
                                     query="SHOW TABLES")
            
            # cleanup
            w.queries.delete(query_id=query.id)

        Create a new query definition.
        
        Creates a new query definition. Queries created with this endpoint belong to the authenticated user
        making the request.
        
        The `data_source_id` field specifies the ID of the SQL warehouse to run this query against. You can
        use the Data Sources API to see a complete list of available SQL warehouses. Or you can copy the
        `data_source_id` from an existing query.
        
        **Note**: You cannot add a visualization until you create the query.
        
        :param data_source_id: str (optional)
          Data source ID maps to the ID of the data source used by the resource and is distinct from the
          warehouse ID. [Learn more].
          
          [Learn more]: https://docs.databricks.com/api/workspace/datasources/list
        :param description: str (optional)
          General description that conveys additional information about this query such as usage notes.
        :param name: str (optional)
          The title of this query that appears in list views, widget headings, and on the query page.
        :param options: Any (optional)
          Exclusively used for storing a list parameter definitions. A parameter is an object with `title`,
          `name`, `type`, and `value` properties. The `value` field here is the default value. It can be
          overridden at runtime.
        :param parent: str (optional)
          The identifier of the workspace folder containing the object.
        :param query: str (optional)
          The text of the query to be run.
        :param run_as_role: :class:`RunAsRole` (optional)
          Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as
          viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
        :param tags: List[str] (optional)
        
        :returns: :class:`Query`
        

    .. py:method:: delete(query_id: str)

        Delete a query.
        
        Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and
        they cannot be used for alerts. The trash is deleted after 30 days.
        
        :param query_id: str
        
        
        

    .. py:method:: get(query_id: str) -> Query


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(name=f'sdk-{time.time_ns()}',
                                     data_source_id=srcs[0].id,
                                     description="test query from Go SDK",
                                     query="SHOW TABLES")
            
            by_id = w.queries.get(query_id=query.id)
            
            # cleanup
            w.queries.delete(query_id=query.id)

        Get a query definition.
        
        Retrieve a query object definition along with contextual permissions information about the currently
        authenticated user.
        
        :param query_id: str
        
        :returns: :class:`Query`
        

    .. py:method:: list( [, order: Optional[str], page: Optional[int], page_size: Optional[int], q: Optional[str]]) -> Iterator[Query]

        Get a list of queries.
        
        Gets a list of queries. Optionally, this list can be filtered by a search term.
        
        ### **Warning: Calling this API concurrently 10 or more times could result in throttling, service
        degradation, or a temporary ban.**
        
        :param order: str (optional)
          Name of query attribute to order by. Default sort order is ascending. Append a dash (`-`) to order
          descending instead.
          
          - `name`: The name of the query.
          
          - `created_at`: The timestamp the query was created.
          
          - `runtime`: The time it took to run this query. This is blank for parameterized queries. A blank
          value is treated as the highest value for sorting.
          
          - `executed_at`: The timestamp when the query was last run.
          
          - `created_by`: The user name of the user that created the query.
        :param page: int (optional)
          Page number to retrieve.
        :param page_size: int (optional)
          Number of queries to return per page.
        :param q: str (optional)
          Full text search term
        
        :returns: Iterator over :class:`Query`
        

    .. py:method:: restore(query_id: str)

        Restore a query.
        
        Restore a query that has been moved to the trash. A restored query appears in list views and searches.
        You can use restored queries for alerts.
        
        :param query_id: str
        
        
        

    .. py:method:: update(query_id: str [, data_source_id: Optional[str], description: Optional[str], name: Optional[str], options: Optional[Any], query: Optional[str], run_as_role: Optional[RunAsRole], tags: Optional[List[str]]]) -> Query


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(name=f'sdk-{time.time_ns()}',
                                     data_source_id=srcs[0].id,
                                     description="test query from Go SDK",
                                     query="SHOW TABLES")
            
            updated = w.queries.update(query_id=query.id,
                                       name=f'sdk-{time.time_ns()}',
                                       data_source_id=srcs[0].id,
                                       description="UPDATED: test query from Go SDK",
                                       query="SELECT 2+2")
            
            # cleanup
            w.queries.delete(query_id=query.id)

        Change a query definition.
        
        Modify this query definition.
        
        **Note**: You cannot undo this operation.
        
        :param query_id: str
        :param data_source_id: str (optional)
          Data source ID maps to the ID of the data source used by the resource and is distinct from the
          warehouse ID. [Learn more].
          
          [Learn more]: https://docs.databricks.com/api/workspace/datasources/list
        :param description: str (optional)
          General description that conveys additional information about this query such as usage notes.
        :param name: str (optional)
          The title of this query that appears in list views, widget headings, and on the query page.
        :param options: Any (optional)
          Exclusively used for storing a list parameter definitions. A parameter is an object with `title`,
          `name`, `type`, and `value` properties. The `value` field here is the default value. It can be
          overridden at runtime.
        :param query: str (optional)
          The text of the query to be run.
        :param run_as_role: :class:`RunAsRole` (optional)
          Sets the **Run as** role for the object. Must be set to one of `"viewer"` (signifying "run as
          viewer" behavior) or `"owner"` (signifying "run as owner" behavior)
        :param tags: List[str] (optional)
        
        :returns: :class:`Query`
        
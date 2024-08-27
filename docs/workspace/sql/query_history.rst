``w.query_history``: Query History
==================================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: QueryHistoryAPI

    A service responsible for storing and retrieving the list of queries run against SQL endpoints and
    serverless compute.

    .. py:method:: list( [, filter_by: Optional[QueryFilter], include_metrics: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> ListQueriesResponse


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            _ = w.query_history.list(filter_by=sql.QueryFilter(
                query_start_time_range=sql.TimeRange(start_time_ms=1690243200000, end_time_ms=1690329600000)))

        List Queries.
        
        List the history of queries through SQL warehouses, and serverless compute.
        
        You can filter by user ID, warehouse ID, status, and time range. Most recently started queries are
        returned first (up to max_results in request). The pagination token returned in response can be used
        to list subsequent query statuses.
        
        :param filter_by: :class:`QueryFilter` (optional)
          A filter to limit query history results. This field is optional.
        :param include_metrics: bool (optional)
          Whether to include the query metrics with each query. Only use this for a small subset of queries
          (max_results). Defaults to false.
        :param max_results: int (optional)
          Limit the number of results returned in one page. Must be less than 1000 and the default is 100.
        :param page_token: str (optional)
          A token that can be used to get the next page of results. The token can contains characters that
          need to be encoded before using it in a URL. For example, the character '+' needs to be replaced by
          %2B. This field is optional.
        
        :returns: :class:`ListQueriesResponse`
        
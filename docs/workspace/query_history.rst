Query History
=============
.. py:class:: QueryHistoryAPI

    Access the history of queries through SQL warehouses.

    .. py:method:: list( [, filter_by, include_metrics, max_results, page_token])

        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            _ = w.query_history.list(filter_by=sql.QueryFilter(
                query_start_time_range=sql.TimeRange(start_time_ms=1690243200000, end_time_ms=1690329600000)))

        List Queries.
        
        List the history of queries through SQL warehouses.
        
        You can filter by user ID, warehouse ID, status, and time range.
        
        :param filter_by: :class:`QueryFilter` (optional)
          A filter to limit query history results. This field is optional.
        :param include_metrics: bool (optional)
          Whether to include metrics about query.
        :param max_results: int (optional)
          Limit the number of results returned in one page. The default is 100.
        :param page_token: str (optional)
          A token that can be used to get the next page of results.
        
        :returns: Iterator over :class:`QueryInfo`
        
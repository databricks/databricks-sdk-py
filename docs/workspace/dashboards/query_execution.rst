``w.query_execution``: Query Execution
======================================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: QueryExecutionAPI

    Query execution APIs for AI / BI Dashboards

    .. py:method:: cancel_published_query_execution(dashboard_name: str, dashboard_revision_id: str [, tokens: Optional[List[str]]]) -> CancelQueryExecutionResponse

        Cancel the results for the a query for a published, embedded dashboard.
        
        :param dashboard_name: str
        :param dashboard_revision_id: str
        :param tokens: List[str] (optional)
          Example: EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ
        
        :returns: :class:`CancelQueryExecutionResponse`
        

    .. py:method:: execute_published_dashboard_query(dashboard_name: str, dashboard_revision_id: str [, override_warehouse_id: Optional[str]])

        Execute a query for a published dashboard.
        
        :param dashboard_name: str
          Dashboard name and revision_id is required to retrieve PublishedDatasetDataModel which contains the
          list of datasets, warehouse_id, and embedded_credentials
        :param dashboard_revision_id: str
        :param override_warehouse_id: str (optional)
          A dashboard schedule can override the warehouse used as compute for processing the published
          dashboard queries
        
        
        

    .. py:method:: poll_published_query_status(dashboard_name: str, dashboard_revision_id: str [, tokens: Optional[List[str]]]) -> PollQueryStatusResponse

        Poll the results for the a query for a published, embedded dashboard.
        
        :param dashboard_name: str
        :param dashboard_revision_id: str
        :param tokens: List[str] (optional)
          Example: EC0A..ChAB7WCEn_4Qo4vkLqEbXsxxEgh3Y2pbWw45WhoQXgZSQo9aS5q2ZvFcbvbx9CgA-PAEAQ
        
        :returns: :class:`PollQueryStatusResponse`
        
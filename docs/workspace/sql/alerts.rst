``w.alerts``: Alerts
====================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: AlertsAPI

    The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks SQL object that
    periodically runs a query, evaluates a condition of its result, and notifies one or more users and/or
    notification destinations if the condition was met. Alerts can be scheduled using the `sql_task` type of
    the Jobs API, e.g. :method:jobs/create.
    
    **Note**: A new version of the Databricks SQL API will soon be available. [Learn more]
    
    [Learn more]: https://docs.databricks.com/en/whats-coming.html#updates-to-the-databricks-sql-api-for-managing-queries-alerts-and-data-sources

    .. py:method:: create(name: str, options: AlertOptions, query_id: str [, parent: Optional[str], rearm: Optional[int]]) -> Alert


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(name=f'sdk-{time.time_ns()}',
                                     data_source_id=srcs[0].id,
                                     description="test query from Go SDK",
                                     query="SELECT 1")
            
            alert = w.alerts.create(options=sql.AlertOptions(column="1", op="==", value="1"),
                                    name=f'sdk-{time.time_ns()}',
                                    query_id=query.id)
            
            # cleanup
            w.queries.delete(query_id=query.id)
            w.alerts.delete(alert_id=alert.id)

        Create an alert.
        
        Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a
        condition of its result, and notifies users or notification destinations if the condition was met.
        
        **Note**: A new version of the Databricks SQL API will soon be available. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/whats-coming.html#updates-to-the-databricks-sql-api-for-managing-queries-alerts-and-data-sources
        
        :param name: str
          Name of the alert.
        :param options: :class:`AlertOptions`
          Alert configuration options.
        :param query_id: str
          Query ID.
        :param parent: str (optional)
          The identifier of the workspace folder containing the object.
        :param rearm: int (optional)
          Number of seconds after being triggered before the alert rearms itself and can be triggered again.
          If `null`, alert will never be triggered again.
        
        :returns: :class:`Alert`
        

    .. py:method:: delete(alert_id: str)

        Delete an alert.
        
        Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note**: Unlike
        queries and dashboards, alerts cannot be moved to the trash.
        
        **Note**: A new version of the Databricks SQL API will soon be available. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/whats-coming.html#updates-to-the-databricks-sql-api-for-managing-queries-alerts-and-data-sources
        
        :param alert_id: str
        
        
        

    .. py:method:: get(alert_id: str) -> Alert


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(name=f'sdk-{time.time_ns()}',
                                     data_source_id=srcs[0].id,
                                     description="test query from Go SDK",
                                     query="SELECT 1")
            
            alert = w.alerts.create(options=sql.AlertOptions(column="1", op="==", value="1"),
                                    name=f'sdk-{time.time_ns()}',
                                    query_id=query.id)
            
            by_id = w.alerts.get(alert_id=alert.id)
            
            # cleanup
            w.queries.delete(query_id=query.id)
            w.alerts.delete(alert_id=alert.id)

        Get an alert.
        
        Gets an alert.
        
        **Note**: A new version of the Databricks SQL API will soon be available. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/whats-coming.html#updates-to-the-databricks-sql-api-for-managing-queries-alerts-and-data-sources
        
        :param alert_id: str
        
        :returns: :class:`Alert`
        

    .. py:method:: list() -> Iterator[Alert]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.alerts.list()

        Get alerts.
        
        Gets a list of alerts.
        
        **Note**: A new version of the Databricks SQL API will soon be available. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/whats-coming.html#updates-to-the-databricks-sql-api-for-managing-queries-alerts-and-data-sources
        
        :returns: Iterator over :class:`Alert`
        

    .. py:method:: update(alert_id: str, name: str, options: AlertOptions, query_id: str [, rearm: Optional[int]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(name=f'sdk-{time.time_ns()}',
                                     data_source_id=srcs[0].id,
                                     description="test query from Go SDK",
                                     query="SELECT 1")
            
            alert = w.alerts.create(options=sql.AlertOptions(column="1", op="==", value="1"),
                                    name=f'sdk-{time.time_ns()}',
                                    query_id=query.id)
            
            w.alerts.update(options=sql.AlertOptions(column="1", op="==", value="1"),
                            alert_id=alert.id,
                            name=f'sdk-{time.time_ns()}',
                            query_id=query.id)
            
            # cleanup
            w.queries.delete(query_id=query.id)
            w.alerts.delete(alert_id=alert.id)

        Update an alert.
        
        Updates an alert.
        
        **Note**: A new version of the Databricks SQL API will soon be available. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/whats-coming.html#updates-to-the-databricks-sql-api-for-managing-queries-alerts-and-data-sources
        
        :param alert_id: str
        :param name: str
          Name of the alert.
        :param options: :class:`AlertOptions`
          Alert configuration options.
        :param query_id: str
          Query ID.
        :param rearm: int (optional)
          Number of seconds after being triggered before the alert rearms itself and can be triggered again.
          If `null`, alert will never be triggered again.
        
        
        
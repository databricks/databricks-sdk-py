``w.alerts_legacy``: Alerts (legacy)
====================================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: AlertsLegacyAPI

    The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks SQL object that
    periodically runs a query, evaluates a condition of its result, and notifies one or more users and/or
    notification destinations if the condition was met. Alerts can be scheduled using the `sql_task` type of
    the Jobs API, e.g. :method:jobs/create.
    
    **Note**: A new version of the Databricks SQL API is now available. Please see the latest version. [Learn
    more]
    
    [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html

    .. py:method:: create(name: str, options: AlertOptions, query_id: str [, parent: Optional[str], rearm: Optional[int]]) -> LegacyAlert

        Create an alert.
        
        Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a
        condition of its result, and notifies users or notification destinations if the condition was met.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use :method:alerts/create
        instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
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
        
        :returns: :class:`LegacyAlert`
        

    .. py:method:: delete(alert_id: str)

        Delete an alert.
        
        Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note**: Unlike
        queries and dashboards, alerts cannot be moved to the trash.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use :method:alerts/delete
        instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
        :param alert_id: str
        
        
        

    .. py:method:: get(alert_id: str) -> LegacyAlert

        Get an alert.
        
        Gets an alert.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use :method:alerts/get
        instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
        :param alert_id: str
        
        :returns: :class:`LegacyAlert`
        

    .. py:method:: list() -> Iterator[LegacyAlert]

        Get alerts.
        
        Gets a list of alerts.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use :method:alerts/list
        instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
        :returns: Iterator over :class:`LegacyAlert`
        

    .. py:method:: update(alert_id: str, name: str, options: AlertOptions, query_id: str [, rearm: Optional[int]])

        Update an alert.
        
        Updates an alert.
        
        **Note**: A new version of the Databricks SQL API is now available. Please use :method:alerts/update
        instead. [Learn more]
        
        [Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html
        
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
        
        
        
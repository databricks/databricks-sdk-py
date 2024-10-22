``w.alerts``: Alerts
====================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: AlertsAPI

    The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks SQL object that
    periodically runs a query, evaluates a condition of its result, and notifies one or more users and/or
    notification destinations if the condition was met. Alerts can be scheduled using the `sql_task` type of
    the Jobs API, e.g. :method:jobs/create.

    .. py:method:: create(name: str, options: AlertOptions, query_id: str [, parent: Optional[str], rearm: Optional[int]]) -> Alert


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(query=sql.CreateQueryRequestQuery(display_name=f'sdk-{time.time_ns()}',
                                                                       warehouse_id=srcs[0].warehouse_id,
                                                                       description="test query from Go SDK",
                                                                       query_text="SELECT 1"))
            
            alert = w.alerts.create(
                alert=sql.CreateAlertRequestAlert(condition=sql.AlertCondition(operand=sql.AlertConditionOperand(
                    column=sql.AlertOperandColumn(name="1")),
                                                                               op=sql.AlertOperator.EQUAL,
                                                                               threshold=sql.AlertConditionThreshold(
                                                                                   value=sql.AlertOperandValue(
                                                                                       double_value=1))),
                                                  display_name=f'sdk-{time.time_ns()}',
                                                  query_id=query.id))
            
            # cleanup
            w.queries.delete(id=query.id)
            w.alerts.delete(id=alert.id)

        Create an alert.
        
        Creates an alert. An alert is a Databricks SQL object that periodically runs a query, evaluates a
        condition of its result, and notifies users or notification destinations if the condition was met.
        
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
        
        Deletes an alert. Deleted alerts are no longer accessible and cannot be restored. **Note:** Unlike
        queries and dashboards, alerts cannot be moved to the trash.
        
        :param alert_id: str
        
        
        

    .. py:method:: get(alert_id: str) -> Alert


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(query=sql.CreateQueryRequestQuery(display_name=f'sdk-{time.time_ns()}',
                                                                       warehouse_id=srcs[0].warehouse_id,
                                                                       description="test query from Go SDK",
                                                                       query_text="SELECT 1"))
            
            alert = w.alerts.create(
                alert=sql.CreateAlertRequestAlert(condition=sql.AlertCondition(operand=sql.AlertConditionOperand(
                    column=sql.AlertOperandColumn(name="1")),
                                                                               op=sql.AlertOperator.EQUAL,
                                                                               threshold=sql.AlertConditionThreshold(
                                                                                   value=sql.AlertOperandValue(
                                                                                       double_value=1))),
                                                  display_name=f'sdk-{time.time_ns()}',
                                                  query_id=query.id))
            
            by_id = w.alerts.get(id=alert.id)
            
            # cleanup
            w.queries.delete(id=query.id)
            w.alerts.delete(id=alert.id)

        Get an alert.
        
        Gets an alert.
        
        :param alert_id: str
        
        :returns: :class:`Alert`
        

    .. py:method:: list() -> Iterator[Alert]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            all = w.alerts.list(sql.ListAlertsRequest())

        Get alerts.
        
        Gets a list of alerts.
        
        :returns: Iterator over :class:`Alert`
        

    .. py:method:: update(alert_id: str, name: str, options: AlertOptions, query_id: str [, rearm: Optional[int]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(query=sql.CreateQueryRequestQuery(display_name=f'sdk-{time.time_ns()}',
                                                                       warehouse_id=srcs[0].warehouse_id,
                                                                       description="test query from Go SDK",
                                                                       query_text="SELECT 1"))
            
            alert = w.alerts.create(
                alert=sql.CreateAlertRequestAlert(condition=sql.AlertCondition(operand=sql.AlertConditionOperand(
                    column=sql.AlertOperandColumn(name="1")),
                                                                               op=sql.AlertOperator.EQUAL,
                                                                               threshold=sql.AlertConditionThreshold(
                                                                                   value=sql.AlertOperandValue(
                                                                                       double_value=1))),
                                                  display_name=f'sdk-{time.time_ns()}',
                                                  query_id=query.id))
            
            _ = w.alerts.update(id=alert.id,
                                alert=sql.UpdateAlertRequestAlert(display_name=f'sdk-{time.time_ns()}'),
                                update_mask="display_name")
            
            # cleanup
            w.queries.delete(id=query.id)
            w.alerts.delete(id=alert.id)

        Update an alert.
        
        Updates an alert.
        
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
        
        
        
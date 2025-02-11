``w.alerts``: Alerts
====================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: AlertsAPI

    The alerts API can be used to perform CRUD operations on alerts. An alert is a Databricks SQL object that
periodically runs a query, evaluates a condition of its result, and notifies one or more users and/or
notification destinations if the condition was met. Alerts can be scheduled using the `sql_task` type of
the Jobs API, e.g. :method:jobs/create.

    .. py:method:: create( [, alert: Optional[CreateAlertRequestAlert]]) -> Alert


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

Creates an alert.

:param alert: :class:`CreateAlertRequestAlert` (optional)

:returns: :class:`Alert`


    .. py:method:: delete(id: str)

        Delete an alert.

Moves an alert to the trash. Trashed alerts immediately disappear from searches and list views, and
can no longer trigger. You can restore a trashed alert through the UI. A trashed alert is permanently
deleted after 30 days.

:param id: str




    .. py:method:: get(id: str) -> Alert


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

:param id: str

:returns: :class:`Alert`


    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ListAlertsResponseAlert]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            all = w.alerts.list(sql.ListAlertsRequest())

        List alerts.

Gets a list of alerts accessible to the user, ordered by creation time. **Warning:** Calling this API
concurrently 10 or more times could result in throttling, service degradation, or a temporary ban.

:param page_size: int (optional)
:param page_token: str (optional)

:returns: Iterator over :class:`ListAlertsResponseAlert`


    .. py:method:: update(id: str, update_mask: str [, alert: Optional[UpdateAlertRequestAlert]]) -> Alert


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

:param id: str
:param update_mask: str
  The field mask must be a single string, with multiple fields separated by commas (no spaces). The
  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
  the entire collection field can be specified. Field names must exactly match the resource field
  names.
  
  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
  changes in the future.
:param alert: :class:`UpdateAlertRequestAlert` (optional)

:returns: :class:`Alert`

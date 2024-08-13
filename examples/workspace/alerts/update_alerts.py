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

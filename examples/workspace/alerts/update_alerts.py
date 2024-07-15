import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

query = w.queries.create(
    query=sql.CreateQueryRequestQuery(
        display_name=f'sdk-{time.time_ns()}',
        description="This is a test query created from the SDK",
        query_text="SELECT 1"
    )
)

alert = w.alerts.create(
    alert=sql.CreateAlertRequestAlert(
        display_name=f'sdk-{time.time_ns()}',
        query_id=query.id,
        condition=sql.AlertCondition(
            op=sql.AlertOperator.LESS_THAN,
            operand=sql.AlertConditionOperand(column=sql.AlertOperandColumn(name="1")),
            threshold=sql.AlertConditionThreshold(
                value=sql.AlertOperandValue(double_value=1.5)
            ),
        ),
    )
)

w.alerts.update(
    id=alert.id,
    alert=sql.UpdateAlertRequestAlert(
        condition=sql.AlertCondition(
            op=sql.AlertOperator.GREATER_THAN,
            operand=sql.AlertConditionOperand(column=sql.AlertOperandColumn(name="1")),
            threshold=sql.AlertConditionThreshold(
                value=sql.AlertOperandValue(double_value=99)
            ),
        ),
    ),
    update_mask="condition",
)

# cleanup
w.queries.delete(id=query.id)
w.alerts.delete(id=alert.id)

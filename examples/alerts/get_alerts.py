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

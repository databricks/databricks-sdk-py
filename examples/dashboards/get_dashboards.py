from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.dashboards.create(name=f'sdk-{time.time_ns()}')

by_id = w.dashboards.get(dashboard_id=created.id)

# cleanup
w.dashboards.delete(dashboard_id=created.id)

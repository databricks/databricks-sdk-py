from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.dashboards.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.dashboards.delete(dashboard_id=created.id)

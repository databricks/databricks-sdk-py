import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.dashboards.create(name=f'sdk-{time.time_ns()}')

by_id = w.dashboards.get(dashboard_id=created.id)

# cleanup
w.dashboards.delete(dashboard_id=created.id)

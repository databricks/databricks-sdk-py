import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.dashboards.create(name=f'sdk-{time.time_ns()}', dashboard_filters_enabled=False, is_draft=True)

by_id = w.dashboards.get(get=created.id)

# cleanup
w.dashboards.delete(delete=created.id)

import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

group = w.groups.create(display_name=f'sdk-{time.time_ns()}')

fetch = w.groups.get(get=group.id)

# cleanup
w.groups.delete(delete=group.id)

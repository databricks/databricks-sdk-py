import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

group = w.groups.create(display_name=f'sdk-{time.time_ns()}')

w.groups.delete(id=group.id)

# cleanup
w.groups.delete(id=group.id)

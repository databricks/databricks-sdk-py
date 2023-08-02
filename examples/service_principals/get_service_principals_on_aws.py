import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.service_principals.create(display_name=f'sdk-{time.time_ns()}')

by_id = w.service_principals.get(id=created.id)

# cleanup
w.service_principals.delete(id=created.id)

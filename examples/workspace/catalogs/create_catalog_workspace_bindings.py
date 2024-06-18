import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.catalogs.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.catalogs.delete(name=created.name, force=True)

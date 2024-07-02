import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.catalogs.delete(name=created_catalog.name, force=True)

import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.catalogs.delete(name=new_catalog.name, force=True)

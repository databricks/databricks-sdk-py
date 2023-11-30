import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.catalogs.create(name=f'sdk-{time.time_ns()}')

_ = w.catalogs.update(name=created.name, comment="updated")

# cleanup
w.catalogs.delete(name=created.name, force=True)

import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=new_catalog.name)

_ = w.schemas.get(full_name=created.full_name)

# cleanup
w.catalogs.delete(name=new_catalog.name, force=True)
w.schemas.delete(full_name=created.full_name)

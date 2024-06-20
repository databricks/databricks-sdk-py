import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=new_catalog.name)

_ = w.schemas.update(full_name=created.full_name, comment=f'sdk-{time.time_ns()}')

# cleanup
w.catalogs.delete(name=new_catalog.name, force=True)
w.schemas.delete(full_name=created.full_name)

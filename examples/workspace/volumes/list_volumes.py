import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)

all_volumes = w.volumes.list(catalog_name=created_catalog.name, schema_name=created_schema.name)

# cleanup
w.schemas.delete(full_name=created_schema.full_name)
w.catalogs.delete(name=created_catalog.name, force=True)

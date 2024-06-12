import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)

summaries = w.tables.list_summaries(catalog_name=created_catalog.name,
                                    schema_name_pattern=created_schema.name)

# cleanup
w.schemas.delete(full_name=created_schema.full_name)
w.catalogs.delete(name=created_catalog.name, force=True)

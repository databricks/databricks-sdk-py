from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

all = w.schemas.list(catalog_name=new_catalog.name)

# cleanup
w.catalogs.delete(name=new_catalog.name, force=True)

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.catalogs.delete(name=created_catalog.name, force=True)

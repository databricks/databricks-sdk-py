from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.catalogs.create(name=f'sdk-{time.time_ns()}')

_ = w.catalogs.get(name=created.name)

# cleanup
w.catalogs.delete(name=created.name, force=True)

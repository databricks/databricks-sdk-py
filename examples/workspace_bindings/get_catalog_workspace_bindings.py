from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.catalogs.create(name=f'sdk-{time.time_ns()}')

bindings = w.workspace_bindings.get(name=created.name)

# cleanup
w.catalogs.delete(name=created.name, force=True)

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

this_workspace_id = os.environ["THIS_WORKSPACE_ID"]

created = w.catalogs.create(name=f'sdk-{time.time_ns()}')

_ = w.workspace_bindings.update(name=created.name, assign_workspaces=[this_workspace_id])

# cleanup
w.catalogs.delete(name=created.name, force=True)

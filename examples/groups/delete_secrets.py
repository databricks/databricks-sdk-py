from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

group = w.groups.create(display_name=f'sdk-{time.time_ns()}')

w.groups.delete(id=group.id)

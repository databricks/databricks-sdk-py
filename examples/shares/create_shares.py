from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created_share = w.shares.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.shares.delete(name=created_share.name)

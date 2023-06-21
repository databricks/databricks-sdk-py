import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created_share = w.shares.create(name=f'sdk-{time.time_ns()}')

# cleanup
w.shares.delete(delete=created_share.name)

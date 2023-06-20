import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.recipients.create(name=f'sdk-{time.time_ns()}')

share_permissions = w.recipients.share_permissions(share_permissions=created.name)

# cleanup
w.recipients.delete(delete=created.name)

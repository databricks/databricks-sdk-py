from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.recipients.create(name=f'sdk-{time.time_ns()}')

_ = w.recipients.get(name=created.name)

# cleanup
w.recipients.delete(name=created.name)

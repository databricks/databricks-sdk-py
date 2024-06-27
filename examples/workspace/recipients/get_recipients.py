import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.recipients.create(name=f'sdk-{time.time_ns()}')

_ = w.recipients.get(name=created.name)

# cleanup
w.recipients.delete(name=created.name)

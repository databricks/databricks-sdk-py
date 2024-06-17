import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')

# cleanup
w.users.delete(id=other_owner.id)

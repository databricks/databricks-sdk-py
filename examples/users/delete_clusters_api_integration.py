import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')

w.users.delete(delete=other_owner.id)

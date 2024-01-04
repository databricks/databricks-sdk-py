from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')

w.users.delete(id=other_owner.id)

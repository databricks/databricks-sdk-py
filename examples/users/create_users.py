import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

user = w.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')

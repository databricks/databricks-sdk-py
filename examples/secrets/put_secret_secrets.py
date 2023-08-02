import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

key_name = f'sdk-{time.time_ns()}'

scope_name = f'sdk-{time.time_ns()}'

w.secrets.create_scope(scope=scope_name)

w.secrets.put_secret(scope=scope_name, key=key_name, string_value=f'sdk-{time.time_ns()}')

# cleanup
w.secrets.delete_secret(scope=scope_name, key=key_name)
w.secrets.delete_scope(scope=scope_name)

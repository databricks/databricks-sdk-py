import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

key_name = f'sdk-{time.time_ns()}'

scope_name = f'sdk-{time.time_ns()}'

w.secrets.create_scope(scope=scope_name)

acls = w.secrets.list_acls(scope=scope_name)

# cleanup
w.secrets.delete_secret(scope=scope_name, key=key_name)
w.secrets.delete_scope(scope=scope_name)

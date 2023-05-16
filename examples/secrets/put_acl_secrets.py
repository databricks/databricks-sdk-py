import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace

w = WorkspaceClient()

key_name = f'sdk-{time.time_ns()}'

group = w.groups.create(display_name=f'sdk-{time.time_ns()}')

scope_name = f'sdk-{time.time_ns()}'

w.secrets.create_scope(scope=scope_name)

w.secrets.put_acl(scope=scope_name, permission=workspace.acl_permission_manage, principal=group.display_name)

# cleanup
w.groups.delete(delete=group.id)
w.secrets.delete_secret(scope=scope_name, key=key_name)
w.secrets.delete_scope(delete_scope=scope_name)

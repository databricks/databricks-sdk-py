import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

group = w.groups.create(display_name=f'sdk-{time.time_ns()}')

obj = w.workspace.get_status(path=notebook_path)

_ = w.permissions.set(request_object_type="notebooks",
                      request_object_id="%d" % (obj.object_id),
                      access_control_list=[
                          iam.AccessControlRequest(group_name=group.display_name,
                                                   permission_level=iam.PermissionLevel.CAN_RUN)
                      ])

# cleanup
w.groups.delete(id=group.id)

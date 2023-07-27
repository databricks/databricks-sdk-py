import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

obj = w.workspace.get_status(path=notebook_path)

levels = w.permissions.get_permission_levels(request_object_type="notebooks",
                                             request_object_id="%d" % (obj.object_id))

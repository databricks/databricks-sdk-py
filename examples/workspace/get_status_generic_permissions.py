import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

obj = w.workspace.get_status(path=notebook_path)

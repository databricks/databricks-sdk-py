import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

get_status_response = w.workspace.get_status(path=notebook)

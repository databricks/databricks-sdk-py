import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

export_response = w.workspace.export(direct_download=False, format="SOURCE", path=notebook)

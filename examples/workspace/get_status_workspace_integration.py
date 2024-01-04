from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

get_status_response = w.workspace.get_status(path=notebook)

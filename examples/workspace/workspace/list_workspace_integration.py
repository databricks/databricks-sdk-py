import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

objects = w.workspace.list(path=os.path.dirname(notebook))

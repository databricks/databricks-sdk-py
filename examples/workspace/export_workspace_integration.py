import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

export_response = w.workspace.export(format=workspace.ExportFormat.SOURCE, path=notebook)

import base64
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

w.workspace.import_(content=base64.b64encode(("CREATE LIVE TABLE dlt_sample AS SELECT 1").encode()).decode(),
                    format=workspace.ImportFormat.SOURCE,
                    language=workspace.Language.SQL,
                    overwrite=True,
                    path=notebook_path)

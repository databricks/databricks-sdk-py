import base64
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

w.workspace.import_(path=notebook_path,
                    overwrite=true_,
                    format=workspace.ImportFormat.SOURCE,
                    language=workspace.Language.PYTHON,
                    content=base64.b64encode(("""print(1)
""").encode()).decode())

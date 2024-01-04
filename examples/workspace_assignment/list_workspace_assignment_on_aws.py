from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

workspace_id = os.environ["DUMMY_WORKSPACE_ID"]

all = a.workspace_assignment.list(workspace_id=workspace_id)

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

conf = w.workspace_conf.get_status(keys="enableWorkspaceFilesystem")

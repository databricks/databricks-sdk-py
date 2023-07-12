import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]

command_context = w.command_execution.start(cluster_id, compute.Language.PYTHON)

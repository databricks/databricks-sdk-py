import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import Language

w = WorkspaceClient()

cluster_id = w.clusters.ensure_cluster_is_running(
    os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]

res = w.command_execution.execute(cluster_id=cluster_id, language=Language.PYTHON, command="print(1)")

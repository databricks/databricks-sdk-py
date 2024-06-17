import os

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

cluster_id = w.clusters.ensure_cluster_is_running(
    os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]

res = w.command_executor.execute(cluster_id, "python", "print(1)")

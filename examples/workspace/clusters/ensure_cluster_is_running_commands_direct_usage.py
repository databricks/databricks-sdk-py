import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]

context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()

w.clusters.ensure_cluster_is_running(cluster_id)

# cleanup
w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

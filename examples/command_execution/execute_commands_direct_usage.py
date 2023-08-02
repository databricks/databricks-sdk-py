import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]

context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()

text_results = w.command_execution.execute(cluster_id=cluster_id,
                                           context_id=context.id,
                                           language=compute.Language.PYTHON,
                                           command="print(1)").result()

# cleanup
w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

cluster_id = w.clusters.ensure_cluster_is_running(
    os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]

w.libraries.update(cluster_id=cluster_id,
                   install=[compute.Library(pypi=compute.PythonPyPiLibrary(package="dbl-tempo"))]).result()

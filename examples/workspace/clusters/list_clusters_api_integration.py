from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

all = w.clusters.list(compute.ListClustersRequest())

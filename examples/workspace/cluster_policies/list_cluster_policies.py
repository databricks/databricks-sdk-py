from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

all = w.cluster_policies.list(compute.ListClusterPoliciesRequest())

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import compute

w = WorkspaceClient()

all = w.policy_families.list(compute.ListPolicyFamiliesRequest())

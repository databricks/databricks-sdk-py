from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

all = w.cluster_policies.list(compute.ListClusterPoliciesRequest())

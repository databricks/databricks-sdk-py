from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

smallest = w.clusters.select_node_type(local_disk=True)

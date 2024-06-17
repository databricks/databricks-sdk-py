from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

conn_list = w.connections.list(catalog.ListConnectionsRequest())

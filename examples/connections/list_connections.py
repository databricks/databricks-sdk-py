from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

conn_list = w.connections.list()

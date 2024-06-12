from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

nodes = w.clusters.list_node_types()

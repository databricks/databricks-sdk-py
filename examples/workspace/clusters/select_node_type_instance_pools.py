from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

smallest = w.clusters.select_node_type(local_disk=True)

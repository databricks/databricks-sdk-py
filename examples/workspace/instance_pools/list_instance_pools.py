from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.instance_pools.list()

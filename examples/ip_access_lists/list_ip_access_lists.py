from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.ip_access_lists.list()

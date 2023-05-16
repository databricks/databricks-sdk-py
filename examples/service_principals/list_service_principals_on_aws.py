from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.service_principals.list()

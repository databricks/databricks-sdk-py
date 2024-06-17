from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

list = w.git_credentials.list()

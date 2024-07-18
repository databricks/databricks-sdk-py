from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.storage_credentials.list()

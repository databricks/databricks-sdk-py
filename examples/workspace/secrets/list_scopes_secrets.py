from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

scopes = w.secrets.list_scopes()

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

workspace_id = w.w.current_workspace_id()

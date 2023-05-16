from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

me2 = w.current_user.me()

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

w.r.wait(update_function)

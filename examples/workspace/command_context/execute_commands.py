from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

res = w.command_context.execute("print(1)")

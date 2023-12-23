from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

res = w.command_execution.execute(command="print(1)")

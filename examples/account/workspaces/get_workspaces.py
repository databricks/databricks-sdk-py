from databricks.sdk import AccountClient

a = AccountClient()

created = a.waiter.get()

by_id = a.workspaces.get(workspace_id=created.workspace_id)

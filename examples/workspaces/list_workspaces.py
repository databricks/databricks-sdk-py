from databricks.sdk import AccountClient

a = AccountClient()

all = a.workspaces.list()

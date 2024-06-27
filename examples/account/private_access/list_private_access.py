from databricks.sdk import AccountClient

a = AccountClient()

all = a.private_access.list()

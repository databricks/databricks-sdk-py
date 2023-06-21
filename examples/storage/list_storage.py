from databricks.sdk import AccountClient

a = AccountClient()

configs = a.storage.list()

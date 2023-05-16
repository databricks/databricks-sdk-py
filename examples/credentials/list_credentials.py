from databricks.sdk import AccountClient

a = AccountClient()

configs = a.credentials.list()

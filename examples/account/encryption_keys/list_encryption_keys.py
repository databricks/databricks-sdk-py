from databricks.sdk import AccountClient

a = AccountClient()

all = a.encryption_keys.list()

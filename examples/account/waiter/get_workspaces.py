from databricks.sdk import AccountClient

a = AccountClient()

created = a.waiter.get()

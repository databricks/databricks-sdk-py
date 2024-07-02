from databricks.sdk import AccountClient

a = AccountClient()

all = a.budgets.list()

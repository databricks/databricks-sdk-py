from databricks.sdk import AccountClient

a = AccountClient()

all = a.vpc_endpoints.list()

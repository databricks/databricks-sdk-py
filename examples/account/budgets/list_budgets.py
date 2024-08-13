from databricks.sdk import AccountClient
from databricks.sdk.service import billing

a = AccountClient()

all = a.budgets.list(billing.ListBudgetConfigurationsRequest())

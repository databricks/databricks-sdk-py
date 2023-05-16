from databricks.sdk import AccountClient
from databricks.sdk.service import billing

a = AccountClient()

all = a.log_delivery.list(billing.ListLogDeliveryRequest())

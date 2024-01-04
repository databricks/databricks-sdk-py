from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

resp = a.billable_usage.download(start_month="2023-01", end_month="2023-02")

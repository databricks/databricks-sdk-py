from databricks.sdk import AccountClient

a = AccountClient()

resp = a.billable_usage.download(start_month="2023-01", end_month="2023-02")

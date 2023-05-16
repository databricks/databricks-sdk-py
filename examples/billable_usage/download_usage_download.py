from databricks.sdk import AccountClient

a = AccountClient()

a.billable_usage.download(start_month="2022-01", end_month="2022-02")

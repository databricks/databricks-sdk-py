from databricks.sdk import AccountClient

a = AccountClient()

resp = a.billable_usage.download(start_month="2024-08", end_month="2024-09")

out = a.io.read(resp.contents)

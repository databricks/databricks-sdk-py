def test_workspaces():
    from databricks.sdk import AccountClient
    a = AccountClient(profile='aws-prod-acct')
    for w in a.workspaces.list():
        print(w.workspace_name)
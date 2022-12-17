def test_workspaces(account_client):
    for w in account_client.workspaces.list():
        print(w.workspace_name)
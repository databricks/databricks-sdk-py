from databricks.sdk import AccountClient, WorkspaceClient


def test_workspace_operations(unified_config):
    client = WorkspaceClient(config=unified_config)
    user = client.current_user.me()
    assert user is not None


def test_account_operations(unified_config):
    client = AccountClient(config=unified_config)
    groups = client.groups.list()
    assert groups is not None

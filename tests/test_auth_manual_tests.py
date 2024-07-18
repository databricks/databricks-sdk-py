from databricks.sdk.core import Config

from .conftest import set_az_path, set_home


def test_azure_cli_workspace_header_present(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    resource_id = '/subscriptions/123/resourceGroups/abc/providers/Microsoft.Databricks/workspaces/abc123'
    cfg = Config(auth_type='azure-cli',
                 host='https://adb-123.4.azuredatabricks.net',
                 azure_workspace_resource_id=resource_id)
    assert 'X-Databricks-Azure-Workspace-Resource-Id' in cfg.authenticate()
    assert cfg.authenticate()['X-Databricks-Azure-Workspace-Resource-Id'] == resource_id


def test_azure_cli_user_with_management_access(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    resource_id = '/subscriptions/123/resourceGroups/abc/providers/Microsoft.Databricks/workspaces/abc123'
    cfg = Config(auth_type='azure-cli',
                 host='https://adb-123.4.azuredatabricks.net',
                 azure_workspace_resource_id=resource_id)
    assert 'X-Databricks-Azure-SP-Management-Token' in cfg.authenticate()


def test_azure_cli_user_no_management_access(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    monkeypatch.setenv('FAIL_IF', 'https://management.core.windows.net/')
    resource_id = '/subscriptions/123/resourceGroups/abc/providers/Microsoft.Databricks/workspaces/abc123'
    cfg = Config(auth_type='azure-cli',
                 host='https://adb-123.4.azuredatabricks.net',
                 azure_workspace_resource_id=resource_id)
    assert 'X-Databricks-Azure-SP-Management-Token' not in cfg.authenticate()


def test_azure_cli_fallback(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    monkeypatch.setenv('FAIL_IF', 'subscription')
    resource_id = '/subscriptions/123/resourceGroups/abc/providers/Microsoft.Databricks/workspaces/abc123'
    cfg = Config(auth_type='azure-cli',
                 host='https://adb-123.4.azuredatabricks.net',
                 azure_workspace_resource_id=resource_id)
    assert 'X-Databricks-Azure-SP-Management-Token' in cfg.authenticate()


def test_azure_cli_with_warning_on_stderr(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    monkeypatch.setenv('WARN', 'this is a warning')
    resource_id = '/subscriptions/123/resourceGroups/abc/providers/Microsoft.Databricks/workspaces/abc123'
    cfg = Config(auth_type='azure-cli',
                 host='https://adb-123.4.azuredatabricks.net',
                 azure_workspace_resource_id=resource_id)
    assert 'X-Databricks-Azure-SP-Management-Token' in cfg.authenticate()

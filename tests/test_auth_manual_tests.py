from databricks.sdk.core import Config

from .conftest import __tests__

def test_azure_cli_workspace_header_present(monkeypatch):
    monkeypatch.setenv('HOME', __tests__ + '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    resource_id = '/subscriptions/123/resourceGroups/abc/providers/Microsoft.Databricks/workspaces/abc123'
    cfg = Config(auth_type='azure-cli', host='x', azure_workspace_resource_id=resource_id)
    assert 'X-Databricks-Azure-Workspace-Resource-Id' in cfg.authenticate()
    assert cfg.authenticate()['X-Databricks-Azure-Workspace-Resource-Id'] == resource_id


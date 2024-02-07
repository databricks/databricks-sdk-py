import pytest


def test_get_workspace_client(a):
    if a.config.is_azure or a.config.is_gcp:
        pytest.skip('not available on Azure and GCP currently')
    wss = list(a.workspaces.list())
    if len(wss) == 0:
        pytest.skip("no workspaces")
    w = a.get_workspace_client(wss[0])
    assert w.current_user.me().active

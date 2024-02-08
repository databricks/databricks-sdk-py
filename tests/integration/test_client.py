import pytest


def test_get_workspace_client(a):
    if a.config.is_azure or a.config.is_gcp:
        pytest.skip('Not available on Azure and GCP currently')
    wss = list(a.workspaces.list())
    if len(wss) == 0:
        pytest.skip("no workspaces")
    w = a.get_workspace_client(wss[0])
    assert w.current_user.me().active


def test_get_workspace_id(ucws, env_or_skip):
    ws_id = int(env_or_skip('THIS_WORKSPACE_ID'))
    assert ucws.get_workspace_id() == ws_id

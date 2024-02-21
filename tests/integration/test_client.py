import pytest


def test_get_workspace_client(a, env_or_skip):
    workspace_id = env_or_skip("TEST_WORKSPACE_ID")
    ws = a.workspaces.get(workspace_id)
    w = a.get_workspace_client(ws)
    assert w.current_user.me().active


def test_get_workspace_id(ucws, env_or_skip):
    ws_id = int(env_or_skip('THIS_WORKSPACE_ID'))
    assert ucws.get_workspace_id() == ws_id


def test_creating_ws_client_from_ac_client_does_not_override_config(a):
    wss = list(a.workspaces.list())
    if len(wss) == 0:
        pytest.skip("no workspaces")
    a.get_workspace_client(wss[0])

    # assert doesn't throw
    wss = list(a.workspaces.list())

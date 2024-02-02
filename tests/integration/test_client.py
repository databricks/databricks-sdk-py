import pytest


def test_get_workspace_client(a):
    wss = list(a.workspaces.list())
    if len(wss) == 0:
        pytest.skip("no workspaces")
    w = a.get_workspace_client(wss[0])
    assert w.current_user.me().active

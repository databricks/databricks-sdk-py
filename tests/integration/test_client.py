def test_get_workspace_client(a, env_or_skip):
    workspace_id = env_or_skip("TEST_WORKSPACE_ID")
    ws = a.workspaces.get(workspace_id)
    w = a.get_workspace_client(ws)
    assert w.current_user.me().active

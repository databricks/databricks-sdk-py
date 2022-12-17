def test_cluster_events(workspace_client, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER")
    count = 0
    for e in workspace_client.clusters.events(cluster_id):
        count += 1
    assert count > 0
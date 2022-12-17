from databricks.sdk.service.clusters import State


def test_cluster_events(workspace_client, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    count = 0
    for e in workspace_client.clusters.events(cluster_id):
        count += 1
    assert count > 0


def test_start_cluster(workspace_client, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    info = workspace_client.clusters.start(cluster_id)
    assert info.state == State.RUNNING
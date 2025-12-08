from databricks.sdk import WorkspaceClient

def test_smallest_node_type_spog_with_profile():
    w = WorkspaceClient(
        profile="spog-test")
    node_type_id = w.clusters.select_node_type(local_disk=True)
    assert node_type_id is not None


def test_smallest_node_type_spog_without_profile():
    w = WorkspaceClient(
        host="https://db-deco-test.databricks.com",
        is_unified_host=True,
    )
    node_type_id = w.clusters.select_node_type(local_disk=True)
    assert node_type_id is not None
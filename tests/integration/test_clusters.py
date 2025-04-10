import pytest

from databricks.sdk.compute.v2 import compute
from databricks.sdk.compute.v2.client import ClustersClient
from databricks.sdk.databricks.core import DatabricksError

# from databricks.sdk.service.compute import EventType


def test_smallest_node_type(w):
    cc = ClustersClient(config=w)
    node_type_id = cc.select_node_type(local_disk=True)
    assert node_type_id is not None


def test_latest_runtime(w):
    cc = ClustersClient(config=w)
    spark_version = cc.select_spark_version(long_term_support=True)
    assert spark_version is not None


def test_cluster_events(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    count = 0
    cc = ClustersClient(config=w)
    for e in cc.events(cluster_id, event_types=[compute.EventType.STARTING, compute.EventType.TERMINATING]):
        count += 1
    assert count > 0


# TODO: Re-enable this test after adding waiters to the SDK
# def test_ensure_cluster_is_running(w, env_or_skip):
#     cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
#     cc = ClustersClient(config=w)
#     cc.ensure_cluster_is_running(cluster_id)


# TODO: Re-enable this test after adding LRO support to the SDK
# def test_create_cluster(w, env_or_skip, random):
#     from databricks.sdk.compute.v2.client import ClustersClient
#     cc = ClustersClient(config=w)

#     info = cc.create(
#         cluster_name=f"databricks-sdk-py-{random(8)}",
#         spark_version=cc.select_spark_version(long_term_support=True),
#         instance_pool_id=env_or_skip("TEST_INSTANCE_POOL_ID"),
#         autotermination_minutes=10,
#         num_workers=1,
#     ).result(timeout=timedelta(minutes=20))
#     logging.info(f"Created: {info}")


def test_error_unmarshall(w, random):
    from databricks.sdk.compute.v2.client import ClustersClient

    cc = ClustersClient(config=w)
    with pytest.raises(DatabricksError) as exc_info:
        cc.get("123__non_existing__")
    err = exc_info.value
    assert "Cluster 123__non_existing__ does not exist" in str(err)
    assert "INVALID_PARAMETER_VALUE" == err.error_code

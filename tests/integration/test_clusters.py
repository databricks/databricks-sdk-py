import logging
from datetime import timedelta

import pytest

from databricks.sdk.core import DatabricksError
from databricks.sdk.service.compute import EventType


def test_noise(w):
    from concurrent.futures import ThreadPoolExecutor, wait
    futures = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(100):
            futures.append(pool.submit(w.clusters.select_node_type, local_disk=True))
        wait(futures)


def test_smallest_node_type(w):
    node_type_id = w.clusters.select_node_type(local_disk=True)
    assert node_type_id is not None


def test_latest_runtime(w):
    spark_version = w.clusters.select_spark_version(long_term_support=True)
    assert spark_version is not None


def test_cluster_events(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    count = 0
    for e in w.clusters.events(cluster_id, event_types=[EventType.STARTING, EventType.TERMINATING]):
        count += 1
    assert count > 0


def test_ensure_cluster_is_running(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    w.clusters.ensure_cluster_is_running(cluster_id)


def test_create_cluster(w, env_or_skip, random):
    info = w.clusters.create(cluster_name=f'databricks-sdk-py-{random(8)}',
                             spark_version=w.clusters.select_spark_version(long_term_support=True),
                             instance_pool_id=env_or_skip('TEST_INSTANCE_POOL_ID'),
                             autotermination_minutes=10,
                             num_workers=1,
                             timeout=timedelta(minutes=10))
    logging.info(f'Created: {info}')


def test_error_unmarshall(w, random):
    with pytest.raises(DatabricksError) as exc_info:
        w.clusters.get('__non_existing__')
    err = exc_info.value
    assert 'Cluster __non_existing__ does not exist' in str(err)
    assert 'INVALID_PARAMETER_VALUE' == err.error_code

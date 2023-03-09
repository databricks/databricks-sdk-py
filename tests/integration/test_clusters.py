import logging

import pytest

from databricks.sdk.service.clusters import State


def test_smallest_node_type(w):
    node_type_id = w.clusters.select_node_type(local_disk=True)
    assert node_type_id is not None


def test_latest_runtime(w):
    spark_version = w.clusters.select_spark_version(long_term_support=True)
    assert spark_version is not None


def test_cluster_events(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    count = 0
    for e in w.clusters.events(cluster_id):
        count += 1
    assert count > 0


def test_start_cluster(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    info = w.clusters.start(cluster_id)
    assert info.state == State.RUNNING


def test_create_cluster(w):
    if not w.config.is_aws:
        pytest.skip("this test runs only on AWS")
    info = w.clusters.create(cluster_name='Created cluster',
                             spark_version='12.0.x-scala2.12',
                             node_type_id='m5d.large',
                             autotermination_minutes=10,
                             num_workers=1,
                             timeout=10)
    logging.info(f'Created: {info}')

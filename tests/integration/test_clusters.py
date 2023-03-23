from datetime import timedelta
import logging


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


def test_ensure_cluster_is_running(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    w.clusters.ensure_cluster_is_running(cluster_id)


def test_create_cluster(w, env_or_skip):
    info = w.clusters.create(cluster_name='Created cluster',
                             spark_version=w.clusters.select_spark_version(long_term_support=True),
                             instance_pool_id=env_or_skip('TEST_INSTANCE_POOL_ID'),
                             autotermination_minutes=10,
                             num_workers=1,
                             timeout=timedelta(minutes=10))
    logging.info(f'Created: {info}')

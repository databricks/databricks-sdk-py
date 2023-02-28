import os


def test_rest_dbfs_ls(w, env_or_skip):
    from databricks.sdk.runtime import dbutils

    x = dbutils.fs.ls('/')

    assert len(x) > 1


def test_proxy_dbfs_mounts(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    os.environ['DATABRICKS_CLUSTER_ID'] = cluster_id

    from databricks.sdk.runtime import dbutils

    x = dbutils.fs.mounts()

    assert len(x) > 1


def test_proxy_secret_scopes(w, env_or_skip):
    cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")
    os.environ['DATABRICKS_CLUSTER_ID'] = cluster_id

    from databricks.sdk.runtime import dbutils

    x = dbutils.secrets.listScopes()

    assert len(x) > 0

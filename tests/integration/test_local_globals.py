from contextlib import contextmanager


@contextmanager
def restorable_env():
    import os
    current_env = os.environ.copy()

    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(current_env)


def test_local_global_spark(w, env_or_skip):
    cluster_id = env_or_skip("SPARK_CONNECT_CLUSTER_ID")
    with restorable_env():
        import os
        os.environ["DATABRICKS_CLUSTER_ID"] = cluster_id
        from databricks.sdk.runtime import spark
        assert spark.sql("SELECT 1").collect()[0][0] == 1


def test_local_global_display(w, env_or_skip):
    from databricks.sdk.runtime import display, displayHTML

    # assert no errors
    display("test")
    displayHTML("test")

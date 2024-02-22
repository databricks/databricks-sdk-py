def test_runtime_spark(w, env_or_skip):
    env_or_skip("SPARK_CONNECT_CLUSTER_ID")

    from databricks.sdk.runtime import spark
    assert spark.sql("SELECT 1").collect()[0][0] == 1

def test_runtime_display(w, env_or_skip):
    from databricks.sdk.runtime import display, displayHTML

    # assert no errors
    display("test")
    displayHTML("test")

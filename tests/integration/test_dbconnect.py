def test_it_works_with_dbconnect(w):
    import pyspark.sql.connect.functions as F
    from pyspark.sql.connect.session import SparkSession

    spark = SparkSession.builder.remote('databricks://default').getOrCreate()

    df = spark.read.table("samples.nyctaxi.trips")
    res = df.where(F.col("trip_distance") < F.lit(10)).limit(10)
    res.show()
    print(1)


def test_it_works_with_vanilla_dbconnect(w):
    import os
    from urllib.parse import urlparse

    import pyspark.sql.connect.functions as F
    from pyspark.sql.connect.session import SparkSession
    h = urlparse(os.getenv("DATABRICKS_HOST"))

    spark = SparkSession.builder.remote(
        f'sc://{h.hostname}:443/;token={os.getenv("DATABRICKS_TOKEN")};use_ssl=true;x-databricks-cluster-id={os.getenv("SPARK_CONNECT_CLUSTER_ID")}'
    ).getOrCreate()

    df = spark.read.table("samples.nyctaxi.trips")
    res = df.where(F.col("trip_distance") < F.lit(10)).limit(10)
    res.show()
    print(1)

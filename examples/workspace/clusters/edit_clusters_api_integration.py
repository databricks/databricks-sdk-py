import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

cluster_name = f'sdk-{time.time_ns()}'

latest = w.clusters.select_spark_version(latest=True, long_term_support=True)

clstr = w.clusters.create(cluster_name=cluster_name,
                          spark_version=latest,
                          instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                          autotermination_minutes=15,
                          num_workers=1).result()

_ = w.clusters.edit(cluster_id=clstr.cluster_id,
                    spark_version=latest,
                    cluster_name=cluster_name,
                    instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                    autotermination_minutes=10,
                    num_workers=2).result()

# cleanup
w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

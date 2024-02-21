import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

latest = w.clusters.select_spark_version(latest=True, long_term_support=True)

cluster_name = f'sdk-{time.time_ns()}'

other_owner = w.users.create(user_name=f'sdk-{time.time_ns()}@example.com')

clstr = w.clusters.create(cluster_name=cluster_name,
                          spark_version=latest,
                          instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                          autotermination_minutes=15,
                          num_workers=1).result()

w.clusters.change_owner(cluster_id=clstr.cluster_id, owner_username=other_owner.user_name)

# cleanup
w.users.delete(id=other_owner.id)
w.clusters.permanent_delete(cluster_id=clstr.cluster_id)

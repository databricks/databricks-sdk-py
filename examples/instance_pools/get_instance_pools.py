import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

smallest = w.clusters.select_node_type(local_disk=True)

created = w.instance_pools.create(instance_pool_name=f'sdk-{time.time_ns()}', node_type_id=smallest)

by_id = w.instance_pools.get(instance_pool_id=created.instance_pool_id)

# cleanup
w.instance_pools.delete(instance_pool_id=created.instance_pool_id)

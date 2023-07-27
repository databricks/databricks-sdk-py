import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.warehouses.create(name=f'sdk-{time.time_ns()}',
                              cluster_size="2X-Small",
                              max_num_clusters=1,
                              auto_stop_mins=10).result()

_ = w.warehouses.edit(id=created.id,
                      name=f'sdk-{time.time_ns()}',
                      cluster_size="2X-Small",
                      max_num_clusters=1,
                      auto_stop_mins=10)

# cleanup
w.warehouses.delete(id=created.id)

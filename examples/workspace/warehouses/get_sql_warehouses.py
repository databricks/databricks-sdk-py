import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

created = w.warehouses.create(
    name=f'sdk-{time.time_ns()}',
    cluster_size="2X-Small",
    max_num_clusters=1,
    auto_stop_mins=10,
    tags=sql.EndpointTags(
        custom_tags=[sql.EndpointTagPair(key="Owner", value="eng-dev-ecosystem-team_at_databricks.com")
                     ])).result()

wh = w.warehouses.get(id=created.id)

# cleanup
w.warehouses.delete(id=created.id)

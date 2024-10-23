import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

srcs = w.data_sources.list()

query = w.queries.create(query=sql.CreateQueryRequestQuery(display_name=f'sdk-{time.time_ns()}',
                                                           warehouse_id=srcs[0].warehouse_id,
                                                           description="test query from Go SDK",
                                                           query_text="SELECT 1"))

# cleanup
w.queries.delete(id=query.id)

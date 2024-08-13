import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

srcs = w.data_sources.list()

query = w.queries.create(query=sql.CreateQueryRequestQuery(display_name=f'sdk-{time.time_ns()}',
                                                           warehouse_id=srcs[0].warehouse_id,
                                                           description="test query from Go SDK",
                                                           query_text="SHOW TABLES"))

updated = w.queries.update(id=query.id,
                           query=sql.UpdateQueryRequestQuery(display_name=f'sdk-{time.time_ns()}',
                                                             description="UPDATED: test query from Go SDK",
                                                             query_text="SELECT 2+2"),
                           update_mask="display_name,description,query_text")

# cleanup
w.queries.delete(id=query.id)

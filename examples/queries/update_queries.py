import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

srcs = w.data_sources.list()

query = w.queries.create(name=f'sdk-{time.time_ns()}',
                         data_source_id=srcs[0].id,
                         description="test query from Go SDK",
                         query="SHOW TABLES")

updated = w.queries.update(query_id=query.id,
                           name=f'sdk-{time.time_ns()}',
                           data_source_id=srcs[0].id,
                           description="UPDATED: test query from Go SDK",
                           query="SELECT 2+2")

# cleanup
w.queries.delete(query_id=query.id)

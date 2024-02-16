import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

conn_create = w.connections.create(comment="Go SDK Acceptance Test Connection",
                                   connection_type=catalog.ConnectionType.DATABRICKS,
                                   name=f'sdk-{time.time_ns()}',
                                   options={
                                       "host":
                                       "%s-fake-workspace.cloud.databricks.com" % (f'sdk-{time.time_ns()}'),
                                       "httpPath":
                                       "/sql/1.0/warehouses/%s" % (f'sdk-{time.time_ns()}'),
                                       "personalAccessToken":
                                       f'sdk-{time.time_ns()}',
                                   })

conn_update = w.connections.update(name=conn_create.name,
                                   options={
                                       "host":
                                       "%s-fake-workspace.cloud.databricks.com" % (f'sdk-{time.time_ns()}'),
                                       "httpPath":
                                       "/sql/1.0/warehouses/%s" % (f'sdk-{time.time_ns()}'),
                                       "personalAccessToken":
                                       f'sdk-{time.time_ns()}',
                                   })

# cleanup
w.connections.delete(name=conn_create.name)

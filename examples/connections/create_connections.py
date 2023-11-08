from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

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

# cleanup
w.connections.delete(name_arg=conn_create.name)

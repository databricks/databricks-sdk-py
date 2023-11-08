from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

new_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=new_catalog.name)

_ = w.schemas.update(full_name=created.full_name, comment=f'sdk-{time.time_ns()}')

# cleanup
w.catalogs.delete(name=new_catalog.name, force=True)
w.schemas.delete(full_name=created.full_name)

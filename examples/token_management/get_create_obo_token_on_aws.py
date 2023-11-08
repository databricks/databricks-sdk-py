from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

groups = w.groups.group_display_name_to_id_map(iam.ListGroupsRequest())

spn = w.service_principals.create(display_name=f'sdk-{time.time_ns()}',
                                  groups=[iam.ComplexValue(value=groups["admins"])])

obo = w.token_management.create_obo_token(application_id=spn.application_id, lifetime_seconds=60)

by_id = w.token_management.get(token_id=obo.token_info.token_id)

# cleanup
w.service_principals.delete(id=spn.id)
w.token_management.delete(token_id=obo.token_info.token_id)

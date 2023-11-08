from databricks.sdk import AccountClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

a = AccountClient()

sp_create = a.service_principals.create(active=True, display_name=f'sdk-{time.time_ns()}')

sp = a.service_principals.get(id=sp_create.id)

a.service_principals.patch(id=sp.id,
                           operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
                           schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])

# cleanup
a.service_principals.delete(id=sp_create.id)

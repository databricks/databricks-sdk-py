import time

from databricks.sdk import AccountClient
from databricks.sdk.service import iam

a = AccountClient()

sp_create = a.service_principals.create(active=True, display_name=f'sdk-{time.time_ns()}')

sp = a.service_principals.get(id=sp_create.id)

a.service_principals.patch(id=sp.id,
                           operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
                           schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])

# cleanup
a.service_principals.delete(id=sp_create.id)

import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

created = w.service_principals.create(display_name=f'sdk-{time.time_ns()}')

by_id = w.service_principals.get(id=created.id)

w.service_principals.patch(id=by_id.id,
                           operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
                           schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])

# cleanup
w.service_principals.delete(id=created.id)

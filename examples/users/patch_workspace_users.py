import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

user = w.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')

w.users.patch(id=user.id,
              operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
              schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])

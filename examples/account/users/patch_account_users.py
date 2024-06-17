import time

from databricks.sdk import AccountClient
from databricks.sdk.service import iam

a = AccountClient()

user = a.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')

a.users.patch(id=user.id,
              schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP],
              operations=[
                  iam.Patch(op=iam.PatchOp.ADD,
                            value=iam.User(roles=[iam.ComplexValue(value="account_admin")]))
              ])

# cleanup
a.users.delete(id=user.id)

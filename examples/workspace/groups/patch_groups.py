import time
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

group = w.groups.create(display_name=f'sdk-{time.time_ns()}-group')
user = w.users.create(
    display_name=f'sdk-{time.time_ns()}-user', user_name=f'sdk-{time.time_ns()}@example.com')

w.groups.patch(
    id=group.id,
    operations=[iam.Patch(
        op=iam.PatchOp.ADD,
        value={"members": [{
            "value": user.id,
        }]},
    )],
    schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP],
)

# cleanup
w.users.delete(id=user.id)
w.groups.delete(id=group.id)

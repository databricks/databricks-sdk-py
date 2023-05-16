import os
import time

from databricks.sdk import AccountClient
from databricks.sdk.service import iam

a = AccountClient()

spn = a.service_principals.create(display_name=f'sdk-{time.time_ns()}')

spn_id = spn.id

workspace_id = os.environ["TEST_WORKSPACE_ID"]

a.workspace_assignment.update(workspace_id=workspace_id,
                              principal_id=spn_id,
                              permissions=[iam.WorkspacePermission.USER])

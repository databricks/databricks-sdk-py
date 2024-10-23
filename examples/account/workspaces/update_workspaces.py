import os
import time

from databricks.sdk import AccountClient
from databricks.sdk.service import provisioning

a = AccountClient()

update_role = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))

created = a.waiter.get()

_ = a.workspaces.update(workspace_id=created.workspace_id, credentials_id=update_role.credentials_id).result()

# cleanup
a.credentials.delete(credentials_id=update_role.credentials_id)

import os
import time

from databricks.sdk import AccountClient
from databricks.sdk.service import provisioning

a = AccountClient()

role = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))

by_id = a.credentials.get(get=role.credentials_id)

# cleanup
a.credentials.delete(delete=role.credentials_id)

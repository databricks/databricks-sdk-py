import os
import time

from databricks.sdk import AccountClient
from databricks.sdk.service import provisioning

a = AccountClient()

creds = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_LOGDELIVERY_ARN"])))

# cleanup
a.credentials.delete(credentials_id=creds.credentials_id)

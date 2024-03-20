import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

storage_credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
    comment="created via SDK")

# cleanup
w.storage_credentials.delete(name=storage_credential.name)

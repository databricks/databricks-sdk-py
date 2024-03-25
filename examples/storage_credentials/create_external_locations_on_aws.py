import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))

# cleanup
w.storage_credentials.delete(name=credential.name)

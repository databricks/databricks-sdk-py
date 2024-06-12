import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

created = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))

by_name = w.storage_credentials.get(get=created.name)

# cleanup
w.storage_credentials.delete(delete=created.name)

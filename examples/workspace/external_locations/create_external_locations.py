import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))

created = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                      credential_name=credential.name,
                                      url=f's3://{os.environ["TEST_BUCKET"]}/sdk-{time.time_ns()}')

# cleanup
w.storage_credentials.delete(delete=credential.name)
w.external_locations.delete(delete=created.name)

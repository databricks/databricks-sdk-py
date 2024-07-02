import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))

created = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                      credential_name=credential.name,
                                      url="s3://%s/%s" % (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))

# cleanup
w.storage_credentials.delete(name=credential.name)
w.external_locations.delete(name=created.name)

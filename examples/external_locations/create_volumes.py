import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

storage_credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
    comment="created via SDK")

external_location = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                credential_name=storage_credential.name,
                                                comment="created via SDK",
                                                url="s3://" + os.environ["TEST_BUCKET"] + "/" +
                                                f'sdk-{time.time_ns()}')

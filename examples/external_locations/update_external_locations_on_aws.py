from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]))

created = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                      credential_name=credential.name,
                                      url="s3://%s/%s" % (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))

_ = w.external_locations.update(name=created.name,
                                credential_name=credential.name,
                                url="s3://%s/%s" % (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))

# cleanup
w.storage_credentials.delete(name=credential.name)
w.external_locations.delete(name=created.name)

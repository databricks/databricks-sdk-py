from databricks.sdk import AccountClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

a = AccountClient()

storage = a.storage.create(
    storage_configuration_name=f'sdk-{time.time_ns()}',
    root_bucket_info=provisioning.RootBucketInfo(bucket_name=os.environ["TEST_ROOT_BUCKET"]))

role = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))

update_role = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_CROSSACCOUNT_ARN"])))

created = a.workspaces.create(workspace_name=f'sdk-{time.time_ns()}',
                              aws_region=os.environ["AWS_REGION"],
                              credentials_id=role.credentials_id,
                              storage_configuration_id=storage.storage_configuration_id).result()

_ = a.workspaces.update(workspace_id=created.workspace_id, credentials_id=update_role.credentials_id).result()

# cleanup
a.storage.delete(storage_configuration_id=storage.storage_configuration_id)
a.credentials.delete(credentials_id=role.credentials_id)
a.credentials.delete(credentials_id=update_role.credentials_id)
a.workspaces.delete(workspace_id=created.workspace_id)

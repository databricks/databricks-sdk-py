from databricks.sdk import AccountClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

a = AccountClient()

bucket = a.storage.create(storage_configuration_name=f'sdk-{time.time_ns()}',
                          root_bucket_info=provisioning.RootBucketInfo(bucket_name=f'sdk-{time.time_ns()}'))

creds = a.credentials.create(
    credentials_name=f'sdk-{time.time_ns()}',
    aws_credentials=provisioning.CreateCredentialAwsCredentials(sts_role=provisioning.CreateCredentialStsRole(
        role_arn=os.environ["TEST_LOGDELIVERY_ARN"])))

created = a.log_delivery.create(log_delivery_configuration=billing.CreateLogDeliveryConfigurationParams(
    config_name=f'sdk-{time.time_ns()}',
    credentials_id=creds.credentials_id,
    storage_configuration_id=bucket.storage_configuration_id,
    log_type=billing.LogType.AUDIT_LOGS,
    output_format=billing.OutputFormat.JSON))

by_id = a.log_delivery.get(log_delivery_configuration_id=created.log_delivery_configuration.config_id)

# cleanup
a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)
a.credentials.delete(credentials_id=creds.credentials_id)
a.log_delivery.patch_status(log_delivery_configuration_id=created.log_delivery_configuration.config_id,
                            status=billing.LogDeliveryConfigStatus.DISABLED)

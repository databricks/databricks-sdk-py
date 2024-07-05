import os
import time

from databricks.sdk import AccountClient
from databricks.sdk.service import billing, provisioning

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

# cleanup
a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)
a.credentials.delete(credentials_id=creds.credentials_id)
a.log_delivery.patch_status(log_delivery_configuration_id=created.log_delivery_configuration.config_id,
                            status=billing.LogDeliveryConfigStatus.DISABLED)

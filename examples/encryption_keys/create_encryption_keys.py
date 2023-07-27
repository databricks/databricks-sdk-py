import os

from databricks.sdk import AccountClient
from databricks.sdk.service import provisioning

a = AccountClient()

created = a.encryption_keys.create(aws_key_info=provisioning.CreateAwsKeyInfo(
    key_arn=os.environ["TEST_MANAGED_KMS_KEY_ARN"], key_alias=os.environ["TEST_STORAGE_KMS_KEY_ALIAS"]),
                                   use_cases=[provisioning.KeyUseCase.MANAGED_SERVICES])

# cleanup
a.encryption_keys.delete(customer_managed_key_id=created.customer_managed_key_id)

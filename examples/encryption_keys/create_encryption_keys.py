from databricks.sdk import AccountClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

a = AccountClient()

created = a.encryption_keys.create(aws_key_info=provisioning.CreateAwsKeyInfo(
    key_arn=os.environ["TEST_MANAGED_KMS_KEY_ARN"], key_alias=os.environ["TEST_STORAGE_KMS_KEY_ALIAS"]),
                                   use_cases=[provisioning.KeyUseCase.MANAGED_SERVICES])

# cleanup
a.encryption_keys.delete(customer_managed_key_id=created.customer_managed_key_id)

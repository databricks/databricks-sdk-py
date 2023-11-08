from databricks.sdk import AccountClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

a = AccountClient()

storage = a.storage.create(
    storage_configuration_name=f'sdk-{time.time_ns()}',
    root_bucket_info=provisioning.RootBucketInfo(bucket_name=os.environ["TEST_ROOT_BUCKET"]))

# cleanup
a.storage.delete(storage_configuration_id=storage.storage_configuration_id)

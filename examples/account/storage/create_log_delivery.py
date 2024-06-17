import time

from databricks.sdk import AccountClient
from databricks.sdk.service import provisioning

a = AccountClient()

bucket = a.storage.create(storage_configuration_name=f'sdk-{time.time_ns()}',
                          root_bucket_info=provisioning.RootBucketInfo(bucket_name=f'sdk-{time.time_ns()}'))

# cleanup
a.storage.delete(storage_configuration_id=bucket.storage_configuration_id)

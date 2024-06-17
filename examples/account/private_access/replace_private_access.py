import os
import time

from databricks.sdk import AccountClient

a = AccountClient()

created = a.private_access.create(private_access_settings_name=f'sdk-{time.time_ns()}',
                                  region=os.environ["AWS_REGION"])

a.private_access.replace(private_access_settings_id=created.private_access_settings_id,
                         private_access_settings_name=f'sdk-{time.time_ns()}',
                         region=os.environ["AWS_REGION"])

# cleanup
a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

import os
import time

from databricks.sdk import AccountClient

a = AccountClient()

created = a.private_access.create(private_access_settings_name=f'sdk-{time.time_ns()}',
                                  region=os.environ["AWS_REGION"])

by_id = a.private_access.get(private_access_settings_id=created.private_access_settings_id)

# cleanup
a.private_access.delete(private_access_settings_id=created.private_access_settings_id)

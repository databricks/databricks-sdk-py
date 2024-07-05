import time

from databricks.sdk import AccountClient

a = AccountClient()

spn = a.service_principals.create(display_name=f'sdk-{time.time_ns()}')

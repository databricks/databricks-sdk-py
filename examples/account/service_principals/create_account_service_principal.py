import time

from databricks.sdk import AccountClient

a = AccountClient()

sp_create = a.service_principals.create(active=True, display_name=f'sdk-{time.time_ns()}')

# cleanup
a.service_principals.delete(id=sp_create.id)

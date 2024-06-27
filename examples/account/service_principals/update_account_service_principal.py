import time

from databricks.sdk import AccountClient

a = AccountClient()

sp_create = a.service_principals.create(active=True, display_name=f'sdk-{time.time_ns()}')

sp = a.service_principals.get(id=sp_create.id)

a.service_principals.update(active=True, display_name=sp.display_name, id=sp.id)

# cleanup
a.service_principals.delete(id=sp_create.id)

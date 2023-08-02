import time

from databricks.sdk import AccountClient

a = AccountClient()

user = a.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')

by_id = a.users.get(get=user.id)

# cleanup
a.users.delete(delete=user.id)

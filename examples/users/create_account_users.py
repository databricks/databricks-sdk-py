import time

from databricks.sdk import AccountClient

a = AccountClient()

user = a.users.create(display_name=f'sdk-{time.time_ns()}', user_name=f'sdk-{time.time_ns()}@example.com')

# cleanup
a.users.delete(id=user.id)

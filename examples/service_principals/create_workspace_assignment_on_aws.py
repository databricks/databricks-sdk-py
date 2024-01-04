from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

spn = a.service_principals.create(display_name=f'sdk-{time.time_ns()}')

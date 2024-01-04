from databricks.sdk import AccountClient
from databricks.sdk.service import _internal
import time, base64, os

a = AccountClient()

ws = a.metastore_assignments.list(metastore_id=os.environ["TEST_METASTORE_ID"])

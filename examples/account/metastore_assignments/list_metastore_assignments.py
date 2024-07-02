import os

from databricks.sdk import AccountClient

a = AccountClient()

ws = a.metastore_assignments.list(metastore_id=os.environ["TEST_METASTORE_ID"])

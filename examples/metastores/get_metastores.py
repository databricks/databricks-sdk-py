from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                              storage_root="s3://%s/%s" %
                              (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))

_ = w.metastores.get(id=created.metastore_id)

# cleanup
w.metastores.delete(id=created.metastore_id, force=True)

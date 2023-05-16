import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                              storage_root=f's3://{os.environ["TEST_BUCKET"]}/sdk-{time.time_ns()}')

# cleanup
w.metastores.delete(id=created.metastore_id, force=True)

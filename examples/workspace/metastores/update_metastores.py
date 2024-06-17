import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                              storage_root="s3://%s/%s" %
                              (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))

_ = w.metastores.update(id=created.metastore_id, new_name=f'sdk-{time.time_ns()}')

# cleanup
w.metastores.delete(id=created.metastore_id, force=True)

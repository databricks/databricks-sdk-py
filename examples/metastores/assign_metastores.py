import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

workspace_id = os.environ["DUMMY_WORKSPACE_ID"]

created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                              storage_root="s3://%s/%s" %
                              (os.environ["TEST_BUCKET"], f'sdk-{time.time_ns()}'))

w.metastores.assign(metastore_id=created.metastore_id, workspace_id=workspace_id)

# cleanup
w.metastores.delete(id=created.metastore_id, force=True)

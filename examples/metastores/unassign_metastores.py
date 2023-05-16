import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

workspace_id = os.environ["TEST_WORKSPACE_ID"]

created = w.metastores.create(name=f'sdk-{time.time_ns()}',
                              storage_root=f's3://{os.environ["TEST_BUCKET"]}/sdk-{time.time_ns()}')

w.metastores.unassign(metastore_id=created.metastore_id, workspace_id=workspace_id)

# cleanup
w.metastores.delete(id=created.metastore_id, force=True)

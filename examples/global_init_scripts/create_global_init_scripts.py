from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

created = w.global_init_scripts.create(name=f'sdk-{time.time_ns()}',
                                       script=base64.b64encode(("echo 1").encode()).decode(),
                                       enabled=True,
                                       position=10)

# cleanup
w.global_init_scripts.delete(script_id=created.script_id)

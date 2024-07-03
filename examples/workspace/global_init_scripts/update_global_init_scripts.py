import base64
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.global_init_scripts.create(name=f'sdk-{time.time_ns()}',
                                       script=base64.b64encode(("echo 1").encode()).decode(),
                                       enabled=True,
                                       position=10)

w.global_init_scripts.update(script_id=created.script_id,
                             name=f'sdk-{time.time_ns()}',
                             script=base64.b64encode(("echo 2").encode()).decode())

# cleanup
w.global_init_scripts.delete(script_id=created.script_id)

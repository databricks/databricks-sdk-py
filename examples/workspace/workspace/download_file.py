import io
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat

w = WorkspaceClient()

py_file = f'/Users/{w.current_user.me().user_name}/file-{time.time_ns()}.py'

w.workspace.upload(py_file, io.BytesIO(b'print(1)'), format=ImportFormat.AUTO)
with w.workspace.download(py_file) as f:
    content = f.read()
    assert content == b'print(1)'

w.workspace.delete(py_file)
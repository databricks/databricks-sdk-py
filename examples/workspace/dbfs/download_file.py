import io
import pathlib
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

root = pathlib.Path(f'/tmp/{time.time_ns()}')

f = io.BytesIO(b"some text data")
w.dbfs.upload(f'{root}/01', f)

with w.dbfs.download(f'{root}/01') as f:
    assert f.read() == b"some text data"
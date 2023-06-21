import io
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/notebook-{time.time_ns()}.py'

w.workspace.upload(notebook, io.BytesIO(b'print(1)'))
with w.workspace.download(notebook) as f:
    content = f.read()
    assert content == b'# Databricks notebook source\nprint(1)'

w.workspace.delete(notebook)
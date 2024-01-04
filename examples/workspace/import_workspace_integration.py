from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

w.workspace.import_(path=notebook,
                    format=workspace.ImportFormat.SOURCE,
                    language=workspace.Language.PYTHON,
                    content=base64.b64encode(
                        ("# Databricks notebook source\nprint('hello from job')").encode()).decode(),
                    overwrite=True)

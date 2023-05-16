import base64
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

notebook = f'/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}'

w.workspace.import_(path=notebook,
                    format="SOURCE",
                    language="PYTHON",
                    content=base64.b64encode(
                        ("# Databricks notebook source\nprint('hello from job')").encode()).decode(),
                    overwrite=True)

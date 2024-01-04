from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal
import time, base64, os

w = WorkspaceClient()

all = w.pipelines.list_pipelines(pipelines.ListPipelinesRequest())

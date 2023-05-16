from databricks.sdk import WorkspaceClient
from databricks.sdk.service import pipelines

w = WorkspaceClient()

all = w.pipelines.list_pipelines(pipelines.ListPipelinesRequest())

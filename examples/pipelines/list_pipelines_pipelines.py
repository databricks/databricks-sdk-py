from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.pipelines.list_pipelines()

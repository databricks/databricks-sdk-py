from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.metastores.list()

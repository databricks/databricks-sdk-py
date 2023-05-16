from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

_ = w.metastores.summary()

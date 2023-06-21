from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

summary = w.metastores.summary()

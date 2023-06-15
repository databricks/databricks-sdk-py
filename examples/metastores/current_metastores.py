from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

current_metastore = w.metastores.current()

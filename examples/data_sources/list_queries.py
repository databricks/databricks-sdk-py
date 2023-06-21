from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

srcs = w.data_sources.list()

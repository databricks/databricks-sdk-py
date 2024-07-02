from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.external_locations.list()

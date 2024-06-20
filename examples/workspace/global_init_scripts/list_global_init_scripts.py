from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all = w.global_init_scripts.list()

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

conf = w.workspace_conf.get_status(keys="enableWorkspaceFilesystem")

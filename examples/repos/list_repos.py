from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace

w = WorkspaceClient()

all = w.repos.list(workspace.ListReposRequest())

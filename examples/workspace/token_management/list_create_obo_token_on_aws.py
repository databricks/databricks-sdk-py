from databricks.sdk import WorkspaceClient
from databricks.sdk.service import settings

w = WorkspaceClient()

all = w.token_management.list(settings.ListTokenManagementRequest())

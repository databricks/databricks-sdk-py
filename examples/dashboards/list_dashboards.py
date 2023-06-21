from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

all = w.dashboards.list(sql.ListDashboardsRequest())

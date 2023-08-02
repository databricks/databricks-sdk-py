from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

_ = w.query_history.list(filter_by=sql.QueryFilter(
    query_start_time_range=sql.TimeRange(start_time_ms=1690243200000, end_time_ms=1690329600000)))

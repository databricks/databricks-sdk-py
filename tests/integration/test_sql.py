from datetime import datetime

from databricks.sdk.sql.v2 import sql
from databricks.sdk.sql.v2.client import QueryHistoryClient


def test_query_history_list_with_filter(w):

    def date_to_ms(date):
        return int(datetime.strptime(date, "%Y-%m-%d").timestamp() * 1000)

    qhc = QueryHistoryClient(config=w)

    filter = sql.QueryFilter(
        query_start_time_range=sql.TimeRange(
            start_time_ms=date_to_ms("2023-01-01"),
            end_time_ms=date_to_ms("2023-01-02"),
        )
    )
    queries = qhc.list(filter_by=filter)
    assert queries.res is not None, "Query history result list (queries.res) is None"
    for q in queries.res:
        print(q)

from datetime import datetime

from databricks.sdk.service.sql import QueryFilter, TimeRange


def test_query_history_list_with_filter(w):

    def date_to_ms(date):
        return int(datetime.strptime(date, '%Y-%m-%d').timestamp() * 1000)

    filter = QueryFilter(query_start_time_range=TimeRange(start_time_ms=date_to_ms('2023-01-01'),
                                                          end_time_ms=date_to_ms('2023-01-02')))
    queries = w.query_history.list(filter_by=filter)
    for q in queries.res:
        print(q)

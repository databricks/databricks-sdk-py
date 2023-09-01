import functools
from datetime import datetime

from databricks.sdk.service.sql import QueryFilter, TimeRange


def test_sql_execution(w):
    all_warehouses = w.warehouses.list()
    assert len(w.warehouses.list()) > 0, 'at least one SQL warehouse required'
    warehouse_id = all_warehouses[0].id

    for (pickup_zip, dropoff_zip) in w.statement_execution.execute_fetch_all(
            warehouse_id, 'SELECT pickup_zip, dropoff_zip FROM nyctaxi.trips LIMIT 10', catalog='samples'):
        print(f'pickup_zip={pickup_zip}, dropoff_zip={dropoff_zip}')


def test_sql_execution_partial(w):
    all_warehouses = w.warehouses.list()
    assert len(w.warehouses.list()) > 0, 'at least one SQL warehouse required'
    warehouse_id = all_warehouses[0].id

    run_sql = functools.partial(w.statement_execution.execute_fetch_all, warehouse_id, catalog='samples')
    for row in run_sql('SELECT * FROM nyctaxi.trips LIMIT 10'):
        print(f'pickup_zip={row.pickup_zip}, dropoff_zip={row.dropoff_zip}')


def test_query_history_list_with_filter(w):

    def date_to_ms(date):
        return int(datetime.strptime(date, '%Y-%m-%d').timestamp() * 1000)

    filter = QueryFilter(query_start_time_range=TimeRange(start_time_ms=date_to_ms('2023-01-01'),
                                                          end_time_ms=date_to_ms('2023-01-02')))
    queries = w.query_history.list(filter_by=filter)
    for q in queries:
        print(q)

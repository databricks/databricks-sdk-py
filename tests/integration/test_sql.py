import functools
from datetime import datetime

from databricks.sdk.service.sql import QueryFilter, TimeRange


def test_sql_execution_chunked(w):
    all_warehouses = w.warehouses.list()
    assert len(w.warehouses.list()) > 0, 'at least one SQL warehouse required'
    warehouse_id = all_warehouses[0].id

    total = 0
    fetch = functools.partial(w.statement_execution.iterate_rows, warehouse_id)
    for (x, ) in fetch('SELECT id FROM range(2000000)'):
        total += x
    print(total)


def test_sql_execution(w, env_or_skip):
    warehouse_id = env_or_skip('TEST_DEFAULT_WAREHOUSE_ID')
    for (pickup_zip, dropoff_zip) in w.statement_execution.iterate_rows(
            warehouse_id, 'SELECT pickup_zip, dropoff_zip FROM nyctaxi.trips LIMIT 10', catalog='samples'):
        print(f'pickup_zip={pickup_zip}, dropoff_zip={dropoff_zip}')


def test_sql_execution_partial(w, env_or_skip):
    warehouse_id = env_or_skip('TEST_DEFAULT_WAREHOUSE_ID')
    iterate_rows = functools.partial(w.statement_execution.iterate_rows, warehouse_id, catalog='samples')
    for row in iterate_rows('SELECT * FROM nyctaxi.trips LIMIT 10'):
        pickup_time, dropoff_time = row[0], row[1]
        pickup_zip = row.pickup_zip
        dropoff_zip = row['dropoff_zip']
        all_fields = row.as_dict()
        print(f'{pickup_zip}@{pickup_time} -> {dropoff_zip}@{dropoff_time}: {all_fields}')


def test_query_history_list_with_filter(w):

    def date_to_ms(date):
        return int(datetime.strptime(date, '%Y-%m-%d').timestamp() * 1000)

    filter = QueryFilter(query_start_time_range=TimeRange(start_time_ms=date_to_ms('2023-01-01'),
                                                          end_time_ms=date_to_ms('2023-01-02')))
    queries = w.query_history.list(filter_by=filter)
    for q in queries:
        print(q)

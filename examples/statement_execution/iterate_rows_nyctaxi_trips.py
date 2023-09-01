from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

all_warehouses = w.warehouses.list()
assert len(w.warehouses.list()) > 0, 'at least one SQL warehouse required'
warehouse_id = all_warehouses[0].id

for (pickup_zip, dropoff_zip) in w.statement_execution.iterate_rows(
        warehouse_id, 'SELECT pickup_zip, dropoff_zip FROM nyctaxi.trips LIMIT 10',
        catalog='samples'):
    print(f'pickup_zip={pickup_zip}, dropoff_zip={dropoff_zip}')
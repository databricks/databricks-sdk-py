import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sharing

w = WorkspaceClient()

table_name = f'sdk-{time.time_ns()}'

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)

_ = w.statement_execution.execute(
    warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
    catalog=created_catalog.name,
    schema=created_schema.name,
    statement="CREATE TABLE %s TBLPROPERTIES (delta.enableDeletionVectors=false) AS SELECT 2+2 as four" %
    (table_name)).result()

table_full_name = "%s.%s.%s" % (created_catalog.name, created_schema.name, table_name)

created_share = w.shares.create(name=f'sdk-{time.time_ns()}')

_ = w.shares.update(name=created_share.name,
                    updates=[
                        sharing.SharedDataObjectUpdate(action=sharing.SharedDataObjectUpdateAction.ADD,
                                                       data_object=sharing.SharedDataObject(
                                                           name=table_full_name, data_object_type="TABLE"))
                    ])

# cleanup
w.schemas.delete(full_name=created_schema.full_name)
w.catalogs.delete(name=created_catalog.name, force=True)
w.tables.delete(full_name=table_full_name)
w.shares.delete(name=created_share.name)

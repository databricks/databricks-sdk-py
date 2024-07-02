import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

table_name = f'sdk-{time.time_ns()}'

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)

_ = w.statement_execution.execute(warehouse_id=os.environ["TEST_DEFAULT_WAREHOUSE_ID"],
                                  catalog=created_catalog.name,
                                  schema=created_schema.name,
                                  statement="CREATE TABLE %s AS SELECT 2+2 as four" % (table_name)).result()

table_full_name = "%s.%s.%s" % (created_catalog.name, created_schema.name, table_name)

account_level_group_name = os.environ["TEST_DATA_ENG_GROUP"]

created_table = w.tables.get(full_name=table_full_name)

x = w.grants.update(full_name=created_table.full_name,
                    securable_type=catalog.SecurableType.TABLE,
                    changes=[
                        catalog.PermissionsChange(add=[catalog.Privilege.MODIFY, catalog.Privilege.SELECT],
                                                  principal=account_level_group_name)
                    ])

# cleanup
w.schemas.delete(full_name=created_schema.full_name)
w.catalogs.delete(name=created_catalog.name, force=True)
w.tables.delete(full_name=table_full_name)

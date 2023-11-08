from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

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

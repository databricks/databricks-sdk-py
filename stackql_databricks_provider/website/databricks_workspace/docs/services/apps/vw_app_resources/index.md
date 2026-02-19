---
title: vw_app_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_app_resources
  - apps
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_app_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_app_resources" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.vw_app_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="app_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the app that owns this resource binding.</td>
</tr>
<tr>
    <td><CopyableCode code="app_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the app that owns this resource binding.</td>
</tr>
<tr>
    <td><CopyableCode code="resource_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name used to reference this resource within the app (one row per resource).</td>
</tr>
<tr>
    <td><CopyableCode code="resource_description" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Optional description of the resource binding.</td>
</tr>
<tr>
    <td><CopyableCode code="resource_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Derived resource type - one of JOB, SQL_WAREHOUSE, SERVING_ENDPOINT, SECRET, EXPERIMENT, DATABASE, GENIE_SPACE, UC_SECURABLE, or UNKNOWN.</td>
</tr>
<tr>
    <td><CopyableCode code="job_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the bound Databricks job (JOB type only).</td>
</tr>
<tr>
    <td><CopyableCode code="job_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the job (JOB type only).</td>
</tr>
<tr>
    <td><CopyableCode code="sql_warehouse_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the bound SQL warehouse (SQL_WAREHOUSE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="sql_warehouse_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the SQL warehouse (SQL_WAREHOUSE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="serving_endpoint_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the bound model serving endpoint (SERVING_ENDPOINT type only).</td>
</tr>
<tr>
    <td><CopyableCode code="serving_endpoint_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the serving endpoint (SERVING_ENDPOINT type only).</td>
</tr>
<tr>
    <td><CopyableCode code="secret_scope" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Secret scope containing the bound secret (SECRET type only).</td>
</tr>
<tr>
    <td><CopyableCode code="secret_key" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Key of the bound secret within the scope (SECRET type only).</td>
</tr>
<tr>
    <td><CopyableCode code="secret_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the secret (SECRET type only).</td>
</tr>
<tr>
    <td><CopyableCode code="experiment_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the bound MLflow experiment (EXPERIMENT type only).</td>
</tr>
<tr>
    <td><CopyableCode code="experiment_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the experiment (EXPERIMENT type only).</td>
</tr>
<tr>
    <td><CopyableCode code="database_instance" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Instance name of the bound Databricks database (DATABASE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the bound database (DATABASE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="database_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the database (DATABASE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="genie_space_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the bound Genie space (GENIE_SPACE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="genie_space_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the Genie space (GENIE_SPACE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="uc_securable_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Full name of the bound Unity Catalog securable (UC_SECURABLE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="uc_securable_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of the Unity Catalog securable (e.g. TABLE, SCHEMA, CATALOG) (UC_SECURABLE type only).</td>
</tr>
<tr>
    <td><CopyableCode code="uc_securable_permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the app on the Unity Catalog securable (UC_SECURABLE type only).</td>
</tr>
</tbody>
</table>

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  a.deployment_name,
  a.name AS app_name,
  a.id AS app_id,
  JSON_EXTRACT(r.value, '$.name') AS resource_name,
  JSON_EXTRACT(r.value, '$.description') AS resource_description,
  CASE
    WHEN JSON_EXTRACT(r.value, '$.job') IS NOT NULL THEN 'JOB'
    WHEN JSON_EXTRACT(r.value, '$.sql_warehouse') IS NOT NULL THEN 'SQL_WAREHOUSE'
    WHEN JSON_EXTRACT(r.value, '$.serving_endpoint') IS NOT NULL THEN 'SERVING_ENDPOINT'
    WHEN JSON_EXTRACT(r.value, '$.secret') IS NOT NULL THEN 'SECRET'
    WHEN JSON_EXTRACT(r.value, '$.experiment') IS NOT NULL THEN 'EXPERIMENT'
    WHEN JSON_EXTRACT(r.value, '$.database') IS NOT NULL THEN 'DATABASE'
    WHEN JSON_EXTRACT(r.value, '$.genie_space') IS NOT NULL THEN 'GENIE_SPACE'
    WHEN JSON_EXTRACT(r.value, '$.uc_securable') IS NOT NULL THEN 'UC_SECURABLE'
    ELSE 'UNKNOWN'
  END AS resource_type,
  JSON_EXTRACT(r.value, '$.job.id') AS job_id,
  JSON_EXTRACT(r.value, '$.job.permission') AS job_permission,
  JSON_EXTRACT(r.value, '$.sql_warehouse.id') AS sql_warehouse_id,
  JSON_EXTRACT(r.value, '$.sql_warehouse.permission') AS sql_warehouse_permission,
  JSON_EXTRACT(r.value, '$.serving_endpoint.name') AS serving_endpoint_name,
  JSON_EXTRACT(r.value, '$.serving_endpoint.permission') AS serving_endpoint_permission,
  JSON_EXTRACT(r.value, '$.secret.scope') AS secret_scope,
  JSON_EXTRACT(r.value, '$.secret.key') AS secret_key,
  JSON_EXTRACT(r.value, '$.secret.permission') AS secret_permission,
  JSON_EXTRACT(r.value, '$.experiment.experiment_id') AS experiment_id,
  JSON_EXTRACT(r.value, '$.experiment.permission') AS experiment_permission,
  JSON_EXTRACT(r.value, '$.database.instance_name') AS database_instance,
  JSON_EXTRACT(r.value, '$.database.database_name') AS database_name,
  JSON_EXTRACT(r.value, '$.database.permission') AS database_permission,
  JSON_EXTRACT(r.value, '$.genie_space.space_id') AS genie_space_id,
  JSON_EXTRACT(r.value, '$.genie_space.permission') AS genie_space_permission,
  JSON_EXTRACT(r.value, '$.uc_securable.securable_full_name') AS uc_securable_name,
  JSON_EXTRACT(r.value, '$.uc_securable.securable_type') AS uc_securable_type,
  JSON_EXTRACT(r.value, '$.uc_securable.permission') AS uc_securable_permission
FROM databricks_workspace.apps.apps a,
     JSON_EACH(a.resources) r
WHERE deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  a.deployment_name,
  a.name AS app_name,
  a.id AS app_id,
  r.value->>'name' AS resource_name,
  r.value->>'description' AS resource_description,
  CASE
    WHEN r.value->'job' IS NOT NULL THEN 'JOB'
    WHEN r.value->'sql_warehouse' IS NOT NULL THEN 'SQL_WAREHOUSE'
    WHEN r.value->'serving_endpoint' IS NOT NULL THEN 'SERVING_ENDPOINT'
    WHEN r.value->'secret' IS NOT NULL THEN 'SECRET'
    WHEN r.value->'experiment' IS NOT NULL THEN 'EXPERIMENT'
    WHEN r.value->'database' IS NOT NULL THEN 'DATABASE'
    WHEN r.value->'genie_space' IS NOT NULL THEN 'GENIE_SPACE'
    WHEN r.value->'uc_securable' IS NOT NULL THEN 'UC_SECURABLE'
    ELSE 'UNKNOWN'
  END AS resource_type,
  r.value->'job'->>'id' AS job_id,
  r.value->'job'->>'permission' AS job_permission,
  r.value->'sql_warehouse'->>'id' AS sql_warehouse_id,
  r.value->'sql_warehouse'->>'permission' AS sql_warehouse_permission,
  r.value->'serving_endpoint'->>'name' AS serving_endpoint_name,
  r.value->'serving_endpoint'->>'permission' AS serving_endpoint_permission,
  r.value->'secret'->>'scope' AS secret_scope,
  r.value->'secret'->>'key' AS secret_key,
  r.value->'secret'->>'permission' AS secret_permission,
  r.value->'experiment'->>'experiment_id' AS experiment_id,
  r.value->'experiment'->>'permission' AS experiment_permission,
  r.value->'database'->>'instance_name' AS database_instance,
  r.value->'database'->>'database_name' AS database_name,
  r.value->'database'->>'permission' AS database_permission,
  r.value->'genie_space'->>'space_id' AS genie_space_id,
  r.value->'genie_space'->>'permission' AS genie_space_permission,
  r.value->'uc_securable'->>'securable_full_name' AS uc_securable_name,
  r.value->'uc_securable'->>'securable_type' AS uc_securable_type,
  r.value->'uc_securable'->>'permission' AS uc_securable_permission
FROM databricks_workspace.apps.apps a,
     jsonb_array_elements(a.resources::jsonb) AS r
WHERE deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>

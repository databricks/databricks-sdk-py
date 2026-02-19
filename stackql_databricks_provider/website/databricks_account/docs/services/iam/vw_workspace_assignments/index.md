---
title: vw_workspace_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_workspace_assignments
  - iam
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_workspace_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_workspace_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.vw_workspace_assignments" /></td></tr>
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
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Numeric ID of the workspace used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="principal_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Numeric ID of the principal assigned to the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Display name of the assigned principal.</td>
</tr>
<tr>
    <td><CopyableCode code="user_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username of the assigned principal if the principal is a user.</td>
</tr>
<tr>
    <td><CopyableCode code="group_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Group name of the assigned principal if the principal is a group.</td>
</tr>
<tr>
    <td><CopyableCode code="service_principal_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Application name of the assigned principal if the principal is a service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="permission" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the principal on the workspace (one row per permission, e.g. USER, ADMIN).</td>
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
  wa.account_id,
  wa.workspace_id,
  JSON_EXTRACT(wa.principal, '$.principal_id') AS principal_id,
  JSON_EXTRACT(wa.principal, '$.display_name') AS display_name,
  JSON_EXTRACT(wa.principal, '$.user_name') AS user_name,
  JSON_EXTRACT(wa.principal, '$.group_name') AS group_name,
  JSON_EXTRACT(wa.principal, '$.service_principal_name') AS service_principal_name,
  p.value AS permission
FROM databricks_account.iam.workspace_assignment wa,
     JSON_EACH(wa.permissions) p
WHERE account_id = '{{ account_id }}'
AND workspace_id = '{{ workspace_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  wa.account_id,
  wa.workspace_id,
  (wa.principal->>'principal_id')::bigint AS principal_id,
  wa.principal->>'display_name' AS display_name,
  wa.principal->>'user_name' AS user_name,
  wa.principal->>'group_name' AS group_name,
  wa.principal->>'service_principal_name' AS service_principal_name,
  p.value AS permission
FROM databricks_account.iam.workspace_assignment wa,
     jsonb_array_elements(wa.permissions::jsonb) AS p
WHERE account_id = '{{ account_id }}'
AND workspace_id = '{{ workspace_id }}'
```

</TabItem>
</Tabs>

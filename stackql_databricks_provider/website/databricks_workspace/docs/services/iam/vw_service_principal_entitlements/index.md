---
title: vw_service_principal_entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_service_principal_entitlements
  - iam
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

Creates, updates, deletes, gets or lists a <code>vw_service_principal_entitlements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_service_principal_entitlements" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.vw_service_principal_entitlements" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable display name of the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationId" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Application ID of the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the service principal is active.</td>
</tr>
<tr>
    <td><CopyableCode code="entitlement" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Entitlement granted to the service principal (one row per entitlement, e.g. workspace-access, databricks-sql-access, allow-cluster-create).</td>
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
  sp.deployment_name,
  sp.id,
  sp.displayName,
  sp.applicationId,
  sp.active,
  JSON_EXTRACT(e.value, '$.value') AS entitlement
FROM databricks_workspace.iam.service_principals_v2 sp,
     JSON_EACH(sp.entitlements) e
WHERE sp.deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  sp.deployment_name,
  sp.id,
  sp.displayName,
  sp.applicationId,
  sp.active,
  e.value->>'value' AS entitlement
FROM databricks_workspace.iam.service_principals_v2 sp,
     jsonb_array_elements(sp.entitlements::jsonb) AS e
WHERE sp.deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>

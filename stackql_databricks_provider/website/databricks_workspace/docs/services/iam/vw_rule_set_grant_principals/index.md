---
title: vw_rule_set_grant_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_rule_set_grant_principals
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

Creates, updates, deletes, gets or lists a <code>vw_rule_set_grant_principals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_rule_set_grant_principals" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.vw_rule_set_grant_principals" /></td></tr>
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
    <td><CopyableCode code="rule_set_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Fully qualified name of the rule set used to scope the query (e.g. accounts/accountId/servicePrincipals/spId/ruleSets/default).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ETag of the rule set used to scope the query and for optimistic concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Role granted by this grant rule (one row per principal per role).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Principal granted the role (e.g. users/alice@example.com, groups/analysts).</td>
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
  rs.deployment_name,
  rs.name AS rule_set_name,
  rs.etag,
  JSON_EXTRACT(gr.value, '$.role') AS role,
  pr.value AS principal
FROM databricks_workspace.iam.rule_sets rs,
     JSON_EACH(rs.grant_rules) gr,
     JSON_EACH(JSON_EXTRACT(gr.value, '$.principals')) pr
WHERE rs.deployment_name = '{{ deployment_name }}'
AND rs.name = '{{ name }}'
AND rs.etag = '{{ etag }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  rs.deployment_name,
  rs.name AS rule_set_name,
  rs.etag,
  gr.value->>'role' AS role,
  pr.value AS principal
FROM databricks_workspace.iam.rule_sets rs,
     jsonb_array_elements(rs.grant_rules::jsonb) AS gr,
     jsonb_array_elements((gr.value->'principals')::jsonb) AS pr
WHERE rs.deployment_name = '{{ deployment_name }}'
AND rs.name = '{{ name }}'
AND rs.etag = '{{ etag }}'
```

</TabItem>
</Tabs>

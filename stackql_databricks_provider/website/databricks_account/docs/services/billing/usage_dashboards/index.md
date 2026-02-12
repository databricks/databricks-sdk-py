---
title: usage_dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_dashboards
  - billing
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

Creates, updates, deletes, gets or lists a <code>usage_dashboards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.usage_dashboards" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="usage_dashboards_get"
    values={[
        { label: 'usage_dashboards_get', value: 'usage_dashboards_get' }
    ]}
>
<TabItem value="usage_dashboards_get">

<SchemaTable fields={[
  {
    "name": "dashboard_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "dashboard_url",
    "type": "string",
    "description": "The URL of the usage dashboard."
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#usage_dashboards_get"><CopyableCode code="usage_dashboards_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-dashboard_type"><code>dashboard_type</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td>Get a usage dashboard specified by workspaceId, accountId, and dashboard type.</td>
</tr>
<tr>
    <td><a href="#usage_dashboards_create"><CopyableCode code="usage_dashboards_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create a usage dashboard specified by workspaceId, accountId, and dashboard type.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-dashboard_type">
    <td><CopyableCode code="dashboard_type" /></td>
    <td><code>string</code></td>
    <td>Workspace level usage dashboard shows usage data for the specified workspace ID. Global level usage dashboard shows usage data for all workspaces in the account.</td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>string</code></td>
    <td>The workspace ID of the workspace in which the usage dashboard is created.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="usage_dashboards_get"
    values={[
        { label: 'usage_dashboards_get', value: 'usage_dashboards_get' }
    ]}
>
<TabItem value="usage_dashboards_get">

Get a usage dashboard specified by workspaceId, accountId, and dashboard type.

```sql
SELECT
dashboard_id,
dashboard_url
FROM databricks_account.billing.usage_dashboards
WHERE account_id = '{{ account_id }}' -- required
AND dashboard_type = '{{ dashboard_type }}'
AND workspace_id = '{{ workspace_id }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="usage_dashboards_create"
    values={[
        { label: 'usage_dashboards_create', value: 'usage_dashboards_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="usage_dashboards_create">

Create a usage dashboard specified by workspaceId, accountId, and dashboard type.

```sql
INSERT INTO databricks_account.billing.usage_dashboards (
data__dashboard_type,
data__major_version,
data__workspace_id,
account_id
)
SELECT 
'{{ dashboard_type }}',
'{{ major_version }}',
'{{ workspace_id }}',
'{{ account_id }}'
RETURNING
dashboard_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: usage_dashboards
  props:
    - name: account_id
      value: string
      description: Required parameter for the usage_dashboards resource.
    - name: dashboard_type
      value: string
      description: |
        Workspace level usage dashboard shows usage data for the specified workspace ID. Global level usage dashboard shows usage data for all workspaces in the account.
    - name: major_version
      value: string
      description: |
        The major version of the usage dashboard template to use. Defaults to VERSION_1.
    - name: workspace_id
      value: string
      description: |
        The workspace ID of the workspace in which the usage dashboard is created.
```
</TabItem>
</Tabs>

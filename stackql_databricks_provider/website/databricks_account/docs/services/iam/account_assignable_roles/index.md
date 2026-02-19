---
title: account_assignable_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - account_assignable_roles
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

Creates, updates, deletes, gets or lists an <code>account_assignable_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_assignable_roles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.account_assignable_roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_assignable_roles_for_resource"
    values={[
        { label: 'get_assignable_roles_for_resource', value: 'get_assignable_roles_for_resource' }
    ]}
>
<TabItem value="get_assignable_roles_for_resource">

<SchemaTable fields={[
  {
    "name": "roles",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
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
    <td><a href="#get_assignable_roles_for_resource"><CopyableCode code="get_assignable_roles_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-resource"><code>resource</code></a></td>
    <td></td>
    <td>Gets all the roles that can be granted on an account level resource. A role is grantable if the rule</td>
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
<tr id="parameter-resource">
    <td><CopyableCode code="resource" /></td>
    <td><code>string</code></td>
    <td>The resource name for which assignable roles will be listed. Examples | Summary :--- | :--- `resource=accounts/<ACCOUNT_ID>` | A resource name for the account. `resource=accounts/<ACCOUNT_ID>/groups/<GROUP_ID>` | A resource name for the group. `resource=accounts/<ACCOUNT_ID>/servicePrincipals/<SP_ID>` | A resource name for the service principal. `resource=accounts/<ACCOUNT_ID>/tagPolicies/<TAG_POLICY_ID>` | A resource name for the tag policy.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_assignable_roles_for_resource"
    values={[
        { label: 'get_assignable_roles_for_resource', value: 'get_assignable_roles_for_resource' }
    ]}
>
<TabItem value="get_assignable_roles_for_resource">

Gets all the roles that can be granted on an account level resource. A role is grantable if the rule

```sql
SELECT
roles
FROM databricks_account.iam.account_assignable_roles
WHERE account_id = '{{ account_id }}' -- required
AND resource = '{{ resource }}' -- required
;
```
</TabItem>
</Tabs>

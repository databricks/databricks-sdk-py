---
title: recipient_share_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - recipient_share_permissions
  - sharing
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

Creates, updates, deletes, gets or lists a <code>recipient_share_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recipient_share_permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.recipient_share_permissions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "next_page_token",
    "type": "string",
    "description": ""
  },
  {
    "name": "permissions_out",
    "type": "array",
    "description": "An array of data share permissions for a recipient.",
    "children": [
      {
        "name": "privilege_assignments",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "principal",
            "type": "string",
            "description": ""
          },
          {
            "name": "privileges",
            "type": "array",
            "description": "The privileges assigned to the principal."
          }
        ]
      },
      {
        "name": "share_name",
        "type": "string",
        "description": "The share name."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets the share permissions for the specified Recipient. The caller must have the **USE_RECIPIENT**</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Recipient.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of permissions to return. - when set to 0, the page length is set to a server configured value (recommended); - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to a value less than 0, an invalid parameter error is returned; - If not set, all valid permissions are returned (not recommended). - Note: The number of returned permissions might be less than the specified max_results size, even zero. The only definitive indication that no further permissions can be fetched is when the next_page_token is unset from the response.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets the share permissions for the specified Recipient. The caller must have the **USE_RECIPIENT**

```sql
SELECT
next_page_token,
permissions_out
FROM databricks_workspace.sharing.recipient_share_permissions
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

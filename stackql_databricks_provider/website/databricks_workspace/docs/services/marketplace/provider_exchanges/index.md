---
title: provider_exchanges
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_exchanges
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>provider_exchanges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_exchanges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_exchanges" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "exchange",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "comment",
        "type": "string",
        "description": ""
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "created_by",
        "type": "string",
        "description": ""
      },
      {
        "name": "filters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "exchange_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "filter_value",
            "type": "string",
            "description": ""
          },
          {
            "name": "filter_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          },
          {
            "name": "created_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "created_by",
            "type": "string",
            "description": ""
          },
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "updated_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "updated_by",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "linked_listings",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "created_at",
            "type": "integer",
            "description": ""
          },
          {
            "name": "created_by",
            "type": "string",
            "description": ""
          },
          {
            "name": "exchange_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "exchange_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "listing_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "listing_name",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "string",
    "description": ""
  },
  {
    "name": "filters",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "exchange_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "filter_value",
        "type": "string",
        "description": ""
      },
      {
        "name": "filter_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "created_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "created_by",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "updated_by",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "linked_listings",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "created_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "created_by",
        "type": "string",
        "description": ""
      },
      {
        "name": "exchange_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "exchange_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "listing_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "listing_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": ""
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get an exchange.<br /><br />:param id: str<br /><br />:returns: :class:`GetExchangeResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List exchanges visible to provider<br /><br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`Exchange`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__exchange"><code>data__exchange</code></a></td>
    <td></td>
    <td>Create an exchange<br /><br />:param exchange: :class:`Exchange`<br /><br />:returns: :class:`CreateExchangeResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__exchange"><code>data__exchange</code></a></td>
    <td></td>
    <td>Update an exchange<br /><br />:param id: str<br />:param exchange: :class:`Exchange`<br /><br />:returns: :class:`UpdateExchangeResponse`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This removes a listing from marketplace.<br /><br />:param id: str</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>:param page_token: str (optional)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get an exchange.<br /><br />:param id: str<br /><br />:returns: :class:`GetExchangeResponse`

```sql
SELECT
exchange
FROM databricks_workspace.marketplace.provider_exchanges
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List exchanges visible to provider<br /><br />:param page_size: int (optional)<br />:param page_token: str (optional)<br /><br />:returns: Iterator over :class:`Exchange`

```sql
SELECT
id,
name,
comment,
created_at,
created_by,
filters,
linked_listings,
updated_at,
updated_by
FROM databricks_workspace.marketplace.provider_exchanges
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create an exchange<br /><br />:param exchange: :class:`Exchange`<br /><br />:returns: :class:`CreateExchangeResponse`

```sql
INSERT INTO databricks_workspace.marketplace.provider_exchanges (
data__exchange,
deployment_name
)
SELECT 
'{{ exchange }}' /* required */,
'{{ deployment_name }}'
RETURNING
exchange_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: provider_exchanges
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the provider_exchanges resource.
    - name: exchange
      value: string
      description: |
        :returns: :class:`CreateExchangeResponse`
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an exchange<br /><br />:param id: str<br />:param exchange: :class:`Exchange`<br /><br />:returns: :class:`UpdateExchangeResponse`

```sql
REPLACE databricks_workspace.marketplace.provider_exchanges
SET 
data__exchange = '{{ exchange }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__exchange = '{{ exchange }}' --required
RETURNING
exchange;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

This removes a listing from marketplace.<br /><br />:param id: str

```sql
DELETE FROM databricks_workspace.marketplace.provider_exchanges
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

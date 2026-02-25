---
title: provider_exchange_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_exchange_listings
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>provider_exchange_listings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_exchange_listings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_exchange_listings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_for_listing"
    values={[
        { label: 'list_for_listing', value: 'list_for_listing' },
        { label: 'list_for_exchange', value: 'list_for_exchange' }
    ]}
>
<TabItem value="list_for_listing">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "exchange_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "listing_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "exchange_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "listing_name",
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
  }
]} />
</TabItem>
<TabItem value="list_for_exchange">

<SchemaTable fields={[]} />
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
    <td><a href="#list_for_listing"><CopyableCode code="list_for_listing" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List exchanges associated with a listing</td>
</tr>
<tr>
    <td><a href="#list_for_exchange"><CopyableCode code="list_for_exchange" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-exchange_id"><code>exchange_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List listings associated with an exchange</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-listing_id"><code>listing_id</code></a>, <a href="#parameter-exchange_id"><code>exchange_id</code></a></td>
    <td></td>
    <td>Associate an exchange with a listing</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Disassociate an exchange with a listing</td>
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
<tr id="parameter-exchange_id">
    <td><CopyableCode code="exchange_id" /></td>
    <td><code>string</code></td>
    <td>:param page_size: int (optional)</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-listing_id">
    <td><CopyableCode code="listing_id" /></td>
    <td><code>string</code></td>
    <td>:param page_size: int (optional)</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>:returns: Iterator over :class:`ExchangeListing`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_for_listing"
    values={[
        { label: 'list_for_listing', value: 'list_for_listing' },
        { label: 'list_for_exchange', value: 'list_for_exchange' }
    ]}
>
<TabItem value="list_for_listing">

List exchanges associated with a listing

```sql
SELECT
id,
exchange_id,
listing_id,
exchange_name,
listing_name,
created_at,
created_by
FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE listing_id = '{{ listing_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="list_for_exchange">

List listings associated with an exchange

```sql
SELECT
*
FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE exchange_id = '{{ exchange_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="add">

Associate an exchange with a listing

```sql
INSERT INTO databricks_workspace.marketplace.provider_exchange_listings (
listing_id,
exchange_id,
workspace
)
SELECT 
'{{ listing_id }}' /* required */,
'{{ exchange_id }}' /* required */,
'{{ workspace }}'
RETURNING
exchange_for_listing
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: provider_exchange_listings
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the provider_exchange_listings resource.
    - name: listing_id
      value: "{{ listing_id }}"
      description: |
        :param exchange_id: str
    - name: exchange_id
      value: "{{ exchange_id }}"
`}</CodeBlock>

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

Disassociate an exchange with a listing

```sql
DELETE FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE id = '{{ id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

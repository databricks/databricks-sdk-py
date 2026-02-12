---
title: system_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - system_schemas
  - catalog
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

Creates, updates, deletes, gets or lists a <code>system_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>system_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.system_schemas" /></td></tr>
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
    "name": "schema",
    "type": "string",
    "description": ""
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current state of enablement for the system schema. An empty string means the system schema is available and ready for opt-in. Possible values: AVAILABLE | ENABLE_INITIALIZED | ENABLE_COMPLETED | DISABLE_INITIALIZED | UNAVAILABLE | MANAGED"
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
    <td><a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of system schemas for a metastore. The caller must be an account admin or a metastore</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Enables the system schema and adds it to the system catalog. The caller must be an account admin or a</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Disables the system schema and removes it from the system catalog. The caller must be an account admin</td>
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
<tr id="parameter-metastore_id">
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td>The metastore ID under which the system schema lives.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Full name of the system schema.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of schemas to return. - When set to 0, the page length is set to a server configured value (recommended); - When set to a value greater than 0, the page length is the minimum of this value and a server configured value; - When set to a value less than 0, an invalid parameter error is returned; - If not set, all the schemas are returned (not recommended).</td>
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

Gets an array of system schemas for a metastore. The caller must be an account admin or a metastore

```sql
SELECT
schema,
state
FROM databricks_workspace.catalog.system_schemas
WHERE metastore_id = '{{ metastore_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="enable"
    values={[
        { label: 'enable', value: 'enable' }
    ]}
>
<TabItem value="enable">

Enables the system schema and adds it to the system catalog. The caller must be an account admin or a

```sql
REPLACE databricks_workspace.catalog.system_schemas
SET 
data__catalog_name = '{{ catalog_name }}'
WHERE 
metastore_id = '{{ metastore_id }}' --required
AND schema_name = '{{ schema_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="disable"
    values={[
        { label: 'disable', value: 'disable' }
    ]}
>
<TabItem value="disable">

Disables the system schema and removes it from the system catalog. The caller must be an account admin

```sql
DELETE FROM databricks_workspace.catalog.system_schemas
WHERE metastore_id = '{{ metastore_id }}' --required
AND schema_name = '{{ schema_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

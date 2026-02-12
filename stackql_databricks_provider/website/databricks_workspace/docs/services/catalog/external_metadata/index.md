---
title: external_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - external_metadata
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

Creates, updates, deletes, gets or lists an <code>external_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.external_metadata" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Unique identifier of the external metadata object."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "columns",
    "type": "array",
    "description": "List of columns associated with the external metadata object."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "Time at which this external metadata object was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of external metadata object creator."
  },
  {
    "name": "description",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "entity_type",
    "type": "string",
    "description": "Type of entity within the external system."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Owner of the external metadata object."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the external metadata object."
  },
  {
    "name": "system_type",
    "type": "string",
    "description": "Type of external system."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Time at which this external metadata object was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified external metadata object."
  },
  {
    "name": "url",
    "type": "string",
    "description": "URL associated with the external metadata object."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Unique identifier of the external metadata object."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "columns",
    "type": "array",
    "description": "List of columns associated with the external metadata object."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "Time at which this external metadata object was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of external metadata object creator."
  },
  {
    "name": "description",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "entity_type",
    "type": "string",
    "description": "Type of entity within the external system."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Owner of the external metadata object."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the external metadata object."
  },
  {
    "name": "system_type",
    "type": "string",
    "description": "Type of external system."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Time at which this external metadata object was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified external metadata object."
  },
  {
    "name": "url",
    "type": "string",
    "description": "URL associated with the external metadata object."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the specified external metadata object in a metastore. The caller must be a metastore admin, the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of external metadata objects in the metastore. If the caller is the metastore admin, all</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__external_metadata"><code>data__external_metadata</code></a></td>
    <td></td>
    <td>Creates a new external metadata object in the parent metastore if the caller is a metastore admin or</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__external_metadata"><code>data__external_metadata</code></a></td>
    <td></td>
    <td>Updates the external metadata object that matches the supplied name. The caller can only update either</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the external metadata object that matches the supplied name. The caller must be a metastore</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>str</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum number of external metadata objects to return in a single response. The value must be less than or equal to 1000.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified external metadata object in a metastore. The caller must be a metastore admin, the

```sql
SELECT
id,
name,
metastore_id,
columns,
create_time,
created_by,
description,
entity_type,
owner,
properties,
system_type,
update_time,
updated_by,
url
FROM databricks_workspace.catalog.external_metadata
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets an array of external metadata objects in the metastore. If the caller is the metastore admin, all

```sql
SELECT
id,
name,
metastore_id,
columns,
create_time,
created_by,
description,
entity_type,
owner,
properties,
system_type,
update_time,
updated_by,
url
FROM databricks_workspace.catalog.external_metadata
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

Creates a new external metadata object in the parent metastore if the caller is a metastore admin or

```sql
INSERT INTO databricks_workspace.catalog.external_metadata (
data__external_metadata,
deployment_name
)
SELECT 
'{{ external_metadata }}' /* required */,
'{{ deployment_name }}'
RETURNING
id,
name,
metastore_id,
columns,
create_time,
created_by,
description,
entity_type,
owner,
properties,
system_type,
update_time,
updated_by,
url
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: external_metadata
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the external_metadata resource.
    - name: external_metadata
      value: string
      description: |
        :returns: :class:`ExternalMetadata`
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the external metadata object that matches the supplied name. The caller can only update either

```sql
UPDATE databricks_workspace.catalog.external_metadata
SET 
data__external_metadata = '{{ external_metadata }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__external_metadata = '{{ external_metadata }}' --required
RETURNING
id,
name,
metastore_id,
columns,
create_time,
created_by,
description,
entity_type,
owner,
properties,
system_type,
update_time,
updated_by,
url;
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

Deletes the external metadata object that matches the supplied name. The caller must be a metastore

```sql
DELETE FROM databricks_workspace.catalog.external_metadata
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

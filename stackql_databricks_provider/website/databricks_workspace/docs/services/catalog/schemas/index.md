---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schemas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.schemas" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "Name of schema, relative to parent catalog."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "schema_id",
    "type": "string",
    "description": "The unique identifier of the schema."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent catalog."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of schema, in form of __catalog_name__.__schema_name__."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "catalog_type",
    "type": "string",
    "description": "The type of the catalog. (DELTASHARING_CATALOG, FOREIGN_CATALOG, INTERNAL_CATALOG, MANAGED_CATALOG, MANAGED_ONLINE_CATALOG, SYSTEM_CATALOG)"
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this schema was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of schema creator."
  },
  {
    "name": "effective_predictive_optimization_flag",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank. (CATALOG, SCHEMA)"
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of schema."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage location for managed tables within schema."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "Storage root URL for managed tables within schema."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this schema was created, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified schema."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of schema, relative to parent catalog."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "schema_id",
    "type": "string",
    "description": "The unique identifier of the schema."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent catalog."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of schema, in form of __catalog_name__.__schema_name__."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "catalog_type",
    "type": "string",
    "description": "The type of the catalog. (DELTASHARING_CATALOG, FOREIGN_CATALOG, INTERNAL_CATALOG, MANAGED_CATALOG, MANAGED_ONLINE_CATALOG, SYSTEM_CATALOG)"
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this schema was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of schema creator."
  },
  {
    "name": "effective_predictive_optimization_flag",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank. (CATALOG, SCHEMA)"
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLE, ENABLE, INHERIT)"
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of schema."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage location for managed tables within schema."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "Storage root URL for managed tables within schema."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this schema was created, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified schema."
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
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Gets the specified schema within the metastore. The caller must be a metastore admin, the owner of the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of schemas for a catalog in the metastore. If the caller is the metastore admin or the</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a></td>
    <td></td>
    <td>Creates a new schema for catalog in the Metastore. The caller must be a metastore admin, or have the</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a schema for a catalog. The caller must be the owner of the schema or a metastore admin. If</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes the specified schema from the parent catalog. The caller must be the owner of the schema or an</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Parent catalog for schemas of interest.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of the schema.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force deletion even if the schema is not empty.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>string</code></td>
    <td>Whether to include schemas in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of schemas to return. If not set, all the schemas are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
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

Gets the specified schema within the metastore. The caller must be a metastore admin, the owner of the

```sql
SELECT
name,
metastore_id,
schema_id,
catalog_name,
full_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
owner,
properties,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.catalog.schemas
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of schemas for a catalog in the metastore. If the caller is the metastore admin or the

```sql
SELECT
name,
metastore_id,
schema_id,
catalog_name,
full_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
owner,
properties,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.catalog.schemas
WHERE catalog_name = '{{ catalog_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND max_results = '{{ max_results }}'
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

Creates a new schema for catalog in the Metastore. The caller must be a metastore admin, or have the

```sql
INSERT INTO databricks_workspace.catalog.schemas (
name,
catalog_name,
comment,
properties,
storage_root,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ catalog_name }}' /* required */,
'{{ comment }}',
'{{ properties }}',
'{{ storage_root }}',
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
schema_id,
catalog_name,
full_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
owner,
properties,
storage_location,
storage_root,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: schemas
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the schemas resource.
    - name: name
      value: string
      description: |
        Name of schema, relative to parent catalog.
    - name: catalog_name
      value: string
      description: |
        Name of parent catalog.
    - name: comment
      value: string
      description: |
        User-provided free-form text description.
    - name: properties
      value: string
      description: |
        A map of key-value properties attached to the securable.
    - name: storage_root
      value: string
      description: |
        Storage root URL for managed tables within schema.
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

Updates a schema for a catalog. The caller must be the owner of the schema or a metastore admin. If

```sql
UPDATE databricks_workspace.catalog.schemas
SET 
comment = '{{ comment }}',
enable_predictive_optimization = '{{ enable_predictive_optimization }}',
new_name = '{{ new_name }}',
owner = '{{ owner }}',
properties = '{{ properties }}'
WHERE 
full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
metastore_id,
schema_id,
catalog_name,
full_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
owner,
properties,
storage_location,
storage_root,
updated_at,
updated_by;
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

Deletes the specified schema from the parent catalog. The caller must be the owner of the schema or an

```sql
DELETE FROM databricks_workspace.catalog.schemas
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

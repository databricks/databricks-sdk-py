---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.connections" /></td></tr>
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
    "description": "Name of the connection."
  },
  {
    "name": "connection_id",
    "type": "string",
    "description": "Unique identifier of the Connection."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of connection."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "connection_type",
    "type": "string",
    "description": "The type of connection."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this connection was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of connection creator."
  },
  {
    "name": "credential_type",
    "type": "string",
    "description": "The type of credential."
  },
  {
    "name": "options",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of the connection."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "provisioning_info",
    "type": "object",
    "description": "Status of an asynchronously provisioned resource.",
    "children": [
      {
        "name": "state",
        "type": "string",
        "description": "The provisioning state of the resource."
      }
    ]
  },
  {
    "name": "read_only",
    "type": "boolean",
    "description": "If the connection is read only."
  },
  {
    "name": "securable_type",
    "type": "string",
    "description": "The type of Unity Catalog securable."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this connection was updated, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified connection."
  },
  {
    "name": "url",
    "type": "string",
    "description": "URL of the remote data source, extracted from options."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the connection."
  },
  {
    "name": "connection_id",
    "type": "string",
    "description": "Unique identifier of the Connection."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of connection."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "connection_type",
    "type": "string",
    "description": "The type of connection."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this connection was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of connection creator."
  },
  {
    "name": "credential_type",
    "type": "string",
    "description": "The type of credential."
  },
  {
    "name": "options",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of the connection."
  },
  {
    "name": "properties",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "provisioning_info",
    "type": "object",
    "description": "Status of an asynchronously provisioned resource.",
    "children": [
      {
        "name": "state",
        "type": "string",
        "description": "The provisioning state of the resource."
      }
    ]
  },
  {
    "name": "read_only",
    "type": "boolean",
    "description": "If the connection is read only."
  },
  {
    "name": "securable_type",
    "type": "string",
    "description": "The type of Unity Catalog securable."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this connection was updated, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified connection."
  },
  {
    "name": "url",
    "type": "string",
    "description": "URL of the remote data source, extracted from options."
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
    <td>Gets a connection from it's name.<br /><br />:param name: str<br />  Name of the connection.<br /><br />:returns: :class:`ConnectionInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all connections.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param max_results: int (optional)<br />  Maximum number of connections to return. - If not set, all connections are returned (not<br />  recommended). - when set to a value greater than 0, the page length is the minimum of this value and<br />  a server configured value; - when set to 0, the page length is set to a server configured value<br />  (recommended); - when set to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`ConnectionInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__connection_type"><code>data__connection_type</code></a>, <a href="#parameter-data__options"><code>data__options</code></a></td>
    <td></td>
    <td>Creates a new connection<br /><br />Creates a new connection to an external data source. It allows users to specify connection details and<br />configurations for interaction with the external server.<br /><br />:param name: str<br />  Name of the connection.<br />:param connection_type: :class:`ConnectionType`<br />  The type of connection.<br />:param options: Dict[str,str]<br />  A map of key-value properties attached to the securable.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param read_only: bool (optional)<br />  If the connection is read only.<br /><br />:returns: :class:`ConnectionInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__options"><code>data__options</code></a></td>
    <td></td>
    <td>Updates the connection that matches the supplied name.<br /><br />:param name: str<br />  Name of the connection.<br />:param options: Dict[str,str]<br />  A map of key-value properties attached to the securable.<br />:param new_name: str (optional)<br />  New name for the connection.<br />:param owner: str (optional)<br />  Username of current owner of the connection.<br /><br />:returns: :class:`ConnectionInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the connection that matches the supplied name.<br /><br />:param name: str<br />  The name of the connection to be deleted.</td>
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
    <td>The name of the connection to be deleted.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of connections to return. - If not set, all connections are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
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

Gets a connection from it's name.<br /><br />:param name: str<br />  Name of the connection.<br /><br />:returns: :class:`ConnectionInfo`

```sql
SELECT
name,
connection_id,
metastore_id,
full_name,
comment,
connection_type,
created_at,
created_by,
credential_type,
options,
owner,
properties,
provisioning_info,
read_only,
securable_type,
updated_at,
updated_by,
url
FROM databricks_workspace.catalog.connections
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all connections.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param max_results: int (optional)<br />  Maximum number of connections to return. - If not set, all connections are returned (not<br />  recommended). - when set to a value greater than 0, the page length is the minimum of this value and<br />  a server configured value; - when set to 0, the page length is set to a server configured value<br />  (recommended); - when set to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`ConnectionInfo`

```sql
SELECT
name,
connection_id,
metastore_id,
full_name,
comment,
connection_type,
created_at,
created_by,
credential_type,
options,
owner,
properties,
provisioning_info,
read_only,
securable_type,
updated_at,
updated_by,
url
FROM databricks_workspace.catalog.connections
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new connection<br /><br />Creates a new connection to an external data source. It allows users to specify connection details and<br />configurations for interaction with the external server.<br /><br />:param name: str<br />  Name of the connection.<br />:param connection_type: :class:`ConnectionType`<br />  The type of connection.<br />:param options: Dict[str,str]<br />  A map of key-value properties attached to the securable.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param read_only: bool (optional)<br />  If the connection is read only.<br /><br />:returns: :class:`ConnectionInfo`

```sql
INSERT INTO databricks_workspace.catalog.connections (
data__name,
data__connection_type,
data__options,
data__comment,
data__properties,
data__read_only,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ connection_type }}' /* required */,
'{{ options }}' /* required */,
'{{ comment }}',
'{{ properties }}',
'{{ read_only }}',
'{{ deployment_name }}'
RETURNING
name,
connection_id,
metastore_id,
full_name,
comment,
connection_type,
created_at,
created_by,
credential_type,
options,
owner,
properties,
provisioning_info,
read_only,
securable_type,
updated_at,
updated_by,
url
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: connections
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the connections resource.
    - name: name
      value: string
      description: |
        Name of the connection.
    - name: connection_type
      value: string
      description: |
        The type of connection.
    - name: options
      value: string
      description: |
        A map of key-value properties attached to the securable.
    - name: comment
      value: string
      description: |
        User-provided free-form text description.
    - name: properties
      value: string
      description: |
        A map of key-value properties attached to the securable.
    - name: read_only
      value: string
      description: |
        If the connection is read only.
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

Updates the connection that matches the supplied name.<br /><br />:param name: str<br />  Name of the connection.<br />:param options: Dict[str,str]<br />  A map of key-value properties attached to the securable.<br />:param new_name: str (optional)<br />  New name for the connection.<br />:param owner: str (optional)<br />  Username of current owner of the connection.<br /><br />:returns: :class:`ConnectionInfo`

```sql
UPDATE databricks_workspace.catalog.connections
SET 
data__options = '{{ options }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__options = '{{ options }}' --required
RETURNING
name,
connection_id,
metastore_id,
full_name,
comment,
connection_type,
created_at,
created_by,
credential_type,
options,
owner,
properties,
provisioning_info,
read_only,
securable_type,
updated_at,
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

Deletes the connection that matches the supplied name.<br /><br />:param name: str<br />  The name of the connection to be deleted.

```sql
DELETE FROM databricks_workspace.catalog.connections
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

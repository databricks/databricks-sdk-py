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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connections" /></td></tr>
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
    "description": "The type of connection. (BIGQUERY, DATABRICKS, GA4_RAW_DATA, GLUE, HIVE_METASTORE, HTTP, MYSQL, ORACLE, POSTGRESQL, POWER_BI, REDSHIFT, SALESFORCE, SALESFORCE_DATA_CLOUD, SERVICENOW, SNOWFLAKE, SQLDW, SQLSERVER, TERADATA, UNKNOWN_CONNECTION_TYPE, WORKDAY_RAAS)"
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
    "description": "The type of credential. (ANY_STATIC_CREDENTIAL, BEARER_TOKEN, OAUTH_ACCESS_TOKEN, OAUTH_M2M, OAUTH_MTLS, OAUTH_REFRESH_TOKEN, OAUTH_RESOURCE_OWNER_PASSWORD, OAUTH_U2M, OAUTH_U2M_MAPPING, OIDC_TOKEN, PEM_PRIVATE_KEY, SERVICE_CREDENTIAL, SSWS_TOKEN, UNKNOWN_CREDENTIAL_TYPE, USERNAME_PASSWORD)"
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
        "description": "The provisioning state of the resource. (ACTIVE, DEGRADED, DELETING, FAILED, PROVISIONING, UPDATING)"
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
    "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
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
    "description": "The type of connection. (BIGQUERY, DATABRICKS, GA4_RAW_DATA, GLUE, HIVE_METASTORE, HTTP, MYSQL, ORACLE, POSTGRESQL, POWER_BI, REDSHIFT, SALESFORCE, SALESFORCE_DATA_CLOUD, SERVICENOW, SNOWFLAKE, SQLDW, SQLSERVER, TERADATA, UNKNOWN_CONNECTION_TYPE, WORKDAY_RAAS)"
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
    "description": "The type of credential. (ANY_STATIC_CREDENTIAL, BEARER_TOKEN, OAUTH_ACCESS_TOKEN, OAUTH_M2M, OAUTH_MTLS, OAUTH_REFRESH_TOKEN, OAUTH_RESOURCE_OWNER_PASSWORD, OAUTH_U2M, OAUTH_U2M_MAPPING, OIDC_TOKEN, PEM_PRIVATE_KEY, SERVICE_CREDENTIAL, SSWS_TOKEN, UNKNOWN_CREDENTIAL_TYPE, USERNAME_PASSWORD)"
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
        "description": "The provisioning state of the resource. (ACTIVE, DEGRADED, DELETING, FAILED, PROVISIONING, UPDATING)"
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
    "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets a connection from it's name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all connections.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-connection_type"><code>connection_type</code></a>, <a href="#parameter-options"><code>options</code></a></td>
    <td></td>
    <td>Creates a new connection</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-options"><code>options</code></a></td>
    <td></td>
    <td>Updates the connection that matches the supplied name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes the connection that matches the supplied name.</td>
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
    <td>The name of the connection to be deleted.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
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

Gets a connection from it's name.

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
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all connections.

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
WHERE workspace = '{{ workspace }}' -- required
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

Creates a new connection

```sql
INSERT INTO databricks_workspace.catalog.connections (
name,
connection_type,
options,
comment,
properties,
read_only,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ connection_type }}' /* required */,
'{{ options }}' /* required */,
'{{ comment }}',
'{{ properties }}',
{{ read_only }},
'{{ workspace }}'
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

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: connections
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the connections resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the connection.
    - name: connection_type
      value: "{{ connection_type }}"
      description: |
        The type of connection.
    - name: options
      value: "{{ options }}"
      description: |
        A map of key-value properties attached to the securable.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided free-form text description.
    - name: properties
      value: "{{ properties }}"
      description: |
        A map of key-value properties attached to the securable.
    - name: read_only
      value: {{ read_only }}
      description: |
        If the connection is read only.
`}</CodeBlock>

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

Updates the connection that matches the supplied name.

```sql
UPDATE databricks_workspace.catalog.connections
SET 
options = '{{ options }}',
new_name = '{{ new_name }}',
owner = '{{ owner }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND options = '{{ options }}' --required
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

Deletes the connection that matches the supplied name.

```sql
DELETE FROM databricks_workspace.catalog.connections
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

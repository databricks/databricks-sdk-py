---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
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

Creates, updates, deletes, gets or lists a <code>catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.catalogs" /></td></tr>
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
    "description": "Name of catalog."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "connection_name",
    "type": "string",
    "description": "The name of the connection to an external data source."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The full name of the catalog. Corresponds with the name field."
  },
  {
    "name": "provider_name",
    "type": "string",
    "description": "The name of delta sharing provider. A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server."
  },
  {
    "name": "share_name",
    "type": "string",
    "description": "The name of the share under the share provider."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "catalog_type",
    "type": "string",
    "description": "The type of the catalog."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this catalog was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of catalog creator."
  },
  {
    "name": "effective_predictive_optimization_flag",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "isolation_mode",
    "type": "string",
    "description": "Whether the current securable is accessible from all workspaces or a specific set of workspaces."
  },
  {
    "name": "options",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of catalog."
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
    "name": "securable_type",
    "type": "string",
    "description": "The type of Unity Catalog securable."
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage Location URL (full path) for managed tables within catalog."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "Storage root URL for managed tables within catalog."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this catalog was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified catalog."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of catalog."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "connection_name",
    "type": "string",
    "description": "The name of the connection to an external data source."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The full name of the catalog. Corresponds with the name field."
  },
  {
    "name": "provider_name",
    "type": "string",
    "description": "The name of delta sharing provider. A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server."
  },
  {
    "name": "share_name",
    "type": "string",
    "description": "The name of the share under the share provider."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "catalog_type",
    "type": "string",
    "description": "The type of the catalog."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this catalog was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of catalog creator."
  },
  {
    "name": "effective_predictive_optimization_flag",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      },
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": "The name of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of the object from which the flag was inherited. If there was no inheritance, this field is left blank."
      }
    ]
  },
  {
    "name": "enable_predictive_optimization",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
  },
  {
    "name": "isolation_mode",
    "type": "string",
    "description": "Whether the current securable is accessible from all workspaces or a specific set of workspaces."
  },
  {
    "name": "options",
    "type": "object",
    "description": "A map of key-value properties attached to the securable."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of catalog."
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
    "name": "securable_type",
    "type": "string",
    "description": "The type of Unity Catalog securable."
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage Location URL (full path) for managed tables within catalog."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "Storage root URL for managed tables within catalog."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this catalog was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified catalog."
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
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the<br />catalog, or a user that has the **USE_CATALOG** privilege set for their account.<br /><br />:param name: str<br />  The name of the catalog.<br />:param include_browse: bool (optional)<br />  Whether to include catalogs in the response for which the principal can only access selective<br />  metadata for<br /><br />:returns: :class:`CatalogInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-include_unbound"><code>include_unbound</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be<br />retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the<br />**USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the<br />elements in the array.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param include_browse: bool (optional)<br />  Whether to include catalogs in the response for which the principal can only access selective<br />  metadata for<br />:param include_unbound: bool (optional)<br />  Whether to include catalogs not bound to the workspace. Effective only if the user has permission to<br />  update the catalog–workspace binding.<br />:param max_results: int (optional)<br />  Maximum number of catalogs to return. - when set to 0, the page length is set to a server configured<br />  value (recommended); - when set to a value greater than 0, the page length is the minimum of this<br />  value and a server configured value; - when set to a value less than 0, an invalid parameter error<br />  is returned; - If not set, all valid catalogs are returned (not recommended). - Note: The number of<br />  returned catalogs might be less than the specified max_results size, even zero. The only definitive<br />  indication that no further catalogs can be fetched is when the next_page_token is unset from the<br />  response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`CatalogInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a></td>
    <td></td>
    <td>Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the<br />**CREATE_CATALOG** privilege.<br /><br />:param name: str<br />  Name of catalog.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param connection_name: str (optional)<br />  The name of the connection to an external data source.<br />:param options: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param provider_name: str (optional)<br />  The name of delta sharing provider.<br /><br />  A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server.<br />:param share_name: str (optional)<br />  The name of the share under the share provider.<br />:param storage_root: str (optional)<br />  Storage root URL for managed tables within catalog.<br /><br />:returns: :class:`CatalogInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the catalog that matches the supplied name. The caller must be either the owner of the<br />catalog, or a metastore admin (when changing the owner field of the catalog).<br /><br />:param name: str<br />  The name of the catalog.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)<br />  Whether predictive optimization should be enabled for this object and objects under it.<br />:param isolation_mode: :class:`CatalogIsolationMode` (optional)<br />  Whether the current securable is accessible from all workspaces or a specific set of workspaces.<br />:param new_name: str (optional)<br />  New name for the catalog.<br />:param options: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param owner: str (optional)<br />  Username of current owner of catalog.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br /><br />:returns: :class:`CatalogInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner<br />of the catalog.<br /><br />:param name: str<br />  The name of the catalog.<br />:param force: bool (optional)<br />  Force deletion even if the catalog is not empty.</td>
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
    <td>The name of the catalog.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force deletion even if the catalog is not empty.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>string</code></td>
    <td>Whether to include catalogs in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-include_unbound">
    <td><CopyableCode code="include_unbound" /></td>
    <td><code>string</code></td>
    <td>Whether to include catalogs not bound to the workspace. Effective only if the user has permission to update the catalog–workspace binding.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of catalogs to return. - when set to 0, the page length is set to a server configured value (recommended); - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to a value less than 0, an invalid parameter error is returned; - If not set, all valid catalogs are returned (not recommended). - Note: The number of returned catalogs might be less than the specified max_results size, even zero. The only definitive indication that no further catalogs can be fetched is when the next_page_token is unset from the response.</td>
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

Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the<br />catalog, or a user that has the **USE_CATALOG** privilege set for their account.<br /><br />:param name: str<br />  The name of the catalog.<br />:param include_browse: bool (optional)<br />  Whether to include catalogs in the response for which the principal can only access selective<br />  metadata for<br /><br />:returns: :class:`CatalogInfo`

```sql
SELECT
name,
metastore_id,
connection_name,
full_name,
provider_name,
share_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
isolation_mode,
options,
owner,
properties,
provisioning_info,
securable_type,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.catalog.catalogs
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be<br />retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the<br />**USE_CATALOG** privilege) will be retrieved. There is no guarantee of a specific ordering of the<br />elements in the array.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param include_browse: bool (optional)<br />  Whether to include catalogs in the response for which the principal can only access selective<br />  metadata for<br />:param include_unbound: bool (optional)<br />  Whether to include catalogs not bound to the workspace. Effective only if the user has permission to<br />  update the catalog–workspace binding.<br />:param max_results: int (optional)<br />  Maximum number of catalogs to return. - when set to 0, the page length is set to a server configured<br />  value (recommended); - when set to a value greater than 0, the page length is the minimum of this<br />  value and a server configured value; - when set to a value less than 0, an invalid parameter error<br />  is returned; - If not set, all valid catalogs are returned (not recommended). - Note: The number of<br />  returned catalogs might be less than the specified max_results size, even zero. The only definitive<br />  indication that no further catalogs can be fetched is when the next_page_token is unset from the<br />  response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`CatalogInfo`

```sql
SELECT
name,
metastore_id,
connection_name,
full_name,
provider_name,
share_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
isolation_mode,
options,
owner,
properties,
provisioning_info,
securable_type,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.catalog.catalogs
WHERE deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND include_unbound = '{{ include_unbound }}'
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

Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the<br />**CREATE_CATALOG** privilege.<br /><br />:param name: str<br />  Name of catalog.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param connection_name: str (optional)<br />  The name of the connection to an external data source.<br />:param options: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param provider_name: str (optional)<br />  The name of delta sharing provider.<br /><br />  A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server.<br />:param share_name: str (optional)<br />  The name of the share under the share provider.<br />:param storage_root: str (optional)<br />  Storage root URL for managed tables within catalog.<br /><br />:returns: :class:`CatalogInfo`

```sql
INSERT INTO databricks_workspace.catalog.catalogs (
data__name,
data__comment,
data__connection_name,
data__options,
data__properties,
data__provider_name,
data__share_name,
data__storage_root,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ comment }}',
'{{ connection_name }}',
'{{ options }}',
'{{ properties }}',
'{{ provider_name }}',
'{{ share_name }}',
'{{ storage_root }}',
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
connection_name,
full_name,
provider_name,
share_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
isolation_mode,
options,
owner,
properties,
provisioning_info,
securable_type,
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
- name: catalogs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the catalogs resource.
    - name: name
      value: string
      description: |
        Name of catalog.
    - name: comment
      value: string
      description: |
        User-provided free-form text description.
    - name: connection_name
      value: string
      description: |
        The name of the connection to an external data source.
    - name: options
      value: string
      description: |
        A map of key-value properties attached to the securable.
    - name: properties
      value: string
      description: |
        A map of key-value properties attached to the securable.
    - name: provider_name
      value: string
      description: |
        The name of delta sharing provider. A Delta Sharing catalog is a catalog that is based on a Delta share on a remote sharing server.
    - name: share_name
      value: string
      description: |
        The name of the share under the share provider.
    - name: storage_root
      value: string
      description: |
        Storage root URL for managed tables within catalog.
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

Updates the catalog that matches the supplied name. The caller must be either the owner of the<br />catalog, or a metastore admin (when changing the owner field of the catalog).<br /><br />:param name: str<br />  The name of the catalog.<br />:param comment: str (optional)<br />  User-provided free-form text description.<br />:param enable_predictive_optimization: :class:`EnablePredictiveOptimization` (optional)<br />  Whether predictive optimization should be enabled for this object and objects under it.<br />:param isolation_mode: :class:`CatalogIsolationMode` (optional)<br />  Whether the current securable is accessible from all workspaces or a specific set of workspaces.<br />:param new_name: str (optional)<br />  New name for the catalog.<br />:param options: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br />:param owner: str (optional)<br />  Username of current owner of catalog.<br />:param properties: Dict[str,str] (optional)<br />  A map of key-value properties attached to the securable.<br /><br />:returns: :class:`CatalogInfo`

```sql
UPDATE databricks_workspace.catalog.catalogs
SET 
data__comment = '{{ comment }}',
data__enable_predictive_optimization = '{{ enable_predictive_optimization }}',
data__isolation_mode = '{{ isolation_mode }}',
data__new_name = '{{ new_name }}',
data__options = '{{ options }}',
data__owner = '{{ owner }}',
data__properties = '{{ properties }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
metastore_id,
connection_name,
full_name,
provider_name,
share_name,
browse_only,
catalog_type,
comment,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
isolation_mode,
options,
owner,
properties,
provisioning_info,
securable_type,
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

Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner<br />of the catalog.<br /><br />:param name: str<br />  The name of the catalog.<br />:param force: bool (optional)<br />  Force deletion even if the catalog is not empty.

```sql
DELETE FROM databricks_workspace.catalog.catalogs
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

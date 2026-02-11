---
title: registered_models
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_models
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

Creates, updates, deletes, gets or lists a <code>registered_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.registered_models" /></td></tr>
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
    "description": "The name of the registered model"
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "The unique identifier of the metastore"
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "The name of the catalog where the schema and the registered model reside"
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The three-level (fully qualified) name of the registered model"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "The name of the schema where the registered model resides"
  },
  {
    "name": "aliases",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "alias_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "catalog_name",
        "type": "string",
        "description": "The name of the catalog containing the model version"
      },
      {
        "name": "id",
        "type": "string",
        "description": "The unique identifier of the alias"
      },
      {
        "name": "model_name",
        "type": "string",
        "description": "The name of the parent registered model of the model version, relative to parent schema"
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "The name of the schema containing the model version, relative to parent catalog"
      },
      {
        "name": "version_num",
        "type": "integer",
        "description": "Integer version number of the model version to which this alias points."
      }
    ]
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "The comment attached to the registered model"
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Creation timestamp of the registered model in milliseconds since the Unix epoch"
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The identifier of the user who created the registered model"
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The identifier of the user who owns the registered model"
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "The storage location on the cloud under which model version data files are stored"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Last-update timestamp of the registered model in milliseconds since the Unix epoch"
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The identifier of the user who updated the registered model last time"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the registered model"
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "The unique identifier of the metastore"
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "The name of the catalog where the schema and the registered model reside"
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The three-level (fully qualified) name of the registered model"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "The name of the schema where the registered model resides"
  },
  {
    "name": "aliases",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "alias_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "catalog_name",
        "type": "string",
        "description": "The name of the catalog containing the model version"
      },
      {
        "name": "id",
        "type": "string",
        "description": "The unique identifier of the alias"
      },
      {
        "name": "model_name",
        "type": "string",
        "description": "The name of the parent registered model of the model version, relative to parent schema"
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "The name of the schema containing the model version, relative to parent catalog"
      },
      {
        "name": "version_num",
        "type": "integer",
        "description": "Integer version number of the model version to which this alias points."
      }
    ]
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "The comment attached to the registered model"
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Creation timestamp of the registered model in milliseconds since the Unix epoch"
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The identifier of the user who created the registered model"
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The identifier of the user who owns the registered model"
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "The storage location on the cloud under which model version data files are stored"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Last-update timestamp of the registered model in milliseconds since the Unix epoch"
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The identifier of the user who updated the registered model last time"
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
    <td><a href="#parameter-include_aliases"><code>include_aliases</code></a>, <a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Get a registered model.<br /><br />The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the<br />registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**<br />privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param include_aliases: bool (optional)<br />  Whether to include registered model aliases in the response<br />:param include_browse: bool (optional)<br />  Whether to include registered models in the response for which the principal can only access<br />  selective metadata for<br /><br />:returns: :class:`RegisteredModelInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a></td>
    <td>List registered models. You can list registered models under a particular schema, or list all<br />registered models in the current metastore.<br /><br />The returned models are filtered based on the privileges of the calling user. For example, the<br />metastore admin is able to list all the registered models. A regular user needs to be the owner or<br />have the **EXECUTE** privilege on the registered model to recieve the registered models in the<br />response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege<br />on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />There is no guarantee of a specific ordering of the elements in the response.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str (optional)<br />  The identifier of the catalog under which to list registered models. If specified, schema_name must<br />  be specified.<br />:param include_browse: bool (optional)<br />  Whether to include registered models in the response for which the principal can only access<br />  selective metadata for<br />:param max_results: int (optional)<br />  Max number of registered models to return.<br /><br />  If both catalog and schema are specified: - when max_results is not specified, the page length is<br />  set to a server configured value (10000, as of 4/2/2024). - when set to a value greater than 0, the<br />  page length is the minimum of this value and a server configured value (10000, as of 4/2/2024); -<br />  when set to 0, the page length is set to a server configured value (10000, as of 4/2/2024); - when<br />  set to a value less than 0, an invalid parameter error is returned;<br /><br />  If neither schema nor catalog is specified: - when max_results is not specified, the page length is<br />  set to a server configured value (100, as of 4/2/2024). - when set to a value greater than 0, the<br />  page length is the minimum of this value and a server configured value (1000, as of 4/2/2024); -<br />  when set to 0, the page length is set to a server configured value (100, as of 4/2/2024); - when set<br />  to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque token to send for the next page of results (pagination).<br />:param schema_name: str (optional)<br />  The identifier of the schema under which to list registered models. If specified, catalog_name must<br />  be specified.<br /><br />:returns: Iterator over :class:`RegisteredModelInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new registered model in Unity Catalog.<br /><br />File storage for model versions in the registered model will be located in the default location which<br />is specified by the parent schema, or the parent catalog, or the Metastore.<br /><br />For registered model creation to succeed, the user must satisfy the following conditions: - The caller<br />must be a metastore admin, or be the owner of the parent catalog and schema, or have the<br />**USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br />- The caller must have the **CREATE MODEL** or **CREATE FUNCTION** privilege on the parent schema.<br /><br />:param aliases: List[:class:`RegisteredModelAlias`] (optional)<br />  List of aliases associated with the registered model<br />:param browse_only: bool (optional)<br />  Indicates whether the principal is limited to retrieving metadata for the associated object through<br />  the BROWSE privilege when include_browse is enabled in the request.<br />:param catalog_name: str (optional)<br />  The name of the catalog where the schema and the registered model reside<br />:param comment: str (optional)<br />  The comment attached to the registered model<br />:param created_at: int (optional)<br />  Creation timestamp of the registered model in milliseconds since the Unix epoch<br />:param created_by: str (optional)<br />  The identifier of the user who created the registered model<br />:param full_name: str (optional)<br />  The three-level (fully qualified) name of the registered model<br />:param metastore_id: str (optional)<br />  The unique identifier of the metastore<br />:param name: str (optional)<br />  The name of the registered model<br />:param owner: str (optional)<br />  The identifier of the user who owns the registered model<br />:param schema_name: str (optional)<br />  The name of the schema where the registered model resides<br />:param storage_location: str (optional)<br />  The storage location on the cloud under which model version data files are stored<br />:param updated_at: int (optional)<br />  Last-update timestamp of the registered model in milliseconds since the Unix epoch<br />:param updated_by: str (optional)<br />  The identifier of the user who updated the registered model last time<br /><br />:returns: :class:`RegisteredModelInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the specified registered model.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />Currently only the name, the owner or the comment of the registered model can be updated.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param aliases: List[:class:`RegisteredModelAlias`] (optional)<br />  List of aliases associated with the registered model<br />:param browse_only: bool (optional)<br />  Indicates whether the principal is limited to retrieving metadata for the associated object through<br />  the BROWSE privilege when include_browse is enabled in the request.<br />:param catalog_name: str (optional)<br />  The name of the catalog where the schema and the registered model reside<br />:param comment: str (optional)<br />  The comment attached to the registered model<br />:param created_at: int (optional)<br />  Creation timestamp of the registered model in milliseconds since the Unix epoch<br />:param created_by: str (optional)<br />  The identifier of the user who created the registered model<br />:param metastore_id: str (optional)<br />  The unique identifier of the metastore<br />:param name: str (optional)<br />  The name of the registered model<br />:param new_name: str (optional)<br />  New name for the registered model.<br />:param owner: str (optional)<br />  The identifier of the user who owns the registered model<br />:param schema_name: str (optional)<br />  The name of the schema where the registered model resides<br />:param storage_location: str (optional)<br />  The storage location on the cloud under which model version data files are stored<br />:param updated_at: int (optional)<br />  Last-update timestamp of the registered model in milliseconds since the Unix epoch<br />:param updated_by: str (optional)<br />  The identifier of the user who updated the registered model last time<br /><br />:returns: :class:`RegisteredModelInfo`</td>
</tr>
<tr>
    <td><a href="#set_alias"><CopyableCode code="set_alias" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__version_num"><code>data__version_num</code></a></td>
    <td></td>
    <td>Set an alias on the specified registered model.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param alias: str<br />  The name of the alias<br />:param version_num: int<br />  The version number of the model version to which the alias points<br /><br />:returns: :class:`RegisteredModelAlias`</td>
</tr>
<tr>
    <td><a href="#delete_alias"><CopyableCode code="delete_alias" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a registered model alias.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param alias: str<br />  The name of the alias</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a registered model and all its model versions from the specified parent catalog and schema.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model</td>
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
<tr id="parameter-alias">
    <td><CopyableCode code="alias" /></td>
    <td><code>string</code></td>
    <td>The name of the alias</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>The three-level (fully qualified) name of the registered model</td>
</tr>
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>The identifier of the catalog under which to list registered models. If specified, schema_name must be specified.</td>
</tr>
<tr id="parameter-include_aliases">
    <td><CopyableCode code="include_aliases" /></td>
    <td><code>string</code></td>
    <td>Whether to include registered model aliases in the response</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>string</code></td>
    <td>Whether to include registered models in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Max number of registered models to return. If both catalog and schema are specified: - when max_results is not specified, the page length is set to a server configured value (10000, as of 4/2/2024). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value (10000, as of 4/2/2024); - when set to 0, the page length is set to a server configured value (10000, as of 4/2/2024); - when set to a value less than 0, an invalid parameter error is returned; If neither schema nor catalog is specified: - when max_results is not specified, the page length is set to a server configured value (100, as of 4/2/2024). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value (1000, as of 4/2/2024); - when set to 0, the page length is set to a server configured value (100, as of 4/2/2024); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque token to send for the next page of results (pagination).</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The identifier of the schema under which to list registered models. If specified, catalog_name must be specified.</td>
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

Get a registered model.<br /><br />The caller must be a metastore admin or an owner of (or have the **EXECUTE** privilege on) the<br />registered model. For the latter case, the caller must also be the owner or have the **USE_CATALOG**<br />privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param include_aliases: bool (optional)<br />  Whether to include registered model aliases in the response<br />:param include_browse: bool (optional)<br />  Whether to include registered models in the response for which the principal can only access<br />  selective metadata for<br /><br />:returns: :class:`RegisteredModelInfo`

```sql
SELECT
name,
metastore_id,
catalog_name,
full_name,
schema_name,
aliases,
browse_only,
comment,
created_at,
created_by,
owner,
storage_location,
updated_at,
updated_by
FROM databricks_workspace.catalog.registered_models
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_aliases = '{{ include_aliases }}'
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

List registered models. You can list registered models under a particular schema, or list all<br />registered models in the current metastore.<br /><br />The returned models are filtered based on the privileges of the calling user. For example, the<br />metastore admin is able to list all the registered models. A regular user needs to be the owner or<br />have the **EXECUTE** privilege on the registered model to recieve the registered models in the<br />response. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege<br />on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />There is no guarantee of a specific ordering of the elements in the response.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str (optional)<br />  The identifier of the catalog under which to list registered models. If specified, schema_name must<br />  be specified.<br />:param include_browse: bool (optional)<br />  Whether to include registered models in the response for which the principal can only access<br />  selective metadata for<br />:param max_results: int (optional)<br />  Max number of registered models to return.<br /><br />  If both catalog and schema are specified: - when max_results is not specified, the page length is<br />  set to a server configured value (10000, as of 4/2/2024). - when set to a value greater than 0, the<br />  page length is the minimum of this value and a server configured value (10000, as of 4/2/2024); -<br />  when set to 0, the page length is set to a server configured value (10000, as of 4/2/2024); - when<br />  set to a value less than 0, an invalid parameter error is returned;<br /><br />  If neither schema nor catalog is specified: - when max_results is not specified, the page length is<br />  set to a server configured value (100, as of 4/2/2024). - when set to a value greater than 0, the<br />  page length is the minimum of this value and a server configured value (1000, as of 4/2/2024); -<br />  when set to 0, the page length is set to a server configured value (100, as of 4/2/2024); - when set<br />  to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque token to send for the next page of results (pagination).<br />:param schema_name: str (optional)<br />  The identifier of the schema under which to list registered models. If specified, catalog_name must<br />  be specified.<br /><br />:returns: Iterator over :class:`RegisteredModelInfo`

```sql
SELECT
name,
metastore_id,
catalog_name,
full_name,
schema_name,
aliases,
browse_only,
comment,
created_at,
created_by,
owner,
storage_location,
updated_at,
updated_by
FROM databricks_workspace.catalog.registered_models
WHERE deployment_name = '{{ deployment_name }}' -- required
AND catalog_name = '{{ catalog_name }}'
AND include_browse = '{{ include_browse }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND schema_name = '{{ schema_name }}'
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

Creates a new registered model in Unity Catalog.<br /><br />File storage for model versions in the registered model will be located in the default location which<br />is specified by the parent schema, or the parent catalog, or the Metastore.<br /><br />For registered model creation to succeed, the user must satisfy the following conditions: - The caller<br />must be a metastore admin, or be the owner of the parent catalog and schema, or have the<br />**USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br />- The caller must have the **CREATE MODEL** or **CREATE FUNCTION** privilege on the parent schema.<br /><br />:param aliases: List[:class:`RegisteredModelAlias`] (optional)<br />  List of aliases associated with the registered model<br />:param browse_only: bool (optional)<br />  Indicates whether the principal is limited to retrieving metadata for the associated object through<br />  the BROWSE privilege when include_browse is enabled in the request.<br />:param catalog_name: str (optional)<br />  The name of the catalog where the schema and the registered model reside<br />:param comment: str (optional)<br />  The comment attached to the registered model<br />:param created_at: int (optional)<br />  Creation timestamp of the registered model in milliseconds since the Unix epoch<br />:param created_by: str (optional)<br />  The identifier of the user who created the registered model<br />:param full_name: str (optional)<br />  The three-level (fully qualified) name of the registered model<br />:param metastore_id: str (optional)<br />  The unique identifier of the metastore<br />:param name: str (optional)<br />  The name of the registered model<br />:param owner: str (optional)<br />  The identifier of the user who owns the registered model<br />:param schema_name: str (optional)<br />  The name of the schema where the registered model resides<br />:param storage_location: str (optional)<br />  The storage location on the cloud under which model version data files are stored<br />:param updated_at: int (optional)<br />  Last-update timestamp of the registered model in milliseconds since the Unix epoch<br />:param updated_by: str (optional)<br />  The identifier of the user who updated the registered model last time<br /><br />:returns: :class:`RegisteredModelInfo`

```sql
INSERT INTO databricks_workspace.catalog.registered_models (
data__aliases,
data__browse_only,
data__catalog_name,
data__comment,
data__created_at,
data__created_by,
data__full_name,
data__metastore_id,
data__name,
data__owner,
data__schema_name,
data__storage_location,
data__updated_at,
data__updated_by,
deployment_name
)
SELECT 
'{{ aliases }}',
'{{ browse_only }}',
'{{ catalog_name }}',
'{{ comment }}',
'{{ created_at }}',
'{{ created_by }}',
'{{ full_name }}',
'{{ metastore_id }}',
'{{ name }}',
'{{ owner }}',
'{{ schema_name }}',
'{{ storage_location }}',
'{{ updated_at }}',
'{{ updated_by }}',
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
catalog_name,
full_name,
schema_name,
aliases,
browse_only,
comment,
created_at,
created_by,
owner,
storage_location,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: registered_models
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the registered_models resource.
    - name: aliases
      value: string
      description: |
        List of aliases associated with the registered model
    - name: browse_only
      value: string
      description: |
        Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request.
    - name: catalog_name
      value: string
      description: |
        The name of the catalog where the schema and the registered model reside
    - name: comment
      value: string
      description: |
        The comment attached to the registered model
    - name: created_at
      value: string
      description: |
        Creation timestamp of the registered model in milliseconds since the Unix epoch
    - name: created_by
      value: string
      description: |
        The identifier of the user who created the registered model
    - name: full_name
      value: string
      description: |
        The three-level (fully qualified) name of the registered model
    - name: metastore_id
      value: string
      description: |
        The unique identifier of the metastore
    - name: name
      value: string
      description: |
        The name of the registered model
    - name: owner
      value: string
      description: |
        The identifier of the user who owns the registered model
    - name: schema_name
      value: string
      description: |
        The name of the schema where the registered model resides
    - name: storage_location
      value: string
      description: |
        The storage location on the cloud under which model version data files are stored
    - name: updated_at
      value: string
      description: |
        Last-update timestamp of the registered model in milliseconds since the Unix epoch
    - name: updated_by
      value: string
      description: |
        The identifier of the user who updated the registered model last time
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

Updates the specified registered model.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />Currently only the name, the owner or the comment of the registered model can be updated.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param aliases: List[:class:`RegisteredModelAlias`] (optional)<br />  List of aliases associated with the registered model<br />:param browse_only: bool (optional)<br />  Indicates whether the principal is limited to retrieving metadata for the associated object through<br />  the BROWSE privilege when include_browse is enabled in the request.<br />:param catalog_name: str (optional)<br />  The name of the catalog where the schema and the registered model reside<br />:param comment: str (optional)<br />  The comment attached to the registered model<br />:param created_at: int (optional)<br />  Creation timestamp of the registered model in milliseconds since the Unix epoch<br />:param created_by: str (optional)<br />  The identifier of the user who created the registered model<br />:param metastore_id: str (optional)<br />  The unique identifier of the metastore<br />:param name: str (optional)<br />  The name of the registered model<br />:param new_name: str (optional)<br />  New name for the registered model.<br />:param owner: str (optional)<br />  The identifier of the user who owns the registered model<br />:param schema_name: str (optional)<br />  The name of the schema where the registered model resides<br />:param storage_location: str (optional)<br />  The storage location on the cloud under which model version data files are stored<br />:param updated_at: int (optional)<br />  Last-update timestamp of the registered model in milliseconds since the Unix epoch<br />:param updated_by: str (optional)<br />  The identifier of the user who updated the registered model last time<br /><br />:returns: :class:`RegisteredModelInfo`

```sql
UPDATE databricks_workspace.catalog.registered_models
SET 
data__aliases = '{{ aliases }}',
data__browse_only = '{{ browse_only }}',
data__catalog_name = '{{ catalog_name }}',
data__comment = '{{ comment }}',
data__created_at = '{{ created_at }}',
data__created_by = '{{ created_by }}',
data__metastore_id = '{{ metastore_id }}',
data__name = '{{ name }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}',
data__schema_name = '{{ schema_name }}',
data__storage_location = '{{ storage_location }}',
data__updated_at = '{{ updated_at }}',
data__updated_by = '{{ updated_by }}'
WHERE 
full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
metastore_id,
catalog_name,
full_name,
schema_name,
aliases,
browse_only,
comment,
created_at,
created_by,
owner,
storage_location,
updated_at,
updated_by;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_alias"
    values={[
        { label: 'set_alias', value: 'set_alias' }
    ]}
>
<TabItem value="set_alias">

Set an alias on the specified registered model.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param alias: str<br />  The name of the alias<br />:param version_num: int<br />  The version number of the model version to which the alias points<br /><br />:returns: :class:`RegisteredModelAlias`

```sql
REPLACE databricks_workspace.catalog.registered_models
SET 
data__version_num = {{ version_num }}
WHERE 
full_name = '{{ full_name }}' --required
AND alias = '{{ alias }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__version_num = '{{ version_num }}' --required
RETURNING
id,
alias_name,
catalog_name,
model_name,
schema_name,
version_num;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_alias"
    values={[
        { label: 'delete_alias', value: 'delete_alias' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_alias">

Deletes a registered model alias.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model<br />:param alias: str<br />  The name of the alias

```sql
DELETE FROM databricks_workspace.catalog.registered_models
WHERE full_name = '{{ full_name }}' --required
AND alias = '{{ alias }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a registered model and all its model versions from the specified parent catalog and schema.<br /><br />The caller must be a metastore admin or an owner of the registered model. For the latter case, the<br />caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />:param full_name: str<br />  The three-level (fully qualified) name of the registered model

```sql
DELETE FROM databricks_workspace.catalog.registered_models
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

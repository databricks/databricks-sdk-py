---
title: metastores
hide_title: false
hide_table_of_contents: false
keywords:
  - metastores
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

Creates, updates, deletes, gets or lists a <code>metastores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.metastores" /></td></tr>
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
    "description": "The user-specified name of the metastore."
  },
  {
    "name": "default_data_access_config_id",
    "type": "string",
    "description": "Unique identifier of the metastore's (Default) Data Access Configuration."
  },
  {
    "name": "global_metastore_id",
    "type": "string",
    "description": "Globally unique metastore ID across clouds and regions, of the form `cloud:region:metastore_id`."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of metastore."
  },
  {
    "name": "storage_root_credential_id",
    "type": "string",
    "description": "UUID of storage credential to access the metastore storage_root."
  },
  {
    "name": "delta_sharing_organization_name",
    "type": "string",
    "description": "The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta Sharing as the official name."
  },
  {
    "name": "storage_root_credential_name",
    "type": "string",
    "description": "Name of the storage credential to access the metastore storage_root."
  },
  {
    "name": "cloud",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this metastore was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of metastore creator."
  },
  {
    "name": "delta_sharing_recipient_token_lifetime_in_seconds",
    "type": "integer",
    "description": "The lifetime of delta sharing recipient token in seconds."
  },
  {
    "name": "delta_sharing_scope",
    "type": "string",
    "description": "The scope of Delta Sharing enabled for the metastore."
  },
  {
    "name": "external_access_enabled",
    "type": "boolean",
    "description": "Whether to allow non-DBR clients to directly access entities under the metastore."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the metastore."
  },
  {
    "name": "privilege_model_version",
    "type": "string",
    "description": "Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region which the metastore serves (e.g., `us-west-2`, `westus`)."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "The storage root URL for metastore"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which the metastore was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the metastore."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The user-specified name of the metastore."
  },
  {
    "name": "default_data_access_config_id",
    "type": "string",
    "description": "Unique identifier of the metastore's (Default) Data Access Configuration."
  },
  {
    "name": "global_metastore_id",
    "type": "string",
    "description": "Globally unique metastore ID across clouds and regions, of the form `cloud:region:metastore_id`."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of metastore."
  },
  {
    "name": "storage_root_credential_id",
    "type": "string",
    "description": "UUID of storage credential to access the metastore storage_root."
  },
  {
    "name": "delta_sharing_organization_name",
    "type": "string",
    "description": "The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta Sharing as the official name."
  },
  {
    "name": "storage_root_credential_name",
    "type": "string",
    "description": "Name of the storage credential to access the metastore storage_root."
  },
  {
    "name": "cloud",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this metastore was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of metastore creator."
  },
  {
    "name": "delta_sharing_recipient_token_lifetime_in_seconds",
    "type": "integer",
    "description": "The lifetime of delta sharing recipient token in seconds."
  },
  {
    "name": "delta_sharing_scope",
    "type": "string",
    "description": "The scope of Delta Sharing enabled for the metastore."
  },
  {
    "name": "external_access_enabled",
    "type": "boolean",
    "description": "Whether to allow non-DBR clients to directly access entities under the metastore."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the metastore."
  },
  {
    "name": "privilege_model_version",
    "type": "string",
    "description": "Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`)."
  },
  {
    "name": "region",
    "type": "string",
    "description": "Cloud region which the metastore serves (e.g., `us-west-2`, `westus`)."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "The storage root URL for metastore"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which the metastore was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the metastore."
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
    <td>Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this<br />info.<br /><br />:param id: str<br />  Unique ID of the metastore.<br /><br />:returns: :class:`MetastoreInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of the available metastores (as __MetastoreInfo__ objects). The caller must be an admin<br />to retrieve this info. There is no guarantee of a specific ordering of the elements in the array.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param max_results: int (optional)<br />  Maximum number of metastores to return. - when set to a value greater than 0, the page length is the<br />  minimum of this value and a server configured value; - when set to 0, the page length is set to a<br />  server configured value (recommended); - when set to a value less than 0, an invalid parameter error<br />  is returned; - If not set, all the metastores are returned (not recommended). - Note: The number of<br />  returned metastores might be less than the specified max_results size, even zero. The only<br />  definitive indication that no further metastores can be fetched is when the next_page_token is unset<br />  from the response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`MetastoreInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a></td>
    <td></td>
    <td>Creates a new metastore based on a provided name and optional storage root path. By default (if the<br />__owner__ field is not set), the owner of the new metastore is the user calling the<br />__createMetastore__ API. If the __owner__ field is set to the empty string (**""**), the ownership is<br />assigned to the System User instead.<br /><br />:param name: str<br />  The user-specified name of the metastore.<br />:param external_access_enabled: bool (optional)<br />  Whether to allow non-DBR clients to directly access entities under the metastore.<br />:param region: str (optional)<br />  Cloud region which the metastore serves (e.g., `us-west-2`, `westus`).<br />:param storage_root: str (optional)<br />  The storage root URL for metastore<br /><br />:returns: :class:`MetastoreInfo`</td>
</tr>
<tr>
    <td><a href="#update_assignment"><CopyableCode code="update_assignment" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a metastore assignment. This operation can be used to update __metastore_id__ or<br />__default_catalog_name__ for a specified Workspace, if the Workspace is already assigned a metastore.<br />The caller must be an account admin to update __metastore_id__; otherwise, the caller can be a<br />Workspace admin.<br /><br />:param workspace_id: int<br />  A workspace ID.<br />:param default_catalog_name: str (optional)<br />  The name of the default catalog in the metastore. This field is deprecated. Please use "Default<br />  Namespace API" to configure the default catalog for a Databricks workspace.<br />:param metastore_id: str (optional)<br />  The unique ID of the metastore.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates information for a specific metastore. The caller must be a metastore admin. If the __owner__<br />field is set to the empty string (**""**), the ownership is updated to the System User.<br /><br />:param id: str<br />  Unique ID of the metastore.<br />:param delta_sharing_organization_name: str (optional)<br />  The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta<br />  Sharing as the official name.<br />:param delta_sharing_recipient_token_lifetime_in_seconds: int (optional)<br />  The lifetime of delta sharing recipient token in seconds.<br />:param delta_sharing_scope: :class:`DeltaSharingScopeEnum` (optional)<br />  The scope of Delta Sharing enabled for the metastore.<br />:param external_access_enabled: bool (optional)<br />  Whether to allow non-DBR clients to directly access entities under the metastore.<br />:param new_name: str (optional)<br />  New name for the metastore.<br />:param owner: str (optional)<br />  The owner of the metastore.<br />:param privilege_model_version: str (optional)<br />  Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`).<br />:param storage_root_credential_id: str (optional)<br />  UUID of storage credential to access the metastore storage_root.<br /><br />:returns: :class:`MetastoreInfo`</td>
</tr>
<tr>
    <td><a href="#assign"><CopyableCode code="assign" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__metastore_id"><code>data__metastore_id</code></a>, <a href="#parameter-data__default_catalog_name"><code>data__default_catalog_name</code></a></td>
    <td></td>
    <td>Creates a new metastore assignment. If an assignment for the same __workspace_id__ exists, it will be<br />overwritten by the new __metastore_id__ and __default_catalog_name__. The caller must be an account<br />admin.<br /><br />:param workspace_id: int<br />  A workspace ID.<br />:param metastore_id: str<br />  The unique ID of the metastore.<br />:param default_catalog_name: str<br />  The name of the default catalog in the metastore. This field is deprecated. Please use "Default<br />  Namespace API" to configure the default catalog for a Databricks workspace.</td>
</tr>
<tr>
    <td><a href="#unassign"><CopyableCode code="unassign" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-metastore_id"><code>metastore_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a metastore assignment. The caller must be an account administrator.<br /><br />:param workspace_id: int<br />  A workspace ID.<br />:param metastore_id: str<br />  Query for the ID of the metastore to delete.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes a metastore. The caller must be a metastore admin.<br /><br />:param id: str<br />  Unique ID of the metastore.<br />:param force: bool (optional)<br />  Force deletion even if the metastore is not empty. Default is false.</td>
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
    <td>Unique ID of the metastore.</td>
</tr>
<tr id="parameter-metastore_id">
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td>Query for the ID of the metastore to delete.</td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>A workspace ID.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Force deletion even if the metastore is not empty. Default is false.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of metastores to return. - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned; - If not set, all the metastores are returned (not recommended). - Note: The number of returned metastores might be less than the specified max_results size, even zero. The only definitive indication that no further metastores can be fetched is when the next_page_token is unset from the response.</td>
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

Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this<br />info.<br /><br />:param id: str<br />  Unique ID of the metastore.<br /><br />:returns: :class:`MetastoreInfo`

```sql
SELECT
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.catalog.metastores
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets an array of the available metastores (as __MetastoreInfo__ objects). The caller must be an admin<br />to retrieve this info. There is no guarantee of a specific ordering of the elements in the array.<br /><br />NOTE: we recommend using max_results=0 to use the paginated version of this API. Unpaginated calls<br />will be deprecated soon.<br /><br />PAGINATION BEHAVIOR: When using pagination (max_results &gt;= 0), a page may contain zero results while<br />still providing a next_page_token. Clients must continue reading pages until next_page_token is<br />absent, which is the only indication that the end of results has been reached.<br /><br />:param max_results: int (optional)<br />  Maximum number of metastores to return. - when set to a value greater than 0, the page length is the<br />  minimum of this value and a server configured value; - when set to 0, the page length is set to a<br />  server configured value (recommended); - when set to a value less than 0, an invalid parameter error<br />  is returned; - If not set, all the metastores are returned (not recommended). - Note: The number of<br />  returned metastores might be less than the specified max_results size, even zero. The only<br />  definitive indication that no further metastores can be fetched is when the next_page_token is unset<br />  from the response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`MetastoreInfo`

```sql
SELECT
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.catalog.metastores
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

Creates a new metastore based on a provided name and optional storage root path. By default (if the<br />__owner__ field is not set), the owner of the new metastore is the user calling the<br />__createMetastore__ API. If the __owner__ field is set to the empty string (**""**), the ownership is<br />assigned to the System User instead.<br /><br />:param name: str<br />  The user-specified name of the metastore.<br />:param external_access_enabled: bool (optional)<br />  Whether to allow non-DBR clients to directly access entities under the metastore.<br />:param region: str (optional)<br />  Cloud region which the metastore serves (e.g., `us-west-2`, `westus`).<br />:param storage_root: str (optional)<br />  The storage root URL for metastore<br /><br />:returns: :class:`MetastoreInfo`

```sql
INSERT INTO databricks_workspace.catalog.metastores (
data__name,
data__external_access_enabled,
data__region,
data__storage_root,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ external_access_enabled }}',
'{{ region }}',
'{{ storage_root }}',
'{{ deployment_name }}'
RETURNING
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: metastores
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the metastores resource.
    - name: name
      value: string
      description: |
        The user-specified name of the metastore.
    - name: external_access_enabled
      value: string
      description: |
        Whether to allow non-DBR clients to directly access entities under the metastore.
    - name: region
      value: string
      description: |
        Cloud region which the metastore serves (e.g., `us-west-2`, `westus`).
    - name: storage_root
      value: string
      description: |
        The storage root URL for metastore
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_assignment"
    values={[
        { label: 'update_assignment', value: 'update_assignment' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_assignment">

Updates a metastore assignment. This operation can be used to update __metastore_id__ or<br />__default_catalog_name__ for a specified Workspace, if the Workspace is already assigned a metastore.<br />The caller must be an account admin to update __metastore_id__; otherwise, the caller can be a<br />Workspace admin.<br /><br />:param workspace_id: int<br />  A workspace ID.<br />:param default_catalog_name: str (optional)<br />  The name of the default catalog in the metastore. This field is deprecated. Please use "Default<br />  Namespace API" to configure the default catalog for a Databricks workspace.<br />:param metastore_id: str (optional)<br />  The unique ID of the metastore.

```sql
UPDATE databricks_workspace.catalog.metastores
SET 
data__default_catalog_name = '{{ default_catalog_name }}',
data__metastore_id = '{{ metastore_id }}'
WHERE 
workspace_id = '{{ workspace_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="update">

Updates information for a specific metastore. The caller must be a metastore admin. If the __owner__<br />field is set to the empty string (**""**), the ownership is updated to the System User.<br /><br />:param id: str<br />  Unique ID of the metastore.<br />:param delta_sharing_organization_name: str (optional)<br />  The organization name of a Delta Sharing entity, to be used in Databricks-to-Databricks Delta<br />  Sharing as the official name.<br />:param delta_sharing_recipient_token_lifetime_in_seconds: int (optional)<br />  The lifetime of delta sharing recipient token in seconds.<br />:param delta_sharing_scope: :class:`DeltaSharingScopeEnum` (optional)<br />  The scope of Delta Sharing enabled for the metastore.<br />:param external_access_enabled: bool (optional)<br />  Whether to allow non-DBR clients to directly access entities under the metastore.<br />:param new_name: str (optional)<br />  New name for the metastore.<br />:param owner: str (optional)<br />  The owner of the metastore.<br />:param privilege_model_version: str (optional)<br />  Privilege model version of the metastore, of the form `major.minor` (e.g., `1.0`).<br />:param storage_root_credential_id: str (optional)<br />  UUID of storage credential to access the metastore storage_root.<br /><br />:returns: :class:`MetastoreInfo`

```sql
UPDATE databricks_workspace.catalog.metastores
SET 
data__delta_sharing_organization_name = '{{ delta_sharing_organization_name }}',
data__delta_sharing_recipient_token_lifetime_in_seconds = '{{ delta_sharing_recipient_token_lifetime_in_seconds }}',
data__delta_sharing_scope = '{{ delta_sharing_scope }}',
data__external_access_enabled = '{{ external_access_enabled }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}',
data__privilege_model_version = '{{ privilege_model_version }}',
data__storage_root_credential_id = '{{ storage_root_credential_id }}'
WHERE 
id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="assign"
    values={[
        { label: 'assign', value: 'assign' }
    ]}
>
<TabItem value="assign">

Creates a new metastore assignment. If an assignment for the same __workspace_id__ exists, it will be<br />overwritten by the new __metastore_id__ and __default_catalog_name__. The caller must be an account<br />admin.<br /><br />:param workspace_id: int<br />  A workspace ID.<br />:param metastore_id: str<br />  The unique ID of the metastore.<br />:param default_catalog_name: str<br />  The name of the default catalog in the metastore. This field is deprecated. Please use "Default<br />  Namespace API" to configure the default catalog for a Databricks workspace.

```sql
REPLACE databricks_workspace.catalog.metastores
SET 
data__metastore_id = '{{ metastore_id }}',
data__default_catalog_name = '{{ default_catalog_name }}'
WHERE 
workspace_id = '{{ workspace_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__metastore_id = '{{ metastore_id }}' --required
AND data__default_catalog_name = '{{ default_catalog_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="unassign"
    values={[
        { label: 'unassign', value: 'unassign' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="unassign">

Deletes a metastore assignment. The caller must be an account administrator.<br /><br />:param workspace_id: int<br />  A workspace ID.<br />:param metastore_id: str<br />  Query for the ID of the metastore to delete.

```sql
DELETE FROM databricks_workspace.catalog.metastores
WHERE workspace_id = '{{ workspace_id }}' --required
AND metastore_id = '{{ metastore_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a metastore. The caller must be a metastore admin.<br /><br />:param id: str<br />  Unique ID of the metastore.<br />:param force: bool (optional)<br />  Force deletion even if the metastore is not empty. Default is false.

```sql
DELETE FROM databricks_workspace.catalog.metastores
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

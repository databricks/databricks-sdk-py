---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.volumes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="read"
    values={[
        { label: 'read', value: 'read' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="read">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the volume"
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "The unique identifier of the metastore"
  },
  {
    "name": "volume_id",
    "type": "string",
    "description": "The unique identifier of the volume"
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "The name of the catalog where the schema and the volume are"
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The three-level (fully qualified) name of the volume"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "The name of the schema where the volume is"
  },
  {
    "name": "access_point",
    "type": "string",
    "description": ""
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "The comment attached to the volume"
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The identifier of the user who created the volume"
  },
  {
    "name": "encryption_details",
    "type": "object",
    "description": "Encryption options that apply to clients connecting to cloud storage.",
    "children": [
      {
        "name": "sse_encryption_details",
        "type": "object",
        "description": "Server-Side Encryption properties for clients communicating with AWS s3.",
        "children": [
          {
            "name": "algorithm",
            "type": "string",
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request."
          },
          {
            "name": "aws_kms_key_arn",
            "type": "string",
            "description": "Optional. The ARN of the SSE-KMS key used with the S3 location, when algorithm = \"SSE-KMS\". Sets the value of the 'x-amz-server-side-encryption-aws-kms-key-id' header."
          }
        ]
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The identifier of the user who owns the volume"
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "The storage location on the cloud"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The identifier of the user who updated the volume last time"
  },
  {
    "name": "volume_type",
    "type": "string",
    "description": "The type of the volume. An external volume is located in the specified external location. A managed volume is located in the default location which is specified by the parent schema, or the parent catalog, or the Metastore. [Learn more] [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the volume"
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "The unique identifier of the metastore"
  },
  {
    "name": "volume_id",
    "type": "string",
    "description": "The unique identifier of the volume"
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "The name of the catalog where the schema and the volume are"
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The three-level (fully qualified) name of the volume"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "The name of the schema where the volume is"
  },
  {
    "name": "access_point",
    "type": "string",
    "description": ""
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "The comment attached to the volume"
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The identifier of the user who created the volume"
  },
  {
    "name": "encryption_details",
    "type": "object",
    "description": "Encryption options that apply to clients connecting to cloud storage.",
    "children": [
      {
        "name": "sse_encryption_details",
        "type": "object",
        "description": "Server-Side Encryption properties for clients communicating with AWS s3.",
        "children": [
          {
            "name": "algorithm",
            "type": "string",
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request."
          },
          {
            "name": "aws_kms_key_arn",
            "type": "string",
            "description": "Optional. The ARN of the SSE-KMS key used with the S3 location, when algorithm = \"SSE-KMS\". Sets the value of the 'x-amz-server-side-encryption-aws-kms-key-id' header."
          }
        ]
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The identifier of the user who owns the volume"
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "The storage location on the cloud"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The identifier of the user who updated the volume last time"
  },
  {
    "name": "volume_type",
    "type": "string",
    "description": "The type of the volume. An external volume is located in the specified external location. A managed volume is located in the default location which is specified by the parent schema, or the parent catalog, or the Metastore. [Learn more] [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external"
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
    <td><a href="#read"><CopyableCode code="read" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Gets a volume from the metastore for a specific catalog and schema.<br /><br />The caller must be a metastore admin or an owner of (or have the **READ VOLUME** privilege on) the<br />volume. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege<br />on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />:param name: str<br />  The three-level (fully qualified) name of the volume<br />:param include_browse: bool (optional)<br />  Whether to include volumes in the response for which the principal can only access selective<br />  metadata for<br /><br />:returns: :class:`VolumeInfo`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of volumes for the current metastore under the parent catalog and schema.<br /><br />The returned volumes are filtered based on the privileges of the calling user. For example, the<br />metastore admin is able to list all the volumes. A regular user needs to be the owner or have the<br />**READ VOLUME** privilege on the volume to receive the volumes in the response. For the latter case,<br />the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />There is no guarantee of a specific ordering of the elements in the array.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str<br />  The identifier of the catalog<br />:param schema_name: str<br />  The identifier of the schema<br />:param include_browse: bool (optional)<br />  Whether to include volumes in the response for which the principal can only access selective<br />  metadata for<br />:param max_results: int (optional)<br />  Maximum number of volumes to return (page length).<br /><br />  If not set, the page length is set to a server configured value (10000, as of 1/29/2024). - when set<br />  to a value greater than 0, the page length is the minimum of this value and a server configured<br />  value (10000, as of 1/29/2024); - when set to 0, the page length is set to a server configured value<br />  (10000, as of 1/29/2024) (recommended); - when set to a value less than 0, an invalid parameter<br />  error is returned;<br /><br />  Note: this parameter controls only the maximum number of volumes to return. The actual number of<br />  volumes returned in a page may be smaller than this value, including 0, even if there are more<br />  pages.<br />:param page_token: str (optional)<br />  Opaque token returned by a previous request. It must be included in the request to retrieve the next<br />  page of results (pagination).<br /><br />:returns: Iterator over :class:`VolumeInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__catalog_name"><code>data__catalog_name</code></a>, <a href="#parameter-data__schema_name"><code>data__schema_name</code></a>, <a href="#parameter-data__name"><code>data__name</code></a>, <a href="#parameter-data__volume_type"><code>data__volume_type</code></a></td>
    <td></td>
    <td>Creates a new volume.<br /><br />The user could create either an external volume or a managed volume. An external volume will be<br />created in the specified external location, while a managed volume will be located in the default<br />location which is specified by the parent schema, or the parent catalog, or the Metastore.<br /><br />For the volume creation to succeed, the user must satisfy following conditions: - The caller must be a<br />metastore admin, or be the owner of the parent catalog and schema, or have the **USE_CATALOG**<br />privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema. - The caller<br />must have **CREATE VOLUME** privilege on the parent schema.<br /><br />For an external volume, following conditions also need to satisfy - The caller must have **CREATE<br />EXTERNAL VOLUME** privilege on the external location. - There are no other tables, nor volumes<br />existing in the specified storage location. - The specified storage location is not under the location<br />of other tables, nor volumes, or catalogs or schemas.<br /><br />:param catalog_name: str<br />  The name of the catalog where the schema and the volume are<br />:param schema_name: str<br />  The name of the schema where the volume is<br />:param name: str<br />  The name of the volume<br />:param volume_type: :class:`VolumeType`<br />  The type of the volume. An external volume is located in the specified external location. A managed<br />  volume is located in the default location which is specified by the parent schema, or the parent<br />  catalog, or the Metastore. [Learn more]<br /><br />  [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external<br />:param comment: str (optional)<br />  The comment attached to the volume<br />:param storage_location: str (optional)<br />  The storage location on the cloud<br /><br />:returns: :class:`VolumeInfo`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the specified volume under the specified parent catalog and schema.<br /><br />The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must<br />also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**<br />privilege on the parent schema.<br /><br />Currently only the name, the owner or the comment of the volume could be updated.<br /><br />:param name: str<br />  The three-level (fully qualified) name of the volume<br />:param comment: str (optional)<br />  The comment attached to the volume<br />:param new_name: str (optional)<br />  New name for the volume.<br />:param owner: str (optional)<br />  The identifier of the user who owns the volume<br /><br />:returns: :class:`VolumeInfo`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a volume from the specified parent catalog and schema.<br /><br />The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must<br />also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**<br />privilege on the parent schema.<br /><br />:param name: str<br />  The three-level (fully qualified) name of the volume</td>
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
    <td>The identifier of the catalog</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The three-level (fully qualified) name of the volume</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The identifier of the schema</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>string</code></td>
    <td>Whether to include volumes in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of volumes to return (page length). If not set, the page length is set to a server configured value (10000, as of 1/29/2024). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value (10000, as of 1/29/2024); - when set to 0, the page length is set to a server configured value (10000, as of 1/29/2024) (recommended); - when set to a value less than 0, an invalid parameter error is returned; Note: this parameter controls only the maximum number of volumes to return. The actual number of volumes returned in a page may be smaller than this value, including 0, even if there are more pages.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque token returned by a previous request. It must be included in the request to retrieve the next page of results (pagination).</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="read"
    values={[
        { label: 'read', value: 'read' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="read">

Gets a volume from the metastore for a specific catalog and schema.<br /><br />The caller must be a metastore admin or an owner of (or have the **READ VOLUME** privilege on) the<br />volume. For the latter case, the caller must also be the owner or have the **USE_CATALOG** privilege<br />on the parent catalog and the **USE_SCHEMA** privilege on the parent schema.<br /><br />:param name: str<br />  The three-level (fully qualified) name of the volume<br />:param include_browse: bool (optional)<br />  Whether to include volumes in the response for which the principal can only access selective<br />  metadata for<br /><br />:returns: :class:`VolumeInfo`

```sql
SELECT
name,
metastore_id,
volume_id,
catalog_name,
full_name,
schema_name,
access_point,
browse_only,
comment,
created_at,
created_by,
encryption_details,
owner,
storage_location,
updated_at,
updated_by,
volume_type
FROM databricks_workspace.catalog.volumes
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of volumes for the current metastore under the parent catalog and schema.<br /><br />The returned volumes are filtered based on the privileges of the calling user. For example, the<br />metastore admin is able to list all the volumes. A regular user needs to be the owner or have the<br />**READ VOLUME** privilege on the volume to receive the volumes in the response. For the latter case,<br />the caller must also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the<br />**USE_SCHEMA** privilege on the parent schema.<br /><br />There is no guarantee of a specific ordering of the elements in the array.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str<br />  The identifier of the catalog<br />:param schema_name: str<br />  The identifier of the schema<br />:param include_browse: bool (optional)<br />  Whether to include volumes in the response for which the principal can only access selective<br />  metadata for<br />:param max_results: int (optional)<br />  Maximum number of volumes to return (page length).<br /><br />  If not set, the page length is set to a server configured value (10000, as of 1/29/2024). - when set<br />  to a value greater than 0, the page length is the minimum of this value and a server configured<br />  value (10000, as of 1/29/2024); - when set to 0, the page length is set to a server configured value<br />  (10000, as of 1/29/2024) (recommended); - when set to a value less than 0, an invalid parameter<br />  error is returned;<br /><br />  Note: this parameter controls only the maximum number of volumes to return. The actual number of<br />  volumes returned in a page may be smaller than this value, including 0, even if there are more<br />  pages.<br />:param page_token: str (optional)<br />  Opaque token returned by a previous request. It must be included in the request to retrieve the next<br />  page of results (pagination).<br /><br />:returns: Iterator over :class:`VolumeInfo`

```sql
SELECT
name,
metastore_id,
volume_id,
catalog_name,
full_name,
schema_name,
access_point,
browse_only,
comment,
created_at,
created_by,
encryption_details,
owner,
storage_location,
updated_at,
updated_by,
volume_type
FROM databricks_workspace.catalog.volumes
WHERE catalog_name = '{{ catalog_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
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

Creates a new volume.<br /><br />The user could create either an external volume or a managed volume. An external volume will be<br />created in the specified external location, while a managed volume will be located in the default<br />location which is specified by the parent schema, or the parent catalog, or the Metastore.<br /><br />For the volume creation to succeed, the user must satisfy following conditions: - The caller must be a<br />metastore admin, or be the owner of the parent catalog and schema, or have the **USE_CATALOG**<br />privilege on the parent catalog and the **USE_SCHEMA** privilege on the parent schema. - The caller<br />must have **CREATE VOLUME** privilege on the parent schema.<br /><br />For an external volume, following conditions also need to satisfy - The caller must have **CREATE<br />EXTERNAL VOLUME** privilege on the external location. - There are no other tables, nor volumes<br />existing in the specified storage location. - The specified storage location is not under the location<br />of other tables, nor volumes, or catalogs or schemas.<br /><br />:param catalog_name: str<br />  The name of the catalog where the schema and the volume are<br />:param schema_name: str<br />  The name of the schema where the volume is<br />:param name: str<br />  The name of the volume<br />:param volume_type: :class:`VolumeType`<br />  The type of the volume. An external volume is located in the specified external location. A managed<br />  volume is located in the default location which is specified by the parent schema, or the parent<br />  catalog, or the Metastore. [Learn more]<br /><br />  [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external<br />:param comment: str (optional)<br />  The comment attached to the volume<br />:param storage_location: str (optional)<br />  The storage location on the cloud<br /><br />:returns: :class:`VolumeInfo`

```sql
INSERT INTO databricks_workspace.catalog.volumes (
data__catalog_name,
data__schema_name,
data__name,
data__volume_type,
data__comment,
data__storage_location,
deployment_name
)
SELECT 
'{{ catalog_name }}' /* required */,
'{{ schema_name }}' /* required */,
'{{ name }}' /* required */,
'{{ volume_type }}' /* required */,
'{{ comment }}',
'{{ storage_location }}',
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
volume_id,
catalog_name,
full_name,
schema_name,
access_point,
browse_only,
comment,
created_at,
created_by,
encryption_details,
owner,
storage_location,
updated_at,
updated_by,
volume_type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: volumes
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the volumes resource.
    - name: catalog_name
      value: string
      description: |
        The name of the catalog where the schema and the volume are
    - name: schema_name
      value: string
      description: |
        The name of the schema where the volume is
    - name: name
      value: string
      description: |
        The name of the volume
    - name: volume_type
      value: string
      description: |
        The type of the volume. An external volume is located in the specified external location. A managed volume is located in the default location which is specified by the parent schema, or the parent catalog, or the Metastore. [Learn more] [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external
    - name: comment
      value: string
      description: |
        The comment attached to the volume
    - name: storage_location
      value: string
      description: |
        The storage location on the cloud
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

Updates the specified volume under the specified parent catalog and schema.<br /><br />The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must<br />also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**<br />privilege on the parent schema.<br /><br />Currently only the name, the owner or the comment of the volume could be updated.<br /><br />:param name: str<br />  The three-level (fully qualified) name of the volume<br />:param comment: str (optional)<br />  The comment attached to the volume<br />:param new_name: str (optional)<br />  New name for the volume.<br />:param owner: str (optional)<br />  The identifier of the user who owns the volume<br /><br />:returns: :class:`VolumeInfo`

```sql
UPDATE databricks_workspace.catalog.volumes
SET 
data__comment = '{{ comment }}',
data__new_name = '{{ new_name }}',
data__owner = '{{ owner }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
metastore_id,
volume_id,
catalog_name,
full_name,
schema_name,
access_point,
browse_only,
comment,
created_at,
created_by,
encryption_details,
owner,
storage_location,
updated_at,
updated_by,
volume_type;
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

Deletes a volume from the specified parent catalog and schema.<br /><br />The caller must be a metastore admin or an owner of the volume. For the latter case, the caller must<br />also be the owner or have the **USE_CATALOG** privilege on the parent catalog and the **USE_SCHEMA**<br />privilege on the parent schema.<br /><br />:param name: str<br />  The three-level (fully qualified) name of the volume

```sql
DELETE FROM databricks_workspace.catalog.volumes
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

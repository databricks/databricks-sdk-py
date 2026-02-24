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
<tr><td><b>Name</b></td><td><CopyableCode code="volumes" /></td></tr>
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
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request. (AWS_SSE_KMS, AWS_SSE_S3)"
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
    "description": "The type of the volume. An external volume is located in the specified external location. A managed volume is located in the default location which is specified by the parent schema, or the parent catalog, or the Metastore. [Learn more] [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external (EXTERNAL, MANAGED)"
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
            "description": "Sets the value of the 'x-amz-server-side-encryption' header in S3 request. (AWS_SSE_KMS, AWS_SSE_S3)"
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
    "description": "The type of the volume. An external volume is located in the specified external location. A managed volume is located in the default location which is specified by the parent schema, or the parent catalog, or the Metastore. [Learn more] [Learn more]: https://docs.databricks.com/aws/en/volumes/managed-vs-external (EXTERNAL, MANAGED)"
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Gets a volume from the metastore for a specific catalog and schema.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of volumes for the current metastore under the parent catalog and schema.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-volume_type"><code>volume_type</code></a></td>
    <td></td>
    <td>Creates a new volume.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates the specified volume under the specified parent catalog and schema.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes a volume from the specified parent catalog and schema.</td>
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
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include volumes in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
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

Gets a volume from the metastore for a specific catalog and schema.

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
AND workspace = '{{ workspace }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of volumes for the current metastore under the parent catalog and schema.

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
AND workspace = '{{ workspace }}' -- required
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

Creates a new volume.

```sql
INSERT INTO databricks_workspace.catalog.volumes (
catalog_name,
schema_name,
name,
volume_type,
comment,
storage_location,
workspace
)
SELECT 
'{{ catalog_name }}' /* required */,
'{{ schema_name }}' /* required */,
'{{ name }}' /* required */,
'{{ volume_type }}' /* required */,
'{{ comment }}',
'{{ storage_location }}',
'{{ workspace }}'
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
    - name: workspace
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

Updates the specified volume under the specified parent catalog and schema.

```sql
UPDATE databricks_workspace.catalog.volumes
SET 
comment = '{{ comment }}',
new_name = '{{ new_name }}',
owner = '{{ owner }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
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

Deletes a volume from the specified parent catalog and schema.

```sql
DELETE FROM databricks_workspace.catalog.volumes
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

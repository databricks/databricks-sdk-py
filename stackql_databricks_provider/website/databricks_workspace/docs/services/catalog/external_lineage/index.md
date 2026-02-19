---
title: external_lineage
hide_title: false
hide_table_of_contents: false
keywords:
  - external_lineage
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

Creates, updates, deletes, gets or lists an <code>external_lineage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="external_lineage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.external_lineage" /></td></tr>
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
    "name": "external_lineage_info",
    "type": "object",
    "description": "Information about the edge metadata of the external lineage relationship.",
    "children": [
      {
        "name": "source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "external_metadata",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "model_version",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "version",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "path",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "table",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "target",
        "type": "object",
        "description": "Target object of the external lineage relationship.",
        "children": [
          {
            "name": "external_metadata",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "model_version",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "version",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "path",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "table",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "columns",
        "type": "array",
        "description": "List of column relationships between source and target objects.",
        "children": [
          {
            "name": "source",
            "type": "string",
            "description": ""
          },
          {
            "name": "target",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "id",
        "type": "string",
        "description": "Unique identifier of the external lineage relationship."
      },
      {
        "name": "properties",
        "type": "object",
        "description": "Key-value properties associated with the external lineage relationship."
      }
    ]
  },
  {
    "name": "external_metadata_info",
    "type": "object",
    "description": "Information about external metadata involved in the lineage relationship.",
    "children": [
      {
        "name": "entity_type",
        "type": "string",
        "description": "Type of entity represented by the external metadata object."
      },
      {
        "name": "event_time",
        "type": "string",
        "description": "Timestamp of the lineage event."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the external metadata object."
      },
      {
        "name": "system_type",
        "type": "string",
        "description": "Type of external system. (AMAZON_REDSHIFT, AZURE_SYNAPSE, CONFLUENT, DATABRICKS, GOOGLE_BIGQUERY, KAFKA, LOOKER, MICROSOFT_FABRIC, MICROSOFT_SQL_SERVER, MONGODB, MYSQL, ORACLE, OTHER, POSTGRESQL, POWER_BI, SALESFORCE, SAP, SERVICENOW, SNOWFLAKE, STREAM_NATIVE, TABLEAU, TERADATA, WORKDAY)"
      }
    ]
  },
  {
    "name": "file_info",
    "type": "object",
    "description": "Information about the file involved in the lineage relationship.",
    "children": [
      {
        "name": "event_time",
        "type": "string",
        "description": "Timestamp of the lineage event."
      },
      {
        "name": "path",
        "type": "string",
        "description": "URL of the path."
      },
      {
        "name": "securable_name",
        "type": "string",
        "description": "The full name of the securable on the path."
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The securable type of the securable on the path."
      },
      {
        "name": "storage_location",
        "type": "string",
        "description": "The storage location associated with securable on the path."
      }
    ]
  },
  {
    "name": "model_info",
    "type": "object",
    "description": "Information about the model version involved in the lineage relationship.",
    "children": [
      {
        "name": "event_time",
        "type": "string",
        "description": "Timestamp of the lineage event."
      },
      {
        "name": "model_name",
        "type": "string",
        "description": "Name of the model."
      },
      {
        "name": "version",
        "type": "integer",
        "description": "Version number of the model."
      }
    ]
  },
  {
    "name": "table_info",
    "type": "object",
    "description": "Information about the table involved in the lineage relationship.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": "Name of Catalog."
      },
      {
        "name": "event_time",
        "type": "string",
        "description": "Timestamp of the lineage event."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of Table."
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "Name of Schema."
      }
    ]
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
    <td><a href="#parameter-object_info"><code>object_info</code></a>, <a href="#parameter-lineage_direction"><code>lineage_direction</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists external lineage relationships of a Databricks object or external metadata given a supplied</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-external_lineage_relationship"><code>external_lineage_relationship</code></a></td>
    <td></td>
    <td>Creates an external lineage relationship between a Databricks or external metadata object and another</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-external_lineage_relationship"><code>external_lineage_relationship</code></a></td>
    <td></td>
    <td>Updates an external lineage relationship between a Databricks or external metadata object and another</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-external_lineage_relationship"><code>external_lineage_relationship</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an external lineage relationship between a Databricks or external metadata object and another</td>
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
<tr id="parameter-external_lineage_relationship">
    <td><CopyableCode code="external_lineage_relationship" /></td>
    <td><code>string</code></td>
    <td>:class:`DeleteRequestExternalLineage`</td>
</tr>
<tr id="parameter-lineage_direction">
    <td><CopyableCode code="lineage_direction" /></td>
    <td><code>string</code></td>
    <td>The lineage direction to filter on.</td>
</tr>
<tr id="parameter-object_info">
    <td><CopyableCode code="object_info" /></td>
    <td><code>string</code></td>
    <td>The object to query external lineage relationships for. Since this field is a query parameter, please flatten the nested fields. For example, if the object is a table, the query parameter should look like: `object_info.table.name=main.sales.customers`</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Specifies the maximum number of external lineage relationships to return in a single response. The value must be less than or equal to 1000.</td>
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

Lists external lineage relationships of a Databricks object or external metadata given a supplied

```sql
SELECT
external_lineage_info,
external_metadata_info,
file_info,
model_info,
table_info
FROM databricks_workspace.catalog.external_lineage
WHERE object_info = '{{ object_info }}' -- required
AND lineage_direction = '{{ lineage_direction }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Creates an external lineage relationship between a Databricks or external metadata object and another

```sql
INSERT INTO databricks_workspace.catalog.external_lineage (
external_lineage_relationship,
deployment_name
)
SELECT 
'{{ external_lineage_relationship }}' /* required */,
'{{ deployment_name }}'
RETURNING
id,
columns,
properties,
source,
target
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: external_lineage
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the external_lineage resource.
    - name: external_lineage_relationship
      value: string
      description: |
        :returns: :class:`ExternalLineageRelationship`
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

Updates an external lineage relationship between a Databricks or external metadata object and another

```sql
UPDATE databricks_workspace.catalog.external_lineage
SET 
external_lineage_relationship = '{{ external_lineage_relationship }}'
WHERE 
update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND external_lineage_relationship = '{{ external_lineage_relationship }}' --required
RETURNING
id,
columns,
properties,
source,
target;
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

Deletes an external lineage relationship between a Databricks or external metadata object and another

```sql
DELETE FROM databricks_workspace.catalog.external_lineage
WHERE external_lineage_relationship = '{{ external_lineage_relationship }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

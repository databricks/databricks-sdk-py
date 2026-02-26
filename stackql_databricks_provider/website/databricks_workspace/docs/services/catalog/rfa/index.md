---
title: rfa
hide_title: false
hide_table_of_contents: false
keywords:
  - rfa
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

Creates, updates, deletes, gets or lists a <code>rfa</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rfa" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.rfa" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_destinations"
    values={[
        { label: 'get_destinations', value: 'get_destinations' }
    ]}
>
<TabItem value="get_destinations">

<SchemaTable fields={[
  {
    "name": "full_name",
    "type": "string",
    "description": "The full name of the securable. Redundant with the name in the securable object, but necessary for Terraform integration"
  },
  {
    "name": "are_any_destinations_hidden",
    "type": "boolean",
    "description": "Indicates whether any destinations are hidden from the caller due to a lack of permissions. This value is true if the caller does not have permission to see all destinations."
  },
  {
    "name": "destination_source_securable",
    "type": "object",
    "description": "Generic definition of a securable, which is uniquely defined in a metastore by its type and full<br />    name.",
    "children": [
      {
        "name": "full_name",
        "type": "string",
        "description": "Required. The full name of the catalog/schema/table. Optional if resource_name is present."
      },
      {
        "name": "provider_share",
        "type": "string",
        "description": "Optional. The name of the Share object that contains the securable when the securable is getting shared in D2D Delta Sharing."
      },
      {
        "name": "type",
        "type": "string",
        "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
      }
    ]
  },
  {
    "name": "destinations",
    "type": "array",
    "description": "The access request destinations for the securable.",
    "children": [
      {
        "name": "destination_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "destination_type",
        "type": "string",
        "description": "The type of the destination. (EMAIL, GENERIC_WEBHOOK, MICROSOFT_TEAMS, SLACK, URL)"
      },
      {
        "name": "special_destination",
        "type": "string",
        "description": "This field is used to denote whether the destination is the email of the owner of the securable object. The special destination cannot be assigned to a securable and only represents the default destination of the securable. The securable types that support default special destinations are: \"catalog\", \"external_location\", \"connection\", \"credential\", and \"metastore\". The **destination_type** of a **special_destination** is always EMAIL. (SPECIAL_DESTINATION_CATALOG_OWNER, SPECIAL_DESTINATION_CONNECTION_OWNER, SPECIAL_DESTINATION_CREDENTIAL_OWNER, SPECIAL_DESTINATION_EXTERNAL_LOCATION_OWNER, SPECIAL_DESTINATION_METASTORE_OWNER)"
      }
    ]
  },
  {
    "name": "securable",
    "type": "object",
    "description": "Generic definition of a securable, which is uniquely defined in a metastore by its type and full<br />    name.",
    "children": [
      {
        "name": "full_name",
        "type": "string",
        "description": "Required. The full name of the catalog/schema/table. Optional if resource_name is present."
      },
      {
        "name": "provider_share",
        "type": "string",
        "description": "Optional. The name of the Share object that contains the securable when the securable is getting shared in D2D Delta Sharing."
      },
      {
        "name": "type",
        "type": "string",
        "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
      }
    ]
  },
  {
    "name": "securable_type",
    "type": "string",
    "description": "The type of the securable. Redundant with the type in the securable object, but necessary for Terraform integration"
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
    <td><a href="#get_destinations"><CopyableCode code="get_destinations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an array of access request destinations for the specified securable. Any caller can see URL</td>
</tr>
<tr>
    <td><a href="#batch_create"><CopyableCode code="batch_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates access requests for Unity Catalog permissions for a specified principal on a securable object.</td>
</tr>
<tr>
    <td><a href="#update_destinations"><CopyableCode code="update_destinations" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-access_request_destinations"><code>access_request_destinations</code></a></td>
    <td></td>
    <td>Updates the access request destinations for the given securable. The caller must be a metastore admin,</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>The full name of the securable.</td>
</tr>
<tr id="parameter-securable_type">
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>The type of the securable.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_destinations"
    values={[
        { label: 'get_destinations', value: 'get_destinations' }
    ]}
>
<TabItem value="get_destinations">

Gets an array of access request destinations for the specified securable. Any caller can see URL

```sql
SELECT
full_name,
are_any_destinations_hidden,
destination_source_securable,
destinations,
securable,
securable_type
FROM databricks_workspace.catalog.rfa
WHERE securable_type = '{{ securable_type }}' -- required
AND full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="batch_create"
    values={[
        { label: 'batch_create', value: 'batch_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="batch_create">

Creates access requests for Unity Catalog permissions for a specified principal on a securable object.

```sql
INSERT INTO databricks_workspace.catalog.rfa (
requests,
deployment_name
)
SELECT 
'{{ requests }}',
'{{ deployment_name }}'
RETURNING
responses
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: rfa
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the rfa resource.
    - name: requests
      description: |
        A list of individual access requests, where each request corresponds to a set of permissions being requested on a list of securables for a specified principal. At most 30 requests per API call.
      value:
        - behalf_of:
            id: "{{ id }}"
            principal_type: "{{ principal_type }}"
          comment: "{{ comment }}"
          securable_permissions: "{{ securable_permissions }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_destinations"
    values={[
        { label: 'update_destinations', value: 'update_destinations' }
    ]}
>
<TabItem value="update_destinations">

Updates the access request destinations for the given securable. The caller must be a metastore admin,

```sql
UPDATE databricks_workspace.catalog.rfa
SET 
access_request_destinations = '{{ access_request_destinations }}'
WHERE 
update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND access_request_destinations = '{{ access_request_destinations }}' --required
RETURNING
full_name,
are_any_destinations_hidden,
destination_source_securable,
destinations,
securable,
securable_type;
```
</TabItem>
</Tabs>

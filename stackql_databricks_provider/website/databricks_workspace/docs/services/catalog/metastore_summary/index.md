---
title: metastore_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - metastore_summary
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

Creates, updates, deletes, gets or lists a <code>metastore_summary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metastore_summary" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.metastore_summary" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    "description": "The scope of Delta Sharing enabled for the metastore. (INTERNAL, INTERNAL_AND_EXTERNAL)"
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets information about a metastore. This summary includes the storage credential, the cloud vendor,</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets information about a metastore. This summary includes the storage credential, the cloud vendor,

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
FROM databricks_workspace.catalog.metastore_summary
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>

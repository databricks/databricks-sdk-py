---
title: consumer_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_providers
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>consumer_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="consumer_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_providers" /></td></tr>
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
    "name": "provider",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "business_contact_email",
        "type": "string",
        "description": ""
      },
      {
        "name": "term_of_service_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "privacy_policy_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "company_website_link",
        "type": "string",
        "description": ""
      },
      {
        "name": "dark_mode_icon_file_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "dark_mode_icon_file_path",
        "type": "string",
        "description": ""
      },
      {
        "name": "description",
        "type": "string",
        "description": ""
      },
      {
        "name": "icon_file_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "icon_file_path",
        "type": "string",
        "description": ""
      },
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "is_featured",
        "type": "boolean",
        "description": "is_featured is accessible by consumers only"
      },
      {
        "name": "published_by",
        "type": "string",
        "description": "published_by is only applicable to data aggregators (e.g. Crux)"
      },
      {
        "name": "support_contact_email",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "dark_mode_icon_file_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "icon_file_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "business_contact_email",
    "type": "string",
    "description": ""
  },
  {
    "name": "company_website_link",
    "type": "string",
    "description": ""
  },
  {
    "name": "dark_mode_icon_file_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "icon_file_path",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_featured",
    "type": "boolean",
    "description": "is_featured is accessible by consumers only"
  },
  {
    "name": "privacy_policy_link",
    "type": "string",
    "description": ""
  },
  {
    "name": "published_by",
    "type": "string",
    "description": "published_by is only applicable to data aggregators (e.g. Crux)"
  },
  {
    "name": "support_contact_email",
    "type": "string",
    "description": ""
  },
  {
    "name": "term_of_service_link",
    "type": "string",
    "description": ""
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
    <td>Get a provider in the Databricks Marketplace with at least one visible listing.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-is_featured"><code>is_featured</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all providers in the Databricks Marketplace with at least one visible listing.</td>
</tr>
<tr>
    <td><a href="#batch_get"><CopyableCode code="batch_get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-ids"><code>ids</code></a></td>
    <td>Batch get a provider in the Databricks Marketplace with at least one visible listing.</td>
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
    <td>:returns: :class:`GetProviderResponse`</td>
</tr>
<tr id="parameter-ids">
    <td><CopyableCode code="ids" /></td>
    <td><code>array</code></td>
    <td>:returns: :class:`BatchGetProvidersResponse`</td>
</tr>
<tr id="parameter-is_featured">
    <td><CopyableCode code="is_featured" /></td>
    <td><code>boolean</code></td>
    <td>:param page_size: int (optional)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>:returns: Iterator over :class:`ProviderInfo`</td>
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

Get a provider in the Databricks Marketplace with at least one visible listing.

```sql
SELECT
provider
FROM databricks_workspace.marketplace.consumer_providers
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all providers in the Databricks Marketplace with at least one visible listing.

```sql
SELECT
id,
name,
dark_mode_icon_file_id,
icon_file_id,
business_contact_email,
company_website_link,
dark_mode_icon_file_path,
description,
icon_file_path,
is_featured,
privacy_policy_link,
published_by,
support_contact_email,
term_of_service_link
FROM databricks_workspace.marketplace.consumer_providers
WHERE deployment_name = '{{ deployment_name }}' -- required
AND is_featured = '{{ is_featured }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch_get"
    values={[
        { label: 'batch_get', value: 'batch_get' }
    ]}
>
<TabItem value="batch_get">

Batch get a provider in the Databricks Marketplace with at least one visible listing.

```sql
EXEC databricks_workspace.marketplace.consumer_providers.batch_get 
@deployment_name='{{ deployment_name }}' --required, 
@ids='{{ ids }}'
;
```
</TabItem>
</Tabs>

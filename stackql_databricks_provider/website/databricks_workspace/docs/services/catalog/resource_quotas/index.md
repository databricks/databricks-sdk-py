---
title: resource_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_quotas
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

Creates, updates, deletes, gets or lists a <code>resource_quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.resource_quotas" /></td></tr>
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
    "name": "quota_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "last_refreshed_at",
        "type": "integer",
        "description": ""
      },
      {
        "name": "parent_full_name",
        "type": "string",
        "description": "Name of the parent resource. Returns metastore ID if the parent is a metastore."
      },
      {
        "name": "parent_securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable."
      },
      {
        "name": "quota_count",
        "type": "integer",
        "description": "The current usage of the resource quota."
      },
      {
        "name": "quota_limit",
        "type": "integer",
        "description": "The current limit of the resource quota."
      },
      {
        "name": "quota_name",
        "type": "string",
        "description": "The name of the quota."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "parent_full_name",
    "type": "string",
    "description": "Name of the parent resource. Returns metastore ID if the parent is a metastore."
  },
  {
    "name": "quota_name",
    "type": "string",
    "description": "The name of the quota."
  },
  {
    "name": "last_refreshed_at",
    "type": "integer",
    "description": ""
  },
  {
    "name": "parent_securable_type",
    "type": "string",
    "description": "The type of Unity Catalog securable."
  },
  {
    "name": "quota_count",
    "type": "integer",
    "description": "The current usage of the resource quota."
  },
  {
    "name": "quota_limit",
    "type": "integer",
    "description": "The current limit of the resource quota."
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
    <td><a href="#parameter-parent_securable_type"><code>parent_securable_type</code></a>, <a href="#parameter-parent_full_name"><code>parent_full_name</code></a>, <a href="#parameter-quota_name"><code>quota_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>The GetQuota API returns usage information for a single resource quota, defined as a child-parent<br />pair. This API also refreshes the quota count if it is out of date. Refreshes are triggered<br />asynchronously. The updated count might not be returned in the first call.<br /><br />:param parent_securable_type: str<br />  Securable type of the quota parent.<br />:param parent_full_name: str<br />  Full name of the parent resource. Provide the metastore ID if the parent is a metastore.<br />:param quota_name: str<br />  Name of the quota. Follows the pattern of the quota type, with "-quota" added as a suffix.<br /><br />:returns: :class:`GetQuotaResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>ListQuotas returns all quota values under the metastore. There are no SLAs on the freshness of the<br />counts returned. This API does not trigger a refresh of quota counts.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param max_results: int (optional)<br />  The number of quotas to return.<br />:param page_token: str (optional)<br />  Opaque token for the next page of results.<br /><br />:returns: Iterator over :class:`QuotaInfo`</td>
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
<tr id="parameter-parent_full_name">
    <td><CopyableCode code="parent_full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of the parent resource. Provide the metastore ID if the parent is a metastore.</td>
</tr>
<tr id="parameter-parent_securable_type">
    <td><CopyableCode code="parent_securable_type" /></td>
    <td><code>string</code></td>
    <td>Securable type of the quota parent.</td>
</tr>
<tr id="parameter-quota_name">
    <td><CopyableCode code="quota_name" /></td>
    <td><code>string</code></td>
    <td>Name of the quota. Follows the pattern of the quota type, with "-quota" added as a suffix.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>The number of quotas to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque token for the next page of results.</td>
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

The GetQuota API returns usage information for a single resource quota, defined as a child-parent<br />pair. This API also refreshes the quota count if it is out of date. Refreshes are triggered<br />asynchronously. The updated count might not be returned in the first call.<br /><br />:param parent_securable_type: str<br />  Securable type of the quota parent.<br />:param parent_full_name: str<br />  Full name of the parent resource. Provide the metastore ID if the parent is a metastore.<br />:param quota_name: str<br />  Name of the quota. Follows the pattern of the quota type, with "-quota" added as a suffix.<br /><br />:returns: :class:`GetQuotaResponse`

```sql
SELECT
quota_info
FROM databricks_workspace.catalog.resource_quotas
WHERE parent_securable_type = '{{ parent_securable_type }}' -- required
AND parent_full_name = '{{ parent_full_name }}' -- required
AND quota_name = '{{ quota_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

ListQuotas returns all quota values under the metastore. There are no SLAs on the freshness of the<br />counts returned. This API does not trigger a refresh of quota counts.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param max_results: int (optional)<br />  The number of quotas to return.<br />:param page_token: str (optional)<br />  Opaque token for the next page of results.<br /><br />:returns: Iterator over :class:`QuotaInfo`

```sql
SELECT
parent_full_name,
quota_name,
last_refreshed_at,
parent_securable_type,
quota_count,
quota_limit
FROM databricks_workspace.catalog.resource_quotas
WHERE deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

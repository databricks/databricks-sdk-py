---
title: provider_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_shares
  - sharing
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

Creates, updates, deletes, gets or lists a <code>provider_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.provider_shares" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_shares"
    values={[
        { label: 'list_shares', value: 'list_shares' }
    ]}
>
<TabItem value="list_shares">

<SchemaTable fields={[
  {
    "name": "name",
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
    <td><a href="#list_shares"><CopyableCode code="list_shares" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of a specified provider's shares within the metastore where:<br /><br />* the caller is a metastore admin, or * the caller is the owner.<br /><br />:param name: str<br />  Name of the provider in which to list shares.<br />:param max_results: int (optional)<br />  Maximum number of shares to return. - when set to 0, the page length is set to a server configured<br />  value (recommended); - when set to a value greater than 0, the page length is the minimum of this<br />  value and a server configured value; - when set to a value less than 0, an invalid parameter error<br />  is returned; - If not set, all valid shares are returned (not recommended). - Note: The number of<br />  returned shares might be less than the specified max_results size, even zero. The only definitive<br />  indication that no further shares can be fetched is when the next_page_token is unset from the<br />  response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`ProviderShare`</td>
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
    <td>Name of the provider in which to list shares.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of shares to return. - when set to 0, the page length is set to a server configured value (recommended); - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to a value less than 0, an invalid parameter error is returned; - If not set, all valid shares are returned (not recommended). - Note: The number of returned shares might be less than the specified max_results size, even zero. The only definitive indication that no further shares can be fetched is when the next_page_token is unset from the response.</td>
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
    defaultValue="list_shares"
    values={[
        { label: 'list_shares', value: 'list_shares' }
    ]}
>
<TabItem value="list_shares">

Gets an array of a specified provider's shares within the metastore where:<br /><br />* the caller is a metastore admin, or * the caller is the owner.<br /><br />:param name: str<br />  Name of the provider in which to list shares.<br />:param max_results: int (optional)<br />  Maximum number of shares to return. - when set to 0, the page length is set to a server configured<br />  value (recommended); - when set to a value greater than 0, the page length is the minimum of this<br />  value and a server configured value; - when set to a value less than 0, an invalid parameter error<br />  is returned; - If not set, all valid shares are returned (not recommended). - Note: The number of<br />  returned shares might be less than the specified max_results size, even zero. The only definitive<br />  indication that no further shares can be fetched is when the next_page_token is unset from the<br />  response.<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br /><br />:returns: Iterator over :class:`ProviderShare`

```sql
SELECT
name
FROM databricks_workspace.sharing.provider_shares
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

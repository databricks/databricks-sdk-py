---
title: billable_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - billable_usage
  - billing
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>billable_usage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billable_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.billable_usage" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="billable_usage_download"
    values={[
        { label: 'billable_usage_download', value: 'billable_usage_download' }
    ]}
>
<TabItem value="billable_usage_download">

<SchemaTable fields={[
  {
    "name": "contents",
    "type": "string (binary)",
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
    <td><a href="#billable_usage_download"><CopyableCode code="billable_usage_download" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-start_month"><code>start_month</code></a>, <a href="#parameter-end_month"><code>end_month</code></a></td>
    <td><a href="#parameter-personal_data"><code>personal_data</code></a></td>
    <td>Returns billable usage logs in CSV format for the specified account and date range. For the data</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-end_month">
    <td><CopyableCode code="end_month" /></td>
    <td><code>string</code></td>
    <td>Format: `YYYY-MM`. Last month to return billable usage logs for. This field is required.</td>
</tr>
<tr id="parameter-start_month">
    <td><CopyableCode code="start_month" /></td>
    <td><code>string</code></td>
    <td>Format specification for month in the format `YYYY-MM`. This is used to specify billable usage `start_month` and `end_month` properties. **Note**: Billable usage logs are unavailable before March 2019 (`2019-03`).</td>
</tr>
<tr id="parameter-personal_data">
    <td><CopyableCode code="personal_data" /></td>
    <td><code>string</code></td>
    <td>Specify whether to include personally identifiable information in the billable usage logs, for example the email addresses of cluster creators. Handle this information with care. Defaults to false.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="billable_usage_download"
    values={[
        { label: 'billable_usage_download', value: 'billable_usage_download' }
    ]}
>
<TabItem value="billable_usage_download">

Returns billable usage logs in CSV format for the specified account and date range. For the data

```sql
SELECT
contents
FROM databricks_account.billing.billable_usage
WHERE account_id = '{{ account_id }}' -- required
AND start_month = '{{ start_month }}' -- required
AND end_month = '{{ end_month }}' -- required
AND personal_data = '{{ personal_data }}'
;
```
</TabItem>
</Tabs>

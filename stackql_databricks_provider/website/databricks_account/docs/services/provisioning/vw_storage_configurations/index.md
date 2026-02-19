---
title: vw_storage_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_storage_configurations
  - provisioning
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

Creates, updates, deletes, gets or lists a <code>vw_storage_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_storage_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_storage_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the storage configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_configuration_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the storage configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the storage configuration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="role_arn" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ARN of the AWS IAM role used to access the root storage bucket (AWS only).</td>
</tr>
<tr>
    <td><CopyableCode code="root_bucket_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the S3 bucket used as the workspace root storage (AWS only).</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Databricks account ID used to scope the query.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  account_id,
  storage_configuration_id,
  storage_configuration_name,
  creation_time,
  role_arn,
  root_bucket_name
FROM databricks_account.provisioning.vw_storage_configurations
WHERE account_id = '{{ account_id }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  s.account_id,
  s.storage_configuration_id,
  s.storage_configuration_name,
  s.creation_time,
  s.role_arn,
  JSON_EXTRACT(s.root_bucket_info, '$.bucket_name') AS root_bucket_name
FROM databricks_account.provisioning.storage s
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  s.account_id,
  s.storage_configuration_id,
  s.storage_configuration_name,
  s.creation_time,
  s.role_arn,
  s.root_bucket_info->>'bucket_name' AS root_bucket_name
FROM databricks_account.provisioning.storage s
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

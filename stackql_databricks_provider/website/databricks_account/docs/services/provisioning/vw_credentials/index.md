---
title: vw_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_credentials
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_credentials" /></td></tr>
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
    <td><CopyableCode code="credentials_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the credential configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the credential configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Unix timestamp (ms) when the credential configuration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="aws_role_arn" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ARN of the AWS IAM role Databricks uses to manage resources in the customer account (AWS only).</td>
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
  credentials_id,
  credentials_name,
  creation_time,
  aws_role_arn
FROM databricks_account.provisioning.vw_credentials
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
  c.account_id,
  c.credentials_id,
  c.credentials_name,
  c.creation_time,
  JSON_EXTRACT(c.aws_credentials, '$.sts_role.role_arn') AS aws_role_arn
FROM databricks_account.provisioning.credentials c
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  c.account_id,
  c.credentials_id,
  c.credentials_name,
  c.creation_time,
  c.aws_credentials->'sts_role'->>'role_arn' AS aws_role_arn
FROM databricks_account.provisioning.credentials c
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

---
title: vw_users
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_users
  - iam
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

Creates, updates, deletes, gets or lists a <code>vw_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_users" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.vw_users" /></td></tr>
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
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name used to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the workspace user.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username (typically email address) of the workspace user.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable display name of the workspace user.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the user account is active.</td>
</tr>
<tr>
    <td><CopyableCode code="externalId" /></td>
    <td><CopyableCode code="string" /></td>
    <td>External identity provider ID for the user (SCIM provisioned users only).</td>
</tr>
<tr>
    <td><CopyableCode code="givenName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>First (given) name of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="familyName" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Last (family) name of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Email address for this entry (one row per email address).</td>
</tr>
<tr>
    <td><CopyableCode code="email_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type classification of the email address (e.g. work).</td>
</tr>
<tr>
    <td><CopyableCode code="is_primary" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether this email address is the user's primary email.</td>
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
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name used to scope the query.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  deployment_name,
  id,
  userName,
  displayName,
  active,
  externalId,
  givenName,
  familyName,
  email,
  email_type,
  is_primary
FROM databricks_workspace.iam.vw_users
WHERE deployment_name = '{{ deployment_name }}';
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
  u.deployment_name,
  u.id,
  u.userName,
  u.displayName,
  u.active,
  u.externalId,
  JSON_EXTRACT(u.name, '$.givenName') AS givenName,
  JSON_EXTRACT(u.name, '$.familyName') AS familyName,
  JSON_EXTRACT(e.value, '$.value') AS email,
  JSON_EXTRACT(e.value, '$.type') AS email_type,
  JSON_EXTRACT(e.value, '$.primary') AS is_primary
FROM databricks_workspace.iam.users_v2 u,
     JSON_EACH(u.emails) e
WHERE u.deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  u.deployment_name,
  u.id,
  u.userName,
  u.displayName,
  u.active,
  u.externalId,
  u.name->>'givenName' AS givenName,
  u.name->>'familyName' AS familyName,
  e.value->>'value' AS email,
  e.value->>'type' AS email_type,
  (e.value->>'primary')::boolean AS is_primary
FROM databricks_workspace.iam.users_v2 u,
     jsonb_array_elements(u.emails::jsonb) AS e
WHERE u.deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>

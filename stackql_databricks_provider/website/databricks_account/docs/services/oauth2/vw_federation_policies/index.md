---
title: vw_federation_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_federation_policies
  - oauth2
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

Creates, updates, deletes, gets or lists a <code>vw_federation_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_federation_policies" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.vw_federation_policies" /></td></tr>
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
    <td><CopyableCode code="policy_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Unique identifier for the federation policy.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Globally unique identifier for the federation policy.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable name of the federation policy.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Optional description of the federation policy.</td>
</tr>
<tr>
    <td><CopyableCode code="service_principal_id" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>ID of the service principal this federation policy is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the federation policy was created (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the federation policy was last updated (ISO 8601).</td>
</tr>
<tr>
    <td><CopyableCode code="oidc_issuer" /></td>
    <td><CopyableCode code="string" /></td>
    <td>OIDC token issuer URL for the federation policy.</td>
</tr>
<tr>
    <td><CopyableCode code="oidc_subject" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Expected subject claim value in the OIDC token.</td>
</tr>
<tr>
    <td><CopyableCode code="oidc_subject_claim" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Name of the claim in the OIDC token used as the subject identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="oidc_audiences" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of acceptable audience values in the OIDC token.</td>
</tr>
<tr>
    <td><CopyableCode code="oidc_jwks_uri" /></td>
    <td><CopyableCode code="string" /></td>
    <td>URI of the JWKS endpoint used to verify the OIDC token signature.</td>
</tr>
<tr>
    <td><CopyableCode code="oidc_jwks_json" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Inline JWKS JSON used to verify the OIDC token signature (alternative to jwks_uri).</td>
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
  policy_id,
  uid,
  name,
  description,
  service_principal_id,
  create_time,
  update_time,
  oidc_issuer,
  oidc_subject,
  oidc_subject_claim,
  oidc_audiences,
  oidc_jwks_uri,
  oidc_jwks_json
FROM databricks_account.oauth2.vw_federation_policies
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
  fp.account_id,
  fp.policy_id,
  fp.uid,
  fp.name,
  fp.description,
  fp.service_principal_id,
  fp.create_time,
  fp.update_time,
  JSON_EXTRACT(fp.oidc_policy, '$.issuer') AS oidc_issuer,
  JSON_EXTRACT(fp.oidc_policy, '$.subject') AS oidc_subject,
  JSON_EXTRACT(fp.oidc_policy, '$.subject_claim') AS oidc_subject_claim,
  JSON_EXTRACT(fp.oidc_policy, '$.audiences') AS oidc_audiences,
  JSON_EXTRACT(fp.oidc_policy, '$.jwks_uri') AS oidc_jwks_uri,
  JSON_EXTRACT(fp.oidc_policy, '$.jwks_json') AS oidc_jwks_json
FROM databricks_account.oauth2.account_federation_policy fp
WHERE account_id = '{{ account_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  fp.account_id,
  fp.policy_id,
  fp.uid,
  fp.name,
  fp.description,
  fp.service_principal_id,
  fp.create_time,
  fp.update_time,
  fp.oidc_policy->>'issuer' AS oidc_issuer,
  fp.oidc_policy->>'subject' AS oidc_subject,
  fp.oidc_policy->>'subject_claim' AS oidc_subject_claim,
  fp.oidc_policy->'audiences' AS oidc_audiences,
  fp.oidc_policy->>'jwks_uri' AS oidc_jwks_uri,
  fp.oidc_policy->>'jwks_json' AS oidc_jwks_json
FROM databricks_account.oauth2.account_federation_policy fp
WHERE account_id = '{{ account_id }}'
```

</TabItem>
</Tabs>

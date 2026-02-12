---
title: service_principal_federation_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_federation_policy
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>service_principal_federation_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_federation_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.service_principal_federation_policy" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="service_principal_federation_policy_get"
    values={[
        { label: 'service_principal_federation_policy_get', value: 'service_principal_federation_policy_get' },
        { label: 'service_principal_federation_policy_list', value: 'service_principal_federation_policy_list' }
    ]}
>
<TabItem value="service_principal_federation_policy_get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name for the federation policy. Example values include `accounts/<account-id>/federationPolicies/my-federation-policy` for Account Federation Policies, and `accounts/<account-id>/servicePrincipals/<service-principal-id>/federationPolicies/my-federation-policy` for Service Principal Federation Policies. Typically an output parameter, which does not need to be specified in create or update requests. If specified in a request, must match the value in the request URL."
  },
  {
    "name": "policy_id",
    "type": "string",
    "description": "The ID of the federation policy. Output only."
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": "The service principal ID that this federation policy applies to. Output only. Only set for service principal federation policies."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the federation policy."
  },
  {
    "name": "oidc_policy",
    "type": "object",
    "description": "Specifies the policy to use for validating OIDC claims in your federated tokens.",
    "children": [
      {
        "name": "audiences",
        "type": "array",
        "description": "The allowed token audiences, as specified in the 'aud' claim of federated tokens. The audience identifier is intended to represent the recipient of the token. Can be any non-empty string value. As long as the audience in the token matches at least one audience in the policy, the token is considered a match. If audiences is unspecified, defaults to your Databricks account id."
      },
      {
        "name": "issuer",
        "type": "string",
        "description": "The required token issuer, as specified in the 'iss' claim of federated tokens."
      },
      {
        "name": "jwks_json",
        "type": "string",
        "description": "The public keys used to validate the signature of federated tokens, in JWKS format. Most use cases should not need to specify this field. If jwks_uri and jwks_json are both unspecified (recommended), Databricks automatically fetches the public keys from your issuer’s well known endpoint. Databricks strongly recommends relying on your issuer’s well known endpoint for discovering public keys."
      },
      {
        "name": "jwks_uri",
        "type": "string",
        "description": "URL of the public keys used to validate the signature of federated tokens, in JWKS format. Most use cases should not need to specify this field. If jwks_uri and jwks_json are both unspecified (recommended), Databricks automatically fetches the public keys from your issuer’s well known endpoint. Databricks strongly recommends relying on your issuer’s well known endpoint for discovering public keys."
      },
      {
        "name": "subject",
        "type": "string",
        "description": "The required token subject, as specified in the subject claim of federated tokens. Must be specified for service principal federation policies. Must not be specified for account federation policies."
      },
      {
        "name": "subject_claim",
        "type": "string",
        "description": "The claim that contains the subject of the token. If unspecified, the default value is 'sub'."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "Unique, immutable id of the federation policy."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Last update time of the federation policy."
  }
]} />
</TabItem>
<TabItem value="service_principal_federation_policy_list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name for the federation policy. Example values include `accounts/<account-id>/federationPolicies/my-federation-policy` for Account Federation Policies, and `accounts/<account-id>/servicePrincipals/<service-principal-id>/federationPolicies/my-federation-policy` for Service Principal Federation Policies. Typically an output parameter, which does not need to be specified in create or update requests. If specified in a request, must match the value in the request URL."
  },
  {
    "name": "policy_id",
    "type": "string",
    "description": "The ID of the federation policy. Output only."
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": "The service principal ID that this federation policy applies to. Output only. Only set for service principal federation policies."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the federation policy."
  },
  {
    "name": "oidc_policy",
    "type": "object",
    "description": "Specifies the policy to use for validating OIDC claims in your federated tokens.",
    "children": [
      {
        "name": "audiences",
        "type": "array",
        "description": "The allowed token audiences, as specified in the 'aud' claim of federated tokens. The audience identifier is intended to represent the recipient of the token. Can be any non-empty string value. As long as the audience in the token matches at least one audience in the policy, the token is considered a match. If audiences is unspecified, defaults to your Databricks account id."
      },
      {
        "name": "issuer",
        "type": "string",
        "description": "The required token issuer, as specified in the 'iss' claim of federated tokens."
      },
      {
        "name": "jwks_json",
        "type": "string",
        "description": "The public keys used to validate the signature of federated tokens, in JWKS format. Most use cases should not need to specify this field. If jwks_uri and jwks_json are both unspecified (recommended), Databricks automatically fetches the public keys from your issuer’s well known endpoint. Databricks strongly recommends relying on your issuer’s well known endpoint for discovering public keys."
      },
      {
        "name": "jwks_uri",
        "type": "string",
        "description": "URL of the public keys used to validate the signature of federated tokens, in JWKS format. Most use cases should not need to specify this field. If jwks_uri and jwks_json are both unspecified (recommended), Databricks automatically fetches the public keys from your issuer’s well known endpoint. Databricks strongly recommends relying on your issuer’s well known endpoint for discovering public keys."
      },
      {
        "name": "subject",
        "type": "string",
        "description": "The required token subject, as specified in the subject claim of federated tokens. Must be specified for service principal federation policies. Must not be specified for account federation policies."
      },
      {
        "name": "subject_claim",
        "type": "string",
        "description": "The claim that contains the subject of the token. If unspecified, the default value is 'sub'."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "Unique, immutable id of the federation policy."
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "Last update time of the federation policy."
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
    <td><a href="#service_principal_federation_policy_get"><CopyableCode code="service_principal_federation_policy_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Get account federation policy.</td>
</tr>
<tr>
    <td><a href="#service_principal_federation_policy_list"><CopyableCode code="service_principal_federation_policy_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List account federation policies.</td>
</tr>
<tr>
    <td><a href="#service_principal_federation_policy_create"><CopyableCode code="service_principal_federation_policy_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-data__policy"><code>data__policy</code></a></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td>Create account federation policy.</td>
</tr>
<tr>
    <td><a href="#service_principal_federation_policy_update"><CopyableCode code="service_principal_federation_policy_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-data__policy"><code>data__policy</code></a></td>
    <td><a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td>Update account federation policy.</td>
</tr>
<tr>
    <td><a href="#service_principal_federation_policy_delete"><CopyableCode code="service_principal_federation_policy_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Delete account federation policy.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The identifier for the federation policy.</td>
</tr>
<tr id="parameter-service_principal_id">
    <td><CopyableCode code="service_principal_id" /></td>
    <td><code>integer</code></td>
    <td>The service principal id for the federation policy.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>:param page_token: str (optional)</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="service_principal_federation_policy_get"
    values={[
        { label: 'service_principal_federation_policy_get', value: 'service_principal_federation_policy_get' },
        { label: 'service_principal_federation_policy_list', value: 'service_principal_federation_policy_list' }
    ]}
>
<TabItem value="service_principal_federation_policy_get">

Get account federation policy.

```sql
SELECT
name,
policy_id,
service_principal_id,
create_time,
description,
oidc_policy,
uid,
update_time
FROM databricks_account.oauth2.service_principal_federation_policy
WHERE account_id = '{{ account_id }}' -- required
AND service_principal_id = '{{ service_principal_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
;
```
</TabItem>
<TabItem value="service_principal_federation_policy_list">

List account federation policies.

```sql
SELECT
name,
policy_id,
service_principal_id,
create_time,
description,
oidc_policy,
uid,
update_time
FROM databricks_account.oauth2.service_principal_federation_policy
WHERE account_id = '{{ account_id }}' -- required
AND service_principal_id = '{{ service_principal_id }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="service_principal_federation_policy_create"
    values={[
        { label: 'service_principal_federation_policy_create', value: 'service_principal_federation_policy_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="service_principal_federation_policy_create">

Create account federation policy.

```sql
INSERT INTO databricks_account.oauth2.service_principal_federation_policy (
data__policy,
account_id,
service_principal_id,
policy_id
)
SELECT 
'{{ policy }}' /* required */,
'{{ account_id }}',
'{{ service_principal_id }}',
'{{ policy_id }}'
RETURNING
name,
policy_id,
service_principal_id,
create_time,
description,
oidc_policy,
uid,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: service_principal_federation_policy
  props:
    - name: account_id
      value: string
      description: Required parameter for the service_principal_federation_policy resource.
    - name: service_principal_id
      value: integer
      description: Required parameter for the service_principal_federation_policy resource.
    - name: policy
      value: string
      description: |
        :param policy_id: str (optional) The identifier for the federation policy. The identifier must contain only lowercase alphanumeric characters, numbers, hyphens, and slashes. If unspecified, the id will be assigned by Databricks.
    - name: policy_id
      value: string
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="service_principal_federation_policy_update"
    values={[
        { label: 'service_principal_federation_policy_update', value: 'service_principal_federation_policy_update' }
    ]}
>
<TabItem value="service_principal_federation_policy_update">

Update account federation policy.

```sql
UPDATE databricks_account.oauth2.service_principal_federation_policy
SET 
data__policy = '{{ policy }}'
WHERE 
account_id = '{{ account_id }}' --required
AND service_principal_id = '{{ service_principal_id }}' --required
AND policy_id = '{{ policy_id }}' --required
AND data__policy = '{{ policy }}' --required
AND update_mask = '{{ update_mask}}'
RETURNING
name,
policy_id,
service_principal_id,
create_time,
description,
oidc_policy,
uid,
update_time;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="service_principal_federation_policy_delete"
    values={[
        { label: 'service_principal_federation_policy_delete', value: 'service_principal_federation_policy_delete' }
    ]}
>
<TabItem value="service_principal_federation_policy_delete">

Delete account federation policy.

```sql
DELETE FROM databricks_account.oauth2.service_principal_federation_policy
WHERE account_id = '{{ account_id }}' --required
AND service_principal_id = '{{ service_principal_id }}' --required
AND policy_id = '{{ policy_id }}' --required
;
```
</TabItem>
</Tabs>

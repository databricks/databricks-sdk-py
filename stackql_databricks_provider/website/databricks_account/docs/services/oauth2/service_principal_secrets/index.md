---
title: service_principal_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_secrets
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

Creates, updates, deletes, gets or lists a <code>service_principal_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth2.service_principal_secrets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="service_principal_secrets_list"
    values={[
        { label: 'service_principal_secrets_list', value: 'service_principal_secrets_list' }
    ]}
>
<TabItem value="service_principal_secrets_list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "ID of the secret"
  },
  {
    "name": "create_time",
    "type": "string",
    "description": ""
  },
  {
    "name": "expire_time",
    "type": "string",
    "description": "UTC time when the secret will expire. If the field is not present, the secret does not expire."
  },
  {
    "name": "secret_hash",
    "type": "string",
    "description": "Secret Hash"
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the secret"
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "UTC time when the secret was updated"
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
    <td><a href="#service_principal_secrets_list"><CopyableCode code="service_principal_secrets_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all secrets associated with the given service principal. This operation only returns information</td>
</tr>
<tr>
    <td><a href="#service_principal_secrets_create"><CopyableCode code="service_principal_secrets_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Create a secret for the given service principal.</td>
</tr>
<tr>
    <td><a href="#service_principal_secrets_delete"><CopyableCode code="service_principal_secrets_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Delete a secret from the given service principal.</td>
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
<tr id="parameter-secret_id">
    <td><CopyableCode code="secret_id" /></td>
    <td><code>string</code></td>
    <td>The secret ID.</td>
</tr>
<tr id="parameter-service_principal_id">
    <td><CopyableCode code="service_principal_id" /></td>
    <td><code>string</code></td>
    <td>The service principal ID.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>:param page_token: str (optional) An opaque page token which was the `next_page_token` in the response of the previous request to list the secrets for this service principal. Provide this token to retrieve the next page of secret entries. When providing a `page_token`, all other parameters provided to the request must match the previous request. To list all of the secrets for a service principal, it is necessary to continue requesting pages of entries until the response contains no `next_page_token`. Note that the number of entries returned must not be used to determine when the listing is complete.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="service_principal_secrets_list"
    values={[
        { label: 'service_principal_secrets_list', value: 'service_principal_secrets_list' }
    ]}
>
<TabItem value="service_principal_secrets_list">

List all secrets associated with the given service principal. This operation only returns information

```sql
SELECT
id,
create_time,
expire_time,
secret_hash,
status,
update_time
FROM databricks_account.oauth2.service_principal_secrets
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
    defaultValue="service_principal_secrets_create"
    values={[
        { label: 'service_principal_secrets_create', value: 'service_principal_secrets_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="service_principal_secrets_create">

Create a secret for the given service principal.

```sql
INSERT INTO databricks_account.oauth2.service_principal_secrets (
data__lifetime,
account_id,
service_principal_id
)
SELECT 
'{{ lifetime }}',
'{{ account_id }}',
'{{ service_principal_id }}'
RETURNING
id,
create_time,
expire_time,
secret,
secret_hash,
status,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: service_principal_secrets
  props:
    - name: account_id
      value: string
      description: Required parameter for the service_principal_secrets resource.
    - name: service_principal_id
      value: string
      description: Required parameter for the service_principal_secrets resource.
    - name: lifetime
      value: string
      description: |
        The lifetime of the secret in seconds. If this parameter is not provided, the secret will have a default lifetime of 730 days (63072000s).
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="service_principal_secrets_delete"
    values={[
        { label: 'service_principal_secrets_delete', value: 'service_principal_secrets_delete' }
    ]}
>
<TabItem value="service_principal_secrets_delete">

Delete a secret from the given service principal.

```sql
DELETE FROM databricks_account.oauth2.service_principal_secrets
WHERE account_id = '{{ account_id }}' --required
AND service_principal_id = '{{ service_principal_id }}' --required
AND secret_id = '{{ secret_id }}' --required
;
```
</TabItem>
</Tabs>

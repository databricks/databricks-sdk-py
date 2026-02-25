---
title: encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_keys
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

Creates, updates, deletes, gets or lists an <code>encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="encryption_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.encryption_keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="encryption_keys_get"
    values={[
        { label: 'encryption_keys_get', value: 'encryption_keys_get' },
        { label: 'encryption_keys_list', value: 'encryption_keys_list' }
    ]}
>
<TabItem value="encryption_keys_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "customer_managed_key_id",
    "type": "string",
    "description": "ID of the encryption key configuration object."
  },
  {
    "name": "aws_key_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "key_arn",
        "type": "string",
        "description": ""
      },
      {
        "name": "key_region",
        "type": "string",
        "description": "The AWS KMS key region."
      },
      {
        "name": "key_alias",
        "type": "string",
        "description": "The AWS KMS key alias."
      },
      {
        "name": "reuse_key_for_cluster_volumes",
        "type": "boolean",
        "description": "This field applies only if the `use_cases` property includes `STORAGE`. If this is set to true or omitted, the key is also used to encrypt cluster EBS volumes. If you do not want to use this key for encrypting EBS volumes, set to false."
      }
    ]
  },
  {
    "name": "azure_key_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "disk_encryption_set_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "key_access_configuration",
        "type": "object",
        "description": "The structure to store key access credential This is set if the Managed Identity is being used to access the Azure Key Vault key.",
        "children": [
          {
            "name": "credential_id",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "key_name",
        "type": "string",
        "description": "The name of the key in KeyVault."
      },
      {
        "name": "key_vault_uri",
        "type": "string",
        "description": "The base URI of the KeyVault."
      },
      {
        "name": "tenant_id",
        "type": "string",
        "description": "The tenant id where the KeyVault lives."
      },
      {
        "name": "version",
        "type": "string",
        "description": "The current key version."
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the customer key was created."
  },
  {
    "name": "gcp_key_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "kms_key_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "gcp_service_account",
        "type": "object",
        "description": "Globally unique service account email that has access to the KMS key. The service account exists within the Databricks CP project.",
        "children": [
          {
            "name": "service_account_email",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "use_cases",
    "type": "array",
    "description": "The cases that the key can be used for."
  }
]} />
</TabItem>
<TabItem value="encryption_keys_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "customer_managed_key_id",
    "type": "string",
    "description": "ID of the encryption key configuration object."
  },
  {
    "name": "aws_key_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "key_arn",
        "type": "string",
        "description": ""
      },
      {
        "name": "key_region",
        "type": "string",
        "description": "The AWS KMS key region."
      },
      {
        "name": "key_alias",
        "type": "string",
        "description": "The AWS KMS key alias."
      },
      {
        "name": "reuse_key_for_cluster_volumes",
        "type": "boolean",
        "description": "This field applies only if the `use_cases` property includes `STORAGE`. If this is set to true or omitted, the key is also used to encrypt cluster EBS volumes. If you do not want to use this key for encrypting EBS volumes, set to false."
      }
    ]
  },
  {
    "name": "azure_key_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "disk_encryption_set_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "key_access_configuration",
        "type": "object",
        "description": "The structure to store key access credential This is set if the Managed Identity is being used to access the Azure Key Vault key.",
        "children": [
          {
            "name": "credential_id",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "key_name",
        "type": "string",
        "description": "The name of the key in KeyVault."
      },
      {
        "name": "key_vault_uri",
        "type": "string",
        "description": "The base URI of the KeyVault."
      },
      {
        "name": "tenant_id",
        "type": "string",
        "description": "The tenant id where the KeyVault lives."
      },
      {
        "name": "version",
        "type": "string",
        "description": "The current key version."
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the customer key was created."
  },
  {
    "name": "gcp_key_info",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "kms_key_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "gcp_service_account",
        "type": "object",
        "description": "Globally unique service account email that has access to the KMS key. The service account exists within the Databricks CP project.",
        "children": [
          {
            "name": "service_account_email",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "use_cases",
    "type": "array",
    "description": "The cases that the key can be used for."
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
    <td><a href="#encryption_keys_get"><CopyableCode code="encryption_keys_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-customer_managed_key_id"><code>customer_managed_key_id</code></a></td>
    <td></td>
    <td>Gets a customer-managed key configuration object for an account, specified by ID. This operation</td>
</tr>
<tr>
    <td><a href="#encryption_keys_list"><CopyableCode code="encryption_keys_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Databricks customer-managed key configurations for an account.</td>
</tr>
<tr>
    <td><a href="#encryption_keys_create"><CopyableCode code="encryption_keys_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-use_cases"><code>use_cases</code></a></td>
    <td></td>
    <td>Creates a customer-managed key configuration object for an account, specified by ID. This operation</td>
</tr>
<tr>
    <td><a href="#encryption_keys_delete"><CopyableCode code="encryption_keys_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-customer_managed_key_id"><code>customer_managed_key_id</code></a></td>
    <td></td>
    <td>Deletes a customer-managed key configuration object for an account. You cannot delete a configuration</td>
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
<tr id="parameter-customer_managed_key_id">
    <td><CopyableCode code="customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td>Databricks encryption key configuration ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="encryption_keys_get"
    values={[
        { label: 'encryption_keys_get', value: 'encryption_keys_get' },
        { label: 'encryption_keys_list', value: 'encryption_keys_list' }
    ]}
>
<TabItem value="encryption_keys_get">

Gets a customer-managed key configuration object for an account, specified by ID. This operation

```sql
SELECT
account_id,
customer_managed_key_id,
aws_key_info,
azure_key_info,
creation_time,
gcp_key_info,
use_cases
FROM databricks_account.provisioning.encryption_keys
WHERE account_id = '{{ account_id }}' -- required
AND customer_managed_key_id = '{{ customer_managed_key_id }}' -- required
;
```
</TabItem>
<TabItem value="encryption_keys_list">

Lists Databricks customer-managed key configurations for an account.

```sql
SELECT
account_id,
customer_managed_key_id,
aws_key_info,
azure_key_info,
creation_time,
gcp_key_info,
use_cases
FROM databricks_account.provisioning.encryption_keys
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="encryption_keys_create"
    values={[
        { label: 'encryption_keys_create', value: 'encryption_keys_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="encryption_keys_create">

Creates a customer-managed key configuration object for an account, specified by ID. This operation

```sql
INSERT INTO databricks_account.provisioning.encryption_keys (
use_cases,
aws_key_info,
gcp_key_info,
account_id
)
SELECT 
'{{ use_cases }}' /* required */,
'{{ aws_key_info }}',
'{{ gcp_key_info }}',
'{{ account_id }}'
RETURNING
account_id,
customer_managed_key_id,
aws_key_info,
azure_key_info,
creation_time,
gcp_key_info,
use_cases
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: encryption_keys
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the encryption_keys resource.
    - name: use_cases
      value:
        - "{{ use_cases }}"
      description: |
        The cases that the key can be used for.
    - name: aws_key_info
      description: |
        :param gcp_key_info: :class:\`CreateGcpKeyInfo\` (optional)
      value:
        key_arn: "{{ key_arn }}"
        key_alias: "{{ key_alias }}"
        key_region: "{{ key_region }}"
        reuse_key_for_cluster_volumes: {{ reuse_key_for_cluster_volumes }}
    - name: gcp_key_info
      value:
        kms_key_id: "{{ kms_key_id }}"
        gcp_service_account:
          service_account_email: "{{ service_account_email }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="encryption_keys_delete"
    values={[
        { label: 'encryption_keys_delete', value: 'encryption_keys_delete' }
    ]}
>
<TabItem value="encryption_keys_delete">

Deletes a customer-managed key configuration object for an account. You cannot delete a configuration

```sql
DELETE FROM databricks_account.provisioning.encryption_keys
WHERE account_id = '{{ account_id }}' --required
AND customer_managed_key_id = '{{ customer_managed_key_id }}' --required
;
```
</TabItem>
</Tabs>

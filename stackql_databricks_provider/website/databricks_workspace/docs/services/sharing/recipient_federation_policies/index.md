---
title: recipient_federation_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - recipient_federation_policies
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

Creates, updates, deletes, gets or lists a <code>recipient_federation_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recipient_federation_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.recipient_federation_policies" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Unique, immutable system-generated identifier for the federation policy."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the federation policy. A recipient can have multiple policies with different names. The name must contain only lowercase alphanumeric characters, numbers, and hyphens."
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "System-generated timestamp indicating when the policy was created."
  },
  {
    "name": "oidc_policy",
    "type": "object",
    "description": "Specifies the policy to use for validating OIDC claims in the federated tokens.",
    "children": [
      {
        "name": "issuer",
        "type": "string",
        "description": "The required token issuer, as specified in the 'iss' claim of federated tokens."
      },
      {
        "name": "subject_claim",
        "type": "string",
        "description": "The claim that contains the subject of the token. Depending on the identity provider and the use case (U2M or M2M), this can vary: - For Entra ID (AAD): * U2M flow (group access): Use `groups`. * U2M flow (user access): Use `oid`. * M2M flow (OAuth App access): Use `azp`. - For other IdPs, refer to the specific IdP documentation. Supported `subject_claim` values are: - `oid`: Object ID of the user. - `azp`: Client ID of the OAuth app. - `groups`: Object ID of the group. - `sub`: Subject identifier for other use cases."
      },
      {
        "name": "subject",
        "type": "string",
        "description": "The required token subject, as specified in the subject claim of federated tokens. The subject claim identifies the identity of the user or machine accessing the resource. Examples for Entra ID (AAD): - U2M flow (group access): If the subject claim is `groups`, this must be the Object ID of the group in Entra ID. - U2M flow (user access): If the subject claim is `oid`, this must be the Object ID of the user in Entra ID. - M2M flow (OAuth App access): If the subject claim is `azp`, this must be the client ID of the OAuth app registered in Entra ID."
      },
      {
        "name": "audiences",
        "type": "array",
        "description": "The allowed token audiences, as specified in the 'aud' claim of federated tokens. The audience identifier is intended to represent the recipient of the token. Can be any non-empty string value. As long as the audience in the token matches at least one audience in the policy,"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "System-generated timestamp indicating when the policy was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Unique, immutable system-generated identifier for the federation policy."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the federation policy. A recipient can have multiple policies with different names. The name must contain only lowercase alphanumeric characters, numbers, and hyphens."
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "System-generated timestamp indicating when the policy was created."
  },
  {
    "name": "oidc_policy",
    "type": "object",
    "description": "Specifies the policy to use for validating OIDC claims in the federated tokens.",
    "children": [
      {
        "name": "issuer",
        "type": "string",
        "description": "The required token issuer, as specified in the 'iss' claim of federated tokens."
      },
      {
        "name": "subject_claim",
        "type": "string",
        "description": "The claim that contains the subject of the token. Depending on the identity provider and the use case (U2M or M2M), this can vary: - For Entra ID (AAD): * U2M flow (group access): Use `groups`. * U2M flow (user access): Use `oid`. * M2M flow (OAuth App access): Use `azp`. - For other IdPs, refer to the specific IdP documentation. Supported `subject_claim` values are: - `oid`: Object ID of the user. - `azp`: Client ID of the OAuth app. - `groups`: Object ID of the group. - `sub`: Subject identifier for other use cases."
      },
      {
        "name": "subject",
        "type": "string",
        "description": "The required token subject, as specified in the subject claim of federated tokens. The subject claim identifies the identity of the user or machine accessing the resource. Examples for Entra ID (AAD): - U2M flow (group access): If the subject claim is `groups`, this must be the Object ID of the group in Entra ID. - U2M flow (user access): If the subject claim is `oid`, this must be the Object ID of the user in Entra ID. - M2M flow (OAuth App access): If the subject claim is `azp`, this must be the client ID of the OAuth app registered in Entra ID."
      },
      {
        "name": "audiences",
        "type": "array",
        "description": "The allowed token audiences, as specified in the 'aud' claim of federated tokens. The audience identifier is intended to represent the recipient of the token. Can be any non-empty string value. As long as the audience in the token matches at least one audience in the policy,"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "System-generated timestamp indicating when the policy was last updated."
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
    <td><a href="#parameter-recipient_name"><code>recipient_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Reads an existing federation policy for an OIDC_FEDERATION recipient for sharing data from Databricks</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-recipient_name"><code>recipient_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists federation policies for an OIDC_FEDERATION recipient for sharing data from Databricks to</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-recipient_name"><code>recipient_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-policy"><code>policy</code></a></td>
    <td></td>
    <td>Create a federation policy for an OIDC_FEDERATION recipient for sharing data from Databricks to</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-recipient_name"><code>recipient_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an existing federation policy for an OIDC_FEDERATION recipient. The caller must be the owner</td>
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
    <td>Name of the policy. This is the name of the policy to be deleted.</td>
</tr>
<tr id="parameter-recipient_name">
    <td><CopyableCode code="recipient_name" /></td>
    <td><code>string</code></td>
    <td>Name of the recipient. This is the name of the recipient for which the policy is being deleted.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>:param page_token: str (optional)</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Reads an existing federation policy for an OIDC_FEDERATION recipient for sharing data from Databricks

```sql
SELECT
id,
name,
comment,
create_time,
oidc_policy,
update_time
FROM databricks_workspace.sharing.recipient_federation_policies
WHERE recipient_name = '{{ recipient_name }}' -- required
AND name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists federation policies for an OIDC_FEDERATION recipient for sharing data from Databricks to

```sql
SELECT
id,
name,
comment,
create_time,
oidc_policy,
update_time
FROM databricks_workspace.sharing.recipient_federation_policies
WHERE recipient_name = '{{ recipient_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a federation policy for an OIDC_FEDERATION recipient for sharing data from Databricks to

```sql
INSERT INTO databricks_workspace.sharing.recipient_federation_policies (
policy,
recipient_name,
deployment_name
)
SELECT 
'{{ policy }}' /* required */,
'{{ recipient_name }}',
'{{ deployment_name }}'
RETURNING
id,
name,
comment,
create_time,
oidc_policy,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: recipient_federation_policies
  props:
    - name: recipient_name
      value: string
      description: Required parameter for the recipient_federation_policies resource.
    - name: deployment_name
      value: string
      description: Required parameter for the recipient_federation_policies resource.
    - name: policy
      value: string
      description: |
        Name of the policy. This is the name of the policy to be created.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an existing federation policy for an OIDC_FEDERATION recipient. The caller must be the owner

```sql
DELETE FROM databricks_workspace.sharing.recipient_federation_policies
WHERE recipient_name = '{{ recipient_name }}' --required
AND name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

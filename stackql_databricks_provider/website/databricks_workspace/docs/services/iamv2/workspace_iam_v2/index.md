---
title: workspace_iam_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_iam_v2
  - iamv2
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

Creates, updates, deletes, gets or lists a <code>workspace_iam_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_iam_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.workspace_iam_v2" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_workspace_access_detail_local"
    values={[
        { label: 'get_workspace_access_detail_local', value: 'get_workspace_access_detail_local' }
    ]}
>
<TabItem value="get_workspace_access_detail_local">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The account ID parent of the workspace where the principal has access."
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID where the principal has access."
  },
  {
    "name": "access_type",
    "type": "string",
    "description": "The type of access the principal has to the workspace."
  },
  {
    "name": "permissions",
    "type": "array",
    "description": "The permissions granted to the principal in the workspace."
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group)."
  },
  {
    "name": "status",
    "type": "string",
    "description": "The activity status of the principal in the workspace. Not applicable for groups at the moment."
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
    <td><a href="#get_workspace_access_detail_local"><CopyableCode code="get_workspace_access_detail_local" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-view"><code>view</code></a></td>
    <td>Returns the access details for a principal in the current workspace. Allows for checking access<br />details for any provisioned principal (user, service principal, or group) in the current workspace. *<br />Provisioned principal here refers to one that has been synced into Databricks from the customer's IdP<br />or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to control<br />what fields are returned (BASIC by default or FULL).<br /><br />:param principal_id: int<br />  Required. The internal ID of the principal (user/sp/group) for which the access details are being<br />  requested.<br />:param view: :class:`WorkspaceAccessDetailView` (optional)<br />  Controls what fields are returned.<br /><br />:returns: :class:`WorkspaceAccessDetail`</td>
</tr>
<tr>
    <td><a href="#resolve_group_proxy"><CopyableCode code="resolve_group_proxy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it<br />will be created in the account. If the customer is not onboarded onto Automatic Identity Management<br />(AIM), this will return an error.<br /><br />:param external_id: str<br />  Required. The external ID of the group in the customer's IdP.<br /><br />:returns: :class:`ResolveGroupResponse`</td>
</tr>
<tr>
    <td><a href="#resolve_service_principal_proxy"><CopyableCode code="resolve_service_principal_proxy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will<br />be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will<br />return an error.<br /><br />:param external_id: str<br />  Required. The external ID of the service principal in the customer's IdP.<br /><br />:returns: :class:`ResolveServicePrincipalResponse`</td>
</tr>
<tr>
    <td><a href="#resolve_user_proxy"><CopyableCode code="resolve_user_proxy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it<br />will be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will<br />return an error.<br /><br />:param external_id: str<br />  Required. The external ID of the user in the customer's IdP.<br /><br />:returns: :class:`ResolveUserResponse`</td>
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
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>Required. The internal ID of the principal (user/sp/group) for which the access details are being requested.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>Controls what fields are returned.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_workspace_access_detail_local"
    values={[
        { label: 'get_workspace_access_detail_local', value: 'get_workspace_access_detail_local' }
    ]}
>
<TabItem value="get_workspace_access_detail_local">

Returns the access details for a principal in the current workspace. Allows for checking access<br />details for any provisioned principal (user, service principal, or group) in the current workspace. *<br />Provisioned principal here refers to one that has been synced into Databricks from the customer's IdP<br />or added explicitly to Databricks via SCIM/UI. Allows for passing in a "view" parameter to control<br />what fields are returned (BASIC by default or FULL).<br /><br />:param principal_id: int<br />  Required. The internal ID of the principal (user/sp/group) for which the access details are being<br />  requested.<br />:param view: :class:`WorkspaceAccessDetailView` (optional)<br />  Controls what fields are returned.<br /><br />:returns: :class:`WorkspaceAccessDetail`

```sql
SELECT
account_id,
principal_id,
workspace_id,
access_type,
permissions,
principal_type,
status
FROM databricks_workspace.iamv2.workspace_iam_v2
WHERE principal_id = '{{ principal_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND view = '{{ view }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resolve_group_proxy"
    values={[
        { label: 'resolve_group_proxy', value: 'resolve_group_proxy' },
        { label: 'resolve_service_principal_proxy', value: 'resolve_service_principal_proxy' },
        { label: 'resolve_user_proxy', value: 'resolve_user_proxy' }
    ]}
>
<TabItem value="resolve_group_proxy">

Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it<br />will be created in the account. If the customer is not onboarded onto Automatic Identity Management<br />(AIM), this will return an error.<br /><br />:param external_id: str<br />  Required. The external ID of the group in the customer's IdP.<br /><br />:returns: :class:`ResolveGroupResponse`

```sql
EXEC databricks_workspace.iamv2.workspace_iam_v2.resolve_group_proxy 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
<TabItem value="resolve_service_principal_proxy">

Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will<br />be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will<br />return an error.<br /><br />:param external_id: str<br />  Required. The external ID of the service principal in the customer's IdP.<br /><br />:returns: :class:`ResolveServicePrincipalResponse`

```sql
EXEC databricks_workspace.iamv2.workspace_iam_v2.resolve_service_principal_proxy 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
<TabItem value="resolve_user_proxy">

Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it<br />will be created. If the customer is not onboarded onto Automatic Identity Management (AIM), this will<br />return an error.<br /><br />:param external_id: str<br />  Required. The external ID of the user in the customer's IdP.<br /><br />:returns: :class:`ResolveUserResponse`

```sql
EXEC databricks_workspace.iamv2.workspace_iam_v2.resolve_user_proxy 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
</Tabs>

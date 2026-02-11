---
title: secret_acls
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_acls
  - workspace
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

Creates, updates, deletes, gets or lists a <code>secret_acls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.secret_acls" /></td></tr>
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
    "name": "permission",
    "type": "string",
    "description": "The permission level applied to the principal."
  },
  {
    "name": "principal",
    "type": "string",
    "description": "The principal in which the permission is applied."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "permission",
    "type": "string",
    "description": "The permission level applied to the principal."
  },
  {
    "name": "principal",
    "type": "string",
    "description": "The principal in which the permission is applied."
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-principal"><code>principal</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Describes the details about the given ACL, such as the group and permission.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "principal": "data-scientists", "permission": "READ" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call. Throws ``INVALID_PARAMETER_VALUE`` if the<br />permission or principal is invalid.<br /><br />:param scope: str<br />  The name of the scope to fetch ACL information from.<br />:param principal: str<br />  The principal to fetch ACL information for.<br /><br />:returns: :class:`AclItem`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists the ACLs set on the given scope.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "acls": [&#123; "principal": "admins", "permission": "MANAGE" &#125;,&#123; "principal": "data-scientists",<br />"permission": "READ" &#125;] &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call.<br /><br />:param scope: str<br />  The name of the scope to fetch ACL information from.<br /><br />:returns: Iterator over :class:`AclItem`</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__scope"><code>data__scope</code></a>, <a href="#parameter-data__principal"><code>data__principal</code></a>, <a href="#parameter-data__permission"><code>data__permission</code></a></td>
    <td></td>
    <td>Creates or overwrites the ACL associated with the given principal (user or group) on the specified<br />scope point. In general, a user or group will use the most powerful permission available to them, and<br />permissions are ordered as follows:<br /><br />* ``MANAGE`` - Allowed to change ACLs, and read and write to this secret scope. * ``WRITE`` - Allowed<br />to read and write to this secret scope. * ``READ`` - Allowed to read this secret scope and list what<br />secrets are available.<br /><br />Note that in general, secret values can only be read from within a command on a cluster (for example,<br />through a notebook). There is no API to read the actual secret value material outside of a cluster.<br />However, the user's permission will be applied based on who is executing the command, and they must<br />have at least READ permission.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope", "principal": "data-scientists", "permission": "READ" &#125;<br /><br />The principal is a user or group name corresponding to an existing Databricks principal to be granted<br />or revoked access.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``RESOURCE_ALREADY_EXISTS``<br />if a permission for the principal already exists. Throws ``INVALID_PARAMETER_VALUE`` if the permission<br />or principal is invalid. Throws ``PERMISSION_DENIED`` if the user does not have permission to make<br />this API call.<br /><br />:param scope: str<br />  The name of the scope to apply permissions to.<br />:param principal: str<br />  The principal in which the permission is applied.<br />:param permission: :class:`AclPermission`<br />  The permission level applied to the principal.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-principal"><code>principal</code></a></td>
    <td></td>
    <td>Deletes the given ACL on the given scope.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope", "principal": "data-scientists" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope, principal, or ACL exists. Throws<br />``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws<br />``INVALID_PARAMETER_VALUE`` if the permission or principal is invalid.<br /><br />:param scope: str<br />  The name of the scope to remove permissions from.<br />:param principal: str<br />  The principal to remove an existing ACL from.</td>
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
<tr id="parameter-principal">
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td>The principal to fetch ACL information for.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The name of the scope to fetch ACL information from.</td>
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

Describes the details about the given ACL, such as the group and permission.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "principal": "data-scientists", "permission": "READ" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call. Throws ``INVALID_PARAMETER_VALUE`` if the<br />permission or principal is invalid.<br /><br />:param scope: str<br />  The name of the scope to fetch ACL information from.<br />:param principal: str<br />  The principal to fetch ACL information for.<br /><br />:returns: :class:`AclItem`

```sql
SELECT
permission,
principal
FROM databricks_workspace.workspace.secret_acls
WHERE scope = '{{ scope }}' -- required
AND principal = '{{ principal }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the ACLs set on the given scope.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example response:<br /><br />.. code::<br /><br />&#123; "acls": [&#123; "principal": "admins", "permission": "MANAGE" &#125;,&#123; "principal": "data-scientists",<br />"permission": "READ" &#125;] &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``PERMISSION_DENIED`` if the<br />user does not have permission to make this API call.<br /><br />:param scope: str<br />  The name of the scope to fetch ACL information from.<br /><br />:returns: Iterator over :class:`AclItem`

```sql
SELECT
permission,
principal
FROM databricks_workspace.workspace.secret_acls
WHERE scope = '{{ scope }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="put">

Creates or overwrites the ACL associated with the given principal (user or group) on the specified<br />scope point. In general, a user or group will use the most powerful permission available to them, and<br />permissions are ordered as follows:<br /><br />* ``MANAGE`` - Allowed to change ACLs, and read and write to this secret scope. * ``WRITE`` - Allowed<br />to read and write to this secret scope. * ``READ`` - Allowed to read this secret scope and list what<br />secrets are available.<br /><br />Note that in general, secret values can only be read from within a command on a cluster (for example,<br />through a notebook). There is no API to read the actual secret value material outside of a cluster.<br />However, the user's permission will be applied based on who is executing the command, and they must<br />have at least READ permission.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope", "principal": "data-scientists", "permission": "READ" &#125;<br /><br />The principal is a user or group name corresponding to an existing Databricks principal to be granted<br />or revoked access.<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope exists. Throws ``RESOURCE_ALREADY_EXISTS``<br />if a permission for the principal already exists. Throws ``INVALID_PARAMETER_VALUE`` if the permission<br />or principal is invalid. Throws ``PERMISSION_DENIED`` if the user does not have permission to make<br />this API call.<br /><br />:param scope: str<br />  The name of the scope to apply permissions to.<br />:param principal: str<br />  The principal in which the permission is applied.<br />:param permission: :class:`AclPermission`<br />  The permission level applied to the principal.

```sql
INSERT INTO databricks_workspace.workspace.secret_acls (
data__scope,
data__principal,
data__permission,
deployment_name
)
SELECT 
'{{ scope }}' /* required */,
'{{ principal }}' /* required */,
'{{ permission }}' /* required */,
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: secret_acls
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the secret_acls resource.
    - name: scope
      value: string
      description: |
        The name of the scope to apply permissions to.
    - name: principal
      value: string
      description: |
        The principal in which the permission is applied.
    - name: permission
      value: string
      description: |
        The permission level applied to the principal.
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the given ACL on the given scope.<br /><br />Users must have the ``MANAGE`` permission to invoke this API.<br /><br />Example request:<br /><br />.. code::<br /><br />&#123; "scope": "my-secret-scope", "principal": "data-scientists" &#125;<br /><br />Throws ``RESOURCE_DOES_NOT_EXIST`` if no such secret scope, principal, or ACL exists. Throws<br />``PERMISSION_DENIED`` if the user does not have permission to make this API call. Throws<br />``INVALID_PARAMETER_VALUE`` if the permission or principal is invalid.<br /><br />:param scope: str<br />  The name of the scope to remove permissions from.<br />:param principal: str<br />  The principal to remove an existing ACL from.

```sql
EXEC databricks_workspace.workspace.secret_acls.delete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"scope": "{{ scope }}", 
"principal": "{{ principal }}"
}'
;
```
</TabItem>
</Tabs>

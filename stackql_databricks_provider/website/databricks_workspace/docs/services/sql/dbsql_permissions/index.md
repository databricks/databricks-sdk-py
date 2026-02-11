---
title: dbsql_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - dbsql_permissions
  - sql
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

Creates, updates, deletes, gets or lists a <code>dbsql_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbsql_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.dbsql_permissions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "object_id",
    "type": "string",
    "description": "An object's type and UUID, separated by a forward slash (/) character."
  },
  {
    "name": "access_control_list",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "group_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "permission_level",
        "type": "string",
        "description": "* `CAN_VIEW`: Can view the query * `CAN_RUN`: Can run the query * `CAN_EDIT`: Can edit the query * `CAN_MANAGE`: Can manage the query"
      },
      {
        "name": "user_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "A singular noun object type."
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
    <td><a href="#parameter-object_type.value"><code>object_type.value</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a JSON representation of the access control list (ACL) for a specified object.<br /><br />**Warning**: This API is deprecated. Please use :method:workspace/getpermissions instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param object_type: :class:`ObjectTypePlural`<br />  The type of object permissions to check.<br />:param object_id: str<br />  Object ID. An ACL is returned for the object with this UUID.<br /><br />:returns: :class:`GetResponse`</td>
</tr>
<tr>
    <td><a href="#set"><CopyableCode code="set" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-object_type.value"><code>object_type.value</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__object_type"><code>data__object_type</code></a></td>
    <td></td>
    <td>Sets the access control list (ACL) for a specified object. This operation will complete rewrite the<br />ACL.<br /><br />**Warning**: This API is deprecated. Please use :method:workspace/setpermissions instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param object_type: :class:`ObjectTypePlural`<br />  The type of object permission to set.<br />:param object_id: str<br />  Object ID. The ACL for the object with this UUID is overwritten by this request's POST content.<br />:param access_control_list: List[:class:`AccessControl`] (optional)<br /><br />:returns: :class:`SetResponse`</td>
</tr>
<tr>
    <td><a href="#transfer_ownership"><CopyableCode code="transfer_ownership" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-object_type.value"><code>object_type.value</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-object_type"><code>object_type</code></a></td>
    <td></td>
    <td>Transfers ownership of a dashboard, query, or alert to an active user. Requires an admin API key.<br /><br />**Warning**: This API is deprecated. For queries and alerts, please use :method:queries/update and<br />:method:alerts/update respectively instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param object_type: :class:`OwnableObjectType`<br />  The type of object on which to change ownership.<br />:param object_id: :class:`TransferOwnershipObjectId`<br />  The ID of the object on which to change ownership.<br />:param new_owner: str (optional)<br />  Email address for the new owner, who must exist in the workspace.<br /><br />:returns: :class:`Success`</td>
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
<tr id="parameter-object_id">
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the object on which to change ownership.</td>
</tr>
<tr id="parameter-object_type">
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>The type of object permissions to check.</td>
</tr>
<tr id="parameter-object_type.value">
    <td><CopyableCode code="object_type.value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a JSON representation of the access control list (ACL) for a specified object.<br /><br />**Warning**: This API is deprecated. Please use :method:workspace/getpermissions instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param object_type: :class:`ObjectTypePlural`<br />  The type of object permissions to check.<br />:param object_id: str<br />  Object ID. An ACL is returned for the object with this UUID.<br /><br />:returns: :class:`GetResponse`

```sql
SELECT
object_id,
access_control_list,
object_type
FROM databricks_workspace.sql.dbsql_permissions
WHERE object_type.value = '{{ object_type.value }}' -- required
AND object_id = '{{ object_id }}' -- required
AND object_type = '{{ object_type }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="set"
    values={[
        { label: 'set', value: 'set' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="set">

Sets the access control list (ACL) for a specified object. This operation will complete rewrite the<br />ACL.<br /><br />**Warning**: This API is deprecated. Please use :method:workspace/setpermissions instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param object_type: :class:`ObjectTypePlural`<br />  The type of object permission to set.<br />:param object_id: str<br />  Object ID. The ACL for the object with this UUID is overwritten by this request's POST content.<br />:param access_control_list: List[:class:`AccessControl`] (optional)<br /><br />:returns: :class:`SetResponse`

```sql
INSERT INTO databricks_workspace.sql.dbsql_permissions (
data__object_type,
data__access_control_list,
object_type.value,
object_id,
deployment_name
)
SELECT 
'{{ object_type }}' /* required */,
'{{ access_control_list }}',
'{{ object_type.value }}',
'{{ object_id }}',
'{{ deployment_name }}'
RETURNING
object_id,
access_control_list,
object_type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dbsql_permissions
  props:
    - name: object_type.value
      value: string
      description: Required parameter for the dbsql_permissions resource.
    - name: object_id
      value: string
      description: Required parameter for the dbsql_permissions resource.
    - name: deployment_name
      value: string
      description: Required parameter for the dbsql_permissions resource.
    - name: object_type
      value: string
      description: |
        The type of object permission to set.
    - name: access_control_list
      value: string
      description: |
        :returns: :class:`SetResponse`
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="transfer_ownership"
    values={[
        { label: 'transfer_ownership', value: 'transfer_ownership' }
    ]}
>
<TabItem value="transfer_ownership">

Transfers ownership of a dashboard, query, or alert to an active user. Requires an admin API key.<br /><br />**Warning**: This API is deprecated. For queries and alerts, please use :method:queries/update and<br />:method:alerts/update respectively instead. [Learn more]<br /><br />[Learn more]: https://docs.databricks.com/en/sql/dbsql-api-latest.html<br /><br />:param object_type: :class:`OwnableObjectType`<br />  The type of object on which to change ownership.<br />:param object_id: :class:`TransferOwnershipObjectId`<br />  The ID of the object on which to change ownership.<br />:param new_owner: str (optional)<br />  Email address for the new owner, who must exist in the workspace.<br /><br />:returns: :class:`Success`

```sql
EXEC databricks_workspace.sql.dbsql_permissions.transfer_ownership 
@object_type.value='{{ object_type.value }}' --required, 
@object_id='{{ object_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"object_type": "{{ object_type }}", 
"new_owner": "{{ new_owner }}"
}'
;
```
</TabItem>
</Tabs>

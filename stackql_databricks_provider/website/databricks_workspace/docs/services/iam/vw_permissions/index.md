---
title: vw_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_permissions
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

Creates, updates, deletes, gets or lists a <code>vw_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_permissions" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.vw_permissions" /></td></tr>
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
    <td><CopyableCode code="request_object_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Object type used to scope the permissions query (e.g. clusters, jobs, notebooks, directories).</td>
</tr>
<tr>
    <td><CopyableCode code="request_object_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Object ID used to scope the permissions query.</td>
</tr>
<tr>
    <td><CopyableCode code="object_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>ID of the object whose permissions are being queried.</td>
</tr>
<tr>
    <td><CopyableCode code="object_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Type of the object (e.g. clusters, jobs, notebooks, directories).</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Display name of the principal in this ACL entry.</td>
</tr>
<tr>
    <td><CopyableCode code="user_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Username of the principal if the principal is a user.</td>
</tr>
<tr>
    <td><CopyableCode code="group_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Group name of the principal if the principal is a group.</td>
</tr>
<tr>
    <td><CopyableCode code="service_principal_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Application name of the principal if the principal is a service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="permission_level" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Permission level granted to the principal (one row per permission, e.g. CAN_VIEW, CAN_RUN, CAN_MANAGE, IS_OWNER).</td>
</tr>
<tr>
    <td><CopyableCode code="inherited" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether this permission is inherited from a parent object.</td>
</tr>
<tr>
    <td><CopyableCode code="inherited_from_object" /></td>
    <td><CopyableCode code="array" /></td>
    <td>List of parent object paths from which this permission is inherited.</td>
</tr>
</tbody>
</table>

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
  p.deployment_name,
  p.request_object_type,
  p.request_object_id,
  p.object_id,
  p.object_type,
  JSON_EXTRACT(acl.value, '$.display_name') AS display_name,
  JSON_EXTRACT(acl.value, '$.user_name') AS user_name,
  JSON_EXTRACT(acl.value, '$.group_name') AS group_name,
  JSON_EXTRACT(acl.value, '$.service_principal_name') AS service_principal_name,
  JSON_EXTRACT(perm.value, '$.permission_level') AS permission_level,
  JSON_EXTRACT(perm.value, '$.inherited') AS inherited,
  JSON_EXTRACT(perm.value, '$.inherited_from_object') AS inherited_from_object
FROM databricks_workspace.iam.permissions p,
     JSON_EACH(p.access_control_list) acl,
     JSON_EACH(JSON_EXTRACT(acl.value, '$.all_permissions')) perm
WHERE p.deployment_name = '{{ deployment_name }}'
AND p.request_object_type = '{{ request_object_type }}'
AND p.request_object_id = '{{ request_object_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  p.deployment_name,
  p.request_object_type,
  p.request_object_id,
  p.object_id,
  p.object_type,
  acl.value->>'display_name' AS display_name,
  acl.value->>'user_name' AS user_name,
  acl.value->>'group_name' AS group_name,
  acl.value->>'service_principal_name' AS service_principal_name,
  perm.value->>'permission_level' AS permission_level,
  (perm.value->>'inherited')::boolean AS inherited,
  perm.value->'inherited_from_object' AS inherited_from_object
FROM databricks_workspace.iam.permissions p,
     jsonb_array_elements(p.access_control_list::jsonb) AS acl,
     jsonb_array_elements((acl.value->'all_permissions')::jsonb) AS perm
WHERE p.deployment_name = '{{ deployment_name }}'
AND p.request_object_type = '{{ request_object_type }}'
AND p.request_object_id = '{{ request_object_id }}'
```

</TabItem>
</Tabs>

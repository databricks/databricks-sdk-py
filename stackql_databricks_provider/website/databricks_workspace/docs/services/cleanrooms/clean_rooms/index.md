---
title: clean_rooms
hide_title: false
hide_table_of_contents: false
keywords:
  - clean_rooms
  - cleanrooms
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

Creates, updates, deletes, gets or lists a <code>clean_rooms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clean_rooms" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.clean_rooms" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "The name of the clean room. It should follow [UC securable naming requirements]. [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"
  },
  {
    "name": "access_restricted",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CSP_MISMATCH, NO_RESTRICTION)"
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "When the clean room was created, in epoch milliseconds."
  },
  {
    "name": "local_collaborator_alias",
    "type": "string",
    "description": "The alias of the collaborator tied to the local clean room."
  },
  {
    "name": "output_catalog",
    "type": "object",
    "description": "Output catalog of the clean room. It is an output only field. Output catalog is manipulated using the separate CreateCleanRoomOutputCatalog API.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "status",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CREATED, NOT_CREATED, NOT_ELIGIBLE)"
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "This is the Databricks username of the owner of the local clean room securable for permission management."
  },
  {
    "name": "remote_detailed_info",
    "type": "object",
    "description": "Central clean room details. During creation, users need to specify cloud_vendor, region, and collaborators.global_metastore_id. This field will not be filled in the ListCleanRooms call.",
    "children": [
      {
        "name": "central_clean_room_id",
        "type": "string",
        "description": "Central clean room ID."
      },
      {
        "name": "cloud_vendor",
        "type": "string",
        "description": "Cloud vendor (aws,azure,gcp) of the central clean room."
      },
      {
        "name": "collaborators",
        "type": "array",
        "description": "Collaborators in the central clean room. There should one and only one collaborator in the list that satisfies the owner condition: 1. It has the creator's global_metastore_id (determined by caller of CreateCleanRoom). 2. Its invite_recipient_email is empty.",
        "children": [
          {
            "name": "collaborator_alias",
            "type": "string",
            "description": "Collaborator alias specified by the clean room creator. It is unique across all collaborators of this clean room, and used to derive multiple values internally such as catalog alias and clean room name for single metastore clean rooms. It should follow [UC securable naming requirements]. [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"
          },
          {
            "name": "display_name",
            "type": "string",
            "description": "Generated display name for the collaborator. In the case of a single metastore clean room, it is the clean room name. For x-metastore clean rooms, it is the organization name of the metastore. It is not restricted to these values and could change in the future"
          },
          {
            "name": "global_metastore_id",
            "type": "string",
            "description": "The global Unity Catalog metastore ID of the collaborator. The identifier is of format cloud:region:metastore-uuid."
          },
          {
            "name": "invite_recipient_email",
            "type": "string",
            "description": "Email of the user who is receiving the clean room \"invitation\". It should be empty for the creator of the clean room, and non-empty for the invitees of the clean room. It is only returned in the output when clean room creator calls GET"
          },
          {
            "name": "invite_recipient_workspace_id",
            "type": "integer",
            "description": "Workspace ID of the user who is receiving the clean room \"invitation\". Must be specified if invite_recipient_email is specified. It should be empty when the collaborator is the creator of the clean room."
          },
          {
            "name": "organization_name",
            "type": "string",
            "description": "[Organization name](:method:metastores/list#metastores-delta_sharing_organization_name) configured in the metastore"
          }
        ]
      },
      {
        "name": "compliance_security_profile",
        "type": "object",
        "description": "The compliance security profile used to process regulated data following compliance standards.",
        "children": [
          {
            "name": "compliance_standards",
            "type": "string",
            "description": "The list of compliance standards that the compliance security profile is configured to enforce."
          },
          {
            "name": "is_enabled",
            "type": "boolean",
            "description": "Whether the compliance security profile is enabled."
          }
        ]
      },
      {
        "name": "creator",
        "type": "object",
        "description": "Publicly visible clean room collaborator.",
        "children": [
          {
            "name": "collaborator_alias",
            "type": "string",
            "description": "Collaborator alias specified by the clean room creator. It is unique across all collaborators of this clean room, and used to derive multiple values internally such as catalog alias and clean room name for single metastore clean rooms. It should follow [UC securable naming requirements]. [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"
          },
          {
            "name": "display_name",
            "type": "string",
            "description": "Generated display name for the collaborator. In the case of a single metastore clean room, it is the clean room name. For x-metastore clean rooms, it is the organization name of the metastore. It is not restricted to these values and could change in the future"
          },
          {
            "name": "global_metastore_id",
            "type": "string",
            "description": "The global Unity Catalog metastore ID of the collaborator. The identifier is of format cloud:region:metastore-uuid."
          },
          {
            "name": "invite_recipient_email",
            "type": "string",
            "description": "Email of the user who is receiving the clean room \"invitation\". It should be empty for the creator of the clean room, and non-empty for the invitees of the clean room. It is only returned in the output when clean room creator calls GET"
          },
          {
            "name": "invite_recipient_workspace_id",
            "type": "integer",
            "description": "Workspace ID of the user who is receiving the clean room \"invitation\". Must be specified if invite_recipient_email is specified. It should be empty when the collaborator is the creator of the clean room."
          },
          {
            "name": "organization_name",
            "type": "string",
            "description": "[Organization name](:method:metastores/list#metastores-delta_sharing_organization_name) configured in the metastore"
          }
        ]
      },
      {
        "name": "egress_network_policy",
        "type": "string",
        "description": "Egress network policy to apply to the central clean room workspace."
      },
      {
        "name": "region",
        "type": "string",
        "description": "Region of the central clean room."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Clean room status. (ACTIVE, DELETED, FAILED, PROVISIONING)"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "When the clean room was last updated, in epoch milliseconds."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the clean room. It should follow [UC securable naming requirements]. [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"
  },
  {
    "name": "access_restricted",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CSP_MISMATCH, NO_RESTRICTION)"
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "When the clean room was created, in epoch milliseconds."
  },
  {
    "name": "local_collaborator_alias",
    "type": "string",
    "description": "The alias of the collaborator tied to the local clean room."
  },
  {
    "name": "output_catalog",
    "type": "object",
    "description": "Output catalog of the clean room. It is an output only field. Output catalog is manipulated using the separate CreateCleanRoomOutputCatalog API.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "status",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CREATED, NOT_CREATED, NOT_ELIGIBLE)"
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "This is the Databricks username of the owner of the local clean room securable for permission management."
  },
  {
    "name": "remote_detailed_info",
    "type": "object",
    "description": "Central clean room details. During creation, users need to specify cloud_vendor, region, and collaborators.global_metastore_id. This field will not be filled in the ListCleanRooms call.",
    "children": [
      {
        "name": "central_clean_room_id",
        "type": "string",
        "description": "Central clean room ID."
      },
      {
        "name": "cloud_vendor",
        "type": "string",
        "description": "Cloud vendor (aws,azure,gcp) of the central clean room."
      },
      {
        "name": "collaborators",
        "type": "array",
        "description": "Collaborators in the central clean room. There should one and only one collaborator in the list that satisfies the owner condition: 1. It has the creator's global_metastore_id (determined by caller of CreateCleanRoom). 2. Its invite_recipient_email is empty.",
        "children": [
          {
            "name": "collaborator_alias",
            "type": "string",
            "description": "Collaborator alias specified by the clean room creator. It is unique across all collaborators of this clean room, and used to derive multiple values internally such as catalog alias and clean room name for single metastore clean rooms. It should follow [UC securable naming requirements]. [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"
          },
          {
            "name": "display_name",
            "type": "string",
            "description": "Generated display name for the collaborator. In the case of a single metastore clean room, it is the clean room name. For x-metastore clean rooms, it is the organization name of the metastore. It is not restricted to these values and could change in the future"
          },
          {
            "name": "global_metastore_id",
            "type": "string",
            "description": "The global Unity Catalog metastore ID of the collaborator. The identifier is of format cloud:region:metastore-uuid."
          },
          {
            "name": "invite_recipient_email",
            "type": "string",
            "description": "Email of the user who is receiving the clean room \"invitation\". It should be empty for the creator of the clean room, and non-empty for the invitees of the clean room. It is only returned in the output when clean room creator calls GET"
          },
          {
            "name": "invite_recipient_workspace_id",
            "type": "integer",
            "description": "Workspace ID of the user who is receiving the clean room \"invitation\". Must be specified if invite_recipient_email is specified. It should be empty when the collaborator is the creator of the clean room."
          },
          {
            "name": "organization_name",
            "type": "string",
            "description": "[Organization name](:method:metastores/list#metastores-delta_sharing_organization_name) configured in the metastore"
          }
        ]
      },
      {
        "name": "compliance_security_profile",
        "type": "object",
        "description": "The compliance security profile used to process regulated data following compliance standards.",
        "children": [
          {
            "name": "compliance_standards",
            "type": "string",
            "description": "The list of compliance standards that the compliance security profile is configured to enforce."
          },
          {
            "name": "is_enabled",
            "type": "boolean",
            "description": "Whether the compliance security profile is enabled."
          }
        ]
      },
      {
        "name": "creator",
        "type": "object",
        "description": "Publicly visible clean room collaborator.",
        "children": [
          {
            "name": "collaborator_alias",
            "type": "string",
            "description": "Collaborator alias specified by the clean room creator. It is unique across all collaborators of this clean room, and used to derive multiple values internally such as catalog alias and clean room name for single metastore clean rooms. It should follow [UC securable naming requirements]. [UC securable naming requirements]: https://docs.databricks.com/en/data-governance/unity-catalog/index.html#securable-object-naming-requirements"
          },
          {
            "name": "display_name",
            "type": "string",
            "description": "Generated display name for the collaborator. In the case of a single metastore clean room, it is the clean room name. For x-metastore clean rooms, it is the organization name of the metastore. It is not restricted to these values and could change in the future"
          },
          {
            "name": "global_metastore_id",
            "type": "string",
            "description": "The global Unity Catalog metastore ID of the collaborator. The identifier is of format cloud:region:metastore-uuid."
          },
          {
            "name": "invite_recipient_email",
            "type": "string",
            "description": "Email of the user who is receiving the clean room \"invitation\". It should be empty for the creator of the clean room, and non-empty for the invitees of the clean room. It is only returned in the output when clean room creator calls GET"
          },
          {
            "name": "invite_recipient_workspace_id",
            "type": "integer",
            "description": "Workspace ID of the user who is receiving the clean room \"invitation\". Must be specified if invite_recipient_email is specified. It should be empty when the collaborator is the creator of the clean room."
          },
          {
            "name": "organization_name",
            "type": "string",
            "description": "[Organization name](:method:metastores/list#metastores-delta_sharing_organization_name) configured in the metastore"
          }
        ]
      },
      {
        "name": "egress_network_policy",
        "type": "string",
        "description": "Egress network policy to apply to the central clean room workspace."
      },
      {
        "name": "region",
        "type": "string",
        "description": "Region of the central clean room."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Clean room status. (ACTIVE, DELETED, FAILED, PROVISIONING)"
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "When the clean room was last updated, in epoch milliseconds."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get the details of a clean room given its name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get a list of all clean rooms of the metastore. Only clean rooms the caller has access to are</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-clean_room"><code>clean_room</code></a></td>
    <td></td>
    <td>Create a new clean room with the specified collaborators. This method is asynchronous; the returned</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update a clean room. The caller must be the owner of the clean room, have **MODIFY_CLEAN_ROOM**</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a clean room. After deletion, the clean room will be removed from the metastore. If the other</td>
</tr>
<tr>
    <td><a href="#create_output_catalog"><CopyableCode code="create_output_catalog" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-output_catalog"><code>output_catalog</code></a></td>
    <td></td>
    <td>Create the output catalog of the clean room.</td>
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
<tr id="parameter-clean_room_name">
    <td><CopyableCode code="clean_room_name" /></td>
    <td><code>string</code></td>
    <td>Name of the clean room.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the clean room.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Maximum number of clean rooms to return (i.e., the page length). Defaults to 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
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

Get the details of a clean room given its name.

```sql
SELECT
name,
access_restricted,
comment,
created_at,
local_collaborator_alias,
output_catalog,
owner,
remote_detailed_info,
status,
updated_at
FROM databricks_workspace.cleanrooms.clean_rooms
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all clean rooms of the metastore. Only clean rooms the caller has access to are

```sql
SELECT
name,
access_restricted,
comment,
created_at,
local_collaborator_alias,
output_catalog,
owner,
remote_detailed_info,
status,
updated_at
FROM databricks_workspace.cleanrooms.clean_rooms
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
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

Create a new clean room with the specified collaborators. This method is asynchronous; the returned

```sql
INSERT INTO databricks_workspace.cleanrooms.clean_rooms (
clean_room,
deployment_name
)
SELECT 
'{{ clean_room }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
access_restricted,
comment,
created_at,
local_collaborator_alias,
output_catalog,
owner,
remote_detailed_info,
status,
updated_at
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: clean_rooms
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the clean_rooms resource.
    - name: clean_room
      value: string
      description: |
        :returns: Long-running operation waiter for :class:`CleanRoom`. See :method:wait_get_clean_room_active for more details.
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a clean room. The caller must be the owner of the clean room, have **MODIFY_CLEAN_ROOM**

```sql
UPDATE databricks_workspace.cleanrooms.clean_rooms
SET 
clean_room = '{{ clean_room }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
access_restricted,
comment,
created_at,
local_collaborator_alias,
output_catalog,
owner,
remote_detailed_info,
status,
updated_at;
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

Delete a clean room. After deletion, the clean room will be removed from the metastore. If the other

```sql
DELETE FROM databricks_workspace.cleanrooms.clean_rooms
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_output_catalog"
    values={[
        { label: 'create_output_catalog', value: 'create_output_catalog' }
    ]}
>
<TabItem value="create_output_catalog">

Create the output catalog of the clean room.

```sql
EXEC databricks_workspace.cleanrooms.clean_rooms.create_output_catalog 
@clean_room_name='{{ clean_room_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"output_catalog": "{{ output_catalog }}"
}'
;
```
</TabItem>
</Tabs>

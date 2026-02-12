---
title: auto_approval_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_approval_rules
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

Creates, updates, deletes, gets or lists an <code>auto_approval_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_approval_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.auto_approval_rules" /></td></tr>
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
    "name": "rule_id",
    "type": "string",
    "description": "A generated UUID identifying the rule."
  },
  {
    "name": "clean_room_name",
    "type": "string",
    "description": "The name of the clean room this auto-approval rule belongs to."
  },
  {
    "name": "author_collaborator_alias",
    "type": "string",
    "description": ""
  },
  {
    "name": "author_scope",
    "type": "string",
    "description": "Scope of authors covered by the rule. Only one of `author_collaborator_alias` and `author_scope` can be set."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Timestamp of when the rule was created, in epoch milliseconds."
  },
  {
    "name": "rule_owner_collaborator_alias",
    "type": "string",
    "description": "The owner of the rule to whom the rule applies."
  },
  {
    "name": "runner_collaborator_alias",
    "type": "string",
    "description": "Collaborator alias of the runner covered by the rule."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "rule_id",
    "type": "string",
    "description": "A generated UUID identifying the rule."
  },
  {
    "name": "clean_room_name",
    "type": "string",
    "description": "The name of the clean room this auto-approval rule belongs to."
  },
  {
    "name": "author_collaborator_alias",
    "type": "string",
    "description": ""
  },
  {
    "name": "author_scope",
    "type": "string",
    "description": "Scope of authors covered by the rule. Only one of `author_collaborator_alias` and `author_scope` can be set."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Timestamp of when the rule was created, in epoch milliseconds."
  },
  {
    "name": "rule_owner_collaborator_alias",
    "type": "string",
    "description": "The owner of the rule to whom the rule applies."
  },
  {
    "name": "runner_collaborator_alias",
    "type": "string",
    "description": "Collaborator alias of the runner covered by the rule."
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
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a auto-approval rule by rule ID</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all auto-approval rules for the caller</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__auto_approval_rule"><code>data__auto_approval_rule</code></a></td>
    <td></td>
    <td>Create an auto-approval rule</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__auto_approval_rule"><code>data__auto_approval_rule</code></a></td>
    <td></td>
    <td>Update a auto-approval rule by rule ID</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a auto-approval rule by rule ID</td>
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
    <td>:param rule_id: str</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-rule_id">
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get a auto-approval rule by rule ID

```sql
SELECT
rule_id,
clean_room_name,
author_collaborator_alias,
author_scope,
created_at,
rule_owner_collaborator_alias,
runner_collaborator_alias
FROM databricks_workspace.cleanrooms.auto_approval_rules
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND rule_id = '{{ rule_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all auto-approval rules for the caller

```sql
SELECT
rule_id,
clean_room_name,
author_collaborator_alias,
author_scope,
created_at,
rule_owner_collaborator_alias,
runner_collaborator_alias
FROM databricks_workspace.cleanrooms.auto_approval_rules
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Create an auto-approval rule

```sql
INSERT INTO databricks_workspace.cleanrooms.auto_approval_rules (
data__auto_approval_rule,
clean_room_name,
deployment_name
)
SELECT 
'{{ auto_approval_rule }}' /* required */,
'{{ clean_room_name }}',
'{{ deployment_name }}'
RETURNING
rule_id,
clean_room_name,
author_collaborator_alias,
author_scope,
created_at,
rule_owner_collaborator_alias,
runner_collaborator_alias
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: auto_approval_rules
  props:
    - name: clean_room_name
      value: string
      description: Required parameter for the auto_approval_rules resource.
    - name: deployment_name
      value: string
      description: Required parameter for the auto_approval_rules resource.
    - name: auto_approval_rule
      value: string
      description: |
        :returns: :class:`CleanRoomAutoApprovalRule`
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

Update a auto-approval rule by rule ID

```sql
UPDATE databricks_workspace.cleanrooms.auto_approval_rules
SET 
data__auto_approval_rule = '{{ auto_approval_rule }}'
WHERE 
clean_room_name = '{{ clean_room_name }}' --required
AND rule_id = '{{ rule_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__auto_approval_rule = '{{ auto_approval_rule }}' --required
RETURNING
rule_id,
clean_room_name,
author_collaborator_alias,
author_scope,
created_at,
rule_owner_collaborator_alias,
runner_collaborator_alias;
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

Delete a auto-approval rule by rule ID

```sql
DELETE FROM databricks_workspace.cleanrooms.auto_approval_rules
WHERE clean_room_name = '{{ clean_room_name }}' --required
AND rule_id = '{{ rule_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

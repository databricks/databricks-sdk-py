---
title: model_registry_transitions
hide_title: false
hide_table_of_contents: false
keywords:
  - model_registry_transitions
  - ml
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>model_registry_transitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="model_registry_transitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.model_registry_transitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Unique identifier for the object."
  },
  {
    "name": "user_id",
    "type": "string",
    "description": "The username of the user that created the object."
  },
  {
    "name": "activity_type",
    "type": "string",
    "description": "Type of activity. Valid values are: * `APPLIED_TRANSITION`: User applied the corresponding stage<br />transition.<br /><br />* `REQUESTED_TRANSITION`: User requested the corresponding stage transition.<br /><br />* `CANCELLED_REQUEST`: User cancelled an existing transition request.<br /><br />* `APPROVED_REQUEST`: User approved the corresponding stage transition.<br /><br />* `REJECTED_REQUEST`: User rejected the coressponding stage transition.<br /><br />* `SYSTEM_TRANSITION`: For events performed as a side effect, such as archiving existing model<br />versions in a stage. (APPLIED_TRANSITION, APPROVED_REQUEST, CANCELLED_REQUEST, NEW_COMMENT, REJECTED_REQUEST, REQUESTED_TRANSITION, SYSTEM_TRANSITION)"
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided comment associated with the activity, comment, or transition request."
  },
  {
    "name": "creation_timestamp",
    "type": "integer",
    "description": "Creation time of the object, as a Unix timestamp in milliseconds."
  },
  {
    "name": "from_stage",
    "type": "string",
    "description": "Source stage of the transition (if the activity is stage transition related). Valid values are: * `None`: The initial stage of a model version. * `Staging`: Staging or pre-production stage. * `Production`: Production stage. * `Archived`: Archived stage."
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Time of the object at last update, as a Unix timestamp in milliseconds."
  },
  {
    "name": "system_comment",
    "type": "string",
    "description": "Comment made by system, for example explaining an activity of type `SYSTEM_TRANSITION`. It usually describes a side effect, such as a version being archived as part of another version's stage transition, and may not be returned for some activity types."
  },
  {
    "name": "to_stage",
    "type": "string",
    "description": "Target stage of the transition (if the activity is stage transition related). Valid values are: * `None`: The initial stage of a model version. * `Staging`: Staging or pre-production stage. * `Production`: Production stage. * `Archived`: Archived stage."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a list of all open stage transition requests for the model version.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-stage"><code>stage</code></a></td>
    <td></td>
    <td>Creates a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#approve"><CopyableCode code="approve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-stage"><code>stage</code></a>, <a href="#parameter-archive_existing_versions"><code>archive_existing_versions</code></a></td>
    <td></td>
    <td>Approves a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-stage"><code>stage</code></a>, <a href="#parameter-creator"><code>creator</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-comment"><code>comment</code></a></td>
    <td>Cancels a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#reject"><CopyableCode code="reject" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-stage"><code>stage</code></a></td>
    <td></td>
    <td>Rejects a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#transition"><CopyableCode code="transition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-stage"><code>stage</code></a>, <a href="#parameter-archive_existing_versions"><code>archive_existing_versions</code></a></td>
    <td></td>
    <td>Transition a model version's stage. This is a Databricks workspace version of the [MLflow endpoint]</td>
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
<tr id="parameter-creator">
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td>Username of the user who created this request. Of the transition requests matching the specified details, only the one transition created by this user will be deleted.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the model.</td>
</tr>
<tr id="parameter-stage">
    <td><CopyableCode code="stage" /></td>
    <td><code>string</code></td>
    <td>Target stage of the transition request. Valid values are: * `None`: The initial stage of a model version. * `Staging`: Staging or pre-production stage. * `Production`: Production stage. * `Archived`: Archived stage.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the model.</td>
</tr>
<tr id="parameter-comment">
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>User-provided comment on the action.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets a list of all open stage transition requests for the model version.

```sql
SELECT
id,
user_id,
activity_type,
comment,
creation_timestamp,
from_stage,
last_updated_timestamp,
system_comment,
to_stage
FROM databricks_workspace.ml.model_registry_transitions
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Creates a model version stage transition request.

```sql
INSERT INTO databricks_workspace.ml.model_registry_transitions (
name,
version,
stage,
comment,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ version }}' /* required */,
'{{ stage }}' /* required */,
'{{ comment }}',
'{{ deployment_name }}'
RETURNING
request
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: model_registry_transitions
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the model_registry_transitions resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the model.
    - name: version
      value: "{{ version }}"
      description: |
        Version of the model.
    - name: stage
      value: "{{ stage }}"
      description: |
        Target stage of the transition. Valid values are: * \`None\`: The initial stage of a model version. * \`Staging\`: Staging or pre-production stage. * \`Production\`: Production stage. * \`Archived\`: Archived stage.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided comment on the action.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="approve"
    values={[
        { label: 'approve', value: 'approve' },
        { label: 'delete', value: 'delete' },
        { label: 'reject', value: 'reject' },
        { label: 'transition', value: 'transition' }
    ]}
>
<TabItem value="approve">

Approves a model version stage transition request.

```sql
EXEC databricks_workspace.ml.model_registry_transitions.approve 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"version": "{{ version }}", 
"stage": "{{ stage }}", 
"archive_existing_versions": {{ archive_existing_versions }}, 
"comment": "{{ comment }}"
}'
;
```
</TabItem>
<TabItem value="delete">

Cancels a model version stage transition request.

```sql
EXEC databricks_workspace.ml.model_registry_transitions.delete 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@stage='{{ stage }}' --required, 
@creator='{{ creator }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@comment='{{ comment }}'
;
```
</TabItem>
<TabItem value="reject">

Rejects a model version stage transition request.

```sql
EXEC databricks_workspace.ml.model_registry_transitions.reject 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"version": "{{ version }}", 
"stage": "{{ stage }}", 
"comment": "{{ comment }}"
}'
;
```
</TabItem>
<TabItem value="transition">

Transition a model version's stage. This is a Databricks workspace version of the [MLflow endpoint]

```sql
EXEC databricks_workspace.ml.model_registry_transitions.transition 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"version": "{{ version }}", 
"stage": "{{ stage }}", 
"archive_existing_versions": {{ archive_existing_versions }}, 
"comment": "{{ comment }}"
}'
;
```
</TabItem>
</Tabs>

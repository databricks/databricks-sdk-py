---
title: instance_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profiles
  - compute
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

Creates, updates, deletes, gets or lists an <code>instance_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="instance_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.instance_profiles" /></td></tr>
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
    "name": "iam_role_arn",
    "type": "string",
    "description": "The AWS IAM role ARN of the role associated with the instance profile. This field is required if your role name and instance profile name do not match and you want to use the instance profile with [Databricks SQL Serverless]. Otherwise, this field is optional. [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html"
  },
  {
    "name": "instance_profile_arn",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_meta_instance_profile",
    "type": "boolean",
    "description": "Boolean flag indicating whether the instance profile should only be used in credential passthrough scenarios. If true, it means the instance profile contains an meta IAM role which could assume a wide range of roles. Therefore it should always be used with authorization. This field is optional, the default value is `false`."
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
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>List the instance profiles that the calling user can use to launch a cluster.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-instance_profile_arn"><code>instance_profile_arn</code></a></td>
    <td></td>
    <td>Registers an instance profile in Databricks. In the UI, you can then give users the permission to use</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-instance_profile_arn"><code>instance_profile_arn</code></a></td>
    <td></td>
    <td>The only supported field to change is the optional IAM role ARN associated with the instance profile.</td>
</tr>
<tr>
    <td><a href="#remove"><CopyableCode code="remove" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Remove the instance profile with the provided ARN. Existing clusters with this instance profile will</td>
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
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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

List the instance profiles that the calling user can use to launch a cluster.

```sql
SELECT
iam_role_arn,
instance_profile_arn,
is_meta_instance_profile
FROM databricks_workspace.compute.instance_profiles
WHERE workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="add">

Registers an instance profile in Databricks. In the UI, you can then give users the permission to use

```sql
INSERT INTO databricks_workspace.compute.instance_profiles (
instance_profile_arn,
iam_role_arn,
is_meta_instance_profile,
skip_validation,
workspace
)
SELECT 
'{{ instance_profile_arn }}' /* required */,
'{{ iam_role_arn }}',
{{ is_meta_instance_profile }},
{{ skip_validation }},
'{{ workspace }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: instance_profiles
  props:
    - name: workspace
      value: string
      description: Required parameter for the instance_profiles resource.
    - name: instance_profile_arn
      value: string
      description: |
        The AWS ARN of the instance profile to register with Databricks. This field is required.
    - name: iam_role_arn
      value: string
      description: |
        The AWS IAM role ARN of the role associated with the instance profile. This field is required if your role name and instance profile name do not match and you want to use the instance profile with [Databricks SQL Serverless]. Otherwise, this field is optional. [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
    - name: is_meta_instance_profile
      value: boolean
      description: |
        Boolean flag indicating whether the instance profile should only be used in credential passthrough scenarios. If true, it means the instance profile contains an meta IAM role which could assume a wide range of roles. Therefore it should always be used with authorization. This field is optional, the default value is `false`.
    - name: skip_validation
      value: boolean
      description: |
        By default, Databricks validates that it has sufficient permissions to launch instances with the instance profile. This validation uses AWS dry-run mode for the RunInstances API. If validation fails with an error message that does not indicate an IAM related permission issue, (e.g. “Your requested instance type is not supported in your requested availability zone”), you can pass this flag to skip the validation and forcibly add the instance profile.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

The only supported field to change is the optional IAM role ARN associated with the instance profile.

```sql
REPLACE databricks_workspace.compute.instance_profiles
SET 
instance_profile_arn = '{{ instance_profile_arn }}',
iam_role_arn = '{{ iam_role_arn }}',
is_meta_instance_profile = {{ is_meta_instance_profile }}
WHERE 
workspace = '{{ workspace }}' --required
AND instance_profile_arn = '{{ instance_profile_arn }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="remove"
    values={[
        { label: 'remove', value: 'remove' }
    ]}
>
<TabItem value="remove">

Remove the instance profile with the provided ARN. Existing clusters with this instance profile will

```sql
DELETE FROM databricks_workspace.compute.instance_profiles
WHERE workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

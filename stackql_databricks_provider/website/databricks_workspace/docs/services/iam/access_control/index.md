---
title: access_control
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control
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

Creates, updates, deletes, gets or lists an <code>access_control</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.access_control" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check"
    values={[
        { label: 'check', value: 'check' }
    ]}
>
<TabItem value="check">

<SchemaTable fields={[
  {
    "name": "consistency_token",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "is_permitted",
    "type": "boolean",
    "description": ""
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
    <td><a href="#check"><CopyableCode code="check" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-actor"><code>actor</code></a>, <a href="#parameter-permission"><code>permission</code></a>, <a href="#parameter-resource"><code>resource</code></a>, <a href="#parameter-consistency_token"><code>consistency_token</code></a>, <a href="#parameter-authz_identity"><code>authz_identity</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-resource_info"><code>resource_info</code></a></td>
    <td>Check access policy to a resource.</td>
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
<tr id="parameter-actor">
    <td><CopyableCode code="actor" /></td>
    <td><code>string</code></td>
    <td>:param permission: str</td>
</tr>
<tr id="parameter-authz_identity">
    <td><CopyableCode code="authz_identity" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-consistency_token">
    <td><CopyableCode code="consistency_token" /></td>
    <td><code>string</code></td>
    <td>:param authz_identity: :class:`RequestAuthzIdentity`</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-permission">
    <td><CopyableCode code="permission" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-resource">
    <td><CopyableCode code="resource" /></td>
    <td><code>string</code></td>
    <td>Ex: (servicePrincipal/use, accounts/&lt;account-id&gt;/servicePrincipals/&lt;sp-id&gt;) Ex: (servicePrincipal.ruleSet/update, accounts/&lt;account-id&gt;/servicePrincipals/&lt;sp-id&gt;/ruleSets/default)</td>
</tr>
<tr id="parameter-resource_info">
    <td><CopyableCode code="resource_info" /></td>
    <td><code>string</code></td>
    <td>:returns: :class:`CheckPolicyResponse`</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="check"
    values={[
        { label: 'check', value: 'check' }
    ]}
>
<TabItem value="check">

Check access policy to a resource.

```sql
SELECT
consistency_token,
is_permitted
FROM databricks_workspace.iam.access_control
WHERE actor = '{{ actor }}' -- required
AND permission = '{{ permission }}' -- required
AND resource = '{{ resource }}' -- required
AND consistency_token = '{{ consistency_token }}' -- required
AND authz_identity = '{{ authz_identity }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND resource_info = '{{ resource_info }}'
;
```
</TabItem>
</Tabs>

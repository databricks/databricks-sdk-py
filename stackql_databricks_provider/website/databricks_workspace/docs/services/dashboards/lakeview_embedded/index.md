---
title: lakeview_embedded
hide_title: false
hide_table_of_contents: false
keywords:
  - lakeview_embedded
  - dashboards
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

Creates, updates, deletes, gets or lists a <code>lakeview_embedded</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lakeview_embedded" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.lakeview_embedded" /></td></tr>
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
    "name": "authorization_details",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "grant_rules",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "permission_set",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "resource_legacy_acl_path",
        "type": "string",
        "description": "The acl path of the tree store resource resource."
      },
      {
        "name": "resource_name",
        "type": "string",
        "description": "The resource name to which the authorization rule applies. This field is specific to `workspace_rule_set` constraint. Format: `workspaces/&#123;workspace_id&#125;/dashboards/&#123;dashboard_id&#125;`"
      },
      {
        "name": "type",
        "type": "string",
        "description": "The type of authorization downscoping policy. Ex: `workspace_rule_set` defines access rules for a specific workspace resource"
      }
    ]
  },
  {
    "name": "custom_claim",
    "type": "string",
    "description": "Custom claim generated from external_value and external_viewer_id. Format: `urn:aibi:external_data:<external_value>:<external_viewer_id>:<dashboard_id>`"
  },
  {
    "name": "scope",
    "type": "string",
    "description": "Scope defining access permissions."
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
    <td><a href="#parameter-dashboard_id"><code>dashboard_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-external_value"><code>external_value</code></a>, <a href="#parameter-external_viewer_id"><code>external_viewer_id</code></a></td>
    <td>Get a required authorization details and scopes of a published dashboard to mint an OAuth token.</td>
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
<tr id="parameter-dashboard_id">
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td>UUID identifying the published dashboard.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-external_value">
    <td><CopyableCode code="external_value" /></td>
    <td><code>string</code></td>
    <td>Provided external value to be included in the custom claim.</td>
</tr>
<tr id="parameter-external_viewer_id">
    <td><CopyableCode code="external_viewer_id" /></td>
    <td><code>string</code></td>
    <td>Provided external viewer id to be included in the custom claim.</td>
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

Get a required authorization details and scopes of a published dashboard to mint an OAuth token.

```sql
SELECT
authorization_details,
custom_claim,
scope
FROM databricks_workspace.dashboards.lakeview_embedded
WHERE dashboard_id = '{{ dashboard_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND external_value = '{{ external_value }}'
AND external_viewer_id = '{{ external_viewer_id }}'
;
```
</TabItem>
</Tabs>

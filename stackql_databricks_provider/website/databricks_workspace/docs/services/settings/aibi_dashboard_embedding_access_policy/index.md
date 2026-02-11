---
title: aibi_dashboard_embedding_access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - aibi_dashboard_embedding_access_policy
  - settings
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

Creates, updates, deletes, gets or lists an <code>aibi_dashboard_embedding_access_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aibi_dashboard_embedding_access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.aibi_dashboard_embedding_access_policy" /></td></tr>
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
    "name": "setting_name",
    "type": "string",
    "description": "Name of the corresponding setting. This field is populated in the response, but it will not be respected even if it's set in the request body. The setting name in the path parameter will be respected instead. Setting name is required to be 'default' if the setting only has one instance per workspace."
  },
  {
    "name": "aibi_dashboard_embedding_access_policy",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "access_policy_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      }
    ]
  },
  {
    "name": "etag",
    "type": "string",
    "description": "etag used for versioning. The response is at least as fresh as the eTag provided. This is used for optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting each other. It is strongly suggested that systems make use of the etag in the read -&gt; update pattern to perform setting updates in order to avoid race conditions. That is, get an etag from a GET request, and pass it with the PATCH request to identify the setting version you are updating."
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Retrieves the AI/BI dashboard embedding access policy. The default setting is ALLOW_APPROVED_DOMAINS,<br />permitting AI/BI dashboards to be embedded on approved domains.<br /><br />:param etag: str (optional)<br />  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for<br />  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting<br />  each other. It is strongly suggested that systems make use of the etag in the read -&gt; delete pattern<br />  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET<br />  request, and pass it with the DELETE request to identify the rule set version you are deleting.<br /><br />:returns: :class:`AibiDashboardEmbeddingAccessPolicySetting`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__allow_missing"><code>data__allow_missing</code></a>, <a href="#parameter-data__setting"><code>data__setting</code></a>, <a href="#parameter-data__field_mask"><code>data__field_mask</code></a></td>
    <td></td>
    <td>Updates the AI/BI dashboard embedding access policy at the workspace level.<br /><br />:param allow_missing: bool<br />  This should always be set to true for Settings API. Added for AIP compliance.<br />:param setting: :class:`AibiDashboardEmbeddingAccessPolicySetting`<br />:param field_mask: str<br />  The field mask must be a single string, with multiple fields separated by commas (no spaces). The<br />  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,<br />  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only<br />  the entire collection field can be specified. Field names must exactly match the resource field<br />  names.<br /><br />  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the<br />  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API<br />  changes in the future.<br /><br />:returns: :class:`AibiDashboardEmbeddingAccessPolicySetting`</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Delete the AI/BI dashboard embedding access policy, reverting back to the default.<br /><br />:param etag: str (optional)<br />  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for<br />  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting<br />  each other. It is strongly suggested that systems make use of the etag in the read -&gt; delete pattern<br />  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET<br />  request, and pass it with the DELETE request to identify the rule set version you are deleting.<br /><br />:returns: :class:`DeleteAibiDashboardEmbeddingAccessPolicySettingResponse`</td>
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
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag used for versioning. The response is at least as fresh as the eTag provided. This is used for optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting each other. It is strongly suggested that systems make use of the etag in the read -&gt; delete pattern to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET request, and pass it with the DELETE request to identify the rule set version you are deleting.</td>
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

Retrieves the AI/BI dashboard embedding access policy. The default setting is ALLOW_APPROVED_DOMAINS,<br />permitting AI/BI dashboards to be embedded on approved domains.<br /><br />:param etag: str (optional)<br />  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for<br />  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting<br />  each other. It is strongly suggested that systems make use of the etag in the read -&gt; delete pattern<br />  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET<br />  request, and pass it with the DELETE request to identify the rule set version you are deleting.<br /><br />:returns: :class:`AibiDashboardEmbeddingAccessPolicySetting`

```sql
SELECT
setting_name,
aibi_dashboard_embedding_access_policy,
etag
FROM databricks_workspace.settings.aibi_dashboard_embedding_access_policy
WHERE deployment_name = '{{ deployment_name }}' -- required
AND etag = '{{ etag }}'
;
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

Updates the AI/BI dashboard embedding access policy at the workspace level.<br /><br />:param allow_missing: bool<br />  This should always be set to true for Settings API. Added for AIP compliance.<br />:param setting: :class:`AibiDashboardEmbeddingAccessPolicySetting`<br />:param field_mask: str<br />  The field mask must be a single string, with multiple fields separated by commas (no spaces). The<br />  field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,<br />  `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only<br />  the entire collection field can be specified. Field names must exactly match the resource field<br />  names.<br /><br />  A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the<br />  fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API<br />  changes in the future.<br /><br />:returns: :class:`AibiDashboardEmbeddingAccessPolicySetting`

```sql
UPDATE databricks_workspace.settings.aibi_dashboard_embedding_access_policy
SET 
data__allow_missing = {{ allow_missing }},
data__setting = '{{ setting }}',
data__field_mask = '{{ field_mask }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND data__allow_missing = {{ allow_missing }} --required
AND data__setting = '{{ setting }}' --required
AND data__field_mask = '{{ field_mask }}' --required
RETURNING
setting_name,
aibi_dashboard_embedding_access_policy,
etag;
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

Delete the AI/BI dashboard embedding access policy, reverting back to the default.<br /><br />:param etag: str (optional)<br />  etag used for versioning. The response is at least as fresh as the eTag provided. This is used for<br />  optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting<br />  each other. It is strongly suggested that systems make use of the etag in the read -&gt; delete pattern<br />  to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET<br />  request, and pass it with the DELETE request to identify the rule set version you are deleting.<br /><br />:returns: :class:`DeleteAibiDashboardEmbeddingAccessPolicySettingResponse`

```sql
DELETE FROM databricks_workspace.settings.aibi_dashboard_embedding_access_policy
WHERE deployment_name = '{{ deployment_name }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>

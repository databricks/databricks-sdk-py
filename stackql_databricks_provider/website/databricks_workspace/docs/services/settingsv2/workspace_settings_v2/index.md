---
title: workspace_settings_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_settings_v2
  - settingsv2
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

Creates, updates, deletes, gets or lists a <code>workspace_settings_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_settings_v2" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settingsv2.workspace_settings_v2" /></td></tr>
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
    "description": "Name of the setting."
  },
  {
    "name": "aibi_dashboard_embedding_access_policy",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "access_policy_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ALLOW_ALL_DOMAINS, ALLOW_APPROVED_DOMAINS, DENY_ALL_DOMAINS)"
      }
    ]
  },
  {
    "name": "aibi_dashboard_embedding_approved_domains",
    "type": "object",
    "description": "Setting value for aibi_dashboard_embedding_approved_domains setting. This is the setting value set by consumers, check effective_aibi_dashboard_embedding_approved_domains for final setting value.",
    "children": [
      {
        "name": "approved_domains",
        "type": "array",
        "description": ""
      }
    ]
  },
  {
    "name": "automatic_cluster_update_workspace",
    "type": "object",
    "description": "Setting value for automatic_cluster_update_workspace setting. This is the setting value set by consumers, check effective_automatic_cluster_update_workspace for final setting value.",
    "children": [
      {
        "name": "can_toggle",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "enabled",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "enablement_details",
        "type": "object",
        "description": "Contains an information about the enablement status judging (e.g. whether the enterprise tier is<br />    enabled) This is only additional information that MUST NOT be used to decide whether the setting<br />    is enabled or not. This is intended to use only for purposes like showing an error message to<br />    the customer with the additional details. For example, using these details we can check why<br />    exactly the feature is disabled for this customer.",
        "children": [
          {
            "name": "forced_for_compliance_mode",
            "type": "boolean",
            "description": "The feature is force enabled if compliance mode is active"
          },
          {
            "name": "unavailable_for_disabled_entitlement",
            "type": "boolean",
            "description": "The feature is unavailable if the corresponding entitlement disabled (see getShieldEntitlementEnable)"
          },
          {
            "name": "unavailable_for_non_enterprise_tier",
            "type": "boolean",
            "description": "The feature is unavailable if the customer doesn't have enterprise tier"
          }
        ]
      },
      {
        "name": "maintenance_window",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "week_day_based_schedule",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "day_of_week",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY)"
              },
              {
                "name": "frequency",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EVERY_WEEK, FIRST_AND_THIRD_OF_MONTH, FIRST_OF_MONTH, FOURTH_OF_MONTH, SECOND_AND_FOURTH_OF_MONTH, SECOND_OF_MONTH, THIRD_OF_MONTH)"
              },
              {
                "name": "window_start_time",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "restart_even_if_no_updates_available",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "boolean_val",
    "type": "object",
    "description": "Setting value for boolean type setting. This is the setting value set by consumers, check effective_boolean_val for final setting value.",
    "children": [
      {
        "name": "value",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_aibi_dashboard_embedding_access_policy",
    "type": "object",
    "description": "Effective setting value for aibi_dashboard_embedding_access_policy setting. This is the final effective value of setting. To set a value use aibi_dashboard_embedding_access_policy.",
    "children": [
      {
        "name": "access_policy_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ALLOW_ALL_DOMAINS, ALLOW_APPROVED_DOMAINS, DENY_ALL_DOMAINS)"
      }
    ]
  },
  {
    "name": "effective_aibi_dashboard_embedding_approved_domains",
    "type": "object",
    "description": "Effective setting value for aibi_dashboard_embedding_approved_domains setting. This is the final effective value of setting. To set a value use aibi_dashboard_embedding_approved_domains.",
    "children": [
      {
        "name": "approved_domains",
        "type": "array",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_automatic_cluster_update_workspace",
    "type": "object",
    "description": "Effective setting value for automatic_cluster_update_workspace setting. This is the final effective value of setting. To set a value use automatic_cluster_update_workspace.",
    "children": [
      {
        "name": "can_toggle",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "enabled",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "enablement_details",
        "type": "object",
        "description": "Contains an information about the enablement status judging (e.g. whether the enterprise tier is<br />    enabled) This is only additional information that MUST NOT be used to decide whether the setting<br />    is enabled or not. This is intended to use only for purposes like showing an error message to<br />    the customer with the additional details. For example, using these details we can check why<br />    exactly the feature is disabled for this customer.",
        "children": [
          {
            "name": "forced_for_compliance_mode",
            "type": "boolean",
            "description": "The feature is force enabled if compliance mode is active"
          },
          {
            "name": "unavailable_for_disabled_entitlement",
            "type": "boolean",
            "description": "The feature is unavailable if the corresponding entitlement disabled (see getShieldEntitlementEnable)"
          },
          {
            "name": "unavailable_for_non_enterprise_tier",
            "type": "boolean",
            "description": "The feature is unavailable if the customer doesn't have enterprise tier"
          }
        ]
      },
      {
        "name": "maintenance_window",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "week_day_based_schedule",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "day_of_week",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY)"
              },
              {
                "name": "frequency",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EVERY_WEEK, FIRST_AND_THIRD_OF_MONTH, FIRST_OF_MONTH, FOURTH_OF_MONTH, SECOND_AND_FOURTH_OF_MONTH, SECOND_OF_MONTH, THIRD_OF_MONTH)"
              },
              {
                "name": "window_start_time",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "restart_even_if_no_updates_available",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_boolean_val",
    "type": "object",
    "description": "Effective setting value for boolean type setting. This is the final effective value of setting. To set a value use boolean_val.",
    "children": [
      {
        "name": "value",
        "type": "boolean",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_integer_val",
    "type": "object",
    "description": "Effective setting value for integer type setting. This is the final effective value of setting. To set a value use integer_val.",
    "children": [
      {
        "name": "value",
        "type": "integer",
        "description": ""
      }
    ]
  },
  {
    "name": "effective_personal_compute",
    "type": "object",
    "description": "Effective setting value for personal_compute setting. This is the final effective value of setting. To set a value use personal_compute.",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing<br />all users to create single-machine compute resources. DELEGATE: Moves access control for the<br />Personal Compute default policy to individual workspaces and requires a workspace’s users or<br />groups to be added to the ACLs of that workspace’s Personal Compute default policy before they<br />will be able to create compute resources through that policy. (DELEGATE, ON)"
      }
    ]
  },
  {
    "name": "effective_restrict_workspace_admins",
    "type": "object",
    "description": "Effective setting value for restrict_workspace_admins setting. This is the final effective value of setting. To set a value use restrict_workspace_admins.",
    "children": [
      {
        "name": "status",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ALLOW_ALL, RESTRICT_TOKENS_AND_JOB_RUN_AS)"
      }
    ]
  },
  {
    "name": "effective_string_val",
    "type": "object",
    "description": "Effective setting value for string type setting. This is the final effective value of setting. To set a value use string_val.",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "integer_val",
    "type": "object",
    "description": "Setting value for integer type setting. This is the setting value set by consumers, check effective_integer_val for final setting value.",
    "children": [
      {
        "name": "value",
        "type": "integer",
        "description": ""
      }
    ]
  },
  {
    "name": "personal_compute",
    "type": "object",
    "description": "Setting value for personal_compute setting. This is the setting value set by consumers, check effective_personal_compute for final setting value.",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": "ON: Grants all users in all workspaces access to the Personal Compute default policy, allowing<br />all users to create single-machine compute resources. DELEGATE: Moves access control for the<br />Personal Compute default policy to individual workspaces and requires a workspace’s users or<br />groups to be added to the ACLs of that workspace’s Personal Compute default policy before they<br />will be able to create compute resources through that policy. (DELEGATE, ON)"
      }
    ]
  },
  {
    "name": "restrict_workspace_admins",
    "type": "object",
    "description": "Setting value for restrict_workspace_admins setting. This is the setting value set by consumers, check effective_restrict_workspace_admins for final setting value.",
    "children": [
      {
        "name": "status",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ALLOW_ALL, RESTRICT_TOKENS_AND_JOB_RUN_AS)"
      }
    ]
  },
  {
    "name": "string_val",
    "type": "object",
    "description": "Setting value for string type setting. This is the setting value set by consumers, check effective_string_val for final setting value.",
    "children": [
      {
        "name": "value",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the setting."
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "docs_link",
    "type": "string",
    "description": "Link to databricks documentation for the setting"
  },
  {
    "name": "type",
    "type": "string",
    "description": "Sample message depicting the type of the setting. To set this setting, the value sent must match this type."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get a setting value at workspace level. See :method:settingsv2/listworkspacesettingsmetadata for list</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List valid setting keys and metadata. These settings are available to be referenced via GET</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-setting"><code>setting</code></a></td>
    <td></td>
    <td>Patch a setting value at workspace level. See :method:settingsv2/listworkspacesettingsmetadata for</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the setting</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of settings to return. The service may return fewer than this value. If unspecified, at most 200 settings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous `ListWorkspaceSettingsMetadataRequest` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListWorkspaceSettingsMetadataRequest` must match the call that provided the page token.</td>
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

Get a setting value at workspace level. See :method:settingsv2/listworkspacesettingsmetadata for list

```sql
SELECT
name,
aibi_dashboard_embedding_access_policy,
aibi_dashboard_embedding_approved_domains,
automatic_cluster_update_workspace,
boolean_val,
effective_aibi_dashboard_embedding_access_policy,
effective_aibi_dashboard_embedding_approved_domains,
effective_automatic_cluster_update_workspace,
effective_boolean_val,
effective_integer_val,
effective_personal_compute,
effective_restrict_workspace_admins,
effective_string_val,
integer_val,
personal_compute,
restrict_workspace_admins,
string_val
FROM databricks_workspace.settingsv2.workspace_settings_v2
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

List valid setting keys and metadata. These settings are available to be referenced via GET

```sql
SELECT
name,
description,
docs_link,
type
FROM databricks_workspace.settingsv2.workspace_settings_v2
WHERE workspace = '{{ workspace }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' }
    ]}
>
<TabItem value="patch">

Patch a setting value at workspace level. See :method:settingsv2/listworkspacesettingsmetadata for

```sql
UPDATE databricks_workspace.settingsv2.workspace_settings_v2
SET 
setting = '{{ setting }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND setting = '{{ setting }}' --required
RETURNING
name,
aibi_dashboard_embedding_access_policy,
aibi_dashboard_embedding_approved_domains,
automatic_cluster_update_workspace,
boolean_val,
effective_aibi_dashboard_embedding_access_policy,
effective_aibi_dashboard_embedding_approved_domains,
effective_automatic_cluster_update_workspace,
effective_boolean_val,
effective_integer_val,
effective_personal_compute,
effective_restrict_workspace_admins,
effective_string_val,
integer_val,
personal_compute,
restrict_workspace_admins,
string_val;
```
</TabItem>
</Tabs>

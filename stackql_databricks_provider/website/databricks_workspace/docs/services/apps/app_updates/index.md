---
title: app_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - app_updates
  - apps
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

Creates, updates, deletes, gets or lists an <code>app_updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_updates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.app_updates" /></td></tr>
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
    "name": "budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "compute_size",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (LARGE, MEDIUM)"
  },
  {
    "name": "description",
    "type": "string",
    "description": ""
  },
  {
    "name": "git_repository",
    "type": "object",
    "description": "Git repository configuration specifying the location of the repository.",
    "children": [
      {
        "name": "url",
        "type": "string",
        "description": "URL of the Git repository."
      },
      {
        "name": "provider",
        "type": "string",
        "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
      }
    ]
  },
  {
    "name": "resources",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
          }
        ]
      },
      {
        "name": "serving_endpoint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FAILED, IN_PROGRESS, NOT_UPDATED, SUCCEEDED)"
      }
    ]
  },
  {
    "name": "user_api_scopes",
    "type": "array",
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Gets the status of an app update.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td></td>
    <td>Creates an app update and starts the update process. The update process is asynchronous and the status</td>
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
<tr id="parameter-app_name">
    <td><CopyableCode code="app_name" /></td>
    <td><code>string</code></td>
    <td>:param update_mask: str The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
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

Gets the status of an app update.

```sql
SELECT
budget_policy_id,
usage_policy_id,
compute_size,
description,
git_repository,
resources,
status,
user_api_scopes
FROM databricks_workspace.apps.app_updates
WHERE app_name = '{{ app_name }}' -- required
AND workspace = '{{ workspace }}' -- required
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

Creates an app update and starts the update process. The update process is asynchronous and the status

```sql
INSERT INTO databricks_workspace.apps.app_updates (
update_mask,
app,
app_name,
workspace
)
SELECT 
'{{ update_mask }}' /* required */,
'{{ app }}',
'{{ app_name }}',
'{{ workspace }}'
RETURNING
budget_policy_id,
usage_policy_id,
compute_size,
description,
git_repository,
resources,
status,
user_api_scopes
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_updates
  props:
    - name: app_name
      value: "{{ app_name }}"
      description: Required parameter for the app_updates resource.
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the app_updates resource.
    - name: update_mask
      value: "{{ update_mask }}"
    - name: app
      description: |
        :returns: Long-running operation waiter for :class:\`AppUpdate\`. See :method:wait_get_update_app_succeeded for more details.
      value:
        name: "{{ name }}"
        active_deployment:
          command:
            - "{{ command }}"
          create_time: "{{ create_time }}"
          creator: "{{ creator }}"
          deployment_artifacts:
            source_code_path: "{{ source_code_path }}"
          deployment_id: "{{ deployment_id }}"
          env_vars:
            - name: "{{ name }}"
              value: "{{ value }}"
              value_from: "{{ value_from }}"
          git_source:
            branch: "{{ branch }}"
            commit: "{{ commit }}"
            git_repository:
              url: "{{ url }}"
              provider: "{{ provider }}"
            resolved_commit: "{{ resolved_commit }}"
            source_code_path: "{{ source_code_path }}"
            tag: "{{ tag }}"
          mode: "{{ mode }}"
          source_code_path: "{{ source_code_path }}"
          status:
            message: "{{ message }}"
            state: "{{ state }}"
          update_time: "{{ update_time }}"
        app_status:
          message: "{{ message }}"
          state: "{{ state }}"
        budget_policy_id: "{{ budget_policy_id }}"
        compute_size: "{{ compute_size }}"
        compute_status:
          active_instances: {{ active_instances }}
          message: "{{ message }}"
          state: "{{ state }}"
        create_time: "{{ create_time }}"
        creator: "{{ creator }}"
        default_source_code_path: "{{ default_source_code_path }}"
        description: "{{ description }}"
        effective_budget_policy_id: "{{ effective_budget_policy_id }}"
        effective_usage_policy_id: "{{ effective_usage_policy_id }}"
        effective_user_api_scopes:
          - "{{ effective_user_api_scopes }}"
        git_repository:
          url: "{{ url }}"
          provider: "{{ provider }}"
        id: "{{ id }}"
        oauth2_app_client_id: "{{ oauth2_app_client_id }}"
        oauth2_app_integration_id: "{{ oauth2_app_integration_id }}"
        pending_deployment:
          command:
            - "{{ command }}"
          create_time: "{{ create_time }}"
          creator: "{{ creator }}"
          deployment_artifacts:
            source_code_path: "{{ source_code_path }}"
          deployment_id: "{{ deployment_id }}"
          env_vars:
            - name: "{{ name }}"
              value: "{{ value }}"
              value_from: "{{ value_from }}"
          git_source:
            branch: "{{ branch }}"
            commit: "{{ commit }}"
            git_repository:
              url: "{{ url }}"
              provider: "{{ provider }}"
            resolved_commit: "{{ resolved_commit }}"
            source_code_path: "{{ source_code_path }}"
            tag: "{{ tag }}"
          mode: "{{ mode }}"
          source_code_path: "{{ source_code_path }}"
          status:
            message: "{{ message }}"
            state: "{{ state }}"
          update_time: "{{ update_time }}"
        resources:
          - name: "{{ name }}"
            database:
              instance_name: "{{ instance_name }}"
              database_name: "{{ database_name }}"
              permission: "{{ permission }}"
            description: "{{ description }}"
            experiment:
              experiment_id: "{{ experiment_id }}"
              permission: "{{ permission }}"
            genie_space:
              name: "{{ name }}"
              space_id: "{{ space_id }}"
              permission: "{{ permission }}"
            job:
              id: "{{ id }}"
              permission: "{{ permission }}"
            secret:
              scope: "{{ scope }}"
              key: "{{ key }}"
              permission: "{{ permission }}"
            serving_endpoint:
              name: "{{ name }}"
              permission: "{{ permission }}"
            sql_warehouse:
              id: "{{ id }}"
              permission: "{{ permission }}"
            uc_securable:
              securable_full_name: "{{ securable_full_name }}"
              securable_type: "{{ securable_type }}"
              permission: "{{ permission }}"
        service_principal_client_id: "{{ service_principal_client_id }}"
        service_principal_id: {{ service_principal_id }}
        service_principal_name: "{{ service_principal_name }}"
        update_time: "{{ update_time }}"
        updater: "{{ updater }}"
        url: "{{ url }}"
        usage_policy_id: "{{ usage_policy_id }}"
        user_api_scopes:
          - "{{ user_api_scopes }}"
`}</CodeBlock>

</TabItem>
</Tabs>

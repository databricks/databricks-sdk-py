---
title: apps_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_settings
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>apps_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.apps_settings" /></td></tr>
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
    "description": ""
  },
  {
    "name": "creator",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the template."
  },
  {
    "name": "git_provider",
    "type": "string",
    "description": "The Git provider of the template."
  },
  {
    "name": "git_repo",
    "type": "string",
    "description": "The Git repository URL that the template resides in."
  },
  {
    "name": "manifest",
    "type": "object",
    "description": "The manifest of the template. It defines fields and default values when installing the template.",
    "children": [
      {
        "name": "version",
        "type": "integer",
        "description": "The manifest schema version, for now only 1 is allowed"
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the app defined by manifest author / publisher"
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the app defined by manifest author / publisher"
      },
      {
        "name": "resource_specs",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Name of the App Resource."
          },
          {
            "name": "description",
            "type": "string",
            "description": "Description of the App Resource."
          },
          {
            "name": "experiment_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
              }
            ]
          },
          {
            "name": "job_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
              }
            ]
          },
          {
            "name": "secret_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Permission to grant on the secret scope. Supported permissions are: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
              }
            ]
          },
          {
            "name": "serving_endpoint_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
              }
            ]
          },
          {
            "name": "sql_warehouse_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_MANAGE, CAN_USE, IS_OWNER)"
              }
            ]
          },
          {
            "name": "uc_securable_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "securable_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MANAGE, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "path",
    "type": "string",
    "description": "The path to the template within the Git repository."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "creator",
    "type": "string",
    "description": ""
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the template."
  },
  {
    "name": "git_provider",
    "type": "string",
    "description": "The Git provider of the template."
  },
  {
    "name": "git_repo",
    "type": "string",
    "description": "The Git repository URL that the template resides in."
  },
  {
    "name": "manifest",
    "type": "object",
    "description": "The manifest of the template. It defines fields and default values when installing the template.",
    "children": [
      {
        "name": "version",
        "type": "integer",
        "description": "The manifest schema version, for now only 1 is allowed"
      },
      {
        "name": "name",
        "type": "string",
        "description": "Name of the app defined by manifest author / publisher"
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the app defined by manifest author / publisher"
      },
      {
        "name": "resource_specs",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Name of the App Resource."
          },
          {
            "name": "description",
            "type": "string",
            "description": "Description of the App Resource."
          },
          {
            "name": "experiment_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
              }
            ]
          },
          {
            "name": "job_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
              }
            ]
          },
          {
            "name": "secret_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Permission to grant on the secret scope. Supported permissions are: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
              }
            ]
          },
          {
            "name": "serving_endpoint_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
              }
            ]
          },
          {
            "name": "sql_warehouse_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_MANAGE, CAN_USE, IS_OWNER)"
              }
            ]
          },
          {
            "name": "uc_securable_spec",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "securable_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MANAGE, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "path",
    "type": "string",
    "description": "The path to the template within the Git repository."
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
    <td>Gets the custom template with the specified name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all custom templates in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-template"><code>template</code></a></td>
    <td></td>
    <td>Creates a custom template.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-template"><code>template</code></a></td>
    <td></td>
    <td>Updates the custom template with the specified name. Note that the template name cannot be updated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes the custom template with the specified name.</td>
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
    <td>The name of the custom template.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of custom templates. Requests first page if absent.</td>
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

Gets the custom template with the specified name.

```sql
SELECT
name,
creator,
description,
git_provider,
git_repo,
manifest,
path
FROM databricks_workspace.apps.apps_settings
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all custom templates in the workspace.

```sql
SELECT
name,
creator,
description,
git_provider,
git_repo,
manifest,
path
FROM databricks_workspace.apps.apps_settings
WHERE workspace = '{{ workspace }}' -- required
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

Creates a custom template.

```sql
INSERT INTO databricks_workspace.apps.apps_settings (
template,
workspace
)
SELECT 
'{{ template }}' /* required */,
'{{ workspace }}'
RETURNING
name,
creator,
description,
git_provider,
git_repo,
manifest,
path
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: apps_settings
  props:
    - name: workspace
      value: string
      description: Required parameter for the apps_settings resource.
    - name: template
      value: object
      description: |
        :returns: :class:`CustomTemplate`
      props:
      - name: name
        value: string
      - name: git_repo
        value: string
        description: |
          The Git repository URL that the template resides in.
      - name: path
        value: string
        description: |
          The path to the template within the Git repository.
      - name: manifest
        value: object
        description: |
          The manifest of the template. It defines fields and default values when installing the template.
        props:
        - name: version
          value: integer
          description: |
            The manifest schema version, for now only 1 is allowed
        - name: name
          value: string
          description: |
            Name of the app defined by manifest author / publisher
        - name: description
          value: string
          description: |
            Description of the app defined by manifest author / publisher
        - name: resource_specs
          value: array
          props:
          - name: name
            value: string
            description: |
              Name of the App Resource.
          - name: description
            value: string
            description: |
              Description of the App Resource.
          - name: experiment_spec
            value: object
            props:
            - name: permission
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
          - name: job_spec
            value: object
            props:
            - name: permission
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
          - name: secret_spec
            value: object
            props:
            - name: permission
              value: string
              description: |
                Permission to grant on the secret scope. Supported permissions are: "READ", "WRITE", "MANAGE".
          - name: serving_endpoint_spec
            value: object
            props:
            - name: permission
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
          - name: sql_warehouse_spec
            value: object
            props:
            - name: permission
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
          - name: uc_securable_spec
            value: object
            props:
            - name: securable_type
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
            - name: permission
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
      - name: git_provider
        value: string
        description: |
          The Git provider of the template.
      - name: creator
        value: string
      - name: description
        value: string
        description: |
          The description of the template.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Updates the custom template with the specified name. Note that the template name cannot be updated.

```sql
REPLACE databricks_workspace.apps.apps_settings
SET 
template = '{{ template }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND template = '{{ template }}' --required
RETURNING
name,
creator,
description,
git_provider,
git_repo,
manifest,
path;
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

Deletes the custom template with the specified name.

```sql
DELETE FROM databricks_workspace.apps.apps_settings
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>

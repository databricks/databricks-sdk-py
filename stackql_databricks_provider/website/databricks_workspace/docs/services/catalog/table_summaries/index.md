---
title: table_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - table_summaries
  - catalog
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

Creates, updates, deletes, gets or lists a <code>table_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.table_summaries" /></td></tr>
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
    "name": "full_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "securable_kind_manifest",
    "type": "object",
    "description": "SecurableKindManifest of table, including capabilities the table has.",
    "children": [
      {
        "name": "assignable_privileges",
        "type": "array",
        "description": "Privileges that can be assigned to the securable."
      },
      {
        "name": "capabilities",
        "type": "array",
        "description": "A list of capabilities in the securable kind."
      },
      {
        "name": "options",
        "type": "array",
        "description": "Detailed specs of allowed options.",
        "children": [
          {
            "name": "allowed_values",
            "type": "array",
            "description": "For drop down / radio button selections, UI will want to know the possible input values, it can also be used by other option types to limit input selections."
          },
          {
            "name": "default_value",
            "type": "string",
            "description": "The default value of the option, for example, value '443' for 'port' option."
          },
          {
            "name": "description",
            "type": "string",
            "description": "A concise user facing description of what the input value of this option should look like."
          },
          {
            "name": "hint",
            "type": "string",
            "description": "The hint is used on the UI to suggest what the input value can possibly be like, for example: example.com for 'host' option. Unlike default value, it will not be applied automatically without user input."
          },
          {
            "name": "is_copiable",
            "type": "boolean",
            "description": "Indicates whether an option should be displayed with copy button on the UI."
          },
          {
            "name": "is_creatable",
            "type": "boolean",
            "description": "Indicates whether an option can be provided by users in the create/update path of an entity."
          },
          {
            "name": "is_hidden",
            "type": "boolean",
            "description": "Is the option value not user settable and is thus not shown on the UI."
          },
          {
            "name": "is_loggable",
            "type": "boolean",
            "description": "Specifies whether this option is safe to log, i.e. no sensitive information."
          },
          {
            "name": "is_required",
            "type": "boolean",
            "description": "Is the option required."
          },
          {
            "name": "is_secret",
            "type": "boolean",
            "description": "Is the option value considered secret and thus redacted on the UI."
          },
          {
            "name": "is_updatable",
            "type": "boolean",
            "description": "Is the option updatable by users."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The unique name of the option."
          },
          {
            "name": "oauth_stage",
            "type": "string",
            "description": "Specifies when the option value is displayed on the UI within the OAuth flow."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the option."
          }
        ]
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "Securable kind to get manifest of."
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable."
      }
    ]
  },
  {
    "name": "table_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_manifest_capabilities"><code>include_manifest_capabilities</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-schema_name_pattern"><code>schema_name_pattern</code></a>, <a href="#parameter-table_name_pattern"><code>table_name_pattern</code></a></td>
    <td>Gets an array of summaries for tables for a schema and catalog within the metastore. The table<br />summaries returned are either:<br /><br />* summaries for tables (within the current metastore and parent catalog and schema), when the user is<br />a metastore admin, or: * summaries for tables and schemas (within the current metastore and parent<br />catalog) for which the user has ownership or the **SELECT** privilege on the table and ownership or<br />**USE_SCHEMA** privilege on the schema, provided that the user also has ownership or the<br />**USE_CATALOG** privilege on the parent catalog.<br /><br />There is no guarantee of a specific ordering of the elements in the array.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str<br />  Name of parent catalog for tables of interest.<br />:param include_manifest_capabilities: bool (optional)<br />  Whether to include a manifest containing table capabilities in the response.<br />:param max_results: int (optional)<br />  Maximum number of summaries for tables to return. If not set, the page length is set to a server<br />  configured value (10000, as of 1/5/2024). - when set to a value greater than 0, the page length is<br />  the minimum of this value and a server configured value (10000, as of 1/5/2024); - when set to 0,<br />  the page length is set to a server configured value (10000, as of 1/5/2024) (recommended); - when<br />  set to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br />:param schema_name_pattern: str (optional)<br />  A sql LIKE pattern (% and _) for schema names. All schemas will be returned if not set or empty.<br />:param table_name_pattern: str (optional)<br />  A sql LIKE pattern (% and _) for table names. All tables will be returned if not set or empty.<br /><br />:returns: Iterator over :class:`TableSummary`</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Name of parent catalog for tables of interest.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-include_manifest_capabilities">
    <td><CopyableCode code="include_manifest_capabilities" /></td>
    <td><code>string</code></td>
    <td>Whether to include a manifest containing table capabilities in the response.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>string</code></td>
    <td>Maximum number of summaries for tables to return. If not set, the page length is set to a server configured value (10000, as of 1/5/2024). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value (10000, as of 1/5/2024); - when set to 0, the page length is set to a server configured value (10000, as of 1/5/2024) (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
<tr id="parameter-schema_name_pattern">
    <td><CopyableCode code="schema_name_pattern" /></td>
    <td><code>string</code></td>
    <td>A sql LIKE pattern (% and _) for schema names. All schemas will be returned if not set or empty.</td>
</tr>
<tr id="parameter-table_name_pattern">
    <td><CopyableCode code="table_name_pattern" /></td>
    <td><code>string</code></td>
    <td>A sql LIKE pattern (% and _) for table names. All tables will be returned if not set or empty.</td>
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

Gets an array of summaries for tables for a schema and catalog within the metastore. The table<br />summaries returned are either:<br /><br />* summaries for tables (within the current metastore and parent catalog and schema), when the user is<br />a metastore admin, or: * summaries for tables and schemas (within the current metastore and parent<br />catalog) for which the user has ownership or the **SELECT** privilege on the table and ownership or<br />**USE_SCHEMA** privilege on the schema, provided that the user also has ownership or the<br />**USE_CATALOG** privilege on the parent catalog.<br /><br />There is no guarantee of a specific ordering of the elements in the array.<br /><br />PAGINATION BEHAVIOR: The API is by default paginated, a page may contain zero results while still<br />providing a next_page_token. Clients must continue reading pages until next_page_token is absent,<br />which is the only indication that the end of results has been reached.<br /><br />:param catalog_name: str<br />  Name of parent catalog for tables of interest.<br />:param include_manifest_capabilities: bool (optional)<br />  Whether to include a manifest containing table capabilities in the response.<br />:param max_results: int (optional)<br />  Maximum number of summaries for tables to return. If not set, the page length is set to a server<br />  configured value (10000, as of 1/5/2024). - when set to a value greater than 0, the page length is<br />  the minimum of this value and a server configured value (10000, as of 1/5/2024); - when set to 0,<br />  the page length is set to a server configured value (10000, as of 1/5/2024) (recommended); - when<br />  set to a value less than 0, an invalid parameter error is returned;<br />:param page_token: str (optional)<br />  Opaque pagination token to go to next page based on previous query.<br />:param schema_name_pattern: str (optional)<br />  A sql LIKE pattern (% and _) for schema names. All schemas will be returned if not set or empty.<br />:param table_name_pattern: str (optional)<br />  A sql LIKE pattern (% and _) for table names. All tables will be returned if not set or empty.<br /><br />:returns: Iterator over :class:`TableSummary`

```sql
SELECT
full_name,
securable_kind_manifest,
table_type
FROM databricks_workspace.catalog.table_summaries
WHERE catalog_name = '{{ catalog_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_manifest_capabilities = '{{ include_manifest_capabilities }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND schema_name_pattern = '{{ schema_name_pattern }}'
AND table_name_pattern = '{{ table_name_pattern }}'
;
```
</TabItem>
</Tabs>

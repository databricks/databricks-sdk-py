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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>table_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="table_summaries" /></td></tr>
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
            "description": "Specifies when the option value is displayed on the UI within the OAuth flow. (BEFORE_ACCESS_TOKEN, BEFORE_AUTHORIZATION_CODE)"
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the option. (OPTION_BIGINT, OPTION_BOOLEAN, OPTION_ENUM, OPTION_MULTILINE_STRING, OPTION_NUMBER, OPTION_SERVICE_CREDENTIAL, OPTION_STRING)"
          }
        ]
      },
      {
        "name": "securable_kind",
        "type": "string",
        "description": "Securable kind to get manifest of. (TABLE_DB_STORAGE, TABLE_DELTA, TABLE_DELTASHARING, TABLE_DELTASHARING_MUTABLE, TABLE_DELTASHARING_OPEN_DIR_BASED, TABLE_DELTA_EXTERNAL, TABLE_DELTA_ICEBERG_DELTASHARING, TABLE_DELTA_ICEBERG_MANAGED, TABLE_DELTA_UNIFORM_HUDI_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_DELTASHARING, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_EXTERNAL, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_HIVE_METASTORE_MANAGED, TABLE_DELTA_UNIFORM_ICEBERG_FOREIGN_SNOWFLAKE, TABLE_EXTERNAL, TABLE_FEATURE_STORE, TABLE_FEATURE_STORE_EXTERNAL, TABLE_FOREIGN_BIGQUERY, TABLE_FOREIGN_DATABRICKS, TABLE_FOREIGN_DELTASHARING, TABLE_FOREIGN_HIVE_METASTORE, TABLE_FOREIGN_HIVE_METASTORE_DBFS_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_DBFS_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_DBFS_SHALLOW_CLONE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_DBFS_VIEW, TABLE_FOREIGN_HIVE_METASTORE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_EXTERNAL, TABLE_FOREIGN_HIVE_METASTORE_SHALLOW_CLONE_MANAGED, TABLE_FOREIGN_HIVE_METASTORE_VIEW, TABLE_FOREIGN_MONGODB, TABLE_FOREIGN_MYSQL, TABLE_FOREIGN_NETSUITE, TABLE_FOREIGN_ORACLE, TABLE_FOREIGN_POSTGRESQL, TABLE_FOREIGN_REDSHIFT, TABLE_FOREIGN_SALESFORCE, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING, TABLE_FOREIGN_SALESFORCE_DATA_CLOUD_FILE_SHARING_VIEW, TABLE_FOREIGN_SNOWFLAKE, TABLE_FOREIGN_SQLDW, TABLE_FOREIGN_SQLSERVER, TABLE_FOREIGN_TERADATA, TABLE_FOREIGN_WORKDAY_RAAS, TABLE_ICEBERG_UNIFORM_MANAGED, TABLE_INTERNAL, TABLE_MANAGED_POSTGRESQL, TABLE_MATERIALIZED_VIEW, TABLE_MATERIALIZED_VIEW_DELTASHARING, TABLE_METRIC_VIEW, TABLE_METRIC_VIEW_DELTASHARING, TABLE_ONLINE_VECTOR_INDEX_DIRECT, TABLE_ONLINE_VECTOR_INDEX_REPLICA, TABLE_ONLINE_VIEW, TABLE_STANDARD, TABLE_STREAMING_LIVE_TABLE, TABLE_STREAMING_LIVE_TABLE_DELTASHARING, TABLE_SYSTEM, TABLE_SYSTEM_DELTASHARING, TABLE_VIEW, TABLE_VIEW_DELTASHARING)"
      },
      {
        "name": "securable_type",
        "type": "string",
        "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
      }
    ]
  },
  {
    "name": "table_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXTERNAL, EXTERNAL_SHALLOW_CLONE, FOREIGN, MANAGED, MANAGED_SHALLOW_CLONE, MATERIALIZED_VIEW, METRIC_VIEW, STREAMING_TABLE, VIEW)"
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
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_manifest_capabilities"><code>include_manifest_capabilities</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-schema_name_pattern"><code>schema_name_pattern</code></a>, <a href="#parameter-table_name_pattern"><code>table_name_pattern</code></a></td>
    <td>Gets an array of summaries for tables for a schema and catalog within the metastore. The table</td>
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
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-include_manifest_capabilities">
    <td><CopyableCode code="include_manifest_capabilities" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include a manifest containing table capabilities in the response.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
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

Gets an array of summaries for tables for a schema and catalog within the metastore. The table

```sql
SELECT
full_name,
securable_kind_manifest,
table_type
FROM databricks_workspace.catalog.table_summaries
WHERE catalog_name = '{{ catalog_name }}' -- required
AND workspace = '{{ workspace }}' -- required
AND include_manifest_capabilities = '{{ include_manifest_capabilities }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
AND schema_name_pattern = '{{ schema_name_pattern }}'
AND table_name_pattern = '{{ table_name_pattern }}'
;
```
</TabItem>
</Tabs>

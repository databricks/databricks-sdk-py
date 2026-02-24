---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
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

Creates, updates, deletes, gets or lists a <code>functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="functions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.functions" /></td></tr>
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
    "description": "Name of function, relative to parent schema."
  },
  {
    "name": "function_id",
    "type": "string",
    "description": "Id of Function, relative to parent schema."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent Catalog."
  },
  {
    "name": "external_name",
    "type": "string",
    "description": "External function name."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of Function, in form of **catalog_name**.**schema_name**.**function_name**"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "Name of parent Schema relative to its parent Catalog."
  },
  {
    "name": "specific_name",
    "type": "string",
    "description": "Specific name of the function; Reserved for future use."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this function was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of function creator."
  },
  {
    "name": "data_type",
    "type": "string",
    "description": "Scalar function return data type. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
  },
  {
    "name": "external_language",
    "type": "string",
    "description": "External function language."
  },
  {
    "name": "full_data_type",
    "type": "string",
    "description": "Pretty printed function data type."
  },
  {
    "name": "input_params",
    "type": "object",
    "description": "Function input parameters.",
    "children": [
      {
        "name": "parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "type_text",
            "type": "string",
            "description": "Full data type spec, SQL/catalogString text."
          },
          {
            "name": "type_name",
            "type": "string",
            "description": "Name of type (INT, STRUCT, MAP, etc.) (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
          },
          {
            "name": "position",
            "type": "integer",
            "description": "Ordinal position of column (starting at position 0)."
          },
          {
            "name": "comment",
            "type": "string",
            "description": "User-provided free-form text description."
          },
          {
            "name": "parameter_default",
            "type": "string",
            "description": "Default value of the parameter."
          },
          {
            "name": "parameter_mode",
            "type": "string",
            "description": "Function parameter mode. (IN)"
          },
          {
            "name": "parameter_type",
            "type": "string",
            "description": "Function parameter type. (COLUMN, PARAM)"
          },
          {
            "name": "type_interval_type",
            "type": "string",
            "description": "Format of IntervalType."
          },
          {
            "name": "type_json",
            "type": "string",
            "description": "Full data type spec, JSON-serialized."
          },
          {
            "name": "type_precision",
            "type": "integer",
            "description": "Digits of precision; required on Create for DecimalTypes."
          },
          {
            "name": "type_scale",
            "type": "integer",
            "description": "Digits to right of decimal; Required on Create for DecimalTypes."
          }
        ]
      }
    ]
  },
  {
    "name": "is_deterministic",
    "type": "boolean",
    "description": "Whether the function is deterministic."
  },
  {
    "name": "is_null_call",
    "type": "boolean",
    "description": "Function null call."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of the function."
  },
  {
    "name": "parameter_style",
    "type": "string",
    "description": "Function parameter style. **S** is the value for SQL. (S)"
  },
  {
    "name": "properties",
    "type": "string",
    "description": "JSON-serialized key-value pair map, encoded (escaped) as a string."
  },
  {
    "name": "return_params",
    "type": "object",
    "description": "Table function return parameters.",
    "children": [
      {
        "name": "parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "type_text",
            "type": "string",
            "description": "Full data type spec, SQL/catalogString text."
          },
          {
            "name": "type_name",
            "type": "string",
            "description": "Name of type (INT, STRUCT, MAP, etc.) (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
          },
          {
            "name": "position",
            "type": "integer",
            "description": "Ordinal position of column (starting at position 0)."
          },
          {
            "name": "comment",
            "type": "string",
            "description": "User-provided free-form text description."
          },
          {
            "name": "parameter_default",
            "type": "string",
            "description": "Default value of the parameter."
          },
          {
            "name": "parameter_mode",
            "type": "string",
            "description": "Function parameter mode. (IN)"
          },
          {
            "name": "parameter_type",
            "type": "string",
            "description": "Function parameter type. (COLUMN, PARAM)"
          },
          {
            "name": "type_interval_type",
            "type": "string",
            "description": "Format of IntervalType."
          },
          {
            "name": "type_json",
            "type": "string",
            "description": "Full data type spec, JSON-serialized."
          },
          {
            "name": "type_precision",
            "type": "integer",
            "description": "Digits of precision; required on Create for DecimalTypes."
          },
          {
            "name": "type_scale",
            "type": "integer",
            "description": "Digits to right of decimal; Required on Create for DecimalTypes."
          }
        ]
      }
    ]
  },
  {
    "name": "routine_body",
    "type": "string",
    "description": "Function language. When **EXTERNAL** is used, the language of the routine function should be specified in the **external_language** field, and the **return_params** of the function cannot be used (as **TABLE** return type is not supported), and the **sql_data_access** field must be **NO_SQL**. (EXTERNAL, SQL)"
  },
  {
    "name": "routine_definition",
    "type": "string",
    "description": "Function body."
  },
  {
    "name": "routine_dependencies",
    "type": "object",
    "description": "function dependencies.",
    "children": [
      {
        "name": "dependencies",
        "type": "array",
        "description": "Array of dependencies.",
        "children": [
          {
            "name": "connection",
            "type": "object",
            "description": "A connection that is dependent on a SQL object.",
            "children": [
              {
                "name": "connection_name",
                "type": "string",
                "description": "Full name of the dependent connection, in the form of __connection_name__."
              }
            ]
          },
          {
            "name": "credential",
            "type": "object",
            "description": "A credential that is dependent on a SQL object.",
            "children": [
              {
                "name": "credential_name",
                "type": "string",
                "description": "Full name of the dependent credential, in the form of __credential_name__."
              }
            ]
          },
          {
            "name": "function",
            "type": "object",
            "description": "A function that is dependent on a SQL object.",
            "children": [
              {
                "name": "function_full_name",
                "type": "string",
                "description": "Full name of the dependent function, in the form of __catalog_name__.__schema_name__.__function_name__."
              }
            ]
          },
          {
            "name": "table",
            "type": "object",
            "description": "A table that is dependent on a SQL object.",
            "children": [
              {
                "name": "table_full_name",
                "type": "string",
                "description": "Full name of the dependent table, in the form of __catalog_name__.__schema_name__.__table_name__."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "security_type",
    "type": "string",
    "description": "Function security type. (DEFINER)"
  },
  {
    "name": "sql_data_access",
    "type": "string",
    "description": "Function SQL data access. (CONTAINS_SQL, NO_SQL, READS_SQL_DATA)"
  },
  {
    "name": "sql_path",
    "type": "string",
    "description": "List of schemes whose objects can be referenced without qualification."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this function was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the function."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of function, relative to parent schema."
  },
  {
    "name": "function_id",
    "type": "string",
    "description": "Id of Function, relative to parent schema."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of parent metastore."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent Catalog."
  },
  {
    "name": "external_name",
    "type": "string",
    "description": "External function name."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "Full name of Function, in form of **catalog_name**.**schema_name**.**function_name**"
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "Name of parent Schema relative to its parent Catalog."
  },
  {
    "name": "specific_name",
    "type": "string",
    "description": "Specific name of the function; Reserved for future use."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description."
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this function was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of function creator."
  },
  {
    "name": "data_type",
    "type": "string",
    "description": "Scalar function return data type. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
  },
  {
    "name": "external_language",
    "type": "string",
    "description": "External function language."
  },
  {
    "name": "full_data_type",
    "type": "string",
    "description": "Pretty printed function data type."
  },
  {
    "name": "input_params",
    "type": "object",
    "description": "Function input parameters.",
    "children": [
      {
        "name": "parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "type_text",
            "type": "string",
            "description": "Full data type spec, SQL/catalogString text."
          },
          {
            "name": "type_name",
            "type": "string",
            "description": "Name of type (INT, STRUCT, MAP, etc.) (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
          },
          {
            "name": "position",
            "type": "integer",
            "description": "Ordinal position of column (starting at position 0)."
          },
          {
            "name": "comment",
            "type": "string",
            "description": "User-provided free-form text description."
          },
          {
            "name": "parameter_default",
            "type": "string",
            "description": "Default value of the parameter."
          },
          {
            "name": "parameter_mode",
            "type": "string",
            "description": "Function parameter mode. (IN)"
          },
          {
            "name": "parameter_type",
            "type": "string",
            "description": "Function parameter type. (COLUMN, PARAM)"
          },
          {
            "name": "type_interval_type",
            "type": "string",
            "description": "Format of IntervalType."
          },
          {
            "name": "type_json",
            "type": "string",
            "description": "Full data type spec, JSON-serialized."
          },
          {
            "name": "type_precision",
            "type": "integer",
            "description": "Digits of precision; required on Create for DecimalTypes."
          },
          {
            "name": "type_scale",
            "type": "integer",
            "description": "Digits to right of decimal; Required on Create for DecimalTypes."
          }
        ]
      }
    ]
  },
  {
    "name": "is_deterministic",
    "type": "boolean",
    "description": "Whether the function is deterministic."
  },
  {
    "name": "is_null_call",
    "type": "boolean",
    "description": "Function null call."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of the function."
  },
  {
    "name": "parameter_style",
    "type": "string",
    "description": "Function parameter style. **S** is the value for SQL. (S)"
  },
  {
    "name": "properties",
    "type": "string",
    "description": "JSON-serialized key-value pair map, encoded (escaped) as a string."
  },
  {
    "name": "return_params",
    "type": "object",
    "description": "Table function return parameters.",
    "children": [
      {
        "name": "parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "type_text",
            "type": "string",
            "description": "Full data type spec, SQL/catalogString text."
          },
          {
            "name": "type_name",
            "type": "string",
            "description": "Name of type (INT, STRUCT, MAP, etc.) (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, GEOGRAPHY, GEOMETRY, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TABLE_TYPE, TIMESTAMP, TIMESTAMP_NTZ, USER_DEFINED_TYPE, VARIANT)"
          },
          {
            "name": "position",
            "type": "integer",
            "description": "Ordinal position of column (starting at position 0)."
          },
          {
            "name": "comment",
            "type": "string",
            "description": "User-provided free-form text description."
          },
          {
            "name": "parameter_default",
            "type": "string",
            "description": "Default value of the parameter."
          },
          {
            "name": "parameter_mode",
            "type": "string",
            "description": "Function parameter mode. (IN)"
          },
          {
            "name": "parameter_type",
            "type": "string",
            "description": "Function parameter type. (COLUMN, PARAM)"
          },
          {
            "name": "type_interval_type",
            "type": "string",
            "description": "Format of IntervalType."
          },
          {
            "name": "type_json",
            "type": "string",
            "description": "Full data type spec, JSON-serialized."
          },
          {
            "name": "type_precision",
            "type": "integer",
            "description": "Digits of precision; required on Create for DecimalTypes."
          },
          {
            "name": "type_scale",
            "type": "integer",
            "description": "Digits to right of decimal; Required on Create for DecimalTypes."
          }
        ]
      }
    ]
  },
  {
    "name": "routine_body",
    "type": "string",
    "description": "Function language. When **EXTERNAL** is used, the language of the routine function should be specified in the **external_language** field, and the **return_params** of the function cannot be used (as **TABLE** return type is not supported), and the **sql_data_access** field must be **NO_SQL**. (EXTERNAL, SQL)"
  },
  {
    "name": "routine_definition",
    "type": "string",
    "description": "Function body."
  },
  {
    "name": "routine_dependencies",
    "type": "object",
    "description": "function dependencies.",
    "children": [
      {
        "name": "dependencies",
        "type": "array",
        "description": "Array of dependencies.",
        "children": [
          {
            "name": "connection",
            "type": "object",
            "description": "A connection that is dependent on a SQL object.",
            "children": [
              {
                "name": "connection_name",
                "type": "string",
                "description": "Full name of the dependent connection, in the form of __connection_name__."
              }
            ]
          },
          {
            "name": "credential",
            "type": "object",
            "description": "A credential that is dependent on a SQL object.",
            "children": [
              {
                "name": "credential_name",
                "type": "string",
                "description": "Full name of the dependent credential, in the form of __credential_name__."
              }
            ]
          },
          {
            "name": "function",
            "type": "object",
            "description": "A function that is dependent on a SQL object.",
            "children": [
              {
                "name": "function_full_name",
                "type": "string",
                "description": "Full name of the dependent function, in the form of __catalog_name__.__schema_name__.__function_name__."
              }
            ]
          },
          {
            "name": "table",
            "type": "object",
            "description": "A table that is dependent on a SQL object.",
            "children": [
              {
                "name": "table_full_name",
                "type": "string",
                "description": "Full name of the dependent table, in the form of __catalog_name__.__schema_name__.__table_name__."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "security_type",
    "type": "string",
    "description": "Function security type. (DEFINER)"
  },
  {
    "name": "sql_data_access",
    "type": "string",
    "description": "Function SQL data access. (CONTAINS_SQL, NO_SQL, READS_SQL_DATA)"
  },
  {
    "name": "sql_path",
    "type": "string",
    "description": "List of schemes whose objects can be referenced without qualification."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this function was last modified, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the function."
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
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Gets a function from within a parent catalog and schema. For the fetch to succeed, the user must</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List functions within the specified parent catalog and schema. If the user is a metastore admin, all</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-function_info"><code>function_info</code></a></td>
    <td></td>
    <td>**WARNING: This API is experimental and will change in future versions**</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates the function that matches the supplied name. Only the owner of the function can be updated. If</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes the function that matches the supplied name. For the deletion to succeed, the user must</td>
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
    <td>Name of parent catalog for functions of interest.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The fully-qualified name of the function (of the form __catalog_name__.__schema_name__.__function__name__) .</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Parent schema of functions.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Force deletion even if the function is notempty.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include functions in the response for which the principal can only access selective metadata for</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of functions to return. If not set, all the functions are returned (not recommended). - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned;</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
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

Gets a function from within a parent catalog and schema. For the fetch to succeed, the user must

```sql
SELECT
name,
function_id,
metastore_id,
catalog_name,
external_name,
full_name,
schema_name,
specific_name,
browse_only,
comment,
created_at,
created_by,
data_type,
external_language,
full_data_type,
input_params,
is_deterministic,
is_null_call,
owner,
parameter_style,
properties,
return_params,
routine_body,
routine_definition,
routine_dependencies,
security_type,
sql_data_access,
sql_path,
updated_at,
updated_by
FROM databricks_workspace.catalog.functions
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

List functions within the specified parent catalog and schema. If the user is a metastore admin, all

```sql
SELECT
name,
function_id,
metastore_id,
catalog_name,
external_name,
full_name,
schema_name,
specific_name,
browse_only,
comment,
created_at,
created_by,
data_type,
external_language,
full_data_type,
input_params,
is_deterministic,
is_null_call,
owner,
parameter_style,
properties,
return_params,
routine_body,
routine_definition,
routine_dependencies,
security_type,
sql_data_access,
sql_path,
updated_at,
updated_by
FROM databricks_workspace.catalog.functions
WHERE catalog_name = '{{ catalog_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND workspace = '{{ workspace }}' -- required
AND include_browse = '{{ include_browse }}'
AND max_results = '{{ max_results }}'
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

**WARNING: This API is experimental and will change in future versions**

```sql
INSERT INTO databricks_workspace.catalog.functions (
function_info,
workspace
)
SELECT 
'{{ function_info }}' /* required */,
'{{ workspace }}'
RETURNING
name,
function_id,
metastore_id,
catalog_name,
external_name,
full_name,
schema_name,
specific_name,
browse_only,
comment,
created_at,
created_by,
data_type,
external_language,
full_data_type,
input_params,
is_deterministic,
is_null_call,
owner,
parameter_style,
properties,
return_params,
routine_body,
routine_definition,
routine_dependencies,
security_type,
sql_data_access,
sql_path,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: functions
  props:
    - name: workspace
      value: string
      description: Required parameter for the functions resource.
    - name: function_info
      value: object
      description: |
        Partial __FunctionInfo__ specifying the function to be created.
      props:
      - name: name
        value: string
      - name: catalog_name
        value: string
        description: |
          Name of parent Catalog.
      - name: schema_name
        value: string
        description: |
          Name of parent Schema relative to its parent Catalog.
      - name: input_params
        value: object
        description: |
          Function input parameters.
        props:
        - name: parameters
          value: array
          props:
          - name: name
            value: string
          - name: type_text
            value: string
            description: |
              Full data type spec, SQL/catalogString text.
          - name: type_name
            value: string
            description: |
              Name of type (INT, STRUCT, MAP, etc.)
          - name: position
            value: integer
            description: |
              Ordinal position of column (starting at position 0).
          - name: comment
            value: string
            description: |
              User-provided free-form text description.
          - name: parameter_default
            value: string
            description: |
              Default value of the parameter.
          - name: parameter_mode
            value: string
            description: |
              Function parameter mode.
          - name: parameter_type
            value: string
            description: |
              Function parameter type.
          - name: type_interval_type
            value: string
            description: |
              Format of IntervalType.
          - name: type_json
            value: string
            description: |
              Full data type spec, JSON-serialized.
          - name: type_precision
            value: integer
            description: |
              Digits of precision; required on Create for DecimalTypes.
          - name: type_scale
            value: integer
            description: |
              Digits to right of decimal; Required on Create for DecimalTypes.
      - name: data_type
        value: string
        description: |
          Scalar function return data type.
      - name: full_data_type
        value: string
        description: |
          Pretty printed function data type.
      - name: routine_body
        value: string
        description: |
          Function language. When **EXTERNAL** is used, the language of the routine function should be specified in the **external_language** field, and the **return_params** of the function cannot be used (as **TABLE** return type is not supported), and the **sql_data_access** field must be **NO_SQL**.
      - name: routine_definition
        value: string
        description: |
          Function body.
      - name: parameter_style
        value: string
        description: |
          Function parameter style. **S** is the value for SQL.
      - name: is_deterministic
        value: boolean
        description: |
          Whether the function is deterministic.
      - name: sql_data_access
        value: string
        description: |
          Function SQL data access.
      - name: is_null_call
        value: boolean
        description: |
          Function null call.
      - name: security_type
        value: string
        description: |
          Function security type.
      - name: specific_name
        value: string
        description: |
          Specific name of the function; Reserved for future use.
      - name: comment
        value: string
        description: |
          User-provided free-form text description.
      - name: external_language
        value: string
        description: |
          External function language.
      - name: external_name
        value: string
        description: |
          External function name.
      - name: properties
        value: string
        description: |
          JSON-serialized key-value pair map, encoded (escaped) as a string.
      - name: return_params
        value: object
        description: |
          Table function return parameters.
        props:
        - name: parameters
          value: array
          props:
          - name: name
            value: string
          - name: type_text
            value: string
            description: |
              Full data type spec, SQL/catalogString text.
          - name: type_name
            value: string
            description: |
              Name of type (INT, STRUCT, MAP, etc.)
          - name: position
            value: integer
            description: |
              Ordinal position of column (starting at position 0).
          - name: comment
            value: string
            description: |
              User-provided free-form text description.
          - name: parameter_default
            value: string
            description: |
              Default value of the parameter.
          - name: parameter_mode
            value: string
            description: |
              Function parameter mode.
          - name: parameter_type
            value: string
            description: |
              Function parameter type.
          - name: type_interval_type
            value: string
            description: |
              Format of IntervalType.
          - name: type_json
            value: string
            description: |
              Full data type spec, JSON-serialized.
          - name: type_precision
            value: integer
            description: |
              Digits of precision; required on Create for DecimalTypes.
          - name: type_scale
            value: integer
            description: |
              Digits to right of decimal; Required on Create for DecimalTypes.
      - name: routine_dependencies
        value: object
        description: |
          function dependencies.
        props:
        - name: dependencies
          value: array
          description: |
            Array of dependencies.
          props:
          - name: connection
            value: object
            description: |
              A connection that is dependent on a SQL object.
            props:
            - name: connection_name
              value: string
              description: |
                Full name of the dependent connection, in the form of __connection_name__.
          - name: credential
            value: object
            description: |
              A credential that is dependent on a SQL object.
            props:
            - name: credential_name
              value: string
              description: |
                Full name of the dependent credential, in the form of __credential_name__.
          - name: function
            value: object
            description: |
              A function that is dependent on a SQL object.
            props:
            - name: function_full_name
              value: string
              description: |
                Full name of the dependent function, in the form of __catalog_name__.__schema_name__.__function_name__.
          - name: table
            value: object
            description: |
              A table that is dependent on a SQL object.
            props:
            - name: table_full_name
              value: string
              description: |
                Full name of the dependent table, in the form of __catalog_name__.__schema_name__.__table_name__.
      - name: sql_path
        value: string
        description: |
          List of schemes whose objects can be referenced without qualification.
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

Updates the function that matches the supplied name. Only the owner of the function can be updated. If

```sql
UPDATE databricks_workspace.catalog.functions
SET 
owner = '{{ owner }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
name,
function_id,
metastore_id,
catalog_name,
external_name,
full_name,
schema_name,
specific_name,
browse_only,
comment,
created_at,
created_by,
data_type,
external_language,
full_data_type,
input_params,
is_deterministic,
is_null_call,
owner,
parameter_style,
properties,
return_params,
routine_body,
routine_definition,
routine_dependencies,
security_type,
sql_data_access,
sql_path,
updated_at,
updated_by;
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

Deletes the function that matches the supplied name. For the deletion to succeed, the user must

```sql
DELETE FROM databricks_workspace.catalog.functions
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>

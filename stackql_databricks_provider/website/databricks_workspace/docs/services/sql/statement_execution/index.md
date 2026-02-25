---
title: statement_execution
hide_title: false
hide_table_of_contents: false
keywords:
  - statement_execution
  - sql
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

Creates, updates, deletes, gets or lists a <code>statement_execution</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="statement_execution" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.statement_execution" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_result_chunk"
    values={[
        { label: 'get_result_chunk', value: 'get_result_chunk' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_result_chunk">

<SchemaTable fields={[
  {
    "name": "byte_count",
    "type": "integer",
    "description": "The number of bytes in the result chunk. This field is not available when using `INLINE` disposition."
  },
  {
    "name": "chunk_index",
    "type": "integer",
    "description": "The position within the sequence of result set chunks."
  },
  {
    "name": "data_array",
    "type": "array",
    "description": "The `JSON_ARRAY` format is an array of arrays of values, where each non-null value is formatted as a string. Null values are encoded as JSON `null`."
  },
  {
    "name": "external_links",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "byte_count",
        "type": "integer",
        "description": ""
      },
      {
        "name": "chunk_index",
        "type": "integer",
        "description": "The position within the sequence of result set chunks."
      },
      {
        "name": "expiration",
        "type": "string",
        "description": "Indicates the date-time that the given external link will expire and becomes invalid, after which point a new `external_link` must be requested."
      },
      {
        "name": "external_link",
        "type": "string",
        "description": "A URL pointing to a chunk of result data, hosted by an external service, with a short expiration time (&lt;= 15 minutes). As this URL contains a temporary credential, it should be considered sensitive and the client should not expose this URL in a log."
      },
      {
        "name": "http_headers",
        "type": "object",
        "description": "HTTP headers that must be included with a GET request to the `external_link`. Each header is provided as a key-value pair. Headers are typically used to pass a decryption key to the external service. The values of these headers should be considered sensitive and the client should not expose these values in a log."
      },
      {
        "name": "next_chunk_index",
        "type": "integer",
        "description": "When fetching, provides the `chunk_index` for the _next_ chunk. If absent, indicates there are no more chunks. The next chunk can be fetched with a :method:statementexecution/getstatementresultchunkn request."
      },
      {
        "name": "next_chunk_internal_link",
        "type": "string",
        "description": "When fetching, provides a link to fetch the _next_ chunk. If absent, indicates there are no more chunks. This link is an absolute `path` to be joined with your `$DATABRICKS_HOST`, and should be treated as an opaque link. This is an alternative to using `next_chunk_index`."
      },
      {
        "name": "row_count",
        "type": "integer",
        "description": "The number of rows within the result chunk."
      },
      {
        "name": "row_offset",
        "type": "integer",
        "description": "The starting row offset within the result set."
      }
    ]
  },
  {
    "name": "next_chunk_index",
    "type": "integer",
    "description": "When fetching, provides the `chunk_index` for the _next_ chunk. If absent, indicates there are no more chunks. The next chunk can be fetched with a :method:statementexecution/getstatementresultchunkn request."
  },
  {
    "name": "next_chunk_internal_link",
    "type": "string",
    "description": "When fetching, provides a link to fetch the _next_ chunk. If absent, indicates there are no more chunks. This link is an absolute `path` to be joined with your `$DATABRICKS_HOST`, and should be treated as an opaque link. This is an alternative to using `next_chunk_index`."
  },
  {
    "name": "row_count",
    "type": "integer",
    "description": "The number of rows within the result chunk."
  },
  {
    "name": "row_offset",
    "type": "integer",
    "description": "The starting row offset within the result set."
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "statement_id",
    "type": "string",
    "description": "The statement ID is returned upon successfully submitting a SQL statement, and is a required reference for all subsequent calls."
  },
  {
    "name": "manifest",
    "type": "object",
    "description": "The result manifest provides schema and metadata for the result set.",
    "children": [
      {
        "name": "chunks",
        "type": "array",
        "description": "Array of result set chunk metadata.",
        "children": [
          {
            "name": "byte_count",
            "type": "integer",
            "description": ""
          },
          {
            "name": "chunk_index",
            "type": "integer",
            "description": "The position within the sequence of result set chunks."
          },
          {
            "name": "row_count",
            "type": "integer",
            "description": "The number of rows within the result chunk."
          },
          {
            "name": "row_offset",
            "type": "integer",
            "description": "The starting row offset within the result set."
          }
        ]
      },
      {
        "name": "format",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ARROW_STREAM, CSV, JSON_ARRAY)"
      },
      {
        "name": "schema",
        "type": "object",
        "description": "The schema is an ordered list of column descriptions.",
        "children": [
          {
            "name": "column_count",
            "type": "integer",
            "description": ""
          },
          {
            "name": "columns",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "position",
                "type": "integer",
                "description": "The ordinal position of the column (starting at position 0)."
              },
              {
                "name": "type_interval_type",
                "type": "string",
                "description": "The format of the interval type."
              },
              {
                "name": "type_name",
                "type": "string",
                "description": "The name of the base data type. This doesn't include details for complex types such as STRUCT, MAP or ARRAY. (ARRAY, BINARY, BOOLEAN, BYTE, CHAR, DATE, DECIMAL, DOUBLE, FLOAT, INT, INTERVAL, LONG, MAP, NULL, SHORT, STRING, STRUCT, TIMESTAMP, USER_DEFINED_TYPE)"
              },
              {
                "name": "type_precision",
                "type": "integer",
                "description": "Specifies the number of digits in a number. This applies to the DECIMAL type."
              },
              {
                "name": "type_scale",
                "type": "integer",
                "description": "Specifies the number of digits to the right of the decimal point in a number. This applies to the DECIMAL type."
              },
              {
                "name": "type_text",
                "type": "string",
                "description": "The full SQL type specification."
              }
            ]
          }
        ]
      },
      {
        "name": "total_byte_count",
        "type": "integer",
        "description": "The total number of bytes in the result set. This field is not available when using `INLINE` disposition."
      },
      {
        "name": "total_chunk_count",
        "type": "integer",
        "description": "The total number of chunks that the result set has been divided into."
      },
      {
        "name": "total_row_count",
        "type": "integer",
        "description": "The total number of rows in the result set."
      },
      {
        "name": "truncated",
        "type": "boolean",
        "description": "Indicates whether the result is truncated due to `row_limit` or `byte_limit`."
      }
    ]
  },
  {
    "name": "result",
    "type": "object",
    "description": "Contains the result data of a single chunk when using `INLINE` disposition. When using<br />    `EXTERNAL_LINKS` disposition, the array `external_links` is used instead to provide URLs to the<br />    result data in cloud storage. Exactly one of these alternatives is used. (While the<br />    `external_links` array prepares the API to return multiple links in a single response. Currently<br />    only a single link is returned.)",
    "children": [
      {
        "name": "byte_count",
        "type": "integer",
        "description": "The number of bytes in the result chunk. This field is not available when using `INLINE` disposition."
      },
      {
        "name": "chunk_index",
        "type": "integer",
        "description": "The position within the sequence of result set chunks."
      },
      {
        "name": "data_array",
        "type": "array",
        "description": "The `JSON_ARRAY` format is an array of arrays of values, where each non-null value is formatted as a string. Null values are encoded as JSON `null`."
      },
      {
        "name": "external_links",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "byte_count",
            "type": "integer",
            "description": ""
          },
          {
            "name": "chunk_index",
            "type": "integer",
            "description": "The position within the sequence of result set chunks."
          },
          {
            "name": "expiration",
            "type": "string",
            "description": "Indicates the date-time that the given external link will expire and becomes invalid, after which point a new `external_link` must be requested."
          },
          {
            "name": "external_link",
            "type": "string",
            "description": "A URL pointing to a chunk of result data, hosted by an external service, with a short expiration time (&lt;= 15 minutes). As this URL contains a temporary credential, it should be considered sensitive and the client should not expose this URL in a log."
          },
          {
            "name": "http_headers",
            "type": "object",
            "description": "HTTP headers that must be included with a GET request to the `external_link`. Each header is provided as a key-value pair. Headers are typically used to pass a decryption key to the external service. The values of these headers should be considered sensitive and the client should not expose these values in a log."
          },
          {
            "name": "next_chunk_index",
            "type": "integer",
            "description": "When fetching, provides the `chunk_index` for the _next_ chunk. If absent, indicates there are no more chunks. The next chunk can be fetched with a :method:statementexecution/getstatementresultchunkn request."
          },
          {
            "name": "next_chunk_internal_link",
            "type": "string",
            "description": "When fetching, provides a link to fetch the _next_ chunk. If absent, indicates there are no more chunks. This link is an absolute `path` to be joined with your `$DATABRICKS_HOST`, and should be treated as an opaque link. This is an alternative to using `next_chunk_index`."
          },
          {
            "name": "row_count",
            "type": "integer",
            "description": "The number of rows within the result chunk."
          },
          {
            "name": "row_offset",
            "type": "integer",
            "description": "The starting row offset within the result set."
          }
        ]
      },
      {
        "name": "next_chunk_index",
        "type": "integer",
        "description": "When fetching, provides the `chunk_index` for the _next_ chunk. If absent, indicates there are no more chunks. The next chunk can be fetched with a :method:statementexecution/getstatementresultchunkn request."
      },
      {
        "name": "next_chunk_internal_link",
        "type": "string",
        "description": "When fetching, provides a link to fetch the _next_ chunk. If absent, indicates there are no more chunks. This link is an absolute `path` to be joined with your `$DATABRICKS_HOST`, and should be treated as an opaque link. This is an alternative to using `next_chunk_index`."
      },
      {
        "name": "row_count",
        "type": "integer",
        "description": "The number of rows within the result chunk."
      },
      {
        "name": "row_offset",
        "type": "integer",
        "description": "The starting row offset within the result set."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The status response includes execution state and if relevant, error information.",
    "children": [
      {
        "name": "error",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "error_code",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ABORTED, ALREADY_EXISTS, BAD_REQUEST, CANCELLED, DEADLINE_EXCEEDED, INTERNAL_ERROR, IO_ERROR, NOT_FOUND, RESOURCE_EXHAUSTED, SERVICE_UNDER_MAINTENANCE, TEMPORARILY_UNAVAILABLE, UNAUTHENTICATED, UNKNOWN, WORKSPACE_TEMPORARILY_UNAVAILABLE)"
          },
          {
            "name": "message",
            "type": "string",
            "description": "A brief summary of the error condition."
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "Statement execution state: - `PENDING`: waiting for warehouse - `RUNNING`: running - `SUCCEEDED`: execution was successful, result data available for fetch - `FAILED`: execution failed; reason for failure described in accompanying error message - `CANCELED`: user canceled; can come from explicit cancel call, or timeout with `on_wait_timeout=CANCEL` - `CLOSED`: execution successful, and statement closed; result no longer available for fetch (CANCELED, CLOSED, FAILED, PENDING, RUNNING, SUCCEEDED)"
      }
    ]
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
    <td><a href="#get_result_chunk"><CopyableCode code="get_result_chunk" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-chunk_index"><code>chunk_index</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>After the statement execution has `SUCCEEDED`, this request can be used to fetch any chunk by index.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>This request can be used to poll for the statement's status. StatementResponse contains `statement_id`</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Requests that an executing statement be canceled. Callers must poll for status to see the terminal</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-statement"><code>statement</code></a>, <a href="#parameter-warehouse_id"><code>warehouse_id</code></a></td>
    <td></td>
    <td>Execute a SQL statement and optionally await its results for a specified time.</td>
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
<tr id="parameter-chunk_index">
    <td><CopyableCode code="chunk_index" /></td>
    <td><code>integer</code></td>
    <td>:returns: :class:`ResultData`</td>
</tr>
<tr id="parameter-statement_id">
    <td><CopyableCode code="statement_id" /></td>
    <td><code>string</code></td>
    <td>The statement ID is returned upon successfully submitting a SQL statement, and is a required reference for all subsequent calls.</td>
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
    defaultValue="get_result_chunk"
    values={[
        { label: 'get_result_chunk', value: 'get_result_chunk' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_result_chunk">

After the statement execution has `SUCCEEDED`, this request can be used to fetch any chunk by index.

```sql
SELECT
byte_count,
chunk_index,
data_array,
external_links,
next_chunk_index,
next_chunk_internal_link,
row_count,
row_offset
FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '{{ statement_id }}' -- required
AND chunk_index = '{{ chunk_index }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="get">

This request can be used to poll for the statement's status. StatementResponse contains `statement_id`

```sql
SELECT
statement_id,
manifest,
result,
status
FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '{{ statement_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'execute', value: 'execute' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="cancel">

Requests that an executing statement be canceled. Callers must poll for status to see the terminal

```sql
INSERT INTO databricks_workspace.sql.statement_execution (
statement_id,
workspace
)
SELECT 
'{{ statement_id }}',
'{{ workspace }}'
;
```
</TabItem>
<TabItem value="execute">

Execute a SQL statement and optionally await its results for a specified time.

```sql
INSERT INTO databricks_workspace.sql.statement_execution (
statement,
warehouse_id,
byte_limit,
catalog,
disposition,
format,
on_wait_timeout,
parameters,
query_tags,
row_limit,
schema,
wait_timeout,
workspace
)
SELECT 
'{{ statement }}' /* required */,
'{{ warehouse_id }}' /* required */,
{{ byte_limit }},
'{{ catalog }}',
'{{ disposition }}',
'{{ format }}',
'{{ on_wait_timeout }}',
'{{ parameters }}',
'{{ query_tags }}',
{{ row_limit }},
'{{ schema }}',
'{{ wait_timeout }}',
'{{ workspace }}'
RETURNING
statement_id,
manifest,
result,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: statement_execution
  props:
    - name: statement_id
      value: "{{ statement_id }}"
      description: Required parameter for the statement_execution resource.
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the statement_execution resource.
    - name: statement
      value: "{{ statement }}"
      description: |
        The SQL statement to execute. The statement can optionally be parameterized, see \`parameters\`. The maximum query text size is 16 MiB.
    - name: warehouse_id
      value: "{{ warehouse_id }}"
      description: |
        Warehouse upon which to execute a statement. See also [What are SQL warehouses?] [What are SQL warehouses?]: https://docs.databricks.com/sql/admin/warehouse-type.html
    - name: byte_limit
      value: {{ byte_limit }}
      description: |
        Applies the given byte limit to the statement's result size. Byte counts are based on internal data representations and might not match the final size in the requested \`format\`. If the result was truncated due to the byte limit, then \`truncated\` in the response is set to \`true\`. When using \`EXTERNAL_LINKS\` disposition, a default \`byte_limit\` of 100 GiB is applied if \`byte_limit\` is not explicitly set.
    - name: catalog
      value: "{{ catalog }}"
      description: |
        Sets default catalog for statement execution, similar to [\`USE CATALOG\`] in SQL. [\`USE CATALOG\`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html
    - name: disposition
      value: "{{ disposition }}"
      description: |
        The fetch disposition provides two modes of fetching results: \`INLINE\` and \`EXTERNAL_LINKS\`. Statements executed with \`INLINE\` disposition will return result data inline, in \`JSON_ARRAY\` format, in a series of chunks. If a given statement produces a result set with a size larger than 25 MiB, that statement execution is aborted, and no result set will be available. **NOTE** Byte limits are computed based upon internal representations of the result set data, and might not match the sizes visible in JSON responses. Statements executed with \`EXTERNAL_LINKS\` disposition will return result data as external links: URLs that point to cloud storage internal to the workspace. Using \`EXTERNAL_LINKS\` disposition allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The resulting links have two important properties: 1. They point to resources _external_ to the Databricks compute; therefore any associated authentication information (typically a personal access token, OAuth token, or similar) _must be removed_ when fetching from these links. 2. These are URLs with a specific expiration, indicated in the response. The behavior when attempting to use an expired link is cloud specific.
    - name: format
      value: "{{ format }}"
      description: |
        Statement execution supports three result formats: \`JSON_ARRAY\` (default), \`ARROW_STREAM\`, and \`CSV\`. Important: The formats \`ARROW_STREAM\` and \`CSV\` are supported only with \`EXTERNAL_LINKS\` disposition. \`JSON_ARRAY\` is supported in \`INLINE\` and \`EXTERNAL_LINKS\` disposition. When specifying \`format=JSON_ARRAY\`, result data will be formatted as an array of arrays of values, where each value is either the *string representation* of a value, or \`null\`. For example, the output of \`SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)\` would look like this: \`\`\` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] \`\`\` When specifying \`format=JSON_ARRAY\` and \`disposition=EXTERNAL_LINKS\`, each chunk in the result contains compact JSON with no indentation or extra whitespace. When specifying \`format=ARROW_STREAM\` and \`disposition=EXTERNAL_LINKS\`, each chunk in the result will be formatted as Apache Arrow Stream. See the [Apache Arrow streaming format]. When specifying \`format=CSV\` and \`disposition=EXTERNAL_LINKS\`, each chunk in the result will be a CSV according to [RFC 4180] standard. All the columns values will have *string representation* similar to the \`JSON_ARRAY\` format, and \`null\` values will be encoded as “null”. Only the first chunk in the result would contain a header row with column names. For example, the output of \`SELECT concat('id-', id) AS strCol, id AS intCol, null as nullCol FROM range(3)\` would look like this: \`\`\` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null \`\`\` [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180
    - name: on_wait_timeout
      value: "{{ on_wait_timeout }}"
      description: |
        When \`wait_timeout > 0s\`, the call will block up to the specified time. If the statement execution doesn't finish within this time, \`on_wait_timeout\` determines whether the execution should continue or be canceled. When set to \`CONTINUE\`, the statement execution continues asynchronously and the call returns a statement ID which can be used for polling with :method:statementexecution/getStatement. When set to \`CANCEL\`, the statement execution is canceled and the call returns with a \`CANCELED\` state.
    - name: parameters
      description: |
        A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists of a name, a value, and optionally a type. To represent a NULL value, the \`value\` field may be omitted or set to \`null\` explicitly. If the \`type\` field is omitted, the value is interpreted as a string. If the type is given, parameters will be checked for type correctness according to the given type. A value is correct if the provided string can be converted to the requested type using the \`cast\` function. The exact semantics are described in the section [\`cast\` function] of the SQL language reference. For example, the following statement contains two parameters, \`my_name\` and \`my_date\`: \`\`\` SELECT * FROM my_table WHERE name = :my_name AND date = :my_date \`\`\` The parameters can be passed in the request body as follows: \` { ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date", "parameters": [ { "name": "my_name", "value": "the name" }, { "name": "my_date", "value": "2020-01-01", "type": "DATE" } ] } \` Currently, positional parameters denoted by a \`?\` marker are not supported by the Databricks SQL Statement Execution API. Also see the section [Parameter markers] of the SQL language reference. [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html [\`cast\` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html
      value:
        - name: "{{ name }}"
          type: "{{ type }}"
          value: "{{ value }}"
    - name: query_tags
      description: |
        An array of query tags to annotate a SQL statement. A query tag consists of a non-empty key and, optionally, a value. To represent a NULL value, either omit the \`value\` field or manually set it to \`null\` or white space. Refer to the SQL language reference for the format specification of query tags. There's no significance to the order of tags. Only one value per key will be recorded. A sequence in excess of 20 query tags will be coerced to 20. Example: { ..., "query_tags": [ { "key": "team", "value": "eng" }, { "key": "some key only tag" } ] }
      value:
        - key: "{{ key }}"
          value: "{{ value }}"
    - name: row_limit
      value: {{ row_limit }}
      description: |
        Applies the given row limit to the statement's result set, but unlike the \`LIMIT\` clause in SQL, it also sets the \`truncated\` field in the response to indicate whether the result was trimmed due to the limit or not.
    - name: schema
      value: "{{ schema }}"
      description: |
        Sets default schema for statement execution, similar to [\`USE SCHEMA\`] in SQL. [\`USE SCHEMA\`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html
    - name: wait_timeout
      value: "{{ wait_timeout }}"
      description: |
        The time in seconds the call will wait for the statement's result set as \`Ns\`, where \`N\` can be set to 0 or to a value between 5 and 50. When set to \`0s\`, the statement will execute in asynchronous mode and the call will not wait for the execution to finish. In this case, the call returns directly with \`PENDING\` state and a statement ID which can be used for polling with :method:statementexecution/getStatement. When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait for the statement execution to finish. If the execution finishes within this time, the call returns immediately with a manifest and result data (or a \`FAILED\` state in case of an execution error). If the statement takes longer to execute, \`on_wait_timeout\` determines what should happen after the timeout is reached.
`}</CodeBlock>

</TabItem>
</Tabs>

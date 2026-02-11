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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>statement_execution</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_execution</code></td></tr>
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
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
                "description": "The name of the base data type. This doesn't include details for complex types such as STRUCT, MAP or ARRAY."
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
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
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
        "description": "Statement execution state: - `PENDING`: waiting for warehouse - `RUNNING`: running - `SUCCEEDED`: execution was successful, result data available for fetch - `FAILED`: execution failed; reason for failure described in accompanying error message - `CANCELED`: user canceled; can come from explicit cancel call, or timeout with `on_wait_timeout=CANCEL` - `CLOSED`: execution successful, and statement closed; result no longer available for fetch"
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
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-chunk_index"><code>chunk_index</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>After the statement execution has `SUCCEEDED`, this request can be used to fetch any chunk by index.<br />Whereas the first chunk with `chunk_index=0` is typically fetched with<br />:method:statementexecution/executeStatement or :method:statementexecution/getStatement, this request<br />can be used to fetch subsequent chunks. The response structure is identical to the nested `result`<br />element described in the :method:statementexecution/getStatement request, and similarly includes the<br />`next_chunk_index` and `next_chunk_internal_link` fields for simple iteration through the result set.<br />Depending on `disposition`, the response returns chunks of data either inline, or as links.<br /><br />:param statement_id: str<br />  The statement ID is returned upon successfully submitting a SQL statement, and is a required<br />  reference for all subsequent calls.<br />:param chunk_index: int<br /><br />:returns: :class:`ResultData`</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This request can be used to poll for the statement's status. StatementResponse contains `statement_id`<br />and `status`; other fields might be absent or present depending on context. When the `status.state`<br />field is `SUCCEEDED` it will also return the result manifest and the first chunk of the result data.<br />When the statement is in the terminal states `CANCELED`, `CLOSED` or `FAILED`, it returns HTTP 200<br />with the state set. After at least 12 hours in terminal state, the statement is removed from the<br />warehouse and further calls will receive an HTTP 404 response.<br /><br />**NOTE** This call currently might take up to 5 seconds to get the latest status and result.<br /><br />:param statement_id: str<br />  The statement ID is returned upon successfully submitting a SQL statement, and is a required<br />  reference for all subsequent calls.<br /><br />:returns: :class:`StatementResponse`</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Requests that an executing statement be canceled. Callers must poll for status to see the terminal<br />state. Cancel response is empty; receiving response indicates successful receipt.<br /><br />:param statement_id: str<br />  The statement ID is returned upon successfully submitting a SQL statement, and is a required<br />  reference for all subsequent calls.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__statement"><code>data__statement</code></a>, <a href="#parameter-data__warehouse_id"><code>data__warehouse_id</code></a></td>
    <td></td>
    <td>Execute a SQL statement and optionally await its results for a specified time.<br /><br />**Use case: small result sets with INLINE + JSON_ARRAY**<br /><br />For flows that generate small and predictable result sets (&lt;= 25 MiB), `INLINE` responses of<br />`JSON_ARRAY` result data are typically the simplest way to execute and fetch result data.<br /><br />**Use case: large result sets with EXTERNAL_LINKS**<br /><br />Using `EXTERNAL_LINKS` to fetch result data allows you to fetch large result sets efficiently. The<br />main differences from using `INLINE` disposition are that the result data is accessed with URLs, and<br />that there are 3 supported formats: `JSON_ARRAY`, `ARROW_STREAM` and `CSV` compared to only<br />`JSON_ARRAY` with `INLINE`.<br /><br />** URLs**<br /><br />External links point to data stored within your workspace's internal storage, in the form of a URL.<br />The URLs are valid for only a short period, &lt;= 15 minutes. Alongside each `external_link` is an<br />expiration field indicating the time at which the URL is no longer valid. In `EXTERNAL_LINKS` mode,<br />chunks can be resolved and fetched multiple times and in parallel.<br /><br />----<br /><br />### **Warning: Databricks strongly recommends that you protect the URLs that are returned by the<br />`EXTERNAL_LINKS` disposition.**<br /><br />When you use the `EXTERNAL_LINKS` disposition, a short-lived, URL is generated, which can be used to<br />download the results directly from . As a short-lived is embedded in this URL, you should protect the<br />URL.<br /><br />Because URLs are already generated with embedded temporary s, you must not set an `Authorization`<br />header in the download requests.<br /><br />The `EXTERNAL_LINKS` disposition can be disabled upon request by creating a support case.<br /><br />See also [Security best practices].<br /><br />----<br /><br />StatementResponse contains `statement_id` and `status`; other fields might be absent or present<br />depending on context. If the SQL warehouse fails to execute the provided statement, a 200 response is<br />returned with `status.state` set to `FAILED` (in contrast to a failure when accepting the request,<br />which results in a non-200 response). Details of the error can be found at `status.error` in case of<br />execution failures.<br /><br />[Security best practices]: https://docs.databricks.com/sql/admin/sql-execution-tutorial.html#security-best-practices<br /><br />:param statement: str<br />  The SQL statement to execute. The statement can optionally be parameterized, see `parameters`. The<br />  maximum query text size is 16 MiB.<br />:param warehouse_id: str<br />  Warehouse upon which to execute a statement. See also [What are SQL warehouses?]<br /><br />  [What are SQL warehouses?]: https://docs.databricks.com/sql/admin/warehouse-type.html<br />:param byte_limit: int (optional)<br />  Applies the given byte limit to the statement's result size. Byte counts are based on internal data<br />  representations and might not match the final size in the requested `format`. If the result was<br />  truncated due to the byte limit, then `truncated` in the response is set to `true`. When using<br />  `EXTERNAL_LINKS` disposition, a default `byte_limit` of 100 GiB is applied if `byte_limit` is not<br />  explicitly set.<br />:param catalog: str (optional)<br />  Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL.<br /><br />  [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html<br />:param disposition: :class:`Disposition` (optional)<br />  The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.<br /><br />  Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`<br />  format, in a series of chunks. If a given statement produces a result set with a size larger than 25<br />  MiB, that statement execution is aborted, and no result set will be available.<br /><br />  **NOTE** Byte limits are computed based upon internal representations of the result set data, and<br />  might not match the sizes visible in JSON responses.<br /><br />  Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links:<br />  URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition<br />  allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The<br />  resulting links have two important properties:<br /><br />  1. They point to resources _external_ to the Databricks compute; therefore any associated<br />  authentication information (typically a personal access token, OAuth token, or similar) _must be<br />  removed_ when fetching from these links.<br /><br />  2. These are URLs with a specific expiration, indicated in the response. The behavior when<br />  attempting to use an expired link is cloud specific.<br />:param format: :class:`Format` (optional)<br />  Statement execution supports three result formats: `JSON_ARRAY` (default), `ARROW_STREAM`, and<br />  `CSV`.<br /><br />  Important: The formats `ARROW_STREAM` and `CSV` are supported only with `EXTERNAL_LINKS`<br />  disposition. `JSON_ARRAY` is supported in `INLINE` and `EXTERNAL_LINKS` disposition.<br /><br />  When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values,<br />  where each value is either the *string representation* of a value, or `null`. For example, the<br />  output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would<br />  look like this:<br /><br />  ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ```<br /><br />  When specifying `format=JSON_ARRAY` and `disposition=EXTERNAL_LINKS`, each chunk in the result<br />  contains compact JSON with no indentation or extra whitespace.<br /><br />  When specifying `format=ARROW_STREAM` and `disposition=EXTERNAL_LINKS`, each chunk in the result<br />  will be formatted as Apache Arrow Stream. See the [Apache Arrow streaming format].<br /><br />  When specifying `format=CSV` and `disposition=EXTERNAL_LINKS`, each chunk in the result will be a<br />  CSV according to [RFC 4180] standard. All the columns values will have *string representation*<br />  similar to the `JSON_ARRAY` format, and `null` values will be encoded as “null”. Only the first<br />  chunk in the result would contain a header row with column names. For example, the output of `SELECT<br />  concat('id-', id) AS strCol, id AS intCol, null as nullCol FROM range(3)` would look like this:<br /><br />  ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ```<br /><br />  [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format<br />  [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180<br />:param on_wait_timeout: :class:`ExecuteStatementRequestOnWaitTimeout` (optional)<br />  When `wait_timeout > 0s`, the call will block up to the specified time. If the statement execution<br />  doesn't finish within this time, `on_wait_timeout` determines whether the execution should continue<br />  or be canceled. When set to `CONTINUE`, the statement execution continues asynchronously and the<br />  call returns a statement ID which can be used for polling with<br />  :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is canceled<br />  and the call returns with a `CANCELED` state.<br />:param parameters: List[:class:`StatementParameterListItem`] (optional)<br />  A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists<br />  of a name, a value, and optionally a type. To represent a NULL value, the `value` field may be<br />  omitted or set to `null` explicitly. If the `type` field is omitted, the value is interpreted as a<br />  string.<br /><br />  If the type is given, parameters will be checked for type correctness according to the given type. A<br />  value is correct if the provided string can be converted to the requested type using the `cast`<br />  function. The exact semantics are described in the section [`cast` function] of the SQL language<br />  reference.<br /><br />  For example, the following statement contains two parameters, `my_name` and `my_date`:<br /><br />  ``` SELECT * FROM my_table WHERE name = :my_name AND date = :my_date ```<br /><br />  The parameters can be passed in the request body as follows:<br /><br />  ` &#123; ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",<br />  "parameters": [ &#123; "name": "my_name", "value": "the name" &#125;, &#123; "name": "my_date", "value":<br />  "2020-01-01", "type": "DATE" &#125; ] &#125; `<br /><br />  Currently, positional parameters denoted by a `?` marker are not supported by the Databricks SQL<br />  Statement Execution API.<br /><br />  Also see the section [Parameter markers] of the SQL language reference.<br /><br />  [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html<br />  [`cast` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html<br />:param query_tags: List[:class:`QueryTag`] (optional)<br />  An array of query tags to annotate a SQL statement. A query tag consists of a non-empty key and,<br />  optionally, a value. To represent a NULL value, either omit the `value` field or manually set it to<br />  `null` or white space. Refer to the SQL language reference for the format specification of query<br />  tags. There's no significance to the order of tags. Only one value per key will be recorded. A<br />  sequence in excess of 20 query tags will be coerced to 20. Example:<br /><br />  &#123; ..., "query_tags": [ &#123; "key": "team", "value": "eng" &#125;, &#123; "key": "some key only tag" &#125; ] &#125;<br />:param row_limit: int (optional)<br />  Applies the given row limit to the statement's result set, but unlike the `LIMIT` clause in SQL, it<br />  also sets the `truncated` field in the response to indicate whether the result was trimmed due to<br />  the limit or not.<br />:param schema: str (optional)<br />  Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL.<br /><br />  [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html<br />:param wait_timeout: str (optional)<br />  The time in seconds the call will wait for the statement's result set as `Ns`, where `N` can be set<br />  to 0 or to a value between 5 and 50.<br /><br />  When set to `0s`, the statement will execute in asynchronous mode and the call will not wait for the<br />  execution to finish. In this case, the call returns directly with `PENDING` state and a statement ID<br />  which can be used for polling with :method:statementexecution/getStatement.<br /><br />  When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait<br />  for the statement execution to finish. If the execution finishes within this time, the call returns<br />  immediately with a manifest and result data (or a `FAILED` state in case of an execution error). If<br />  the statement takes longer to execute, `on_wait_timeout` determines what should happen after the<br />  timeout is reached.<br /><br />:returns: :class:`StatementResponse`</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-statement_id">
    <td><CopyableCode code="statement_id" /></td>
    <td><code>string</code></td>
    <td>The statement ID is returned upon successfully submitting a SQL statement, and is a required reference for all subsequent calls.</td>
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

After the statement execution has `SUCCEEDED`, this request can be used to fetch any chunk by index.<br />Whereas the first chunk with `chunk_index=0` is typically fetched with<br />:method:statementexecution/executeStatement or :method:statementexecution/getStatement, this request<br />can be used to fetch subsequent chunks. The response structure is identical to the nested `result`<br />element described in the :method:statementexecution/getStatement request, and similarly includes the<br />`next_chunk_index` and `next_chunk_internal_link` fields for simple iteration through the result set.<br />Depending on `disposition`, the response returns chunks of data either inline, or as links.<br /><br />:param statement_id: str<br />  The statement ID is returned upon successfully submitting a SQL statement, and is a required<br />  reference for all subsequent calls.<br />:param chunk_index: int<br /><br />:returns: :class:`ResultData`

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
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="get">

This request can be used to poll for the statement's status. StatementResponse contains `statement_id`<br />and `status`; other fields might be absent or present depending on context. When the `status.state`<br />field is `SUCCEEDED` it will also return the result manifest and the first chunk of the result data.<br />When the statement is in the terminal states `CANCELED`, `CLOSED` or `FAILED`, it returns HTTP 200<br />with the state set. After at least 12 hours in terminal state, the statement is removed from the<br />warehouse and further calls will receive an HTTP 404 response.<br /><br />**NOTE** This call currently might take up to 5 seconds to get the latest status and result.<br /><br />:param statement_id: str<br />  The statement ID is returned upon successfully submitting a SQL statement, and is a required<br />  reference for all subsequent calls.<br /><br />:returns: :class:`StatementResponse`

```sql
SELECT
statement_id,
manifest,
result,
status
FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '{{ statement_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Requests that an executing statement be canceled. Callers must poll for status to see the terminal<br />state. Cancel response is empty; receiving response indicates successful receipt.<br /><br />:param statement_id: str<br />  The statement ID is returned upon successfully submitting a SQL statement, and is a required<br />  reference for all subsequent calls.

```sql
INSERT INTO databricks_workspace.sql.statement_execution (
statement_id,
deployment_name
)
SELECT 
'{{ statement_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="execute">

Execute a SQL statement and optionally await its results for a specified time.<br /><br />**Use case: small result sets with INLINE + JSON_ARRAY**<br /><br />For flows that generate small and predictable result sets (&lt;= 25 MiB), `INLINE` responses of<br />`JSON_ARRAY` result data are typically the simplest way to execute and fetch result data.<br /><br />**Use case: large result sets with EXTERNAL_LINKS**<br /><br />Using `EXTERNAL_LINKS` to fetch result data allows you to fetch large result sets efficiently. The<br />main differences from using `INLINE` disposition are that the result data is accessed with URLs, and<br />that there are 3 supported formats: `JSON_ARRAY`, `ARROW_STREAM` and `CSV` compared to only<br />`JSON_ARRAY` with `INLINE`.<br /><br />** URLs**<br /><br />External links point to data stored within your workspace's internal storage, in the form of a URL.<br />The URLs are valid for only a short period, &lt;= 15 minutes. Alongside each `external_link` is an<br />expiration field indicating the time at which the URL is no longer valid. In `EXTERNAL_LINKS` mode,<br />chunks can be resolved and fetched multiple times and in parallel.<br /><br />----<br /><br />### **Warning: Databricks strongly recommends that you protect the URLs that are returned by the<br />`EXTERNAL_LINKS` disposition.**<br /><br />When you use the `EXTERNAL_LINKS` disposition, a short-lived, URL is generated, which can be used to<br />download the results directly from . As a short-lived is embedded in this URL, you should protect the<br />URL.<br /><br />Because URLs are already generated with embedded temporary s, you must not set an `Authorization`<br />header in the download requests.<br /><br />The `EXTERNAL_LINKS` disposition can be disabled upon request by creating a support case.<br /><br />See also [Security best practices].<br /><br />----<br /><br />StatementResponse contains `statement_id` and `status`; other fields might be absent or present<br />depending on context. If the SQL warehouse fails to execute the provided statement, a 200 response is<br />returned with `status.state` set to `FAILED` (in contrast to a failure when accepting the request,<br />which results in a non-200 response). Details of the error can be found at `status.error` in case of<br />execution failures.<br /><br />[Security best practices]: https://docs.databricks.com/sql/admin/sql-execution-tutorial.html#security-best-practices<br /><br />:param statement: str<br />  The SQL statement to execute. The statement can optionally be parameterized, see `parameters`. The<br />  maximum query text size is 16 MiB.<br />:param warehouse_id: str<br />  Warehouse upon which to execute a statement. See also [What are SQL warehouses?]<br /><br />  [What are SQL warehouses?]: https://docs.databricks.com/sql/admin/warehouse-type.html<br />:param byte_limit: int (optional)<br />  Applies the given byte limit to the statement's result size. Byte counts are based on internal data<br />  representations and might not match the final size in the requested `format`. If the result was<br />  truncated due to the byte limit, then `truncated` in the response is set to `true`. When using<br />  `EXTERNAL_LINKS` disposition, a default `byte_limit` of 100 GiB is applied if `byte_limit` is not<br />  explicitly set.<br />:param catalog: str (optional)<br />  Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL.<br /><br />  [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html<br />:param disposition: :class:`Disposition` (optional)<br />  The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.<br /><br />  Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`<br />  format, in a series of chunks. If a given statement produces a result set with a size larger than 25<br />  MiB, that statement execution is aborted, and no result set will be available.<br /><br />  **NOTE** Byte limits are computed based upon internal representations of the result set data, and<br />  might not match the sizes visible in JSON responses.<br /><br />  Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links:<br />  URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition<br />  allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The<br />  resulting links have two important properties:<br /><br />  1. They point to resources _external_ to the Databricks compute; therefore any associated<br />  authentication information (typically a personal access token, OAuth token, or similar) _must be<br />  removed_ when fetching from these links.<br /><br />  2. These are URLs with a specific expiration, indicated in the response. The behavior when<br />  attempting to use an expired link is cloud specific.<br />:param format: :class:`Format` (optional)<br />  Statement execution supports three result formats: `JSON_ARRAY` (default), `ARROW_STREAM`, and<br />  `CSV`.<br /><br />  Important: The formats `ARROW_STREAM` and `CSV` are supported only with `EXTERNAL_LINKS`<br />  disposition. `JSON_ARRAY` is supported in `INLINE` and `EXTERNAL_LINKS` disposition.<br /><br />  When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values,<br />  where each value is either the *string representation* of a value, or `null`. For example, the<br />  output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would<br />  look like this:<br /><br />  ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ```<br /><br />  When specifying `format=JSON_ARRAY` and `disposition=EXTERNAL_LINKS`, each chunk in the result<br />  contains compact JSON with no indentation or extra whitespace.<br /><br />  When specifying `format=ARROW_STREAM` and `disposition=EXTERNAL_LINKS`, each chunk in the result<br />  will be formatted as Apache Arrow Stream. See the [Apache Arrow streaming format].<br /><br />  When specifying `format=CSV` and `disposition=EXTERNAL_LINKS`, each chunk in the result will be a<br />  CSV according to [RFC 4180] standard. All the columns values will have *string representation*<br />  similar to the `JSON_ARRAY` format, and `null` values will be encoded as “null”. Only the first<br />  chunk in the result would contain a header row with column names. For example, the output of `SELECT<br />  concat('id-', id) AS strCol, id AS intCol, null as nullCol FROM range(3)` would look like this:<br /><br />  ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ```<br /><br />  [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format<br />  [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180<br />:param on_wait_timeout: :class:`ExecuteStatementRequestOnWaitTimeout` (optional)<br />  When `wait_timeout > 0s`, the call will block up to the specified time. If the statement execution<br />  doesn't finish within this time, `on_wait_timeout` determines whether the execution should continue<br />  or be canceled. When set to `CONTINUE`, the statement execution continues asynchronously and the<br />  call returns a statement ID which can be used for polling with<br />  :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is canceled<br />  and the call returns with a `CANCELED` state.<br />:param parameters: List[:class:`StatementParameterListItem`] (optional)<br />  A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists<br />  of a name, a value, and optionally a type. To represent a NULL value, the `value` field may be<br />  omitted or set to `null` explicitly. If the `type` field is omitted, the value is interpreted as a<br />  string.<br /><br />  If the type is given, parameters will be checked for type correctness according to the given type. A<br />  value is correct if the provided string can be converted to the requested type using the `cast`<br />  function. The exact semantics are described in the section [`cast` function] of the SQL language<br />  reference.<br /><br />  For example, the following statement contains two parameters, `my_name` and `my_date`:<br /><br />  ``` SELECT * FROM my_table WHERE name = :my_name AND date = :my_date ```<br /><br />  The parameters can be passed in the request body as follows:<br /><br />  ` &#123; ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date",<br />  "parameters": [ &#123; "name": "my_name", "value": "the name" &#125;, &#123; "name": "my_date", "value":<br />  "2020-01-01", "type": "DATE" &#125; ] &#125; `<br /><br />  Currently, positional parameters denoted by a `?` marker are not supported by the Databricks SQL<br />  Statement Execution API.<br /><br />  Also see the section [Parameter markers] of the SQL language reference.<br /><br />  [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html<br />  [`cast` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html<br />:param query_tags: List[:class:`QueryTag`] (optional)<br />  An array of query tags to annotate a SQL statement. A query tag consists of a non-empty key and,<br />  optionally, a value. To represent a NULL value, either omit the `value` field or manually set it to<br />  `null` or white space. Refer to the SQL language reference for the format specification of query<br />  tags. There's no significance to the order of tags. Only one value per key will be recorded. A<br />  sequence in excess of 20 query tags will be coerced to 20. Example:<br /><br />  &#123; ..., "query_tags": [ &#123; "key": "team", "value": "eng" &#125;, &#123; "key": "some key only tag" &#125; ] &#125;<br />:param row_limit: int (optional)<br />  Applies the given row limit to the statement's result set, but unlike the `LIMIT` clause in SQL, it<br />  also sets the `truncated` field in the response to indicate whether the result was trimmed due to<br />  the limit or not.<br />:param schema: str (optional)<br />  Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL.<br /><br />  [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html<br />:param wait_timeout: str (optional)<br />  The time in seconds the call will wait for the statement's result set as `Ns`, where `N` can be set<br />  to 0 or to a value between 5 and 50.<br /><br />  When set to `0s`, the statement will execute in asynchronous mode and the call will not wait for the<br />  execution to finish. In this case, the call returns directly with `PENDING` state and a statement ID<br />  which can be used for polling with :method:statementexecution/getStatement.<br /><br />  When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait<br />  for the statement execution to finish. If the execution finishes within this time, the call returns<br />  immediately with a manifest and result data (or a `FAILED` state in case of an execution error). If<br />  the statement takes longer to execute, `on_wait_timeout` determines what should happen after the<br />  timeout is reached.<br /><br />:returns: :class:`StatementResponse`

```sql
INSERT INTO databricks_workspace.sql.statement_execution (
data__statement,
data__warehouse_id,
data__byte_limit,
data__catalog,
data__disposition,
data__format,
data__on_wait_timeout,
data__parameters,
data__query_tags,
data__row_limit,
data__schema,
data__wait_timeout,
deployment_name
)
SELECT 
'{{ statement }}' /* required */,
'{{ warehouse_id }}' /* required */,
'{{ byte_limit }}',
'{{ catalog }}',
'{{ disposition }}',
'{{ format }}',
'{{ on_wait_timeout }}',
'{{ parameters }}',
'{{ query_tags }}',
'{{ row_limit }}',
'{{ schema }}',
'{{ wait_timeout }}',
'{{ deployment_name }}'
RETURNING
statement_id,
manifest,
result,
status
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: statement_execution
  props:
    - name: statement_id
      value: string
      description: Required parameter for the statement_execution resource.
    - name: deployment_name
      value: string
      description: Required parameter for the statement_execution resource.
    - name: statement
      value: string
      description: |
        The SQL statement to execute. The statement can optionally be parameterized, see `parameters`. The maximum query text size is 16 MiB.
    - name: warehouse_id
      value: string
      description: |
        Warehouse upon which to execute a statement. See also [What are SQL warehouses?] [What are SQL warehouses?]: https://docs.databricks.com/sql/admin/warehouse-type.html
    - name: byte_limit
      value: string
      description: |
        Applies the given byte limit to the statement's result size. Byte counts are based on internal data representations and might not match the final size in the requested `format`. If the result was truncated due to the byte limit, then `truncated` in the response is set to `true`. When using `EXTERNAL_LINKS` disposition, a default `byte_limit` of 100 GiB is applied if `byte_limit` is not explicitly set.
    - name: catalog
      value: string
      description: |
        Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL. [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html
    - name: disposition
      value: string
      description: |
        The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`. Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY` format, in a series of chunks. If a given statement produces a result set with a size larger than 25 MiB, that statement execution is aborted, and no result set will be available. **NOTE** Byte limits are computed based upon internal representations of the result set data, and might not match the sizes visible in JSON responses. Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links: URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The resulting links have two important properties: 1. They point to resources _external_ to the Databricks compute; therefore any associated authentication information (typically a personal access token, OAuth token, or similar) _must be removed_ when fetching from these links. 2. These are URLs with a specific expiration, indicated in the response. The behavior when attempting to use an expired link is cloud specific.
    - name: format
      value: string
      description: |
        Statement execution supports three result formats: `JSON_ARRAY` (default), `ARROW_STREAM`, and `CSV`. Important: The formats `ARROW_STREAM` and `CSV` are supported only with `EXTERNAL_LINKS` disposition. `JSON_ARRAY` is supported in `INLINE` and `EXTERNAL_LINKS` disposition. When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values, where each value is either the *string representation* of a value, or `null`. For example, the output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would look like this: ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ``` When specifying `format=JSON_ARRAY` and `disposition=EXTERNAL_LINKS`, each chunk in the result contains compact JSON with no indentation or extra whitespace. When specifying `format=ARROW_STREAM` and `disposition=EXTERNAL_LINKS`, each chunk in the result will be formatted as Apache Arrow Stream. See the [Apache Arrow streaming format]. When specifying `format=CSV` and `disposition=EXTERNAL_LINKS`, each chunk in the result will be a CSV according to [RFC 4180] standard. All the columns values will have *string representation* similar to the `JSON_ARRAY` format, and `null` values will be encoded as “null”. Only the first chunk in the result would contain a header row with column names. For example, the output of `SELECT concat('id-', id) AS strCol, id AS intCol, null as nullCol FROM range(3)` would look like this: ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ``` [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180
    - name: on_wait_timeout
      value: string
      description: |
        When `wait_timeout > 0s`, the call will block up to the specified time. If the statement execution doesn't finish within this time, `on_wait_timeout` determines whether the execution should continue or be canceled. When set to `CONTINUE`, the statement execution continues asynchronously and the call returns a statement ID which can be used for polling with :method:statementexecution/getStatement. When set to `CANCEL`, the statement execution is canceled and the call returns with a `CANCELED` state.
    - name: parameters
      value: string
      description: |
        A list of parameters to pass into a SQL statement containing parameter markers. A parameter consists of a name, a value, and optionally a type. To represent a NULL value, the `value` field may be omitted or set to `null` explicitly. If the `type` field is omitted, the value is interpreted as a string. If the type is given, parameters will be checked for type correctness according to the given type. A value is correct if the provided string can be converted to the requested type using the `cast` function. The exact semantics are described in the section [`cast` function] of the SQL language reference. For example, the following statement contains two parameters, `my_name` and `my_date`: ``` SELECT * FROM my_table WHERE name = :my_name AND date = :my_date ``` The parameters can be passed in the request body as follows: ` { ..., "statement": "SELECT * FROM my_table WHERE name = :my_name AND date = :my_date", "parameters": [ { "name": "my_name", "value": "the name" }, { "name": "my_date", "value": "2020-01-01", "type": "DATE" } ] } ` Currently, positional parameters denoted by a `?` marker are not supported by the Databricks SQL Statement Execution API. Also see the section [Parameter markers] of the SQL language reference. [Parameter markers]: https://docs.databricks.com/sql/language-manual/sql-ref-parameter-marker.html [`cast` function]: https://docs.databricks.com/sql/language-manual/functions/cast.html
    - name: query_tags
      value: string
      description: |
        An array of query tags to annotate a SQL statement. A query tag consists of a non-empty key and, optionally, a value. To represent a NULL value, either omit the `value` field or manually set it to `null` or white space. Refer to the SQL language reference for the format specification of query tags. There's no significance to the order of tags. Only one value per key will be recorded. A sequence in excess of 20 query tags will be coerced to 20. Example: { ..., "query_tags": [ { "key": "team", "value": "eng" }, { "key": "some key only tag" } ] }
    - name: row_limit
      value: string
      description: |
        Applies the given row limit to the statement's result set, but unlike the `LIMIT` clause in SQL, it also sets the `truncated` field in the response to indicate whether the result was trimmed due to the limit or not.
    - name: schema
      value: string
      description: |
        Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL. [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html
    - name: wait_timeout
      value: string
      description: |
        The time in seconds the call will wait for the statement's result set as `Ns`, where `N` can be set to 0 or to a value between 5 and 50. When set to `0s`, the statement will execute in asynchronous mode and the call will not wait for the execution to finish. In this case, the call returns directly with `PENDING` state and a statement ID which can be used for polling with :method:statementexecution/getStatement. When set between 5 and 50 seconds, the call will behave synchronously up to this timeout and wait for the statement execution to finish. If the execution finishes within this time, the call returns immediately with a manifest and result data (or a `FAILED` state in case of an execution error). If the statement takes longer to execute, `on_wait_timeout` determines what should happen after the timeout is reached.
```
</TabItem>
</Tabs>

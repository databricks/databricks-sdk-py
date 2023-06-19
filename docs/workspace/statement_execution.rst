Statement Execution
===================
.. py:class:: StatementExecutionAPI

    The SQL Statement Execution API manages the execution of arbitrary SQL statements and the fetching of
    result data.
    
    **Release status**
    
    This feature is in [Public Preview].
    
    **Getting started**
    
    We suggest beginning with the [SQL Statement Execution API tutorial].
    
    **Overview of statement execution and result fetching**
    
    Statement execution begins by issuing a :method:statementexecution/executeStatement request with a valid
    SQL statement and warehouse ID, along with optional parameters such as the data catalog and output format.
    
    When submitting the statement, the call can behave synchronously or asynchronously, based on the
    `wait_timeout` setting. When set between 5-50 seconds (default: 10) the call behaves synchronously and
    waits for results up to the specified timeout; when set to `0s`, the call is asynchronous and responds
    immediately with a statement ID that can be used to poll for status or fetch the results in a separate
    call.
    
    **Call mode: synchronous**
    
    In synchronous mode, when statement execution completes within the `wait timeout`, the result data is
    returned directly in the response. This response will contain `statement_id`, `status`, `manifest`, and
    `result` fields. The `status` field confirms success whereas the `manifest` field contains the result data
    column schema and metadata about the result set. The `result` field contains the first chunk of result
    data according to the specified `disposition`, and links to fetch any remaining chunks.
    
    If the execution does not complete before `wait_timeout`, the setting `on_wait_timeout` determines how the
    system responds.
    
    By default, `on_wait_timeout=CONTINUE`, and after reaching `wait_timeout`, a response is returned and
    statement execution continues asynchronously. The response will contain only `statement_id` and `status`
    fields, and the caller must now follow the flow described for asynchronous call mode to poll and fetch the
    result.
    
    Alternatively, `on_wait_timeout` can also be set to `CANCEL`; in this case if the timeout is reached
    before execution completes, the underlying statement execution is canceled, and a `CANCELED` status is
    returned in the response.
    
    **Call mode: asynchronous**
    
    In asynchronous mode, or after a timed-out synchronous request continues, a `statement_id` and `status`
    will be returned. In this case polling :method:statementexecution/getStatement calls are required to fetch
    the result and metadata.
    
    Next, a caller must poll until execution completes (`SUCCEEDED`, `FAILED`, etc.) by issuing
    :method:statementexecution/getStatement requests for the given `statement_id`.
    
    When execution has succeeded, the response will contain `status`, `manifest`, and `result` fields. These
    fields and the structure are identical to those in the response to a successful synchronous submission.
    The `result` field will contain the first chunk of result data, either `INLINE` or as `EXTERNAL_LINKS`
    depending on `disposition`. Additional chunks of result data can be fetched by checking for the presence
    of the `next_chunk_internal_link` field, and iteratively `GET` those paths until that field is unset: `GET
    https://$DATABRICKS_HOST/{next_chunk_internal_link}`.
    
    **Fetching result data: format and disposition**
    
    To specify the result data format, set the `format` field to `JSON_ARRAY` (JSON), `ARROW_STREAM` ([Apache
    Arrow Columnar]), or `CSV`.
    
    You can also configure how to fetch the result data in two different modes by setting the `disposition`
    field to `INLINE` or `EXTERNAL_LINKS`.
    
    The `INLINE` disposition can only be used with the `JSON_ARRAY` format and allows results up to 16 MiB.
    When a statement executed with `INLINE` disposition exceeds this limit, the execution is aborted, and no
    result can be fetched.
    
    The `EXTERNAL_LINKS` disposition allows fetching large result sets in `JSON_ARRAY`, `ARROW_STREAM` and
    `CSV` formats, and with higher throughput.
    
    The API uses defaults of `format=JSON_ARRAY` and `disposition=INLINE`. Databricks recommends that you
    explicit setting the format and the disposition for all production use cases.
    
    **Statement response: statement_id, status, manifest, and result**
    
    The base call :method:statementexecution/getStatement returns a single response combining `statement_id`,
    `status`, a result `manifest`, and a `result` data chunk or link, depending on the `disposition`. The
    `manifest` contains the result schema definition and the result summary metadata. When using
    `disposition=EXTERNAL_LINKS`, it also contains a full listing of all chunks and their summary metadata.
    
    **Use case: small result sets with INLINE + JSON_ARRAY**
    
    For flows that generate small and predictable result sets (<= 16 MiB), `INLINE` downloads of `JSON_ARRAY`
    result data are typically the simplest way to execute and fetch result data.
    
    When the result set with `disposition=INLINE` is larger, the result can be transferred in chunks. After
    receiving the initial chunk with :method:statementexecution/executeStatement or
    :method:statementexecution/getStatement subsequent calls are required to iteratively fetch each chunk.
    Each result response contains a link to the next chunk, when there are additional chunks to fetch; it can
    be found in the field `.next_chunk_internal_link`. This link is an absolute `path` to be joined with your
    `$DATABRICKS_HOST`, and of the form `/api/2.0/sql/statements/{statement_id}/result/chunks/{chunk_index}`.
    The next chunk can be fetched by issuing a :method:statementexecution/getStatementResultChunkN request.
    
    When using this mode, each chunk may be fetched once, and in order. A chunk without a field
    `next_chunk_internal_link` indicates the last chunk was reached and all chunks have been fetched from the
    result set.
    
    **Use case: large result sets with EXTERNAL_LINKS + ARROW_STREAM**
    
    Using `EXTERNAL_LINKS` to fetch result data in Arrow format allows you to fetch large result sets
    efficiently. The primary difference from using `INLINE` disposition is that fetched result chunks contain
    resolved `external_links` URLs, which can be fetched with standard HTTP.
    
    **Presigned URLs**
    
    External links point to data stored within your workspace's internal DBFS, in the form of a presigned URL.
    The URLs are valid for only a short period, <= 15 minutes. Alongside each `external_link` is an expiration
    field indicating the time at which the URL is no longer valid. In `EXTERNAL_LINKS` mode, chunks can be
    resolved and fetched multiple times and in parallel.
    
    ----
    
    ### **Warning: We recommend you protect the URLs in the EXTERNAL_LINKS.**
    
    When using the EXTERNAL_LINKS disposition, a short-lived pre-signed URL is generated, which the client can
    use to download the result chunk directly from cloud storage. As the short-lived credential is embedded in
    a pre-signed URL, this URL should be protected.
    
    Since pre-signed URLs are generated with embedded temporary credentials, you need to remove the
    authorization header from the fetch requests.
    
    ----
    
    Similar to `INLINE` mode, callers can iterate through the result set, by using the
    `next_chunk_internal_link` field. Each internal link response will contain an external link to the raw
    chunk data, and additionally contain the `next_chunk_internal_link` if there are more chunks.
    
    Unlike `INLINE` mode, when using `EXTERNAL_LINKS`, chunks may be fetched out of order, and in parallel to
    achieve higher throughput.
    
    **Limits and limitations**
    
    Note: All byte limits are calculated based on internal storage metrics and will not match byte counts of
    actual payloads.
    
    - Statements with `disposition=INLINE` are limited to 16 MiB and will abort when this limit is exceeded. -
    Statements with `disposition=EXTERNAL_LINKS` are limited to 100 GiB. - The maximum query text size is 16
    MiB. - Cancelation may silently fail. A successful response from a cancel request indicates that the
    cancel request was successfully received and sent to the processing engine. However, for example, an
    outstanding statement may complete execution during signal delivery, with the cancel signal arriving too
    late to be meaningful. Polling for status until a terminal state is reached is a reliable way to determine
    the final state. - Wait timeouts are approximate, occur server-side, and cannot account for caller delays,
    network latency from caller to service, and similarly. - After a statement has been submitted and a
    statement_id is returned, that statement's status and result will automatically close after either of 2
    conditions: - The last result chunk is fetched (or resolved to an external link). - One hour passes with
    no calls to get the status or fetch the result. Best practice: in asynchronous clients, poll for status
    regularly (and with backoff) to keep the statement open and alive. - After fetching the last result chunk
    (including chunk_index=0) the statement is automatically closed.
    
    [Apache Arrow Columnar]: https://arrow.apache.org/overview/
    [Public Preview]: https://docs.databricks.com/release-notes/release-types.html
    [SQL Statement Execution API tutorial]: https://docs.databricks.com/sql/api/sql-execution-tutorial.html

    .. py:method:: cancel_execution(statement_id)

        Cancel statement execution.
        
        Requests that an executing statement be canceled. Callers must poll for status to see the terminal
        state.
        
        :param statement_id: str
        
        
        

    .. py:method:: execute_statement( [, byte_limit, catalog, disposition, format, on_wait_timeout, schema, statement, wait_timeout, warehouse_id])

        Execute a SQL statement.
        
        Execute a SQL statement, and if flagged as such, await its result for a specified time.
        
        :param byte_limit: int (optional)
          Applies the given byte limit to the statement's result size. Byte counts are based on internal
          representations and may not match measurable sizes in the requested `format`.
        :param catalog: str (optional)
          Sets default catalog for statement execution, similar to [`USE CATALOG`] in SQL.
          
          [`USE CATALOG`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-catalog.html
        :param disposition: :class:`Disposition` (optional)
          The fetch disposition provides two modes of fetching results: `INLINE` and `EXTERNAL_LINKS`.
          
          Statements executed with `INLINE` disposition will return result data inline, in `JSON_ARRAY`
          format, in a series of chunks. If a given statement produces a result set with a size larger than 16
          MiB, that statement execution is aborted, and no result set will be available.
          
          **NOTE** Byte limits are computed based upon internal representations of the result set data, and
          may not match the sizes visible in JSON responses.
          
          Statements executed with `EXTERNAL_LINKS` disposition will return result data as external links:
          URLs that point to cloud storage internal to the workspace. Using `EXTERNAL_LINKS` disposition
          allows statements to generate arbitrarily sized result sets for fetching up to 100 GiB. The
          resulting links have two important properties:
          
          1. They point to resources _external_ to the Databricks compute; therefore any associated
          authentication information (typically a personal access token, OAuth token, or similar) _must be
          removed_ when fetching from these links.
          
          2. These are presigned URLs with a specific expiration, indicated in the response. The behavior when
          attempting to use an expired link is cloud specific.
        :param format: :class:`Format` (optional)
          Statement execution supports three result formats: `JSON_ARRAY` (default), `ARROW_STREAM`, and
          `CSV`.
          
          When specifying `format=JSON_ARRAY`, result data will be formatted as an array of arrays of values,
          where each value is either the *string representation* of a value, or `null`. For example, the
          output of `SELECT concat('id-', id) AS strCol, id AS intCol, null AS nullCol FROM range(3)` would
          look like this:
          
          ``` [ [ "id-1", "1", null ], [ "id-2", "2", null ], [ "id-3", "3", null ], ] ```
          
          `JSON_ARRAY` is supported with `INLINE` and `EXTERNAL_LINKS` dispositions.
          
          `INLINE` `JSON_ARRAY` data can be found at the path `StatementResponse.result.data_array`.
          
          For `EXTERNAL_LINKS` `JSON_ARRAY` results, each URL points to a file in cloud storage that contains
          compact JSON with no indentation or extra whitespace.
          
          When specifying `format=ARROW_STREAM`, each chunk in the result will be formatted as Apache Arrow
          Stream. See the [Apache Arrow streaming format].
          
          IMPORTANT: The format `ARROW_STREAM` is supported only with `EXTERNAL_LINKS` disposition.
          
          When specifying `format=CSV`, each chunk in the result will be a CSV according to [RFC 4180]
          standard. All the columns values will have *string representation* similar to the `JSON_ARRAY`
          format, and `null` values will be encoded as “null”. Only the first chunk in the result would
          contain a header row with column names. For example, the output of `SELECT concat('id-', id) AS
          strCol, id AS intCol, null as nullCol FROM range(3)` would look like this:
          
          ``` strCol,intCol,nullCol id-1,1,null id-2,2,null id-3,3,null ```
          
          IMPORTANT: The format `CSV` is supported only with `EXTERNAL_LINKS` disposition.
          
          [Apache Arrow streaming format]: https://arrow.apache.org/docs/format/Columnar.html#ipc-streaming-format
          [RFC 4180]: https://www.rfc-editor.org/rfc/rfc4180
        :param on_wait_timeout: :class:`TimeoutAction` (optional)
          When in synchronous mode with `wait_timeout > 0s` it determines the action taken when the timeout is
          reached:
          
          `CONTINUE` → the statement execution continues asynchronously and the call returns a statement ID
          immediately.
          
          `CANCEL` → the statement execution is canceled and the call returns immediately with a `CANCELED`
          state.
        :param schema: str (optional)
          Sets default schema for statement execution, similar to [`USE SCHEMA`] in SQL.
          
          [`USE SCHEMA`]: https://docs.databricks.com/sql/language-manual/sql-ref-syntax-ddl-use-schema.html
        :param statement: str (optional)
          SQL statement to execute
        :param wait_timeout: str (optional)
          The time in seconds the API service will wait for the statement's result set as `Ns`, where `N` can
          be set to 0 or to a value between 5 and 50. When set to '0s' the statement will execute in
          asynchronous mode.
        :param warehouse_id: str (optional)
          Warehouse upon which to execute a statement. See also [What are SQL
          warehouses?](/sql/admin/warehouse-type.html)
        
        :returns: :class:`ExecuteStatementResponse`
        

    .. py:method:: get_statement(statement_id)

        Get status, manifest, and result first chunk.
        
        This request can be used to poll for the statement's status. When the `status.state` field is
        `SUCCEEDED` it will also return the result manifest and the first chunk of the result data. When the
        statement is in the terminal states `CANCELED`, `CLOSED` or `FAILED`, it returns HTTP 200 with the
        state set. After at least 12 hours in terminal state, the statement is removed from the warehouse and
        further calls will receive an HTTP 404 response.
        
        **NOTE** This call currently may take up to 5 seconds to get the latest status and result.
        
        :param statement_id: str
        
        :returns: :class:`GetStatementResponse`
        

    .. py:method:: get_statement_result_chunk_n(statement_id, chunk_index)

        Get result chunk by index.
        
        After the statement execution has `SUCCEEDED`, the result data can be fetched by chunks. Whereas the
        first chuck with `chunk_index=0` is typically fetched through a `get status` request, subsequent
        chunks can be fetched using a `get result` request. The response structure is identical to the nested
        `result` element described in the `get status` request, and similarly includes the `next_chunk_index`
        and `next_chunk_internal_link` fields for simple iteration through the result set.
        
        :param statement_id: str
        :param chunk_index: int
        
        :returns: :class:`ResultData`
        